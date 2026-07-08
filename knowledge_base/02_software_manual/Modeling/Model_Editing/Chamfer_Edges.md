---
title: "倒斜角"
merged_source: "current_waveda_agent_kb"
source_relative_path: "Modeling/Model_Editing/Chamfer_Edges.html"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 倒斜角

- 原始相对路径: `Modeling/Model_Editing/Chamfer_Edges.html`
- 知识模块: `建模总览`

## 正文抽取
## 倒斜角

该功能常用于处理几何体的边缘，创建斜切或倒角的过渡，从而使模型的边缘更加平滑，避免尖锐的边缘或角落。 通常在制造、组装、或电磁仿真中使用。倒角常用于消除锐角，提高结构的机械强度或减少电磁波的反射。 这在建模过程中，特别是处理金属零件、微波组件、天线设计和电磁仿真时非常有用。

#### 激活倒斜角功能

切换到选线模式，选择要应用倒斜角的棱边。可以选择单个棱边，或者多个棱边进行倒角，选中主菜单栏“建模”->“形状”下的倒斜角

> 图示要点：`Chamfer_Edges_1.png` 展示“激活倒斜角功能”相关的操作界面或示例，后续审查通过后再补图。

图标。

> 图示要点：`Chamfer_Edges_5.png` 展示“激活倒斜角功能”相关的操作界面或示例，后续审查通过后再补图。

> 图示要点：`Chamfer_Edges_3.png` 展示“激活倒斜角功能”相关的操作界面或示例，后续审查通过后再补图。

#### 设置参数

> 图示要点：`Chamfer_Edges_2.png` 展示“设置参数”相关的操作界面或示例，后续审查通过后再补图。

输入倒角的两个主要参数：倒角距离和角度。

##### 倒角距离

这是倒角切除斜边的直线距离。软件默认15，可以根据需要设置其他距离。

注意：倒角距离是否适合几何，避免自相交或拓扑错误。

##### 角度

这是倒角的倾斜角度，软件默认45°，可以根据需要设置其他角度。点击“完成”后可以看到棱边变成了斜角边。

> 图示要点：`Chamfer_Edges_6.png` 展示“角度”相关的操作界面或示例，后续审查通过后再补图。

> 图示要点：`Chamfer_Edges_4.png` 展示“角度”相关的操作界面或示例，后续审查通过后再补图。

##### 反转

反转可以将倒角的方向反向，例如设置15°，设置的模型倒角的方向向下，点击“反转”，倒角的方向向上。

> 图示要点：`Chamfer_Edges_7.png` 展示“反转”相关的操作界面或示例，后续审查通过后再补图。

> 图示要点：`Chamfer_Edges_8.png` 展示“反转”相关的操作界面或示例，后续审查通过后再补图。

#### 相关文档

面平移调整， 倒圆角， 从现有面拉伸成体。

## 页内/相关链接

- 面平移调整: `../Model_Editing/Move_Face_To_Modify_Solid.html`
- 面平移调整， 倒圆角: `../Model_Editing/Blend_Edges.html`
- 面平移调整， 倒圆角， 从现有面拉伸成体: `../Model_Editing/Extrusion.html`


## 待补图片清单
以下图片暂不插入正文，后续等人工审查后再从本机或官方帮助目录复制到知识库图片资源目录。
| 图片名称 | 当前资源路径 | 建议保留原因 |
| --- | --- | --- |
| Chamfer_Edges_1.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Model_Editing/images/Chamfer_Edges_1.png` | 展示“激活倒斜角功能”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Chamfer_Edges_5.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Model_Editing/images/Chamfer_Edges_5.png` | 展示“激活倒斜角功能”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Chamfer_Edges_3.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Model_Editing/images/Chamfer_Edges_3.png` | 展示“激活倒斜角功能”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Chamfer_Edges_2.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Model_Editing/images/Chamfer_Edges_2.png` | 展示“设置参数”步骤的菜单或参数界面，便于新人按界面完成操作。 |
| Chamfer_Edges_6.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Model_Editing/images/Chamfer_Edges_6.png` | 展示“角度”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Chamfer_Edges_4.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Model_Editing/images/Chamfer_Edges_4.png` | 展示“角度”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Chamfer_Edges_7.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Model_Editing/images/Chamfer_Edges_7.png` | 展示“反转”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Chamfer_Edges_8.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Model_Editing/images/Chamfer_Edges_8.png` | 展示“反转”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
