---
title: 单参数扫参 — XML 模板
category: scripting
tags: [模板, XML, 单参数, 代码]
indexing: true
---

# 单参数扫参 XML 模板

```xml
<?xml version="1.0" encoding="UTF-8"?>
<script version="1.0" >
    <!--
    单参数扫参 基础脚本模板

    【你需要改】
    1. load 命令 file="..."    → .tsp 工程路径
    2. modify 命令 name="..."  → 变量名
    3. export obv 命令 name="..." → Observer 数据集名
    4. export port 命令 name="..." → Port S参数数据集名

    【不需要改】
    - value="25"、file="..."  → sweep_main 自动替换
    -->
    <command cmdType="load"   obj1="project"    file="你的.tsp工程路径" />
    <command cmdType="modify" obj1="var"        name="你的变量名"    value="25" />
    <command cmdType="delete" obj1="mesh"       />
    <command cmdType="sim"                      solver="auto" />
    <command cmdType="export" obj1="result"  obj2="obv"    name="Observer数据集名"   file="./obv_data.txt" />
    <command cmdType="export" obj1="result"  obj2="port"   name="Port数据集名"        file="./port_data.txt" />
    <command cmdType="close" obj1="project" />
    <command cmdType="close" obj1="gui" />
</script>
```
