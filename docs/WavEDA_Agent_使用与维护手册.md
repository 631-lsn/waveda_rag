# WavEDA Agent 使用与维护手册

> 文档用途：项目交付、日常使用、知识库维护、二次开发和 Windows 发布  
> 适用基线：2026-07-16 的 `main` 分支桌面版  
> 维护原则：以实际代码和自动化测试为准；历史设计文档只用于理解演进过程

## 1. 先认识这个项目

WavEDA Agent 是一个面向 WavEDA 初学者的本地桌面 RAG 问答工具。它不是 WavEDA 求解器，也不是一个独立部署的 Web 后端。它在用户电脑上完成资料读取、分块、检索和界面展示，再通过 OpenAI-compatible HTTP API 调用外部大模型生成回答。

项目当前由四部分组成：

1. PySide6 桌面前端：聊天、会话、设置、收藏、来源查看和知识库管理。
2. 本地 RAG 后端：文档加载、清洗分块、向量索引、混合检索、提示词和模型调用。
3. WavEDA 知识资产：团队教程、软件手册、案例、错误、参考资料、理论资料和官方 HTML 帮助。
4. Windows 交付工具：源码便携启动脚本、PyInstaller EXE、ZIP 发布包和桌面快捷方式。


## 2. 项目迭代形成了什么

本项目由小组成员的多个模型与知识库版本融合而来，之后围绕“让新人拿到后能直接用、让维护人员能继续扩展”完成了以下迭代：

- 将分散资料整理为统一的六层知识库，并为电磁、光子、电路、热、力学、声学压电、多物理场和封装预留框架。
- 增补 WavEDA 新手教程、FAQ、错误排查、端口、边界、求解器、后处理和案例说明。
- 将官方帮助中的图片信息转成可检索文字，只保留真正辅助操作的界面图、选项图和结果图候选。
- 建立“项目内图片优先，本机 WavEDA 帮助和 Example 图片兜底”的解析逻辑。
- 增加桌面 GUI、深浅主题、中英文、人格、设置、快捷问题、来源追溯和收藏夹。
- 增加多会话与连续对话，最近 5 轮会进入下一次检索和提示词上下文。
- 增加流式输出、后台工作线程、启动加载状态和知识库重建状态。
- 增加临时文档附件、知识库管理页、自动分类建议、自动监听和手动重建索引。
- 将全量重复构建优化为按文档指纹和 chunk ID 复用的增量构建，并增加图片 LRU 缓存。
- 建立源码启动、免安装 EXE、ZIP 校验、个人路径清理、空白会话发布和桌面快捷方式流程。

## 3. 两种交付形态

| 形态 | 适用对象 | 启动方式 | 是否需要 Python |
| --- | --- | --- | --- |
| Windows EXE 发布包 | 普通用户、培训和演示 | 双击 `WavEDA_Assistant.exe` | 不需要 |
| Git 源码仓库 | 维护人员、开发人员 | `setup_env.bat` 后运行 `start.bat` | 通常需要 |

注意：`runtime/` 和 `.venv/` 均被 `.gitignore` 排除。维护者本机虽然可能存在 `runtime/python`，但全新 Git clone 不会自动得到它。只有专门制作且包含 runtime 的源码压缩包才是真正的“便携 Python 版”。对普通用户优先交付 EXE ZIP。

## 4. 普通用户使用教程

### 4.1 EXE 第一次启动

1. 完整解压 ZIP，不要在压缩软件预览窗口中直接启动。
2. 保持 `WavEDA_Assistant.exe`、`_internal/`、`knowledge_base/`、`wavEDA_docs/`、`data/` 和 `config/` 的相对位置不变。
3. 将整个目录放在用户有写权限的位置，例如桌面或文档目录，不建议放入 `C:\Program Files`。
4. 双击 `WavEDA_Assistant.exe`。
5. 第一次启动时可选择创建桌面快捷方式。
6. 欢迎页出现“知识块”和模型信息后即可提问。

### 4.2 源码版第一次启动

1. 安装 Python 3.11 或更高版本，并安装 Python Launcher `py`。
2. 从 `https://github.com/631-lsn/waveda_rag.git` clone 项目，进入项目根目录。
3. 在项目根目录双击 `setup_env.bat`。
4. 脚本会优先使用 `runtime/python`；不存在时创建 `.venv`、安装依赖、构建索引并运行冒烟测试。
5. 配置完成后双击 `start.bat`。
6. 日常启动不需要重复运行 setup；知识库或依赖发生重大变化时再运行。

