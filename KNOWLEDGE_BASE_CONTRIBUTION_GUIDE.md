# WavEDA 多物理场知识库放置指南

## 1. 先判断资料类型，再判断物理场

知识库采用两个维度：

1. 顶层目录表示资料类型，例如团队教程、软件手册、案例、错误、参考资料和理论资料。
2. 顶层目录内部再按物理场或软件模块分类。

不要为同一份资料制作多个副本。跨物理场资料放入“多物理场耦合”，并通过 Markdown 链接引用相关单物理场文档。

## 2. 顶层目录职责

| 目录 | 应放内容 | 不应放内容 |
| --- | --- | --- |
| `01_team_tutorials` | 已人工验证的操作步骤、FAQ、新手工作流 | 未核实的原始手册摘录 |
| `02_software_manual` | 按 WavEDA GUI 和版本整理的软件功能说明 | 大段理论推导、个人实验记录 |
| `03_examples` | 可复现案例、工程参数、结果与检查点 | 只有概念而没有仿真流程的文章 |
| `04_error_cases` | 报错原文、触发条件、原因、处理步骤 | 普通教程和软件概述 |
| `05_reference` | 材料、按钮、模块、术语和外部资料索引 | 完整操作教程的重复副本 |
| `06_theory_notes` | 公式、物理背景、数值方法、教材与论文笔记 | 与 WavEDA 无关且无法支持仿真的泛科普 |

## 3. 物理场目录

| 物理场 | 团队教程 | 软件手册 | 案例 | 理论资料 |
| --- | --- | --- | --- | --- |
| 电磁与射频 | `tutorials/01_电磁模块` | `EM_Project` | `EM` | `01_电磁与射频` |
| 光子与波导 | `tutorials/04_光子与波导模块` | `Photonics_Waveguide` | `Photonics` | `02_光子与波导` |
| 电路与系统 | `tutorials/03_电路模块` | `Circuit_Project` | `Circuit` | `03_电路与系统` |
| 热学 | `tutorials/05_热学模块` | `Thermal_Project` | `Thermal` | `04_热传导与热可靠性` |
| 结构力学 | `tutorials/06_力学与声学模块` | `Mechanical_Acoustic` | `Mech` | `05_结构力学` |
| 声学、弹性波、压电 | `tutorials/06_力学与声学模块` | `Mechanical_Acoustic` | `Acoustic_Piezoelectric` | `06_声学与弹性波`、`07_压电与机电耦合` |
| 多物理场耦合 | `tutorials/07_多物理场耦合` | `MultiPhysics_Project` | `Multi-Physics` | `08_多物理场耦合` |
| 版图与封装 | `tutorials/08_版图与封装` | `Layout_Packaging` | `Layout_Packaging` | `09_版图封装与可靠性` |
| 共通建模与数值方法 | 放入对应操作模块 | `Modeling`、`Mesh`、`Simulation` | 按主要物理场放置 | `00_通用建模与数值方法` |

“光子与波导”是知识领域分类，不表示它一定是独立的软件求解器；具体页面仍应写明所使用的 WavEDA 模块和求解方法。

## 4. 新文档 Frontmatter

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

- `physics_domain` 建议使用：`em_rf`、`photonics`、`circuit`、`thermal`、`mechanical`、`acoustic`、`piezoelectric`、`multiphysics`、`layout_packaging`、`common`。
- `priority` 为 1 到 5；只有经过验证且适合新手优先采用的内容才使用 4 或 5。
- 框架占位说明使用 `indexing: false`，不会进入 Agent 检索。
- 草稿可以进入 Git，但未经验证的关键参数、菜单路径和结论必须标注“待确认”。

## 5. 推荐文档结构

1. 适用模块和软件版本。
2. 使用场景与前置条件。
3. GUI 路径和逐步操作。
4. 参数含义、默认建议与适用范围。
5. 运行前检查项。
6. 结果判断方法。
7. 常见错误与限制。
8. 来源、验证人和验证日期。

## 6. 图片与路径

- 优先使用项目内图片的相对路径。
- 本机 WavEDA 帮助图片使用配置后的 WavEDA 根目录解析，不在文档中写个人电脑绝对路径。
- 图片必须辅助识别选项界面、按钮位置、图例或结果，不能代替关键文字步骤。

## 7. 合入前检查

- 文档位置与主要物理场一致。
- 菜单路径和参数名称已在对应版本中核实。
- 单位、材料、边界、激励、求解器和结果含义写清楚。
- 没有 API Key、个人绝对路径或临时聊天记录。
- 执行 `python scripts/build_knowledge_base.py` 后无异常，并用至少一个典型问题检查检索结果。
