---
title: "变量"
merged_source: "current_waveda_agent_kb"
source_relative_path: "10_extracted_pages/Tool/Variables.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\10_extracted_pages\Tool\Variables.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 变量

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Tool\Variables.html`
- 原始相对路径: `Tool/Variables.html`
- 知识模块: `工具`

## 正文抽取
## 变量

- 变量用途 - 描述 - 保留变量名称 - 以函数形式创建 - 绘制

模型建立过程中如果需要设置变量，则可以在工具->变量添加并查看所有变量的信息。输入变量名称，并在输入栏填写相应数值，点击添加即完成。 若想修改已添加的变量值，需要选中该变量后在数值位置修改，再点击“编辑修改”，这样就完成修改。

注意：输入变量的名称是不区分大小写的。例如："N"和"n"是同一个变量。

> 图片: `./images/Variables_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Tool\images\Variables_1.png`

### 变量用途

所有使用该变量定义的物体将显示在该列表。

### 描述

添加变量后可以为它添加备注，方便对应该变量的含义，便于对模型理解。

### 保留变量名称

pi, e, t, t1, t2是软件已经定义的变量名称，不可以再次被定义。请注意添加时命名问题。

### 以函数形式创建

这里列举了支持以函数形式创建的变量函数，可以参照列举的以下函数添加函数变量。sin();cos(); tan();sind(); cosd(); tand(); asin(); acos(); atan():sinh(); cosh();tanh(); asinh(); acosh(); atanh();log2(); log10(); ln(); exp(); abs(); sqrt()。

### 绘制

变量添加支持生成函数曲线。变量使用函数输入，可以看到该变量的函数的绘图曲线。 首先，选择目标表达式变量，点击绘制进入编辑绘制界面，选择当前表达式中的目标变量作为变量，输入需要查看的横坐标范围（最小值和最大值），点击绘制即可看到当前变量在当前表达式中的曲线变化结果。

注意：如果该变量的表达式包含多个变量，软件会涉及的变量分级表示出来。 （例如：D表达式中包含了B和C两个变量，C表达式由A变量组成，那么B和C在第二级表达式中体现，A的表达式在最后一级表达式显示，以此类推）。

> 图片: `./images/Variables_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Tool\images\Variables_3.png`

## 图片资源

1. `./images/Variables_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Tool\images\Variables_1.png`
2. `./images/Variables_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Tool\images\Variables_3.png`

## 页内/相关链接

- - 变量用途: `#Variable usage`
- - 变量用途 - 描述: `#Reserved Variable Name`
- - 变量用途 - 描述 - 保留变量名称: `#Reserved Variable Name`
- - 变量用途 - 描述 - 保留变量名称 - 以函数形式创建: `#Build-In Function`
- - 变量用途 - 描述 - 保留变量名称 - 以函数形式创建 - 绘制: `#Plot`
