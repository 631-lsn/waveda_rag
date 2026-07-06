# 威尔金森功分器

- 案例分类: `Circuit`
- 来源 HTML: `D:\Staid\app\waveda\Example\Circuit\Wilkinson power divider\Wilkinson power divider\Wilkinson power divider.html`
- 工程文件: `D:\Staid\app\waveda\Example\Circuit\Wilkinson power divider\Wilkinson power divider\Wilkinson power divider.tsp`
- 截图数量: 7

## 工程摘要

- 工程类型: `Circuit`
- WavEDA 版本: `1.3.6530.1784.    (Alpha)`
- 坐标类型: ``
- 单位: `{}`
- 求解器: `{}`
- 计算区域/Domain: `{}`
- 变量数量: 0
- 材料: 未抽取到
- 对象数量: face=0, solid=0, curve=0, lumped-port=0, wave-port=0, point-source=0, plane-wave=0, far-field=0

## 案例教程抽取

## 威尔金森功分器

- 模型描述 - 仿真设置 - 后处理

### 模型描述

本模型为一分二等分威尔金森功分器，工作频段覆盖2-3 GHz，采用微带线结构设计，核心包含阻抗匹配线段与隔离电阻，实现输入信号均等地分配到两路输出端，同时保障两个输出端口间的良好隔离度。电路示意图如下图所示：

> 图片: `./res/Wilkinson_power_divider_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Circuit\Wilkinson power divider\Wilkinson power divider\res\Wilkinson_power_divider_1.png`

### 仿真设置

1. 端口设置 在基础元器件中选择Term G作为端口，并设置端口的电压和电阻大小。

> 图片: `./res/Wilkinson_power_divider_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Circuit\Wilkinson power divider\Wilkinson power divider\res\Wilkinson_power_divider_2.png`

> 图片: `./res/Wilkinson_power_divider_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Circuit\Wilkinson power divider\Wilkinson power divider\res\Wilkinson_power_divider_3.png`

2. 仿真控件设置 在原理图中插入S参数仿真控件SP，扫描类型设置为Linear，仿真范围为2-3 GHz，步长为0.01 GHz。具体设置如下图：

> 图片: `./res/Wilkinson_power_divider_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Circuit\Wilkinson power divider\Wilkinson power divider\res\Wilkinson_power_divider_4.png`

> 图片: `./res/Wilkinson_power_divider_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Circuit\Wilkinson power divider\Wilkinson power divider\res\Wilkinson_power_divider_5.png`

### 后处理

S参数结果 电路创建完成后点击仿真，仿真结束后弹出结果窗口，在结果窗口中创建S参数曲线图，选择S11、S12、S13和S23创建结果，S11和S23射系数<-20dB，表明端口匹配性能和隔离度良好，S12、S13在工作频段内稳定在-3.01dB，实现等分输出的设计目标。 如下图所示。

> 图片: `./res/Wilkinson_power_divider_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Circuit\Wilkinson power divider\Wilkinson power divider\res\Wilkinson_power_divider_6.png`

> 图片: `./res/Wilkinson_power_divider_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Circuit\Wilkinson power divider\Wilkinson power divider\res\Wilkinson_power_divider_7.png`

## 图片资源

1. `./res/Wilkinson_power_divider_1.png` -> `D:\Staid\app\waveda\Example\Circuit\Wilkinson power divider\Wilkinson power divider\res\Wilkinson_power_divider_1.png`
2. `./res/Wilkinson_power_divider_2.png` -> `D:\Staid\app\waveda\Example\Circuit\Wilkinson power divider\Wilkinson power divider\res\Wilkinson_power_divider_2.png`
3. `./res/Wilkinson_power_divider_3.png` -> `D:\Staid\app\waveda\Example\Circuit\Wilkinson power divider\Wilkinson power divider\res\Wilkinson_power_divider_3.png`
4. `./res/Wilkinson_power_divider_4.png` -> `D:\Staid\app\waveda\Example\Circuit\Wilkinson power divider\Wilkinson power divider\res\Wilkinson_power_divider_4.png`
5. `./res/Wilkinson_power_divider_5.png` -> `D:\Staid\app\waveda\Example\Circuit\Wilkinson power divider\Wilkinson power divider\res\Wilkinson_power_divider_5.png`
6. `./res/Wilkinson_power_divider_6.png` -> `D:\Staid\app\waveda\Example\Circuit\Wilkinson power divider\Wilkinson power divider\res\Wilkinson_power_divider_6.png`
7. `./res/Wilkinson_power_divider_7.png` -> `D:\Staid\app\waveda\Example\Circuit\Wilkinson power divider\Wilkinson power divider\res\Wilkinson_power_divider_7.png`
