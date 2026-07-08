---
title: "物体相交"
merged_source: "current_waveda_agent_kb"
source_relative_path: "Modeling/Create_3D_Geometry/Solid_Intersection.html"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 物体相交

- 原始相对路径: `Modeling/Create_3D_Geometry/Solid_Intersection.html`
- 知识模块: `建模总览`

## 正文抽取
## 物体相交

创建模型时，在创建与一个(或多个)现有形状(A)相交的新形状(B)后，会自动打开物体相交对话框。可以决定如何处理相交的物体。

### 新物体

两个物体相交时，旧的物体(形状A)会减去与新的物体(形状B)。详见布尔运算相减操作。

> 图示要点：`Solid_Intersection_1.png` 展示“新物体”相关的操作界面或示例，后续审查通过后再补图。

### 已经存在的物体

两个物体相交时，新的物体(形状B)会减去与旧的物体(形状A)。详见布尔运算相减操作。

> 图示要点：`Solid_Intersection_2.png` 展示“已经存在的物体”相关的操作界面或示例，后续审查通过后再补图。

### 空

物体保留原有的形状。通常不建议这样做，因为这会导致相交的部分物体材料分布不明确。

> 图示要点：`Solid_Intersection_3.png` 展示“空”相关的操作界面或示例，后续审查通过后再补图。

### 将新物体用于之后的冲突情况

如果当前新物体（形状D）会与多个物体（形状A\形状B\形状C）相交，保留新物体（形状A）的形状，让旧物体（形状B\形状C\形状D）减去与新物体（形状A）相交的部分。

> 图示要点：`Solid_Intersection_4.png` 展示“将新物体用于之后的冲突情况”相关的操作界面或示例，后续审查通过后再补图。

### 将现有物体用于之后的冲突情况

如果当前新物体（形状D）会与多个物体（形状A\形状B\形状C）相交，保留旧物体（形状B\形状C\形状D）的形状，让新物体（形状A）减去与旧物体（形状B\形状C\形状D）相交的部分。

> 图示要点：`Solid_Intersection_5.png` 展示“将现有物体用于之后的冲突情况”相关的操作界面或示例，后续审查通过后再补图。

### 不选择任何物体用于之后的冲突情况

和“空”一致，应用于新物体（形状D）多个物体（形状A\形状B\形状C）相交的情况，物体保留原有的形状。通常不建议这样做，因为这会导致相交的部分物体材料分布不明确。

> 图示要点：`Solid_Intersection_6.png` 展示“不选择任何物体用于之后的冲突情况”相关的操作界面或示例，后续审查通过后再补图。

## 页内/相关链接

- 两个物体相交时，旧的物体(形状A)会减去与新的物体(形状B)。详见布尔运算: `../Model_Editing/Boolean.html`
- 两个物体相交时，新的物体(形状B)会减去与旧的物体(形状A)。详见布尔运算: `../Model_Editing/Boolean.html`


## 待补图片清单
以下图片暂不插入正文，后续等人工审查后再从本机或官方帮助目录复制到知识库图片资源目录。
| 图片名称 | 当前资源路径 | 建议保留原因 |
| --- | --- | --- |
| Solid_Intersection_1.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Create_3D_Geometry/images/Solid_Intersection_1.png` | 展示“新物体”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Solid_Intersection_2.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Create_3D_Geometry/images/Solid_Intersection_2.png` | 展示“已经存在的物体”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Solid_Intersection_3.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Create_3D_Geometry/images/Solid_Intersection_3.png` | 展示“空”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Solid_Intersection_4.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Create_3D_Geometry/images/Solid_Intersection_4.png` | 展示“将新物体用于之后的冲突情况”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Solid_Intersection_5.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Create_3D_Geometry/images/Solid_Intersection_5.png` | 展示“将现有物体用于之后的冲突情况”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Solid_Intersection_6.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Create_3D_Geometry/images/Solid_Intersection_6.png` | 展示“不选择任何物体用于之后的冲突情况”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
