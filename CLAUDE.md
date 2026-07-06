# waveda_rag 项目配置

## Python 环境
- 使用 `yolo_env` (C:\Users\HP\.conda\envs\yolo_env\python.exe)
- 便携包内置Python在 `runtime\python\python.exe`

## 项目背景
WavEDA 多物理场仿真软件的本地 RAG 知识库助手。三人团队（大一下本科生）。

### 核心功能
- 检索 WavEDA 帮助文档 + 团队教程 + 理论笔记，LLM 生成回答
- 桌面应用 (PySide6 + QWebEngineView)，双击 start.bat 启动
- 支持 DeepSeek/Kimi/千问/百炼 等大模型，界面上切换
- 回答支持 Markdown 渲染、LaTeX 公式、本地图片显示
- 知识库 1908 个知识块，使用本地哈希向量 + 关键词混合检索

### 目录结构
```
waveda_rag/
├── start.bat                    # 双击启动
├── knowledge_base/              # 团队教程 (Markdown)
│   ├── tutorials/02_电磁模块/   # 端口、激励、边界、求解器、后处理
│   └── tutorials/03_案例/       # 微环谐振器、Y分支波导
├── wavEDA_docs/                 # WavEDA 软件文档
│   ├── extracted_pages/         # 帮助页提取为 Markdown
│   ├── helpHtml/                # 官方 HTML 帮助（含图片）
│   ├── examples/                # 仿真案例
│   └── error_cases/             # 错误排查
├── config/
│   ├── .env                     # API Key (Git忽略)
│   └── kb_sources.yaml          # 知识库数据源配置
├── scripts/
│   └── add_document.py          # 单文档增量追加到索引
├── data/index/                  # 知识库索引 (Git忽略)
├── src/raggg/                   # RAG 引擎源码
│   ├── desktop/main_window.py   # PySide6 桌面界面
│   ├── pipeline/                # 检索+生成管线
│   └── indexing/                # 本地哈希向量 (384维)
└── runtime/python/              # 便携 Python 运行时 (Git忽略)
```

### 知识库更新流程
1. 在 knowledge_base/ 下写新 Markdown
2. 运行 `runtime/python/python.exe scripts/add_document.py <文件路径>`
3. 界面上点"重新载入索引"
