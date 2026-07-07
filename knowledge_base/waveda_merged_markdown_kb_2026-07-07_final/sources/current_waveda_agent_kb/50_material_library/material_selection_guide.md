---
title: "材料选择指南"
merged_source: "current_waveda_agent_kb"
source_relative_path: "50_material_library/material_selection_guide.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\50_material_library\material_selection_guide.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 材料选择指南

## 使用方式

- 查材料是否存在：先看 `material_index.csv` 或 `materials.md`。
- 查电磁仿真参数：重点看 `em_type`、`epsilon_r`、`conductivity`、`mu_r`、`loss_tan`。
- 查热仿真参数：重点看 `thermal_rho`、`thermal_cp`、`thermal_kappa`。
- 查多物理场可用性：看 `modules` 是否包含 `EM`、`Thermal`、`Ela`、`Piezo`。

## 新手常见判断

- `PEC` 常用于理想金属导体。
- `Air` 常用于背景材料或空气盒子。
- `FR-4` 类材料常用于 PCB/微带天线基板，应关注介电常数和损耗角正切。
- 金属材料通常关注电导率；介质材料通常关注介电常数和损耗角正切。

## 排错提示

- 如果材料损耗没有生效，检查材料设置中损耗角正切选项是否启用。
- 如果多物理场结果异常，检查材料是否启用了对应物理模块。
- 如果材料名重复或导入失败，检查自定义材料名是否已存在。
