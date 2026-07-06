# SIW双频带滤波器

- 案例分类: `EM`
- 来源 HTML: `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\SIW_dual_band_filter.html`
- 工程文件: `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\SIW_dual_band_filter.tsp`
- 截图数量: 9

## 工程摘要

- 工程类型: `EM`
- WavEDA 版本: `2.0.7527.2126`
- 坐标类型: `3d`
- 单位: `{"freq": "GHz", "thermal": "K", "length": "mm", "time": "ns"}`
- 求解器: `{"method": "fault", "solver": "fem", "basic": "2", "ray-tube-type": "0", "basicsem": "2", "save-path": "0"}`
- 计算区域/Domain: `{"gap": "2,2,0,2,2,2", "gapType": "user-define-gap", "shape-type": "box"}`
- 变量数量: 8
- 材料: Air, PEC, TLX-6
- 对象数量: face=3, solid=60, curve=0, lumped-port=2, wave-port=0, point-source=0, plane-wave=0, far-field=2
- XML 解析提示: `junk after document element: line 761, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | freq-domain | 1 | 9 | 161 | 0.05 | 2 | 1 |
| MH | time-domain |  |  |  |  | 0 |  |
| TL | time-domain |  |  |  |  | 0 |  |
| LT | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |

### 变量摘要

| 变量 | 表达式 |
| --- | --- |
| h | 1.016 |
| s | 2.1 |
| w2 | 3.9 |
| le1 | 0.5 |
| le2 | 7.4 |
| c1 | 1.8 |
| c2 | 3.6 |
| lw | 23.2 |

## 案例教程抽取

## SIW双频带滤波器

- 模型描述 - 仿真设置 - 后处理

### 模型描述

基片集成波导双频段滤波器，双频带分别为2.13 GHz ~ 2.56 GHz，5.42 GHz ~ 6.05 GHz。 滤波器整体尺寸为52.8*31.3*1.016 mm3，基底的介电常数为2.65，中间金属通孔为copper。

> 图片: `./res/SIW_dual_band_filter_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\res\SIW_dual_band_filter_1.png`

### 仿真设置

1. 仿真频率设置 该模型仿真频率为1~9 GHz，为观察SIW腔体内场分布，采用快速扫频方法进行仿真。

> 图片: `./res/SIW_dual_band_filter_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\res\SIW_dual_band_filter_2.png`

2. Domain及边界条件设置 为节省计算成本，滤波器的Domain尺寸设计为距离模型2 mm即可。 模型底部为金属面，因此模型底部方向的Domain可直接贴紧模型，且设置为PEC边界。

> 图片: `./res/SIW_dual_band_filter_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\res\SIW_dual_band_filter_3.png`

2. 网格设置 自适应网格频率设置为5.67 GHz，残差设置为0.02，具体设置如下图：

> 图片: `./res/SIW_dual_band_filter_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\res\SIW_dual_band_filter_4.png`

3. 快照设置 在介质层上创建面Snaphot， 并选择Snapshot频点为第一通带和第二通带的中心频点2.3 GHz和5.7 GHz，并选择网格质量为30。

> 图片: `./res/SIW_dual_band_filter_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\res\SIW_dual_band_filter_5.png`

4. 创建端口 从微带线到地，画一个与微带线等宽的面，创建集总面端口，端口积分线均设置为金属面垂直到地。

> 图片: `./res/SIW_dual_band_filter_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\res\SIW_dual_band_filter_6.png`

### 后处理

1. 3D网格 仿真完成后，选中关键部分物体，进入查看网格窗口查看网格剖分情况。

> 图片: `./res/SIW_dual_band_filter_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\res\SIW_dual_band_filter_7.png`

2. Snapshot结果 直接点击对应Snapshot查看结果。

> 图片: `./res/SIW_dual_band_filter_8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\res\SIW_dual_band_filter_8.png`

2. 仿真结果 仿真后添加S参数曲线查看该滤波器性能。

> 图片: `./res/SIW_dual_band_filter_9.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\res\SIW_dual_band_filter_9.png`

## 图片资源

1. `./res/SIW_dual_band_filter_1.png` -> `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\res\SIW_dual_band_filter_1.png`
2. `./res/SIW_dual_band_filter_2.png` -> `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\res\SIW_dual_band_filter_2.png`
3. `./res/SIW_dual_band_filter_3.png` -> `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\res\SIW_dual_band_filter_3.png`
4. `./res/SIW_dual_band_filter_4.png` -> `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\res\SIW_dual_band_filter_4.png`
5. `./res/SIW_dual_band_filter_5.png` -> `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\res\SIW_dual_band_filter_5.png`
6. `./res/SIW_dual_band_filter_6.png` -> `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\res\SIW_dual_band_filter_6.png`
7. `./res/SIW_dual_band_filter_7.png` -> `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\res\SIW_dual_band_filter_7.png`
8. `./res/SIW_dual_band_filter_8.png` -> `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\res\SIW_dual_band_filter_8.png`
9. `./res/SIW_dual_band_filter_9.png` -> `D:\Staid\app\waveda\Example\EM\Filter\SIW_dual_band_filter\res\SIW_dual_band_filter_9.png`
