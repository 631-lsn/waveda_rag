# 双频带微带天线

- 案例分类: `EM`
- 来源 HTML: `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\dual_band_antenna.html`
- 工程文件: `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\dual_band_antenna.tsp`
- 截图数量: 9

## 工程摘要

- 工程类型: `EM`
- WavEDA 版本: `1.1.4031.1031.    (Alpha)`
- 坐标类型: `3d`
- 单位: `{"time": "ns", "thermal": "K", "length": "mm", "freq": "GHz"}`
- 求解器: `{"basic": "2", "method": "fault", "solver": "fem"}`
- 计算区域/Domain: `{"gapType": "user-define-gap", "shape-type": "box", "gap": "30"}`
- 变量数量: 12
- 材料: Air, PEC, FR-4
- 对象数量: face=4, solid=1, curve=0, lumped-port=1, wave-port=0, point-source=0, plane-wave=0, far-field=1

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | freq-domain | 2 | 6 | 100 | 0.040404 | 2 | 2 |

### 变量摘要

| 变量 | 表达式 |
| --- | --- |
| h | 1.6 |
| w1 | 2 |
| w2 | 1.5 |
| d | 20 |
| d1 | 24 |
| d2 | 16 |
| a | 20 |
| s | 1 |
| g | 4 |
| l | 60 |
| w | 50 |
| wf | 3 |

## 案例教程抽取

## 双频带微带天线

- 模型描述 - 仿真设置 - 后处理

### 模型描述

此模型利用了微带线结构和接地面结构的对称性来调节天线的共振频率，生成两个不同频率的共振模式，确保天线在目标频段（2-6 GHz）内的稳定工作。在设计频段内保持50 Ω阻抗匹配，以确保信号的高效传输。 该设计的双频带天线适用于多个通信系统，尤其是在需要宽频带支持的无线通信、雷达系统和多功能无线设备中。

整体模型尺寸为60x50x1.6 mm³，基底的材料为FR-4（介电常数为4.4，损耗角正切为0.02），微带线和金属地的材料都是PEC，边界条件为一阶吸收边界。

> 图片: `./res/dual_band_antenna_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\res\dual_band_antenna_1.png`

### 仿真设置

1. 仿真频率和网格划分 该模型使用软件自适应网格进行剖分，使用集总面端口馈电，仿真范围在 2 - 6 GHz。 采用自适应网格进行剖分，自适应网格频率设置为6 GHz，具体设置如下图。

> 图片: `./res/dual_band_antenna_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\res\dual_band_antenna_2.png`

2. 创建端口 采用集总面端口，WavEDA支持自动创建积分线并识别端口面的方向。

> 图片: `./res/dual_band_antenna_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\res\dual_band_antenna_3.png`

3. 计算区域设置 WaEDA可以根据用户给定的频率点设置对应的计算外边界大小，本案例以2.4 GHz为参考频点计算出对应的空气盒子大小为四分之一波长（30 mm），确保天线计算的准确性。

> 图片: `./res/dual_band_antenna_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\res\dual_band_antenna_4.png`

4. 添加远场监测点 选择第一个谐振点（2.4 GHz）作为远场监测点。

> 图片: `./res/dual_band_antenna_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\res\dual_band_antenna_5.png`

### 后处理

1. 网格查看 网格剖分完成后，选中目标体或面，进入View Mesh窗口网格剖分情况。

> 图片: `./res/dual_band_antenna_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\res\dual_band_antenna_6.png`

2. S参数结果 仿真结束查看模型的S参数，通过添加标记点查看S参数的谐振点的信息，分别在2.4 GHz和5.3 GHz出现谐振点，达到双频带天线的设计目标。 如下图：

> 图片: `./res/dual_band_antenna_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\res\dual_band_antenna_7.png`

3. 远场结果 查看添加的远场监测点的增益，可以查看三维结果、直角坐标系结果和极坐标结果。2.4 GHz下远场增益如图，远场相关信息在左下角显示。

> 图片: `./res/dual_band_antenna_8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\res\dual_band_antenna_8.png`

> 图片: `./res/dual_band_antenna_9.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\res\dual_band_antenna_9.png`

## 图片资源

1. `./res/dual_band_antenna_1.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\res\dual_band_antenna_1.png`
2. `./res/dual_band_antenna_2.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\res\dual_band_antenna_2.png`
3. `./res/dual_band_antenna_3.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\res\dual_band_antenna_3.png`
4. `./res/dual_band_antenna_4.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\res\dual_band_antenna_4.png`
5. `./res/dual_band_antenna_5.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\res\dual_band_antenna_5.png`
6. `./res/dual_band_antenna_6.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\res\dual_band_antenna_6.png`
7. `./res/dual_band_antenna_7.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\res\dual_band_antenna_7.png`
8. `./res/dual_band_antenna_8.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\res\dual_band_antenna_8.png`
9. `./res/dual_band_antenna_9.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\dual_band_antenna\res\dual_band_antenna_9.png`