### 4.3 界面区域

- 左侧会话栏：新建、切换和删除会话。空会话会在下次启动时自动清理。
- 中央聊天区：欢迎页、快捷示例、用户问题、流式回答和附件入口。
- 右侧资料栏：默认折叠，点击右上角方形按钮或按 `Ctrl+B` 展开。这里显示知识库、知识块、模型、监听状态、重建按钮、快捷问题和来源证据。
- 设置窗口：个性化、API、WavEDA 路径和知识库管理。

```text
┌────────────┬──────────────────────────────┬──────────────┐
│ 左侧会话栏   │          中央聊天区            │ 右侧资料与状态栏 │
│ + 新建会话   │ 欢迎页、问题、流式回答、附件     │ 状态、重建索引   │
│ 切换历史会话 │ 来源关联图片、输入框、发送按钮     │ 快捷问题、来源证据 │
│ 删除当前会话 │                              │ 设置、收藏夹     │
└────────────┴──────────────────────────────┴──────────────┘
```

隐藏左右栏只改变布局，不会停止知识检索、会话保存或知识库文件监听。

### 4.4 提问方法

推荐同时说明“目标、当前步骤、具体报错、已有设置”，例如：

```text
我正在做微带天线频域仿真，波端口预览方向朝内，运行后 S11 异常。
请告诉我应该检查哪些设置，并给出 GUI 路径。
```

输入完成后按 `Enter` 或点击向上箭头发送。当前版本没有实现 `Ctrl+Enter` 专用快捷键。

回答开始前会显示检索状态；模型返回内容后会流式显示。右侧会列出命中的来源、文件路径和匹配分数。点击来源路径可以打开原始 Markdown 或 HTML 文档。

模型 API 不可用时，程序会退回本地检索片段回答。此时仍能查看来源，但回答的归纳和表达能力会下降。

没有 API Key 时仍可使用本地检索、来源查看、收藏、会话管理、知识库编辑和索引重建，适合离线核验知识库内容。

### 4.5 连续对话和会话

- 当前会话最多保存最近 5 轮问答作为上下文。
- 检索时会把最近 3 个问题与当前问题组合，帮助理解“这个参数呢”“上一步之后怎么办”等追问。
- 最多保留 50 个会话，超出后自动删除最早会话。
- 会话保存在 `data/conversations.json`，只属于本机，不应提交到 Git 或放入发布包。
- 首轮回答后会尝试用大模型生成会话标题；API 不可用时使用问题前 20 个字符。

### 4.6 临时附件与永久入库的区别

聊天框旁的 `+` 是临时附件，不是永久入库：

| 操作 | 用途 | 是否写入知识库 | 当前支持 |
| --- | --- | --- | --- |
| 聊天框 `+` | 针对当前文件提问 | 否 | PDF、PPTX、DOCX、MD、TXT、HTML；部分模型显示图片选项 |
| 设置 → 知识库管理 | 长期资料维护 | 是 | PDF、PPTX、MD |
| 直接维护 `knowledge_base/` | 批量和正式维护 | 是 | MD、PDF、DOCX；详见第 5 节 |

临时附件只把提取文本的前 3000 个字符拼入本次问题，发送后自动清空。长文档需要分段提问，或正式入库后再检索。

选择文件后，输入框上方会显示附件名称；发送前可点击旁边的 `×` 移除。

图片上传目前属于实验入口，不应作为正式多模态能力宣传。现有客户端仍把图片数据放进普通文本消息，且附件内容会被截断，并未按模型 API 的 `image_url`/多段 content 格式发送。真正的截图识别需要按第 8.6 节改造后再验收。

### 4.7 回答中的图片

程序会从检索来源的图片字段中选取最多 6 张图片，优先顺序为：

1. `knowledge_base/assets/images/`
2. `assets/images/`
3. 项目自带 `wavEDA_docs/helpHtml/helpHtml/`
4. 用户配置的本机 WavEDA 帮助目录
5. 用户配置的本机 WavEDA Example 目录

如果图片没有出现，先确认知识文档中记录的是相对路径，再确认“设置 → WavEDA 路径”填写正确并已重启软件。

### 4.8 设置

#### 个性化

可设置浅色/深色主题、中英文和回答人格。设置写入 `config/.env`。为保证窗口样式、欢迎页和所有文本一致，保存后应重启应用。

#### API

当前界面预置 DeepSeek、Kimi、通义千问/百炼和 OpenAI-compatible 配置。选择提供商后 URL 与模型名自动填写，只需设置 API Key。

