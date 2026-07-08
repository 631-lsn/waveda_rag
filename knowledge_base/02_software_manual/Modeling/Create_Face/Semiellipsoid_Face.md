---
title: "半椭球面"
merged_source: "current_waveda_agent_kb"
source_relative_path: "10_extracted_pages/Modeling/Create_Face/Semiellipsoid_Face.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\10_extracted_pages\Modeling\Create_Face\Semiellipsoid_Face.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 半椭球面

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\Semiellipsoid_Face.html`
- 原始相对路径: `Modeling/Create_Face/Semiellipsoid_Face.html`
- 知识模块: `建模总览`

## 正文抽取
## 半椭球面

此对话框用于创建半椭球面。半椭球面可使用数字或变量(变量表达式)定义， 其位置支持全局坐标以及局部坐标定义。 每个半椭球面将被赋予一种材料，同时也会被赋予该材料的颜色属性。 半椭球面的名称为其唯一标识符，一旦一个新的半椭球面被定义，将在树-面这一栏中列出。下图为半椭球面的示意图：

> 图片: `./images/Semiellipsoid_Face_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\images\Semiellipsoid_Face_1.png`

### 名称

给半椭球面赋一个唯一的名称。

### 材料

在下拉列表中选择半椭球面的材料。

### 透明度

拖动滑块可改变半椭球面透明度，100是完全透明。

### 颜色

选择半椭球面在建模视图显示的颜色。若未修改，默认显示为赋予材料的颜色。

### 建模

通过给定半椭球面中心点，球半径以及弧度定义半椭球面位置和尺寸。若未勾选球复选框，则需要定义中心横截面的椭圆长半轴以及短半轴。 注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。

### 高级选项

勾选虚拟面复选框可将该参数面半椭球面参数面设置为端口面，在仿真时不将其作为实体处理。

当面的材料为PEC以外的其他金属，此时阻抗边界条件复选框生效，若勾选该复选框可将此半椭球面参数面设置为阻抗边界条件。

当面的材料为PEC以外的其他金属，电穿透面复选框生效，勾选该复选框，可将此半椭球面定义为表面电流边界条件，此时可定义面的厚度。

### 相关文档

矩形， 椭圆， 多边形， 参数面， 圆锥面。

## 图片资源

1. `./images/Semiellipsoid_Face_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\images\Semiellipsoid_Face_1.png`

## 页内/相关链接

- 此对话框用于创建半椭球面。半椭球面可使用数字或变量: `../../Tool/Variables.html`
- 此对话框用于创建半椭球面。半椭球面可使用数字或变量(变量表达式)定义， 其位置支持全局坐标以及局部坐标: `../LCS.html`
- 此对话框用于创建半椭球面。半椭球面可使用数字或变量(变量表达式)定义， 其位置支持全局坐标以及局部坐标定义。 每个半椭球面将被赋予一种材料: `../Bkg_Mat/Materials.html`
- 矩形: `./Rectangle.html`
- 矩形， 椭圆: `./Ellipse.html`
- 矩形， 椭圆， 多边形: `./Polygon.html`
- 矩形， 椭圆， 多边形， 参数面: `./Parametric_Face.html`
- 矩形， 椭圆， 多边形， 参数面， 圆锥面: `./Cone_Face.html`
