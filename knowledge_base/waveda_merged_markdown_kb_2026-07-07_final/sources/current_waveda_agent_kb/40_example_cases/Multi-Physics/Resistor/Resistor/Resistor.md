---
title: "贴片电阻模型"
merged_source: "current_waveda_agent_kb"
source_relative_path: "40_example_cases/Multi-Physics/Resistor/Resistor/Resistor.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\40_example_cases\Multi-Physics\Resistor\Resistor\Resistor.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 贴片电阻模型

- 案例分类: `Multi-Physics`
- 来源 HTML: `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\Resistor.html`
- 工程文件: `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\Resistor.tsp`
- 截图数量: 12

## 工程摘要

- 工程类型: `EM,Thermal,Elastic`
- WavEDA 版本: `2.1.7446.2090.    (Alpha)`
- 坐标类型: `3d`
- 单位: `{"time": "s", "freq": "GHz", "thermal": "K", "length": "mm"}`
- 求解器: `{"max-iterations": "0", "solver": "fem", "method": "fault", "ray-tube-type": "0", "save-path": "1", "number-of-intersection": "1"}`
- 计算区域/Domain: `{"freq-type": "center", "gap": "0", "shape-type": "solid", "gap-type": "auto"}`
- 变量数量: 0
- 材料: Air, FR-4, Alumina 96pct, Copper, Silver, Solder
- 对象数量: face=2, solid=25, curve=0, lumped-port=0, wave-port=0, point-source=0, plane-wave=0, far-field=1
- XML 解析提示: `junk after document element: line 1226, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |
| MH | steady |  |  |  |  |  |  |
| TL | steady |  |  |  |  |  |  |
| LT | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |

## 案例教程抽取

## 贴片电阻模型

- 模型描述 - 仿真设置 - 后处理

### 模型描述

本模型为贴片电阻焊接在介质板的完整装配模型，通过多物理场仿真贴片电阻受热导致形变的情况。

> 图片: `./res/Resistor_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_1.png`

### 仿真设置

1. 多物理场设置 多物理场条件设置如下：五个电阻设置为热源，每个电阻的热量为 0.1 W；其余表面设置为对流热通量，介质板底面设置为固定约束。

> 图片: `./res/Resistor_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_2.png`

> 图片: `./res/Resistor_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_3.png`

> 图片: `./res/Resistor_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_4.png`

> 图片: `./res/Resistor_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_5.png`

2. 仿真配置 选择热学、力学进行热膨胀仿真，仿真类型全部选择 Steady。具体设置如下图：

> 图片: `./res/Resistor_12.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_12.png`

### 后处理

多物理场结果 仿真结束后，分别展开温度结果和力学结果两个节点，添加温度、位移及应力等场分布。对已经添加的线接收器，可以查看该线段上的场分布结果。如下图所示，分别展示了各场的仿真结果，温度主要集中在电阻上，因此电阻与介质板连接处受热导致位移和应力也较大。

温度结果

> 图片: `./res/Resistor_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_6.png`

> 图片: `./res/Resistor_9.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_9.png`

力学结果

> 图片: `./res/Resistor_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_7.png`

> 图片: `./res/Resistor_10.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_10.png`

> 图片: `./res/Resistor_8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_8.png`

> 图片: `./res/Resistor_11.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_11.png`

## 图片资源

1. `./res/Resistor_1.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_1.png`
2. `./res/Resistor_2.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_2.png`
3. `./res/Resistor_3.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_3.png`
4. `./res/Resistor_4.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_4.png`
5. `./res/Resistor_5.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_5.png`
6. `./res/Resistor_12.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_12.png`
7. `./res/Resistor_6.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_6.png`
8. `./res/Resistor_9.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_9.png`
9. `./res/Resistor_7.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_7.png`
10. `./res/Resistor_10.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_10.png`
11. `./res/Resistor_8.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_8.png`
12. `./res/Resistor_11.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Resistor\Resistor\res\Resistor_11.png`
