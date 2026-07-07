---
title: "远场"
merged_source: "current_waveda_agent_kb"
source_relative_path: "10_extracted_pages/EM_Project/Far_field.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\10_extracted_pages\EM_Project\Far_field.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 远场

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Far_field.html`
- 原始相对路径: `EM_Project/Far_field.html`
- 知识模块: `EM设计与结果`

## 正文抽取
## 远场

- 远场 - 添加远场频点 - 编辑端口激励 - 删除所有结果 - 禁用远场仿真 - 添加轴比、增益频率曲线对应的监视频点与角度 - 远场仿真后结果查看

这里主要用于仿真前添加远场场监视设置，以便仿真后能查看远场分布，仿真前一般只需要设置添加远场监视频点；仿真后可以根据需要编辑端口激励（也可以仿真前设置），主要分为以下步骤：

- 添加监视频点；

- 编辑端口激励；

- 删除所有结果；

- 禁用远场仿真；

- 添加轴比、增益频率曲线对应的监视频点与角度；

- 结果查看。

### 远场

> 图片: `images/far_field1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field1.png`

如上图，在工程树左下方可以找到远场标识，对其右键可以进行相关设置。

### 添加远场频点

> 图片: `images/far_field2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field2.png`

如图，在工程树上选中远场，右键，然后点击添加远场频点，进入如下对话框：

> 图片: `images/far_field3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field3.png`

在此对话框中可以根据需要添加对应的远场监视频点，先选择扫频方法，包括单频点，步长和频点数；

- 单频点表示只监视一个频点；

- 间隔取频点需要设定起始频点、结束频点，以及步长，比如添加2.4-3 GHz，步长为0.2 GHz；

- 另外平均取频点需要设定起始频点、结束频点，以及点数；

如上图，待输入需要的监视频点后，点击添加，此时远场监视频点就出现在对话框的右边方框内，之后点击下方完成，同时自动关闭该对话框。

### 编辑端口激励

> 图片: `images/far_field4.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field4.png`

如图，点击编辑端口激励，进入如下对话框，在此可以设置需要的端口激励组合，其中幅度默认为1 W，幅度填0表示不进行激励；相位默认为0度，也可以设置其他角度，添加好激励组合后，可以点击完成，同时关闭该对话框。

> 图片: `images/far_field5.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field5.png`

说明：上述该激励端口对话框的设置，可以在仿真运行前设置，也可以在仿真运行后设置（常用一般在仿真设置即可，并且运行后每次更改设置后，都可以立刻查看对应的远场结果，而不需要重新点击仿真运行）。

### 删除所有结果

> 图片: `images/far_field6.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field6.png`

如图，点击删除所有结果，则将刚才添加的远场监视频点删除。

### 禁用远场仿真

> 图片: `images/far_field7.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field7.png`

如图，点击禁用远场仿真后，表示该功能关闭，相应的远场标识也变暗。

> 图片: `images/far_field8.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field8.png`

### 添加轴比、增益频率曲线对应的监视频点与角度

> 图片: `images/far_field18.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field18.png`

如图，点击增加轴比，进入如下对话框：

> 图片: `images/far_field17.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field17.png`

由于前面已经添加了远场监视频点，在该对话框中需要进一步添加轴比频率曲线需要查看的频点与对应的角度，如图，选择了4个频点，角度选取phi=30度,theta=0度, 然后点击添加，最后点击完成，如上图：

另外添加增益频率曲线方法与上述添加轴比曲线相同。

### 结果查看

> 图片: `images/far_field9.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field9.png`

如上图，经过前面提到仿真前添加远场监视频点后，仿真后可以在工程树左下角，找到电磁结果的远场部分，点击远场可以查看对应的远场结果； 直接双击远场结果各个频点，可以生成远场3D方向图，如下图，另外关于远场结果查看该部分的详细说明可以查看 电磁结果查看(远场部分）文档。

> 图片: `images/far_field10.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field10.png`

## 图片资源

1. `images/far_field1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field1.png`
2. `images/far_field2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field2.png`
3. `images/far_field3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field3.png`
4. `images/far_field4.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field4.png`
5. `images/far_field5.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field5.png`
6. `images/far_field6.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field6.png`
7. `images/far_field7.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field7.png`
8. `images/far_field8.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field8.png`
9. `images/far_field18.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field18.png`
10. `images/far_field17.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field17.png`
11. `images/far_field9.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field9.png`
12. `images/far_field10.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\far_field10.png`

## 页内/相关链接

- - 远场: `#length`
- - 远场 - 添加远场频点: `#F`
- - 远场 - 添加远场频点 - 编辑端口激励: `#a`
- - 远场 - 添加远场频点 - 编辑端口激励 - 删除所有结果: `#b`
- - 远场 - 添加远场频点 - 编辑端口激励 - 删除所有结果 - 禁用远场仿真: `#c`
- - 远场 - 添加远场频点 - 编辑端口激励 - 删除所有结果 - 禁用远场仿真 - 添加轴比、增益频率曲线对应的监视频点与角度: `#m`
- - 远场 - 添加远场频点 - 编辑端口激励 - 删除所有结果 - 禁用远场仿真 - 添加轴比、增益频率曲线对应的监视频点与角度 - 远场仿真后结果查看: `#d`
- 如上图，经过前面提到仿真前添加远场监视频点后，仿真后可以在工程树左下角，找到电磁结果的远场部分，点击远场可以查看对应的远场结果； 直接双击远场结果各个频点，可以生成远场3D方向图，如下图，另外关于远场结果查看该部分的详细说明可以查看 电磁结果查看(远场部分）: `./EM_Results.html`