自定义 Base URL 或自定义模型目前没有独立 GUI 输入框，可直接编辑 `config/.env`。再次用设置窗口保存 API 时可能被预置提供商覆盖，因此企业自定义接口最好同时扩展 `LLM_PROVIDERS`。

#### WavEDA 路径

通常只填写安装根目录：

```text
D:\Program Files\WavEDA
```

安装结构特殊时再单独填写帮助文档目录和 Example 目录。路径配置只影响本机图片查找，不会把本机 WavEDA 文件复制到项目。保存后必须重启，启动时才会重新建立图片路径索引。

### 4.9 收藏和纠错

- “复制”：复制当前回答文本。
- “收藏”：保存到 `data/favorites.json`，收藏夹支持问题和回答内容搜索。
- “纠错”：把用户修正意见交给模型润色，再追加到 `knowledge_base/01_team_tutorials/02_常见问题FAQ.md`。

收藏搜索会同时匹配问题和回答，忽略英文大小写，并兼容普通空格、连续空格、制表符和全角空格。

纠错内容会进入团队高优先级教程，必须由懂 WavEDA 的维护人员复核。不要把未经验证的模型润色结果直接当作公司正式知识。

### 4.10 快捷键

| 快捷键 | 功能 |
| --- | --- |
| `Ctrl+L` | 聚焦并选中提问框 |
| `Ctrl+N` | 新建会话 |
| `Ctrl+B` | 显示或隐藏右侧资料栏 |

## 5. 知识库维护教程

### 5.1 选择维护方式

| 场景 | 推荐方式 |
| --- | --- |
| 偶尔导入一份 PDF/PPTX/MD | 设置 → 知识库管理 |
| 编写教程、FAQ、错误案例 | 直接编辑对应 Markdown |
| 批量迁移资料或调整目录 | 后端直接维护 `knowledge_base/` 后运行构建脚本 |
| 更新官方帮助 HTML | 更新 `wavEDA_docs/helpHtml/helpHtml/` 后手动重建 |
| 临时阅读用户文件 | 聊天框 `+`，不要入库 |

### 5.2 从前端永久入库

1. 打开“设置 → 知识库管理”。
2. 点击“选择文件”，选择 PDF、PPTX 或 Markdown。
3. 选择六大资料类型之一。
4. 选择具体子目录，或保留“自动推荐”。
5. 检查重要度。团队教程默认 5，软件手册和案例默认 4，错误默认 3，参考默认 2，理论默认 1。
6. 填写必填备注，用于自动分类判断。
7. 点击确认导入，检查目标目录、AI 分类建议和 Markdown 预览。
8. 再次确认后写入知识库。主窗口会检测变化并在后台重建索引。
9. 用一个典型问题验证新资料是否出现在右侧来源中。

注意事项：

- PDF 只提取可复制文本，扫描件没有 OCR，可能得到空内容。
- PPTX 只提取文本框和表格，不保留版式、动画和图片含义。
- 导入备注用于分类辅助，目前不会自动写入最终 Markdown。
- 同名文件的 UI 导入可能覆盖同目录已有 Markdown；确认前先检查目标路径，必要时重命名源文件。

### 5.3 在前端编辑和删除

知识库管理页左侧树展示 Markdown 文件。点击文件可编辑，保存后触发后台重建；右键文件可以删除。

删除前应确认：

1. 该内容是否被其他文档链接。
2. 是否存在同名案例或图片依赖。
3. Git 中是否已有可恢复版本。
4. 删除后是否已重建索引并验证旧答案不再命中。

### 5.4 后端直接新增资料

正式维护推荐直接把源文件放入正确目录，而不是直接编辑 `data/index/`：

```text
knowledge_base/
├─ 01_team_tutorials   人工验证的新手教程、FAQ、标准工作流
├─ 02_software_manual  WavEDA GUI 和功能手册
├─ 03_examples         可复现工程案例
├─ 04_error_cases      报错原文、原因和解决步骤
├─ 05_reference        材料、按钮、索引、专题和外部参考
└─ 06_theory_notes     物理理论、教材和论文笔记
```

物理场目录和验收规则以项目根目录的 `KNOWLEDGE_BASE_CONTRIBUTION_GUIDE.md` 为准。不要把同一份资料复制到多个物理场目录；跨场资料放入“多物理场耦合”，其他目录用链接引用。

当前生产构建器会读取：

- `knowledge_base/` 内所有非隐藏 Markdown。
- `knowledge_base/` 内 PDF 和 DOCX 的可提取文本。
- `WAVEDA_HELP_ROOT` 下所有 HTML/HTM 官方帮助。

