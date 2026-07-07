---
title: "端口与激励选择卡"
merged_source: "current_waveda_agent_kb"
source_relative_path: "30_topic_cards/ports_and_excitations.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\30_topic_cards\ports_and_excitations.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 端口与激励选择卡

## 波端口

- 用于模拟从端口进入或离开的电磁波模式。
- 波端口面的材料需为非金属。
- 当前文档说明只支持贴在 Domain 上的波端口，不支持不在 Domain 上的波端口。
- 端口名称只能为数字。
- 多导体终端形式的波端口必须选择一个导体作为参考导体，通常选共地导体。
- 来源：`10_extracted_pages/Modeling/Stimulate/Wave_Port.md`、`10_extracted_pages/Modeling/Stimulate/Multi_Conductors.md`

## 集总端口

- 用于模拟信号进入或离开设备的内部表面，常用于激励设备和测量 S 参数。
- 分为集总面端口和集总线端口。
- 集总面端口当前仅支持在圆环面和矩形面上建立，所在面材料由软件默认为空气，用户无法设置。
- 集总面端口仅支持上下边接触金属结构，不可经过金属体截面。
- 可使用集总面端口时建议优先使用；无法建立面端口时再考虑集总线端口。
- 集总线端口路径不可完全位于模型外边界，不可完全贴着空气盒子。
- 端口阻抗必须是大于零的实数，默认 50 Ω。
- 来源：`10_extracted_pages/Modeling/Stimulate/Lumped_Port.md`

## 点激励源

- 适合模拟从单点或局部位置发射的电磁波。
- 与波端口、集总面端口、平面波不同，通常用于难以用面激励表达的复杂结构。
- WavEDA 仅支持快速扫频和离散扫频时添加点激励源进行计算。
- 点源形式包括电偶极子和磁偶极子。
- 来源：`10_extracted_pages/Modeling/Stimulate/Create_Point_Source.md`

## 平面波

- 用于模拟来自远处的外部电磁波入射。
- 必须满足：背景材料为普通材料而不是导电材料；边界条件为开放边界；仿真方法仅限离散扫频。
- 传播方向不可输入 `(0,0,0)`。
- 频域仿真时参考频率不可填写。
- 椭圆极化用长半轴/短半轴电场定义时，长半轴电场必须大于短半轴电场。
- 来源：`10_extracted_pages/Modeling/Stimulate/Plane_Wave.md`
