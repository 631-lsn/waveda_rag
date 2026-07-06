# 磁色散材料

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Bkg_Mat\Magnetic_Dispersion.html`
- 原始相对路径: `Modeling/Bkg_Mat/Magnetic_Dispersion.html`
- 知识模块: `建模总览`

## 正文抽取
## 磁色散材料

- 磁介质色散 - 拟合

磁色散材料是在不同频率下展现出不同电磁性质的材料，主要表现为磁介电常数随频率的变化，在不同的频段中表现出不同的特性。 软件支持导入色散模型文件或手动输入磁介电常数随频率变化参数，可进行色散材料曲线的拟合。 进入材料设置界面后，单击“磁介质色散”进入电介质色散材料设置。

### 磁介质色散

> 图片: `./images/Magnetic_Dispersion_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Bkg_Mat\images\Magnetic_Dispersion_1.png`

- 选择色散模型或是用户自定义。

- 磁性极大值：在高频磁场下（如微波、射频范围），材料的磁导率或磁损耗（tanδ）可能出现局部极大值。这一峰值通常与特定磁矩弛豫机制相关。

- 磁性稳态值：在静态磁场​（频率趋近于0）或极低频条件下，材料中所有磁矩（如电子自旋、轨道磁矩、畴壁磁矩等）均能完全响应外加磁场，此时材料的磁导率（μ）或磁化率（χ）达到稳定值。

- 松弛时间：是描述磁性材料响应时间延迟的一个重要参数，表示材料从一个外部磁场扰动中恢复到平衡状态所需要的时间。 在频率较低时，材料的磁性反应主要由这些松弛过程控制。松弛时间通常用于描述磁性材料中磁化的延迟效应，尤其是在涉及到磁畴的变化或旋转时。

- 拟合误差：利用理论模型（如Debye模型、Lorentz模型等）拟合电介质材料的介电常数与频率之间的关系时， 实际测量数据与模型预测值之间的差异。拟合误差的大小直接影响到模型对材料电磁特性的描述精度和有效性。 软件会在用户点击“更新结果”后实时更新拟合误差。

### 拟合

该处拟合内容与电色散材料相同，具体查看电色散材料文档中有关拟合章节描述。

## 图片资源

1. `./images/Magnetic_Dispersion_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Bkg_Mat\images\Magnetic_Dispersion_1.png`

## 页内/相关链接

- - 磁介质色散: `#磁介质色散`
- - 磁介质色散 - 拟合: `#拟合`
- 该处拟合内容与电色散材料相同，具体查看电色散材料: `./Dielectric_Dispersion.html`
