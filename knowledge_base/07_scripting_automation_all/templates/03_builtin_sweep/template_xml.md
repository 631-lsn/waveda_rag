---
title: 工程内置扫描 — XML 模板
category: scripting
tags: [模板, XML, 内置扫描, 代码]
indexing: true
---

# 工程内置扫描 XML 模板

**无 `modify` 命令**，参数由 `.tsp` 工程内部控制：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<script version="1.0" >
    <!--
    工程内置参数扫描 脚本模板（无 modify 命令）
    适用：.tsp 工程已在 GUI 中配置了参数扫描，WavEDA 一次跑完所有组合

    【你需要改】
    1. load 命令 file="..."    → .tsp 工程路径
    2. export port 命令 name="..." → Port S参数数据集名

    【注意】模板中没有 modify 命令，参数由 .tsp 工程内部控制
    -->
    <command cmdType="load"   obj1="project"    file="你的.tsp工程路径" />
    <command cmdType="delete" obj1="mesh"       />
    <command cmdType="sim"                      solver="auto" />
    <command cmdType="export" obj1="result"  obj2="port"   name="Port数据集名"  file="./port_data.txt" />
    <command cmdType="close" obj1="project" />
    <command cmdType="close" obj1="gui" />
</script>
```
