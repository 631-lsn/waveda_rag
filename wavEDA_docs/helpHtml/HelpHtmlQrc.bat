@echo off
setlocal enabledelayedexpansion

:: 设置资源文件前缀
set DISK_DIR=Z:\TsSolverLibrary\helpDoc\documentation\helpHtml
set FILENAME=helpWavEDA

set PREFIX=/
set QRC=helpHtml.qrc

:: 从共享盘拷贝
rd helpHtml  /s /q
md helpHtml
xcopy %DISK_DIR% helpHtml /D /Y /S /R /K


:: 创建资源文件并写入头部
(
    echo ^<RCC^>
    echo     ^<qresource prefix="%PREFIX%"^>
) > %QRC%

:: 遍历当前目录及子目录，添加文件到资源文件
for /r %%i in (*) do (
    set FILE=%%i
    set FILE=!FILE:%cd%\=!
    set FILE=!FILE:\=/!
    echo         ^<file^>!FILE!^</file^> >> %QRC%
)

:: 写入资源文件尾部
echo     ^</qresource^>>> %QRC%
echo ^</RCC^> >> %QRC%

echo %QRC% 文件已生成。
