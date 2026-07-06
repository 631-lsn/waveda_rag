# PBGA封装热力仿真

- 案例分类: `Multi-Physics`
- 来源 HTML: `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\PBGA.html`
- 工程文件: `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\PBGA.tsp`
- 截图数量: 12

## 工程摘要

- 工程类型: `EM,Thermal,Elastic`
- WavEDA 版本: `2.0.7015.1911`
- 坐标类型: `3d`
- 单位: `{"length": "mm", "freq": "Hz", "thermal": "K", "time": "s"}`
- 求解器: `{"basicsem": "2", "method": "fault", "ray-tube-type": "0", "save-path": "1", "basic": "2", "solver": "fem", "number-of-intersection": "1"}`
- 计算区域/Domain: `{"shape-type": "solid", "gap": "0", "gapType": "no-gap"}`
- 变量数量: 0
- 材料: Air, solder, Mold compound, via material, substrate material, epoxy resin typical, si typical, filler block jc, die attach, trace, fr4, pcb_Substrate, pcb_Substrate_B, pcbb_substrate_mo
- 对象数量: face=6, solid=402, curve=0, lumped-port=0, wave-port=0, point-source=0, plane-wave=0, far-field=3
- XML 解析提示: `junk after document element: line 2420, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | time-domain |  |  |  |  | 0 |  |
| MH | time-domain |  |  |  |  | 0 |  |
| TL | time-domain |  |  |  |  | 0 |  |
| LT | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |

## 案例教程抽取

## PBGA封装热力仿真

- 模型描述 - 仿真设置 - 后处理

### 模型描述

PBGA封装热力仿真模型进行瞬态热力仿真，采用面激励源、分段函数脉冲进行0-10 s瞬态时域仿真，模型示意图如下图所示：

> 图片: `./res/PBGA_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_1.png`

该模型尺寸为114.5*101.5*3.2 (mm)，包含PCB板。

### 仿真设置

1. 仿真时间及网格设置 该模型仿真类型为Time window类型，仿真时间窗Time windows设置为10 s，即进行0-10 s瞬态热力仿真；设置时步为0.2 s。

采用手动网格剖分，设置每波长网格为12 EPW，基函数阶数为2阶，即网格采样率为24 PPW，具体设置如下图：

> 图片: `./res/PBGA_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_2.png`

> 图片: `./res/PBGA_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_3.png`

2. 面激励源 选中硅介质的上表面，设置激励大小为1 W，设置分段函数脉冲进行激励。

> 图片: `./res/PBGA_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_4.png`

> 图片: `./res/PBGA_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_5.png`

3. 边界条件设置 温度场边界设置：四个热薄近似边界条件，PCB四周设置温度边界。力场边界设置：PCB板底部设置硬边界。

> 图片: `./res/PBGA_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_6.png`

4. 点接收器设置 设置点接收器1（7.5 15.5 0）位置和点接收器2（7.5 7.5 0.96）位置，坐标单位都为mm。

> 图片: `./res/PBGA_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_7.png`

### 后处理

1. 3D网格 仿真完成后，窗口右击选中View Mesh，查看网格剖分情况。

> 图片: `./res/PBGA_8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_8.png`

2. 查看点接收器结果 仿真完成后，鼠标右键点击工程树热结果和力结果接收器处选择绘制点接收器随时间变化的温度、位移、等效应力结果。

> 图片: `./res/PBGA_9.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_9.png`

3. 查看快照结果 仿真完成后，鼠标右键点击工程树快照结果查看温度场、位移场、等效应力3D结果。

> 图片: `./res/PBGA_10.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_10.png`

> 图片: `./res/PBGA_11.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_11.png`

> 图片: `./res/PBGA_12.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_12.png`

## 图片资源

1. `./res/PBGA_1.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_1.png`
2. `./res/PBGA_2.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_2.png`
3. `./res/PBGA_3.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_3.png`
4. `./res/PBGA_4.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_4.png`
5. `./res/PBGA_5.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_5.png`
6. `./res/PBGA_6.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_6.png`
7. `./res/PBGA_7.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_7.png`
8. `./res/PBGA_8.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_8.png`
9. `./res/PBGA_9.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_9.png`
10. `./res/PBGA_10.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_10.png`
11. `./res/PBGA_11.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_11.png`
12. `./res/PBGA_12.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\PBGA\PBGA\res\PBGA_12.png`
