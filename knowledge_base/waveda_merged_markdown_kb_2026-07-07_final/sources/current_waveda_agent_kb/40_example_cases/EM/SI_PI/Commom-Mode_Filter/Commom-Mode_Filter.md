---
title: "蘑菇形共模低通滤波器"
merged_source: "current_waveda_agent_kb"
source_relative_path: "40_example_cases/EM/SI_PI/Commom-Mode_Filter/Commom-Mode_Filter.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\40_example_cases\EM\SI_PI\Commom-Mode_Filter\Commom-Mode_Filter.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 蘑菇形共模低通滤波器

- 案例分类: `EM`
- 来源 HTML: `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\Commom-Mode_Filter.html`
- 工程文件: `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\Commom-Mode_Filter.tsp`
- 截图数量: 9

## 工程摘要

- 工程类型: `EM`
- WavEDA 版本: `2.0.7527.2126`
- 坐标类型: `3d`
- 单位: `{"freq": "GHz", "thermal": "K", "length": "mm", "time": "ns"}`
- 求解器: `{"method": "fault", "solver": "fem", "basic": "2", "ray-tube-type": "0", "basicsem": "2", "save-path": "0"}`
- 计算区域/Domain: `{"gap": "4", "gapType": "user-define-gap", "shape-type": "box"}`
- 变量数量: 23
- 材料: Air, PEC, Copper, RO4003
- 对象数量: face=4, solid=40, curve=0, lumped-port=4, wave-port=0, point-source=0, plane-wave=0, far-field=0

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | freq-domain | 0.1 | 4.5 | 221 | 0.02 | 1 | 1 |
| MH | time-domain |  |  |  |  | 0 |  |
| TL | time-domain |  |  |  |  | 0 |  |
| LT | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |

### 变量摘要

| 变量 | 表达式 |
| --- | --- |
| gndx | 20 |
| gndy | 10 |
| gndh | 0.1 |
| die_h1 | 60*0.0254 |
| die_h2 | 8*0.0254 |
| sig_h | 0.1 |
| l1 | 3.9 |
| g | 0.1 |
| tl_x | 3.9 |
| s1 | 0.2 |
| w1 | 0.15 |
| patch_h | 0.1 |
| w2 | 0.75 |
| s2 | 0.15 |
| patch_w | s1+2*(w1+w2+s2) |
| d | 0.1 |
| s3 | s2/2 |
| p | 2.8 |
| w3 | 0.5 |
| w4 | 0.2 |
| w5 | (w3-w4)/2 |
| l2 | 0.5 |
| r2 | (l2-0.1)/2 |

## 案例教程抽取

## 蘑菇形共模低通滤波器

- 模型描述 - 仿真设置 - 后处理 - 参考文献

### 模型描述

采用耦合线和蘑菇谐振器的小型化共模低通滤波器，设置0.1-4.5 GHz频率范围仿真，查看共模S参数结果，模型示意图如下图所示。

> 图片: `./res/Commom-Mode_Filter_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\res\Commom-Mode_Filter_1.png`

该模型为4个蘑菇形单元组成，介质基板材料为RO4003C，厚度为68 mil。对于内部制造，采用双层平版蚀刻工艺，贴片嵌入到介质内部， 差分线在基板上方，边界条件为ABC。

### 仿真设置

1. 仿真频率及网格设置 该模型仿真频率设置为0.1-4.5 GHz，扫频方式选择插值(离散/快速也适用)。 设置网格采样率为3 PPW，采用自适应网格进行剖分，自适应网格频率设置为2.5 GHz，残差设置为WavEDA默认值0.01，具体设置如下图：

> 图片: `./res/Commom-Mode_Filter_2.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\res\Commom-Mode_Filter_2.png`

> 图片: `./res/Commom-Mode_Filter_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\res\Commom-Mode_Filter_3.png`

2. 创建端口 模型激励采用面集总端口馈电，如下图所示：

> 图片: `./res/Commom-Mode_Filter_4.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\res\Commom-Mode_Filter_4.png`

3. 差分对设置 对四个端口设置两组差分对，注意差分对结果属于后处理结果，可在仿真完成后再进行差分对设置，具体设置如下图所示：

> 图片: `./res/Commom-Mode_Filter_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\res\Commom-Mode_Filter_5.png`

> 图片: `./res/Commom-Mode_Filter_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\res\Commom-Mode_Filter_6.png`

### 后处理

1. 3D网格 仿真完成后，选中关键部分物体，进入查看网格窗口查看网格剖分情况。

> 图片: `./res/Commom-Mode_Filter_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\res\Commom-Mode_Filter_7.png`

2. 共模S参数结果 端口结果可从工程树端口处访问，添加S(Comm1，Comm1)、S(Comm2，Comm1)结果查看共模滤波器性能。

> 图片: `./res/Commom-Mode_Filter_8.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\res\Commom-Mode_Filter_8.png`

> 图片: `./res/Commom-Mode_Filter_9.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\res\Commom-Mode_Filter_9.png`

### 参考文献

[1] B. -F. Su and T. -G. Ma, "Miniaturized Common-Mode Filter Using Coupled Synthesized Lines and Mushroom Resonators for High-Speed Differential Signals," in IEEE Microwave and Wireless Components Letters, vol. 25, no. 2, pp. 112-114, Feb. 2015, doi: 10.1109/LMWC.2014.2382650.

## 图片资源

1. `./res/Commom-Mode_Filter_1.png` -> `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\res\Commom-Mode_Filter_1.png`
2. `./res/Commom-Mode_Filter_2.png` -> `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\res\Commom-Mode_Filter_2.png`
3. `./res/Commom-Mode_Filter_3.png` -> `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\res\Commom-Mode_Filter_3.png`
4. `./res/Commom-Mode_Filter_4.png` -> `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\res\Commom-Mode_Filter_4.png`
5. `./res/Commom-Mode_Filter_5.png` -> `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\res\Commom-Mode_Filter_5.png`
6. `./res/Commom-Mode_Filter_6.png` -> `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\res\Commom-Mode_Filter_6.png`
7. `./res/Commom-Mode_Filter_7.png` -> `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\res\Commom-Mode_Filter_7.png`
8. `./res/Commom-Mode_Filter_8.png` -> `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\res\Commom-Mode_Filter_8.png`
9. `./res/Commom-Mode_Filter_9.png` -> `D:\Staid\app\waveda\Example\EM\SI_PI\Commom-Mode_Filter\res\Commom-Mode_Filter_9.png`
