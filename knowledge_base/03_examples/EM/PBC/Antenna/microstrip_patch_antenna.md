---
title: "微带贴片天线"
merged_source: "current_waveda_agent_kb"
source_relative_path: "40_example_cases/EM/PBC/Antenna/microstrip_patch_antenna.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\40_example_cases\EM\PBC\Antenna\microstrip_patch_antenna.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 微带贴片天线

- 案例分类: `EM`
- 来源 HTML: `D:\Staid\app\waveda\Example\EM\PBC\Antenna\microstrip_patch_antenna.html`
- 工程文件: `D:\Staid\app\waveda\Example\EM\PBC\Antenna\microstrip_patch_antenna.tsp`
- 截图数量: 5

## 工程摘要

- 工程类型: `EM`
- WavEDA 版本: `2.0.7527.2126`
- 坐标类型: `3d`
- 单位: `{"freq": "GHz", "thermal": "K", "length": "mm", "time": "ns"}`
- 求解器: `{"method": "fault", "solver": "fem", "basic": "2", "ray-tube-type": "0", "basicsem": "2", "save-path": "0"}`
- 计算区域/Domain: `{"gap": "0", "gapType": "no-gap", "shape-type": "box"}`
- 变量数量: 0
- 材料: Air, PEC, sub
- 对象数量: face=4, solid=3, curve=0, lumped-port=1, wave-port=0, point-source=0, plane-wave=0, far-field=43
- XML 解析提示: `junk after document element: line 198, column 0`（已使用容错抽取）

### 频率/激励设置摘要

| physics | type | start | end | point | step | sweep_method | method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EM | freq-domain | 1.3 | 1.7 | 41 | 0.01 | 2 | 1 |
| MH | time-domain |  |  |  |  | 0 |  |
| TL | time-domain |  |  |  |  | 0 |  |
| LT | freq-domain | 1 | 1 | 1 | 1 | 0 | 0 |

## 案例教程抽取

## 微带贴片天线

- 模型描述 - 仿真设置 - 后处理

### 模型描述

本案例仿真微带贴片天线，工作频率在1.3-1.7 GHz之间，扫频方式选快速。集总面端口为激励。

本案例采用馈线和辐射元件位于接地板的两侧，接地板上开有缝隙，微带馈线穿过缝隙并延伸形成匹配枝节。 通过调整缝隙尺寸和匹配枝节的长度，优化输入阻抗以最小化S11。 接地板上方为薄导体贴片，作为辐射元件，与馈线通过缝隙耦合实现能量传输。下面显示了所得几何图形的图片。

> 图片: `./res/microstrip_patch_antenna_1.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\Antenna\res\microstrip_patch_antenna_1.png`

### 仿真设置

1. 计算域设置 本案例在Zmax方向上根据中心频率处波长求得计算区域离模型78 mm。建模空气盒子大小为91.3x91.3x78.4 mm³。

> 图片: `./res/microstrip_patch_antenna_3.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\Antenna\res\microstrip_patch_antenna_3.png`

2. 周期边界设置 在Zmax和Zmin方向上为一阶吸收边界，在Xmin、Xmax和Ymin、Ymanx方向都添加了周期边界。设置如图所示，本案例通过周期边界法通过简化无限周期结构的场分布条件，高效实现阵列天线的初步仿真。

> 图片: `./res/microstrip_patch_antenna_6.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\Antenna\res\microstrip_patch_antenna_6.png`

### 后处理

1. 3D网格 仿真完成后，选中关键部分物体，进入显示网格窗口查看网格剖分情况。

> 图片: `./res/microstrip_patch_antenna_7.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\Antenna\res\microstrip_patch_antenna_7.png`

2.S参数从S参数图可以看出本案例的天线性能，在1.5 GHz附近表现出优异的辐射特性（S11=−30 dB），-10 dB带宽覆盖16%，满足多数阵列单元天线设计指标。

> 图片: `./res/microstrip_patch_antenna_5.png`  
> 原始路径: `D:\Staid\app\waveda\Example\EM\PBC\Antenna\res\microstrip_patch_antenna_5.png`

## 图片资源

1. `./res/microstrip_patch_antenna_1.png` -> `D:\Staid\app\waveda\Example\EM\PBC\Antenna\res\microstrip_patch_antenna_1.png`
2. `./res/microstrip_patch_antenna_3.png` -> `D:\Staid\app\waveda\Example\EM\PBC\Antenna\res\microstrip_patch_antenna_3.png`
3. `./res/microstrip_patch_antenna_6.png` -> `D:\Staid\app\waveda\Example\EM\PBC\Antenna\res\microstrip_patch_antenna_6.png`
4. `./res/microstrip_patch_antenna_7.png` -> `D:\Staid\app\waveda\Example\EM\PBC\Antenna\res\microstrip_patch_antenna_7.png`
5. `./res/microstrip_patch_antenna_5.png` -> `D:\Staid\app\waveda\Example\EM\PBC\Antenna\res\microstrip_patch_antenna_5.png`
