---
title: "螺栓"
merged_source: "current_waveda_agent_kb"
source_relative_path: "40_example_cases/Mech/Bolt/Bolt/Bolt.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\40_example_cases\Mech\Bolt\Bolt\Bolt.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 螺栓

- 案例分类: `Mech`
- 来源 HTML: `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\Bolt.html`
- 工程文件: `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\Bolt.tsp`
- 截图数量: 10

## 工程摘要

- 工程类型: `Elastic`
- WavEDA 版本: `2.0.7657.2194`
- 坐标类型: `3d`
- 单位: `{"length": "cm", "time": "ms", "thermal": "K", "freq": "kHz"}`
- 求解器: `{"basicsem": "2", "ray-tube-type": "0", "solver": "fem", "method": "fault", "basic": "2", "number-of-intersection": "1", "save-path": "1"}`
- 计算区域/Domain: `{"shape-type": "solid", "gap": "0", "gapType": "auto-gap"}`
- 变量数量: 0
- 材料: Water, Structural steel
- 对象数量: face=1, solid=56, curve=0, lumped-port=0, wave-port=0, point-source=0, plane-wave=0, far-field=2
- XML 解析提示: `junk after document element: line 415, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |
| MH | time-domain |  |  |  |  | 0 |  |
| TL | time-domain |  |  |  |  | 0 |  |
| LT | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |

## 案例教程抽取

## 螺栓

- 模型描述 - 仿真设置 - 后处理

### 模型描述

螺栓模型瞬态应力仿真，采用面激励源、BHW-1阶脉冲进行0-10 ms瞬态时域仿真，模型示意图如下图所示：

> 图片: `./res/Bolt_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_1.png`

该模型尺寸为10.25*15*4.6 (cm)，配有螺孔和螺钉，边界条件为软边界soft，设置-Y方向上一个面为硬边界。

### 仿真设置

1. 仿真时间及网格设置 该模型仿真类型为Time window类型，仿真时间窗Time windows设置为10 ms，即进行0-10 ms瞬态应力仿真；设置时步为0.025 ms。

采用手动网格剖分，设置每波长网格数（EPW）为6，基函数阶数为2阶，即网格采样率（PPW）为12，具体设置如下图：

> 图片: `./res/Bolt_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_2.png`

> 图片: `./res/Bolt_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_3.png`

2. 面激励源 选中中间矩形洞的8个面设置面激励，设置激励大小为100 N/m^2，选择默认脉冲(BHW-1阶)进行激励。

> 图片: `./res/Bolt_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_4.png`

> 图片: `./res/Bolt_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_5.png`

3. 边界条件设置 设置默认边界条件为软边界，选择-Y轴上下方的面设置为硬边界。

> 图片: `./res/Bolt_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_6.png`

4. 点接收器设置 设置点接收器1（3.125 7.5 0.6）位置和点接收器2（0 7.5 2.54953）位置，坐标单位都为cm。

> 图片: `./res/Bolt_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_7.png`

### 后处理

1. 3D网格 仿真完成后，进入Mesh->Show|Hide Mesh，建模窗口选中关键部分物体，查看网格剖分情况。

> 图片: `./res/Bolt_8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_8.png`

2. 查看点接收器结果 仿真完成后，鼠标右键点击工程树接收器处选择绘制点接收器随时间变化的位移或等效应力结果。

> 图片: `./res/Bolt_9.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_9.png`

3. 查看快照结果 仿真完成后，鼠标右键点击工程树快照结果查看位移场或等效应力3D结果。

> 图片: `./res/Bolt_10.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_10.png`

## 图片资源

1. `./res/Bolt_1.png` -> `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_1.png`
2. `./res/Bolt_2.png` -> `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_2.png`
3. `./res/Bolt_3.png` -> `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_3.png`
4. `./res/Bolt_4.png` -> `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_4.png`
5. `./res/Bolt_5.png` -> `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_5.png`
6. `./res/Bolt_6.png` -> `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_6.png`
7. `./res/Bolt_7.png` -> `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_7.png`
8. `./res/Bolt_8.png` -> `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_8.png`
9. `./res/Bolt_9.png` -> `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_9.png`
10. `./res/Bolt_10.png` -> `D:\Staid\app\waveda\Example\Mech\Bolt\Bolt\res\Bolt_10.png`
