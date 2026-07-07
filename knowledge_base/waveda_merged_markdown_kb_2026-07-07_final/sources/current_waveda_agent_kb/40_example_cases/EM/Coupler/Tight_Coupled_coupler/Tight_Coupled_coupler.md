---
title: "紧耦合定向耦合器"
merged_source: "current_waveda_agent_kb"
source_relative_path: "40_example_cases/EM/Coupler/Tight_Coupled_coupler/Tight_Coupled_coupler.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\40_example_cases\EM\Coupler\Tight_Coupled_coupler\Tight_Coupled_coupler.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 紧耦合定向耦合器

- 案例分类: `EM`
- 来源 HTML: `D:\Staid\app\waveda\Example\EM\Coupler\Tight_Coupled_coupler\Tight_Coupled_coupler.html`
- 工程文件: `D:\Staid\app\waveda\Example\EM\Coupler\Tight_Coupled_coupler\Tight_Coupled_coupler.tsp`
- 截图数量: 7

## 工程摘要

- 工程类型: `EM`
- WavEDA 版本: `1.1.4005.1031.    (Alpha)`
- 坐标类型: `3d`
- 单位: `{"length": "mm", "time": "ns", "thermal": "K", "freq": "GHz"}`
- 求解器: `{"basic": "2", "solver": "fem", "method": "fault"}`
- 计算区域/Domain: `{"gap": "0", "gapType": "no-gap", "shape-type": "box"}`
- 变量数量: 0
- 材料: Air, PEC, copper, RO5430B
- 对象数量: face=7, solid=2, curve=0, lumped-port=4, wave-port=0, point-source=0, plane-wave=0, far-field=0
- XML 解析提示: `junk after document element: line 181, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | freq-domain | 1 | 3 | 101 | 0.02 | 1 | 1 |

## 案例教程抽取

## 紧耦合定向耦合器

- 模型描述 - 仿真设置 - 后处理 - 参考文献

### 模型描述

该模型属于对称宽带高指向性紧耦合定向耦合器。 该定向耦合器由两条简单的耦合线组成两条三折叠耦合线，满足了 宽带、紧密耦合和高方向性。

介质基板材料为FR4，介电常数为3.66，损耗角正切为0.0037。 耦合线与地等金属均采用PEC，如下图：

> 图片: `res/Tight_Coupled_coupler1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Coupler\Tight_Coupled_coupler\res\Tight_Coupled_coupler1.png`

### 仿真设置

1. 仿真频率及网格设置 该模型仿真频率设置为1~ 3 GHz，扫频方式选插值(离散/快速也适用), 具体设置如下图：

> 图片: `res/Tight_Coupled_coupler5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Coupler\Tight_Coupled_coupler\res\Tight_Coupled_coupler5.png`

2. 创建端口 采用集总面端口馈电，包括四个端口，如下图：

> 图片: `res/Tight_Coupled_coupler2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Coupler\Tight_Coupled_coupler\res\Tight_Coupled_coupler2.png`

3.网格剖分 采用了自适应网格设置，频率选择了中心频率，最大迭代次数为20，残差为0.02，如下图：

> 图片: `res/Tight_Coupled_coupler6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Coupler\Tight_Coupled_coupler\res\Tight_Coupled_coupler6.png`

### 后处理

1. 模型网格 仿真完成后，在模型窗口右键，进入View Mesh窗口网格剖分情况。

> 图片: `res/Tight_Coupled_coupler8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Coupler\Tight_Coupled_coupler\res\Tight_Coupled_coupler8.png`

> 图片: `res/Tight_Coupled_coupler7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Coupler\Tight_Coupled_coupler\res\Tight_Coupled_coupler7.png`

2.S参数结果 仿真后可以在电磁结果端口中通过获取S参数，以查看该耦合器性能。 如下图：

> 图片: `res/Tight_Coupled_coupler4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Coupler\Tight_Coupled_coupler\res\Tight_Coupled_coupler4.png`

由以上S参数结果可见：回波损耗（|S11|）和隔离度（|S41|）均高于 20分贝，表明该耦合器具有较高的方向性与隔离度。

### 参考文献

[1] L. Pan, Y. Wu, W. Wang, Y. Zheng and Y. Liu, "A Symmetrical Broadband Tight-Coupled Directional Coupler With High Directivity Using Three-Folded-Coupled Lines," in IEEE Transactions on Circuits and Systems II: Express Briefs, vol. 69, no. 9, pp. 3744-3748, Sept. 2022, doi: 10.1109/TCSII.2022.3169160.

## 图片资源

1. `res/Tight_Coupled_coupler1.png` -> `D:\Staid\app\waveda\Example\EM\Coupler\Tight_Coupled_coupler\res\Tight_Coupled_coupler1.png`
2. `res/Tight_Coupled_coupler5.png` -> `D:\Staid\app\waveda\Example\EM\Coupler\Tight_Coupled_coupler\res\Tight_Coupled_coupler5.png`
3. `res/Tight_Coupled_coupler2.png` -> `D:\Staid\app\waveda\Example\EM\Coupler\Tight_Coupled_coupler\res\Tight_Coupled_coupler2.png`
4. `res/Tight_Coupled_coupler6.png` -> `D:\Staid\app\waveda\Example\EM\Coupler\Tight_Coupled_coupler\res\Tight_Coupled_coupler6.png`
5. `res/Tight_Coupled_coupler8.png` -> `D:\Staid\app\waveda\Example\EM\Coupler\Tight_Coupled_coupler\res\Tight_Coupled_coupler8.png`
6. `res/Tight_Coupled_coupler7.png` -> `D:\Staid\app\waveda\Example\EM\Coupler\Tight_Coupled_coupler\res\Tight_Coupled_coupler7.png`
7. `res/Tight_Coupled_coupler4.png` -> `D:\Staid\app\waveda\Example\EM\Coupler\Tight_Coupled_coupler\res\Tight_Coupled_coupler4.png`
