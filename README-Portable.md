# Portable / 分享版说明

当前项目统一使用 `README.md` 作为主说明文档。

给新用户分享时，让对方按这两个文件操作即可：

1. 第一次使用：双击 `setup_env.bat`
2. 日常启动：双击 `start.bat`

如果要做真正“免安装依赖”的便携包，需要额外打包 `runtime/python/` 和已经生成好的 `data/index/`。当前 Git 协作仓库默认不提交这两个运行时产物。
