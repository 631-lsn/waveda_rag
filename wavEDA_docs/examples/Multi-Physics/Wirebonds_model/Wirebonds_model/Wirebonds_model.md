# Wirebonds model

- 案例分类: `Multi-Physics`
- 来源 HTML: `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\Wirebonds_model.html`
- 工程文件: `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\Wirebonds_model.tsp`
- 截图数量: 16

## 工程摘要

- 工程类型: `EM,Thermal,Elastic`
- WavEDA 版本: `2.0.7072.1937`
- 坐标类型: `3d`
- 单位: `{"thermal": "K", "freq": "Hz", "length": "mm", "time": "s"}`
- 求解器: `{"basicsem": "2", "number-of-intersection": "1", "save-path": "1", "ray-tube-type": "0", "basic": "2", "method": "fault", "solver": "fem"}`
- 计算区域/Domain: `{"gap": "0", "shape-type": "solid", "gapType": "auto-gap"}`
- 变量数量: 0
- 材料: Air, PEC, copper1, FR4, PP, solder, gold, silicon, silicon1
- 对象数量: face=6, solid=129, curve=0, lumped-port=0, wave-port=0, point-source=0, plane-wave=0, far-field=3
- XML 解析提示: `junk after document element: line 1224, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | time-domain |  |  |  |  | 0 |  |
| MH | time-domain |  |  |  |  | 0 |  |
| TL | time-domain |  |  |  |  | 0 |  |
| LT | freq-domain | 1e+09 | 1 | 1 | 1 | 0 | 0 |

## 案例教程抽取

## Wirebonds model

- 模型描述 - 仿真设置 - 后处理

### 模型描述

本模型为Wirebonds封装模型，芯片Die的材料为Silicon，通过键合线与下层走线连接，键合线材料为Gold，走线材料为Copper，填充材料分别为PP和FR4。

> 图片: `./res/Wirebonds_model_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_1.png`

### 仿真设置

1. 多物理场设置 多物理场条件设置如下：在键合线顶端设置为0.05 V电压源，并加载分段脉冲函数，底端电压设置为0 V；封装结构的PCB外表面设置对流热通量边界条件，温度为293.15 K，对流热通量为10 W/m^2*K；结构底层基板设置固定约束。在0-10 s进行瞬态电热力仿真。

> 图片: `./res/Wirebonds_model_8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_8.png`

> 图片: `./res/Wirebonds_model_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_2.png`

> 图片: `./res/Wirebonds_model_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_3.png`

> 图片: `./res/Wirebonds_model_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_4.png`

> 图片: `./res/Wirebonds_model_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_5.png`

2. 仿真配置 选择电磁、热学、力学，并同时勾选电热耦合和热膨胀选项，仿真类型全部选择 Time Domain，进入设置界面后进行瞬态参数配置。具体设置如下图：

> 图片: `./res/Wirebonds_model_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_6.png`

> 图片: `./res/Wirebonds_model_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_7.png`

### 后处理

多物理场结果 仿真结束后，分别展开电磁结果、温度结果和力学结果三个节点，添加电势、温度、位移及应力等场分布。对已经添加的点接收器，同时可以查看模型上该点对应的场结果随时间的变化情况。如下图所示，分别展示了各个场的仿真结果，在电压较高的区域，温度、位移和应力也较大。

电场结果

> 图片: `./res/Wirebonds_model_13.gif`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_13.gif`

> 图片: `./res/Wirebonds_model_9.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_9.png`

温度结果

> 图片: `./res/Wirebonds_model_14.gif`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_14.gif`

> 图片: `./res/Wirebonds_model_10.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_10.png`

力学结果

> 图片: `./res/Wirebonds_model_15.gif`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_15.gif`

> 图片: `./res/Wirebonds_model_11.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_11.png`

> 图片: `./res/Wirebonds_model_16.gif`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_16.gif`

> 图片: `./res/Wirebonds_model_12.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_12.png`

## 图片资源

1. `./res/Wirebonds_model_1.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_1.png`
2. `./res/Wirebonds_model_8.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_8.png`
3. `./res/Wirebonds_model_2.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_2.png`
4. `./res/Wirebonds_model_3.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_3.png`
5. `./res/Wirebonds_model_4.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_4.png`
6. `./res/Wirebonds_model_5.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_5.png`
7. `./res/Wirebonds_model_6.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_6.png`
8. `./res/Wirebonds_model_7.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_7.png`
9. `./res/Wirebonds_model_13.gif` -> `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_13.gif`
10. `./res/Wirebonds_model_9.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_9.png`
11. `./res/Wirebonds_model_14.gif` -> `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_14.gif`
12. `./res/Wirebonds_model_10.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_10.png`
13. `./res/Wirebonds_model_15.gif` -> `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_15.gif`
14. `./res/Wirebonds_model_11.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_11.png`
15. `./res/Wirebonds_model_16.gif` -> `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_16.gif`
16. `./res/Wirebonds_model_12.png` -> `D:\Staid\app\waveda\Example\Multi-Physics\Wirebonds_model\Wirebonds_model\res\Wirebonds_model_12.png`
