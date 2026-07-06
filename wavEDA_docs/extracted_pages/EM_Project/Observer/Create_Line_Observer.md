# 创建线接收器

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Observer\Create_Line_Observer.html`
- 原始相对路径: `EM_Project/Observer/Create_Line_Observer.html`
- 知识模块: `EM设计与结果`

## 正文抽取
## 创建线接收器

- 直线 - 椭圆曲线 - 参数化曲线

右键点击工程树上的接收器，可创建线接收器，点击之后进入创建线接收器界面。

> 图片: `./images/Create_Line_Observer_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Observer\images\Create_Line_Observer_1.png`

### 直线

点击选项框中直线曲线类型，在曲线类型选项框右边可以填写点1和点2坐标或在建模窗口选择起始点1和终止点2创建线接收器，并通过设置数据点数设置直线由多少个数据点绘制而成，默认为100个数据点。

> 图片: `./images/Create_Line_Observer_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Observer\images\Create_Line_Observer_2.png`

### 椭圆曲线

点击选项框中椭圆曲线类型，在曲线类型选项框右边可以填写椭圆曲线原点坐标、Ru和Rv半径、法向位置、旋转角度从而创建线接收器，并通过设置数据点数设置椭圆曲线由多少个数据点绘制而成，默认为100个数据点。

> 图片: `./images/Create_Line_Observer_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Observer\images\Create_Line_Observer_3.png`

确定好原点坐标和长短轴大小后，可修改沿轴位置改变曲线沿着那个轴进行绘制，同时旋转角度决定所画椭圆曲线的路径大小。

> 图片: `./images/Create_Line_Observer_4.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Observer\images\Create_Line_Observer_4.png`

- 设置法向(1, 0, 0)时，椭圆曲线沿着X轴进行绘制，设置-180°-0°即可画出半圈曲线。

> 图片: `./images/Create_Line_Observer_5.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Observer\images\Create_Line_Observer_5.png`

- 设置法向(0, 1, 0)时，椭圆曲线沿着Y轴进行绘制，设置-180°-90°即可画出四分之三曲线。

> 图片: `./images/Create_Line_Observer_6.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Observer\images\Create_Line_Observer_6.png`

- 设置法向(0, 0, 1)时，椭圆曲线沿着Z轴进行绘制，设置-180°-180°即可画出全范围曲线。

### 参数化曲线

点击选项框中参数曲线类型，给定参数t0和t1指定取值范围。给参数线上点的坐标指定一个关于t的有效函数，并通过设置数据点数设置直线由多少个数据点绘制而成，默认为100个数据点。注意一切均是基于原点(u, v, w)以及UV轴所决定的坐标系下来定义的，默认为全局坐标系。

> 图片: `./images/Create_Line_Observer_7.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Observer\images\Create_Line_Observer_7.png`

## 图片资源

1. `./images/Create_Line_Observer_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Observer\images\Create_Line_Observer_1.png`
2. `./images/Create_Line_Observer_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Observer\images\Create_Line_Observer_2.png`
3. `./images/Create_Line_Observer_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Observer\images\Create_Line_Observer_3.png`
4. `./images/Create_Line_Observer_4.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Observer\images\Create_Line_Observer_4.png`
5. `./images/Create_Line_Observer_5.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Observer\images\Create_Line_Observer_5.png`
6. `./images/Create_Line_Observer_6.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Observer\images\Create_Line_Observer_6.png`
7. `./images/Create_Line_Observer_7.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Observer\images\Create_Line_Observer_7.png`

## 页内/相关链接

- - 直线: `#直线`
- - 直线 - 椭圆曲线: `#椭圆曲线`
- - 直线 - 椭圆曲线 - 参数化曲线: `#参数化曲线`
