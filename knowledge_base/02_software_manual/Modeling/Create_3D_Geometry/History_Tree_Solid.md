---
title: "历史树-体"
merged_source: "current_waveda_agent_kb"
source_relative_path: "Modeling/Create_3D_Geometry/History_Tree_Solid.html"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 历史树-体

- 原始相对路径: `Modeling/Create_3D_Geometry/History_Tree_Solid.html`
- 知识模块: `建模总览`

## 正文抽取
## 历史树-体

双击编辑后的体，在体的属性窗口中记录体的所有操作步骤，即体的历史树。 WavEDA的体-历史树支持模型编辑和历史操作撤回等操作，下面将逐一介绍。

> 图示要点：`History_Tree_Solid_1.png` 展示“历史树-体”相关的操作界面或示例，后续审查通过后再补图。

### 布尔操作

在历史树中可直接对该模型与列出的几何形状进行布尔运算。

> 图示要点：`History_Tree_Solid_2.png` 展示“布尔操作”相关的操作界面或示例，后续审查通过后再补图。

#### 操作步骤：

- 选中在相加、相减或相交。

- 点击另一种模型类型进行创建。

- 创建过程中选择预览，确定另一个模型的位置和大小。

- 点击完成，查看效果。

以一个正方体加上一个小球为例：

- 双击正方体，打开历史树。

> 图示要点：`History_Tree_Solid_7.png` 展示“操作步骤：”相关的操作界面或示例，后续审查通过后再补图。

- 选中相加布尔操作，点击圆，填入尺寸。

> 图示要点：`History_Tree_Solid_4.png` 展示“操作步骤：”相关的操作界面或示例，后续审查通过后再补图。

- 点击预览查看效果，点击完成。

> 图示要点：`History_Tree_Solid_5.png` 展示“操作步骤：”相关的操作界面或示例，后续审查通过后再补图。

- 此时即完成了在历史树中完成一次布尔操作的操作，且该此操作加在了历史树中。

> 图示要点：`History_Tree_Solid_6.png` 展示“操作步骤：”相关的操作界面或示例，后续审查通过后再补图。

### 撤销操作

选中之前对模型的编辑操作，可进行撤销，还原等操作。图中依次为删除，解除关联以及恢复操作。

> 图示要点：`History_Tree_Solid_8.png` 展示“撤销操作”相关的操作界面或示例，后续审查通过后再补图。

- 删除：选中操作，点击删除，即可删除操作。

- 解除关联：解除该操作时，两个或多个物体之间的关联。

- 恢复：将原始物体恢复。


## 待补图片清单
以下图片暂不插入正文，路径为 WavEDA 帮助文档内部相对路径；运行时 agent 会按项目内帮助图片和用户本机 WavEDA 帮助目录进行查找。
| 图片名称 | WavEDA 帮助相对路径 | 建议保留原因 |
| --- | --- | --- |
| History_Tree_Solid_1.png | `Modeling/Create_3D_Geometry/images/History_Tree_Solid_1.png` | 展示“历史树-体”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| History_Tree_Solid_2.png | `Modeling/Create_3D_Geometry/images/History_Tree_Solid_2.png` | 展示“布尔操作”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| History_Tree_Solid_7.png | `Modeling/Create_3D_Geometry/images/History_Tree_Solid_7.png` | 展示“操作步骤：”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| History_Tree_Solid_4.png | `Modeling/Create_3D_Geometry/images/History_Tree_Solid_4.png` | 展示“操作步骤：”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| History_Tree_Solid_5.png | `Modeling/Create_3D_Geometry/images/History_Tree_Solid_5.png` | 展示“操作步骤：”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| History_Tree_Solid_6.png | `Modeling/Create_3D_Geometry/images/History_Tree_Solid_6.png` | 展示“操作步骤：”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| History_Tree_Solid_8.png | `Modeling/Create_3D_Geometry/images/History_Tree_Solid_8.png` | 展示“撤销操作”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
