---
title: "3D网格"
merged_source: "current_waveda_agent_kb"
source_relative_path: "10_extracted_pages/Mesh/3D_Mesh.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\10_extracted_pages\Mesh\3D_Mesh.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 3D网格

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Mesh\3D_Mesh.html`
- 原始相对路径: `Mesh/3D_Mesh.html`
- 知识模块: `网格`

## 正文抽取
## 3D网格

在WavEDA中待求解的几何模型会被剖分成许多大小不同的四面体，然后使用混合有限元算法（Mixed Finite Element Method, MFEM）计算这些四面体单元之间的关系，从而精确高效地生成电磁仿真结果。

网格是将几何模型离散成小的四面体和三角形单元，如下图展示了WavEDA剖分的四面体形状。四面体是可以被任意拉伸的，因此各种形状的三维模型都可以被离散为若干个四面体单元。

> 图片: `./images/3D_Mesh_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_1.png`

#### WavEDA网格剖分流程：

- 根据用户设置的3D网格参数和局部网格加密参数生成一个初始网格；

- 使用生成的网格计算结构中的电磁场；

- 根据初始网格求出的解，WavEDA会生成误差估算，并在误差较高的区域对网格进行更细致的剖分，然后使用细化后的网格生成另一个电磁场的解；

- WavEDA执行求解、误差分析和自适应细化的迭代过程，直到满足用户设定的残差值或完成最大自适应迭代次数。

> 图片: `./images/3D_Mesh_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_2.png`

#### 初始网格设置：

在3D网格“常规”页面可以设置初始网格。

- 频率 (GHz)：初始网格剖分的频率，建议采用中心频率，若对精度要求较高可设置更高的频率；

- 采样率 (PPW，Points Per Wavelength)：为基于上述设置频率下空气中波长(波长=光速/频率)内至少剖分的网格数量，WavEDA默认的采样率为3 PPW。对于电大问题，即模型尺寸远大于波长，建议将采样率设置为10 PPW或者更大。但太高的采样率会导致网格剖分较多，仿真效率降低，因此采样率不宜设置过高；

- 网格增长率：从小尺寸网格过度到大尺寸网格的比率，WavEDA的网格增长率范围是1.2-3，默认值为2。网格增长率设置的较小会导致网格过密，设置的较大会导致仿真结果不准确，建议适中较好。

下图设置表示频率为2 GHz时对应波长为150 mm，在一个波长（空气中）中至少剖分3个网格，即初始网格剖分的尺寸必须小于50 mm。

> 图片: `./images/3D_Mesh_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_3.png`

#### 局部网格加密

对于复杂的几何形状或需要高精度的场合，比如与端口接触的结构或其他关键结构，用户可以手动调整网格参数。在3D网格“体”界面中“编辑”进入局部网格尺寸设置界面。可在此界面顶部输入需要加密的体或面的起始和终止编号或者不连续多选，根据物体尺寸设置其网格最大尺寸，可以控制此物体上至少剖分的网格数量，需要注意的是局部网格尺寸不可设置过小，会导致网格数量剧增。点击设置即成功设置对所选体或面的布局加密。

若需要取消局部加密，直接点击重置则取消所有局部加密设置；多选物体后点击重置，则取消此部分物体局部加密设置。

> 图片: `./images/3D_Mesh_4.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_4.png`

WavEDA也支持在工程树和模型显示界面选中物体后右击-->属性-->修改网格尺寸，在弹出的局部网格尺寸定义窗口中输入局部加密参数。

> 图片: `./images/3D_Mesh_5.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_5.png`

> 图片: `./images/3D_Mesh_6.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_6.png`

> 图片: `./images/3D_Mesh_7.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_7.png`

初始网格和局部加密网格剖分设置完成后，可以在3D网格中点击“剖分网格”。通过显示网格中的病态网格选项，可以检查网格剖分的质量，并对病态网格分布较多的区域进行局部加密或调整局部加密参数设置。点击“保存并退出”将保存当前的网格剖分设置并退出3D网格界面；点击“取消”则会放弃当前的设置并退出。

初始网格设置和局部网格加密完成后，可以进入自适应网格进行自适应网格剖分设置。

进入3D网格的“常规”界面，其他设置建议使用默认选项，下面将详细解释从边界扩展网格尺寸和使用扩展控制功能的作用，这两个功能仅对手动设置网格剖分生效，对于自适应网格剖分不起作用。

> 图片: `./images/3D_Mesh_8.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_8.png`

> 图片: `./images/3D_Mesh_9.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_9.png`

> 图片: `./images/3D_Mesh_10.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_10.png`

> 图片: `./images/3D_Mesh_11.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_11.png`

## 图片资源

1. `./images/3D_Mesh_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_1.png`
2. `./images/3D_Mesh_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_2.png`
3. `./images/3D_Mesh_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_3.png`
4. `./images/3D_Mesh_4.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_4.png`
5. `./images/3D_Mesh_5.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_5.png`
6. `./images/3D_Mesh_6.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_6.png`
7. `./images/3D_Mesh_7.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_7.png`
8. `./images/3D_Mesh_8.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_8.png`
9. `./images/3D_Mesh_9.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_9.png`
10. `./images/3D_Mesh_10.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_10.png`
11. `./images/3D_Mesh_11.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\3D_Mesh_11.png`

## 页内/相关链接

- 初始网格和局部加密网格剖分设置完成后，可以在3D网格中点击“剖分网格”。通过显示网格: `./Show_Mesh.html`
- 初始网格设置和局部网格加密完成后，可以进入自适应网格: `./Adaptive_Mesh.html`
