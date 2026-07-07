---
title: "WavEDA"
merged_source: "current_waveda_agent_kb"
source_relative_path: "40_example_cases/Circuit/Filter/Filter/Filter.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\40_example_cases\Circuit\Filter\Filter\Filter.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# WavEDA

- 案例分类: `Circuit`
- 来源 HTML: `D:\Staid\app\waveda\Example\Circuit\Filter\Filter\Filter.html`
- 工程文件: `D:\Staid\app\waveda\Example\Circuit\Filter\Filter\Filter.tsp`
- 截图数量: 5

## 工程摘要

- 工程类型: `Circuit`
- WavEDA 版本: `1.3.6530.1784.    (Alpha)`
- 坐标类型: ``
- 单位: `{}`
- 求解器: `{}`
- 计算区域/Domain: `{}`
- 变量数量: 0
- 材料: 未抽取到
- 对象数量: face=0, solid=0, curve=0, lumped-port=0, wave-port=0, point-source=0, plane-wave=0, far-field=0

## 案例教程抽取

## WavEDA

## 二极管检波电路模型介绍

- 模型描述 - 仿真设置 - 后处理

### 模型描述

本模型为基于肖特基二极管的射频检波电路，工作频率为1 GHz。电路由正弦电压源（V1）、50 Ω限流/匹配电阻（R1）、二极管检波器（D1）和电压探针（Vprobe1）组成，构成典型的半波整流结构。

> 图片: `./res/filter1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Circuit\Filter\Filter\res\filter1.png`

### 仿真设置

采用瞬态分析（Tran1），仿真时间窗口为0-10 ns，覆盖10个完整信号周期。设置参数如下:

> 图片: `./res/filter5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Circuit\Filter\Filter\res\filter5.png`

正弦源幅度设为1 V，频率1 GHz。二极管使用实际器件模型（DiodeModel1），包含非线性结电容和串联电阻效应，模拟高频下的真实检波行为。点击仿真按键，软件将自动计算。

> 图片: `./res/filter2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Circuit\Filter\Filter\res\filter2.png`

仿真结束后，在页面内选中对应的结果参数，点击绘制。

> 图片: `./res/filter3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Circuit\Filter\Filter\res\filter3.png`

### 后处理

通过监测电压探针Vprobe1获得整流后的时域波形。仿真结果显示：输出为震荡波形，初始峰值1 V，反映电路的瞬态建立过程。该特性适用于射频场和脉冲信号测量等应用场景。

> 图片: `./res/filter4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\Circuit\Filter\Filter\res\filter4.png`

>

## 图片资源

1. `./res/filter1.png` -> `D:\Staid\app\waveda\Example\Circuit\Filter\Filter\res\filter1.png`
2. `./res/filter5.png` -> `D:\Staid\app\waveda\Example\Circuit\Filter\Filter\res\filter5.png`
3. `./res/filter2.png` -> `D:\Staid\app\waveda\Example\Circuit\Filter\Filter\res\filter2.png`
4. `./res/filter3.png` -> `D:\Staid\app\waveda\Example\Circuit\Filter\Filter\res\filter3.png`
5. `./res/filter4.png` -> `D:\Staid\app\waveda\Example\Circuit\Filter\Filter\res\filter4.png`
