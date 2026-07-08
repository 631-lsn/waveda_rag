---
title: "参数面"
merged_source: "current_waveda_agent_kb"
source_relative_path: "10_extracted_pages/Modeling/Create_Face/Parametric_Face.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\10_extracted_pages\Modeling\Create_Face\Parametric_Face.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 参数面

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\Parametric_Face.html`
- 原始相对路径: `Modeling/Create_Face/Parametric_Face.html`
- 知识模块: `建模总览`

## 正文抽取
## 参数面

此对话框用于创建参数面。参数面可使用数字或变量(变量表达式)定义， 其位置支持全局坐标以及局部坐标定义。 每个参数面将被赋予一种材料，同时也会被赋予该材料的颜色属性。 参数面的名称为其唯一标识符，一旦一个新的参数面被定义，将在树-面这一栏中列出。下图为参数面的示意图：

> 图片: `./images/Parametric_Face_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\images\Parametric_Face_1.png`

### 名称

给参数面赋一个唯一的名称。

### 材料

在下拉列表中选择参数面的材料。

### 透明度

拖动滑块可改变参数面透明度，100是完全透明。

### 颜色

选择多边形在建模视图显示的颜色。若未修改，默认显示为赋予材料的颜色。

### 参数化坐标

给参数面上点的坐标指定一个关于t1及t2的有效函数。 注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。

### 参数范围

给参数t1和t2指定取值范围。

### 高级选项

勾选虚拟面复选框可将该参数面参数面参数面设置为端口面，在仿真时不将其作为实体处理。

当面的材料为PEC以外的其他金属，此时阻抗边界条件复选框生效，若勾选该复选框可将此参数面参数面设置为阻抗边界条件。

当面的材料为PEC以外的其他金属，电穿透面复选框生效，勾选该复选框，可将此参数面定义为表面电流边界条件，此时可定义面的厚度。

### 相关文档

矩形， 椭圆， 多边形， 半椭球面， 圆锥面。

## 图片资源

1. `./images/Parametric_Face_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\images\Parametric_Face_1.png`

## 页内/相关链接

- 此对话框用于创建参数面。参数面可使用数字或变量: `../../Tool/Variables.html`
- 此对话框用于创建参数面。参数面可使用数字或变量(变量表达式)定义， 其位置支持全局坐标以及局部坐标: `../LCS.html`
- 此对话框用于创建参数面。参数面可使用数字或变量(变量表达式)定义， 其位置支持全局坐标以及局部坐标定义。 每个参数面将被赋予一种材料: `../Bkg_Mat/Materials.html`
- 矩形: `./Rectangle.html`
- 矩形， 椭圆: `./Ellipse.html`
- 矩形， 椭圆， 多边形: `./Polygon.html`
- 矩形， 椭圆， 多边形， 半椭球面: `./Semiellipsoid_Face.html`
- 矩形， 椭圆， 多边形， 半椭球面， 圆锥面: `./Cone_Face.html`
