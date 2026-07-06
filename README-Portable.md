# RAGGG Portable 使用说明

这是 `WavEDA + 多物理场笔记 RAG` 的 Windows 便携版。

## 怎么启动

双击：

```text
start.bat
```

或在命令行中运行：

```powershell
cd /d 这个文件夹
start.bat
```

## 便携能力

- 内置 Python 运行时。
- 内置 PySide6 和 numpy。
- 内置已经构建好的知识库索引。
- 可以复制整个文件夹到其他 Windows 位置后直接运行。
- 不需要目标电脑预先安装 Python。

## 注意事项

- `config\.env` 中包含 API Key，请不要公开分享。
- 如果目标电脑无法联网，仍可检索本地来源；但模型生成回答需要联网访问 DeepSeek。
- 当前便携包主要用于使用已构建好的知识库。如果要重新构建知识库，需要把原始 WavEDA helpHtml 和 Obsidian 笔记一起带过去，并修改 `config\.env` 中的源路径。

## 验证

双击：

```text
run_smoke_test.bat
```

它会运行三条基础问答，确认知识库和模型调用是否可用。
