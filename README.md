# WavEDA + 多物理场笔记 RAG

这是一个便携的本地 RAG 系统，用于合并检索三类资料：

- WavEDA 本地帮助文档（Markdown 提取页 + HTML）
- 团队自编教程（Markdown）
- 多物理场理论笔记（Obsidian Markdown）

系统重点服务 WavEDA 软件使用问题。涉及端口、边界、PML、网格、激励源、3D 几何建模、仿真设置等问题时，会优先检索 WavEDA 帮助文档；理论笔记主要用于补充电磁场、有限元、吸收边界等理论背景。

## 当前能力

- 合并 WavEDA HTML 帮助文档、提取页、团队教程和理论笔记。
- 构建本地知识库索引。
- 使用 WavEDA 优先的混合检索排序。
- 支持 DeepSeek / OpenAI 兼容接口生成回答。
- 未配置 API Key 时也能返回本地检索片段式回答。
- 提供 PySide6 深色桌面工作台。
- 回答中支持基础 Markdown 渲染：加粗、编号列表、项目列表。
- 回答中支持常见 LaTeX 公式可读化渲染。
- 右侧显示来源证据、来源类型、文件路径和匹配分数。

## 项目结构

```text
waveda_rag/
├── app/desktop_app.py              # 桌面应用入口
├── knowledge_base/                 # 团队教程、FAQ、案例
│   ├── tutorials/
│   │   ├── 02_电磁模块/
│   │   └── 03_案例/
│   └── theory_notes/
├── wavEDA_docs/                    # WavEDA 软件文档
│   ├── extracted_pages/
│   ├── helpHtml/
│   ├── examples/
│   └── error_cases/
├── data/
│   ├── raw_manifest.json
│   ├── processed_chunks.json
│   └── index/
│       ├── chunks.json
│       └── vectors.npy
├── config/
│   ├── .env                        # API Key 配置（不要公开）
│   ├── .env.example
│   └── kb_sources.yaml            # 知识库数据源配置
├── scripts/
│   ├── build_knowledge_base.py
│   ├── add_document.py            # 单文档增量追加
│   └── smoke_test.py
└── src/raggg/                     # RAG 引擎
    ├── loaders/
    ├── preprocessing/
    ├── indexing/
    ├── retrieval/
    ├── generation/
    ├── pipeline/
    └── desktop/
```

## 怎么启动

双击 `start.bat`。内置 Python 运行时，不需要预先装 Python。

## API Key 配置

`config/.env` 中已配置 DeepSeek API Key。也可以用其他 OpenAI 兼容接口：

```text
RAG_LLM_BASE_URL=https://api.deepseek.com
RAG_LLM_API_KEY=你的API密钥
RAG_LLM_MODEL=deepseek-chat
```

注意：`.env` 中包含密钥，不要公开、提交或截图发送。

## 验证

双击 `run_smoke_test.bat`，运行三条基础问答，确认知识库和模型调用是否可用。

## 更新知识库

新增文档后追加到索引：

```bash
runtime/python/python.exe scripts/add_document.py <文件路径>
```

然后在界面上点"重新载入索引"即可生效。

## 当前限制

- 使用本地哈希向量和关键词混合检索，无需下载 embedding 模型，但语义检索能力弱于 BGE/FAISS 方案。
- LaTeX 公式渲染是轻量转换，不是完整 MathJax 引擎。
- 知识库更新需要手动运行构建脚本。

## 推荐使用方式

1. 启动桌面工作台（双击 `start.bat`）。
2. 优先用明确的软件对象提问，例如：
   - `波端口怎么设置？`
   - `PML 和吸收边界有什么关系？`
   - `平面波激励怎么设置？`
