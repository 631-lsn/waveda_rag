---
title: "LC低通滤波器"
merged_source: "current_waveda_agent_kb"
source_relative_path: "40_example_cases/Circuit/LC_LPF/LC_LPF/LC_LPF.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\40_example_cases\Circuit\LC_LPF\LC_LPF\LC_LPF.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# LC低通滤波器

- 案例分类: `Circuit`
- 来源 HTML: `D:\Staid\app\waveda\Example\Circuit\LC_LPF\LC_LPF\LC_LPF.html`
- 工程文件: `D:\Staid\app\waveda\Example\Circuit\LC_LPF\LC_LPF\LC_LPF.tsp`
- 截图数量: 5

## 工程摘要

- 工程类型: `Circuit`
- WavEDA 版本: `1.3.6227.1686.    (Alpha)`
- 坐标类型: ``
- 单位: `{}`
- 求解器: `{}`
- 计算区域/Domain: `{}`
- 变量数量: 0
- 材料: 未抽取到
- 对象数量: face=0, solid=0, curve=0, lumped-port=0, wave-port=0, point-source=0, plane-wave=0, far-field=0

## 案例教程抽取

## LC低通滤波器

- 模型描述 - 仿真设置 - 后处理

### 模型描述

LC低通滤波器主要有LC器件组成，两端接有端口以进行S参数查看，放置SP控件仿真0.1-10 GHz的S参数，为增加高频抑制效果，通过并联谐振网络，结合WavEDA的电路调谐功能实时查看S参数结果，达到目标。电路示意图如下图所示：

> 图片: `./res/LC_LPF_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Circuit\LC_LPF\LC_LPF\res\LC_LPF_1.png`

### 仿真设置

1. 仿真控件设置 该电路模型仿真S参数，设置SP控件，类型为Linear，仿真范围为0.1-10 GHz，点数为401。具体设置如下图：

> 图片: `./res/LC_LPF_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Circuit\LC_LPF\LC_LPF\res\LC_LPF_2.png`

2. 变量设置 选择变量控件，添加变量C5、C6、C7，并设置C5=1、C6=0.5、C7=0.2，具体设置如下图：

> 图片: `./res/LC_LPF_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Circuit\LC_LPF\LC_LPF\res\LC_LPF_3.png`

3. 参数化扫描设置 选择工具->参数化扫描，进入窗口后分别设置C5、C6、C7的变量范围为起始0.1，终止1.5，步长0.1；并启用变量扫描功能。

> 图片: `./res/LC_LPF_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Circuit\LC_LPF\LC_LPF\res\LC_LPF_4.png`

### 后处理

调谐调试S参数 电路创建完毕后，点击仿真->调谐后，弹出结果与调谐窗口，首先在结果窗口创建S参数，选择S11和S21创建结果；通过调谐窗口选择滑块移动改变C5、C6、C7的值实时查看S参数结果，以达到目标需求。

> 图片: `./res/LC_LPF_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Circuit\LC_LPF\LC_LPF\res\LC_LPF_5.png`

## 图片资源

1. `./res/LC_LPF_1.png` -> `D:\Staid\app\waveda\Example\Circuit\LC_LPF\LC_LPF\res\LC_LPF_1.png`
2. `./res/LC_LPF_2.png` -> `D:\Staid\app\waveda\Example\Circuit\LC_LPF\LC_LPF\res\LC_LPF_2.png`
3. `./res/LC_LPF_3.png` -> `D:\Staid\app\waveda\Example\Circuit\LC_LPF\LC_LPF\res\LC_LPF_3.png`
4. `./res/LC_LPF_4.png` -> `D:\Staid\app\waveda\Example\Circuit\LC_LPF\LC_LPF\res\LC_LPF_4.png`
5. `./res/LC_LPF_5.png` -> `D:\Staid\app\waveda\Example\Circuit\LC_LPF\LC_LPF\res\LC_LPF_5.png`
