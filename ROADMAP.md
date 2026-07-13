# WavEDA RAG 优化路线图

> 写给 Codex 的执行清单。每个任务独立可执行，有明确的验收标准。

---

## 项目速览

- **定位**：WavEDA 多物理场仿真软件的桌面端本地 RAG 知识库助手
- **技术栈**：Python 3.x + PySide6 + QWebEngineView + numpy
- **核心依赖**：`numpy>=2.0`, `PySide6>=6.11`（只有这两个硬依赖）
- **入口**：`python app/desktop_app.py`
- **环境**：conda env `yolo_env`（`C:\Users\HP\.conda\envs\yolo_env\python.exe`）

### 关键路径速查

```
src/raggg/
├── config.py                  # Settings dataclass, .env 加载
├── models.py                  # Document, Chunk 数据结构
├── theme.py                   # 浅色/深色主题系统
├── i18n.py                    # 中/英文国际化
├── desktop/
│   └── main_window.py         # 桌面 GUI (~1580行，需拆分)
├── pipeline/
│   ├── builder.py             # 知识库全量构建
│   ├── rag_pipeline.py        # RAG 主流程：检索→生成
│   ├── ingestion.py           # 文档导入 (pdf/docx/md/html/txt)
│   └── source_watch.py        # 文件变更监听→自动重建
├── indexing/
│   ├── embeddings.py          # MD5哈希嵌入 (384维)
│   └── vector_store.py        # chunks.json + vectors.npy
├── retrieval/
│   └── retriever.py           # 混合检索 (向量0.65 + 关键词0.35 + heuristic)
├── generation/
│   ├── llm_client.py          # OpenAI 兼容 HTTP 客户端 (urllib)
│   └── prompt_builder.py      # Prompt 模板 + 本地降级答案
├── preprocessing/
│   ├── chunker.py             # 文档切块 (~800字符)
│   └── cleaner.py             # 文本清洗
└── loaders/
    ├── html_loader.py         # WavEDA HTML 帮助文档
    └── markdown_loader.py     # Obsidian/团队 Markdown 笔记
```

### 数据流

```
Document → Cleaner → Chunker → Chunk
                                 ↓
                    HashedEmbeddingModel.embed_many()
                                 ↓
                          np.ndarray (N×384)
                                 ↓
                           VectorStore
                           ↙          ↘
                     Retriever        LLM Client
                     (混合打分)       (OpenAI协议)
                           ↘          ↙
                         RAGPipeline.ask()
                              ↓
                         RAGAnswer → WebView 渲染
```

---

## 优先级说明

- **P0**：立即可做，效果立竿见影
- **P1**：重要但需要一定工作量
- **P2**：锦上添花，长期优化

---

## P0 — 架构重构（先做这个，否则后续改动越来越难）

### 任务 0-1：拆分 main_window.py

**现状**：`src/raggg/desktop/main_window.py` 1581 行，包含 GUI 布局、Markdown 渲染、图片管理、设置对话框、文件导入、文件监听、收藏夹、启动动画等所有逻辑。

**目标**：拆分为以下模块，每个文件 <400 行：

| 新文件 | 职责 | 从 main_window.py 拆出 |
|---|---|---|
| `desktop/chat_panel.py` | 聊天 WebView、消息追加、用户/助手气泡 | `_append_user()`, `_append_assistant()`, `_append_html()`, `_welcome_html()` |
| `desktop/sidebar_panel.py` | 侧边栏面板、状态卡片、快捷问题、来源列表 | `_sidebar_panel()`, `MetricCard`, `_sources_html()`, `_empty_sources_html()` |
| `desktop/settings_dialog.py` | 设置窗口 (API/主题/语言/WavEDA路径) | `SettingsDialog`, `LLM_PROVIDERS` |
| `desktop/loader_overlay.py` | 启动/加载动画 | `AILoaderOverlay` |
| `desktop/markdown_renderer.py` | Markdown→HTML、LaTeX→HTML、图片引用转换 | `markdown_to_html()`, `latex_formula_to_html()`, `latex_to_readable()`, `render_inline_markdown()`, `_convert_image_refs()`, `web_wrapper()` |
| `desktop/image_manager.py` | 图片索引构建、data URI 缓存、图片提取 | `_build_image_index()`, `_path_to_data_uri()`, `_preload_all_images()`, `_extract_images_from_sources()`, `IMAGE_PATH_RE`, `_normalize_image_key()` |
| `desktop/favorites_dialog.py` | 收藏夹对话框 | `_open_favorites()`, `_do_fav()`, `_do_fav_del()`, `_load_favs()` |