它不会直接读取 `knowledge_base/` 内的 TXT、PPTX 或 HTML。此类文件应先转成 Markdown；PPTX 可通过前端知识库管理导入。

### 5.5 Frontmatter 模板

```yaml
---
title: "文档标题"
content_kind: "tutorial"
physics_domain: "thermal"
waveda_module: "Thermal"
software_version: "待确认"
priority: 3
status: "draft"
indexing: true
---
```

- `priority` 范围 1 到 5，数值越高越容易优先检索。
- `indexing: false` 用于目录说明、维护入口和不应回答给用户的文档。
- `physics_domain` 建议值见 `KNOWLEDGE_BASE_CONTRIBUTION_GUIDE.md`。
- 未写 priority 时，按六层目录自动设置默认值。
- 关键参数、菜单路径和结论未经验证时必须标注“待确认”。

### 5.6 文档写作规范

正式教程建议至少包含：

1. 适用模块、软件版本和使用场景。
2. 前置条件、单位、材料和几何要求。
3. 准确的 GUI 路径与逐步操作。
4. 参数含义、默认建议和适用范围。
5. 运行前检查项。
6. 正确结果的判断方法。
7. 常见错误、限制和不适用场景。
8. 来源、验证人和验证日期。

图片只能辅助识别按钮、选项界面、图例和结果，关键步骤必须同时有文字。禁止写维护者个人电脑的绝对路径。

FAQ 和教程小节标题应写成用户会实际提出的问题，并同时包含“对象 + 动作”，例如：

```markdown
## 如何导出 S 参数并找到 snp 文件？

在左侧工程树中找到“电磁结果 → 端口”……
```

不要只写“说明”“设置”“注意事项”等泛化标题。当前检索会同时使用标题、小节和正文，但标题有单独的匹配权重；具体标题能提升准确率，正文仍需保留完整步骤和同义词。

### 5.7 重建索引

优先使用项目虚拟环境：

```powershell
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe -B scripts\build_knowledge_base.py
```

如果交付包包含便携 Python：

```powershell
.\runtime\python\python.exe -B scripts\build_knowledge_base.py
```

也可以在右侧资料栏点击“重建索引”。程序运行期间会每 5 秒扫描一次 `knowledge_base/`，检测到变化后等待 2 秒稳定时间，再后台增量构建；正在回答时会等到空闲再构建。

官方帮助目录不在这个自动监听范围内。修改 `wavEDA_docs/` 或外部帮助路径后，应手动点击“重建索引”或运行脚本。

以下情况建议主动手动重建并验证知识块数量：

- 批量复制、移动或删除了知识源文件。
- 修改了官方帮助目录或外部 WavEDA 帮助路径。
- 源文件已经更新，但监听状态长期没有变化。
- `data/index/` 被清理、损坏或只剩部分文件。
- 修改了 loader、cleaner、chunker、embedding 或 metadata 规则。

### 5.8 构建产物

```text
data/
├─ raw_manifest.json          文档指纹和来源清单
├─ processed_chunks.json      构建过程输出的全部 chunk
└─ index/
   ├─ chunks.json             检索文本与元数据
   ├─ vectors.npy             384 维 float32 向量矩阵
   └─ build_meta.json         chunk/embedding 结构版本
```

这些文件都是可再生数据，不应手工编辑，也不提交 Git。删除索引后重新运行构建脚本即可恢复。

### 5.9 入库验收

每次正式入库至少完成：

1. 运行构建脚本且无异常。
2. 运行 `run_smoke_test.bat`。
3. 用新资料中的明确术语运行 `scripts/debug_retrieval.py` 的定制查询，或在 GUI 提问。
4. 检查新文档是否进入前 6 个来源。
5. 检查旧的典型问题是否没有明显回退。
6. 检查图片路径、个人路径、API Key、聊天记录和内部敏感信息。
7. 由专业人员审核后再把 `status` 从 draft 改为 verified 或团队约定状态。

## 6. 后端架构

### 6.1 问答调用链

```text
app/desktop_app.py
  → load_settings()
  → WorkbenchWindow
  → RAGPipeline.ask()
  → Retriever.search()
  → build_prompt()
  → OpenAICompatibleClient.complete_stream()
  → 流式回传 GUI
  → 保存会话、显示来源和关联图片
```

“后端”全部运行在桌面进程内部，没有 FastAPI、Flask、数据库服务或独立守护进程。

### 6.2 索引构建链

