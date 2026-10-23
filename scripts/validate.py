"""Validate package structure, references, dependency graph and optional lock."""
import argparse
import json
import re
import sys
from urllib.parse import unquote
from library import ROOT, packages, files, lock, render_catalog

def validate(check_lock=False):
    errors=[]
    try:
        pkgs=packages()
    except (ValueError, OSError) as exc:
        return ['Cannot read skill metadata: '+str(exc)]
    discovered={p.parent.name for p in ROOT.glob('*/SKILL.md')}
    if discovered!=set(pkgs): errors.append('SKILL.md and skill.json directory sets differ')
    for name, meta in pkgs.items():
        folder=ROOT/name
        for filename in ['SKILL.md','README.md','CHANGELOG.md','ORIGIN.md']:
            if not (folder/filename).is_file(): errors.append(f'{name}: missing {filename}')
        if meta.get('name')!=name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name): errors.append(f'{name}: invalid/mismatched name')
        if not re.fullmatch(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)',meta.get('version','')): errors.append(f'{name}: invalid version')
        if not meta.get('origin',{}).get('evidence'):errors.append(f'{name}: missing origin evidence')
        for dep in meta.get('skill_dependencies',[]):
            if dep not in pkgs: errors.append(f'{name}: missing dependency {dep}')
        skill=(folder/'SKILL.md').read_text() if (folder/'SKILL.md').exists() else ''
        match=re.match(r'\A---\s*\n(.*?)\n---(?:\n|$)',skill,re.S)
        if not match:errors.append(f'{name}: missing frontmatter')
        else:
            front=match.group(1)
            n=re.search(r'^name:\s*[\"\']?([a-z0-9-]+)[\"\']?\s*$',front,re.M)
            if not n or n.group(1)!=name:errors.append(f'{name}: frontmatter name mismatch')
            if not re.search(r'^description:\s*\S',front,re.M):errors.append(f'{name}: missing description')
        changelog=(folder/'CHANGELOG.md').read_text() if (folder/'CHANGELOG.md').exists() else ''
        if f"## {meta.get('version')} " not in changelog:errors.append(f'{name}: version missing from changelog')
        for p in files(name):
            if p.is_symlink():errors.append(f'{p.relative_to(ROOT)}: package must not depend on an external symlink')
            if p.suffix not in {'.md','.py','.sh','.json','.yaml','.yml','.html'}:continue
            content=p.read_text(errors='replace')
            if re.search(r'/Users/[^/\s]+/|/home/[^/\s]+/',content): errors.append(f'{p.relative_to(ROOT)}: personal absolute path')
            if re.search(r'-----BEGIN [A-Z ]*PRIVATE KEY-----|\bghp_[A-Za-z0-9]{20,}|\bgithub_pat_[A-Za-z0-9_]{20,}|\bsk-[A-Za-z0-9_-]{24,}',content):errors.append(f'{p.relative_to(ROOT)}: credential pattern (value not printed)')
            if p.suffix=='.md':
                # Ignore fenced examples; check actual local Markdown links.
                prose=re.sub(r'```.*?```','',content,flags=re.S)
                for target in re.findall(r'\]\(([^\s)]+)\)',prose):
                    if '://' in target or target.startswith(('#','mailto:')):continue
                    target=unquote(target.split('#')[0])
                    if target and not (p.parent/target).exists():errors.append(f'{p.relative_to(ROOT)}: broken link {target}')
    def visit(n, stack):
        if n in stack:errors.append('Dependency cycle: '+' -> '.join(stack+[n]));return
        for dep in pkgs[n].get('skill_dependencies',[]):
            if dep in pkgs:visit(dep,stack+[n])
    for n in pkgs:visit(n,[])
    if check_lock:
        try:
            if json.loads((ROOT/'skills-lock.json').read_text())!=lock():errors.append('Content lock differs; update versions/changelog as needed, then regenerate catalog')
            if (ROOT/'CATALOG.md').read_text()!=render_catalog():errors.append('CATALOG.md is stale')
        except (OSError,ValueError):errors.append('Missing/invalid catalog or content lock')
    return errors

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-lock',action='store_true')
    errors=validate(parser.parse_args().check_lock)
    if errors:
        print('\n'.join(errors),file=sys.stderr)
        raise SystemExit(1)
    print(f'Validated {len(packages())} skill packages (structure and references; no live financial calls)')
