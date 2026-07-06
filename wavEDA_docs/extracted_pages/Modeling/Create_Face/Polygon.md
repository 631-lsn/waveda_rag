# 多边形面

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\Polygon.html`
- 原始相对路径: `Modeling/Create_Face/Polygon.html`
- 知识模块: `建模总览`

## 正文抽取
## 多边形

此对话框用于创建多边形面。多边形尺寸可使用数字或变量(变量表达式)输入， 其位置支持全局坐标以及变量定义。 每个多边形将被赋予一种材料，同时也会被赋予该材料的颜色属性。 多边形的名称为其唯一标识符，一旦一个新的多边形被定义，将在树-面这一栏中列出。下图为多边形的示意图：

> 图片: `./images/Polygon_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\images\Polygon_1.png`

### 名称

给多边形赋一个唯一的名称。

### 材料

在下拉列表中选择多边形的材料。

### 透明度

拖动滑块可改变多边形透明度，100是完全透明。

### 颜色

选择多边形在建模视图显示的颜色。若未修改，默认显示为赋予材料的颜色。

### 建模

通过给定多边形面中点，起始点以及多边形边数定义多边形位置和尺寸。 注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。

### 规则多边形复选框

如下图所示，若勾选该规则多边形复选框，则底部建模为正多边形。

> 图片: `./images/Polygon_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\images\Polygon_2.png`

反之若需创建底面为非正多边形面，可点击编辑多边形，进入编辑多边形窗口窗口。

### 高级选项

勾选虚拟面复选框可将该多边形面设置为端口面，在仿真时不将其作为实体处理。

当面的材料为PEC以外的其他金属，此时阻抗边界条件复选框生效，若勾选该复选框可将此多边形面设置为阻抗边界条件。

当面的材料为PEC以外的其他金属，电穿透面复选框生效，勾选该复选框，可将此多边形面定义为表面电流边界条件，此时可定义面的厚度。

### 画图模式

点击菜单栏画图模式直至其图标变暗，可开启画图模式。开启画图模式后可通过双击选取建模视图中的点来创建物体。 多边形面在画图模式下的创建步骤为依次选中多边形角点，最后以起始点结束，由所选点的连线围成多边形面。

### 相关文档

矩形， 椭圆， 参数面， 半椭球面， 圆锥面。

## 图片资源

1. `./images/Polygon_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\images\Polygon_1.png`
2. `./images/Polygon_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\images\Polygon_2.png`

## 页内/相关链接

- 此对话框用于创建多边形面。多边形尺寸可使用数字或变量: `../../Tool/Variables.html`
- 此对话框用于创建多边形面。多边形尺寸可使用数字或变量(变量表达式)输入， 其位置支持全局坐标以及变量: `../../Tool/Variables.html`
- 此对话框用于创建多边形面。多边形尺寸可使用数字或变量(变量表达式)输入， 其位置支持全局坐标以及变量定义。 每个多边形将被赋予一种材料: `../Bkg_Mat/Materials.html`
- 反之若需创建底面为非正多边形面，可点击编辑多边形，进入编辑多边形窗口: `./Edit_Polygon.html`
- 矩形: `./Rectangle.html`
- 矩形， 椭圆: `./Ellipse.html`
- 矩形， 椭圆， 参数面: `./Parametric_Face.html`
- 矩形， 椭圆， 参数面， 半椭球面: `./Semiellipsoid_Face.html`
- 矩形， 椭圆， 参数面， 半椭球面， 圆锥面: `./Cone_Face.html`
