---
title: "硅基板-铜柱阵列结构模型"
merged_source: "current_waveda_agent_kb"
source_relative_path: "40_example_cases/Thermal/Silicon_sub_copper_pillar_array/Silicon_sub_copper_pillar_array/Silicon_sub_copper_pillar_array.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\40_example_cases\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 硅基板-铜柱阵列结构模型

- 案例分类: `Thermal`
- 来源 HTML: `D:\Staid\app\waveda\Example\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array.html`
- 工程文件: `D:\Staid\app\waveda\Example\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array.tsp`
- 截图数量: 8

## 工程摘要

- 工程类型: `Thermal`
- WavEDA 版本: `1.3.6326.1715.    (Alpha)`
- 坐标类型: `3d`
- 单位: `{"time": "s", "freq": "Hz", "length": "mm", "thermal": "K"}`
- 求解器: `{"basic": "2", "method": "fault", "basicsem": "2", "number-of-intersection": "1", "solver": "fem", "save-path": "1", "ray-tube-type": "0"}`
- 计算区域/Domain: `{"shape-type": "solid", "gapType": "auto-gap", "gap": "0"}`
- 变量数量: 0
- 材料: Air, Silicon, Copper
- 对象数量: face=1, solid=37, curve=0, lumped-port=0, wave-port=0, point-source=0, plane-wave=0, far-field=0
- XML 解析提示: `junk after document element: line 311, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |
| MH | time-domain |  |  |  |  | 0 |  |
| TL | steady |  |  |  |  |  |  |
| LT | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |

## 案例教程抽取

## 硅基板-铜柱阵列结构模型

- 模型描述 - 仿真设置 - 后处理

### 模型描述

硅基板-铜柱阵列结构模型稳态温度场仿真，采用恒温边界、热通量边界进行仿真，模型示意图如下图所示：

> 图片: `./res/Silicon_sub_copper_pillar_array_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\res\Silicon_sub_copper_pillar_array_1.png`

该模型尺寸为1000*1000*1010 (mm)，模型分为硅基板和上边铜柱阵列，边界条件为热通量边界，设置硅基板底部为温度边界。

### 仿真设置

1. 仿真时间及网格设置 该模型仿真类型为稳态Steady类型。 初始网格设置每波长网格为1 EPW，基函数阶数为2阶，即网格采样率为2 PPW；采用自适应网格剖分，设置Longest Edge Bisection方法，残差为0.01；具体设置如下图：

> 图片: `./res/Silicon_sub_copper_pillar_array_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\res\Silicon_sub_copper_pillar_array_2.png`

> 图片: `./res/Silicon_sub_copper_pillar_array_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\res\Silicon_sub_copper_pillar_array_3.png`

2. 边界条件设置 设置默认边界条件为热通量边界，温度为293.15 K，热传递系数为2000 W/m^2·K；设置硅基板底部为温度边界，温度为393.15 K。

> 图片: `./res/Silicon_sub_copper_pillar_array_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\res\Silicon_sub_copper_pillar_array_4.png`

3. 线接收器设置 设置线接收器1起始点（1000 0 100）和终止点（0 1000 100）位置、线接收器2起始点（540 380 1010）和终止点（540 380 10）位置，坐标单位都为mm。

> 图片: `./res/Silicon_sub_copper_pillar_array_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\res\Silicon_sub_copper_pillar_array_5.png`

### 后处理

1. 3D网格 仿真完成后，选中关键部分物体，进入显示网格窗口查看网格剖分情况。

> 图片: `./res/Silicon_sub_copper_pillar_array_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\res\Silicon_sub_copper_pillar_array_6.png`

2. 查看线接收器结果 仿真完成后，鼠标右键点击工程树接收器处选择绘制线接收器随距离变化的温度结果。

> 图片: `./res/Silicon_sub_copper_pillar_array_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\res\Silicon_sub_copper_pillar_array_7.png`

3. 查看快照结果 仿真完成后，鼠标右键点击工程树快照结果查看温度场3D结果。

> 图片: `./res/Silicon_sub_copper_pillar_array_8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\res\Silicon_sub_copper_pillar_array_8.png`

## 图片资源

1. `./res/Silicon_sub_copper_pillar_array_1.png` -> `D:\Staid\app\waveda\Example\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\res\Silicon_sub_copper_pillar_array_1.png`
2. `./res/Silicon_sub_copper_pillar_array_2.png` -> `D:\Staid\app\waveda\Example\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\res\Silicon_sub_copper_pillar_array_2.png`
3. `./res/Silicon_sub_copper_pillar_array_3.png` -> `D:\Staid\app\waveda\Example\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\res\Silicon_sub_copper_pillar_array_3.png`
4. `./res/Silicon_sub_copper_pillar_array_4.png` -> `D:\Staid\app\waveda\Example\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\res\Silicon_sub_copper_pillar_array_4.png`
5. `./res/Silicon_sub_copper_pillar_array_5.png` -> `D:\Staid\app\waveda\Example\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\res\Silicon_sub_copper_pillar_array_5.png`
6. `./res/Silicon_sub_copper_pillar_array_6.png` -> `D:\Staid\app\waveda\Example\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\res\Silicon_sub_copper_pillar_array_6.png`
7. `./res/Silicon_sub_copper_pillar_array_7.png` -> `D:\Staid\app\waveda\Example\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\res\Silicon_sub_copper_pillar_array_7.png`
8. `./res/Silicon_sub_copper_pillar_array_8.png` -> `D:\Staid\app\waveda\Example\Thermal\Silicon_sub_copper_pillar_array\Silicon_sub_copper_pillar_array\res\Silicon_sub_copper_pillar_array_8.png`
