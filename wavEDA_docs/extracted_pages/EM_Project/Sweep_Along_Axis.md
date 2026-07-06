# 沿轴扫描

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Sweep_Along_Axis.html`
- 原始相对路径: `EM_Project/Sweep_Along_Axis.html`
- 知识模块: `EM设计与结果`

## 正文抽取
## 沿轴扫描

沿轴扫描是用线段生成面的快捷方法。同样，部分面也可以通过该方式生成体。

> 图片: `./images/Sweep_Along_Axis_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Sweep_Along_Axis_1.png`

### 名称

沿轴扫描得到的几何，名称自动生成，完成后可手动修改面的名称

### 扫描参数

该节点目录下的的设置将决定得到的几何面大小。

#### 扫描参数

- 旋转轴上一点

沿轴扫描，得到的几何圆心是旋转轴上一点。

- 旋转轴方向

旋转轴方向输入一个三维矢量，该线段将以输入矢量方向为旋转中心得到几何， 例如输入（0,0,1）,则该线段将绕Z轴旋转得到几何。

> 图片: `./images/Sweep_Along_Axis_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Sweep_Along_Axis_2.png`

- 旋转角度

输入一个旋转角度后，得到的几何将按照固定角度旋转。注意这个值需要大于等于0.0001。

### 其他

勾选删除原物体后，则沿轴扫描功能只生成得到的面。不勾选该功能，软件将保留原有的新线段，并生成新的面。

## 图片资源

1. `./images/Sweep_Along_Axis_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Sweep_Along_Axis_1.png`
2. `./images/Sweep_Along_Axis_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Sweep_Along_Axis_2.png`
