---
title: "从现有面拉伸成体"
merged_source: "current_waveda_agent_kb"
source_relative_path: "10_extracted_pages/Modeling/Model_Editing/Extrusion.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\10_extracted_pages\Modeling\Model_Editing\Extrusion.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 从现有面拉伸成体

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\Extrusion.html`
- 原始相对路径: `Modeling/Model_Editing/Extrusion.html`
- 知识模块: `建模总览`

## 正文抽取
## 从现有面拉伸成体

> 图片: `./images/Extrusion_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extrusion_1.png`

此功能可以将面转换成体，同时也可以转换成特定的锥体。可以在界面上方修改拉伸体的名称。

#### 激活拉伸功能

选择要拉伸的二维形状，可以是一个简单的轮廓（如矩形、圆形、多边形等）。软件只支持对单个面进行突出。 切换到选面模式，选择要应用面突出的面。选中主菜单栏“建模”->“形状”下的“从现有面拉伸成体”

> 图片: `./images/Extrusion_7.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extrusion_7.png`

图标。

#### 高度

设置参数为选中的面拉伸成体的高度。以长方体为示例操作，选择长方体的顶面作为操作面。

> 图片: `./images/Extrusion_6.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extrusion_6.png`

设置高度为200，原始模型高度为100，点击“预览”，可以看到拉伸后的模型高度为原始模型的两倍。

> 图片: `./images/Extrusion_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extrusion_1.png`

> 图片: `./images/Extrusion_5.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extrusion_5.png`

#### 锥形化

此参数是将面拉伸成锥体需要转换的角度，设置后可以得到以选中面为底面，高度为200，推出锥形化角度为45°的锥体。

> 图片: `./images/Extrusion_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extrusion_2.png`

> 图片: `./images/Extrusion_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extrusion_3.png`

注意：可以选择矩形和圆形拉伸成锥体，但是不规则的多边形不支持使用该功能，锥形化只能为默认参数0。

#### 原始材料

选择需要的材料作为拉伸后体的材料，软件默认不勾选，即默认为PEC材料。若勾选了原始材料，则默认跟随面的材料定义体的材料。

#### 选点模式

若没有通过选面模式创建，可以在选点模式中定义拉伸的点的坐标，以便为突出操作提供轮廓曲线。

#### 相关文档

倒斜角， 面平移调整， 倒圆角。

## 图片资源

1. `./images/Extrusion_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extrusion_1.png`
2. `./images/Extrusion_7.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extrusion_7.png`
3. `./images/Extrusion_6.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extrusion_6.png`
4. `./images/Extrusion_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extrusion_1.png`
5. `./images/Extrusion_5.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extrusion_5.png`
6. `./images/Extrusion_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extrusion_2.png`
7. `./images/Extrusion_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Extrusion_3.png`

## 页内/相关链接

- 倒斜角: `../Model_Editing/Chamfer_Edges.html`
- 倒斜角， 面平移调整: `../Model_Editing/Move_Face_To_Modify_Solid.html`
- 倒斜角， 面平移调整， 倒圆角: `../Model_Editing/Blend_Edges.html`
