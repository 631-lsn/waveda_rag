# 梯面尺

- 案例分类: `Mech`
- 来源 HTML: `D:\Staid\app\waveda\Example\Mech\ruler\ruler\ruler.html`
- 工程文件: `D:\Staid\app\waveda\Example\Mech\ruler\ruler\ruler.tsp`
- 截图数量: 11

## 工程摘要

- 工程类型: `Elastic`
- WavEDA 版本: `1.3.6262.1698.    (Alpha)`
- 坐标类型: `3d`
- 单位: `{"freq": "Hz", "thermal": "K", "length": "mm", "time": "ms"}`
- 求解器: `{"number-of-intersection": "1", "basicsem": "2", "basic": "2", "solver": "fem", "save-path": "1", "method": "fault", "ray-tube-type": "0"}`
- 计算区域/Domain: `{"gapType": "no-gap", "shape-type": "solid", "gap": "0"}`
- 变量数量: 0
- 材料: Water, Steel, ps
- 对象数量: face=5, solid=1, curve=0, lumped-port=0, wave-port=0, point-source=0, plane-wave=0, far-field=2
- XML 解析提示: `junk after document element: line 261, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |
| MH | time-domain |  |  |  |  | 0 |  |
| TL | time-domain |  |  |  |  | 0 |  |
| LT | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |

## 案例教程抽取

## 梯面尺

- 模型描述 - 仿真设置 - 后处理

### 模型描述

梯面尺模型长300 mm的尺子，材料为ps，在一端距离10 mm边界固定，另外一端受垂直受力。 模型瞬态仿真，采用面激励源、BHW-1阶脉冲进行0-5 ms瞬态时域仿真，模型示意图如下图所示：

> 图片: `./res/Rules_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_1.png`

该模型尺寸为32*2*310 (mm)，边界条件为软边界soft，设置-Y方向上一个面为硬边界。

### 仿真设置

1. 仿真时间及网格设置 该模型仿真类型为瞬态仿真，仿真时间窗Time windows设置为5 ms，即进行0-5 ms瞬态应力仿真；设置时步为0.01 ms，共计500步。

采用手动网格剖分，设置每波长网格数量（EPW）为3，基函数阶数为2阶，即网格采样率（PPW）为6，具体设置如下图：

> 图片: `./res/Rules_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_2.png`

> 图片: `./res/Rules_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_3.png`

2. 面激励源 在梯面尺靠近+Z方向设置面激励模拟受力，设置激励幅值为20 N/m^2，选择默认脉冲(BHW-1阶)进行激励。

> 图片: `./res/Rules_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_6.png`

3. 边界条件设置 设置默认边界条件为软边界，设置起始端10mm宽度的面顶部底部边界面为硬边界。

> 图片: `./res/Rules_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_7.png`

4. 点接收器设置 设置起始端点接收器1（0,0,0）位置和点接收器2（11,1,310）位置，坐标单位都为mm。

> 图片: `./res/Rules_8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_8.png`

### 后处理

1. 3D网格 仿真完成后，进入Mesh->Show|Hide Mesh，建模窗口选中关键部分物体，查看网格剖分情况。

> 图片: `./res/Rules_9.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_9.png`

2. 查看点接收器结果 仿真完成后，鼠标右键点击工程树接收器处选择绘制点接收器随时间变化的位移或等效应力结果。

> 图片: `./res/Rules_10.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_10.png`

> 图片: `./res/Rules_11.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_11.png`

3. 查看快照结果 仿真完成后，鼠标右键点击工程树快照结果查看位移场或等效应力3D结果。

> 图片: `./res/Rules_12.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_12.png`

> 图片: `./res/Rules_13.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_13.png`

## 图片资源

1. `./res/Rules_1.png` -> `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_1.png`
2. `./res/Rules_2.png` -> `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_2.png`
3. `./res/Rules_3.png` -> `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_3.png`
4. `./res/Rules_6.png` -> `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_6.png`
5. `./res/Rules_7.png` -> `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_7.png`
6. `./res/Rules_8.png` -> `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_8.png`
7. `./res/Rules_9.png` -> `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_9.png`
8. `./res/Rules_10.png` -> `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_10.png`
9. `./res/Rules_11.png` -> `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_11.png`
10. `./res/Rules_12.png` -> `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_12.png`
11. `./res/Rules_13.png` -> `D:\Staid\app\waveda\Example\Mech\ruler\ruler\res\Rules_13.png`
