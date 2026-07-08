@echo off
setlocal
set "RAGGG_PORTABLE_ROOT=%~dp0"
set "PYTHONPATH=%RAGGG_PORTABLE_ROOT%src"
set "PYTHONUTF8=1"
cd /d "%RAGGG_PORTABLE_ROOT%"
if exist "%RAGGG_PORTABLE_ROOT%runtime\python\pythonw.exe" (
    "%RAGGG_PORTABLE_ROOT%runtime\python\pythonw.exe" "%RAGGG_PORTABLE_ROOT%app\desktop_app.py"
) else if exist "%RAGGG_PORTABLE_ROOT%.venv\Scripts\pythonw.exe" (
    "%RAGGG_PORTABLE_ROOT%.venv\Scripts\pythonw.exe" "%RAGGG_PORTABLE_ROOT%app\desktop_app.py"
) else (
    echo Local environment is not ready.
    echo Please double-click setup_env.bat first, then run start.bat again.
    pause
    exit /b 1
)
endlocal
