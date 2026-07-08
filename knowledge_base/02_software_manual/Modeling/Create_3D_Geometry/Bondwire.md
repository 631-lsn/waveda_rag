---
title: "键合线"
merged_source: "current_waveda_agent_kb"
source_relative_path: "10_extracted_pages/Modeling/Create_3D_Geometry/Bondwire.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\10_extracted_pages\Modeling\Create_3D_Geometry\Bondwire.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 键合线

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\Bondwire.html`
- 原始相对路径: `Modeling/Create_3D_Geometry/Bondwire.html`
- 知识模块: `建模总览`

## 正文抽取
## 键合线

此对话框用于创建键合线形状物体。键合线尺寸可使用数字或变量(变量表达式)输入， 其位置支持全局坐标以及局部坐标定义。 每个键合线将被赋予一种材料，同时也会被赋予该材料的颜色属性。 键合线的名称为其唯一标识符，一旦一个新的键合线被定义，将在树-体这一栏中列出。下图为键合线的示意图：

> 图片: `./images/Bondwire_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Bondwire_1.png`

### 名称

给键合线赋一个唯一的名称。

### 材料

在下拉列表中选择键合线的材料。

### 透明度

拖动滑块可改变键合线透明度，100是完全透明。

### 颜色

选择键合线在画布中显示的颜色。若未修改，默认显示为赋予材料的颜色。

### 建模

通过给定起始点坐标，终止点坐标，高度，延展方向以及截面圆半径等来定义键合线。 注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。

### 其他

键合线的直径在此设置。若勾选设为曲线勾选框，则生成一条穿过键合线中心，与键合线形状一样的弧线。 设为曲线操作不可逆，若设为曲线，阻抗边界勾选框会开启。

> 图片: `./images/Bondwire_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Bondwire_2.png`

### 相关文档

长方体， 球，圆锥/棱锥， 环，圆柱， 棱柱，环形螺旋线圈， 阿基米德螺旋线。

## 图片资源

1. `./images/Bondwire_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Bondwire_1.png`
2. `./images/Bondwire_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Bondwire_2.png`

## 页内/相关链接

- 此对话框用于创建键合线形状物体。键合线尺寸可使用数字或变量: `../../Tool/Variables.html`
- 此对话框用于创建键合线形状物体。键合线尺寸可使用数字或变量(变量表达式)输入， 其位置支持全局坐标以及局部坐标: `../LCS.html`
- 此对话框用于创建键合线形状物体。键合线尺寸可使用数字或变量(变量表达式)输入， 其位置支持全局坐标以及局部坐标定义。 每个键合线将被赋予一种材料: `../Bkg_Mat/Materials.html`
- 长方体: `./Box.html`
- 长方体， 球: `./Sphere.html`
- 长方体， 球，圆锥/棱锥: `./Cone.html`
- 长方体， 球，圆锥/棱锥， 环: `./Torus.html`
- 长方体， 球，圆锥/棱锥， 环，圆柱: `./Cylinder.html`
- 长方体， 球，圆锥/棱锥， 环，圆柱， 棱柱: `./Prism.html`
- 长方体， 球，圆锥/棱锥， 环，圆柱， 棱柱，环形螺旋线圈: `./Toroidal_spiral.html`
- 长方体， 球，圆锥/棱锥， 环，圆柱， 棱柱，环形螺旋线圈， 阿基米德螺旋线: `./Archimedean_spiral.html`
