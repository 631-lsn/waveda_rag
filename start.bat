@echo off
setlocal
set "RAGGG_PORTABLE_ROOT=%~dp0"
set "PYTHONPATH=%RAGGG_PORTABLE_ROOT%src"
set "PYTHONUTF8=1"
cd /d "%RAGGG_PORTABLE_ROOT%"

if not exist "%RAGGG_PORTABLE_ROOT%runtime\python\pythonw.exe" (
    echo ========================================
    echo  缺少 Python 运行时，无法启动
    echo ========================================
    echo.
    echo  本项目采用双轨发布：
    echo    GitHub 仓库（源码，~20MB）  — 不含运行时
    echo    GitHub Releases（完整包）  — 含 Python 运行时，解压即用
    echo.
    echo  请前往 Releases 页面下载完整包：
    echo   https://github.com/631-lsn/waveda_rag/releases
    echo.
    pause
    exit /b 1
)

"%RAGGG_PORTABLE_ROOT%runtime\python\pythonw.exe" "%RAGGG_PORTABLE_ROOT%app\desktop_app.py"
endlocal
