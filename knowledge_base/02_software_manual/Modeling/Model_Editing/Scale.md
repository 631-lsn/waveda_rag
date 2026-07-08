---
title: "缩放"
merged_source: "current_waveda_agent_kb"
source_relative_path: "Modeling/Model_Editing/Scale.html"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 缩放

- 原始相对路径: `Modeling/Model_Editing/Scale.html`
- 知识模块: `建模总览`

## 正文抽取
## 缩放

缩放操作可对体与面进行放大与缩小，该功能只能在选中物体后才会被激活，且可通过预览按钮检查操作的正确性。

> 图示要点：`Scale_1.png` 展示“缩放”相关的操作界面或示例，后续审查通过后再补图。

#### 缩放原点

缩放原点可选择“在GSC(全局坐标系)上自定义点”，“在LSC(局部坐标系)上自定义点”，“单体质心”以及“边界盒子中心”。 其中“在GSC(全局坐标系)上自定义点”和“在LSC(局部坐标系)上自定义点”选项需要输入点的坐标或在选点模式下选中点， “单体质心”和“边界盒子中心”由WavEDA判断缩放原点坐标。

#### 缩放因子

可单独给定U轴、V轴、W轴的缩放因子（大于0），也可勾选下图所示“统一缩放因子”复选框，只输入单个数字即可。

> 图示要点：`Scale_2.png` 展示“缩放因子”相关的操作界面或示例，后续审查通过后再补图。

对于面的缩放操作，面的厚度方向上的缩放因子无效。

#### 高级

如下图，若勾选保留原始物体复选框可保留原始物体，开启后可输入旋转生成的物体名称。

> 图示要点：`Scale_3.png` 展示“高级”相关的操作界面或示例，后续审查通过后再补图。

如下图，若勾选链接受影响的对象复选框，在保留原始物体的基础上，更改原始物体属性时，旋转生成的物体也会一起被修改。

> 图示要点：`Scale_4.png` 展示“高级”相关的操作界面或示例，后续审查通过后再补图。

#### 例子

尺寸为100*100*100的正方体，选择正方体的一个角点为缩放点，缩放因子为2，效果如下图所示。

> 图示要点：`Scale_7.png` 展示“例子”相关的操作界面或示例，后续审查通过后再补图。

#### 相关文档

阵列复制， 移动， 镜像， 旋转， 与坐标系平面对齐， 切割， 挖空。

## 页内/相关链接

- 阵列复制: `../Model_Editing/Array_Copy.html`
- 阵列复制， 移动: `../Model_Editing/Translate.html`
- 阵列复制， 移动， 镜像: `../Model_Editing/Mirror.html`
- 阵列复制， 移动， 镜像， 旋转: `../Model_Editing/Rotate.html`
- 阵列复制， 移动， 镜像， 旋转， 与坐标系平面对齐: `../Model_Editing/Align.html`
- 阵列复制， 移动， 镜像， 旋转， 与坐标系平面对齐， 切割: `../Model_Editing/Split.html`
- 阵列复制， 移动， 镜像， 旋转， 与坐标系平面对齐， 切割， 挖空: `../Model_Editing/Shell.html`


## 待补图片清单
以下图片暂不插入正文，后续等人工审查后再从本机或官方帮助目录复制到知识库图片资源目录。
| 图片名称 | 当前资源路径 | 建议保留原因 |
| --- | --- | --- |
| Scale_1.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Model_Editing/images/Scale_1.png` | 展示“缩放”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Scale_2.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Model_Editing/images/Scale_2.png` | 展示“缩放因子”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Scale_3.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Model_Editing/images/Scale_3.png` | 展示“高级”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Scale_4.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Model_Editing/images/Scale_4.png` | 展示“高级”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Scale_7.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Model_Editing/images/Scale_7.png` | 展示“例子”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
