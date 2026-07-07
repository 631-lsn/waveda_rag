---
title: "WavEDA 非 documentation 资源蒸馏盘点"
merged_source: "current_waveda_agent_kb"
source_relative_path: "02_non_document_source_inventory.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\02_non_document_source_inventory.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# WavEDA 非 documentation 资源蒸馏盘点

本文件记录对 `D:\Staid\app\waveda` 中除 `documentation` 以外资源的首次盘点结果，用于规划第二轮知识库蒸馏。

## 结论

最值得继续蒸馏的资源有四类：

1. `Example/`：案例教程、工程文件、截图资源。适合补成“按案例上手”的教学库。
2. `resources/language/*.ts`：真实 UI 文案和报错翻译。适合补成“报错原因与处理建议”库。
3. `library/material/waveda_material.lib`：材料库。适合补成“材料参数速查”和“如何选材料”知识。
4. `resources/component/` 与 `resources/icons/toolbar/`：电路元件、工具栏图标和按钮资源。适合补成“按钮图标识别”和“电路元件说明”知识。

DLL、Qt 插件、WebEngine 资源、卸载程序、许可程序等运行时文件不适合直接蒸馏为教学知识，只保留为安装/环境排错的背景信息即可。

## 资源概览

顶层目录中，除 `documentation` 外主要包括：

- `Example`：案例工程与教程。
- `library`：材料库、数学库、ngspice 动态库。
- `module_description` 与 `resources/module_description`：模块介绍文案。
- `resources`：组件图标、工具栏图标、样式、语言翻译、模块描述。
- `translations`：Qt/WebEngine 翻译资源，教学价值低于 `resources/language`。
- `iconengines`、`imageformats`、`platforms`、`sqldrivers`、`tls` 等：Qt 运行时插件，通常不进入教学知识库。

## 1. Example 案例库

路径：`D:\Staid\app\waveda\Example`

统计：

- 30 个 `.html` 案例说明页。
- 30 个 `.tsp` 工程文件。
- 291 张 `.png`、36 张 `.jpg`、4 张 `.gif` 案例截图。
- 案例按一级目录分布：`Circuit` 3 个，`EM` 15 个，`Mech` 3 个，`Multi-Physics` 6 个，`Thermal` 3 个。

可蒸馏内容：

- 每个案例的目标、适用场景、模型尺寸、材料、边界条件、激励、频率范围、网格设置、后处理结果。
- `.html` 中的图文步骤可转为“案例任务流程卡”。
- `.tsp` 是 XML 风格工程文件，可抽取变量、单位、求解器、频率、Domain、材料、几何对象、端口/激励、远场/结果设置。
- 截图资源可保留原路径或挑选核心图复制入多模态知识库。

优先蒸馏建议：

1. 先蒸馏 `EM` 下 15 个案例，因为它最贴近当前 WavEDA 新手仿真 Agent 的主目标。
2. 再蒸馏 `Circuit`，补充电路器件与端口/仿真器使用。
3. 最后处理 `Thermal`、`Mech`、`Multi-Physics`，扩展到多物理场教学。

建议输出目录：

- `40_example_cases/`
- `40_example_cases/index.md`
- `40_example_cases/em/`
- `40_example_cases/circuit/`
- `40_example_cases/thermal_mech_multiphysics/`

注意：

- 部分 `.tsp` 用标准 XML 解析会失败，需要容错解析或基于标签正则抽取。不要直接丢弃解析失败的工程。

## 2. 语言翻译与真实报错文本

路径：`D:\Staid\app\waveda\resources\language`

统计：

- `st_Chinese.ts`：约 11478 条消息。
- `st_core_Chinese.ts`：约 1073 条消息。
- `st_cad_Chinese.ts`：约 298 条消息。
- `st_mesher_Chinese.ts`：约 121 条消息。
- `st_simulator_Chinese.ts`：约 82 条消息。
- 初筛含“失败、错误、无法、不能、不允许、请检查、警告”等中文提示的消息约 1078 条。

可蒸馏内容：

- 真实 UI 菜单项、按钮项、弹窗文本。
- 真实报错文本及其中文翻译。
- 验证失败、建模失败、网格失败、端口失败、导入导出失败等排错入口。

已发现的典型报错文本：

- `创建波端口失败，所选面不是平面。`
- `创建波端口失败，所选面不在同一平面。`
- `仿真过程中不允许创建波端口。`
- `所选信息为空，不能创建集总元件。`
- `波端口%1：波端口内导体数量已更改，请在波端口对话框中重置电势。`
- `波端口%1：波端口全部连接在金属上。`
- `仿真前参数校验失败。`
- `错误：准备仿真参数失败`
- `错误：网格类型和求解器不一致`
- `波端口%1网格剖分失败`

建议输出目录：

- `40_error_cases/`
- `40_error_cases/raw_ui_messages.md`
- `40_error_cases/error_message_index.md`
- `40_error_cases/error_to_solution_mapping.md`

注意：

- 翻译文件提供的是“报错原文”，不一定提供解决办法。需要结合帮助文档限制、示例工程设置和用户真实案例补齐“原因”和“处理步骤”。

## 3. 材料库

路径：`D:\Staid\app\waveda\library\material\waveda_material.lib`

统计：

- XML 风格材料库。
- 当前可识别材料数量：76 个。