```text
Markdown/PDF/DOCX + 官方 HTML
  → loader 转成 Document
  → cleaner 去除 Frontmatter 和维护噪声
  → chunker 按标题和约 800 字符分块
  → 生成稳定 chunk ID
  → 384 维本地哈希向量
  → NumPy 矩阵 + chunks.json
```

构建器会比较文档指纹，未变化文档复用旧 chunk；相同 chunk ID 复用旧向量。删除源文件后，下次构建会自动把对应内容移出索引。

### 6.3 检索策略

`Retriever` 同时计算哈希向量相似度、全文词项重合和标题词项重合，再叠加：

- 六层知识库 priority 权重。
- WavEDA 术语、PML、吸收边界、定义类问题和公式类问题加分。
- 团队教程、软件手册和官方帮助优先。
- 同一文档最多返回 2 个 chunk，避免长文档占满上下文。

默认向模型提供前 6 个来源，每个来源最多截取 900 个字符。

### 6.4 连续对话

最近 5 轮问答会压缩后加入提示词；最近 3 个问题会用于扩展检索查询。历史保存在本地 JSON，不进入知识索引。

### 6.5 模型调用和降级

`OpenAICompatibleClient` 使用标准 `/chat/completions`、Bearer Token 和 SSE 流式响应。若供应商不接受 `stream=true`，自动回退普通请求；API 仍失败时返回本地来源片段并显示警告。

### 6.6 配置加载

配置优先读取 `<应用根目录>/config/.env`，不存在时再读取根目录 `.env`。主要变量如下：

| 变量 | 含义 |
| --- | --- |
| `RAG_LLM_BASE_URL` | OpenAI-compatible API 根地址 |
| `RAG_LLM_API_KEY` | API Key |
| `RAG_LLM_MODEL` | 模型名 |
| `RAG_LANGUAGE` | `zh` 或 `en` |
| `RAG_THEME` | `light` 或 `dark` |
| `RAG_PERSONALITY` | 人格键名 |
| `WAVEDA_ROOT` | 本机 WavEDA 安装根目录 |
| `WAVEDA_HELP_ROOT` | 官方帮助 HTML 根目录 |
| `WAVEDA_EXAMPLE_ROOT` | 本机 Example 根目录 |
| `OBSIDIAN_VAULT_ROOT` | 主知识库根目录，默认 `knowledge_base` |
| `RAG_DATA_DIR` | 本地数据目录，默认 `data` |

`config/kb_sources.yaml` 当前没有被 `build_knowledge_base()` 读取。不要以为只改这个 YAML 就能增加生产数据源；若要启用多数据源配置，需要在 builder 中实现 YAML 解析、路径校验、去重和测试。

### 6.7 数据流、隐私和备份

使用外部大模型时，客户端会把当前问题、压缩后的最近对话、临时附件片段以及命中的知识库正文发送给所配置的 API 服务。工程名称、报错、参数和内部资料可能因此离开本机。公司部署前应确认供应商的数据保留、训练使用、地域和访问控制政策；敏感项目优先接入公司网关。

建议按数据性质备份：

| 数据 | 是否应备份 | 说明 |
| --- | --- | --- |
| `knowledge_base/`、`wavEDA_docs/` | 必须 | 知识源文件，应由 Git 或受控文档库管理 |
| `config/.env.example` | 必须 | 无密钥配置模板，可进 Git |
| `config/.env` | 受控备份 | 含 API Key 和本机路径，不可进 Git |
| `data/conversations.json` | 按需 | 本机聊天记录，可能含工程信息 |
| `data/favorites.json` | 按需 | 用户收藏；发布前应清空个人数据 |
| `data/index/` | 通常不需要 | 可由源文件重新构建，不应作为唯一备份 |
| 已发布 ZIP | 建议保留 | 与 Git commit、知识库版本和发布日期一同归档 |

## 7. 代码目录和职责

