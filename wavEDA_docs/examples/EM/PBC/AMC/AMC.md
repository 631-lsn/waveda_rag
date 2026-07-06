# 人工磁体单元胞

- 案例分类: `EM`
- 来源 HTML: `D:\Staid\app\waveda\Example\EM\PBC\AMC\AMC.html`
- 工程文件: `D:\Staid\app\waveda\Example\EM\PBC\AMC\AMC.tsp`
- 截图数量: 9

## 工程摘要

- 工程类型: `EM`
- WavEDA 版本: `1.1.3985.1031.    (Alpha)`
- 坐标类型: `3d`
- 单位: `{"thermal": "K", "freq": "GHz", "time": "ns", "length": "mm"}`
- 求解器: `{"method": "fault", "solver": "fem", "basic": "2"}`
- 计算区域/Domain: `{"gap": "0", "gapType": "no-gap", "shape-type": "box"}`
- 变量数量: 7
- 材料: Air, PEC, Rogers RT5880
- 对象数量: face=4, solid=2, curve=0, lumped-port=0, wave-port=1, point-source=0, plane-wave=0, far-field=0

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | freq-domain | 2 | 8 | 61 | 0.1 | 2 | 2 |

### 变量摘要

| 变量 | 表达式 |
| --- | --- |
| SL | 28.6 |
| SW | 28.6 |
| H | 3.15 |
| OUTP | 24.5 |
| CUTP | 21.5 |
| INP | 15.5 |
| BOXH | 80 |

## 案例教程抽取

## 人工磁体单元胞

- 模型描述 - 仿真设置 - 后处理 - 参考文献

### 模型描述

人工磁体单元胞(Artificial Magnetic Unit Cell，AMC)是一种通过人工周期性结构(如超材料或电磁带隙结构)实现特定电磁特性的功能单元， 模型示意图如下图所示。

> 图片: `./res/AMC_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\AMC\res\AMC_1.png`

该AMC单元由Rogers RT5880介电衬底，金属接地平面，顶部为矩形外环的金属贴片散热器组成，边界条件为周期边界条件。

### 仿真设置

1. 仿真频率及网格设置 该模型仿真频率设置为2-8 GHz，扫频方式选择快速(离散/插值也适用)。 设置网格采样率为10 PPW，采用自适应网格进行剖分，自适应网格频率设置为8 GHz，残差设置为WavEDA默认值0.01，具体设置如下图：

> 图片: `./res/AMC_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\AMC\res\AMC_2.png`

> 图片: `./res/AMC_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\AMC\res\AMC_3.png`

2. 边界条件设置 设置-X、+X方向为一对周期边界，-Y、+Y方向为另一对周期边界，设置扫描角为theta=0°、phi=0°，设置方法与示意图如下图所示：

> 图片: `./res/AMC_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\AMC\res\AMC_4.png`

3. 创建端口 模型激励采用波端口馈电，在上图中已显示端口，端口设置如下图所示：

> 图片: `./res/AMC_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\AMC\res\AMC_5.png`

### 后处理

1. 3D网格 仿真完成后，选中关键部分物体，进入显示网格窗口查看网格剖分情况。

> 图片: `./res/AMC_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\AMC\res\AMC_6.png`

2. 端口模式 查看波端口模式以更好地了解模型特性，查看波端口模式如下图所示：

> 图片: `./res/AMC_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\AMC\res\AMC_7.png`

3. 共模S参数结果 端口结果可从工程树端口处访问，添加S(1:1,1:1)结果查看AMC结构性能。

> 图片: `./res/AMC_8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\AMC\res\AMC_8.png`

> 图片: `./res/AMC_9.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\AMC\res\AMC_9.png`

### 参考文献

[1] T. Nuzhat and M. N. Hasan, "Artificial Magnetic Conductor Unit Cell Design Using Machine Learning Algorithms," 2022 IEEE International IOT, Electronics and Mechatronics Conference (IEMTRONICS), Toronto, ON, Canada, 2022, pp. 1-7, doi: 10.1109/IEMTRONICS55184.2022.9795851.

## 图片资源

1. `./res/AMC_1.png` -> `D:\Staid\app\waveda\Example\EM\PBC\AMC\res\AMC_1.png`
2. `./res/AMC_2.png` -> `D:\Staid\app\waveda\Example\EM\PBC\AMC\res\AMC_2.png`
3. `./res/AMC_3.png` -> `D:\Staid\app\waveda\Example\EM\PBC\AMC\res\AMC_3.png`
4. `./res/AMC_4.png` -> `D:\Staid\app\waveda\Example\EM\PBC\AMC\res\AMC_4.png`
5. `./res/AMC_5.png` -> `D:\Staid\app\waveda\Example\EM\PBC\AMC\res\AMC_5.png`
6. `./res/AMC_6.png` -> `D:\Staid\app\waveda\Example\EM\PBC\AMC\res\AMC_6.png`
7. `./res/AMC_7.png` -> `D:\Staid\app\waveda\Example\EM\PBC\AMC\res\AMC_7.png`
8. `./res/AMC_8.png` -> `D:\Staid\app\waveda\Example\EM\PBC\AMC\res\AMC_8.png`
9. `./res/AMC_9.png` -> `D:\Staid\app\waveda\Example\EM\PBC\AMC\res\AMC_9.png`
