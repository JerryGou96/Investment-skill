"""Run the locally configured read-only Tiger adapter; never send messages."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=Path(os.environ.get('TRADING_REVIEW_CONFIG', str(Path.home()/'.openclaw/local-config/trading-review.json'))))
    args = parser.parse_args()
    try:
        config = json.loads(args.config.expanduser().read_text())
        directory = Path(config['tiger_api_dir']).expanduser().resolve(strict=True)
        python = directory/'.venv/bin/python3'
        script = directory/'read_only.py'
        if not python.is_file() or not os.access(python, os.X_OK) or not script.is_file():
            raise ValueError('Configured Tiger adapter needs .venv/bin/python3 and read_only.py')
        return subprocess.run([str(python), str(script)], cwd=directory, check=False, timeout=120).returncode
    except (OSError, ValueError, KeyError, subprocess.TimeoutExpired):
        print('Cannot run the configured read-only Tiger adapter. Check local config, venv and read_only.py; no broker operation was requested by this helper beyond running that adapter.', file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
