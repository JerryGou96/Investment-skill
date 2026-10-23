"""Regenerate the human catalog and content lock from per-skill metadata."""
import json
from library import ROOT, lock, render_catalog

if __name__ == '__main__':
    (ROOT/'skills-lock.json').write_text(json.dumps(lock(), ensure_ascii=False, indent=2)+'\n')
    (ROOT/'CATALOG.md').write_text(render_catalog())
    print('Updated CATALOG.md and skills-lock.json')
