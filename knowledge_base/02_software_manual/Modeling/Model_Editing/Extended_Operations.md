---
title: "扩展操作"
merged_source: "current_waveda_agent_kb"
source_relative_path: "10_extracted_pages/Modeling/Model_Editing/Extended_Operations.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\10_extracted_pages\Modeling\Model_Editing\Extended_Operations.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 扩展操作

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\Extended_Operations.html`
- 原始相对路径: `Modeling/Model_Editing/Extended_Operations.html`
- 知识模块: `建模总览`

## 正文抽取
## 扩展操作

- 在选定面上创建一个面 - 加厚面 - 移除特征 - 在选定面上挖空体 - 在选定面上对齐体 - 连接 - 基于LCS(UV)切割物体 - 分割 - 沿轴扫描 - 沿路径扫描

#### 在选定面上创建一个面

支持在基于现有几何生成新的面，可以避免手动绘制的误差，提升建模速度。

步骤：在选面模式下选中现有模型几何上的面，右击菜单栏中选择“面操作”->“在选中的面上创建一个面”。此时可以在工程树上面节点下，查看到创建的新的面"face_1"。

> 图片: `./images/Extended_Operations_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extended_Operations_1.png`

#### 加厚面

对模型的选定表面进行加厚成实体。可根据需求对正向面、反向面或两边同时加厚，生成具有厚度的实体结构。具体操作可以查看 加厚面。

#### 移除特征

在工程树或模型中直接单击需移除的特征（如孔、倒角、拉伸体等）。此功能便于设计修正，移除错误或冗余特征（如误添加的孔、错误尺寸的凸台）；模型简化，为仿真分析减少网格复杂度，提升计算效率。

步骤：在选面模式下，选中特征操作的几何上的面，右击菜单栏中选择“面操作”->“移除特征”。此时可以看到该面上的特征操作（示例中的倒圆角面）被删除。

> 图片: `./images/Extended_Operations_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extended_Operations_2.png`

#### 在选定面上挖空体

通过选定体上的目标面，给定挖空后物体的厚度以及挖空后物体的延伸方向进行挖空。延伸方向可选择向内、向外或者两边均延伸。具体操作可以查看 挖空。

#### 在选定面上对齐体

将两个非连接且不对齐的体通过选定体上的目标面，以两个目标面的中心为基准，第二次选中的面为参考面对齐并连接。

步骤：在选面模式下，选中第一个体（工具体）上的一个面，再选择第二体（基体）的一个面作为参考面，右击菜单栏中选择“面操作”->“在选定面上对齐体”。可以看到两个体分别以选中的两个目标面的中点为中心，并以第二个体的面为参考面对齐在一起。

> 图片: `./images/Extended_Operations_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extended_Operations_3.png`

#### 连接

将两个非连接的物体，通过两个相邻面连接在一起并生成新的体。

步骤：在选面模式下，选中第一个体上的一个面，再选择第二体的一个面，右击菜单栏中选择“连接两个面创建一个体”。可以看到两个目标面的连接起来生成一个体。

> 图片: `./images/Extended_Operations_4.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extended_Operations_4.png`

#### 基于LCS(UV)切割物体

开启局部坐标系，根据局部坐标系的UV轴切割物体。可以修改局部坐标系的方向以及位置来确定切割平面。

> 图片: `./images/Extended_Operations_5.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extended_Operations_5.png`

#### 分割

将一个物体或面中包含多个互不相交的几何（体或面）分割成对应的多个物体。分割后的几何完全分离为独立的实体，并生成对应的实体名称在工程树显示。

#### 沿轴扫描

用于创建体，在设置窗口进行旋转轴以及旋转角度的设置。具体操作可以查看沿轴扫描。

#### 沿路径扫描

沿路径扫描得到的几何，通过两条线用于生成面，且原始线的起点和终点将作为生成面的其中一条边。具体操作可以查看沿路径扫描。

## 图片资源

1. `./images/Extended_Operations_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extended_Operations_1.png`
2. `./images/Extended_Operations_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extended_Operations_2.png`
3. `./images/Extended_Operations_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extended_Operations_3.png`
4. `./images/Extended_Operations_4.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extended_Operations_4.png`
5. `./images/Extended_Operations_5.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extended_Operations_5.png`

## 页内/相关链接

- - 在选定面上创建一个面: `#在选定面上创建一个面`
- - 在选定面上创建一个面 - 加厚面: `#加厚面`
- - 在选定面上创建一个面 - 加厚面 - 移除特征: `#移除特征`
- - 在选定面上创建一个面 - 加厚面 - 移除特征 - 在选定面上挖空体: `#在选定面上挖空体`
- - 在选定面上创建一个面 - 加厚面 - 移除特征 - 在选定面上挖空体 - 在选定面上对齐体: `#在选定面上对齐体`
- - 在选定面上创建一个面 - 加厚面 - 移除特征 - 在选定面上挖空体 - 在选定面上对齐体 - 连接: `#连接`
- - 在选定面上创建一个面 - 加厚面 - 移除特征 - 在选定面上挖空体 - 在选定面上对齐体 - 连接 - 基于LCS(UV)切割物体: `#基于LCS(UV)切割物体`
- - 在选定面上创建一个面 - 加厚面 - 移除特征 - 在选定面上挖空体 - 在选定面上对齐体 - 连接 - 基于LCS(UV)切割物体 - 分割: `#分割`
- - 在选定面上创建一个面 - 加厚面 - 移除特征 - 在选定面上挖空体 - 在选定面上对齐体 - 连接 - 基于LCS(UV)切割物体 - 分割 - 沿轴扫描: `#沿轴扫描`
- - 在选定面上创建一个面 - 加厚面 - 移除特征 - 在选定面上挖空体 - 在选定面上对齐体 - 连接 - 基于LCS(UV)切割物体 - 分割 - 沿轴扫描 - 沿路径扫描: `#沿路径扫描`
- 对模型的选定表面进行加厚成实体。可根据需求对正向面、反向面或两边同时加厚，生成具有厚度的实体结构。具体操作可以查看 加厚面: `./Face_Thicken.html`
- 通过选定体上的目标面，给定挖空后物体的厚度以及挖空后物体的延伸方向进行挖空。延伸方向可选择向内、向外或者两边均延伸。具体操作可以查看 挖空: `./Shell.html`
- 用于创建体，在设置窗口进行旋转轴以及旋转角度的设置。具体操作可以查看沿轴扫描: `../../EM_Project/Sweep_Along_Axis.html`
- 沿路径扫描得到的几何，通过两条线用于生成面，且原始线的起点和终点将作为生成面的其中一条边。具体操作可以查看沿路径扫描: `../../EM_Project/Sweep_Along_Path.html`
