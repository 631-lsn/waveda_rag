---
title: "WavEDA XML 命令与最小诊断矩阵"
content_kind: "tutorial"
physics_domain: "common"
waveda_module: "Automation"
software_version: "WavEDA 2.1/2.2，以目标安装版本为准"
priority: 5
status: "validated"
indexing: true
updated_at: "2026-07-23"
---

# WavEDA XML 命令与最小诊断矩阵

## 检索关键词

`script=`、`cmdType`、load、modify、delete mesh、sim、export、close、逐命令隔离。

## 典型命令链

```xml
<?xml version="1.0" encoding="UTF-8"?>
<script version="1.0">
    <command cmdType="load" obj1="project" file="&lt;PROJECT_FILE&gt;" />
    <command cmdType="modify" obj1="var" name="INP" value="18.5" />
    <command cmdType="delete" obj1="mesh" />
    <command cmdType="sim" solver="auto" />
    <command cmdType="export" obj1="result" obj2="port"
             name="Port_S_data_1" file="&lt;PORT_FILE&gt;" />
    <command cmdType="close" obj1="project" />
    <command cmdType="close" obj1="gui" />
</script>
```

## 顺序规则

- `load` 先于所有工程操作。
- 全部变量修改完成后只删除一次网格。
- 本轮 `sim` 完成后才能导出本轮结果。
- `export name` 必须与工程结果节点完全一致。
- 路径必须做 XML 转义。
- 最后关闭工程和 GUI，减少下一轮进程和许可证冲突。

## 最小诊断矩阵

| 阶段 | 命令 | 目的 |
| --- | --- | --- |
| 1 | `load + close` | 确认工程可由脚本加载。 |
| 2 | `load + modify + close` | 确认变量存在且脚本修改被接受。 |
| 3 | 加 `delete mesh` | 确认删除网格命令可执行。 |
| 4 | 加 `sim`，不导出 | 隔离模型、网格和求解器问题。 |
| 5 | 只导出 port | 检查端口结果节点。 |
| 6 | 只导出 observer | 检查观察器结果节点。 |
| 7 | 组合导出 | 验证正式工作流。 |

如果某一阶段首次失败，后续复杂命令暂时不要继续添加。

## 退出码的证据化解释

| 退出码 | 已观察现象 | 处理 |
| --- | --- | --- |
| `-1 / 0xFFFFFFFF` | 某些安装中 GUI 正常关闭且文件完整 | 记录警告；文件有效则判成功。不是所有版本的通用成功码。 |
| `-1073741819 / 0xC0000005` | Windows 访问冲突 | 拆分 sim、port、observer；不能只凭代码断言根因。 |
| `-532265403 / 0xE0464645` | 曾在结果生成/导出阶段出现 | 检查节点、名称和导出时序。 |
| 超时 | 网格、求解或 GUI 无响应 | 停止进程，记录阶段，缩小模型或降低频点后验证。 |

## 启动方式

优先直接启动 WavEDA 可执行文件并传入独立参数。若特定安装因 DLL 搜索路径失败，可使用 BAT 兼容方案：

```bat
cd /d "<WAVEDA_HOME>"
WavEDA.exe "script=<RUN_XML>"
```

BAT 是兼容回退，不应被描述为所有环境的强制要求。

