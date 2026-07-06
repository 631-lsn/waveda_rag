# WavEDA + 多物理场笔记 RAG

这是一个独立放在 `D:\RAGGG` 的本地 RAG 系统，用于合并检索两类资料：

- WavEDA 本地帮助文档：`D:\Program Files (x86)\documentation\helpHtml`
- Obsidian 多物理场学习笔记：`D:\暑期实践\多物理场仿真知识库`

系统重点服务 WavEDA 软件使用问题。涉及端口、边界、PML、网格、激励源、3D 几何建模、仿真设置等问题时，会优先检索 WavEDA 帮助文档；Obsidian 笔记主要用于补充电磁场、有限元、吸收边界等理论背景。

## 当前能力

- 合并 WavEDA HTML 帮助文档和 Obsidian Markdown 笔记。
- 构建本地知识库索引。
- 使用 WavEDA 优先的混合检索排序。
- 支持 DeepSeek / OpenAI 兼容接口生成回答。
- 未配置 API Key 时也能返回本地检索片段式回答。
- 提供 PySide6 深色桌面工作台。
- 回答中支持基础 Markdown 渲染：加粗、编号列表、项目列表。
- 回答中支持常见 LaTeX 公式可读化渲染，例如 `\oiint`、`\iiint`、`\frac`、`\partial`、`\rho_f` 等。
- 右侧显示来源证据、来源类型、文件路径和匹配分数。

## 项目结构

```text
D:\RAGGG
  app\
    desktop_app.py              # 桌面应用入口
  data\
    raw_manifest.json           # 原始文档清单
    processed_chunks.json       # 预处理后的知识块
    index\
      chunks.json               # 检索用知识块
      vectors.npy               # 本地向量
  docs\
    user_guide.md               # 使用说明
    progress\                   # 进度记录与截图
    superpowers\                # 设计文档与实施计划
  scripts\
    build_knowledge_base.py     # 构建知识库
    smoke_test.py               # 基础问答验证
    debug_retrieval.py          # 检索排序诊断
  src\raggg\
    loaders\                    # HTML / Markdown 读取
    preprocessing\              # 清洗与切块
    indexing\                   # 本地向量与索引
    retrieval\                  # 检索排序
    generation\                 # 模型调用与提示词
    pipeline\                   # 构建和问答管线
    desktop\                    # PySide6 桌面界面
  tests\                        # 自动测试
  .env                          # 本地配置，不要公开
  .env.example                  # 配置模板
  requirements.txt
```

## 环境准备

项目使用本地虚拟环境：

```text
D:\RAGGG\.venv
```

已安装主要依赖：

- `numpy`
- `PySide6`

如需重新安装依赖：

```powershell
cd /d D:\RAGGG
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## API Key 配置

复制配置模板：

```powershell
cd /d D:\RAGGG
Copy-Item .env.example .env
notepad .env
```

DeepSeek 示例：

```text
RAG_LLM_BASE_URL=https://api.deepseek.com
RAG_LLM_API_KEY=你的API密钥
RAG_LLM_MODEL=deepseek-chat
```

OpenAI 兼容接口示例：

```text
RAG_LLM_BASE_URL=https://api.openai.com/v1
RAG_LLM_API_KEY=你的API密钥
RAG_LLM_MODEL=gpt-4o-mini
```

注意：`.env` 中包含密钥，不要公开、提交或截图发送。

## 构建知识库

```powershell
cd /d D:\RAGGG
.\.venv\Scripts\python.exe scripts\build_knowledge_base.py
```

当前一次成功构建结果：

```text
documents=201
waveda_documents=97
obsidian_documents=104
chunks=1408
data_dir=D:\RAGGG\data
```

构建后会生成：

```text
D:\RAGGG\data\raw_manifest.json
D:\RAGGG\data\processed_chunks.json
D:\RAGGG\data\index\chunks.json
D:\RAGGG\data\index\vectors.npy
```

## 启动桌面工作台

```powershell
cd /d D:\RAGGG
py -3 app\desktop_app.py
```

启动脚本会自动切换到 `D:\RAGGG\.venv` 中的 PySide6 环境。

界面分为三块：

- 左侧：知识库状态、知识块数量、模型状态、快捷问题。
- 中间：问答区。
- 右侧：来源证据卡片。

## 常用验证命令

运行完整测试：

```powershell
cd /d D:\RAGGG
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

运行基础问答 smoke test：

```powershell
.\.venv\Scripts\python.exe scripts\smoke_test.py
```

诊断检索排序：

```powershell
.\.venv\Scripts\python.exe scripts\debug_retrieval.py
```

当前测试状态：

```text
24 tests passed
```

## WavEDA 优先规则

系统对 WavEDA 问题做了专门排序优化：

- 查询中出现具体 WavEDA 对象名时，标题精确命中的 WavEDA 帮助页强优先。
- 例如 `怎么设置棱柱？` 会优先返回 `Modeling/Create_3D_Geometry/Prism.html`。
- `波端口`、`点激励源`、`平面波`、`PML`、`边界` 等软件术语会优先匹配 WavEDA 文档。
- `设计设置`、`建模`、`选项` 等泛页面不会因为“设置”这类泛词压过具体对象页面。
- 纯理论问题会更多使用 Obsidian 笔记，例如 Maxwell 方程、吸收边界条件、有限元概念等。

## 已修复的问题

- 桌面界面从基础 `tkinter` 升级为 PySide6 深色工作台。
- 模型回答中的 `**加粗**` 不再裸露，已渲染为富文本。
- 常见 LaTeX 公式不再显示成 `oiint_S`、`\frac`、`\partial` 这类原始字符。
- `怎么设置棱柱？` 这类问题不再被“设计设置”泛页面带偏。

## 当前限制

- 第一版使用本地哈希向量和关键词混合检索，稳定、无需下载 embedding 模型，但语义检索能力弱于真正的 BGE / FAISS 向量方案。
- LaTeX 公式渲染是轻量转换，不是完整 MathJax 引擎。常见电磁公式能正常显示，但复杂矩阵、分段函数、长推导可能仍需后续增强。
- 当前知识库更新需要手动运行构建脚本，尚未开启自动监听原始文档变化。

## 推荐使用方式

1. 先运行 `build_knowledge_base.py` 构建知识库。
2. 启动桌面工作台。
3. 优先用明确的软件对象提问，例如：
   - `怎么设置棱柱？`
   - `波端口积分线怎么设置？`
   - `平面波激励怎么设置？`
   - `PML 和吸收边界有什么关系？`
4. 需要排查检索问题时运行 `debug_retrieval.py`。
