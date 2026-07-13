from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

VENV_PYTHON = ROOT / ".venv" / "Scripts" / "python.exe"
if importlib.util.find_spec("PySide6") is None and VENV_PYTHON.exists():
    current = Path(sys.executable).resolve()
    target = VENV_PYTHON.resolve()
    if current != target:
        os.execv(str(target), [str(target), *sys.argv])

from raggg.desktop.main_window import run_desktop_app


if __name__ == "__main__":
    raise SystemExit(run_desktop_app())
