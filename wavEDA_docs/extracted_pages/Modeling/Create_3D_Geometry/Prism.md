# 棱柱

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\Prism.html`
- 原始相对路径: `Modeling/Create_3D_Geometry/Prism.html`
- 知识模块: `建模总览`

## 正文抽取
## 棱柱

此对话框用于创建棱柱形状物体。棱柱尺寸可使用数字或变量(变量表达式)输入， 其位置支持全局坐标以及局部坐标定义。 每个棱柱将被赋予一种材料，同时也会被赋予该材料的颜色属性。 棱柱的名称为其唯一标识符，一旦一个新的棱柱被定义，将在树-体这一栏中列出。下图为棱柱的示意图：

> 图片: `./images/Prism_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Prism_1.png`

### 名称

给棱柱赋一个唯一的名称。

### 材料

在下拉列表中选择棱柱的材料。

### 透明度

拖动滑块可改变棱柱透明度，100是完全透明。

### 颜色

选择棱柱在画布中显示的颜色。若未修改，默认显示为赋予材料的颜色。

### 建模

通过定义底面中点，底面多边形起始点以及高度来定义棱柱。 注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。

### 规则多边形复选框

如下图所示，若勾选该规则多边形复选框，则底部建模为正多边形。

> 图片: `./images/Prism_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Prism_2.png`

反之若需创建底面为非正多边形的棱柱，可点击编辑多边形，进入编辑多边形窗口窗口。

### 画图模式

点击菜单栏画图模式直至其图标变暗，可开启画图模式。开启画图模式后可通过双击选取建模视图中的点来创建物体。 画图模式下，WavEDA默认创建正六边形棱柱，创建步骤为先确定底面中点以及多边形外圆半径，最后选取一点确定棱柱的高度，从而完成创建过程。

### 相关文档

长方体， 球， 圆锥/棱锥， 环，圆柱， 阿基米德螺旋线， 环形螺旋线圈， 键合线 。

## 图片资源

1. `./images/Prism_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Prism_1.png`
2. `./images/Prism_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Prism_2.png`

## 页内/相关链接

- 此对话框用于创建棱柱形状物体。棱柱尺寸可使用数字或变量: `../../Tool/Variables.html`
- 此对话框用于创建棱柱形状物体。棱柱尺寸可使用数字或变量(变量表达式)输入， 其位置支持全局坐标以及局部坐标: `../LCS.html`
- 此对话框用于创建棱柱形状物体。棱柱尺寸可使用数字或变量(变量表达式)输入， 其位置支持全局坐标以及局部坐标定义。 每个棱柱将被赋予一种材料: `../Bkg_Mat/Materials.html`
- 反之若需创建底面为非正多边形的棱柱，可点击编辑多边形，进入编辑多边形窗口: `../Create_Face/Edit_Polygon.html`
- 长方体: `./Box.html`
- 长方体， 球: `./Sphere.html`
- 长方体， 球， 圆锥/棱锥: `./Cone.html`
- 长方体， 球， 圆锥/棱锥， 环: `./Torus.html`
- 长方体， 球， 圆锥/棱锥， 环，圆柱: `./Cylinder.html`
- 长方体， 球， 圆锥/棱锥， 环，圆柱， 阿基米德螺旋线: `./Archimedean_Spiral.html`
- 长方体， 球， 圆锥/棱锥， 环，圆柱， 阿基米德螺旋线， 环形螺旋线圈: `./Toroidal_Spiral.html`
- 长方体， 球， 圆锥/棱锥， 环，圆柱， 阿基米德螺旋线， 环形螺旋线圈， 键合线: `./Bondwire.html`