| 路径 | 职责 |
| --- | --- |
| `app/desktop_app.py` | 源码/EXE 统一入口、应用根目录、桌面快捷方式 |
| `src/raggg/config.py` | `.env` 读取、路径解析、Settings |
| `src/raggg/desktop/main_window.py` | 主窗口、问答、会话、来源、附件、自动重建 |
| `src/raggg/desktop/settings_dialog.py` | 个性化、API、WavEDA 路径、知识库管理入口 |
| `src/raggg/desktop/knowledge_manager.py` | 知识树编辑、删除、PDF/PPTX/MD 导入 |
| `src/raggg/desktop/session_manager.py` | 会话 JSON 持久化和轮数限制 |
| `src/raggg/desktop/widgets.py` | 状态卡和加载动画 |
| `src/raggg/desktop/image_cache.py` | 图片按需 Base64 编码和 LRU 缓存 |
| `src/raggg/loaders/` | Markdown 和 HTML 转 Document |
| `src/raggg/preprocessing/` | 清洗和分块 |
| `src/raggg/indexing/` | 哈希 embedding 和 VectorStore |
| `src/raggg/retrieval/retriever.py` | 混合检索、优先级和去重复 |
| `src/raggg/generation/` | 提示词、人格和模型客户端 |
| `src/raggg/pipeline/builder.py` | 全量语义一致、实现增量复用的索引构建器 |
| `src/raggg/pipeline/rag_pipeline.py` | 检索、生成、流式回退的总编排 |
| `src/raggg/pipeline/source_watch.py` | 知识源文件变化检测 |
| `scripts/` | 构建、冒烟、检索调试和发布工具 |
| `packaging/` | PyInstaller spec |
| `tests/` | 单元和界面回归测试 |

## 8. 常见二次开发任务

### 8.1 修改 GUI

1. 主布局和交互放在 `desktop/main_window.py`。
2. 可复用控件放在 `desktop/widgets.py`。
3. 设置项放在 `desktop/settings_dialog.py`。
4. 中英文文本放在 `i18n.py`、`i18n_kb.py` 或 `i18n_prompt.py`，不要在多个窗口重复硬编码。
5. 颜色和控件样式放在 `theme.py`。
6. 为可观察行为补充 `tests/test_desktop_layout.py`。
7. 同时在浅色、深色、左右栏展开和窗口最小尺寸下检查。

耗时的索引、网络和文档解析任务必须继续使用 `Worker/QThreadPool`，不能阻塞 Qt 主线程。

### 8.2 增加模型提供商

1. 在 `settings_dialog.py` 的 `LLM_PROVIDERS` 增加名称、Base URL 和默认模型。
2. 确认接口兼容 `/chat/completions`、Bearer Token 和 SSE。
3. 如果返回结构不同，在 `generation/llm_client.py` 做提供商适配。
4. 补充普通响应、流式响应、401 和超时测试。
5. 更新 `.env.example`、本手册和发布配置。

### 8.3 修改 Prompt 或人格

- 回答事实约束和输出结构：`generation/prompt_builder.py` 与 `i18n_prompt.py`。
- 人格风格：`generation/personality.py`。
- 欢迎语：`i18n.py`。

人格只能改变表达方式，不能覆盖“以来源为准、信息不足要说明”的事实约束。企业正式版本建议默认使用 `normal`。

### 8.4 支持新的文档格式

需要同时考虑四层：

1. 文件选择器是否允许选择。
2. 是否有稳定解析器，能提取文字、表格和必要元数据。
3. 解析后是保存原文件还是转换 Markdown。
4. PyInstaller 是否包含依赖和 hidden import。

修改位置通常包括 `pipeline/ingestion.py`、`pipeline/knowledge_import.py`、`desktop/knowledge_manager.py`、`pipeline/builder.py`、requirements、spec 和 tests。

### 8.5 增加物理场或知识层级

1. 按贡献指南创建目录和 `_README.md`。
2. 更新 `markdown_loader.py` 的知识层级或物理场推断。
3. 更新 `knowledge_manager.py` 的分类、显示名和默认 priority。
4. 更新知识库结构文档和模板。
5. 用该领域的同义词、缩写和跨场问题补检索测试。

### 8.6 实现真正的图片多模态

当前功能尚未达到生产标准。完整改造至少需要：

1. 将 `llm_client.py` 的 message content 改为文本和 `image_url` 的结构化数组。
2. 只对确认支持视觉的提供商和模型开放图片选择。
3. 图片做尺寸、格式、体积和隐私检查，不把 Base64 截断。
4. 区分“当前用户上传图片”和“知识库回答配图”，两者用途不同。
5. 增加无视觉模型、超大图片、损坏图片和供应商拒绝请求的降级路径。
6. 用真实 WavEDA 截图做端到端验收，确认能识别报错、选项和工程树位置。

### 8.7 检索规模扩大

当前约数千 chunk，NumPy 全矩阵检索简单且足够。达到数万或更多 chunk 并出现实测延迟后，再评估 FAISS、LanceDB 或服务化向量库。迁移时必须保留 metadata、priority、来源路径、同文档去重和可再生索引能力。

