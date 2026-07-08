---
title: "仿真方法对比卡"
merged_source: "current_waveda_agent_kb"
source_relative_path: "30_topic_cards/simulation_methods_comparison.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\30_topic_cards\simulation_methods_comparison.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 仿真方法对比卡

## 离散扫频

- 做法：利用当前网格剖分，逐点求解各频点电磁场。
- 优点：文档中说明为最准确的方法；适合关注各个频点场分布、频点数不多的情况。
- 缺点：速度较慢。
- 适用：结果有争议时可用离散方法复核；平面波源要求仿真方法仅限离散扫频。
- 来源：`10_extracted_pages/Modeling/Design/Frequency.md`、`10_extracted_pages/Modeling/Stimulate/Plane_Wave.md`

## 插值扫频

- 做法：在频率范围内由软件自动确定求解频点，再通过内插得到整个扫频范围响应。
- 关键参数：最大插值点数、插值误差。文档中默认最大插值点数为 250，默认插值误差为 1%。
- 收敛逻辑：满足插值误差或达到最大插值点数之一即结束；若达到最大插值点后误差仍大于目标，则结果不收敛。
- 注意：插值扫频频点由算法决定；应用插值扫频时，用户无法查看选定频点的 Snapshot。
- 来源：`10_extracted_pages/Modeling/Design/Frequency.md`

## 快速扫频

- 做法：基于降阶模型提升宽频带仿真速度。
- 优点：宽频带仿真建议优先采用。
- 关键参数：迭代次数表示降阶模型阶数，默认 100；一般越大越准确但更耗时。毫米波段建议 300，一般不要超过 500。
- 限制：平面波源目前不支持快速扫频。
- 来源：`10_extracted_pages/Modeling/Design/Frequency.md`

## 参数化扫描

- 做法：设置一个或多个设计参数的变化范围，软件自动生成一系列仿真任务。
- 前提：必须先在“变量”中添加变量；未设置变量的模型无法使用参数化扫描。
- 操作：仿真 -> 参数化扫描，选择变量、设置范围/步长/次数或任意点，添加到右侧并勾选后验证、开始。
- 默认参数选项：勾选“将默认参数设为一个参量”时，变量初始值会被加入扫描任务。
- 来源：`10_extracted_pages/Simulation/Parameter_Sweep.md`

## 自适应网格相关

- 自适应网格用于迭代改善网格和结果；详细日志中会显示迭代次数、残差、收敛数量、单元数、自由度和耗时。
- 残差越小，计算结果越接近真实值。
- 病态网格可通过显示网格定位，再在 3D 网格或自适应网格参数中调整。
- 来源：`10_extracted_pages/Tool/Details_logs.md`、`10_extracted_pages/Mesh/Show_Mesh.md`
