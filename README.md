# WavEDA RAG — 多物理场仿真知识库助手

[![Python](https://img.shields.io/badge/python-3.14-blue)]()
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)]()
[![Version](https://img.shields.io/badge/version-1.0-orange)]()
[![License](https://img.shields.io/badge/license-Internal-red)]()

一个便携的本地 RAG（检索增强生成）问答系统，帮助用户快速解决 WavEDA 仿真软件的操作问题。**解压即用，无需安装 Python。**

## 快速开始

```bash
# 1. 下载
点击绿色 "<> Code" → Download ZIP → 解压

# 2. 启动
双击 start.bat

# 3. 配置 API
左侧点击 "API 设置" → 下拉选择大模型 → 输入你自己的 Key → 保存

# 4. 提问
在输入框输入问题，如"波端口怎么设置？"
```

> 内置 Python 运行时和知识库索引，不需要联网下载任何模型。

## 能做什么

- 问 WavEDA 怎么用（端口设置、边界条件、激励源、求解器……）→ 自动检索帮助文档回答
- 问电磁理论（Maxwell 方程、PML、有限元……）→ 检索理论笔记补充背景
- 支持 Markdown 渲染、LaTeX 公式显示
- 每条回答标注来源文档，可追溯

## 怎么用

1. 双击 `start.bat` 启动桌面工作台
2. 打开后点左侧 **"API 设置"** → 下拉选择大模型 → 输入你自己的 API Key → 保存
3. 在输入框里用明确的术语提问，例如：
   - `波端口怎么设置？`
   - `PML 和吸收边界有什么区别？`
   - `如何设置平面波激励？`

## 支持的大模型

| 提供商 | 需要什么 |
|------|------|
| DeepSeek | DeepSeek API Key |
| Kimi (Moonshot) | Moonshot API Key |
| 千问 / 百炼 (阿里云) | 阿里云百炼 API Key |
| OpenAI | OpenAI API Key |

在界面的 API 设置里一键切换，**不需要手动填网址和模型名**。

## 项目结构

```
waveda_rag/
├── start.bat                        # 双击启动
├── app/desktop_app.py               # 桌面应用入口
├── knowledge_base/                  # 团队自编教程（Markdown）
│   ├── 00_软件概述.md
│   ├── 01_快速入门.md
│   ├── 03_常见问题FAQ.md
│   ├── 04_错误排查指南.md
│   └── tutorials/
│       ├── 02_电磁模块/             # 端口、激励、边界、求解器、后处理
│       └── 03_案例/                 # 微环谐振器、Y分支波导
├── wavEDA_docs/                     # WavEDA 软件文档
│   ├── extracted_pages/             # 帮助页（Markdown）
│   ├── helpHtml/                    # 官方 HTML 帮助
│   ├── examples/                    # 案例库
│   └── error_cases/                 # 错误排查
├── data/index/                      # 知识库索引（向量 + 知识块）
├── config/
│   ├── .env                         # API Key（本地，不提交）
│   └── kb_sources.yaml             # 知识库数据源配置
├── scripts/
│   ├── add_document.py              # 单文档增量追加
│   └── smoke_test.py                # 基础问答验证
└── src/raggg/                       # RAG 引擎核心
    ├── desktop/                     # PySide6 深色界面
    ├── retrieval/                   # 混合检索（向量 + 关键词）
    ├── generation/                  # LLM 调用与提示词
    └── indexing/                    # 本地哈希向量
```

## 开发指南

### 安装（开发者）

本项目内置 Python 运行时，无需额外安装 Python。如果要开发：

```bash
pip install PySide6 numpy
```

### 更新知识库

在 `knowledge_base/` 下写好新 Markdown 文档，然后：

```bash
runtime/python/python.exe scripts/add_document.py knowledge_base/新文档.md
```

在界面上点 **"重新载入索引"** 即可，不需要重启。

### API Key 配置

API Key 存在 `config/.env` 中（已加入 `.gitignore`，不会泄露）。也可以在界面上直接配置。

## 当前版本

- **v1.0** — 知识库 1908 个知识块，覆盖 WavEDA 电磁模块 + 多物理场理论
- 检索方式：本地哈希向量 + 关键词混合检索
- 界面：PySide6 深色桌面工作台

## 许可证

内部项目，仅供团队使用。
