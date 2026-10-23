"""Install selected skills as shared links or workspace copies, preserving backups."""
import argparse
from datetime import datetime
from pathlib import Path
import os
import hashlib
import shutil
import sys
import uuid
from library import ROOT, packages, IGNORED
from validate import validate

def content(folder):
    return {str(p.relative_to(folder)):hashlib.sha256(p.read_bytes()).hexdigest() for p in folder.rglob('*') if p.is_file() and not(set(p.relative_to(folder).parts)&IGNORED) and p.suffix!='.pyc'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('skills',nargs='+',help='Skill folder names; dependencies are included')
    parser.add_argument('--target',type=Path,default=Path.home()/'.openclaw/skills')
    parser.add_argument('--backup-root',type=Path,default=Path.home()/'.openclaw/skill-backups')
    parser.add_argument('--apply',action='store_true')
    parser.add_argument('--mode',choices=['auto','link','copy'],default='auto',help='Auto links shared installs; other targets receive portable copies')
    parser.add_argument('--replace',action='store_true',help='Back up conflicting installs before replacing')
    args=parser.parse_args()
    errors=validate(check_lock=True)
    if errors: raise ValueError('\n'.join(errors))
    pkgs=packages(); order=[]
    def add(name):
        if name not in pkgs:raise ValueError('Unknown skill: '+name)
        for dep in pkgs[name].get('skill_dependencies',[]):add(dep)
        if name not in order:order.append(name)
    for name in args.skills:add(name)
    target=args.target.expanduser().resolve()
    mode=args.mode if args.mode!='auto' else ('link' if target==(Path.home()/'.openclaw/skills').resolve() else 'copy')
    if target==ROOT or ROOT in target.parents:raise ValueError('Install target must be outside the source repository')
    actions=[]
    for name in order:
        dest=target/name; source=ROOT/name
        if mode=='link' and dest.is_symlink() and dest.resolve()==source.resolve():
            print('Already linked:',name);continue
        if mode=='copy' and dest.is_dir() and not dest.is_symlink() and content(dest)==content(source):
            print('Already synchronized:',name);continue
        if os.path.lexists(dest) and not args.replace:raise ValueError(f'{dest} exists; compare it, then use --replace to back up and replace')
        actions.append((dest,source))
        print(('Install' if args.apply else 'Would install'),name,'mode='+mode,'->',source)
    if not args.apply:return 0
    target.mkdir(parents=True,exist_ok=True)
    backup=args.backup_root.expanduser().resolve()/('install-'+datetime.now().strftime('%Y%m%d-%H%M%S')+'-'+uuid.uuid4().hex[:8])
    if backup==target or target in backup.parents:raise ValueError('Backup must be outside the installation discovery directory')
    changed=[]
    try:
        for dest,source in actions:
            previous=None
            if os.path.lexists(dest):
                backup.mkdir(parents=True,exist_ok=True)
                previous=backup/dest.name
                dest.rename(previous)
            changed.append((dest,previous))
            if mode=='link':dest.symlink_to(source,target_is_directory=True)
            else:shutil.copytree(source,dest,ignore=shutil.ignore_patterns(*IGNORED,'*.pyc'))
    except BaseException:
        for dest,previous in reversed(changed):
            if dest.is_symlink() and dest.resolve()==(ROOT/dest.name).resolve():dest.unlink()
            elif mode=='copy' and dest.is_dir() and not dest.is_symlink():shutil.rmtree(dest)
            if previous is not None and os.path.lexists(previous):previous.rename(dest)
        raise
    if backup.exists():print('Previous installs backed up to',backup)
    print('Installed',len(actions),mode+' packages; no skill executed')
    return 0

if __name__=='__main__':
    try:raise SystemExit(main())
    except (OSError,ValueError) as exc:
        print(str(exc),file=sys.stderr);raise SystemExit(1)
