# 波端口积分线

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\Integration_Line.html`
- 原始相对路径: `Modeling/Stimulate/Integration_Line.html`
- 知识模块: `建模总览`

## 正文抽取
## 波端口积分线

波端口积分线用于模式对齐以及极性设置，通常应用于波端口为单导体以及双导体的情况下。 波端口包含多导体时，建议使用波端口多导体功能来设置导体电势。

下图为WavEDA积分线设置界面，可以选择“使用积分线设置模式极性”和“使用积分线对齐模式”来选择积分线对模式的控制作用。

> 图片: `./images/Integration_Line_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Integration_Line_1.png`

### 创建积分线

切换到积分线创建窗口后，建模界面会切换到选点模式。选取起始点和结束点定义积分线，积分线可点击反向切换方向。 起始点和结束点一般选取对应模式下，电势差最大的两个点。对于双导体波端口，积分线起始和结束点通常分布在两个导体上。

创建积分线后，点击预览在建模视图中查看各个模式下的积分线情况，下图给出了矩形波端口在三个模式下设置的三条积分线情况图。

> 图片: `./images/Integration_Line_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Integration_Line_2.png`

### 使用积分线设置模式极性

该选项下，积分线可用来设置模式中电场的极性，但无法控制电场的方向。 当模型存在两个或两个以上的波端口，且端口之间模式电场的方向需要对齐时，通常会选择该选项。 下图给出了两个同轴波端口在设置积分线前（左）后（右）模式图。当两个端口模式的极性明确时，S参数的相位才具有参考性。

> 图片: `./images/Integration_Line_5.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Integration_Line_5.png`

> 图片: `./images/Integration_Line_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Integration_Line_3.png`

> 图片: `./images/Integration_Line_4.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Integration_Line_4.png`

### 使用积分线对齐模式

该选项下，积分线用来设置模式中电压的积分方向。当波端口存在简并模式需要区分时， 需选择该选项，并给出所有简并模的电场的方向为各模式的积分线方向，否则WavEDA将随机给定模式。 下面给出了圆波导在模式对齐前（上）后（下）的模式图，只有在模式对齐后，S参数结果才具有参考性。

> 图片: `./images/Integration_Line_8.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Integration_Line_8.png`

> 图片: `./images/Integration_Line_6_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Integration_Line_6_1.png`

> 图片: `./images/Integration_Line_6_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Integration_Line_6_2.png`

## 图片资源

1. `./images/Integration_Line_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Integration_Line_1.png`
2. `./images/Integration_Line_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Integration_Line_2.png`
3. `./images/Integration_Line_5.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Integration_Line_5.png`
4. `./images/Integration_Line_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Integration_Line_3.png`
5. `./images/Integration_Line_4.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Integration_Line_4.png`
6. `./images/Integration_Line_8.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Integration_Line_8.png`
7. `./images/Integration_Line_6_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Integration_Line_6_1.png`
8. `./images/Integration_Line_6_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Integration_Line_6_2.png`

## 页内/相关链接

- 波端口积分线用于模式对齐以及极性设置，通常应用于波端口为单导体以及双导体的情况下。 波端口包含多导体时，建议使用波端口多导体: `./Multi_Conductors.html`
