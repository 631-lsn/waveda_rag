---
title: "Multi_Conductors"
merged_source: "current_waveda_agent_kb"
source_relative_path: "Modeling/Stimulate/Multi_Conductors.html"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# Multi_Conductors

- 原始相对路径: `Modeling/Stimulate/Multi_Conductors.html`
- 知识模块: `建模总览`

## 正文抽取
## 波端口多导体

波端口多导体设置一般应用于波端口中导体数量大于2的模型。 当波端口中有N个导体时，存在N-1个TEM模，此时可通过多导体设置，给定每个导体的电势以确定模式。

点击以下按钮可进入波端口多导体设置界面，WavEDA支持两种多导体设置方法，模式设置方法和终端设置方法。 其中终端设置方法只能将导体设置成差分对和单端形式，模式设置方法可任意设置各导体的电势。

> 图示要点：`Multi_Conductors_1.png` 展示“波端口多导体”相关的操作界面或示例，后续审查通过后再补图。

### 模式设置方法

当波端口激励的传输线类型为CPW传输线、GCPW传输线以及导体数目大于2的传输线时，一般需要用模式设置方法控制端口模式。

模式设置方法界面如下图，该界面中，左上角给出了波端口中导体的分布情况，并依次将导体命名为EC1，EC2，EC3... 而右侧列表列出了波端口中的电导体以及磁导体。

> 图示要点：`Multi_Conductors_2.png` 展示“模式设置方法”相关的操作界面或示例，后续审查通过后再补图。

下面电势设计列表列出了每个模式下各导体的电势。用模式设置方法设置导体电势时， 只能定义TEM模和准TEM模的电势，因此该列表中模式数量为N-1。 双击列表中各电势，可引出下拉菜单切换导体电势。

> 图示要点：`Multi_Conductors_4.png` 展示“模式设置方法”相关的操作界面或示例，后续审查通过后再补图。

为明确模式设置方法对模式的控制效果，下图给出了四根内导体电缆在模式设置方法对应电势设置下的模式分析。

> 图示要点：`Multi_Conductors_7.png` 展示“模式设置方法”相关的操作界面或示例，后续审查通过后再补图。

下图给出了波端口激励CPW传输线时，在模式设计方法下的电势设置，以及模式分析结果。 为保证之后全波仿真正确性，需确保同一个端口设置模式场不一致。

> 图示要点：`Multi_Conductors_6.png` 展示“模式设置方法”相关的操作界面或示例，后续审查通过后再补图。

### 终端设置方法

WavEDA中的终端设置方法只用于将单个模式下的导体电势，设置成差分共模或者单端的形式。 可用于计算波端口馈电情况下的差分共模信号仿真，其设置界面如下图。

> 图示要点：`Multi_Conductors_3.png` 展示“终端设置方法”相关的操作界面或示例，后续审查通过后再补图。

WavEDA在设置终端形式的波端口时，必须选择一个导体为参考导体，通常选择信号的共地导体为参考导体。 设置好参考地后，该导体各个模式下的电势将置为0。点击差分对设置，进入下图所示差分对设置窗口。

> 图示要点：`Multi_Conductors_5.png` 展示“终端设置方法”相关的操作界面或示例，后续审查通过后再补图。

点击添加差分对，左侧列表会列出差分对配对情况，同样在列表的下拉列表中选择 差分对中正负极性对应的导体。 差分对的设置中，不能重复用一个导体去定义差分对，由此也可知差分对数量是有限制的。 设置好差分对后，导体的电势设置将会显示在终端设置方法下面的列表中。

下图给出了微带差分线的波端口设置以及其模式分析结果。 从模式图中可以看出，此时，模式1对应差模分析结果，模式2对应共模分析结果。 在之后的全波仿真结果中，模式与差分共模结果对应也是如此。

> 图示要点：`Multi_Conductors_8.png` 展示“终端设置方法”相关的操作界面或示例，后续审查通过后再补图。


## 待补图片清单
以下图片暂不插入正文，后续等人工审查后再从本机或官方帮助目录复制到知识库图片资源目录。
| 图片名称 | 当前资源路径 | 建议保留原因 |
| --- | --- | --- |
| Multi_Conductors_1.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Stimulate/images/Multi_Conductors_1.png` | 展示“波端口多导体”相关界面或示例，后续审查时判断是否需要作为辅助配图。 |
| Multi_Conductors_2.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Stimulate/images/Multi_Conductors_2.png` | 展示“模式设置方法”步骤的菜单或参数界面，便于新人按界面完成操作。 |
| Multi_Conductors_4.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Stimulate/images/Multi_Conductors_4.png` | 展示“模式设置方法”步骤的菜单或参数界面，便于新人按界面完成操作。 |
| Multi_Conductors_7.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Stimulate/images/Multi_Conductors_7.png` | 展示“模式设置方法”步骤的菜单或参数界面，便于新人按界面完成操作。 |
| Multi_Conductors_6.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Stimulate/images/Multi_Conductors_6.png` | 展示“模式设置方法”步骤的菜单或参数界面，便于新人按界面完成操作。 |
| Multi_Conductors_3.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Stimulate/images/Multi_Conductors_3.png` | 展示“终端设置方法”步骤的菜单或参数界面，便于新人按界面完成操作。 |
| Multi_Conductors_5.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Stimulate/images/Multi_Conductors_5.png` | 展示“终端设置方法”步骤的菜单或参数界面，便于新人按界面完成操作。 |
| Multi_Conductors_8.png | `wavEDA_docs/helpHtml/helpHtml/Modeling/Stimulate/images/Multi_Conductors_8.png` | 展示“终端设置方法”步骤的菜单或参数界面，便于新人按界面完成操作。 |
