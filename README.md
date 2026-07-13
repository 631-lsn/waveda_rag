# WavEDA RAG 新手教学 Agent

这是一个面向 WavEDA 初学者的本地 RAG 问答工具。它会优先检索项目内置的 WavEDA 教程、官方帮助文档、案例和常见错误排查资料，再结合大模型生成更适合新手阅读的回答。

## 第一次使用

Windows 用户按下面三步来：

1. 双击 `setup_env.bat`
   - 优先使用项目内置的 `runtime/python`
   - 如果没有内置 Python，才会自动创建本地虚拟环境 `.venv` 并安装依赖
   - 自动构建本地知识库索引 `data/index`
   - 最后会跑一次基础问答验证

2. 配置 API Key（可选，但推荐）
   - GitHub 上只会同步 `config/.env.example`，不会同步 `config/.env`
   - 如果要使用大模型回答，请复制一份 `config/.env.example`，改名为 `config/.env`
   - 打开 `config/.env`，把 `RAG_LLM_API_KEY=` 后面改成自己的 API Key
   - 不知道怎么填也可以先跳过；没有 API Key 时仍然可以使用本地知识库检索

3. 双击 `start.bat`
   - 打开 WavEDA Knowledge Workbench 桌面界面
   - 第一次提问前，可以在左侧点击 `API 设置`，填入自己的 API Key

界面采用 React + TypeScript + Tailwind CSS，并按 shadcn 约定组织组件。`setup_env.bat` 会自动构建静态前端；日常运行不需要单独启动 Node.js 或 Web 服务。

如果你不确定有没有安装好，双击 `run_smoke_test.bat`。它会跑三条基础问题，能看到来源说明就表示核心检索链路正常。

## 需要提前准备什么

- Windows 10/11
- 正常从 GitHub 下载完整仓库时，不需要提前安装 Python
- 如果你的版本里缺少 `runtime/python`，则需要安装 Python 3.11 或更新版本，并确保本机有 Python 启动器 `py`

如果双击 `setup_env.bat` 时提示找不到内置 Python，也找不到 `py`，请先安装 Python 3.11 或更新版本，并勾选 “Add python.exe to PATH” 或安装 Python Launcher。

## 能做什么

- 回答 WavEDA 基础操作问题，例如端口设置、边界条件、激励源、求解器、后处理等
- 回答常见错误和排查问题，例如端口与 PML 冲突、模型设置不完整、结果异常等
- 检索案例、官方帮助、团队自编教程，并在回答中显示来源
- 在桌面界面中导入 `.md`、`.html`、`.txt`、`.pdf`、`.docx` 资料并自动重建本地索引
- API 不可用时，仍然可以基于本地知识库片段给出保底回答

## 支持的大模型

界面左侧的 `API 设置` 支持切换：

| 提供商 | 需要填写 |
| --- | --- |
| DeepSeek | DeepSeek API Key |
| Kimi / Moonshot | Moonshot API Key |
| 通义千问 / 百炼 | 阿里云兼容接口 API Key |
| OpenAI | OpenAI API Key |

API Key 保存在本地 `config/.env`，不会提交到 Git。

## 项目结构

```text
waveda_rag/
├─ setup_env.bat                  # 第一次使用：安装环境 + 构建索引
├─ start.bat                      # 日常启动桌面应用
├─ run_smoke_test.bat             # 验证检索和问答链路
├─ app/desktop_app.py             # 桌面应用入口
├─ frontend/                      # React + TypeScript 前端
│  ├─ src/components/ui/          # shadcn 共享组件默认目录
│  ├─ src/index.css               # Tailwind 与全局主题样式
│  └─ dist/                       # PySide6 加载的生产构建
├─ src/raggg/                     # RAG 核心代码
│  ├─ desktop/                    # PySide6 桌面壳与 QWebChannel 桥接
│  ├─ generation/                 # 提示词和大模型调用
│  ├─ indexing/                   # 本地向量索引
│  ├─ loaders/                    # Markdown / HTML 文档读取
│  ├─ pipeline/                   # 构建与问答流水线
│  └─ retrieval/                  # 检索逻辑
├─ knowledge_base/                # 融合后的 Markdown 知识库
├─ wavEDA_docs/                   # WavEDA 官方帮助、案例、图片、错误信息
├─ data/index/                    # 本地生成的索引，不提交 Git
├─ config/.env                    # 本地 API 配置，不提交 Git
└─ requirements.txt               # Python 依赖
```

