---
title: "后处理与结果查看卡"
merged_source: "current_waveda_agent_kb"
source_relative_path: "30_topic_cards/post_processing_results.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\30_topic_cards\post_processing_results.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 后处理与结果查看卡

## 电磁结果入口

仿真结束后，可在工程树“电磁结果”中查看接收器、端口、快照和远场结果。

## 端口结果

- 右键端口结果可新建端口结果、新建史密斯圆图、导出 Snp、删除所有结果。
- 新建端口结果可查看 S 参数、差分对、Z 参数、TDR、TDT、电压、电流等；波端口还可查看 Y 参数、线阻抗和 Gamma。
- 可通过添加曲线选择单位并绘制目标端口结果。
- 来源：`10_extracted_pages/EM_Project/EM_Results.md`、`10_extracted_pages/Post_Processing/New_Port.md`

## 远场结果

- 仿真前需要进行远场设置。
- 仿真完成后可查看接收功率、辐射功率、辐射效率、总效率、单站 RCS、平均功率、轴比、轴比-频率曲线、远场 3D/2D/1D 增益图等。
- 平面波仿真可查看单站雷达散射截面曲线。
- 来源：`10_extracted_pages/EM_Project/Far_field.md`、`10_extracted_pages/EM_Project/EM_Results.md`

## 接收器结果

- 接收器仿真只能在离散或快速扫频下进行。
- 仿真完成后可以再新建接收器查看结果，但需要在工具栏“设计设置”中选择保存结果。
- 来源：`10_extracted_pages/Post_Processing/New_Observers.md`

## 导出

- 可导出图片和 Snp 文件。
- 图表设置中改变 X 轴范围只改变显示，导出数据时仍导出全范围 X 轴数据。
- 来源：`10_extracted_pages/Tool/Export_Figure.md`、`10_extracted_pages/Tool/Export_Snp.md`、`10_extracted_pages/Post_Processing/New_Port.md`
