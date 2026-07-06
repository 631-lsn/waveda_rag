# 灯泡模型

- 案例分类: `Thermal`
- 来源 HTML: `D:\Staid\app\waveda\Example\Thermal\Light_bulb\Light_bulb\Light_bulb.html`
- 工程文件: `D:\Staid\app\waveda\Example\Thermal\Light_bulb\Light_bulb\Light_bulb.tsp`
- 截图数量: 8

## 工程摘要

- 工程类型: `Thermal`
- WavEDA 版本: `1.3.6222.1657.    (Alpha)`
- 坐标类型: `3d`
- 单位: `{"freq": "Hz", "thermal": "℃", "length": "mm", "time": "s"}`
- 求解器: `{"basicsem": "2", "number-of-intersection": "1", "method": "fault", "ray-tube-type": "0", "solver": "fem", "save-path": "1", "basic": "2"}`
- 计算区域/Domain: `{"gap": "0", "gapType": "auto-gap", "shape-type": "solid"}`
- 变量数量: 0
- 材料: Air, glass, wu
- 对象数量: face=0, solid=2, curve=0, lumped-port=0, wave-port=0, point-source=0, plane-wave=0, far-field=0

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |
| MH | time-domain |  |  |  |  | 0 |  |
| TL | time-domain |  |  |  |  | 0 |  |
| LT | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |

## 案例教程抽取

## 灯泡模型

- 模型描述 - 仿真设置 - 后处理

### 模型描述

灯泡模型瞬态温度场仿真，采用热通量边界进行仿真，模型示意图如下图所示：

> 图片: `./res/Light_bulb_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Light_bulb\Light_bulb\res\Light_bulb_1.png`

该模型尺寸为40*40*47 (mm)，模型分为灯泡和钨丝，边界条件为热通量边界。

### 仿真设置

1. 仿真时间及网格设置 该模型仿真类型为Time window类型，仿真时间窗Time windows设置为20 s，即进行0-20 s瞬态应力仿真；设置时步为0.05 s。 初始网格设置每波长网格为1 EPW，基函数阶数为2阶，即网格采样率为2 PPW；采用自适应网格剖分，设置Rebuild Mesh with Size Field方法，残差为0.001；具体设置如下图：

> 图片: `./res/Light_bulb_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Light_bulb\Light_bulb\res\Light_bulb_2.png`

2. 体激励源 选中钨丝设置体激励，设置激励大小为10 W进行激励

> 图片: `./res/Light_bulb_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Light_bulb\Light_bulb\res\Light_bulb_3.png`

3. 边界条件设置 设置热通量边界，温度为20 ℃，热传递系数为10 W/m^2·K。

> 图片: `./res/Light_bulb_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Light_bulb\Light_bulb\res\Light_bulb_4.png`

4. 点接收器设置 设置点接收器1（0 0 0）位置和点接收器2（0 0 -15）位置，坐标单位都为mm。

> 图片: `./res/Light_bulb_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Light_bulb\Light_bulb\res\Light_bulb_5.png`

### 后处理

1. 3D网格 仿真完成后，选中关键部分物体，进入显示网格窗口查看网格剖分情况。

> 图片: `./res/Light_bulb_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Light_bulb\Light_bulb\res\Light_bulb_6.png`

2. 查看点接收器结果 仿真完成后，鼠标右键点击工程树接收器处选择绘制点接收器随时间变化的温度结果。

> 图片: `./res/Light_bulb_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Light_bulb\Light_bulb\res\Light_bulb_7.png`

3. 查看快照结果 仿真完成后，鼠标右键点击工程树快照结果查看温度场3D结果

> 图片: `./res/Light_bulb_8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Thermal\Light_bulb\Light_bulb\res\Light_bulb_8.png`

## 图片资源

1. `./res/Light_bulb_1.png` -> `D:\Staid\app\waveda\Example\Thermal\Light_bulb\Light_bulb\res\Light_bulb_1.png`
2. `./res/Light_bulb_2.png` -> `D:\Staid\app\waveda\Example\Thermal\Light_bulb\Light_bulb\res\Light_bulb_2.png`
3. `./res/Light_bulb_3.png` -> `D:\Staid\app\waveda\Example\Thermal\Light_bulb\Light_bulb\res\Light_bulb_3.png`
4. `./res/Light_bulb_4.png` -> `D:\Staid\app\waveda\Example\Thermal\Light_bulb\Light_bulb\res\Light_bulb_4.png`
5. `./res/Light_bulb_5.png` -> `D:\Staid\app\waveda\Example\Thermal\Light_bulb\Light_bulb\res\Light_bulb_5.png`
6. `./res/Light_bulb_6.png` -> `D:\Staid\app\waveda\Example\Thermal\Light_bulb\Light_bulb\res\Light_bulb_6.png`
7. `./res/Light_bulb_7.png` -> `D:\Staid\app\waveda\Example\Thermal\Light_bulb\Light_bulb\res\Light_bulb_7.png`
8. `./res/Light_bulb_8.png` -> `D:\Staid\app\waveda\Example\Thermal\Light_bulb\Light_bulb\res\Light_bulb_8.png`