## 前端开发与重新构建

项目没有依赖系统全局 Node.js。运行以下命令会优先使用已有 Node.js，否则把官方 Windows x64 LTS 运行时下载到 Git 已忽略的 `.tmp/`：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\build_frontend.ps1
```

前端默认组件路径是 `frontend/src/components/ui/`，并通过 `@/components/ui` 导入。保留这个目录对 shadcn CLI 很重要，因为 `frontend/components.json` 的组件生成、别名解析和后续升级都依赖该约定。全局样式默认位于 `frontend/src/index.css`。

## 知识库说明

当前主要知识库位于：

```text
knowledge_base/
```

它融合了：

- 现有 WavEDA agent 知识库
- 新版 waveda_rag 自编教程
- WavEDA 操作教学型 Agent 知识库
- 用户补充资料

`setup_env.bat` 会把这些 Markdown 文档和 `wavEDA_docs/helpHtml/helpHtml` 中的官方 HTML 帮助一起构建成本地索引。

## 回答中的图片

桌面端回答会优先调用项目内已有图片，例如后续补充到 `knowledge_base/assets/images`、`assets/images` 或当前项目自带的 `wavEDA_docs/helpHtml/helpHtml` 图片。

案例库中的图片先以 `待补图片清单` 形式保留候选项，路径写成 WavEDA 安装目录下的相对路径，例如 `Example/EM/Antenna/.../res/xxx.png`。运行时 agent 会根据用户在 `config/.env` 中填写的本机 WavEDA 路径去查找。

如果新人电脑上安装了 WavEDA，可以在 `config/.env` 里设置自己的安装路径作为兜底图片来源：

```env
WAVEDA_ROOT=D:\Program Files\WavEDA
```

也可以只设置帮助文档目录或案例目录：

```env
WAVEDA_HELP_ROOT=D:\Program Files\WavEDA\documentation\helpHtml
WAVEDA_EXAMPLE_ROOT=D:\Program Files\WavEDA\Example
```

不同电脑的安装路径可以不同，只需要改自己的 `config/.env`，不要提交这个文件。知识库里建议写相对路径，例如 `EM_Project/images/xxx.png`、`wavEDA_docs/helpHtml/helpHtml/EM_Project/images/xxx.png` 或 `Example/.../res/xxx.png`，程序会自动按“项目内图片优先，本机 WavEDA 图片兜底”的顺序查找。本机帮助文档路径通常只到一层 `helpHtml`，项目内的 `wavEDA_docs/helpHtml/helpHtml` 是仓库打包后的内部路径。

## 更新知识库后

如果新增或修改了知识库文档，运行：

```powershell
.\runtime\python\python.exe -B scripts\build_knowledge_base.py
```

如果当前版本没有 `runtime/python`，但已经通过 `setup_env.bat` 创建了 `.venv`，也可以运行：

```powershell
.\.venv\Scripts\python.exe -B scripts\build_knowledge_base.py
```

最简单的方式仍然是重新双击 `setup_env.bat`，它会重新构建索引。

桌面界面左侧也提供 `导入资料入库` 按钮，可选择单个 `.md`、`.markdown`、`.html`、`.htm`、`.txt`、`.pdf` 或 `.docx` 文件。导入文件会保存到 `knowledge_base/05_reference/imported/`，随后自动重建索引并重新载入。

软件运行时会自动监听 `knowledge_base/` 下的支持格式文件。手动修改、增加或删除这些文件后，界面会在文件稳定后自动后台重建索引并重新载入；重建期间提问和导入按钮会暂时禁用。

## 常见问题

### 双击 start.bat 没反应

先双击 `setup_env.bat`。如果还不行，再双击 `run_smoke_test.bat` 看具体错误。

### setup_env.bat 安装依赖失败

如果项目内置的 `runtime/python` 存在，通常不会走联网安装依赖。只有缺少内置 Python、需要创建 `.venv` 时，才可能因为网络问题安装失败。可以换网络后再运行一次；脚本会先使用默认 pip 源，失败后自动尝试清华 PyPI 镜像。

### 没有 API Key 能不能用

可以。没有 API Key 时，工具仍然能检索本地知识库并给出片段式回答；只是不会调用大模型润色和综合。

### data/index 为什么不提交 Git

它是本地生成的索引文件，体积会变大，而且可以由知识库重新构建。协作时提交源文档和代码即可，索引用 `setup_env.bat` 生成。
