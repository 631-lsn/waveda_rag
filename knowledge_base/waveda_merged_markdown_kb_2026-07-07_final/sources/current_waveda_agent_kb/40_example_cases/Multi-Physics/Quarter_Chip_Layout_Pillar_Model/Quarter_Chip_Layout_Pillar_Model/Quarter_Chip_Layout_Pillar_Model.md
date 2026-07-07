---
title: "QCLP_Model 仿真模型介绍"
merged_source: "current_waveda_agent_kb"
source_relative_path: "40_example_cases/Multi-Physics/Quarter_Chip_Layout_Pillar_Model/Quarter_Chip_Layout_Pillar_Model/Quarter_Chip_Layout_Pillar_Model.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\40_example_cases\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# QCLP_Model 仿真模型介绍

- 案例分类: `Multi-Physics`
- 来源 HTML: `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model.html`
- 工程文件: `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model.tsp`
- 截图数量: 11

## 工程摘要

- 工程类型: `EM,Thermal,Elastic`
- WavEDA 版本: `2.1.7791.2238.    (Alpha)`
- 坐标类型: `3d`
- 单位: `{"length": "mm", "freq": "kHz", "thermal": "K", "time": "s"}`
- 求解器: `{"tolerance": "0.000001", "ray-tube-type": "0", "number-of-intersection": "1", "method": "fault", "solver": "fem", "ksp-rtol": "0.00001", "save-path": "1", "max-iterations": "0", "ksp-dtol": "100000"}`
- 计算区域/Domain: `{"gap-type": "auto", "freq-type": "center", "gap": "0", "shape-type": "solid"}`
- 变量数量: 0
- 材料: Air, PEC, Copper, Gold, Silicon, FR-4, odb_copper_1, odb_dielectric_1, odb_dielectric_2, Copper_1, Copper_2, Copper_3, Copper_4, odb_copper_2, odb_copper_3, odb_copper_4
- 对象数量: face=2, solid=26, curve=0, lumped-port=0, wave-port=0, point-source=0, plane-wave=0, far-field=3
- XML 解析提示: `junk after document element: line 1218, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | steady |  |  |  |  |  |  |
| MH | steady |  |  |  |  |  |  |
| TL | steady |  |  |  |  |  |  |
| LT | freq-domain | 1e+06 | 1 | 1 | 1 | 0 | 0 |

## 案例教程抽取

## QCLP_Model 仿真模型介绍

## QCLP_Model 模型

- 模型描述 - 仿真设置 - 后处理

### 模型描述

模型 QCLP_Model 基于 1/4 芯片版图转 3D 仿真技术，模型尺寸为 5 x 5 x 1.929 mm³，模型示意图如下图所示：

> 图片: `./res/Quarter_Chip_Layout_Pillar_Model1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model1.png`

在结构分布上，模型核心走线与底部焊球均采用高导电金属材料 Copper ，确保了电流能在传导路径完成导通；衬底部分采用 Silicon 材料，而层间材料则由 Odb Dielectric 介质填充，形成了完整的多层芯片封装结构。仿真电流流经 Copper 走线至接地端产生的物理场变化。

### 仿真设置

1. 电热耦合多物理场仿真配置

WavEDA 支持高度集成的电热耦合多物理场设置，通过在“多物理场”节点中添加电磁热联动接口，实现电流产生的焦耳热与固体传热模块之间的耦合场仿真，从而精确仿真芯片在电压激励下的热演化过程。

> 图片: `./res/Quarter_Chip_Layout_Pillar_Model2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model2.png`

2. 稳态与时域脉冲仿真态设置

WavEDA 支持对该模型进行双仿真态分析：在稳态配置下，通过定常求解器评估系统的长期热平衡分布；在时域脉冲配置下，通过设置特定的脉冲激励波形与瞬态步长，捕捉系统在周期性电信号冲击下的动态温升曲线。

> 图片: `./res/Quarter_Chip_Layout_Pillar_Model3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model3.png`

> 图片: `./res/Quarter_Chip_Layout_Pillar_Model4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model4.png`

3. 独立物理场边界条件设定

WavEDA 支持对每个物理场单独进行边界配置：在电流学模块中，通过定义金属走线末端为“终端”并施加激励，同时将底层焊球定义为“接地”以构建回路；在热学模块中，为芯片封装外表面指定“对流热通量”边界，模拟外部空气对流引起的散热环境。

> 图片: `./res/Quarter_Chip_Layout_Pillar_Model5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model5.png`

> 图片: `./res/Quarter_Chip_Layout_Pillar_Model6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model6.png`

4. 线接收器设置

设置线接收器选中走线表面两点右击创建，实际坐标为起始点（-2.87 3.69135 1.63576）和终止点（-2.87 4.11858 1.63576）位置坐标单位为 mm。

> 图片: `./res/Quarter_Chip_Layout_Pillar_Model9.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model9.png`

### 后处理

1. 3D 网格

仿真完成后，选中关键部分物体，进入显示网格窗口查看网格剖分情况。

> 图片: `./res/Quarter_Chip_Layout_Pillar_Model10.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model10.png`

2. 查看线接收器结果

稳态仿真完成后，鼠标右键点击工程树接收器处选择绘制线接收器随距离变化的温度结果。

> 图片: `./res/Quarter_Chip_Layout_Pillar_Model11.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model11.png`

时域仿真完成后，鼠标右键点击工程树接收器处选择绘制线接收器随距离变化的电场结果。

> 图片: `./res/Quarter_Chip_Layout_Pillar_Model7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model7.png`

3. 查看快照结果

仿真完成后，鼠标右键点击工程树快照结果查看电场、电流、电势、温度 3D 结果。

> 图片: `./res/Quarter_Chip_Layout_Pillar_Model13.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model13.png`

## 图片资源

1. `./res/Quarter_Chip_Layout_Pillar_Model1.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model1.png`
2. `./res/Quarter_Chip_Layout_Pillar_Model2.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model2.png`
3. `./res/Quarter_Chip_Layout_Pillar_Model3.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model3.png`
4. `./res/Quarter_Chip_Layout_Pillar_Model4.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model4.png`
5. `./res/Quarter_Chip_Layout_Pillar_Model5.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model5.png`
6. `./res/Quarter_Chip_Layout_Pillar_Model6.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model6.png`
7. `./res/Quarter_Chip_Layout_Pillar_Model9.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model9.png`
8. `./res/Quarter_Chip_Layout_Pillar_Model10.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model10.png`
9. `./res/Quarter_Chip_Layout_Pillar_Model11.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model11.png`
10. `./res/Quarter_Chip_Layout_Pillar_Model7.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model7.png`
11. `./res/Quarter_Chip_Layout_Pillar_Model13.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Quarter_Chip_Layout_Pillar_Model\Quarter_Chip_Layout_Pillar_Model\res\Quarter_Chip_Layout_Pillar_Model13.png`
