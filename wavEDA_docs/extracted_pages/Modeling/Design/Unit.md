# 单位

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\Unit.html`
- 原始相对路径: `Modeling/Design/Unit.html`
- 知识模块: `建模总览`

## 正文抽取
## 单位

- 长度 - 时间 - 频率 - 长度/频率单位变化选项

> 图片: `./images/Unit_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Unit_2.png`

在建模仿真之前，需要设置模型所需的几何和物理单位。在单位修改界面可以修改长度单位，时间单位以及频率单位。

注意：整个工程文件的单位都在此设置，此处设置的单位为全局单位，其他界面编辑时不能带额外单位。

你可以通过点击上方主菜单栏中"设计"->"unit"图标打开对话框

> 图片: `./images/Unit_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Unit_1.png`

，也可以通过双击左侧工程树"设计"->"单位"打开对话框。

#### 长度

可以设置模型的长度单位，默认为 mm。

#### 时间

可以设置仿真的时间单位，默认为 ns。

#### 频率

可以设置仿真频率单位，默认为 GHz。

#### 长度/频率单位变化选项

默认勾选该选项，切换单位后模型大小不会随着系统单位缩放。例如：选择厘米（cm）作为新的长度单位，结果是10毫米（mm）的尺寸变为1厘米（cm）。

如果取消勾选，切换单位后模型大小会随着系统单位缩放。例如：选择厘米（cm）作为新的长度单位，结果是10毫米（mm）的尺寸变为10厘米（cm）。

## 图片资源

1. `./images/Unit_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Unit_2.png`
2. `./images/Unit_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Unit_1.png`

## 页内/相关链接

- - 长度: `#length`
- - 长度 - 时间: `#Time`
- - 长度 - 时间 - 频率: `#Frequency`
- - 长度 - 时间 - 频率 - 长度/频率单位变化选项: `#长度/频率单位变化选项`
