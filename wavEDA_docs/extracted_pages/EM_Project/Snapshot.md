# 快照

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Snapshot.html`
- 原始相对路径: `EM_Project/Snapshot.html`
- 知识模块: `EM设计与结果`

## 正文抽取
## 快照

- 快照（Snapshot） - 快照设置 - 面快照 - 体快照 - 快照仿真后结果查看

这里主要用于仿真前添加场监视设置，以便仿真后能查看场分布，包括电场、磁场、电流等；场监视设置主要包括：设置监视频点、被监视面、被监视体，主要分为以下步骤：

- 快照设置（监视频点）；

- 定义面快照或者体块照；

- 快照结果查看。

### 快照（Snapshot）

> 图片: `images/Snapshot1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot1.png`

### 快照设置

如图，在工程树上选中快照设置，双击，进入如下对话框：

> 图片: `images/Snapshot3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot3.png`

在该对话框中需要设置：

- 网格质量（默认5）；

- 需要在频率左边小框内点打钩（默认不勾选：表示默认不添加场监视）；

- 在需要被监视的频率的左边检查列表对应的方框内打钩，表示监视该频点，数量按需；

- 点击完成。

### 面快照

> 图片: `images/Snapshot5.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot5.png`

如图，选中面快照，右键，点击新建面快照，进入如下图对话框（定义监视面）：

> 图片: `images/Snapshot6.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot6.png`

在该对话框中需要设置：

- 被定义面的名称；

- 形状（支持矩形、圆/椭圆）以及设置各类形状面对应的坐标、尺寸等，具体关于如何建面的操作介绍可以参考 如何建面文档；

- 记录场默认为电场、磁场以及各个分量。

下方点击预览，可以查看刚才建立的面监视区域效果；点击完成后，自动关闭对话框。

面快照建立后节点生成

面快照建立后会自动生成节点，选中该节点右键，可以对其进行二次编辑与修改、删除以及调整其视图。

> 图片: `images/Snapshot7.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot7.png`

### 体快照

> 图片: `images/Snapshot8.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot8.png`

如图，选中面快照，右键，点击新建体快照，进入如下图对话框（定义监视体）：

> 图片: `images/Snapshot9.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot9.png`

在该对话框中需要设置 ：

- 被定义体的名称；

- 体形状对应的坐标、尺寸等，具体关于如何建面的操作介绍可以参考 如何建体文档；

- 记录场默认为电场、磁场以及各个分量；

下方点击预览，可以查看刚才建立的面监视区域效果；点击完成后，自动关闭对话框。

体快照建立后节点生成

如图，体快照建立后会自动生成节点，选中该节点右键，可以对其进行二次编辑与修改、删除以及调整其视图。

> 图片: `images/Snapshot10.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot10.png`

### 快照结果查看

> 图片: `images/Snapshot11.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot11.png`

如图，在电磁结果中点击快照，可以查看面快照与体快照结果；如点击面快照前面小黑三角形，则可以将面快照展开，且看到它下面的节点名称（face_snapshot_2），双击该节点则可以进入查看该面快照结果（场分布），如下图，另外关于该部分快照结果查看的详细说明，也可以参考 快照结果查看文档。

> 图片: `images/Snapshot12.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot12.png`

## 图片资源

1. `images/Snapshot1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot1.png`
2. `images/Snapshot3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot3.png`
3. `images/Snapshot5.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot5.png`
4. `images/Snapshot6.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot6.png`
5. `images/Snapshot7.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot7.png`
6. `images/Snapshot8.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot8.png`
7. `images/Snapshot9.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot9.png`
8. `images/Snapshot10.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot10.png`
9. `images/Snapshot11.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot11.png`
10. `images/Snapshot12.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Snapshot12.png`

## 页内/相关链接

- - 快照（Snapshot）: `#length`
- - 快照（Snapshot） - 快照设置: `#Time`
- - 快照（Snapshot） - 快照设置 - 面快照: `#Frequency`
- - 快照（Snapshot） - 快照设置 - 面快照 - 体快照: `#F`
- - 快照（Snapshot） - 快照设置 - 面快照 - 体快照 - 快照仿真后结果查看: `#Fr`
- 形状（支持矩形、圆/椭圆）以及设置各类形状面对应的坐标、尺寸等，具体关于如何建面的操作介绍可以参考 如何建面: `../Modeling/Create_Face/Rectangle.html`
- 体形状对应的坐标、尺寸等，具体关于如何建面的操作介绍可以参考 如何建体: `../Modeling/Create_3D_Geometry/Box.html`
- 如图，在电磁结果中点击快照，可以查看面快照与体快照结果；如点击面快照前面小黑三角形，则可以将面快照展开，且看到它下面的节点名称（face_snapshot_2），双击该节点则可以进入查看该面快照结果（场分布），如下图，另外关于该部分快照结果查看的详细说明，也可以参考 快照结果查看: `./EM_Results.html`
