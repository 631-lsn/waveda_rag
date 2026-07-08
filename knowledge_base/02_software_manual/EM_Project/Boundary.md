---
title: "边界"
merged_source: "current_waveda_agent_kb"
source_relative_path: "10_extracted_pages/EM_Project/Boundary.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\10_extracted_pages\EM_Project\Boundary.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 边界

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\Boundary.html`
- 原始相对路径: `EM_Project/Boundary.html`
- 知识模块: `EM设计与结果`

## 正文抽取
## 边界

- 默认边界条件 - 设置边界条件

### 默认边界条件

默认边界条件选项可进行计算区域边界条件的设置。

> 图片: `./images/Boundary_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Boundary_1.png`

> 图片: `./images/Boundary_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Boundary_2.png`

- 开放边界：分为一阶吸收边界ABC边界和完美匹配层PML边界，适用于天线辐射问题，但其吸收性能与入射角和距离有关，计算天线等强辐射问题时，距离辐射体应至少四分之一波长。 有关完美匹配层PML设置如下图所示： 图中，单元表示PML往外扩展多少个单元，多项式表示PML 多项式系数，衰减因子表示PML衰减系数，伸缩因子表示PML空间坐标伸缩系数。

- 理想电导体边界：即PEC边界，电场垂直于平面。

- 理想磁导体边界：即PMC边界，电场平行于平面，磁场垂直于平面。

### 设置边界条件

边界条件还可根据模型或自定义面进行不同方向上不同边界条件的设置，右击工程树下的边界选项，可进入边界条件设置界面。

> 图片: `./images/Boundary_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Boundary_3.png`

- 辐射ABC边界：点击辐射边界，可进入辐射边界设置界面，选择一个或多个方向或点击自定义面选择面进行辐射边界设置，同时还可在建模窗口选择要设置的面， 鼠标右键设置ABC边界条件。

> 图片: `./images/Boundary_4.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Boundary_4.png`

- 完美匹配层PML边界：点击PML边界，可进入PML边界设置界面，选择一个或多个方向进行PML边界设置，有关高级设置在上一章节已经介绍。

> 图片: `./images/Boundary_5.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Boundary_5.png`

- 完美电导体PEC边界：其设置与ABC边界类似。

> 图片: `./images/Boundary_6.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Boundary_6.png`

- 完美磁导体PMC边界：其设置与ABC边界类似。

> 图片: `./images/Boundary_7.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Boundary_7.png`

- 阻抗边界：其设置与ABC边界类似。通常用于近似描述某些物理介质（如金属表面、导电层、或者具有特定电磁响应的材料表面）的边界。

> 图片: `./images/Boundary_8.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Boundary_8.png`

> 图片: `./images/Boundary_9.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Boundary_9.png`

## 图片资源

1. `./images/Boundary_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Boundary_1.png`
2. `./images/Boundary_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Boundary_2.png`
3. `./images/Boundary_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Boundary_3.png`
4. `./images/Boundary_4.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Boundary_4.png`
5. `./images/Boundary_5.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Boundary_5.png`
6. `./images/Boundary_6.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Boundary_6.png`
7. `./images/Boundary_7.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Boundary_7.png`
8. `./images/Boundary_8.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Boundary_8.png`
9. `./images/Boundary_9.png` -> `D:\Staid\app\waveda\documentation\helpHtml\EM_Project\images\Boundary_9.png`

## 页内/相关链接

- - 默认边界条件: `#默认边界条件`
- - 默认边界条件 - 设置边界条件: `#设置边界条件`
