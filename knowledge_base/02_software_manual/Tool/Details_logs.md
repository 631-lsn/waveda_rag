---
title: "详细日志"
merged_source: "current_waveda_agent_kb"
source_relative_path: "10_extracted_pages/Tool/Details_logs.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\10_extracted_pages\Tool\Details_logs.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 详细日志

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Tool\Details_logs.html`
- 原始相对路径: `Tool/Details_logs.html`
- 知识模块: `工具`

## 正文抽取
## 详细日志

- 详细信息 - 网格 - 网格数量

这里主要展示模型仿真过程中的详细日志与网格信息。

### 详细信息

主要显示模型仿真过程中的网格密度，自由度，仿真时间等信息，如下图：

- 电磁求解器：是否采用了自适应网格；

- 节点数量；

- 网格数量；

- 网格最大值和最小值大小（网格尺寸）；

- 采样率最大值和最小值；

- 自由度数量；

- 方程右侧；

- 仿真时间（包括仿真起始、终止、网格剖分、求解过程等时间）；

> 图片: `images/Details_logs1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Tool\images\Details_logs1.png`

### 网格

主要显示模型采用自适应网格仿真过程中的每次迭代情况， 具体包括：

- 迭代次数：包含实际值（实际迭代次数）、最大值、最小值；

- 迭代残差：目标值、当前值(迭代残差用来判断迭代是否收敛。迭代残差越小，说明计算结果越接近真实值。）；

- 数据设置：可以选择表格形式，或者图表形式，窗口右侧具体展示表格或者图表，其中表格中详细展示了包括迭代次数、误差、单元数、自由度、网格剖分时间、仿真时间、总时间；

- 收敛数量：目标值、当前值；

如下图：

> 图片: `images/Details_logs2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Tool\images\Details_logs2.png`

### 网格数量

主要显示模型中参与网格剖分的各个物体对应的网格数量情况；

图中左边显示物体名称，右边显示对应的网格数量，如下图：

> 图片: `images/Details_logs3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Tool\images\Details_logs3.png`

## 图片资源

1. `images/Details_logs1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Tool\images\Details_logs1.png`
2. `images/Details_logs2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Tool\images\Details_logs2.png`
3. `images/Details_logs3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Tool\images\Details_logs3.png`

## 页内/相关链接

- - 详细信息: `#详细信息`
- - 详细信息 - 网格: `#网格`
- - 详细信息 - 网格 - 网格数量: `#网格数量`
