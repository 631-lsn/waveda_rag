---
title: "三频带功分器"
merged_source: "current_waveda_agent_kb"
source_relative_path: "40_example_cases/EM/Divider/triband_power_divider/triband_power_divider.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\40_example_cases\EM\Divider\triband_power_divider\triband_power_divider.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 三频带功分器

- 案例分类: `EM`
- 来源 HTML: `D:\Staid\app\waveda\Example\EM\Divider\triband_power_divider\triband_power_divider.html`
- 工程文件: `D:\Staid\app\waveda\Example\EM\Divider\triband_power_divider\triband_power_divider.tsp`
- 截图数量: 5

## 工程摘要

- 工程类型: `EM`
- WavEDA 版本: `2.0.7527.2126`
- 坐标类型: `3d`
- 单位: `{"freq": "GHz", "thermal": "K", "length": "mm", "time": "ns"}`
- 求解器: `{"method": "fault", "solver": "fem", "basic": "2", "ray-tube-type": "0", "basicsem": "2", "save-path": "0"}`
- 计算区域/Domain: `{"gap": "-1", "gapType": "auto-gap", "shape-type": "solid"}`
- 变量数量: 13
- 材料: Air, PEC, FR4
- 对象数量: face=9, solid=2, curve=0, lumped-port=3, wave-port=0, point-source=0, plane-wave=0, far-field=0

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | freq-domain | 0.05 | 4.5 | 150 | 0.03 | 1 | 1 |
| MH | time-domain |  |  |  |  | 0 |  |
| TL | time-domain |  |  |  |  | 0 |  |
| LT | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |

### 变量摘要

| 变量 | 表达式 |
| --- | --- |
| L1 | 19.5 |
| L2 | 31 |
| Ls | 17.2 |
| W1 | 1 |
| s | 0.4 |
| Ws | 0.7 |
| W2 | 0.7 |
| d | 2 |
| Lm | 15.3 |
| wf | 3.43 |
| lf | 5 |
| h | 1.6 |
| N | 2*l2/7+lf |

## 案例教程抽取

## 三频带功分器

- 模型描述 - 仿真设置 - 后处理

### 模型描述

基于耦合线结构的小型化三频带滤波功率分配器， 该结构将滤波功能集成与功分器， 通过耦合线频率实现多频带响应。 功分器工作于sub-6GHz频段，带宽分别为：20.0%（1.1–1.35 GHz）、37.0%（2.0–2.9 GHz）、15.0%（3.25–3.8 GHz）。

整体模型尺寸为 35*32*1.6 mm，基底的介电常数为FR-4（介电常数为4.4，损耗角正切为0.02），微带线和接地板为PEC，边界条件为一阶吸收边界。

> 图片: `./res/triband_power_divider_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Divider\triband_power_divider\res\triband_power_divider_1.png`

### 仿真设置

1. 仿真频率 该模型使用集总面端口馈电。扫频范围在0.05 - 4.5 GHz，扫频方式选离散（插值/快速也适用）。 具体设置如下图：

> 图片: `./res/triband_power_divider_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Divider\triband_power_divider\res\triband_power_divider_6.png`

2. 创建端口 三个端口均采用集总面端口，WavEDA支持自动创建积分线并识别端口面的方向，进入集总端口设置界面后可以点击预览查看，同时也可以对积分线方向反向。本案例中端口方向均从微带线指向金属地。

> 图片: `./res/triband_power_divider_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Divider\triband_power_divider\res\triband_power_divider_2.png`

### 后处理

1. 网格查看 网格剖分完成后，选中目标体或面，进入View Mesh窗口网格剖分情况。

> 图片: `./res/triband_power_divider_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Divider\triband_power_divider\res\triband_power_divider_3.png`

2. 仿真结果 仿真完成后，可以查看S参数结果，可以看到仿真结果符合功分器的效果，输入反射功率仅1.1%，匹配良好。插入损耗0.2 dB，接近理想均分。输出间泄漏功率约1.6%，满足多数WLAN系统需求。 如下图：

> 图片: `./res/triband_power_divider_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Divider\triband_power_divider\res\triband_power_divider_5.png`

### 参考文献

[1] D. K. Choudhary, N. Mishra, P. K. Singh and A. Sharma, "Miniaturized Power Divider With Triple-Band Filtering Response Using Coupled Line," in IEEE Access, vol. 11, pp. 27602-27608, 2023, doi: 10.1109/ACCESS.2023.3257985.

## 图片资源

1. `./res/triband_power_divider_1.png` -> `D:\Staid\app\waveda\Example\EM\Divider\triband_power_divider\res\triband_power_divider_1.png`
2. `./res/triband_power_divider_6.png` -> `D:\Staid\app\waveda\Example\EM\Divider\triband_power_divider\res\triband_power_divider_6.png`
3. `./res/triband_power_divider_2.png` -> `D:\Staid\app\waveda\Example\EM\Divider\triband_power_divider\res\triband_power_divider_2.png`
4. `./res/triband_power_divider_3.png` -> `D:\Staid\app\waveda\Example\EM\Divider\triband_power_divider\res\triband_power_divider_3.png`
5. `./res/triband_power_divider_5.png` -> `D:\Staid\app\waveda\Example\EM\Divider\triband_power_divider\res\triband_power_divider_5.png`
