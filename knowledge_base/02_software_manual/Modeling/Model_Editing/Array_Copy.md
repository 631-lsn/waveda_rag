---
title: "阵列复制"
merged_source: "current_waveda_agent_kb"
source_relative_path: "Modeling/Model_Editing/Array_Copy.html"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 阵列复制

- 原始相对路径: `Modeling/Model_Editing/Array_Copy.html`
- 知识模块: `建模总览`

## 正文抽取
## 阵列复制

阵列复制可用于将物体进行多方向上（单次最多在三个方向上）等间距多次复制，该功能只能在选中物体后才会被激活， 且可通过预览按钮检查阵列复制的正确性。

> 图示要点：`Array_Copy_1.png` 展示“阵列复制”相关的操作界面或示例，后续审查通过后再补图。

#### 阵列名称

给阵列赋一个唯一的名称，WavEDA会自动根据阵列创建的顺序命名为 ac_n（n = 1,2,3...）， 修改阵列名称后可点击检查名称按钮判断改名称是否合法。

#### 阵列属性

如下图所示，WavEDA默认启用方向一方向的阵列复制。

> 图示要点：`Array_Copy_2.png` 展示“阵列属性”相关的操作界面或示例，后续审查通过后再补图。

启用方向后，可通过“位移”和“复制数量”确定阵列复制属性。其中“位移”可通过选点确定，在选点模式下选中两点，点击“选点”按钮即可。

#### 第一个阵列单元间距

该对话框可给定第一个阵列单元与原始物体的间距，勾选“删除原始物体”可删除原始物体。

#### 例子

球体向X和Y方向同时阵列复制十次，效果如下图。

> 图示要点：`Array_Copy_3.png` 展示“例子”相关的操作界面或示例，后续审查通过后再补图。

#### 相关文档

移动， 镜像， 旋转， 缩放， 切割， 与坐标系平面对齐， 挖空。

## 页内/相关链接

- 移动: `../Model_Editing/Translate.html`
- 移动， 镜像: `../Model_Editing/Mirror.html`
- 移动， 镜像， 旋转: `../Model_Editing/Rotate.html`
- 移动， 镜像， 旋转， 缩放: `../Model_Editing/Scale.html`
- 移动， 镜像， 旋转， 缩放， 切割: `../Model_Editing/Split.html`
- 移动， 镜像， 旋转， 缩放， 切割， 与坐标系平面对齐: `../Model_Editing/Align.html`
- 移动， 镜像， 旋转， 缩放， 切割， 与坐标系平面对齐， 挖空: `../Model_Editing/Shell.html`


## 待补图片清单
以下图片暂不插入正文，路径为 WavEDA 帮助文档内部相对路径；运行时 agent 会按项目内帮助图片和用户本机 WavEDA 帮助目录进行查找。
| 图片名称 | WavEDA 帮助相对路径 | 建议保留原因 |
| --- | --- | --- |
| Array_Copy_1.png | `Modeling/Model_Editing/images/Array_Copy_1.png` | 展示“阵列复制”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Array_Copy_2.png | `Modeling/Model_Editing/images/Array_Copy_2.png` | 展示“阵列属性”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Array_Copy_3.png | `Modeling/Model_Editing/images/Array_Copy_3.png` | 展示“例子”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
