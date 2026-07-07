---
title: "知识地图"
merged_source: "current_waveda_agent_kb"
source_relative_path: "20_indexes/knowledge_map.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\20_indexes\knowledge_map.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 知识地图

## 新手主线

1. **认识软件与文件入口**：新建、打开、保存工程，重置工程。 来源：[File/Homepage.md](../10_extracted_pages/File/Homepage.md)
2. **设置全局单位**：长度、时间、频率单位，工程内其他界面不要带额外单位。 来源：[Modeling/Design/Unit.md](../10_extracted_pages/Modeling/Design/Unit.md)
3. **设置背景与材料**：背景材料、普通材料/色散材料等。 来源：[Modeling/Bkg_Mat/Background.md](../10_extracted_pages/Modeling/Bkg_Mat/Background.md)
4. **设置计算区域**：空气盒子/Domain 会影响精度、效率和资源消耗。 来源：[Modeling/Design/Domain.md](../10_extracted_pages/Modeling/Design/Domain.md)
5. **建立几何模型**：创建体、面、线并通过模型编辑调整。 来源：[Modeling/Modeling.md](../10_extracted_pages/Modeling/Modeling.md)
6. **设置求解器与扫频**：MFEM、基函数阶数、离散/插值/快速扫频。 来源：[Modeling/Design/Solver.md](../10_extracted_pages/Modeling/Design/Solver.md)
7. **设置激励/端口**：波端口、集总端口、点源、平面波、多导体与积分线。 来源：[Modeling/Stimulate/Wave_Port.md](../10_extracted_pages/Modeling/Stimulate/Wave_Port.md)
8. **设置网格**：初始网格、局部加密、自适应网格、波端口网格。 来源：[Mesh/3D_Mesh.md](../10_extracted_pages/Mesh/3D_Mesh.md)
9. **验证并运行仿真**：验证、运行、停止、清除、运行波端口。 来源：[Simulation/Simulation.md](../10_extracted_pages/Simulation/Simulation.md)
10. **查看结果与导出**：端口结果、远场、快照、导出 Snp/图片。 来源：[EM_Project/EM_Results.md](../10_extracted_pages/EM_Project/EM_Results.md)

## Agent 问题类型到知识入口
- “按钮在哪/有什么用”：`button_location_function_index.md` + 对应抽取页图片资源。
- “怎么开始仿真”：`beginner_simulation_workflow.md`。
- “扫频方法怎么选”：`simulation_methods_comparison.md`。
- “端口怎么选/为什么建不了”：`ports_and_excitations.md` + 排错卡。
- “报错/验证不过”：`troubleshooting_and_constraints.md`，并让用户提供完整日志。
- “结果怎么看/怎么导出”：`post_processing_results.md`。
