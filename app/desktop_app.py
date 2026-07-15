from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

if getattr(sys, "frozen", False):
    ROOT = Path(sys.executable).resolve().parent
else:
    ROOT = Path(__file__).resolve().parents[1]

os.environ.setdefault("RAGGG_PORTABLE_ROOT", str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

VENV_PYTHON = ROOT / ".venv" / "Scripts" / "python.exe"
if importlib.util.find_spec("PySide6") is None and VENV_PYTHON.exists():
    current = Path(sys.executable).resolve()
    target = VENV_PYTHON.resolve()
    if current != target:
        os.execv(str(target), [str(target), *sys.argv])

from raggg.desktop.main_window import run_desktop_app


def _offer_desktop_shortcut() -> None:
    """第一次启动 EXE 时询问是否创建桌面快捷方式（用 Windows 原生弹窗，不依赖 PySide6）"""
    if not getattr(sys, "frozen", False):
        return

    shortcut_path = Path.home() / "Desktop" / "WavEDA 仿真助手.lnk"
    if shortcut_path.exists():
        return

    import ctypes
    reply = ctypes.windll.user32.MessageBoxW(
        0,
        "是否在桌面创建「WavEDA 仿真助手」快捷方式？\n\n以后双击桌面图标即可快速启动。",
        "创建快捷方式",
        4,  # 4 = Yes/No
    )
    if reply != 6:  # 6 = Yes
        return

    import subprocess
    exe_path = str(Path(sys.executable).resolve())
    work_dir = str(ROOT.resolve())
    lnk_path = str(shortcut_path.resolve())
    ps_cmd = (
        f"$s = (New-Object -COM WScript.Shell).CreateShortcut('{lnk_path}');"
        f"$s.TargetPath = '{exe_path}';"
        f"$s.WorkingDirectory = '{work_dir}';"
        f"$s.IconLocation = '{exe_path}';"
        f"$s.Description = 'WavEDA 仿真助手';"
        f"$s.Save()"
    )
    subprocess.run(["powershell", "-Command", ps_cmd], capture_output=True)


if __name__ == "__main__":
    _offer_desktop_shortcut()
    raise SystemExit(run_desktop_app())
