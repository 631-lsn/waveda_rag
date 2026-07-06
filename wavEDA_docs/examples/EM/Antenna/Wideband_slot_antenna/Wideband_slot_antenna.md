# 超宽带缝隙形天线

- 案例分类: `EM`
- 来源 HTML: `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\Wideband_slot_antenna.html`
- 工程文件: `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\Wideband_slot_antenna.tsp`
- 截图数量: 10

## 工程摘要

- 工程类型: `EM`
- WavEDA 版本: `1.1.4031.1031.    (Alpha)`
- 坐标类型: `3d`
- 单位: `{"thermal": "K", "freq": "GHz", "time": "ns", "length": "mm"}`
- 求解器: `{"method": "fault", "solver": "fem", "basic": "2"}`
- 计算区域/Domain: `{"shape-type": "box", "gap": "0,0,20,0,0,29.6", "gapType": "user-define-gap"}`
- 变量数量: 24
- 材料: Air, PEC, FR4
- 对象数量: face=7, solid=1, curve=0, lumped-port=0, wave-port=2, point-source=0, plane-wave=0, far-field=2

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | freq-domain | 1 | 11 | 101 | 0.1 | 2 | 1 |

### 变量摘要

| 变量 | 表达式 |
| --- | --- |
| W | 38.5 |
| L | 38.5 |
| W1 | 25.2 |
| L1 | 25.2 |
| W2 | 4 |
| W3 | 1.5 |
| W4 | 3 |
| L2 | 20.4 |
| L3 | 12 |
| L4 | 7.4 |
| D1 | 8 |
| D2 | 19.25 |
| D3 | 19.25 |
| D4 | 12.35 |
| D5 | 12.6 |
| D6 | 7.8 |
| G1 | 0.5 |
| G2 | 0.3 |
| S1 | 11.5 |
| S2 | 4.15 |
| S3 | 7.3 |
| S4 | 1.3 |
| hs | 1.6 |
| wx | sin(s4)+2*W |

## 案例教程抽取

## 超宽带缝隙形天线

- 模型描述 - 仿真设置 - 后处理

### 模型描述

本案例仿真超宽带缝隙形天线，工作频率为1-11 GHz，实现了小于-10 dB的带宽占比66.5%。两个谐振频率间隔5 GHz。 天线整体尺寸为38.5*38.5*1.6 mm³。

本案例在WavEDA中对天线的几何形状进行了建模。 首先建立结构是由一块尺寸为38.5*38.5*1.6 mm³的介质基板，并设置材料为FR-4，相对介电常数约为4.4，损耗角正切为0.02。结构采用微带线馈电，在微带线开口处采用阶梯阻抗变换作为阻抗匹配结构。背面设计蝶形缝隙，结合渐变微带馈线仿真。下图为模型几何。

> 图片: `./res/Wideband_slot_antenna_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_1.png`

### 仿真设置

1.计算域设置

接下来，添加了一个区域来定义计算域的边界,其几何大小取决于当前的仿真频段结合模型尺寸计算，设置整体的计算区域离模型几何20 mm的位置。并且确保波端口紧贴计算域边界，这确保了S参数的正确计算。

2.端口设置

然后在模型域的 X,Y 面添加波端口作为激励，积分线的关键设置，如下图所示。

> 图片: `./res/Wideband_slot_antenna_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_3.png`

3.网格设置

该模型利用自适应网格进行剖分，考虑几何尺寸大于半波长，为了保证仿真结果的准确性，在网格剖分时，自适应网格频率设置为8 GHz，设置采样率为10。

> 图片: `./res/Wideband_slot_antenna_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_4.png`

> 图片: `./res/Wideband_slot_antenna_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_2.png`

### 后处理

1.波端口模式

通过模式特性调整端口尺寸或匹配结构，减少反射。以下是该模型的两个波端口模式。

> 图片: `./res/Wideband_slot_antenna_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_5.png`

> 图片: `./res/Wideband_slot_antenna_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_6.png`

2.S参数

从S参数图可以本案例的天线性能，包括回波损耗和入射损耗。 S(1,1) 表示端口1的反射系数本案例S(1,1)在大部分频段（如3.0–10.0 GHz）低于-10 dB，表明该天线在超宽带范围内（UWB，通常3.1–10.6 GHz）具备良好的阻抗匹配特性。S(2,1)在超宽带范围内呈现显著波动，部分频段传输损耗较高。

> 图片: `./res/Wideband_slot_antenna_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_7.png`

> 图片: `./res/Wideband_slot_antenna_8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_8.png`

3.远场结果

在WavEDA的结果后处理内可以选则查看3D远场结果图，或者特殊角度下的平面远场结果。 辐射方向图半功率波瓣宽度（HPBW）>103°。

> 图片: `./res/Wideband_slot_antenna_9.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_9.png`

> 图片: `./res/Wideband_slot_antenna_10.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_10.png`

## 图片资源

1. `./res/Wideband_slot_antenna_1.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_1.png`
2. `./res/Wideband_slot_antenna_3.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_3.png`
3. `./res/Wideband_slot_antenna_4.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_4.png`
4. `./res/Wideband_slot_antenna_2.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_2.png`
5. `./res/Wideband_slot_antenna_5.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_5.png`
6. `./res/Wideband_slot_antenna_6.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_6.png`
7. `./res/Wideband_slot_antenna_7.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_7.png`
8. `./res/Wideband_slot_antenna_8.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_8.png`
9. `./res/Wideband_slot_antenna_9.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_9.png`
10. `./res/Wideband_slot_antenna_10.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\Wideband_slot_antenna\res\Wideband_slot_antenna_10.png`
