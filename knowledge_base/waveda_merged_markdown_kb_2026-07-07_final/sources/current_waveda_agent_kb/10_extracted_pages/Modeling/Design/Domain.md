---
title: "计算区域"
merged_source: "current_waveda_agent_kb"
source_relative_path: "10_extracted_pages/Modeling/Design/Domain.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\10_extracted_pages\Modeling\Design\Domain.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 计算区域

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\Domain.html`
- 原始相对路径: `Modeling/Design/Domain.html`
- 知识模块: `建模总览`

## 正文抽取
## 计算区域

- 计算区域形状 - 间距 - 边界区域尺寸

计算区域定义了电磁场方程的求解空间范围，确定计算区域以及边界条件后，可通过求解区域以及边界上的Maxwell方程计算各类激励下的电磁场问题。 在电磁仿真中，计算区域的设置直接影响仿真结果的精度、计算效率和资源消耗。

首先要选择计算区域形状，再设置对应的间距，此时边界区域尺寸就会显示在右下角区域。 可以双击左侧工程树下“设计”->“计算区域”打开对话框。 也可以点击上方主菜单栏中“建模”->“设计”->“计算区域”

> 图片: `./images/Domain_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_1.png`

图标打开对话框。

### 计算区域形状

可以设置以下不同形状的计算区域的盒子；

- 包围所有物体的长方体盒子作为计算区域；

> 图片: `./images/Domain_6.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_6.png`

- 仅计算3D物体所在区域：以模型本身的形状作为计算区域，常常适用于不规则的模型。

> 图片: `./images/Domain_7.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_7.png`

同时，切换设置时右上角示意图也会提示当前选择的选项。

### 间距

选择区域形状后可以修改模型与边界的间距，此时可设置长方体各面与物体的距离，从而定义计算区域的尺寸。目前只有长方体盒子为计算区域可以修改边界的间距，且默认此长方体内填充材料为Air。 此处的单位都是跟随系统单位设置。有以下四种方式可以修改：

> 图片: `./images/Domain_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_2.png`

- 无间距，不需要设置任何参数，边界即贴在模型外部。

> 图片: `./images/Domain_8.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_8.png`

- 自动间距，软件提供自动计算波长功能，默认为中心频率计算出来的四分之一波长。如图例模型的扫频范围为1-10 GHz，中心频率为5.5 GHz，软件计算出的四分之一波长为13.6269 mm。

> 图片: `./images/Domain_9.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_9.png`

根据用户设置的频率计算出四分之一波长。如图例定义8 GHz，软件计算出的四分之一波长为9.3685 mm。

> 图片: `./images/Domain_10.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_10.png`

- 自定义间距，根据用户给定的间距数据，默认勾选“应用至所有方向”，只需要设置一次，该间距会应用到所有方向。如图例，设置间距为100，则X/Y/Z方向的间距都为100。

> 图片: `./images/Domain_11.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_11.png`

取消勾选“应用至所有方向”，用户根据需求分别设置模型在X/Y/Z方向上的间距。如图例，设置X方向间距为100，Y方向间距为100，Z方向间距为0。

> 图片: `./images/Domain_12.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_12.png`

- 自定义校正边界盒子，可以理解为参数化建模计算区域盒子，同样需要用户手动输入空气盒子在X/Y/Z方向上的数据，输入参数时需要注意负方向的数值要小于正方向的数值。 建议根据无间距状态下的模型在X/Y/Z方向的尺寸进行增加间距设置。 如图例，无间距下的模型尺寸各个方向都为50，设置-X方向间距为150，+X方向间距为150，-Y方向间距为150，+Y方向间距为150，-Z方向间距为150，+Z方向间距为150。 得到各个方向间距为100的计算区域。

> 图片: `./images/Domain_13.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_13.png`

### 边界区域尺寸

以上设置完会在该区域显示出当前边界盒子的尺寸数据。

> 图片: `./images/Domain_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_3.png`

## 图片资源

1. `./images/Domain_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_1.png`
2. `./images/Domain_6.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_6.png`
3. `./images/Domain_7.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_7.png`
4. `./images/Domain_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_2.png`
5. `./images/Domain_8.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_8.png`
6. `./images/Domain_9.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_9.png`
7. `./images/Domain_10.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_10.png`
8. `./images/Domain_11.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_11.png`
9. `./images/Domain_12.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_12.png`
10. `./images/Domain_13.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_13.png`
11. `./images/Domain_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Domain_3.png`

## 页内/相关链接

- - 计算区域形状: `#计算区域形状`
- - 计算区域形状 - 间距: `#间距`
- - 计算区域形状 - 间距 - 边界区域尺寸: `#边界区域尺寸`
- 首先要选择计算区域形状: `#计算区域形状`
- 首先要选择计算区域形状，再设置对应的间距: `#间距`
- 首先要选择计算区域形状，再设置对应的间距，此时边界区域尺寸: `#边界区域尺寸`