**注意**：
- `WorkbenchWindow` 保留在 `main_window.py`，只负责组装组件和处理信号/槽
- `COLORS` 来自 `theme.get_colors()`，拆分后的模块通过参数或函数调用获取
- 所有 `self._xxx` 私有方法移到对应模块后，`WorkbenchWindow` 中保留薄封装或信号连接

**验收标准**：`python app/desktop_app.py` 启动正常，功能无回归（提问、收藏、设置、导入、监听均正常）。

---

## P0 — 检索质量提升

### 任务 0-2：用语义嵌入替换哈希嵌入

**现状**：`src/raggg/indexing/embeddings.py` — `HashedEmbeddingModel` 对每个 token 做 MD5 → 384 维位置 + 随机符号，完全不捕捉语义相似性。全靠 `retriever.py` 里一堆 heuristic 规则补救（WavEDA 术语加分、标题匹配加分、PML 特殊加分...这些规则本质是在弥补嵌入质量的不足）。

**目标**：引入 sentence-transformers 的 `all-MiniLM-L6-v2`（384 维，与当前维度一致，无需改 VectorStore 结构）。

**步骤**：
1. 新建 `src/raggg/indexing/semantic_embeddings.py`，实现 `SemanticEmbeddingModel` 类，接口与 `HashedEmbeddingModel` 一致（`embed_text() -> np.ndarray`, `embed_many() -> np.ndarray`）
2. 在 `config.py` 的 `Settings` 中把 `embedding_model` 默认值改为 `"all-MiniLM-L6-v2"`
3. 在 `builder.py` 的 `build_knowledge_base()` 中根据 `settings.embedding_model` 选择模型
4. 提供降级：如果 sentence-transformers 没装，自动回退到 `HashedEmbeddingModel` 并打印提示

**代码框架**：
```python
# semantic_embeddings.py
class SemanticEmbeddingModel:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(model_name)
        self.dimensions = self.model.get_sentence_embedding_dimension()

    def embed_text(self, text: str) -> np.ndarray:
        return self.model.encode([text], normalize_embeddings=True)[0]

    def embed_many(self, texts: list[str]) -> np.ndarray:
        return self.model.encode(texts, normalize_embeddings=True, show_progress_bar=True)
```

**依赖**：`sentence-transformers>=2.0`（首次运行自动下载 ~90MB 模型到本地缓存）

**验收标准**：用相同问题对比新旧嵌入的 top-5 检索结果，语义嵌入的命中率显著优于哈希嵌入（可以用 `scripts/debug_retrieval.py` 做 A/B 对比）。

### 任务 0-3：精简 retriever 的 heuristic 规则

**现状**：`retriever.py` 的 `search()` 方法有 ~20 条硬编码加分规则（PML +0.3, 吸收边界 +0.25, 定义类 +0.45...）。语义嵌入上线后，大部分规则不再需要。

**目标**：
1. 换语义嵌入后，先保留核心加权框架，把规则精简到只保留：
   - `score = 0.7 * vector_score + 0.3 * lexical_overlap`（语义为主，关键词为辅）
   - `source_type` 优先级：`waveda_help` > `user_tutorial` > `obsidian_note`（WavEDA 帮助文档默认权重更高）
   - 公式查询 + 含公式 chunk 加分（`has_formula` metadata）
2. 删除所有针对特定术语的硬编码加分（PML、吸收边界、端口、定义类...）
3. 如果发现特定 case 语义嵌入也捞不上来，再考虑加少量 domain-specific prompt 改写而非 retriever 加权

**验收标准**：检索结果不差于旧版（人工抽 20 个问题对比），且代码行数减少 40%+。

---

## P1 — 工程优化

### 任务 1-1：LLM 流式输出

**现状**：`llm_client.py` 用 `urllib.request.urlopen` 发同步 POST，等完整响应后一次性返回。用户等待 5-15 秒看完整答案。

**目标**：改为 SSE streaming，WebView 中逐 token 追加显示。

