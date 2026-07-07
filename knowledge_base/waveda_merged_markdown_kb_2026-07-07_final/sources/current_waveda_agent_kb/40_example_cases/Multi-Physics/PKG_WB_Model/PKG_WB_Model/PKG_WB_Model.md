---
title: "PKG_WB封装电热力仿真"
merged_source: "current_waveda_agent_kb"
source_relative_path: "40_example_cases/Multi-Physics/PKG_WB_Model/PKG_WB_Model/PKG_WB_Model.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\40_example_cases\Multi-Physics\PKG_WB_Model\PKG_WB_Model\PKG_WB_Model.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# PKG_WB封装电热力仿真

- 案例分类: `Multi-Physics`
- 来源 HTML: `D:\Staid\app\waveda\Example\Multi-Physics\PKG_WB_Model\PKG_WB_Model\PKG_WB_Model.html`
- 工程文件: `D:\Staid\app\waveda\Example\Multi-Physics\PKG_WB_Model\PKG_WB_Model\PKG_WB_Model.tsp`
- 截图数量: 8

## 工程摘要

- 工程类型: `EM,Thermal,Elastic`
- WavEDA 版本: `2.1.7688.2195.    (Alpha)`
- 坐标类型: `3d`
- 单位: `{"freq": "GHz", "length": "mm", "time": "s", "thermal": "K"}`
- 求解器: `{"solver": "fem", "number-of-intersection": "1", "ksp-atol": "0.0", "ksp-rtol": "0.0", "method": "fault", "ray-tube-type": "0", "save-path": "1"}`
- 计算区域/Domain: `{"gap-type": "auto", "shape-type": "solid", "gap": "0", "freq-type": "center"}`
- 变量数量: 0
- 材料: Air, copper, gold, solder, pp, FR4, silicon
- 对象数量: face=4, solid=293, curve=0, lumped-port=0, wave-port=0, point-source=0, plane-wave=0, far-field=3
- XML 解析提示: `junk after document element: line 1734, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | steady |  |  |  |  |  |  |
| MH | steady |  |  |  |  |  |  |
| TL | steady |  |  |  |  |  |  |
| LT | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |

## 案例教程抽取

## PKG_WB封装电热力仿真

- 模型描述 - 仿真设置 - 后处理

### 模型描述

PKG_WB封装电热力仿真模型进行稳态电热力仿真，采用电势边界进行稳态电热力仿真，模型示意图如下图所示：

> 图片: `./res/PKG_WB_Model_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PKG_WB_Model\PKG_WB_Model\res\PKG_WB_Model_1.png`

该模型尺寸为10*10*1.488 (mm)。

### 仿真设置

1. 仿真类型及网格设置 该模型仿真类型为steady类型；采用手动网格剖分，设置每波长网格为3 EPW，基函数阶数为2阶，即网格采样率为6 PPW，具体设置如下图：

> 图片: `./res/PKG_WB_Model_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PKG_WB_Model\PKG_WB_Model\res\PKG_WB_Model_2.png`

2. 边界条件设置 电流场边界设置：设置电势边界和接地边界。温度场边界设置：PCB四周设置热通量边界。力场边界设置：BGA球底部设置硬边界。

> 图片: `./res/PKG_WB_Model_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PKG_WB_Model\PKG_WB_Model\res\PKG_WB_Model_3.png`

4. 线接收器设置 选择Wire Bonds上的两条线进行设置线接收器1和线接收器2。

> 图片: `./res/PKG_WB_Model_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PKG_WB_Model\PKG_WB_Model\res\PKG_WB_Model_4.png`

### 后处理

1. 3D网格 仿真完成后，窗口右击选中View Mesh，查看网格剖分情况。

> 图片: `./res/PKG_WB_Model_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PKG_WB_Model\PKG_WB_Model\res\PKG_WB_Model_5.png`

2. 查看线接收器结果 仿真完成后，鼠标右键点击工程树电磁结果、热结果、力结果接收器处选择绘制线接收器随位移变化的电势、温度、位移、等效应力结果。

> 图片: `./res/PKG_WB_Model_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PKG_WB_Model\PKG_WB_Model\res\PKG_WB_Model_6.png`

3. 查看快照结果 仿真完成后，鼠标右键点击工程树快照结果查看电势场、温度场、位移场、等效应力3D结果。

> 图片: `./res/PKG_WB_Model_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PKG_WB_Model\PKG_WB_Model\res\PKG_WB_Model_7.png`

> 图片: `./res/PKG_WB_Model_8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PKG_WB_Model\PKG_WB_Model\res\PKG_WB_Model_8.png`

## 图片资源

1. `./res/PKG_WB_Model_1.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PKG_WB_Model\PKG_WB_Model\res\PKG_WB_Model_1.png`
2. `./res/PKG_WB_Model_2.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PKG_WB_Model\PKG_WB_Model\res\PKG_WB_Model_2.png`
3. `./res/PKG_WB_Model_3.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PKG_WB_Model\PKG_WB_Model\res\PKG_WB_Model_3.png`
4. `./res/PKG_WB_Model_4.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PKG_WB_Model\PKG_WB_Model\res\PKG_WB_Model_4.png`
5. `./res/PKG_WB_Model_5.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PKG_WB_Model\PKG_WB_Model\res\PKG_WB_Model_5.png`
6. `./res/PKG_WB_Model_6.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PKG_WB_Model\PKG_WB_Model\res\PKG_WB_Model_6.png`
7. `./res/PKG_WB_Model_7.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PKG_WB_Model\PKG_WB_Model\res\PKG_WB_Model_7.png`
8. `./res/PKG_WB_Model_8.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PKG_WB_Model\PKG_WB_Model\res\PKG_WB_Model_8.png`
