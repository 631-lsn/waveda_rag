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
- 知识库 4974 个知识块，使用本地哈希向量 + 关键词混合检索

### 目录结构
```
waveda_rag/
├── start.bat                        # 双击启动
├── knowledge_base/                  # 知识库（Markdown）
│   ├── 01_team_tutorials/           # 团队自编教程
│   │   └── tutorials/               # 02_电磁模块/ 03_案例/
│   ├── 02_software_manual/          # 软件功能手册（98页）
│   ├── 03_examples/                 # 仿真案例（29个）
│   ├── 04_error_cases/              # 错误排查
│   ├── 05_reference/                # 参考资料（索引/专题/材料库）
│   └── 06_theory_notes/             # 理论笔记（Obsidian vault）
├── wavEDA_docs/
│   └── helpHtml/                    # 官方 HTML 帮助（原始文件+图片）
├── config/
│   ├── .env                         # API Key (Git忽略)
│   └── kb_sources.yaml              # 知识库数据源配置
├── scripts/
│   ├── add_document.py              # 单文档增量追加
│   └── rebuild_index_merge.py       # 合并式索引重建
├── data/index/                      # 知识库索引
├── src/raggg/                       # RAG 引擎源码
│   ├── desktop/main_window.py       # PySide6 桌面界面
│   ├── pipeline/                    # 检索+生成管线
│   └── indexing/                    # 本地哈希向量 (384维)
└── runtime/python/                  # 便携 Python 运行时
```

### 知识库更新流程
1. 在 knowledge_base/ 下写新 Markdown
2. 运行 `runtime/python/python.exe scripts/add_document.py <文件路径>`
3. 界面上点"重新载入索引"
