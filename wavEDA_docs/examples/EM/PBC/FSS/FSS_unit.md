# 频率选择表面

- 案例分类: `EM`
- 来源 HTML: `D:\Staid\app\waveda\Example\EM\PBC\FSS\FSS_unit.html`
- 工程文件: `D:\Staid\app\waveda\Example\EM\PBC\FSS\FSS_unit.tsp`
- 截图数量: 9

## 工程摘要

- 工程类型: `EM`
- WavEDA 版本: `2.0.7527.2126`
- 坐标类型: `3d`
- 单位: `{"freq": "GHz", "thermal": "K", "length": "mm", "time": "ns"}`
- 求解器: `{"method": "fault", "solver": "fem", "basic": "2", "ray-tube-type": "0", "basicsem": "2", "save-path": "0"}`
- 计算区域/Domain: `{"gap": "0,0,0,0,0,0", "gapType": "user-define-gap", "shape-type": "box"}`
- 变量数量: 0
- 材料: Air, PEC
- 对象数量: face=4, solid=0, curve=0, lumped-port=0, wave-port=2, point-source=0, plane-wave=0, far-field=2
- XML 解析提示: `junk after document element: line 165, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | freq-domain | 0.01 | 25 | 201 | 0.12495 | 2 | 2 |
| MH | time-domain |  |  |  |  | 0 |  |
| TL | time-domain |  |  |  |  | 0 |  |
| LT | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |

## 案例教程抽取

## 频率选择表面

- 模型描述 - 仿真设置 - 后处理 - 参考文献

### 模型描述

此案例是一个频率选择表面模型，可以实现线极化到圆极化的转化。Zmin和 Zmax方向上是波端口馈电，四周为周期边界，扫频范围为0.01-25 GHz。

> 图片: `./res/FSS_unit_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\FSS\res\FSS_unit_1.png`

利用参考文献[1]中的几何参数，本案例在WavEDA中对FSS的几何进行建模。在本例中，首先建立结构是由一块零厚度的完美电导体薄片，后对这个薄片进行挖空处理得到一对自互补超表面,下图为本案例的几何。

接下来，添加了一个区域来定义计算域的边界，其几何大小取决于当前的仿真频段。定义了沿 X和Y方向的正确晶胞尺寸，这确保了S参数的正确计算。参考40 dB时的衰减量为7.8 mm，设置该计算域距离几何10 mm。

### 仿真设置

模型结构是零厚度的，材料设置为理想电导体。在绘制几何形状并定义材料后，下一步是分配边界和激励，FSS通常是周期性的散射体阵列。

1.边界设置

在X和Y方向上均设置了周期边界，该设置使得晶胞和激励在X和Y方向上周期性重复。关于周期边界的正确定义的详细说明可以在WavEDA帮助文档中找到。

> 图片: `./res/FSS_unit_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\FSS\res\FSS_unit_2.png`

> 图片: `./res/FSS_unit_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\FSS\res\FSS_unit_3.png`

2.端口设置

然后在模型域的Zmin和Zmax面添加波端口作为激励，在本例中，波端口的模式数为10。

> 图片: `./res/FSS_unit_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\FSS\res\FSS_unit_4.png`

3.网格设置

该模型利用自适应网格进行剖分，考虑几何尺寸大于半波长，为了保证仿真结果的准确性，在网格剖分时，设置采样率为18。

> 图片: `./res/FSS_unit_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\FSS\res\FSS_unit_5.png`

### 后处理

1.波端口模式

通过模式特性调整端口尺寸或匹配结构，减少反射。以下是该模型的两个波端口模式。

> 图片: `./res/FSS_unit_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\FSS\res\FSS_unit_6.png`

> 图片: `./res/FSS_unit_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\FSS\res\FSS_unit_7.png`

2.S参数幅值

可以看出在6.33 GHz和7.97 GHz处线极化到圆极化的转换。

> 图片: `./res/FSS_unit_8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\FSS\res\FSS_unit_8.png`

3.相位差

在几个频率处，正交极化的透射和反射系数的幅度在-3 dB的水平上交叉。在这些特定频率下，入射功率的一半被透射，而另一半被反射。相位图可以清楚地看出相位差是 90°。

> 图片: `./res/FSS_unit_9.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\FSS\res\FSS_unit_9.png`

### 参考文献

[1] J. D. Baena, A. P. Slobozhanyuk, J. D. Ortiz and P. A. Belov, "Linear to circular polarization converters based on self-complementary metasurfaces," 2014 8th International Congress on Advanced Electromagnetic Materials in Microwaves and Optics, Copenhagen, Denmark, 2014, pp. 43-45, doi: 10.1109/MetaMaterials.2014.6948588.

## 图片资源

1. `./res/FSS_unit_1.png` -> `D:\Staid\app\waveda\Example\EM\PBC\FSS\res\FSS_unit_1.png`
2. `./res/FSS_unit_2.png` -> `D:\Staid\app\waveda\Example\EM\PBC\FSS\res\FSS_unit_2.png`
3. `./res/FSS_unit_3.png` -> `D:\Staid\app\waveda\Example\EM\PBC\FSS\res\FSS_unit_3.png`
4. `./res/FSS_unit_4.png` -> `D:\Staid\app\waveda\Example\EM\PBC\FSS\res\FSS_unit_4.png`
5. `./res/FSS_unit_5.png` -> `D:\Staid\app\waveda\Example\EM\PBC\FSS\res\FSS_unit_5.png`
6. `./res/FSS_unit_6.png` -> `D:\Staid\app\waveda\Example\EM\PBC\FSS\res\FSS_unit_6.png`
7. `./res/FSS_unit_7.png` -> `D:\Staid\app\waveda\Example\EM\PBC\FSS\res\FSS_unit_7.png`
8. `./res/FSS_unit_8.png` -> `D:\Staid\app\waveda\Example\EM\PBC\FSS\res\FSS_unit_8.png`
9. `./res/FSS_unit_9.png` -> `D:\Staid\app\waveda\Example\EM\PBC\FSS\res\FSS_unit_9.png`
