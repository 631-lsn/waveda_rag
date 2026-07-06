# 凳子模型

- 案例分类: `Mech`
- 来源 HTML: `D:\Staid\app\waveda\Example\Mech\Stool\Stool\Stool.html`
- 工程文件: `D:\Staid\app\waveda\Example\Mech\Stool\Stool\Stool.tsp`
- 截图数量: 8

## 工程摘要

- 工程类型: `Elastic`
- WavEDA 版本: `1.3.6222.1657.    (Alpha)`
- 坐标类型: `3d`
- 单位: `{"freq": "kHz", "time": "ms", "thermal": "K", "length": "cm"}`
- 求解器: `{"basicsem": "2", "ray-tube-type": "0", "solver": "fem", "basic": "2", "save-path": "1", "number-of-intersection": "1", "method": "fault"}`
- 计算区域/Domain: `{"gapType": "auto-gap", "shape-type": "solid", "gap": "0"}`
- 变量数量: 0
- 材料: Water, Steel
- 对象数量: face=1, solid=5, curve=0, lumped-port=0, wave-port=0, point-source=0, plane-wave=0, far-field=2
- XML 解析提示: `junk after document element: line 271, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |
| MH | steady |  |  |  |  |  |  |
| TL | time-domain |  |  |  |  | 0 |  |
| LT | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |

## 案例教程抽取

## 凳子模型

- 模型描述 - 仿真设置 - 后处理

### 模型描述

凳子模型稳态应力仿真，采用Soft边界、固定约束边界进行仿真，模型示意图如下图所示：

> 图片: `./res/Stool_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\Stool\Stool\res\Stool_1.png`

该模型尺寸为50*74*50 (cm)，模型分为凳子面和四条凳子腿，边界条件为Soft边界，设置凳子腿底部为固定约束。

### 仿真设置

1. 仿真时间及网格设置 该模型仿真类型为稳态Steady类型。 初始网格设置每波长网格为3 EPW，基函数阶数为2阶，即网格采样率为6 PPW；采用自适应网格剖分，设置Rebuild Mesh with Size Field方法，残差为0.01；具体设置如下图：

> 图片: `./res/Stool_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\Stool\Stool\res\Stool_2.png`

2. 面激励源 选中凳子面设置面激励，设置激励大小为1500 N/m^2进行激励。

> 图片: `./res/Stool_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\Stool\Stool\res\Stool_3.png`

3. 边界条件设置 设置默认边界条件为Soft边界；设置凳子腿底部为固定约束。

> 图片: `./res/Stool_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\Stool\Stool\res\Stool_4.png`

4. 线接收器设置 设置线接收器1起始点（25 -71.5 25）和终止点（25 2.5 25）位置，坐标单位都为cm。

> 图片: `./res/Stool_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\Stool\Stool\res\Stool_5.png`

### 后处理

1. 3D网格 仿真完成后，选中关键部分物体，进入显示网格窗口查看网格剖分情况。

> 图片: `./res/Stool_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\Stool\Stool\res\Stool_6.png`

2. 查看线接收器结果 仿真完成后，鼠标右键点击工程树接收器处选择绘制线接收器随弧长变化的位移或等效应力结果。

> 图片: `./res/Stool_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\Stool\Stool\res\Stool_7.png`

3. 查看快照结果 仿真完成后，鼠标右键点击工程树快照结果查看位移场或等效应力3D结果

> 图片: `./res/Stool_8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Mech\Stool\Stool\res\Stool_8.png`

## 图片资源

1. `./res/Stool_1.png` -> `D:\Staid\app\waveda\Example\Mech\Stool\Stool\res\Stool_1.png`
2. `./res/Stool_2.png` -> `D:\Staid\app\waveda\Example\Mech\Stool\Stool\res\Stool_2.png`
3. `./res/Stool_3.png` -> `D:\Staid\app\waveda\Example\Mech\Stool\Stool\res\Stool_3.png`
4. `./res/Stool_4.png` -> `D:\Staid\app\waveda\Example\Mech\Stool\Stool\res\Stool_4.png`
5. `./res/Stool_5.png` -> `D:\Staid\app\waveda\Example\Mech\Stool\Stool\res\Stool_5.png`
6. `./res/Stool_6.png` -> `D:\Staid\app\waveda\Example\Mech\Stool\Stool\res\Stool_6.png`
7. `./res/Stool_7.png` -> `D:\Staid\app\waveda\Example\Mech\Stool\Stool\res\Stool_7.png`
8. `./res/Stool_8.png` -> `D:\Staid\app\waveda\Example\Mech\Stool\Stool\res\Stool_8.png`
