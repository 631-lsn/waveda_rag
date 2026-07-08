---
title: "球"
merged_source: "current_waveda_agent_kb"
source_relative_path: "40_example_cases/EM/Plane Wave/Sphere/sphere.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\40_example_cases\EM\Plane Wave\Sphere\sphere.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 球

- 案例分类: `EM`
- 来源 HTML: `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\sphere.html`
- 工程文件: `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\sphere.tsp`
- 截图数量: 9

## 工程摘要

- 工程类型: `EM`
- WavEDA 版本: `1.1.4031.1031.    (Alpha)`
- 坐标类型: `3d`
- 单位: `{"length": "cm", "freq": "GHz", "time": "ns", "thermal": "K"}`
- 求解器: `{"basic": "2", "method": "fault", "solver": "fem"}`
- 计算区域/Domain: `{"shape-type": "solid", "gapType": "no-gap", "gap": "0"}`
- 变量数量: 7
- 材料: Air, PEC
- 对象数量: face=0, solid=2, curve=0, lumped-port=0, wave-port=0, point-source=0, plane-wave=0, far-field=51

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | freq-domain | 0.04 | 2.54 | 51 | 0.05 | 0 | 1 |

### 变量摘要

| 变量 | 表达式 |
| --- | --- |
| l1 | 53 |
| w1 | 32 |
| xg | 10 |
| yg | 5 |
| xf | w1/2 |
| xs | 3 |
| sw | 6 |

## 案例教程抽取

## 球

- 模型描述 - 仿真设置 - 后处理

### 模型描述

PEC球平面波RCS仿真，设置传播方向为(0，1，1)，电场方向为(1，0，0)的平面波激励，扫频范围为0.04-2.54 GHz，模型示意图如下图所示：

> 图片: `./res/Sphere_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\res\Sphere_1.png`

该模型为半径为10 cm球组成，边界条件为ABC。

### 仿真设置

1. 仿真频率及网格设置 该模型仿真频率设置为0.04-2.54 GHz，扫频方式选择离散仿真，该平面波激励不支持插值和快速方法。 采用手动网格剖分，设置网格采样率为4 PPW，具体设置如下图：

> 图片: `./res/Sphere_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\res\Sphere_2.png`

> 图片: `./res/Sphere_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\res\Sphere_3.png`

2. 平面波设置 有关平面波设置如下图所示，首先设置k方向为(0，1，1)，参考轴为(0，0，1)，V(TM)=1 V/m，H(TE)=0 V/m；得出电场方向(1，0，0)

> 图片: `./res/Sphere_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\res\Sphere_4.png`

> 图片: `./res/Sphere_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\res\Sphere_5.png`

3. 远场频点设置 添加0.04-2.54 GHz范围、步长0.1 GHz远场频点。

> 图片: `./res/Sphere_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\res\Sphere_6.png`

### 后处理

1. 3D网格 仿真完成后，选中关键部分物体，进入显示网格窗口查看网格剖分情况。

> 图片: `./res/Sphere_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\res\Sphere_7.png`

2. 查看单站雷达散射截面结果 仿真完成后，鼠标右键点击工程树远场处选择绘制单站雷达散射截面。

> 图片: `./res/Sphere_8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\res\Sphere_8.png`

3. 查看双站雷达散射截面结果 仿真完成后，鼠标右键点击工程树远场结果查看双站雷达散射截面3D、2D极坐标结果。

> 图片: `./res/Sphere_9.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\res\Sphere_9.png`

## 图片资源

1. `./res/Sphere_1.png` -> `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\res\Sphere_1.png`
2. `./res/Sphere_2.png` -> `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\res\Sphere_2.png`
3. `./res/Sphere_3.png` -> `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\res\Sphere_3.png`
4. `./res/Sphere_4.png` -> `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\res\Sphere_4.png`
5. `./res/Sphere_5.png` -> `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\res\Sphere_5.png`
6. `./res/Sphere_6.png` -> `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\res\Sphere_6.png`
7. `./res/Sphere_7.png` -> `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\res\Sphere_7.png`
8. `./res/Sphere_8.png` -> `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\res\Sphere_8.png`
9. `./res/Sphere_9.png` -> `D:\Staid\app\waveda\Example\EM\Plane Wave\Sphere\res\Sphere_9.png`
