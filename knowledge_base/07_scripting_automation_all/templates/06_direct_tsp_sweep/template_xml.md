---
title: 直改 .tsp 扫参 — 精简 XML 脚本模板（无 modify 命令）
category: scripting
tags: [模板, XML, tsp, 精简, 代码]
indexing: true
---

# 直改 .tsp 方式 — 精简 XML 脚本模板

与标准模板的区别：没有 `modify` 命令（变量已直接写入 `.tsp` 文件），脚本仅负责 load → sim → export → close。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<script version="1.0" >
    <!--
    精简脚本模板（无 modify 命令）
    变量值已直接写入 .tsp 文件，脚本只负责 load -> sim -> export

    【你需要改】
    1. load 命令 file="..." -> 临时 .tsp 文件的路径（由 sweep_main 自动替换）
    2. export 命令 name="..." -> 数据集名称

    【不需要改】file="..." -> sweep_main 自动替换
    -->
    <command cmdType="load"   obj1="project"    file="临时.tsp路径" />
    <command cmdType="delete" obj1="mesh"       />
    <command cmdType="sim"                      solver="auto" />
    <command cmdType="export" obj1="result"  obj2="obv"    name="Observer数据集名"   file="./obv_data.txt" />
    <command cmdType="export" obj1="result"  obj2="port"   name="Port数据集名"        file="./port_data.txt" />
    <command cmdType="close" obj1="project" />
    <command cmdType="close" obj1="gui" />
</script>
```
