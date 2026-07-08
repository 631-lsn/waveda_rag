---
title: "矩形"
merged_source: "current_waveda_agent_kb"
source_relative_path: "10_extracted_pages/Modeling/Create_Face/Rectangle.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\10_extracted_pages\Modeling\Create_Face\Rectangle.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 矩形

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\Rectangle.html`
- 原始相对路径: `Modeling/Create_Face/Rectangle.html`
- 知识模块: `建模总览`

## 正文抽取
## 矩形

此对话框用于创建矩形面。矩形尺寸可使用数字或变量(变量表达式)输入， 其位置支持全局坐标以及局部坐标定义。 每个矩形将被赋予一种材料，同时也会被赋予该材料的颜色属性。 矩形的名称为其唯一标识符，一旦一个新的矩形被定义，将在树-面这一栏中列出。下图为矩形的示意图：

> 图片: `./images/Rectangle_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\images\Rectangle_1.png`

### 名称

给矩形赋一个唯一的名称。

### 材料

在下拉列表中选择矩形的材料。

### 透明度

拖动滑块可改变矩形透明度，100是完全透明。

### 颜色

选择矩形在建模视图显示的颜色。若未修改，默认显示为赋予材料的颜色。

### 单角点模式

单角点模式定义矩形的示意图如下，通过输入矩形在x方向最小值，y方向最小值， 以及长度和宽度来定义矩形位置和尺寸。 注意一切均是基于原点(u,v,w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。

> 图片: `./images/Rectangle_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\images\Rectangle_2.png`

### 双角点模式

双角点模式定义矩形的示意图如下，通过输入长方体在X方向最小值，Y方向最小值 以及X方向最大值，Y方向最大值来定义矩形的位置和尺寸。 注意一切均是基于原点(u,v,w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。

> 图片: `./images/Rectangle_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\images\Rectangle_3.png`

### 中心点模式

中心点模式定义矩形的示意图如下，通过输入矩形中心点坐标 以及长度和宽度来定义矩形位置和尺寸。 注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。

> 图片: `./images/Rectangle_4.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\images\Rectangle_4.png`

### 高级选项

勾选虚拟面复选框可将该矩形面设置为端口面，在仿真时不将其作为实体处理。

当面的材料为PEC以外的其他金属，此时阻抗边界条件复选框生效，若勾选该复选框可将此矩形面设置为阻抗边界条件。

当面的材料为PEC以外的其他金属，电穿透面复选框生效，勾选该复选框，可将此矩形面定义为表面电流边界条件，此时可定义面的厚度。

### 画图模式

点击菜单栏画图模式直至其图标变暗，可开启画图模式。开启画图模式后可通过双击选取建模视图中的点来创建物体。 长方形在画图模式下的创建步骤为选中长方体两个对角点。

### 相关文档

椭圆， 多边形， 参数面， 半椭球面， 圆锥面。

## 图片资源

1. `./images/Rectangle_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\images\Rectangle_1.png`
2. `./images/Rectangle_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\images\Rectangle_2.png`
3. `./images/Rectangle_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\images\Rectangle_3.png`
4. `./images/Rectangle_4.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\images\Rectangle_4.png`

## 页内/相关链接

- 此对话框用于创建矩形面。矩形尺寸可使用数字或变量: `../../Tool/Variables.html`
- 此对话框用于创建矩形面。矩形尺寸可使用数字或变量(变量表达式)输入， 其位置支持全局坐标以及局部坐标: `../LCS.html`
- 此对话框用于创建矩形面。矩形尺寸可使用数字或变量(变量表达式)输入， 其位置支持全局坐标以及局部坐标定义。 每个矩形将被赋予一种材料: `../Bkg_Mat/Materials.html`
- 椭圆: `./Ellipse.html`
- 椭圆， 多边形: `./Polygon.html`
- 椭圆， 多边形， 参数面: `./Parametric_Face.html`
- 椭圆， 多边形， 参数面， 半椭球面: `./Semiellipsoid_Face.html`
- 椭圆， 多边形， 参数面， 半椭球面， 圆锥面: `./Cone_Face.html`
