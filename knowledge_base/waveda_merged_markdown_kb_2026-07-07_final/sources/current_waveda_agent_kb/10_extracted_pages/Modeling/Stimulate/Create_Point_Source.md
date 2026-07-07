---
title: "点激励源"
merged_source: "current_waveda_agent_kb"
source_relative_path: "10_extracted_pages/Modeling/Stimulate/Create_Point_Source.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\10_extracted_pages\Modeling\Stimulate\Create_Point_Source.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 点激励源

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\Create_Point_Source.html`
- 原始相对路径: `Modeling/Stimulate/Create_Point_Source.html`
- 知识模块: `建模总览`

## 正文抽取
## 点激励源

- 形式 - 坐标 - 极化 - 阵列排序

点激励源是一种理想化的激励方式，通常用于模拟从单个点或局部位置发射的电磁波。它与波端口、集总面端口或平面波不同，点激励源通常用于模拟非常局部的激励源。它适合用于那些难以通过面激励或其他形式的激励来表达的复杂结构。WavEDA仅支持快速扫频和离散扫频时，添加点激励源进行计算。用户可以在选点模式下，选中某个点在下拉菜单底部创建点激励源，也可在程序树上通过激励源-点激励源来添加。

#### 点激励源的应用场景：

- 天线馈电： 在某些天线设计中，尤其是复杂结构或非常局部的馈电源，点激励源可以模拟电流从某个点开始发射，进一步分析天线的辐射和接收特性。

- 微波电路： 对于一些微波电路中的特定元件，如微波放大器、功率分配器等，可以使用点激励源来模拟局部电流或电压源的影响。

> 图片: `./images//Create_Point_Source_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Create_Point_Source_1.png`

### 形式

WavEDA点激励源有两种形式，电偶极子（Electric Dipole）和 磁偶极子（Magnetic Dipole）作为点激励源时有着不同的工作原理、使用场景、仿真运算方法以及仿真结果的差异。它们主要的区别在于电场和磁场的产生方式、使用的物理模型以及它们的应用场景。

> 图片: `./images/Create_Point_Source_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Create_Point_Source_2.png`

#### 电偶极子：

- 工作原理

电偶极子主要影响电场，它产生的电场主要表现为电荷间的相互作用，电场的分布通常呈现出辐射状的结构。

- 应用场景

天线设计：电偶极子通常用于分析和设计与电场相关的天线，特别是在低频和中频范围，适用于小型天线设计或低增益天线。

辐射特性分析：电偶极子常常用于模拟从源点（例如天线的馈电端）发出的电磁波，分析电场分布和辐射模式，特别是在有明显电场成分的区域。

电磁波传播：适用于模拟电磁波在自由空间中传播，特别是在需要模拟电场辐射源的场合。

- 仿真结果

辐射模式：电偶极子的仿真结果通常表现为电场的分布和辐射模式。例如，天线的辐射图可以展示电场的方向、强度以及辐射角度。

增益和方向性：电偶极子的仿真结果中，通常会关注天线的增益和方向性，例如分析天线的指向性和电场强度在不同角度下的分布。

输入阻抗：电偶极子还可以用来分析输入阻抗，确定天线的电场特性是否与馈电源匹配。

#### 磁偶极子:

- 工作原理

磁偶极子主要影响磁场，它产生的磁场是通过磁矩与电流的相互作用产生的。与电偶极子的电场辐射不同，磁偶极子则会产生一种旋转的磁场模式。

- 应用场景

磁性材料分析：磁偶极子常用于分析和模拟磁性材料或结构的辐射和响应，尤其在高频应用中，可以帮助分析由磁场激励的设备，如微波器件中的磁场行为。

天线设计：磁偶极子也常用于分析具有磁场响应的天线或电磁波源，尤其是对磁场有特殊要求的天线设计。

- 仿真结果

磁场分布：磁偶极子的仿真结果通常展示为磁场的分布和磁矩的行为，特别是在与导体、磁性材料等交互时。

磁场辐射：磁偶极子的仿真结果强调磁场的辐射模式和磁场的方向性。仿真结果可以用于分析设备在外部磁场激励下的反应，或磁场如何影响电流流动。

共振频率：磁偶极子的仿真也可以关注共振频率，即磁偶极子在特定频率下的最大辐射或响应。

### 坐标

对于点激励源，输入对应的三维坐标即可，选定激励源的位置。

### 极化

电偶极子极化方向通常与偶极矩方向一致，即电场沿着偶极子的轴振荡，产生的辐射主要依赖电场的变化。 磁偶极子是磁场激励源，其极化方向通常与磁偶极矩的方向一致，即磁场沿着偶极子的磁矩方向变化。其辐射模式主要与磁场变化相关，产生的电磁波的电场和磁场是相互垂直的。 WavEDA的默认极化方向是（0,0,1）。

### 阵列排序

阵列排序为点激励源提供三个方向的排序，勾选方向后，用户可以自定义这个方向的位移大小，以及需要复制的数量。位移的单位参考全局系统的默认单位。具体可以参考阵列复制。

> 图片: `./images/Create_Point_Source_6.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Create_Point_Source_6.png`

效果图如下，方向框后数值代表着xyz方向，为0则无位移，大小表示该方向的位移。数量框后数值代表该方向的阵列量。整体的阵列排序个数为三个方向数量的乘积。

> 图片: `./images/Create_Point_Source_5.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Create_Point_Source_5.png`

### 选点

对于选点功能，在建模窗口用快捷键切换到选点模式，点击需要的点，WavEDA将在被选中的点上设置点激励源。

## 图片资源

1. `./images//Create_Point_Source_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Create_Point_Source_1.png`
2. `./images/Create_Point_Source_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Create_Point_Source_2.png`
3. `./images/Create_Point_Source_6.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Create_Point_Source_6.png`
4. `./images/Create_Point_Source_5.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Create_Point_Source_5.png`

## 页内/相关链接

- - 形式: `#形式`
- - 形式 - 坐标: `#坐标`
- - 形式 - 坐标 - 极化: `#极化`
- - 形式 - 坐标 - 极化 - 阵列排序: `#阵列排序`
- 阵列排序为点激励源提供三个方向的排序，勾选方向后，用户可以自定义这个方向的位移大小，以及需要复制的数量。位移的单位参考全局系统的默认单位。具体可以参考阵列复制: `../Model_Editing/Array_Copy.html`
