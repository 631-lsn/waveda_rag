---
title: "直接修改 WavEDA TSP 工程文件（实验性）"
content_kind: "reference"
physics_domain: "common"
waveda_module: "Automation"
software_version: "不同工程和版本的 XML 结构可能不同"
priority: 1
status: "draft"
indexing: true
updated_at: "2026-07-23"
---

# 直接修改 WavEDA TSP 工程文件（实验性）

## 风险声明

`.tsp` 在部分工程中可作为 XML 读取，但这不代表可以用一套固定 XPath 安全修改所有工程。变量、频扫、端口、观察器、计算域和结果节点会随物理场、工程类型和 WavEDA 版本变化。

Agent 默认只读检查 `.tsp`，默认通过运行 XML 的 `modify var` 改基础变量。

## 可以安全借鉴的部分

- 只读解析变量、单位、频扫、端口、网格和结果节点。
- 对源工程计算哈希并保留原文件。
- 生成新工程文件，不覆盖唯一原件。
- 修改后先在 GUI 加载和单点仿真。

## 不可直接通用化的假设

- 频域扫描不一定使用 `max-freq/min-freq/freq`；已见工程使用 `start/end/step/point`。
- 波端口与集总端口节点不同，`resistance` 只适用于特定端口类型。
- 观察器不一定是 `<point pos="...">`，也可能是线、面或其他结构。
- `domain-space gap` 的语义和格式随计算域类型变化。
- 结果节点内部结构复杂，不应未经版本验证直接注入。

## 实验性修改流程

1. 复制源 `.tsp` 到新文件。
2. 校验项目版本和目标节点实际结构。
3. 仅修改明确存在的属性。
4. 不改内部 UUID/标识字段。
5. 保存前后差异清单。
6. 用 WavEDA GUI 加载。
7. 手工检查变量、几何、端口和频扫。
8. 单点仿真通过后才允许进入自动化。

在完成多个真实工程和版本验证前，本方法不得用于 Agent 无人值守批量改工程。

## 已验证的修改能力（实验性工具集）

基于 `dipole.tsp` 的 XML 结构测试，以下修改可行（仅限结构相同的工程）：

| 工具 | 修改目标 | 关键节点 |
|------|---------|---------|
| `change_variable` | 变量值 | `<var expression="..." origin="...">` |
| `change_material` | 实体/背景材料 | `<solid material="...">`、`<bkg material="...">` |
| `change_excitation` | 激励幅度/相位 | `<excitation mag="..." phase="...">` |
| `change_port` | 端口阻抗 | `<lumped-port resistance="...">` |
| `change_frequency` | 频率范围（EM） | `<frequency-pulse physics-type="EM">` |
| `change_mesh` | 网格密度（EM） | `<mesh-3d-setting physics="EM">` |
| `change_observer` | 观测点坐标 | `<point pos="...">` |
| `change_domain` | 计算域边界 | `<domain-space gap="...">` |

所有工具遵循：只读原文件 → 修改 → 写入新文件（不覆盖原件）。改后必须在 GUI 中加载验证。内部 UUID 属性 (`inner="..."`) 不可修改。完整代码见 `templates/05_direct_tsp_tools/`。

