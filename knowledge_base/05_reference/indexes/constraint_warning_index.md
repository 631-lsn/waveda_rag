---
title: "限制、注意与疑似故障原因索引"
merged_source: "current_waveda_agent_kb"
source_relative_path: "20_indexes/constraint_warning_index.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\20_indexes\constraint_warning_index.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 限制、注意与疑似故障原因索引

本索引从帮助文档中抽取“必须、无法、不能、不可、不支持、注意、建议、检查、收敛、过大/过小”等语句。它不是完整报错库，但适合排查验证失败和仿真异常。

## EM设计与结果
- **边界**：## 边界
- 默认边界条件 - 设置边界条件
### 默认边界条件
默认边界条件选项可进行计算区域边界条件的设置。 来源：[10_extracted_pages/EM_Project/Boundary.md](../10_extracted_pages/EM_Project/Boundary.md)
- **远场**：### 编辑端口激励
> 图片: `images/far_field4.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field4.png`
如图，点击编辑端口激励，进入如下对话框，在此可以设置需要的端口激励组合，其中幅度默认为1 W，幅度填0表示不进行激励； 来源：[10_extracted_pages/EM_Project/Far_field.md](../10_extracted_pages/EM_Project/Far_field.md)
- **远场**：相位默认为0度，也可以设置其他角度，添加好激励组合后，可以点击完成，同时关闭该对话框。 来源：[10_extracted_pages/EM_Project/Far_field.md](../10_extracted_pages/EM_Project/Far_field.md)
- **场结果**：> 图片: `./images/Field_Result_20.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Field_Result_20.png`
### 注意事项
该场结果操作信息适用波端口模式显示与远场结果查看场信息。 来源：[10_extracted_pages/EM_Project/Field_Result.md](../10_extracted_pages/EM_Project/Field_Result.md)
- **快捷键**：#### 选定模型
点击选定模型，该模式下可以建模窗口上被选中的模型将锁定，所有的建模操作都将被锁定这单个几何上，且无法选中其他几何。 来源：[10_extracted_pages/EM_Project/HotKey.md](../10_extracted_pages/EM_Project/HotKey.md)
- **创建线接收器**：> 图片: `./images/Create_Line_Observer_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Observer\images\Create_Line_Observer_1.png`
### 直线
点击选项框中直线曲线类型，在曲线类型选项框右边可以填写点1和点2坐标或在建模窗口选择起始点1和终止点2创建线接收器，并通过设置数据点数设置直线由多少个数据点绘制而成，默认为100个数据点。 来源：[10_extracted_pages/EM_Project/Observer/Create_Line_Observer.md](../10_extracted_pages/EM_Project/Observer/Create_Line_Observer.md)
- **创建线接收器**：给参数线上点的坐标指定一个关于t的有效函数，并通过设置数据点数设置直线由多少个数据点绘制而成，默认为100个数据点。 来源：[10_extracted_pages/EM_Project/Observer/Create_Line_Observer.md](../10_extracted_pages/EM_Project/Observer/Create_Line_Observer.md)
- **创建线接收器**：注意一切均是基于原点(u, v, w)以及UV轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/EM_Project/Observer/Create_Line_Observer.md](../10_extracted_pages/EM_Project/Observer/Create_Line_Observer.md)
- **创建点接收器**：> 图片: `./images/Create_Point_Observer_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Observer\images\Create_Point_Observer_2.png`
### 输入接收器坐标
在接收器位置框中输入接收器x、y、z轴坐标，点击创建即可建立点接收器，同时创建多个点默认分为一个组，再次创建将会另分为一个组； 来源：[10_extracted_pages/EM_Project/Observer/Create_Point_Observer.md](../10_extracted_pages/EM_Project/Observer/Create_Point_Observer.md)
- **快照**：- 需要在频率左边小框内点打钩（默认不勾选：表示默认不添加场监视）； 来源：[10_extracted_pages/EM_Project/Snapshot.md](../10_extracted_pages/EM_Project/Snapshot.md)
- **快照**：- 在需要被监视的频率的左边检查列表对应的方框内打钩，表示监视该频点，数量按需； 来源：[10_extracted_pages/EM_Project/Snapshot.md](../10_extracted_pages/EM_Project/Snapshot.md)
- **快照**：- 记录场默认为电场、磁场以及各个分量。 来源：[10_extracted_pages/EM_Project/Snapshot.md](../10_extracted_pages/EM_Project/Snapshot.md)
- **快照**：- 记录场默认为电场、磁场以及各个分量； 来源：[10_extracted_pages/EM_Project/Snapshot.md](../10_extracted_pages/EM_Project/Snapshot.md)
- **沿轴扫描**：注意这个值需要大于等于0.0001。 来源：[10_extracted_pages/EM_Project/Sweep_Along_Axis.md](../10_extracted_pages/EM_Project/Sweep_Along_Axis.md)
- **面节点**：需要注意的是这里的反选功能是对工程文件内的所有面进行反选，即在隐藏A面，显示B面时选中此功能后的效果为显示A面，隐藏B面。 来源：[10_extracted_pages/EM_Project/Tree_Faces.md](../10_extracted_pages/EM_Project/Tree_Faces.md)
- **面节点**：注意该功能只对金属面有效。 来源：[10_extracted_pages/EM_Project/Tree_Faces.md](../10_extracted_pages/EM_Project/Tree_Faces.md)
- **面节点**：但需要注意的是旋转角度需要不小于0.0001。 来源：[10_extracted_pages/EM_Project/Tree_Faces.md](../10_extracted_pages/EM_Project/Tree_Faces.md)
- **面节点**：但需要注意的是要保证至少有一个面和一条线段。 来源：[10_extracted_pages/EM_Project/Tree_Faces.md](../10_extracted_pages/EM_Project/Tree_Faces.md)
- **体节点**：> 图片: `./images/Tree_Solids_6.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Tree_Solids_6.png`
- 默认情况下，对于电导率较高的材料（如铜、银等良导体），不会求解模型内部的场分布， 因为电磁场的能量主要集中在导体表面，这是由于趋肤效应。 来源：[10_extracted_pages/EM_Project/Tree_Solids.md](../10_extracted_pages/EM_Project/Tree_Solids.md)
- **体节点**：因此，对于良导体，默认情况下不求解物体内部，将会把物体设置成阻抗边界体(IBC)进行仿真。 来源：[10_extracted_pages/EM_Project/Tree_Solids.md](../10_extracted_pages/EM_Project/Tree_Solids.md)
- **体节点**：- 对于具有显著电导率损耗的材料或特定厚度的导体,如果导体的厚度与趋肤深度相近或小于趋肤深度时，如果需要精确考虑导体损耗，需要求解物体内部。 来源：[10_extracted_pages/EM_Project/Tree_Solids.md](../10_extracted_pages/EM_Project/Tree_Solids.md)

