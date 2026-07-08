# Portable / 分享版说明

当前项目统一使用 `README.md` 作为主说明文档。

给新用户分享时，让对方按这两个文件操作即可：

1. 第一次使用：双击 `setup_env.bat`
2. 日常启动：双击 `start.bat`

当前 Git 协作仓库包含 `runtime/python/`，因此新用户一般不需要提前安装 Python。`data/index/` 是本地生成的索引文件，默认不提交 Git；第一次双击 `setup_env.bat` 会自动生成。

如果以后制作压缩包或网盘分享版，请确认压缩包中包含 `runtime/python/`。如果不包含，就需要用户本机安装 Python 3.11 或更新版本。
