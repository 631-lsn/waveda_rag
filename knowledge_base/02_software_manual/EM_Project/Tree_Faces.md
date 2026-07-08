---
title: "面节点"
merged_source: "current_waveda_agent_kb"
source_relative_path: "10_extracted_pages/EM_Project/Tree_Faces.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\10_extracted_pages\EM_Project\Tree_Faces.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 面节点

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Tree_Faces.html`
- 原始相对路径: `EM_Project/Tree_Faces.html`
- 知识模块: `EM设计与结果`

## 正文抽取
## 面节点

- 创建面 - 创建新组 - 删除、显示、隐藏以及反选功能 - 编辑求解物体内部属性 - 以材料分组 - 转换 - 转换导入的面 - 创建端口 - 沿轴扫描 - 沿路径扫描 - 对面加厚 - 其他功能

这里是面的右击功能介绍，如下图示意，右击程序树上的面内可触发一些快捷键，每个菜单项对应一个可用的命令，可以通过快捷键快速访问。

> 图片: `./images/Faces_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_1.png`

### 创建面

右击面可看见展开的几个节点，创建线内包括创建矩形、创建椭圆、创建多边形面、创建参数面、创建半椭球、创建圆锥面。以上几个模块有对应的帮助文档，可转跳继续查看。

> 图片: `./images/Faces_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_2.png`

### 创建新组

可通过创建分组来自定义面的分组和名称，同样点击下方的“展开所有节点”、“折叠所有节点”可以快速对现有面进行管理。

> 图片: `./images/Faces_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_3.png`

### 删除、显示、隐藏以及反选功能

通过右键可对现有面进行快捷操作：删除、显示、隐藏和反选创建的所有面。需要注意的是这里的反选功能是对工程文件内的所有面进行反选，即在隐藏A面，显示B面时选中此功能后的效果为显示A面，隐藏B面。

### 编辑求解物体内部属性

此功能可以结合实际设计需求判断是否需要对所创建面的内部属性进行求解，当去掉该选项时，将把该面设置成阻抗边界条件。注意该功能只对金属面有效。

> 图片: `./images/Faces_4.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_4.png`

### 属性

创建面后右键会出现如下方的菜单栏，可对该面进行编辑。属性栏右键继续衍生可对该面的材料、尺寸、透明度和网格尺寸进行修改。

> 图片: `./images/Faces_5.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_5.png`

### 转换

此功能可对选中的面进行阵列复制、移动、镜像、旋转、缩放、切割操作。详细操作见对应的帮助文档。

> 图片: `./images/Faces_7.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_7.png`

### 转换导入的面

此功能可针对导入的模型进行修正，支持转换成矩形，圆形，正多边形以及圆柱面。

> 图片: `./images/Faces_13.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_13.png`

选中导入的一个面右键进行转换操作，这里演示的是将导入的矩形转换成一个圆，在该对话框可进行是否转换操作，以及系统会提示转换结果。

> 图片: `./images/Faces_14.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_14.png`

最终转化的效果如图所示：蓝色矩形为导入几何，红色为转化后的几何。

> 图片: `./images/Faces_15.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_15.png`

### 创建端口

右键所选中的面可进行端口设置，根据实际需求选择创建端口的类型：波端口或者集总端口。关于端口创建详见对应的帮助文档。

### 沿轴扫描

沿轴扫描设置窗口如图所示。此功能用于创建体，在设置窗口进行旋转轴以及旋转角度的设置。

> 图片: `./images/Faces_11.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_11.png`

具体例子如下：旋转轴方向输入一个由旋转轴上一点和旋转轴方向构成的三维矢量，例如输入旋转轴上一点（0, 0, 0）、旋转轴方向（0, 1, 0）以及输入一个旋转角度360°，则该面将绕yoz面旋转得到对应的体。但需要注意的是旋转角度需要不小于0.0001。

勾选删除原物体后，则沿轴扫描功能只生成得到的体。不勾选该功能，软件将保留原有的面，并生成新的体。

### 沿路径扫描

沿路径扫描对话框如下图所示，具体操作可参照沿路径扫描。但需要注意的是要保证至少有一个面和一条线段。

> 图片: `./images/Faces_12.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_12.png`

### 对面加厚

对面加厚设置窗口如图所示。此功能用于对模型的选定表面进行加厚操作，可根据需求对正向面、反向面或两边同时加厚，生成具有厚度的实体结构。下拉方向对话框可选择要加厚的方向，加厚的厚度可以根据实际需求在对话框中进行设置。

> 图片: `./images/Faces_9.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_9.png`

### 其他功能

除上述功能外，右击线还有其他的快捷功能，支持复制粘贴线段、显示或隐藏网格、以及展开、折叠所有节点操作均可以在右击菜单栏内使用。

## 图片资源

1. `./images/Faces_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_1.png`
2. `./images/Faces_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_2.png`
3. `./images/Faces_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_3.png`
4. `./images/Faces_4.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_4.png`
5. `./images/Faces_5.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_5.png`
6. `./images/Faces_7.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_7.png`
7. `./images/Faces_13.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_13.png`
8. `./images/Faces_14.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_14.png`
9. `./images/Faces_15.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_15.png`
10. `./images/Faces_11.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_11.png`
11. `./images/Faces_12.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_12.png`
12. `./images/Faces_9.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Faces_9.png`

## 页内/相关链接

- - 创建面: `#创建面`
- - 创建面 - 创建新组: `#创建新组`
- - 创建面 - 创建新组 - 删除、显示、隐藏以及反选功能: `#删除、显示、隐藏以及反选功能`
- - 创建面 - 创建新组 - 删除、显示、隐藏以及反选功能 - 编辑求解物体内部属性: `#编辑求解物体内部属性`
- - 创建面 - 创建新组 - 删除、显示、隐藏以及反选功能 - 编辑求解物体内部属性 - 以材料分组: `#以材料分组`
- - 创建面 - 创建新组 - 删除、显示、隐藏以及反选功能 - 编辑求解物体内部属性 - 以材料分组 - 转换: `#转换`
- - 创建面 - 创建新组 - 删除、显示、隐藏以及反选功能 - 编辑求解物体内部属性 - 以材料分组 - 转换 - 转换导入的面: `#转换导入的面`
- - 创建面 - 创建新组 - 删除、显示、隐藏以及反选功能 - 编辑求解物体内部属性 - 以材料分组 - 转换 - 转换导入的面 - 创建端口: `#创建端口`
- - 创建面 - 创建新组 - 删除、显示、隐藏以及反选功能 - 编辑求解物体内部属性 - 以材料分组 - 转换 - 转换导入的面 - 创建端口 - 沿轴扫描: `#沿轴扫描`
- - 创建面 - 创建新组 - 删除、显示、隐藏以及反选功能 - 编辑求解物体内部属性 - 以材料分组 - 转换 - 转换导入的面 - 创建端口 - 沿轴扫描 - 沿路径扫描: `#沿路径扫描`
- - 创建面 - 创建新组 - 删除、显示、隐藏以及反选功能 - 编辑求解物体内部属性 - 以材料分组 - 转换 - 转换导入的面 - 创建端口 - 沿轴扫描 - 沿路径扫描 - 对面加厚: `#对面加厚`
- - 创建面 - 创建新组 - 删除、显示、隐藏以及反选功能 - 编辑求解物体内部属性 - 以材料分组 - 转换 - 转换导入的面 - 创建端口 - 沿轴扫描 - 沿路径扫描 - 对面加厚 - 其他功能: `#其他功能`
- 右击面可看见展开的几个节点，创建线内包括创建矩形: `../Modeling/Create_Face/Rectangle.html`
- 右击面可看见展开的几个节点，创建线内包括创建矩形、创建椭圆: `../Modeling/Create_Face/Ellipse.html`
- 右击面可看见展开的几个节点，创建线内包括创建矩形、创建椭圆、创建多边形面: `../Modeling/Create_Face/Polygon.html`
- 右击面可看见展开的几个节点，创建线内包括创建矩形、创建椭圆、创建多边形面、创建参数面: `../Modeling/Create_Face/Parametric_Face.html`
- 右击面可看见展开的几个节点，创建线内包括创建矩形、创建椭圆、创建多边形面、创建参数面、创建半椭球: `../Modeling/Create_Face/Semiellipsoid_Face.html`
- 右击面可看见展开的几个节点，创建线内包括创建矩形、创建椭圆、创建多边形面、创建参数面、创建半椭球、创建圆锥面: `../Modeling/Create_Face/Cone_Face.html`
- 此功能可对选中的面进行阵列复制: `../Modeling/Model_Editing/Array_Copy.html`
- 此功能可对选中的面进行阵列复制、移动: `../Modeling/Model_Editing/Translate.html`
- 此功能可对选中的面进行阵列复制、移动、镜像: `../Modeling/Model_Editing/Mirror.html`
- 此功能可对选中的面进行阵列复制、移动、镜像、旋转: `../Modeling/Model_Editing/Rotate.html`
- 此功能可对选中的面进行阵列复制、移动、镜像、旋转、缩放: `../Modeling/Model_Editing/Scale.html`
- 此功能可对选中的面进行阵列复制、移动、镜像、旋转、缩放、切割: `../Modeling/Model_Editing/Split.html`
- 右键所选中的面可进行端口设置，根据实际需求选择创建端口的类型：波端口: `../Modeling/Stimulate/Wave_Port.html`
- 右键所选中的面可进行端口设置，根据实际需求选择创建端口的类型：波端口或者集总端口: `../Modeling/Stimulate/Lumped_Port.html`
- 沿路径扫描对话框如下图所示，具体操作可参照沿路径扫描: `./Sweep_Along_Path.html`