## 仿真
- **Parameter Sweep**：> 图片: `./images/Parameter_Sweep_16.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Simulation\images\Parameter_Sweep_16.png`
注意，参数化扫描前必须在变量中添加变量，才可以调用已添加的变量，未设置变量的模型无法使用参数化扫描。 来源：[10_extracted_pages/Simulation/Parameter_Sweep.md](../10_extracted_pages/Simulation/Parameter_Sweep.md)
- **仿真**：如果有问题软件在验证后在下方日志报错警告，可以根据提示去检查模型设置问题。 来源：[10_extracted_pages/Simulation/Simulation.md](../10_extracted_pages/Simulation/Simulation.md)
- **仿真**：注意：有些模型可能停止的时间较长，可以在日志右下角查看当前仿真的进度条。 来源：[10_extracted_pages/Simulation/Simulation.md](../10_extracted_pages/Simulation/Simulation.md)

## 后处理
- **新建接收器结果**：注意接收器仿真只能在离散或快速扫频下才可以仿真，仿真完成后可以再新建接收器查看结果，但需要点击工具栏设计设置中选择保存结果。 来源：[10_extracted_pages/Post_Processing/New_Observers.md](../10_extracted_pages/Post_Processing/New_Observers.md)
- **新建端口结果**：> 图片: `./images/New_Port_7.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\images\New_Port_7.png`
有关图表设置如下图所示，可进行X、Y轴名称修改，坐标值标签字体和大小修改，X/Y轴范围修改(注意X轴范围不能超过仿真频率范围)，图例名称、曲线颜色、样式、标识、宽度、是否显示修改。 来源：[10_extracted_pages/Post_Processing/New_Port.md](../10_extracted_pages/Post_Processing/New_Port.md)
- **新建端口结果**：> 图片: `./images/New_Port_8.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\images\New_Port_8.png`
注意改变X轴范围仅改变了显示，导出数据时还是导出全范围X轴数据。 来源：[10_extracted_pages/Post_Processing/New_Port.md](../10_extracted_pages/Post_Processing/New_Port.md)