**步骤**：
1. 在 `OpenAICompatibleClient` 中新增 `complete_stream()` 方法，用 `urllib.request.urlopen` 读取 `stream: true` 响应，逐行 yield delta content
2. 在 `RAGPipeline` 中新增 `ask_stream()` 方法，yield 增量答案片段
3. 在 `chat_panel.py` 中，流式回答用 `QTimer` 定期从生成线程取 token 追加到 WebView
4. 降级：不支持 streaming 时走原 `complete()` 路径

**关键细节**：
```
请求加 "stream": true
响应是 text/event-stream:
  data: {"choices":[{"delta":{"content":"波"}}]}
  data: {"choices":[{"delta":{"content":"端口"}}]}
  ...
  data: [DONE]
```

**验收标准**：回答逐字出现（类似 ChatGPT），不需要等完整结果。

### 任务 1-2：来源引用标注

**现状**：LLM 回答展示在 WebView，来源列表在侧边栏。用户不知道答案中哪句话对应哪个来源。

**目标**：Prompt 中要求 LLM 在回答中用 `[1]` `[2]` 标注引用；在 markdown_to_html 中把 `[N]` 渲染为可点击的上标链接，hover 显示来源标题。点击侧边栏中的来源卡片则高亮对应引用。

**步骤**：
1. 修改 `prompt_builder.py` 的 prompt：明确要求"引用资料时在句末标注来源编号，如 [1][2]"
2. 在 `markdown_renderer.py` 中，正则 `\[(\d+)\]` → 渲染为 `<sup>` 标签
3. 点击引用编号时，JavaScript 发 `console.log("RAGGG_CITE:N")`，`QWebEnginePage.javaScriptConsoleMessage` 拦截后高亮侧边栏对应来源卡片

**验收标准**：回答中出现可点击的 `[1]` `[2]` 引用标记，点击跳转到对应来源。

### 任务 1-3：配置管理规范化

**现状**：`config/.env` 手动编辑，格式损坏静默失败。`Settings.from_env()` 无 schema 校验。

**目标**：不引入 dataclasses-json 等重依赖，保持轻量。

**步骤**：
1. 在 `config.py` 中新增 `validate_settings()` 函数，检查必填字段、URL 格式、路径存在性
2. 在 `load_settings()` 中调用验证，异常时打印人类可读的修复建议（"请在 config/.env 中设置 RAG_LLM_API_KEY=sk-... "）
3. `SettingsDialog._save_all_and_accept()` 写入前做一次 validate
4. 在 `start.bat` 中加一行检测：如果 `config/.env` 不存在或 API key 为空，弹提示

**验收标准**：删除 `config/.env` 后启动，命令行能看到"请先设置 API Key"的提示而非神秘报错。

---

## P2 — 用户体验

### 任务 2-1：搜索历史

**现状**：只有收藏夹，没有自动保存的搜索历史。用户关了应用就丢失上下文。

**目标**：自动保存最近 50 条问答到 `data/history.json`，侧边栏增加"历史"标签可回溯。

**步骤**：
1. 每次 `_remember_turn()` 时追加到 `data/history.json`（与收藏夹类似的数据结构）
2. 侧边栏或右键菜单增加"历史记录"入口，点击加载历史 Q&A 到聊天区
3. 不自动加载历史到 LLM 上下文（避免 token 浪费），只有用户点击才加载

**验收标准**：关闭重开应用，能在界面上看到上次的问答记录。

### 任务 2-2：知识库构建进度

**现状**：`build_knowledge_base()` 一次性跑完，大 PDF 导入时界面卡在 loader 动画，无进度反馈。

**目标**：分阶段报告进度到 UI。

**步骤**：
1. `build_knowledge_base()` 改为 generator，yield 进度事件（`("loading", file_count)`, `("chunking", chunk_count)`, `("embedding", done, total)`, `("done", report)`）
2. Worker 线程通过 `Signal` 发送进度事件
3. `AILoaderOverlay` 接收进度，更新动画下方的文字（"正在索引第 3/29 个文档..."）

**验收标准**：导入大 PDF 时，loader 动画下方能看到进度文字实时更新。

### 任务 2-3：chunk 策略优化

**现状**：`chunker.py` 按 800 字符固定切分，标题处截断，不在公式中间切。这是比较粗糙的策略。

