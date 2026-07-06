# 毫米波IPD滤波器

- 案例分类: `EM`
- 来源 HTML: `D:\Staid\app\waveda\Example\EM\Filter\mmwave_bpf_IPD\mmwave_bpf_IPD.html`
- 工程文件: `D:\Staid\app\waveda\Example\EM\Filter\mmwave_bpf_IPD\mmwave_bpf_IPD.tsp`
- 截图数量: 7

## 工程摘要

- 工程类型: `EM`
- WavEDA 版本: `2.0.7527.2126`
- 坐标类型: `3d`
- 单位: `{"freq": "GHz", "thermal": "K", "length": "um", "time": "ns"}`
- 求解器: `{"method": "fault", "solver": "fem", "basic": "2", "ray-tube-type": "0", "basicsem": "2", "save-path": "0"}`
- 计算区域/Domain: `{"gap": "250,250,0,250,250,250", "gapType": "user-define-gap", "shape-type": "box"}`
- 变量数量: 0
- 材料: Air, PEC, SiN, GaAs
- 对象数量: face=10, solid=8, curve=0, lumped-port=2, wave-port=0, point-source=0, plane-wave=0, far-field=2
- XML 解析提示: `junk after document element: line 221, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | freq-domain | 1 | 56 | 276 | 0.2 | 2 | 1 |
| MH | time-domain |  |  |  |  | 0 |  |
| TL | time-domain |  |  |  |  | 0 |  |
| LT | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |

## 案例教程抽取

## 毫米波IPD滤波器

- 模型描述 - 仿真设置 - 后处理 - 参考文献

### 模型描述

毫米波宽带滤波器，通带为20 ~ 40 GHz。整个滤波器为微带线和耦合微带线组合结构，可通过奇偶模分析法计算得滤波器的传输零点。

采用基底为75um-GaAs的IPD工艺制造，GSG端口馈电，金属层用PEC面代替仿真，整体尺寸为1.265*2.468*0.075 mm3。

> 图片: `./res/mmwave_bpf_IPD_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Filter\mmwave_bpf_IPD\res\mmwave_bpf_IPD_1.png`

### 仿真设置

1. 仿真频率设置 该模型仿真频率为1 ~56 GHz。最大尺寸大概为0.23 λg@28 GHz ， 结构中存在薄层结构，网格会较多，可采用快速扫频方法计算。

> 图片: `./res/mmwave_bpf_IPD_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Filter\mmwave_bpf_IPD\res\mmwave_bpf_IPD_2.png`

2. Domain及边界条件设置 为节省计算成本，滤波器的Domain尺寸设计为距离模型250 um即可。 模型底部为金属面，因此模型底部方向的Domain可直接贴紧模型，且设置为PEC边界。

> 图片: `./res/mmwave_bpf_IPD_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Filter\mmwave_bpf_IPD\res\mmwave_bpf_IPD_3.png`

2. 网格设置 自适应网格频率设置为28 GHz，残差设置为0.02，具体设置如下图：

> 图片: `./res/mmwave_bpf_IPD_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Filter\mmwave_bpf_IPD\res\mmwave_bpf_IPD_4.png`

3. 创建端口 为方便测试，原模型为GSG端口，但仿真中只需从GSG端口的信号线馈电。 从微带线到地，画一个与微带线等宽的面，创建集总面端口，端口积分线均设置为金属面垂直到地。

> 图片: `./res/mmwave_bpf_IPD_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Filter\mmwave_bpf_IPD\res\mmwave_bpf_IPD_5.png`

### 后处理

1. 3D网格 仿真完成后，选中关键部分物体，进入查看网格窗口查看网格剖分情况。

> 图片: `./res/mmwave_bpf_IPD_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Filter\mmwave_bpf_IPD\res\mmwave_bpf_IPD_6.png`

2. 仿真结果 仿真后添加S参数曲线查看该滤波器性能。

> 图片: `./res/mmwave_bpf_IPD_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Filter\mmwave_bpf_IPD\res\mmwave_bpf_IPD_7.png`

### 参考文献

[1] X. Zhang, Y. Wu, Y. Yang, H. Yu, W. Wang and W. Wang, "A Compact mm-Wave Bandpass Filter Based on Transversal Signal Interference Concept in IPD Technology," 2022 International Applied Computational Electromagnetics Society Symposium (ACES-China), Xuzhou, China, 2022, pp. 1-3, doi: 10.1109/ACES-China56081.2022.10064779.

## 图片资源

1. `./res/mmwave_bpf_IPD_1.png` -> `D:\Staid\app\waveda\Example\EM\Filter\mmwave_bpf_IPD\res\mmwave_bpf_IPD_1.png`
2. `./res/mmwave_bpf_IPD_2.png` -> `D:\Staid\app\waveda\Example\EM\Filter\mmwave_bpf_IPD\res\mmwave_bpf_IPD_2.png`
3. `./res/mmwave_bpf_IPD_3.png` -> `D:\Staid\app\waveda\Example\EM\Filter\mmwave_bpf_IPD\res\mmwave_bpf_IPD_3.png`
4. `./res/mmwave_bpf_IPD_4.png` -> `D:\Staid\app\waveda\Example\EM\Filter\mmwave_bpf_IPD\res\mmwave_bpf_IPD_4.png`
5. `./res/mmwave_bpf_IPD_5.png` -> `D:\Staid\app\waveda\Example\EM\Filter\mmwave_bpf_IPD\res\mmwave_bpf_IPD_5.png`
6. `./res/mmwave_bpf_IPD_6.png` -> `D:\Staid\app\waveda\Example\EM\Filter\mmwave_bpf_IPD\res\mmwave_bpf_IPD_6.png`
7. `./res/mmwave_bpf_IPD_7.png` -> `D:\Staid\app\waveda\Example\EM\Filter\mmwave_bpf_IPD\res\mmwave_bpf_IPD_7.png`