## 工具
- **设计设置**：若不勾选则默认材料的介电常数和电导率是常数。 来源：[10_extracted_pages/Tool/Design_Setting.md](../10_extracted_pages/Tool/Design_Setting.md)
- **设计设置**：勾选“设置为默认”则将此窗口的设置判定为软件的默认设置。 来源：[10_extracted_pages/Tool/Design_Setting.md](../10_extracted_pages/Tool/Design_Setting.md)
- **详细日志**：- 迭代残差：目标值、当前值(迭代残差用来判断迭代是否收敛。 来源：[10_extracted_pages/Tool/Details_logs.md](../10_extracted_pages/Tool/Details_logs.md)
- **详细日志**：- 收敛数量：目标值、当前值； 来源：[10_extracted_pages/Tool/Details_logs.md](../10_extracted_pages/Tool/Details_logs.md)
- **导出Snp**：注意事项： 不同的应用场景可能需要不同的参考阻抗，例如通信系统中常用50Ω，而有线电视系统则使用75Ω。 来源：[10_extracted_pages/Tool/Export_Snp.md](../10_extracted_pages/Tool/Export_Snp.md)
- **导出Snp**：在进行阻抗匹配时，归一化阻抗可以简化匹配网络的设计和调试过程，但必须注意实际工作条件下的差异。 来源：[10_extracted_pages/Tool/Export_Snp.md](../10_extracted_pages/Tool/Export_Snp.md)
- **变量**：注意：输入变量的名称是不区分大小写的。 来源：[10_extracted_pages/Tool/Variables.md](../10_extracted_pages/Tool/Variables.md)
- **变量**：### 保留变量名称
pi, e, t, t1, t2是软件已经定义的变量名称，不可以再次被定义。 来源：[10_extracted_pages/Tool/Variables.md](../10_extracted_pages/Tool/Variables.md)
- **变量**：请注意添加时命名问题。 来源：[10_extracted_pages/Tool/Variables.md](../10_extracted_pages/Tool/Variables.md)
- **变量**：注意：如果该变量的表达式包含多个变量，软件会涉及的变量分级表示出来。 来源：[10_extracted_pages/Tool/Variables.md](../10_extracted_pages/Tool/Variables.md)
- **矢量拟合**：操作步骤如下：
1）如图，在软件窗口顶部工具栏里边点击矢量拟合：
> 图片: `images/Vector_Fitting1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Tool\images\Vector_Fitting1.png`
2）点击矢量拟合，打开该功能对话框， 如下图：
- 下拉S参数>可以选择参数类型（S参数、Y参数、Z参数，默认为S参数）； 来源：[10_extracted_pages/Tool/Vector_Fitting.md](../10_extracted_pages/Tool/Vector_Fitting.md)
- **矢量拟合**：- 下拉dB >可以选择数据类型（dB、Real、Imag，Phase、Mag,默认为dB）； 来源：[10_extracted_pages/Tool/Vector_Fitting.md](../10_extracted_pages/Tool/Vector_Fitting.md)

## 建模总览
- **背景**：> 图片: `./images/Background_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Bkg_Mat\images\Background_1.png`
### 均匀介质材料
该处可设置计算区域为均匀材料，默认为均匀空气材料，可根据需要修改材料，可新建材料或选择材料库中材料。 来源：[10_extracted_pages/Modeling/Bkg_Mat/Background.md](../10_extracted_pages/Modeling/Bkg_Mat/Background.md)
- **电色散材料**：注意此处的频率支持支以GHz为单位的色散材料频率范围。 来源：[10_extracted_pages/Modeling/Bkg_Mat/Dielectric_Dispersion.md](../10_extracted_pages/Modeling/Bkg_Mat/Dielectric_Dispersion.md)
- **材料**：欧拉角暂不支持修改。 来源：[10_extracted_pages/Modeling/Bkg_Mat/Materials.md](../10_extracted_pages/Modeling/Bkg_Mat/Materials.md)
- **材料**：软件默认使用各向同性的介电常数。 来源：[10_extracted_pages/Modeling/Bkg_Mat/Materials.md](../10_extracted_pages/Modeling/Bkg_Mat/Materials.md)
- **材料**：软件的默认矩阵为{1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1}(WavEDA中分号和逗号具有相同功能)，用户根据实际需要修改矩阵。 来源：[10_extracted_pages/Modeling/Bkg_Mat/Materials.md](../10_extracted_pages/Modeling/Bkg_Mat/Materials.md)
- **材料**：软件默认使用各向同性的电导率。 来源：[10_extracted_pages/Modeling/Bkg_Mat/Materials.md](../10_extracted_pages/Modeling/Bkg_Mat/Materials.md)
- **材料**：注意，设置电损耗角正切和磁损耗角正切时需要将前面的选项框勾选上，软件默认没有设置电损耗角正切和磁损耗角正切。 来源：[10_extracted_pages/Modeling/Bkg_Mat/Materials.md](../10_extracted_pages/Modeling/Bkg_Mat/Materials.md)
- **阿基米德螺旋线**：若未修改，默认显示为赋予材料的颜色。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Archimedean_Spiral.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Archimedean_Spiral.md)
- **阿基米德螺旋线**：注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Archimedean_Spiral.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Archimedean_Spiral.md)
- **键合线**：若未修改，默认显示为赋予材料的颜色。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Bondwire.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Bondwire.md)
- **键合线**：注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Bondwire.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Bondwire.md)
- **键合线**：设为曲线操作不可逆，若设为曲线，阻抗边界勾选框会开启。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Bondwire.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Bondwire.md)
- **长方体**：若未修改，默认显示为赋予材料的颜色。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Box.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Box.md)
- **长方体**：注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Box.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Box.md)
- **圆锥/棱锥**：若未修改，默认显示为赋予材料的颜色。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Cone.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Cone.md)
- **圆锥/棱锥**：注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Cone.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Cone.md)
- **圆柱**：若未修改，默认显示为赋予材料的颜色。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Cylinder.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Cylinder.md)
- **圆柱**：注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Cylinder.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Cylinder.md)
- **棱柱**：若未修改，默认显示为赋予材料的颜色。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Prism.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Prism.md)
- **棱柱**：注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Prism.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Prism.md)
- **棱柱**：画图模式下，WavEDA默认创建正六边形棱柱，创建步骤为先确定底面中点以及多边形外圆半径，最后选取一点确定棱柱的高度，从而完成创建过程。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Prism.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Prism.md)
- **物体相交**：通常不建议这样做，因为这会导致相交的部分物体材料分布不明确。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Solid_Intersection.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Solid_Intersection.md)
- **sphere**：若未修改，默认显示为赋予材料的颜色。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Sphere.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Sphere.md)
- **环形螺旋线圈**：若未修改，默认显示为赋予材料的颜色
### 建模
通过给定主圆环半径，子圆环半径，线圈圈数，圈数，起始角度以及终止角度来定义环形螺旋线圈。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Toroidal_Spiral.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Toroidal_Spiral.md)
- **环形螺旋线圈**：注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Toroidal_Spiral.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Toroidal_Spiral.md)
- **环**：若未修改，默认显示为赋予材料的颜色
### 建模
通过定义外圆中点，外圆半径以及内圆半径来定义环。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Torus.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Torus.md)
- **环**：注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_3D_Geometry/Torus.md](../10_extracted_pages/Modeling/Create_3D_Geometry/Torus.md)
- **弧线**：注意一切均是基于原点(u ,v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_Curve/Circular_Arc.md](../10_extracted_pages/Modeling/Create_Curve/Circular_Arc.md)
- **弧线**：注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_Curve/Circular_Arc.md](../10_extracted_pages/Modeling/Create_Curve/Circular_Arc.md)
- **直线**：注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_Curve/Line.md](../10_extracted_pages/Modeling/Create_Curve/Line.md)
- **3D参数曲线**：注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_Curve/Parametric_Curve.md](../10_extracted_pages/Modeling/Create_Curve/Parametric_Curve.md)
- **折线**：注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_Curve/Polyline.md](../10_extracted_pages/Modeling/Create_Curve/Polyline.md)
- **圆锥面**：若未修改，默认显示为赋予材料的颜色。 来源：[10_extracted_pages/Modeling/Create_Face/Cone_Face.md](../10_extracted_pages/Modeling/Create_Face/Cone_Face.md)
- **圆锥面**：注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_Face/Cone_Face.md](../10_extracted_pages/Modeling/Create_Face/Cone_Face.md)
- **编辑多边形面**：> 图片: `./images/Edit_Polygon_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_Face\images\Edit_Polygon_1.png`
坐标编辑支持一键清空，默认行数为50行，若坐标多于50个，可点击添加坐标加入行。 来源：[10_extracted_pages/Modeling/Create_Face/Edit_Polygon.md](../10_extracted_pages/Modeling/Create_Face/Edit_Polygon.md)
- **椭圆**：若未修改，默认显示为赋予材料的颜色。 来源：[10_extracted_pages/Modeling/Create_Face/Ellipse.md](../10_extracted_pages/Modeling/Create_Face/Ellipse.md)
- **椭圆**：注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_Face/Ellipse.md](../10_extracted_pages/Modeling/Create_Face/Ellipse.md)
- **椭圆**：画图模式下，WavEDA默认创建圆形面，创建步骤为先确定中心点，再确定半径即可创建此圆面。 来源：[10_extracted_pages/Modeling/Create_Face/Ellipse.md](../10_extracted_pages/Modeling/Create_Face/Ellipse.md)
- **参数面**：若未修改，默认显示为赋予材料的颜色。 来源：[10_extracted_pages/Modeling/Create_Face/Parametric_Face.md](../10_extracted_pages/Modeling/Create_Face/Parametric_Face.md)
- **参数面**：注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_Face/Parametric_Face.md](../10_extracted_pages/Modeling/Create_Face/Parametric_Face.md)
- **多边形面**：若未修改，默认显示为赋予材料的颜色。 来源：[10_extracted_pages/Modeling/Create_Face/Polygon.md](../10_extracted_pages/Modeling/Create_Face/Polygon.md)
- **多边形面**：注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_Face/Polygon.md](../10_extracted_pages/Modeling/Create_Face/Polygon.md)
- **矩形**：若未修改，默认显示为赋予材料的颜色。 来源：[10_extracted_pages/Modeling/Create_Face/Rectangle.md](../10_extracted_pages/Modeling/Create_Face/Rectangle.md)
- **矩形**：注意一切均是基于原点(u,v,w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_Face/Rectangle.md](../10_extracted_pages/Modeling/Create_Face/Rectangle.md)
- **矩形**：注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_Face/Rectangle.md](../10_extracted_pages/Modeling/Create_Face/Rectangle.md)
- **半椭球面**：若未修改，默认显示为赋予材料的颜色。 来源：[10_extracted_pages/Modeling/Create_Face/Semiellipsoid_Face.md](../10_extracted_pages/Modeling/Create_Face/Semiellipsoid_Face.md)
- **半椭球面**：注意一切均是基于原点(u, v, w)以及UVW轴所决定的坐标系下来定义的，默认为全局坐标系。 来源：[10_extracted_pages/Modeling/Create_Face/Semiellipsoid_Face.md](../10_extracted_pages/Modeling/Create_Face/Semiellipsoid_Face.md)
- **计算区域**：目前只有长方体盒子为计算区域可以修改边界的间距，且默认此长方体内填充材料为Air。 来源：[10_extracted_pages/Modeling/Design/Domain.md](../10_extracted_pages/Modeling/Design/Domain.md)
- **计算区域**：> 图片: `./images/Domain_8.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_8.png`
- 自动间距，软件提供自动计算波长功能，默认为中心频率计算出来的四分之一波长。 来源：[10_extracted_pages/Modeling/Design/Domain.md](../10_extracted_pages/Modeling/Design/Domain.md)
- **计算区域**：> 图片: `./images/Domain_10.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_10.png`
- 自定义间距，根据用户给定的间距数据，默认勾选“应用至所有方向”，只需要设置一次，该间距会应用到所有方向。 来源：[10_extracted_pages/Modeling/Design/Domain.md](../10_extracted_pages/Modeling/Design/Domain.md)
- **计算区域**：> 图片: `./images/Domain_12.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_12.png`
- 自定义校正边界盒子，可以理解为参数化建模计算区域盒子，同样需要用户手动输入空气盒子在X/Y/Z方向上的数据，输入参数时需要注意负方向的数值要小于正方向的数值。 来源：[10_extracted_pages/Modeling/Design/Domain.md](../10_extracted_pages/Modeling/Design/Domain.md)
- **计算区域**：建议根据无间距状态下的模型在X/Y/Z方向的尺寸进行增加间距设置。 来源：[10_extracted_pages/Modeling/Design/Domain.md](../10_extracted_pages/Modeling/Design/Domain.md)
- **频率**：注意：输入步长必须在扫频范围内。 来源：[10_extracted_pages/Modeling/Design/Frequency.md](../10_extracted_pages/Modeling/Design/Frequency.md)
- **频率**：注意：对于一般模型而言，扫频的点数不需要设置太多，最多设置为301即可。 来源：[10_extracted_pages/Modeling/Design/Frequency.md](../10_extracted_pages/Modeling/Design/Frequency.md)
- **频率**：> 图片: `./images/Frequency_11.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Frequency_11.png`
- 多频点：设置多个频点扫频，多个频点输入必须为英文逗号字符","分隔，只有离散扫频方法支持多频点扫频。 来源：[10_extracted_pages/Modeling/Design/Frequency.md](../10_extracted_pages/Modeling/Design/Frequency.md)
- **频率**：其中，软件最大插值点数为250，默认插值误差为1%，当插值误差减少到1%时插值扫频结束，结果收敛，若达到最大插值点后误差大干1%、则插值扫频结束，结果不收敛。 来源：[10_extracted_pages/Modeling/Design/Frequency.md](../10_extracted_pages/Modeling/Design/Frequency.md)
- **频率**：建议插值误差不要小于0.5%。 来源：[10_extracted_pages/Modeling/Design/Frequency.md](../10_extracted_pages/Modeling/Design/Frequency.md)
- **频率**：插值方法的频点由算法决定的，收敛后会根据插值结果计算用户设置频点的S参数。 来源：[10_extracted_pages/Modeling/Design/Frequency.md](../10_extracted_pages/Modeling/Design/Frequency.md)
- **频率**：需要注意的是，应用插值扫频时，用户无法查看选定频点的Snapshot； 来源：[10_extracted_pages/Modeling/Design/Frequency.md](../10_extracted_pages/Modeling/Design/Frequency.md)
- **频率**：若设置远场频点，WaVEDA会强行将该频点插入计算列表，但查看效率频率曲线等结果时，也无法保证频点个数。 来源：[10_extracted_pages/Modeling/Design/Frequency.md](../10_extracted_pages/Modeling/Design/Frequency.md)

