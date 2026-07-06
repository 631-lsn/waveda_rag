# GIS insulator 仿真模型介绍

- 案例分类: `Multi-Physics`
- 来源 HTML: `D:\Staid\app\waveda\Example\Multi-Physics\Gis insulator\Gis insulator\Gis insulator.html`
- 工程文件: `D:\Staid\app\waveda\Example\Multi-Physics\Gis insulator\Gis insulator\Gis insulator.tsp`
- 截图数量: 7

## 工程摘要

- 工程类型: `EM,Thermal,Elastic`
- WavEDA 版本: `2.1.7805.2248.    (Alpha)`
- 坐标类型: `3d`
- 单位: `{"length": "cm", "time": "s", "freq": "MHz", "thermal": "K"}`
- 求解器: `{"method": "fault", "save-path": "1", "solver": "fem", "number-of-intersection": "1", "ksp-rtol": "0.00001", "ray-tube-type": "0", "ksp-dtol": "100000", "tolerance": "0.000001", "max-iterations": "10000"}`
- 计算区域/Domain: `{"gap": "((0)*0.1)*10", "shape-type": "solid", "gap-type": "no"}`
- 变量数量: 0
- 材料: Air, epoxy resin, Aluminum, sf6, al
- 对象数量: face=3, solid=7, curve=0, lumped-port=0, wave-port=0, point-source=0, plane-wave=0, far-field=3
- XML 解析提示: `junk after document element: line 343, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | steady |  |  |  |  |  |  |
| MH | steady |  |  |  |  |  |  |
| TL | steady |  |  |  |  |  |  |
| LT | freq-domain | 1000 | 1 | 1 | 1 | 0 | 0 |

## 案例教程抽取

## GIS insulator 仿真模型介绍

## GIS insulator 模型

- 模型描述 - 仿真设置 - 后处理

### 模型描述

模型 GIS Insulator (气体绝缘子) 是电力系统中“气体绝缘金属封闭开关设备”的核心关键组件。该模型主要模拟高压电源线在受限空间内的电气绝缘特性，其结构由内部导电回路、环绕的固体绝缘材料（ep）以及填充的绝缘气体（sf6）组成，最外层为铝制（al）接地外壳。

> 图片: `./res/GIS_insulator_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Gis insulator\Gis insulator\res\GIS_insulator_1.png`

模型整体尺寸为 12.6 x 12.6 x 12.8 mm³。在材料属性上，模型详细定义了 ep 材料的介电常数、sf6 气体的热导率以及金属铝的电导率（38000 S/m），通过这种多介质包裹线路的设计，能够有效隔离高压电势并引导电流产生的热量通过外壳接地端进行消散。

### 仿真设置

1. 电热耦合多物理场仿真配置

WavEDA 通过预设的电热耦合接口，将电流场计算得出的损耗作为体热源引入固体传热场，从而精确评估绝缘子内部因电场集中引起局部温升的物理过程。

2. 稳态设置

在研究节点中，系统被配置为单稳态求解模式，旨在仿真设备在恒定运行电压下达到的最终热平衡状态，确保物理场结果的长期可靠性。

> 图片: `./res/GIS_insulator_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Gis insulator\Gis insulator\res\GIS_insulator_2.png`

3. 独立物理场边界条件设定

在电流学物理场中，通过选择顶部内导体表面定义为“终端”边界并加载激励，同时将外部筒体设置为“接地”；在热学物理场中，为外壳外表面添加“对流热通量”边界条件，以模拟绝缘子在真实散热环境下的热交换。

> 图片: `./res/GIS_insulator_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Gis insulator\Gis insulator\res\GIS_insulator_3.png`

4. 线接收器设置

设置线接收器选中走线表面两点右击创建，实际坐标为起始点（-1.01999e-14 , 3.2 , -1.4）和终止点（-1.00983e-15 , 6 , -7.34788e-16）位置坐标单位为 mm。

> 图片: `./res/GIS_insulator_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Gis insulator\Gis insulator\res\GIS_insulator_4.png`

### 后处理

1. 3D 网格

仿真完成后，进入显示网格窗口查看网格剖分情况。

> 图片: `./res/GIS_insulator_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Gis insulator\Gis insulator\res\GIS_insulator_5.png`

2. 查看线接收器结果

时域仿真完成后，鼠标右键点击工程树接收器处选择绘制线接收器随距离变化的电场和电势结果。

> 图片: `./res/GIS_insulator_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Gis insulator\Gis insulator\res\GIS_insulator_6.png`

3. 查看快照结果

仿真完成后，鼠标右键点击工程树快照结果查看电场、电流、电势、温度 3D 结果。

> 图片: `./res/GIS_insulator_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Gis insulator\Gis insulator\res\GIS_insulator_7.png`

## 图片资源

1. `./res/GIS_insulator_1.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Gis insulator\Gis insulator\res\GIS_insulator_1.png`
2. `./res/GIS_insulator_2.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Gis insulator\Gis insulator\res\GIS_insulator_2.png`
3. `./res/GIS_insulator_3.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Gis insulator\Gis insulator\res\GIS_insulator_3.png`
4. `./res/GIS_insulator_4.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Gis insulator\Gis insulator\res\GIS_insulator_4.png`
5. `./res/GIS_insulator_5.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Gis insulator\Gis insulator\res\GIS_insulator_5.png`
6. `./res/GIS_insulator_6.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Gis insulator\Gis insulator\res\GIS_insulator_6.png`
7. `./res/GIS_insulator_7.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Gis insulator\Gis insulator\res\GIS_insulator_7.png`
