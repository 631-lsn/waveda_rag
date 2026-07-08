---
title: "散热器"
merged_source: "current_waveda_agent_kb"
source_relative_path: "40_example_cases/Thermal/Radiator/Radiator/Radiator.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\40_example_cases\Thermal\Radiator\Radiator\Radiator.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 散热器

- 案例分类: `Thermal`
- 来源 HTML: `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\Radiator.html`
- 工程文件: `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\Radiator.tsp`
- 截图数量: 10

## 工程摘要

- 工程类型: `Thermal`
- WavEDA 版本: `2.0.7657.2194`
- 坐标类型: `3d`
- 单位: `{"length": "mm", "freq": "Hz", "time": "s", "thermal": "K"}`
- 求解器: `{"number-of-intersection": "1", "basic": "2", "ray-tube-type": "0", "solver": "fem", "method": "fault", "save-path": "1", "basicsem": "2"}`
- 计算区域/Domain: `{"gapType": "no-gap", "gap": "0", "shape-type": "solid"}`
- 变量数量: 0
- 材料: Air, Silicon, Aluminum
- 对象数量: face=3, solid=3, curve=0, lumped-port=0, wave-port=0, point-source=0, plane-wave=0, far-field=1
- XML 解析提示: `junk after document element: line 264, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |
| MH | time-domain |  |  |  |  | 0 |  |
| TL | time-domain |  |  |  |  | 0 |  |
| LT | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |

## 案例教程抽取

## 散热器

- 模型描述 - 仿真设置 - 后处理

### 模型描述

散热板硅芯片模型仿真瞬态，采用恒温边界、热通量边界仿真。 模型尺寸为100*50*46 (mm)，散热片为铝，底下为硅芯片，默认边界条件为恒温边界。

> 图片: `./res/Radiator_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_1.png`

### 仿真设置

1. 仿真时间及网格设置 该模型仿真类型为瞬态仿真。 仿真时间窗Time windows设置为75 s，进行0-75 s瞬态热仿真，设置时步为0.01 s，时间步为7500步。

> 图片: `./res/Radiator_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_2.png`

2. 边界设置 设置默认边界条件为恒温边界，温度为293.15 K； 其余面的边界条件为热通量边界，温度为293.15 K，热传递系数为100 W/m^2·K。

> 图片: `./res/Radiator_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_3.png`

设置硅基板底部为热率边界，功耗值为50 W。

> 图片: `./res/Radiator_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_4.png`

3. 自适应网格设置 使用Rebuild Mesh with Size Field方法，Theta设置为0.4，Residual Tolerance设置为0.01。

> 图片: `./res/Radiator_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_5.png`

4. 点接收器设置 设置点接收器坐标为(13.4167,20,23),单位为 mm，该接收器点位于散热片的中央。

> 图片: `./res/Radiator_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_6.png`

### 后处理

1. 网格查看 仿真完成后，打开网格显示开关并选择体网格显示按键，查看散热器模型的网格分布。

> 图片: `./res/Radiator_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_7.png`

2.查看点接收器结果 在左侧树选择结果接收器右击绘制点接收器的结果。可以看到在该点上温度随时间变化的结果。

> 图片: `./res/Radiator_8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_8.png`

3.查看快照结果 在左侧树选择结果快照右击绘制温度场结果。 可以看到整体散热器模型随着时间的变化，温度分布的变化。下图分别是时间在10 s和75 s的温度场结果。

> 图片: `./res/Radiator_9.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_9.png`

> 图片: `./res/Radiator_10.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_10.png`

## 图片资源

1. `./res/Radiator_1.png` -> `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_1.png`
2. `./res/Radiator_2.png` -> `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_2.png`
3. `./res/Radiator_3.png` -> `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_3.png`
4. `./res/Radiator_4.png` -> `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_4.png`
5. `./res/Radiator_5.png` -> `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_5.png`
6. `./res/Radiator_6.png` -> `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_6.png`
7. `./res/Radiator_7.png` -> `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_7.png`
8. `./res/Radiator_8.png` -> `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_8.png`
9. `./res/Radiator_9.png` -> `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_9.png`
10. `./res/Radiator_10.png` -> `D:\Staid\app\waveda\Example\Thermal\Radiator\Radiator\res\Radiator_10.png`
