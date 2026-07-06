# 缩放

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\Scale.html`
- 原始相对路径: `Modeling/Model_Editing/Scale.html`
- 知识模块: `建模总览`

## 正文抽取
## 缩放

缩放操作可对体与面进行放大与缩小，该功能只能在选中物体后才会被激活，且可通过预览按钮检查操作的正确性。

> 图片: `./images/Scale_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Scale_1.png`

#### 缩放原点

缩放原点可选择“在GSC(全局坐标系)上自定义点”，“在LSC(局部坐标系)上自定义点”，“单体质心”以及“边界盒子中心”。 其中“在GSC(全局坐标系)上自定义点”和“在LSC(局部坐标系)上自定义点”选项需要输入点的坐标或在选点模式下选中点， “单体质心”和“边界盒子中心”由WavEDA判断缩放原点坐标。

#### 缩放因子

可单独给定U轴、V轴、W轴的缩放因子（大于0），也可勾选下图所示“统一缩放因子”复选框，只输入单个数字即可。

> 图片: `./images/Scale_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Scale_2.png`

对于面的缩放操作，面的厚度方向上的缩放因子无效。

#### 高级

如下图，若勾选保留原始物体复选框可保留原始物体，开启后可输入旋转生成的物体名称。

> 图片: `./images/Scale_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Scale_3.png`

如下图，若勾选链接受影响的对象复选框，在保留原始物体的基础上，更改原始物体属性时，旋转生成的物体也会一起被修改。

> 图片: `./images/Scale_4.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Scale_4.png`

#### 例子

尺寸为100*100*100的正方体，选择正方体的一个角点为缩放点，缩放因子为2，效果如下图所示。

> 图片: `./images/Scale_7.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Scale_7.png`

#### 相关文档

阵列复制， 移动， 镜像， 旋转， 与坐标系平面对齐， 切割， 挖空。

## 图片资源

1. `./images/Scale_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Scale_1.png`
2. `./images/Scale_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Scale_2.png`
3. `./images/Scale_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Scale_3.png`
4. `./images/Scale_4.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Scale_4.png`
5. `./images/Scale_7.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Model_Editing\images\Scale_7.png`

## 页内/相关链接

- 阵列复制: `../Model_Editing/Array_Copy.html`
- 阵列复制， 移动: `../Model_Editing/Translate.html`
- 阵列复制， 移动， 镜像: `../Model_Editing/Mirror.html`
- 阵列复制， 移动， 镜像， 旋转: `../Model_Editing/Rotate.html`
- 阵列复制， 移动， 镜像， 旋转， 与坐标系平面对齐: `../Model_Editing/Align.html`
- 阵列复制， 移动， 镜像， 旋转， 与坐标系平面对齐， 切割: `../Model_Editing/Split.html`
- 阵列复制， 移动， 镜像， 旋转， 与坐标系平面对齐， 切割， 挖空: `../Model_Editing/Shell.html`