## 文件与主页
- **文件**：#### 重置
点击重置，弹出警告窗口后，模块功能会提醒你“重置该工程可能会清除所有数据，是否继续？ 来源：[10_extracted_pages/File/File.md](../10_extracted_pages/File/File.md)
- **主页**：#### 另存为
点击保存，弹出文件夹后，你可以选择任意的位置另保存WavEDA文件，注意修改文件名称。 来源：[10_extracted_pages/File/Homepage.md](../10_extracted_pages/File/Homepage.md)
- **选项**：软件内默认为24核，具体的核数可通过电脑自身的硬件进行配置。 来源：[10_extracted_pages/File/Options.md](../10_extracted_pages/File/Options.md)

## 网格
- **3D网格**：- 频率 (GHz)：初始网格剖分的频率，建议采用中心频率，若对精度要求较高可设置更高的频率； 来源：[10_extracted_pages/Mesh/3D_Mesh.md](../10_extracted_pages/Mesh/3D_Mesh.md)
- **3D网格**：- 采样率 (PPW，Points Per Wavelength)：为基于上述设置频率下空气中波长(波长=光速/频率)内至少剖分的网格数量，WavEDA默认的采样率为3 PPW。 来源：[10_extracted_pages/Mesh/3D_Mesh.md](../10_extracted_pages/Mesh/3D_Mesh.md)
- **3D网格**：对于电大问题，即模型尺寸远大于波长，建议将采样率设置为10 PPW或者更大。 来源：[10_extracted_pages/Mesh/3D_Mesh.md](../10_extracted_pages/Mesh/3D_Mesh.md)
- **3D网格**：- 网格增长率：从小尺寸网格过度到大尺寸网格的比率，WavEDA的网格增长率范围是1.2-3，默认值为2。 来源：[10_extracted_pages/Mesh/3D_Mesh.md](../10_extracted_pages/Mesh/3D_Mesh.md)
- **3D网格**：网格增长率设置的较小会导致网格过密，设置的较大会导致仿真结果不准确，建议适中较好。 来源：[10_extracted_pages/Mesh/3D_Mesh.md](../10_extracted_pages/Mesh/3D_Mesh.md)
- **3D网格**：下图设置表示频率为2 GHz时对应波长为150 mm，在一个波长（空气中）中至少剖分3个网格，即初始网格剖分的尺寸必须小于50 mm。 来源：[10_extracted_pages/Mesh/3D_Mesh.md](../10_extracted_pages/Mesh/3D_Mesh.md)
- **3D网格**：可在此界面顶部输入需要加密的体或面的起始和终止编号或者不连续多选，根据物体尺寸设置其网格最大尺寸，可以控制此物体上至少剖分的网格数量，需要注意的是局部网格尺寸不可设置过小，会导致网格数量剧增。 来源：[10_extracted_pages/Mesh/3D_Mesh.md](../10_extracted_pages/Mesh/3D_Mesh.md)
- **3D网格**：通过显示网格中的病态网格选项，可以检查网格剖分的质量，并对病态网格分布较多的区域进行局部加密或调整局部加密参数设置。 来源：[10_extracted_pages/Mesh/3D_Mesh.md](../10_extracted_pages/Mesh/3D_Mesh.md)
- **3D网格**：进入3D网格的“常规”界面，其他设置建议使用默认选项，下面将详细解释从边界扩展网格尺寸和使用扩展控制功能的作用，这两个功能仅对手动设置网格剖分生效，对于自适应网格剖分不起作用。 来源：[10_extracted_pages/Mesh/3D_Mesh.md](../10_extracted_pages/Mesh/3D_Mesh.md)
- **自适应网格**：#### 自适应网格设置：
- 频率：自适应网格剖分迭代的频点，频率越高网格剖分越密，建议大于或等于中心频点； 来源：[10_extracted_pages/Mesh/Adaptive_Mesh.md](../10_extracted_pages/Mesh/Adaptive_Mesh.md)
- **自适应网格**：当连续自适应迭代网格计算的S参数的误差小于预设的残差值或者达到最大迭代次数，自适应网格剖分则停止。 来源：[10_extracted_pages/Mesh/Adaptive_Mesh.md](../10_extracted_pages/Mesh/Adaptive_Mesh.md)
- **自适应网格**：在初始网格的基础上对电磁场强度变化大的地方不断细化，对电磁场变化较小的地方粗化网格，直至满足收敛标准，并生成合适的最终网格。 来源：[10_extracted_pages/Mesh/Adaptive_Mesh.md](../10_extracted_pages/Mesh/Adaptive_Mesh.md)
- **显示网格**：- 病态：选中“病态”选项，用于检查测试模型网格剖分质量，查看网格剖分质量较差的区域，此部分网格倾斜度接近1，便于定位网格剖分质量较差的体/面，并在3D网格对其进行局部加密或在自适应网格界面调整自适应网格参数设置，以消除关键结构处病态网格，得到准确仿真结果。 来源：[10_extracted_pages/Mesh/Show_Mesh.md](../10_extracted_pages/Mesh/Show_Mesh.md)
