@echo off
setlocal
set "RAGGG_PORTABLE_ROOT=%~dp0"
set "PYTHONPATH=%RAGGG_PORTABLE_ROOT%src"
set "PYTHONUTF8=1"
cd /d "%RAGGG_PORTABLE_ROOT%"
"%RAGGG_PORTABLE_ROOT%runtime\python\pythonw.exe" "%RAGGG_PORTABLE_ROOT%app\desktop_app.py"
endlocal
