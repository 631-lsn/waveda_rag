---
title: "孔隙介质"
merged_source: "current_waveda_agent_kb"
source_relative_path: "40_example_cases/EM/geological exploration/porous_medium/porosity_medium.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\40_example_cases\EM\geological exploration\porous_medium\porosity_medium.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 孔隙介质

- 案例分类: `EM`
- 来源 HTML: `D:\Staid\app\waveda\Example\EM\geological exploration\porous_medium\porosity_medium.html`
- 工程文件: `D:\Staid\app\waveda\Example\EM\geological exploration\porous_medium\porosity_medium.tsp`
- 截图数量: 6

## 工程摘要

- 工程类型: `EM`
- WavEDA 版本: `1.1.3985.1031.    (Alpha)`
- 坐标类型: `3d`
- 单位: `{"time": "ns", "thermal": "K", "length": "mm", "freq": "GHz"}`
- 求解器: `{"basic": "2", "method": "fault", "solver": "fem"}`
- 计算区域/Domain: `{"gap": "0", "shape-type": "solid", "gapType": "auto-gap"}`
- 变量数量: 0
- 材料: Air, PEC, rock, water, pmc
- 对象数量: face=0, solid=18, curve=0, lumped-port=0, wave-port=0, point-source=0, plane-wave=0, far-field=0
- XML 解析提示: `junk after document element: line 199, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | freq-domain | 1e-4 | 1 | 1 | 0.0499995 | 0 | 0 |

## 案例教程抽取

## 孔隙介质

- 模型描述 - 仿真设置 - 后处理

### 模型描述

此模型为空孔隙介质模型，其中大小不一的球形孔隙被水和空气填充，其他介质为岩石。模型尺寸为800*800*400 mm³，仿真频点为10 MHz。

> 图示要点：此处原图对应当前段落的关键步骤或结果，后续审查通过后再补图。

### 仿真设置

1. 创建点源 激励形式采用电偶极子源，如下图所示红色圆点为电偶极子源。

> 图示要点：此处原图对应当前段落的关键步骤或结果，后续审查通过后再补图。

2. 创建接收器 如下图所示，红色直线为接收器。需要注意的是接收器不可放置在介质分层处、物体的边缘或过于靠近其他激励源，这些情况都会引起奇异值。

> 图示要点：此处原图对应当前段落的关键步骤或结果，后续审查通过后再补图。

### 后处理

仿真结束后，可以在电磁结果-->接收器查看线接收器处的近场分布。在创建接收器结果界面需要选择激励模型、类型和频率点。

> 图示要点：此处原图对应当前段落的关键步骤或结果，后续审查通过后再补图。

如下图所示，分别是线接收器在x、y、z三个方向上的电\磁场的实虚部分量。

> 图示要点：此处原图对应当前段落的关键步骤或结果，后续审查通过后再补图。

## 待补图片清单

| 文件名 | WavEDA 相对路径 | 用途 |
| --- | --- | --- |
| porous_medium_1.png | `Example/EM/geological exploration/porous_medium/res/porous_medium_1.png` | 展示该案例中的关键模型、设置或结果，后续审查后决定是否补图。 |
| porous_medium_2.png | `Example/EM/geological exploration/porous_medium/res/porous_medium_2.png` | 展示该案例中的关键模型、设置或结果，后续审查后决定是否补图。 |
| porous_medium_4.png | `Example/EM/geological exploration/porous_medium/res/porous_medium_4.png` | 展示该案例中的关键模型、设置或结果，后续审查后决定是否补图。 |
| porous_medium_5.png | `Example/EM/geological exploration/porous_medium/res/porous_medium_5.png` | 展示该案例中的关键模型、设置或结果，后续审查后决定是否补图。 |