**目标**：
1. 引入 overlap：相邻 chunk 共享 100 字符上下文
2. 保留 heading chain：每个 chunk 的 `section` 字段记录完整路径（如 "电磁模块 > 边界条件 > PML 设置"）
3. PDF 导入的文档，按页切分后再按段落切分（`ingestion.py` 中 `_extract_pdf_text` 当前每页间用 `\n\n`，应保留页码边界标记）

**验收标准**：检索结果中同一个标题下的连续内容不再被切成两个语义不完整的 chunk。

---

## P2 — 功能扩展

### 任务 2-4：多模态 Vision 支持

**现状**：WavEDA 帮助文档包含大量操作截图（`wavEDA_docs/helpHtml/helpHtml/images/`），当前只能展示图片，不能让 LLM 看图。

**目标**：当 LLM 是 GPT-4o / Qwen-VL 等多模态模型时，将图片 base64 作为 vision API 请求的一部分发送。

**步骤**：
1. 在 `OpenAICompatibleClient` 中新增 `complete_with_images(prompt, image_paths)` 方法，构造 `{"type": "image_url", "image_url": {"url": "data:image/png;base64,..."}}` 格式的 messages
2. 在 `RAGPipeline.ask()` 中，如果检索到的来源包含图片，且模型支持 vision（配置项 `RAG_LLM_VISION=true`），则走带图路径
3. 降级：模型不支持 vision 时保持文本模式

**验收标准**：提问"这个设置界面在哪里？"，LLM 能看到界面截图并回答。

### 任务 2-5：本地 LLM 支持 (Ollama)

**现状**：LLM 客户端只走 OpenAI 兼容 HTTP API，无法使用本地模型。

**目标**：新增 Ollama 提供商支持（`http://localhost:11434/api/chat`）。

**步骤**：
1. `LLM_PROVIDERS` 列表新增 `("Ollama (本地)", "http://localhost:11434/v1", "llama3")`
2. 对于 Ollama，`complete_stream()` 使用 Ollama 原生 API 格式（`http://localhost:11434/api/chat`），因为 Ollama 的 OpenAI 兼容层不稳定
3. 在设置窗口的提供商列表中加入 Ollama 选项，并在旁边显示"需要先安装 Ollama"

**验收标准**：本地运行 `ollama run qwen2.5` 后，选择 Ollama 提供商，RAG 问答正常。

### 任务 2-6：导出的知识库报告

**现状**：问答结果只能在应用内查看。

**目标**：支持将当前问答（问题+回答+来源+图片）导出为单个 HTML 文件或 Markdown 文件，方便分享。

**验收标准**：工具栏增加"导出"按钮，点击保存为带图片的 HTML 文件，浏览器能正常打开。

---

## 需要注意的坑

1. **不要引入重型依赖**。项目前期设计就是轻量的（不用 FAISS、不用 PyTorch）。sentence-transformers 是唯一建议新增的较重依赖，其他优化用标准库或已有依赖完成。
2. **拆分 main_window.py 时注意信号/槽连接**。QRunnable Worker 的 signals 需要传回 WorkbenchWindow，拆分后的模块应该通过回调或信号与主窗口通信。
3. **图片路径兼容性**。当前图片索引支持多 root 来源（项目 assets、WavEDA 安装目录、Example 目录），修改 image_manager 时保持 `_normalize_image_key()` 逻辑不变。
4. **语义嵌入模型首次运行需下载**。`all-MiniLM-L6-v2` 约 90MB，首次 `SentenceTransformer("all-MiniLM-L6-v2")` 会自动下载到 huggingface 缓存。如果没有网络，降级到 HashedEmbeddingModel。
5. **Git 仓库中 `data/index/` 应持续 ignore**。索引是派生数据，不提交到 Git。`.gitignore` 中已包含。

---

## 建议执行顺序

```
第一轮: 0-1 (拆分main_window) → 0-2 (语义嵌入) → 1-2 (来源引用)
第二轮: 0-3 (精简retriever) → 1-1 (流式输出) → 1-3 (配置校验)
第三轮: 2-1 (搜索历史) → 2-2 (构建进度) → 2-3 (chunk优化)
第四轮: 2-4 (Vision) → 2-5 (Ollama) → 2-6 (导出报告)
```

每轮结束后启动完整功能验证：`python app/desktop_app.py` + 跑 `scripts/smoke_test.py`。
