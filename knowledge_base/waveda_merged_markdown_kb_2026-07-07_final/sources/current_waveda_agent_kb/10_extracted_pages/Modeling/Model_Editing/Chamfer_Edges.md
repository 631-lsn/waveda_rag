---
title: "倒斜角"
merged_source: "current_waveda_agent_kb"
source_relative_path: "10_extracted_pages/Modeling/Model_Editing/Chamfer_Edges.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\10_extracted_pages\Modeling\Model_Editing\Chamfer_Edges.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 倒斜角

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\Chamfer_Edges.html`
- 原始相对路径: `Modeling/Model_Editing/Chamfer_Edges.html`
- 知识模块: `建模总览`

## 正文抽取
## 倒斜角

该功能常用于处理几何体的边缘，创建斜切或倒角的过渡，从而使模型的边缘更加平滑，避免尖锐的边缘或角落。 通常在制造、组装、或电磁仿真中使用。倒角常用于消除锐角，提高结构的机械强度或减少电磁波的反射。 这在建模过程中，特别是处理金属零件、微波组件、天线设计和电磁仿真时非常有用。

#### 激活倒斜角功能

切换到选线模式，选择要应用倒斜角的棱边。可以选择单个棱边，或者多个棱边进行倒角，选中主菜单栏“建模”->“形状”下的倒斜角

> 图片: `./images/Chamfer_Edges_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Chamfer_Edges_1.png`

图标。

> 图片: `./images/Chamfer_Edges_5.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Chamfer_Edges_5.png`

> 图片: `./images/Chamfer_Edges_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Chamfer_Edges_3.png`

#### 设置参数

> 图片: `./images/Chamfer_Edges_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Chamfer_Edges_2.png`

输入倒角的两个主要参数：倒角距离和角度。

##### 倒角距离

这是倒角切除斜边的直线距离。软件默认15，可以根据需要设置其他距离。

注意：倒角距离是否适合几何，避免自相交或拓扑错误。

##### 角度

这是倒角的倾斜角度，软件默认45°，可以根据需要设置其他角度。点击“完成”后可以看到棱边变成了斜角边。

> 图片: `./images/Chamfer_Edges_6.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Chamfer_Edges_6.png`

> 图片: `./images/Chamfer_Edges_4.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Chamfer_Edges_4.png`

##### 反转

反转可以将倒角的方向反向，例如设置15°，设置的模型倒角的方向向下，点击“反转”，倒角的方向向上。

> 图片: `./images/Chamfer_Edges_7.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Chamfer_Edges_7.png`

> 图片: `./images/Chamfer_Edges_8.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Chamfer_Edges_8.png`

#### 相关文档

面平移调整， 倒圆角， 从现有面拉伸成体。

## 图片资源

1. `./images/Chamfer_Edges_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Chamfer_Edges_1.png`
2. `./images/Chamfer_Edges_5.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Chamfer_Edges_5.png`
3. `./images/Chamfer_Edges_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Chamfer_Edges_3.png`
4. `./images/Chamfer_Edges_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Chamfer_Edges_2.png`
5. `./images/Chamfer_Edges_6.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Chamfer_Edges_6.png`
6. `./images/Chamfer_Edges_4.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Chamfer_Edges_4.png`
7. `./images/Chamfer_Edges_7.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Chamfer_Edges_7.png`
8. `./images/Chamfer_Edges_8.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Chamfer_Edges_8.png`

## 页内/相关链接

- 面平移调整: `../Model_Editing/Move_Face_To_Modify_Solid.html`
- 面平移调整， 倒圆角: `../Model_Editing/Blend_Edges.html`
- 面平移调整， 倒圆角， 从现有面拉伸成体: `../Model_Editing/Extrusion.html`
