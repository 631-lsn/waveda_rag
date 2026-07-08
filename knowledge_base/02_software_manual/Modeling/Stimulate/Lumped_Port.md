---
title: "集总端口"
merged_source: "current_waveda_agent_kb"
source_relative_path: "10_extracted_pages/Modeling/Stimulate/Lumped_Port.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\10_extracted_pages\Modeling\Stimulate\Lumped_Port.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 集总端口

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\Lumped_Port.html`
- 原始相对路径: `Modeling/Stimulate/Lumped_Port.html`
- 知识模块: `建模总览`

## 正文抽取
## 集总端口

- 集总端口类型 - 创建集总端口 - 设置差分对

在电磁仿真中，端口激励是用来模拟电磁波源和信号输入的一种方式。集总端口表示信号进入或离开设备的内部表面，用于激励设备和测量散射参数（S参数）的集总元件。

### 集总端口类型

WavEDA的集总端口分为集总面端口和集总线端口，如下图所示。

> 图片: `./images/Lumped_Port_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_2.png`

> 图片: `./images/Lumped_Port_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_1.png`

#### 集总面端口

WavEDA当前仅支持在圆环面和矩形面上建立集总面端口（绿色面），集总端口所在面的材料用户无法设置，软件默认为空气。

> 图片: `./images/Lumped_Port_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_3.png`

> 图片: `./images/Lumped_Port_4.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_4.png`

需要注意的是集总面端口仅支持上下边接触金属结构，集总面端口不可经过金属体的截面，如下图所示集总面端口（绿色面）不可与金属结构的横截面交叉（红色体结构）

> 图片: `./images/Lumped_Port_5.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_5.png`

#### 集总线端口

可以使用集总面端口的模型建议使用集总面端口。若无法建立集总面端口则使用集总线端口，如下图螺丝连接器模型所示，可在核心模型结构顶点与顶部PEC面之间建立集总线端口。

> 图片: `./images/Lumped_Port_6.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_6.png`

> 图片: `./images/Lumped_Port_7.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_7.png`

需要注意的是集总线端口的路径不可完全位于模型的外边界（即集总线端口不可完全贴着空气盒子）。

### 创建集总端口

集总端口的阻抗必须是大于零的实数，软件默认端口阻抗为50 Ω。所选面如果是一个独立的面，成功创建端口后此面会被自动移至“Ports”组下；所选面若是体结构上的一个面，则在“Ports”下会自动生成一个名称为lp-face面，若有多个端口则命名会以lp_face、lp_face_1、lp_face_2...类推。

> 图片: `./images/Lumped_Port_8.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_8.png`

#### 创建集总面端口

选面/体模式下，选中需要创建集总端口的面，点击“建模”栏下的“集总端口”，软件会默认给出集总面端口的积分线。若积分线方向并非用户所需要要，点击“反向”即可反转积分线方向。若积分线位置并非用户需要的，可以连续选中两个点并点击“选点”，则生成新的积分线。

> 图片: `./images/Lumped_Port_9.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_9.png`

创建集总面端口的方式：

- 用户建立了一个材料为空气的平面（矩形和圆环），在此面上定义集总面端口。

- 在选边模式下，选中两条平行的金属棱边，点击“集总端口”（或右击选择创建端口），WavEDA自动在选中的两条棱边之间生成一个集总面端口。

> 图片: `./images/Lumped_Port_10.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_10.png`

> 图片: `./images/Lumped_Port_11.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_11.png`

- 在选面模式下选中一个金属面，长按键盘Ctrl，切换至选边模式选中一条金属棱边，点击“集总端口”（或右击选择创建端口），在选中的面和棱边之间生成一个集总面端口。

> 图片: `./images/Lumped_Port_12.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_12.png`

#### 创建集总线端口

- 在选点模式下选中金属面/体上的两点，点击“集总端口”（或右击选择创建端口），WavEDA自动在选中的两点之间会生成集总线端口。

- 在选边模式下，选中金属棱边，长按键盘Ctrl，切换至选点模式选中一个点，点击“集总端口”（或右击选择创建端口），WavEDA自动在所选点和边之间生成一个积分路径最短的集总线端口。

- 在选面模式下，选中金属面，长按键盘Ctrl，切换至选点模式选中一个点，点击“集总端口”（或右击选择创建端口），WavEDA自动在所选点和面之间生成一个积分路径最短的集总线端口。

> 图片: `./images/Lumped_Port_13.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_13.png`

### 设置差分对

集总端口激励支持差分共模信号的仿真。在仿真前后均可右击工程树中的集总端口，选择"设置差分对"，弹出差分对设置窗口。

> 图片: `./images/Lumped_Port_14.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_14.png`

将需要配对的端口列入同一差分对中，设置差分阻抗与共模阻抗。设置好的差分对将在集总端口树下，WavEDA也支持差分共模与单端信号的混合仿真。

> 图片: `./images/Lumped_Port_15.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_15.png`

> 图片: `./images/Lumped_Port_16.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_16.png`

## 图片资源

1. `./images/Lumped_Port_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_2.png`
2. `./images/Lumped_Port_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_1.png`
3. `./images/Lumped_Port_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_3.png`
4. `./images/Lumped_Port_4.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_4.png`
5. `./images/Lumped_Port_5.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_5.png`
6. `./images/Lumped_Port_6.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_6.png`
7. `./images/Lumped_Port_7.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_7.png`
8. `./images/Lumped_Port_8.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_8.png`
9. `./images/Lumped_Port_9.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_9.png`
10. `./images/Lumped_Port_10.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_10.png`
11. `./images/Lumped_Port_11.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_11.png`
12. `./images/Lumped_Port_12.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_12.png`
13. `./images/Lumped_Port_13.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_13.png`
14. `./images/Lumped_Port_14.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_14.png`
15. `./images/Lumped_Port_15.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_15.png`
16. `./images/Lumped_Port_16.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Lumped_Port_16.png`

## 页内/相关链接

- - 集总端口类型: `#集总端口类型`
- - 集总端口类型 - 创建集总端口: `#创建集总端口`
- - 集总端口类型 - 创建集总端口 - 设置差分对: `#设置差分对`
