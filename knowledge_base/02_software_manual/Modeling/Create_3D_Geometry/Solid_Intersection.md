---
title: "物体相交"
merged_source: "current_waveda_agent_kb"
source_relative_path: "10_extracted_pages/Modeling/Create_3D_Geometry/Solid_Intersection.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\10_extracted_pages\Modeling\Create_3D_Geometry\Solid_Intersection.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 物体相交

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\Solid_Intersection.html`
- 原始相对路径: `Modeling/Create_3D_Geometry/Solid_Intersection.html`
- 知识模块: `建模总览`

## 正文抽取
## 物体相交

创建模型时，在创建与一个(或多个)现有形状(A)相交的新形状(B)后，会自动打开物体相交对话框。可以决定如何处理相交的物体。

### 新物体

两个物体相交时，旧的物体(形状A)会减去与新的物体(形状B)。详见布尔运算相减操作。

> 图片: `./images/Solid_Intersection_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Solid_Intersection_1.png`

### 已经存在的物体

两个物体相交时，新的物体(形状B)会减去与旧的物体(形状A)。详见布尔运算相减操作。

> 图片: `./images/Solid_Intersection_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Solid_Intersection_2.png`

### 空

物体保留原有的形状。通常不建议这样做，因为这会导致相交的部分物体材料分布不明确。

> 图片: `./images/Solid_Intersection_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Solid_Intersection_3.png`

### 将新物体用于之后的冲突情况

如果当前新物体（形状D）会与多个物体（形状A\形状B\形状C）相交，保留新物体（形状A）的形状，让旧物体（形状B\形状C\形状D）减去与新物体（形状A）相交的部分。

> 图片: `./images/Solid_Intersection_4.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Solid_Intersection_4.png`

### 将现有物体用于之后的冲突情况

如果当前新物体（形状D）会与多个物体（形状A\形状B\形状C）相交，保留旧物体（形状B\形状C\形状D）的形状，让新物体（形状A）减去与旧物体（形状B\形状C\形状D）相交的部分。

> 图片: `./images/Solid_Intersection_5.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Solid_Intersection_5.png`

### 不选择任何物体用于之后的冲突情况

和“空”一致，应用于新物体（形状D）多个物体（形状A\形状B\形状C）相交的情况，物体保留原有的形状。通常不建议这样做，因为这会导致相交的部分物体材料分布不明确。

> 图片: `./images/Solid_Intersection_6.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Solid_Intersection_6.png`

## 图片资源

1. `./images/Solid_Intersection_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Solid_Intersection_1.png`
2. `./images/Solid_Intersection_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Solid_Intersection_2.png`
3. `./images/Solid_Intersection_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Solid_Intersection_3.png`
4. `./images/Solid_Intersection_4.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Solid_Intersection_4.png`
5. `./images/Solid_Intersection_5.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Solid_Intersection_5.png`
6. `./images/Solid_Intersection_6.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Create_3D_Geometry\images\Solid_Intersection_6.png`

## 页内/相关链接

- 两个物体相交时，旧的物体(形状A)会减去与新的物体(形状B)。详见布尔运算: `../Model_Editing/Boolean.html`
- 两个物体相交时，新的物体(形状B)会减去与旧的物体(形状A)。详见布尔运算: `../Model_Editing/Boolean.html`