### 8.8 不应继续使用的旧入口

- `scripts/add_document.py` 仍引用旧的 `MarkdownChunker` 和旧 `VectorStore` API，与当前代码不兼容，不应作为生产入库命令。
- `scripts/rebuild_index_merge.py` 是保留外部旧 chunk 的特殊迁移工具，不是日常构建入口。
- `docs/superpowers/` 是历史设计记录，不保证描述当前 UI。

日常构建统一使用 `scripts/build_knowledge_base.py`。

## 9. 开发环境和测试

### 9.1 建立环境

最简单方式是运行 `setup_env.bat`。开发者也可以手动执行：

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:PYTHONPATH = "src"
```

### 9.2 从源码启动

```powershell
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe app\desktop_app.py
```

调试 GUI 时使用 `python.exe` 可以看到控制台输出；`start.bat` 使用 `pythonw.exe`，不会显示终端。

### 9.3 测试

```powershell
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m compileall -q src app scripts
git diff --check
```

涉及知识库或检索时再执行：

```powershell
.\.venv\Scripts\python.exe -B scripts\build_knowledge_base.py
.\.venv\Scripts\python.exe -B scripts\smoke_test.py
```

Qt 测试在无显示环境可设置：

```powershell
$env:QT_QPA_PLATFORM = "offscreen"
```

## 10. EXE 打包与发布

### 10.1 打包前准备

1. `.venv` 已安装 `requirements-build.txt`。
2. 知识库已经构建并通过冒烟测试。
3. `config/.env` 中存在发布所需 API Key；当前脚本发现空 Key 会拒绝打包。
4. `WAVEDA_ROOT` 和 `WAVEDA_EXAMPLE_ROOT` 可以保留在本机配置中，但发布脚本会清空发布副本。
5. 不提交或携带 `data/conversations.json` 和个人收藏。

### 10.2 打包命令

双击：

```text
build_exe.bat
```

或运行：

```powershell
.\.venv\Scripts\python.exe -B scripts\build_exe_release.py
```

脚本会依次：

1. 从项目图标生成 Windows ICO。
2. 重建知识索引。
3. 运行 PyInstaller one-dir 构建。
4. 复制知识库、官方帮助和索引。
5. 生成发布专用 `.env`，清空个人 WavEDA 路径。
6. 清空收藏并排除聊天历史。
7. 清理文本中的开发者路径。
8. 校验 EXE、索引、Key、路径和隐私文件。
9. 生成 ZIP，并执行 CRC 和最长路径检查；PNG 等图片使用不压缩存储，降低解压错误概率。

输出位置：

```text
dist/WavEDA_Assistant/
dist/WavEDA_Assistant_Windows_YYYYMMDD.zip
```

### 10.3 发布验收

必须在另一处新目录完整解压并检查：

1. EXE 能启动，欢迎页显示非零知识块。
2. 能完成一条普通问题和一条连续追问。
3. 右侧来源可点击打开。
4. 深浅主题、左右栏和流式输出正常。
5. 设置中的 WavEDA 路径为空，没有开发者电脑路径。
6. 不存在旧会话和个人收藏。
7. 填入测试 WavEDA 路径并重启后，图片可显示。
8. 桌面快捷方式目标和工作目录正确。
9. ZIP 可由 Windows 资源管理器正常解压。

### 10.4 API Key 安全

桌面应用中的 API Key 最终会以可读取形式存在 `config/.env`。把 Key 打进 EXE 发布包并不能真正保密，用户或恶意程序都可能读取它。

企业发布建议：

- 使用公司 API 网关，不直接分发上游永久 Key。
- 对 Key 设置调用来源、额度、速率和有效期限制。
- 按版本或部门轮换 Key，并准备吊销流程。
- 不在 Git、日志、截图、PPT 或知识库中保存 Key。
- 如有严格权限要求，应改为服务端代理和用户鉴权，而不是继续在桌面端隐藏 Key。

## 11. 常见故障排查

### 11.1 源码版提示找不到 Python

全新 Git clone 不含 `runtime/`。安装 Python 3.11+ 和 Python Launcher，再运行 `setup_env.bat`。

### 11.2 启动后显示知识库未构建

检查 `data/index/chunks.json` 和 `vectors.npy`，然后运行构建脚本。不要从其他电脑只复制其中一个文件。

### 11.3 API 401 或模型不可用

检查 `config/.env` 的 Key、Base URL 和模型名。关闭并重启应用。即使 API 失败，本地来源检索仍应可用。

### 11.4 修改资料后没有生效

等待监听状态完成自动重建，或展开右侧资料栏点击“重建索引”。修改的是 `wavEDA_docs/` 时必须手动重建。

### 11.5 PDF 导入为空

PDF 可能是扫描图片或字体编码特殊。当前没有 OCR，应先用受控工具转成可校对 Markdown，再入库。

### 11.6 回答没有图片

检查文档图片相对路径、图片扩展名、WavEDA 路径和文件是否存在。保存路径设置后重启应用。

### 11.7 EXE 无法保存设置或会话

把整个应用目录移到用户有写权限的位置；不要只移动 EXE，也不要在 ZIP 内运行。

### 11.8 EXE 没有日志

当前 PyInstaller 配置为 `console=False`，也没有正式滚动日志文件。维护排障时优先从源码用 `python.exe` 复现。若进入公司长期运维，应增加按级别、脱敏和容量轮转的文件日志。

### 11.9 更新代码后界面或检索行为没有变化

关闭所有应用窗口，再到任务管理器确认没有旧的 `WavEDA_Assistant.exe` 或运行 `app/desktop_app.py` 的 `pythonw.exe`。旧进程会继续使用启动时加载的代码和索引；结束后重新启动。若只更新了知识源，再执行一次手动重建。

### 11.10 回答引用了不相关内容

先在右侧来源栏确认实际命中的文档。把过于宽泛的 FAQ 标题改成具体的“对象 + 动作”问题，补充用户常用同义词，并检查 priority 是否被错误设得过高。重建后用 `scripts/debug_retrieval.py` 或典型问题复测，不要只靠修改 Prompt 掩盖检索问题。

## 12. 当前边界和待改进项

- 本地哈希向量强调零下载和可便携，不等同于高质量语义 embedding。
- 当前检索是 NumPy 线性扫描，适合数千到低数万 chunk，未针对超大库设计。
- 临时文档只使用前 3000 字符，不适合整本手册问答。
- 图片上传不是真正的生产级多模态调用。
- 扫描 PDF 没有 OCR。
- 没有用户登录、角色权限、审计日志、配置加密和自动更新。
- API Key 保存在本地明文配置。
- 知识正确性依赖人工审核；RAG 只能提高可追溯性，不能保证答案绝对正确。
- `kb_sources.yaml` 尚未接入生产 builder。
- 纠错入口会修改高优先级 FAQ，交付后应增加审核状态或审批流程。
- 当前没有稳定的应用内诊断日志和崩溃报告。

## 13. 建议的公司维护流程

1. 需求进入：区分知识更新、界面功能、检索质量、模型接入和发布问题。
2. 建分支：不要直接在 `main` 上开发。
3. 修改源文件或代码，并同步文档和测试。
4. 知识变更由 WavEDA 专业人员审核；代码变更由开发人员评审。
5. 运行全套单元测试、索引构建和冒烟测试。
6. 合并到 `main` 后生成候选 EXE ZIP。
7. 在干净电脑/目录做发布验收。
8. 记录版本号、Git commit、知识库构建时间、模型配置和发布 Key 标识。
9. 保留上一稳定 ZIP 和对应 commit，出现问题时整体回滚，不手工拼接旧索引。

## 14. 交接清单

- [ ] 接收人能解释临时附件和永久入库的区别。
- [ ] 接收人能从 GUI 导入并验证一份资料。
- [ ] 接收人能按目录规范直接新增 Markdown。
- [ ] 接收人能重建索引并读懂构建报告。
- [ ] 接收人能运行测试、冒烟和检索调试。
- [ ] 接收人知道 `.env`、会话、收藏和索引的 Git 策略。
- [ ] 接收人知道 `runtime/` 不随 Git clone 提供。
- [ ] 接收人知道 `add_document.py` 和 `kb_sources.yaml` 的当前边界。
- [ ] 接收人能修改 GUI、i18n、Prompt、模型提供商和文档格式入口。
- [ ] 接收人能构建并在干净目录验收 EXE ZIP。
- [ ] 公司已明确 API Key 网关、额度、轮换和吊销责任。
- [ ] 公司已指定 WavEDA 专业内容审核人和软件维护负责人。

## 15. 相关文档

- 项目快速开始：`README.md`
- EXE 用户说明：`README-EXE.md`
- 知识库完整结构：`KNOWLEDGE_BASE_STRUCTURE.md`
- 多物理场资料规范：`KNOWLEDGE_BASE_CONTRIBUTION_GUIDE.md`
- 后续技术方向：`ROADMAP.md`
