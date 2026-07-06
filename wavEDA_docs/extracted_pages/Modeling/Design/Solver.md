# 求解器

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\Solver.html`
- 原始相对路径: `Modeling/Design/Solver.html`
- 知识模块: `建模总览`

## 正文抽取
## 求解器

双击左侧工程树下“设计”->“求解器”打开对话框。 也可以点击上方主菜单栏中“建模”->“设计”->“求解器”图标打开对话框。

> 图片: `./images/Solver_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Solver_1.png`

### 求解器

软件默认使用混合有限元算法（Mixed Finite Element Method, MFEM) 进行电磁场数值仿真。 有限元法将复杂的物理场问题划分为有限个单元，并施加相应边界条件，选择基函数用于近似求解。传统有限元方法在求解高密度问题（网格尺寸远小于波长）时，常常难以求得准确解。WavEDA软件创新性地对电磁场方程进行约束，使得高密度问题也可进行精确仿真。

### 基函数

在有限元法中，基函数用于表示每个单元内的物理量（如电磁、位移、温度等）的变化。基函数的选择对于求解精度和计算效率有重要影响。 一阶基函数是指每个单元内的基函数为线性函数。 二阶基函数是指基函数是二次多项式，通常用于提高近似精度，尤其是在物理量变化较为剧烈的区域。注意，在同等网格数量下，选择二阶基函数，求解的自由度相对于一阶基函数更多。软件默认使用二阶基函数。

## 图片资源

1. `./images/Solver_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Solver_1.png`
