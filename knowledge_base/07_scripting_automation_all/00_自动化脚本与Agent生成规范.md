---
title: "WavEDA 自动化脚本与 Agent 生成规范"
content_kind: "tutorial"
physics_domain: "common"
waveda_module: "Automation"
software_version: "WavEDA 2.1/2.2，以目标安装版本为准"
priority: 5
status: "validated"
indexing: true
updated_at: "2026-07-23"
---

# WavEDA 自动化脚本与 Agent 生成规范

## 检索关键词

WavEDA 自动化、脚本生成、Agent 生成 XML、MATLAB 扫参、Python 扫参、批量仿真、参数优化。

## 目标

Agent 应把用户需求转成统一任务配置，再从同一配置生成可直接运行的 XML、`.m`、`.py` 和运行说明。不要分别手写三套互不一致的参数。

## Agent 必须完成的流程

1. 读取 `.tsp`，识别单位、基础变量、表达式变量、频扫、端口、网格和结果节点。
2. 只向用户询问工程中无法确认且会影响脚本行为的信息。
3. 将自然语言转换为明确的变量、数值、策略、目标指标和约束。
4. 先生成单点验证，再生成端点检查和正式批量任务。
5. 改变几何时默认强制删除旧网格。
6. 用导出文件的内容判断成功，退出码只作为诊断信息。
7. 每个点结束后保存进度，失败点记录后继续，不丢失已完成结果。
8. 给用户完整文件，不只给“修改某一行”的补丁。

## 最小输入

| 字段 | 来源 |
| --- | --- |
| WavEDA 可执行文件路径 | 用户或安装探测 |
| `.tsp` 工程路径 | 用户 |
| 输出目录 | 用户或安全默认值 |
| 扫描变量 | 工程解析后由用户选择 |
| 扫描值或目标效果 | 用户自然语言 |
| 结果节点、类型、曲线顺序 | 工程解析或 GUI 确认 |
| 主控制器 | MATLAB 或 Python |

## 推荐任务配置

```json
{
  "project_file": "<PROJECT_DIR>/model.tsp",
  "waveda_exe": "<WAVEDA_HOME>/WavEDA.exe",
  "output_dir": "<PROJECT_DIR>/automation_output",
  "controller": "matlab",
  "sweep": {
    "variables": {"L_t2": [4.5, 5.0, 5.5, 6.0]},
    "strategy": "explicit_values",
    "force_remesh": true
  },
  "results": [{
    "name": "Port_S_data_1",
    "type": "port",
    "traces": ["S11 dB", "S21 dB"]
  }],
  "reliability": {
    "timeout_seconds": 1800,
    "max_attempts": 3,
    "resume": true
  }
}
```

## 推荐交付物

```text
automation_task/
├── README_运行说明.md
├── task_config.json
├── run_batch.m 或 run_batch.py
├── generated_xml/
└── output/
    ├── task_manifest.json
    ├── progress.csv
    ├── raw/
    ├── figures/
    └── logs/
```

## 模块划分

- `project_inspector`：只读解析 `.tsp`。
- `intent_parser`：自然语言转任务配置。
- `strategy_planner`：选择单点、线性、网格或粗到细策略。
- `artifact_generator`：生成 XML/MATLAB/Python/README。
- `static_validator`：检查变量、节点、路径、语法和危险删除目标。
- `run_monitor`：可选执行、超时、重试和资源释放。
- `result_validator`：验证导出数据并计算指标。
- `diagnostic_planner`：失败时生成最小诊断 XML。

## 证据范围

- Dipole 外部单变量循环：已运行验证。
- AMC 强制重建网格、结果节点诊断和反射相位扫描：已运行验证。
- 紧凑型模式转换器 GUI S11/S21：已验证；批量脚本应从单点继续验证。
- 内置扫描、直接修改 `.tsp` 和并行运行：不属于当前默认已验证路径。

