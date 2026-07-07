---
title: "WavEDA 使用教导 Agent 知识库（第一版）"
merged_source: "current_waveda_agent_kb"
source_relative_path: "00_README.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\00_README.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# WavEDA 使用教导 Agent 知识库（第一版）

本目录由 `D:\Staid\app\waveda\documentation` 下的 WavEDA 帮助文档首次提炼生成，目标是服务“新手使用教导 Agent”：回答按钮位置、功能解释、仿真流程、仿真方法差异、常见限制与排错方向等问题。

## 目录结构

- `00_README.md`：本说明。
- `01_agent_usage_guide.md`：给后续 Agent/RAG 使用的回答策略。
- `20_indexes/`：索引层，适合检索入口和导航。
- `30_topic_cards/`：面向新手问答的专题卡片。
- `40_error_cases/`：从软件翻译文件抽取的真实 UI 报错、警告和弹窗文案。
- `40_example_cases/`：从 `Example` 目录抽取的案例教程、工程摘要和截图路径。
- `50_material_library/`：内置材料库索引和材料选择指南。
- `60_circuit_components/`：电路组件、显示名、提示和图标路径。
- `70_ui_icons/`：工具栏图标文件名和初步功能分类。
- `10_extracted_pages/`：从原始 HTML 逐页抽取的 Markdown，保留原始来源与图片路径。
- `90_maintenance_templates/`：后续补充报错、按钮、案例时可直接复制的模板。
- `_source_manifest.jsonl`：每页来源、模块、图片数量、抽取文件路径清单。
- `_extract_waveda_kb.py`：本次提炼脚本，后续可复用刷新知识库。
- `_extract_waveda_extra_sources.py`：非 documentation 资源增量提炼脚本。

## 已抽取范围

- 原始 HTML 页数：98
- 图片未复制入库，Markdown 中保留原始图片绝对路径，避免第一版知识库过大。

## 模块页数

- `EM_Project`（EM设计与结果）：15 页
- `Simulation`（仿真）：2 页
- `Post_Processing`（后处理）：3 页
- `helpHtml`（基础介绍）：2 页
- `Tool`（工具）：7 页
- `Modeling`（建模总览）：57 页
- `File`（文件与主页）：3 页
- `Mesh`（网格）：7 页
- `View`（视图）：2 页

## 使用建议

1. 新手问答优先检索 `30_topic_cards/`，再回到 `10_extracted_pages/` 查源文。
2. 涉及“按钮在哪里”的问题，优先查 `20_indexes/button_location_function_index.md`。
3. 涉及“为什么不能仿真/报错如何解决”，优先查 `30_topic_cards/troubleshooting_and_constraints.md`。
4. 涉及“仿真方法怎么选”，优先查 `30_topic_cards/simulation_methods_comparison.md`。
5. 涉及“有没有类似案例/参数怎么设”，优先查 `40_example_cases/index.md`。
6. 涉及真实报错文本，优先查 `40_error_cases/error_message_index.md` 和 `error_message_index.csv`。
7. 涉及材料参数，优先查 `50_material_library/materials.md` 和 `material_index.csv`。
8. 如果后续收集到用户真实排错过程，请继续补到 `90_maintenance_templates/error_case_template.md` 或 `40_error_cases/`。
