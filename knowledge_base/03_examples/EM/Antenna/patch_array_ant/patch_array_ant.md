---
title: "阵列贴片天线"
merged_source: "current_waveda_agent_kb"
source_relative_path: "40_example_cases/EM/Antenna/patch_array_ant/patch_array_ant.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\40_example_cases\EM\Antenna\patch_array_ant\patch_array_ant.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 阵列贴片天线

- 案例分类: `EM`
- 来源 HTML: `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\patch_array_ant.html`
- 工程文件: `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\patch_array_ant.tsp`
- 截图数量: 10

## 工程摘要

- 工程类型: `EM`
- WavEDA 版本: `2.1.7491.2100.    (Alpha)`
- 坐标类型: `3d`
- 单位: `{"time": "ns", "thermal": "K", "length": "mm", "freq": "GHz"}`
- 求解器: `{"max-iterations": "0", "solver": "fem", "number-of-intersection": "1", "save-path": "1", "method": "fault", "ray-tube-type": "0"}`
- 计算区域/Domain: `{"shape-type": "box", "gap-type": "user-ab", "gap": "15"}`
- 变量数量: 0
- 材料: Air, PEC, fr4
- 对象数量: face=14, solid=5, curve=0, lumped-port=4, wave-port=0, point-source=0, plane-wave=0, far-field=3
- XML 解析提示: `junk after document element: line 235, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | freq-domain | 4 | 5 | 101 | 0.01 | 1 | 2 |
| MH | time-domain |  |  |  |  | 0 |  |
| TL | time-domain |  |  |  |  | 0 |  |
| LT | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |

## 案例教程抽取

## 阵列贴片天线

- 模型描述 - 仿真设置 - 后处理 - 参考文献

### 模型描述

此模型为阵列贴片天线，馈电方式为集总面端口，与过孔和地平面相连接。仿真范围为4-6 GHz。对于天线模型，空气盒子至少偏离模型四分之一波长，若对仿真结果精度要求更高，可以适当增大空气盒子尺寸。

> 图片: `./res/patch_array_ant_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_1.png`

> 图片: `./res/patch_array_ant_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_2.png`

### 仿真设置

1. 网格划分 此模型采用自适应网格剖分，为了提高仿真精确度，对金属过孔和贴片进行局部加密。

> 图片: `./res/patch_array_ant_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_3.png`

2. 扫频设置 此模型结构相对简单，最高频率为6 GHz，快速算法迭代200次即可获得收敛结果。已知此阵列贴片天线模型的工作谐振点较少，结果曲线相对光滑，扫频点数设置为101。若模型复杂、仿真频率较高、结果曲线较为曲折需要增加迭代次数和扫频点数。

> 图片: `./res/patch_array_ant_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_4.png`

### 后处理

1. 网格剖分情况分析 查看网格时WavEDA支持以纵横比显示，如下图所示，大部分网格纵横比集中在2左右，纵横比越小网格剖分质量越好。

> 图片: `./res/patch_array_ant_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_5.png`

> 图片: `./res/patch_array_ant_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_6.png`

2. S参数 下图为4个端口的S参数结果，可以看出其工作谐振点在5 GHz左右。

> 图片: `./res/patch_array_ant_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_7.png`

3. 远场辐射 首先在远场-->编辑端口激励界面设置四个端口同时激励，下图展示了4个端口同时激励得到的三维远场辐射结果。

> 图片: `./res/patch_array_ant_8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_8.png`

> 图片: `./res/patch_array_ant_9.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_9.png`

> 图片: `./res/patch_array_ant_10.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_10.png`

### 参考文献

[1] Liu Y, Wang H, Li K, et al. RCS reduction of a patch array antenna based on microstrip resonators[J]. IEEE Antennas and Wireless Propagation Letters, 2014, 14: 4-7.

## 图片资源

1. `./res/patch_array_ant_1.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_1.png`
2. `./res/patch_array_ant_2.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_2.png`
3. `./res/patch_array_ant_3.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_3.png`
4. `./res/patch_array_ant_4.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_4.png`
5. `./res/patch_array_ant_5.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_5.png`
6. `./res/patch_array_ant_6.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_6.png`
7. `./res/patch_array_ant_7.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_7.png`
8. `./res/patch_array_ant_8.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_8.png`
9. `./res/patch_array_ant_9.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_9.png`
10. `./res/patch_array_ant_10.png` -> `D:\Staid\app\waveda\Example\EM\Antenna\patch_array_ant\res\patch_array_ant_10.png`
