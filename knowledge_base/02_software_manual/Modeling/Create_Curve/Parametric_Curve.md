---
title: "3D参数曲线"
merged_source: "current_waveda_agent_kb"
source_relative_path: "Modeling/Create_Curve/Parametric_Curve.html"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 3D参数曲线

- 原始相对路径: `Modeling/Create_Curve/Parametric_Curve.html`
- 知识模块: `建模总览`

## 正文抽取
## 3D参数曲线

此对话框用于创建参数曲线。参数曲线尺寸可使用数字或变量(变量表达式)输入， 其位置支持全局坐标以及局部坐标定义。 每条参数曲线将被赋予一种材料，同时也会被赋予该材料的颜色属性。 参数曲线的名称为其唯一标识符，一旦一条新的参数曲线被定义，将在树-线这一栏中列出。下图为参数曲线的示意图：

> 图示要点：`Parametric_Curve_2.png` 展示“3D参数曲线”相关的操作界面或示例，后续审查通过后再补图。

### 名称

给参数曲线赋一个唯一的名称。

### 材料

曲线的材料只能是PEC。

### 参数范围

给参数t指定取值范围。

### 参数曲线的创建

给参数面上点的坐标指定一个关于t的有效函数。 注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。

### 相关文档

直线， 折线， 弧线。

## 页内/相关链接

- 此对话框用于创建参数曲线。参数曲线尺寸可使用数字或变量: `../../Tool/Variables.html`
- 此对话框用于创建参数曲线。参数曲线尺寸可使用数字或变量(变量表达式)输入， 其位置支持全局坐标以及局部坐标: `../LCS.html`
- 此对话框用于创建参数曲线。参数曲线尺寸可使用数字或变量(变量表达式)输入， 其位置支持全局坐标以及局部坐标定义。 每条参数曲线将被赋予一种材料: `../Bkg_Mat/Materials.html`
- 直线: `./Line.html`
- 直线， 折线: `./Polyline.html`
- 直线， 折线， 弧线: `./Circular_Arc.html`


## 待补图片清单
以下图片暂不插入正文，路径为 WavEDA 帮助文档内部相对路径；运行时 agent 会按项目内帮助图片和用户本机 WavEDA 帮助目录进行查找。
| 图片名称 | WavEDA 帮助相对路径 | 建议保留原因 |
| --- | --- | --- |
| Parametric_Curve_2.png | `Modeling/Create_Curve/images/Parametric_Curve_2.png` | 展示“3D参数曲线”的结果入口或查看界面，便于新人确认后处理位置。 |
