# 基片集成波导耦合器

- 案例分类: `EM`
- 来源 HTML: `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\HMSIW_coupler.html`
- 工程文件: `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\HMSIW_coupler.tsp`
- 截图数量: 9

## 工程摘要

- 工程类型: `EM`
- WavEDA 版本: `2.0.7527.2126`
- 坐标类型: `3d`
- 单位: `{"freq": "GHz", "thermal": "K", "length": "mm", "time": "ns"}`
- 求解器: `{"method": "fault", "solver": "fem", "basic": "2", "ray-tube-type": "0", "basicsem": "2", "save-path": "0"}`
- 计算区域/Domain: `{"gap": "5", "gapType": "user-define-gap", "shape-type": "box"}`
- 变量数量: 12
- 材料: Air, PEC, Sub
- 对象数量: face=7, solid=41, curve=0, lumped-port=4, wave-port=0, point-source=0, plane-wave=0, far-field=2
- XML 解析提示: `junk after document element: line 1022, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | freq-domain | 14 | 24 | 201 | 0.05 | 2 | 1 |
| MH | time-domain |  |  |  |  | 0 |  |
| TL | time-domain |  |  |  |  | 0 |  |
| LT | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |

### 变量摘要

| 变量 | 表达式 |
| --- | --- |
| Wms | 1.5 |
| Ltr | 11 |
| Lvsp | 0.8 |
| Lslot | 21.5 |
| Rms | 5.25 |
| Whsiw | 6 |
| Wint | 1.5 |
| Wslot | 0.8 |
| Wtr | 3.5 |
| Rvia | 0.25 |
| L | Lslot+5*2 |
| W | Whsiw+5 |

## 案例教程抽取

## 基片集成波导耦合器

- 模型描述 - 仿真设置 - 后处理

### 模型描述

本案例中半模基片集成波导定向耦合器，将两个HMSIW接地板介质重叠，通过将接地板开槽实现能量耦合，特别说明缝隙是在中间的那层接地板，不在上层与下层微带上。

介质基板材料为FR4，介电常数为2.2，损耗角正切为0.009， 金属采用PEC，如下图：

> 图片: `res/HMSIW_Coupler_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\res\HMSIW_Coupler_1.png`

### 仿真设置

1. 仿真频率及网格设置 该模型仿真频率设置为14 ~ 24GHz，扫频方式选快速（离散/插值也适用）。 具体设置如下图：

> 图片: `res/HMSIW_Coupler_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\res\HMSIW_Coupler_7.png`

2. 创建端口 采用集总面端口馈电，包括四个端口，如下图：

> 图片: `res/HMSIW_Coupler_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\res\HMSIW_Coupler_2.png`

3.网格剖分 未采用自适应网格，没有对局部物体进行单独加密，采用了默认网格进行剖分,如下图(局部网格尺寸默认为-1)，如下图：

> 图片: `res/HMSIW_Coupler_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\res\HMSIW_Coupler_3.png`

### 后处理

1. 模型网格 仿真完成后，在模型窗口右键，进入View Mesh窗口网格剖分情况。

> 图片: `res/HMSIW_Coupler_9.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\res\HMSIW_Coupler_9.png`

> 图片: `res/HMSIW_Coupler_10.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\res\HMSIW_Coupler_10.png`

2.S参数结果 仿真后可以在电磁结果端口中通过获取S参数，以查看该耦合器性能。 如下图：

> 图片: `res/HMSIW_Coupler_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\res\HMSIW_Coupler_4.png`

3. Snapshot结果仿真后可以在电磁结果快照中查看Snapshot，本模型分为上层SIW，下层SIW,如下图：

Snapshot结果(上层SIW)：

> 图片: `res/HMSIW_Coupler_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\res\HMSIW_Coupler_5.png`

Snapshot结果(下层SIW)：

> 图片: `res/HMSIW_Coupler_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\res\HMSIW_Coupler_6.png`

由以上S参数以及Snapshot结果来看，该耦合器具有较高的方向性与隔离度。

### 参考文献

[1] Wu K. Integration and interconnect techniques of planar and nonplanar structures for microwave and millimeter-wave cir-Cuits-current status and future trend. 2001 Asia-Pacific Microwave Conf Proc, Taiwan , 2001.

## 图片资源

1. `res/HMSIW_Coupler_1.png` -> `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\res\HMSIW_Coupler_1.png`
2. `res/HMSIW_Coupler_7.png` -> `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\res\HMSIW_Coupler_7.png`
3. `res/HMSIW_Coupler_2.png` -> `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\res\HMSIW_Coupler_2.png`
4. `res/HMSIW_Coupler_3.png` -> `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\res\HMSIW_Coupler_3.png`
5. `res/HMSIW_Coupler_9.png` -> `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\res\HMSIW_Coupler_9.png`
6. `res/HMSIW_Coupler_10.png` -> `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\res\HMSIW_Coupler_10.png`
7. `res/HMSIW_Coupler_4.png` -> `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\res\HMSIW_Coupler_4.png`
8. `res/HMSIW_Coupler_5.png` -> `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\res\HMSIW_Coupler_5.png`
9. `res/HMSIW_Coupler_6.png` -> `D:\Staid\app\waveda\Example\EM\Coupler\HMSIW_Coupler\res\HMSIW_Coupler_6.png`
