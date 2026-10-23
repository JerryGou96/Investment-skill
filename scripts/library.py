"""Standard-library helpers for the skill catalog."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {'.git', '__pycache__', '.venv', 'cache', 'log', 'logs', 'output', 'outputs', '.DS_Store'}

def packages():
    return {p.parent.name: json.loads(p.read_text()) for p in sorted(ROOT.glob('*/skill.json'))}

def files(name):
    folder = ROOT/name
    return [p for p in sorted(folder.rglob('*')) if p.is_file() and not (set(p.relative_to(folder).parts) & IGNORED) and p.suffix != '.pyc']

def lock():
    result = {'schema_version': 1, 'skills': {}}
    for name, meta in packages().items():
        hashes = {str(p.relative_to(ROOT/name)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files(name)}
        payload = json.dumps(hashes, sort_keys=True, separators=(',', ':')).encode()
        result['skills'][name] = {'version': meta['version'], 'sha256': hashlib.sha256(payload).hexdigest(), 'files': hashes}
    return result

def render_catalog():
    text = '# 投资技能目录\n\n由 `python3 scripts/catalog.py` 从 skill.json 生成。\n\n| 技能 | 分类 | 用途 | 版本 | 来源类型 |\n|---|---|---|---|---|\n'
    for name, meta in packages().items():
        text += f"| [{name}]({name}/README.md) | {meta['category']} | {meta['summary']} | {meta['version']} | {meta['origin']['kind']} |\n"
    text += '\n## Finance 原始导入（待逐步整理）\n\n'
    text += '完整原仓库位于 [imports/Finance-Skill](imports/Finance-Skill/README.md)，保留来源、许可与历史；不加入默认安装列表。详见 [合并说明](docs/FINANCE-MERGE.md)。\n\n'
    text += '| 原始技能 | 处理方式 |\n|---|---|\n'
    for name in ['comex-delivery-analysis', 'daily-portfolio-review', 'nfp-labor-market-analysis', 'us-weekly-cross-asset-recap']:
        note = '保留新增的原始技能' if name == 'comex-delivery-analysis' else '与根目录维护版并存，供后续比较'
        text += f'| [{name}](imports/Finance-Skill/skills/{name}/SKILL.md) | {note} |\n'
    return text