可蒸馏内容：

- 材料名称。
- 支持物理模块：EM、Thermal、Ela、Piezo。
- 电磁参数：介电常数、电导率、磁导率、损耗角正切、各向异性参数。
- 热参数：密度、比热容、导热系数。
- 弹性/声学参数：密度、速度、杨氏模量等。

适合回答的问题：

- “FR-4 / Alumina / Aluminum 该怎么选？”
- “某材料是否支持电磁/热/力学？”
- “材料参数在哪里看？”
- “为什么材料损耗角正切没有生效？”

建议输出目录：

- `50_material_library/`
- `50_material_library/material_index.csv`
- `50_material_library/materials.md`
- `50_material_library/material_selection_guide.md`

注意：

- 材料参数来自软件内置库，应标明来源路径和字段名。
- 不建议把完整 XML 原样塞进问答上下文，应转成结构化表格和重点材料卡。

## 4. 电路组件与图标资源

路径：

- `D:\Staid\app\waveda\resources\component`
- `D:\Staid\app\waveda\resources\component\componentSetting.ini`

组件分类统计：

- `Basic_icon`：23 个。
- `Source_icon`：19 个。
- `Nonlinear_icon`：45 个。
- `Amplifier_icon`：11 个。
- `Transmission line_icon`：7 个。
- `Trans formers_icon`：5 个。
- `Simulator_icon`：4 个。
- `Switch_icon`：4 个。
- `Probe_icon`：3 个。
- `File Compnents_icon`：2 个。

可蒸馏内容：

- 电阻、电容、电感、端口、电压源、电流源、探针、传输线、滤波器、非线性器件、仿真器等组件清单。
- `componentSetting.ini` 中包含组件显示名称和 tooltip 文案。
- SVG 文件名可作为组件英文名和图标路径索引。

适合回答的问题：

- “电路里 R/C/L/TermG/Probe 是什么？”
- “电路仿真用 AC、DC、SP、Trans 分别做什么？”
- “某个元件图标在哪里？”

建议输出目录：

- `60_circuit_components/`
- `60_circuit_components/component_index.md`
- `60_circuit_components/component_icon_index.csv`

## 5. 工具栏图标与按钮识别

路径：`D:\Staid\app\waveda\resources\icons\toolbar`

观察：

- 该目录含大量 `.svg`、少量 `.png/.jpg/.ico`。
- 文件名覆盖建模、网格、仿真、视图、端口、结果、导出、变量、单位、频率、材料、Domain 等常用按钮。
- 典型图标名包括：`run.svg`、`stop.svg`、`check.svg`、`clear-mesh.svg`、`run-waveport.svg`、`waveport.svg`、`lumpedport.svg`、`par_sweeping.svg`、`export-snp.svg`、`details-log.svg`、`Unit.svg`、`Frequency.svg`、`material.svg`、`DomainEdit.svg`。

可蒸馏内容：

- 按钮图标文件名到功能名的索引。
- 帮助文档中的按钮说明与图标文件的交叉索引。
- 面向新手的“看图找按钮”知识。

建议输出目录：

- `70_ui_icons/`
- `70_ui_icons/toolbar_icon_index.md`
- `70_ui_icons/icon_to_function_mapping.md`

注意：

- 图标文件名不等于界面最终显示名，需要结合翻译文件、帮助文档、截图共同校准。

## 6. 模块描述

路径：

- `D:\Staid\app\waveda\module_description`
- `D:\Staid\app\waveda\resources\module_description`

可蒸馏内容：

- EM、电路、热、力学、多物理场、Layout 等模块的官方简介。
- 适合放入 Agent 的“能力边界”和“用户该选哪个模块”说明。

示例：

- EM 模块强调混合有限元算法、自适应网格、模型降阶、边界条件、点源/平面波/集总端口/波端口、S 参数、近场/远场、快照和波端口模式。
- 多物理场模块强调电-热-力耦合、焦耳热、热膨胀、电磁力、压电效应，以及温度云图、应力云图、位移云图等后处理。

建议输出文件：

- `20_indexes/module_capability_index.md`
- `30_topic_cards/module_selection_guide.md`

## 第二轮蒸馏路线

建议按以下顺序继续：

1. 抽取 `resources/language/*.ts`，生成真实报错索引。
2. 抽取 `Example/EM`，生成 15 个 EM 案例流程卡。
3. 解析 `.tsp` 工程，给每个案例补充结构化参数摘要。
4. 抽取材料库，生成材料速查表。
5. 抽取组件和工具栏图标，补充按钮识别与电路元件索引。
6. 整合模块描述，生成模块选择指南。

## 推荐知识库结构增量

```text
waveda_agent_kb/
  40_error_cases/
  40_example_cases/
  50_material_library/
  60_circuit_components/
  70_ui_icons/
```

## 不建议优先蒸馏的内容

- `.dll`、`.exe`、`.pak`、Qt 插件目录：主要是运行时依赖，教学价值低。
- `styles`、大部分 `.qss`：主要是界面样式，除非需要做 UI 自动化定位。
- `translations/qtwebengine_locales`：通用 Qt/WebEngine 语言包，和 WavEDA 业务知识关系弱。
- `license.lic`：不要进入知识库正文，避免泄露授权信息；只可在环境排错文档中泛化说明“许可证配置相关”。
