---
title: "从现有面拉伸成体"
merged_source: "current_waveda_agent_kb"
source_relative_path: "Modeling/Model_Editing/Extrusion.html"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 从现有面拉伸成体

- 原始相对路径: `Modeling/Model_Editing/Extrusion.html`
- 知识模块: `建模总览`

## 正文抽取
## 从现有面拉伸成体

> 图示要点：`Extrusion_1.png` 展示“从现有面拉伸成体”相关的操作界面或示例，后续审查通过后再补图。

此功能可以将面转换成体，同时也可以转换成特定的锥体。可以在界面上方修改拉伸体的名称。

#### 激活拉伸功能

选择要拉伸的二维形状，可以是一个简单的轮廓（如矩形、圆形、多边形等）。软件只支持对单个面进行突出。 切换到选面模式，选择要应用面突出的面。选中主菜单栏“建模”->“形状”下的“从现有面拉伸成体”

> 图示要点：`Extrusion_7.png` 展示“激活拉伸功能”相关的操作界面或示例，后续审查通过后再补图。

图标。

#### 高度

设置参数为选中的面拉伸成体的高度。以长方体为示例操作，选择长方体的顶面作为操作面。

> 图示要点：`Extrusion_6.png` 展示“高度”相关的操作界面或示例，后续审查通过后再补图。

设置高度为200，原始模型高度为100，点击“预览”，可以看到拉伸后的模型高度为原始模型的两倍。

> 图示要点：`Extrusion_1.png` 展示“高度”相关的操作界面或示例，后续审查通过后再补图。

> 图示要点：`Extrusion_5.png` 展示“高度”相关的操作界面或示例，后续审查通过后再补图。

#### 锥形化

此参数是将面拉伸成锥体需要转换的角度，设置后可以得到以选中面为底面，高度为200，推出锥形化角度为45°的锥体。

> 图示要点：`Extrusion_2.png` 展示“锥形化”相关的操作界面或示例，后续审查通过后再补图。

> 图示要点：`Extrusion_3.png` 展示“锥形化”相关的操作界面或示例，后续审查通过后再补图。

注意：可以选择矩形和圆形拉伸成锥体，但是不规则的多边形不支持使用该功能，锥形化只能为默认参数0。

#### 原始材料

选择需要的材料作为拉伸后体的材料，软件默认不勾选，即默认为PEC材料。若勾选了原始材料，则默认跟随面的材料定义体的材料。

#### 选点模式

若没有通过选面模式创建，可以在选点模式中定义拉伸的点的坐标，以便为突出操作提供轮廓曲线。

#### 相关文档

倒斜角， 面平移调整， 倒圆角。

## 页内/相关链接

- 倒斜角: `../Model_Editing/Chamfer_Edges.html`
- 倒斜角， 面平移调整: `../Model_Editing/Move_Face_To_Modify_Solid.html`
- 倒斜角， 面平移调整， 倒圆角: `../Model_Editing/Blend_Edges.html`


## 待补图片清单
以下图片暂不插入正文，路径为 WavEDA 帮助文档内部相对路径；运行时 agent 会按项目内帮助图片和用户本机 WavEDA 帮助目录进行查找。
| 图片名称 | WavEDA 帮助相对路径 | 建议保留原因 |
| --- | --- | --- |
| Extrusion_1.png | `Modeling/Model_Editing/images/Extrusion_1.png` | 展示“从现有面拉伸成体”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Extrusion_7.png | `Modeling/Model_Editing/images/Extrusion_7.png` | 展示“激活拉伸功能”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Extrusion_6.png | `Modeling/Model_Editing/images/Extrusion_6.png` | 展示“高度”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Extrusion_5.png | `Modeling/Model_Editing/images/Extrusion_5.png` | 展示“高度”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Extrusion_2.png | `Modeling/Model_Editing/images/Extrusion_2.png` | 展示“锥形化”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Extrusion_3.png | `Modeling/Model_Editing/images/Extrusion_3.png` | 展示“锥形化”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
