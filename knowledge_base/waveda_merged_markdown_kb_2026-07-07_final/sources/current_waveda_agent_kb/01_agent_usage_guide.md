---
title: "Agent 使用指南"
merged_source: "current_waveda_agent_kb"
source_relative_path: "01_agent_usage_guide.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\01_agent_usage_guide.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# Agent 使用指南

## 回答定位

这个知识库的目标用户是 WavEDA 新手。回答应优先给出“该点哪里、为什么、怎么做、出错怎么办”的可执行说明，而不是只复述文档。

## 推荐回答结构

- 入口位置：说明菜单、工程树、工具栏或右键位置。
- 操作步骤：按 1、2、3 列出最短路径。
- 参数含义：解释用户会看到的关键字段。
- 适用场景：说明什么时候应该用这个功能。
- 常见限制：列出必须满足的条件。
- 排错建议：告诉用户去哪里看日志、如何缩小问题。
- 来源追溯：引用 `10_extracted_pages` 中的具体页面。

## 检索优先级

1. 新手流程、仿真方法、排错等综合问题：先查 `30_topic_cards`。
2. 按钮/入口/右键菜单：先查 `20_indexes/button_location_function_index.md`。
3. 某个具体功能名：查 `20_indexes/module_page_index.md` 后进入抽取页。
4. 真实报错、弹窗、日志文案：先查 `40_error_cases/error_message_index.md`，再查 `error_message_index.csv`。
5. 示例模型、案例参数、类似工程：先查 `40_example_cases/index.md`，再进入对应案例页。
6. 材料参数：先查 `50_material_library/materials.md` 或 `material_index.csv`。
7. 电路元件：先查 `60_circuit_components/component_index.md`。
8. 图标识别：先查 `70_ui_icons/toolbar_icon_index.md`。
9. 图片定位：抽取页的“图片资源”保留了原始截图路径，可打开原图核对按钮位置。

## 回答边界

第一版主要来自官方帮助文档。原文中没有完整的报错代码库，因此遇到具体报错时应：

- 先让用户提供完整日志文本、操作步骤、模型设置和截图。
- 用 `40_error_cases/error_message_index.md` 匹配真实文案，再用 `troubleshooting_and_constraints.md` 中的“限制/必须/不支持”规则做初筛。
- 明确区分“文档明确说明”和“根据限制推断”。
