# 倒圆角

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\Blend_Edges.html`
- 原始相对路径: `Modeling/Model_Editing/Blend_Edges.html`
- 知识模块: `建模总览`

## 正文抽取
## 倒圆角

该功能常用于在构建复杂几何体时，用于平滑连接不同表面或边缘。 它有助于减少几何体中不同面或曲面之间的硬过渡，使得模型更加自然、平滑，尤其是在进行电磁场仿真时，平滑过渡可以避免不必要的奇异点或不连续性。 优点在于可以减少尖锐边缘对美观和物理性能的影响。

#### 激活倒圆角功能

切换到选线模式，选择要应用倒圆角的棱边。可以选择单个棱边，或者多个棱边进行倒圆角，选中主菜单栏“建模”的“形状”下的倒圆角图标。

> 图片: `./images/Blend_Edges_5.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Blend_Edges_5.png`

> 图片: `./images/Blend_Edges_4.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Blend_Edges_4.png`

#### 半径

> 图片: `./images/Blend_Edges_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Blend_Edges_1.png`

半径决定了两个面或边缘之间平滑过渡的范围。过渡半径越大，过渡区域的曲率就越大，连接的区域越平滑。软件默认为15°。 对于大多数设计，建议开始时选择较小的半径。 确保在设置倒圆角时，点击“预览”模型查看整体效果，避免局部过渡过于极端。点击“完成”后你可以看到棱边变成了平滑过渡的弧边。

> 图片: `./images/Blend_Edges_6.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Blend_Edges_6.png`

> 图片: `./images/Blend_Edges_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Blend_Edges_3.png`

注意：过渡半径的选择是否合理。过渡半径过大可能会导致几何不相交或拓扑错误，过小可能达不到预期效果。

#### 相关文档

面平移调整， 倒斜角， 从现有面拉伸成体。

## 图片资源

1. `./images/Blend_Edges_5.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Blend_Edges_5.png`
2. `./images/Blend_Edges_4.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Blend_Edges_4.png`
3. `./images/Blend_Edges_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Blend_Edges_1.png`
4. `./images/Blend_Edges_6.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Blend_Edges_6.png`
5. `./images/Blend_Edges_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Blend_Edges_3.png`

## 页内/相关链接

- 面平移调整: `../Model_Editing/Move_Face_To_Modify_Solid.html`
- 面平移调整， 倒斜角: `../Model_Editing/Chamfer_Edges.html`
- 面平移调整， 倒斜角， 从现有面拉伸成体: `../Model_Editing//Extrusion.html`
