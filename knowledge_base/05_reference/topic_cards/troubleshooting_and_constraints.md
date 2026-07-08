---
title: "排错与约束卡"
merged_source: "current_waveda_agent_kb"
source_relative_path: "30_topic_cards/troubleshooting_and_constraints.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\30_topic_cards\troubleshooting_and_constraints.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 排错与约束卡

## 先看哪里

- “仿真 -> 验证”后，下方日志会给出报错或警告，优先按日志提示检查模型设置。
- “工具 -> 详细日志”可查看网格密度、自由度、仿真时间、自适应网格迭代、残差、收敛数量和每个物体的网格数量。
- “网格 -> 显示网格 -> 病态”可定位网格质量较差区域，再做局部加密或调整自适应网格参数。

## 常见问题到检查项

| 现象/问题 | 优先检查 | 相关来源 |
|---|---|---|
| 参数化扫描无法使用 | 是否已在“变量”中添加变量 | `Simulation/Parameter_Sweep.md` |
| 平面波无法仿真或验证失败 | 背景材料是否普通材料、边界是否开放、扫频是否离散 | `Modeling/Stimulate/Plane_Wave.md` |
| 波端口建不了/结果异常 | 端口面是否非金属、是否贴在 Domain 上、名称是否为数字 | `Modeling/Stimulate/Wave_Port.md` |
| 集总面端口建不了 | 面是否为圆环面或矩形面，是否上下边接触金属，是否穿过金属截面 | `Modeling/Stimulate/Lumped_Port.md` |
| 集总线端口异常 | 路径是否完全位于模型外边界/空气盒子上 | `Modeling/Stimulate/Lumped_Port.md` |
| 网格数量爆炸/仿真很慢 | 局部网格尺寸是否设置过小，扫频点数是否过多，基函数阶数是否过高 | `Mesh/3D_Mesh.md`、`Modeling/Design/Frequency.md`、`Modeling/Design/Solver.md` |
| 结果不收敛 | 插值误差目标是否过小、最大插值点数是否不足、病态网格是否较多 | `Modeling/Design/Frequency.md`、`Mesh/Show_Mesh.md` |
| 停止仿真很慢 | 文档说明有些模型停止时间较长，可看日志右下角进度条 | `Simulation/Simulation.md` |
| 变量定义失败/冲突 | 变量名不区分大小写，`pi`、`e`、`t`、`t1`、`t2` 已被软件定义，不能再次定义 | `Tool/Variables.md` |
| 单位输入异常 | 单位在“单位”界面全局设置，其他界面编辑时不能带额外单位 | `Modeling/Design/Unit.md` |

## 第一版缺口

原始帮助文档没有提供完整“错误码/报错文本 -> 原因 -> 解决方案”表。后续建议把真实日志按模板补充到 `90_maintenance_templates/error_case_template.md`，形成 `40_error_cases/`。

更多自动抽取的限制语句见：`20_indexes/constraint_warning_index.md`。
