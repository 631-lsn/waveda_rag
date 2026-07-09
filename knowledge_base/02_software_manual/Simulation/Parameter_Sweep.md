---
title: "Parameter Sweep"
merged_source: "current_waveda_agent_kb"
source_relative_path: "Simulation/Parameter_Sweep.html"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# Parameter Sweep

- 原始相对路径: `Simulation/Parameter_Sweep.html`
- 知识模块: `仿真`

## 正文抽取
## 参数化扫描

参数化扫描是指通过设置一个或多个设计参数的变化范围，软件自动生成一系列仿真任务，每次仿真都使用不同的参数值。 仿真结果（如反射系数、增益、带宽等）会随着参数的变化而变化，帮助用户深入分析设计空间，并找到最佳的设计方案。

使用参数化建模创建模型，设置激励和扫频，设置计算区域后，可以进行参数化扫描。点击主菜单栏“仿真”->“参数化扫描”图标。

> 图示要点：`Parameter_Sweep_16.png` 展示“参数化扫描”相关的操作界面或示例，后续审查通过后再补图。

注意，参数化扫描前必须在变量中添加变量，才可以调用已添加的变量，未设置变量的模型无法使用参数化扫描。

### 参数化扫描设置

> 图示要点：`Parameter_Sweep_2.png` 展示“参数化扫描设置”相关的操作界面或示例，后续审查通过后再补图。

- 选择扫描变量：在参数化扫描编辑框的选择变量下拉菜单栏中选择扫描变量。

> 图示要点：`Parameter_Sweep_.png` 展示“参数化扫描设置”相关的操作界面或示例，后续审查通过后再补图。

- 设置扫描范围：根据需求选定变量，设置变量的扫频范围以及步长、次数，也可以选择点数、对数型、任意点输入。

- 新建：点击“新建”，当前编辑的变量被新建到右侧。勾选变量前的选项框，进行参数化扫描。

- 删除： 选中右侧变量，点击“删除”，变量被删除。

- 修改：如果需要修改变量，选中变量，在左侧修改变量范围，点击“修改”，修改完成。

> 图示要点：`Parameter_Sweep_4.png` 展示“参数化扫描设置”相关的操作界面或示例，后续审查通过后再补图。

- 参数设置列表：在设置多个扫描变量后，点击“上移”、“下移”按键，修改变量的排序，软件会根据排序按顺序扫描变量，该操作对结果无影响。

- 验证：在添加完成之后，可以点击“验证”，查看该参数是否被合理使用在模型中。验证无误后，就可以点击“开始”参数化扫描。

- 开始：验证无误后，就可以点击“开始”参数化扫描。

> 图示要点：`Parameter_Sweep_7.png` 展示“参数化扫描设置”相关的操作界面或示例，后续审查通过后再补图。

### 查看参数化扫描结果

- 添加对应结果参数即可查看参数化扫描的结果。

> 图示要点：`Parameter_Sweep_9.png` 展示“查看参数化扫描结果”相关的操作界面或示例，后续审查通过后再补图。

- 如果存在多个变量，可以选择目标变量的结果，也可以查看所有变量的结果。例如：可以查看 w0 = 36, w1 = 全部 的所有扫描结果，如图。

> 图示要点：`Parameter_Sweep_8.png` 展示“查看参数化扫描结果”相关的操作界面或示例，后续审查通过后再补图。

## 页内/相关链接

- 注意，参数化扫描前必须在变量: `../Tool/Variables.html`
- 在结果: `../EM_Project/EM_Results.html`


## 待补图片清单
以下图片暂不插入正文，路径为 WavEDA 帮助文档内部相对路径；运行时 agent 会按项目内帮助图片和用户本机 WavEDA 帮助目录进行查找。
| 图片名称 | WavEDA 帮助相对路径 | 建议保留原因 |
| --- | --- | --- |
| Parameter_Sweep_16.png | `Simulation/images/Parameter_Sweep_16.png` | 展示“参数化扫描”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Parameter_Sweep_2.png | `Simulation/images/Parameter_Sweep_2.png` | 展示“参数化扫描设置”步骤的菜单或参数界面，便于新人按界面完成操作。 |
| Parameter_Sweep_.png | `Simulation/images/Parameter_Sweep_.png` | 展示“参数化扫描设置”步骤的菜单或参数界面，便于新人按界面完成操作。 |
| Parameter_Sweep_4.png | `Simulation/images/Parameter_Sweep_4.png` | 展示“参数化扫描设置”步骤的菜单或参数界面，便于新人按界面完成操作。 |
| Parameter_Sweep_7.png | `Simulation/images/Parameter_Sweep_7.png` | 展示“参数化扫描设置”步骤的菜单或参数界面，便于新人按界面完成操作。 |
| Parameter_Sweep_9.png | `Simulation/images/Parameter_Sweep_9.png` | 展示“查看参数化扫描结果”的结果入口或查看界面，便于新人确认后处理位置。 |
| Parameter_Sweep_8.png | `Simulation/images/Parameter_Sweep_8.png` | 展示“查看参数化扫描结果”的结果入口或查看界面，便于新人确认后处理位置。 |
