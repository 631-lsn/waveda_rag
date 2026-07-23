---
title: "07_scripting_automation 知识库结构说明"
content_kind: "framework"
indexing: false
---

# 07_scripting_automation 结构说明

> 仅供维护者阅读，不进入语义索引。

## 文件清单（10 个知识文档 + 19 个代码模板 = 29 个文件）

```
07_scripting_automation/
│
├── _STRUCTURE.md                           <- 本文件
│
├── 00_自动化脚本与Agent生成规范.md           <- Agent 职责边界、最小输入、执行流程
├── 01_XML命令与诊断矩阵.md                  <- XML 命令格式、7 种命令、诊断阶梯
├── 02_单参数与双参数扫描策略.md              <- 三种扫参模式、决策树、预热跑
├── 03_内置扫描与外部循环对比.md              <- 内置扫描 vs 脚本循环、互斥关系
├── 04_结果解析与成功判据.md                  <- 数据文件格式、退出码不信任原则
├── 05_故障诊断与恢复.md                      <- 6 大类问题排查 + 退出码表 + 异常检测
├── 06_代码模板与生成器设计.md                <- 模板结构规范 + templates/ 索引
├── 07_直接修改TSP_实验性.md                  <- 直改 .tsp 方案、风险、工具列表
├── 08_案例验证记录.md                        <- Dipole/AMC/模式转换器 验证结论
├── 09_快速开始与选择树.md                    <- 5 步上手 + checklist + 模式选择
│
└── templates/                               <- 完整可执行代码
    ├── 01_single_param/                     <- 单参数扫参（3 个文件）
    ├── 02_dual_param/                       <- 双参数扫参（3 个文件）
    ├── 03_builtin_sweep/                    <- 工程内置扫描（2 个文件）
    ├── 04_python/                           <- Python 版（1 个文件）
    ├── 05_direct_tsp_tools/                 <- 直改 .tsp 工具（8 个文件）
    └── 06_direct_tsp_sweep/                 <- 直改扫参核心（2 个文件）
```

## 维护说明

- 新增知识文档：按编号递增（`10_xxx.md`），同步更新本文件
- 新增代码模板：在 `templates/` 下新建子目录（`07_xxx/`），同步更新 `06` 和本文件
- 修改现有文件：更新 `updated_at` 日期
- frontmatter 约定：`content_kind`（tutorial/reference/worked_example/framework）、`priority`（5=核心, 1=实验）、`status`（validated/draft）、`indexing`（true/false）
