---
title: "边界"
merged_source: "current_waveda_agent_kb"
source_relative_path: "EM_Project/Boundary.html"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 边界

- 原始相对路径: `EM_Project/Boundary.html`
- 知识模块: `EM设计与结果`

## 正文抽取
## 边界

- 默认边界条件 - 设置边界条件

### 默认边界条件

默认边界条件选项可进行计算区域边界条件的设置。

> 图示要点：`Boundary_1.png` 展示“默认边界条件”相关的操作界面或示例，后续审查通过后再补图。

> 图示要点：`Boundary_2.png` 展示“默认边界条件”相关的操作界面或示例，后续审查通过后再补图。

- 开放边界：分为一阶吸收边界ABC边界和完美匹配层PML边界，适用于天线辐射问题，但其吸收性能与入射角和距离有关，计算天线等强辐射问题时，距离辐射体应至少四分之一波长。 有关完美匹配层PML设置如下图所示： 图中，单元表示PML往外扩展多少个单元，多项式表示PML 多项式系数，衰减因子表示PML衰减系数，伸缩因子表示PML空间坐标伸缩系数。

- 理想电导体边界：即PEC边界，电场垂直于平面。

- 理想磁导体边界：即PMC边界，电场平行于平面，磁场垂直于平面。

### 设置边界条件

边界条件还可根据模型或自定义面进行不同方向上不同边界条件的设置，右击工程树下的边界选项，可进入边界条件设置界面。

> 图示要点：`Boundary_3.png` 展示“设置边界条件”相关的操作界面或示例，后续审查通过后再补图。

- 辐射ABC边界：点击辐射边界，可进入辐射边界设置界面，选择一个或多个方向或点击自定义面选择面进行辐射边界设置，同时还可在建模窗口选择要设置的面， 鼠标右键设置ABC边界条件。

> 图示要点：`Boundary_4.png` 展示“设置边界条件”相关的操作界面或示例，后续审查通过后再补图。

- 完美匹配层PML边界：点击PML边界，可进入PML边界设置界面，选择一个或多个方向进行PML边界设置，有关高级设置在上一章节已经介绍。

> 图示要点：`Boundary_5.png` 展示“设置边界条件”相关的操作界面或示例，后续审查通过后再补图。

- 完美电导体PEC边界：其设置与ABC边界类似。

> 图示要点：`Boundary_6.png` 展示“设置边界条件”相关的操作界面或示例，后续审查通过后再补图。

- 完美磁导体PMC边界：其设置与ABC边界类似。

> 图示要点：`Boundary_7.png` 展示“设置边界条件”相关的操作界面或示例，后续审查通过后再补图。

- 阻抗边界：其设置与ABC边界类似。通常用于近似描述某些物理介质（如金属表面、导电层、或者具有特定电磁响应的材料表面）的边界。

> 图示要点：`Boundary_8.png` 展示“设置边界条件”相关的操作界面或示例，后续审查通过后再补图。

> 图示要点：`Boundary_9.png` 展示“设置边界条件”相关的操作界面或示例，后续审查通过后再补图。

## 页内/相关链接

- - 默认边界条件: `#默认边界条件`
- - 默认边界条件 - 设置边界条件: `#设置边界条件`


## 待补图片清单
以下图片暂不插入正文，后续等人工审查后再从本机或官方帮助目录复制到知识库图片资源目录。
| 图片名称 | 当前资源路径 | 建议保留原因 |
| --- | --- | --- |
| Boundary_1.png | `wavEDA_docs/helpHtml/helpHtml/EM_Project/images/Boundary_1.png` | 展示与“默认边界条件”相关的关键界面，适合作为后续图文教程配图。 |
| Boundary_2.png | `wavEDA_docs/helpHtml/helpHtml/EM_Project/images/Boundary_2.png` | 展示与“默认边界条件”相关的关键界面，适合作为后续图文教程配图。 |
| Boundary_3.png | `wavEDA_docs/helpHtml/helpHtml/EM_Project/images/Boundary_3.png` | 展示“设置边界条件”步骤的菜单或参数界面，便于新人按界面完成操作。 |
| Boundary_4.png | `wavEDA_docs/helpHtml/helpHtml/EM_Project/images/Boundary_4.png` | 展示“设置边界条件”步骤的菜单或参数界面，便于新人按界面完成操作。 |
| Boundary_5.png | `wavEDA_docs/helpHtml/helpHtml/EM_Project/images/Boundary_5.png` | 展示“设置边界条件”步骤的菜单或参数界面，便于新人按界面完成操作。 |
| Boundary_6.png | `wavEDA_docs/helpHtml/helpHtml/EM_Project/images/Boundary_6.png` | 展示“设置边界条件”步骤的菜单或参数界面，便于新人按界面完成操作。 |
| Boundary_7.png | `wavEDA_docs/helpHtml/helpHtml/EM_Project/images/Boundary_7.png` | 展示“设置边界条件”步骤的菜单或参数界面，便于新人按界面完成操作。 |
| Boundary_8.png | `wavEDA_docs/helpHtml/helpHtml/EM_Project/images/Boundary_8.png` | 展示“设置边界条件”步骤的菜单或参数界面，便于新人按界面完成操作。 |
| Boundary_9.png | `wavEDA_docs/helpHtml/helpHtml/EM_Project/images/Boundary_9.png` | 展示“设置边界条件”步骤的菜单或参数界面，便于新人按界面完成操作。 |
