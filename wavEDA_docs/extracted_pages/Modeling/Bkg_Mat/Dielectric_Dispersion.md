# 电色散材料

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Bkg_Mat\Dielectric_Dispersion.html`
- 原始相对路径: `Modeling/Bkg_Mat/Dielectric_Dispersion.html`
- 知识模块: `建模总览`

## 正文抽取
## 电色散材料

- 电介质色散 - 拟合

电色散材料是在不同频率下展现出不同电磁性质的材料，主要表现为介电常数随频率的变化，在不同的频段中表现出不同的特性。 软件支持导入色散模型文件或手动输入介电常数随频率变化参数，可进行色散材料曲线的拟合。 进入材料设置界面后，单击“电介质色散”进入电介质色散材料设置。

### 电介质色散

> 图片: `./images/Dielectric_Dispersion_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Bkg_Mat\images\Dielectric_Dispersion_1.png`

- 选择色散模型或是用户自定义。

- 电极大值： 在介电常数（或介电损耗）随频率变化的曲线中，可能出现局部极大值。这一峰值通常与特定极化机制的松弛过程相关。

- 电稳态值：当频率趋近于零（直流条件）或极低频时，材料中的所有极化机制（如偶极子极化、离子极化、界面极化等）均能充分响应电场变化，此时材料的介电常数达到一个稳定值。

- 松弛时间是描述电介质材料极化过程的一个时间常数。 它表示电介质在外加电场作用下，材料的极化强度达到稳态所需要的时间。松弛时间是一个重要的物理量，它与材料中电子、原子或分子极化的速度有关。

- 拟合误差：利用理论模型（如Debye模型、Lorentz模型等）拟合电介质材料的介电常数与频率之间的关系时， 实际测量数据与模型预测值之间的差异。拟合误差的大小直接影响到模型对材料电磁特性的描述精度和有效性。 软件会在用户点击“更新结果”后实时更新拟合误差。

### 拟合

> 图片: `./images/Dielectric_Dispersion_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Bkg_Mat\images\Dielectric_Dispersion_2.png`

- 列表 频率(GHz)：该列是色散材料的频率，需要指定频率范围。 软件允许用户为材料的色散特性指定一个频率范围，在此范围内，软件将计算材料的介电常数，并根据频率依赖关系更新介电常数。 注意此处的频率支持支以GHz为单位的色散材料频率范围。 Eps′：表示材料的介电常数的实部，是材料的储能能力，决定了电场传播的速度。高Eps′的材料可以较慢地传播电磁波。 Eps′′：表示材料的介电常数的虚部，与材料的损耗相关，反映了材料对电磁波的吸收。 插入行：用户自定义色散参数，根据需要插入合适的行数。 删除行：根据需要删除不需要的行，选中目标行，点击“删除行”，完成删除行。 清除列表：点击此处清空列表所有内容。 导入文件：支持导入预设的色散模型，只支持txt格式导入。 导出文件：支持列表中的数据导出到外部文件。支持txt格式导出。

> 图片: `./images/Dielectric_Dispersion_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Bkg_Mat\images\Dielectric_Dispersion_3.png`

- 拟合结果图 根据左侧列表输入的参数，点击“更新结果”，软件提供拟合工具，通过最小化残差来优化这些参数，确保模型与实验数据尽可能吻合。 在拟合结果图中，你可以看到四条曲线，分别是初始的Eps′曲线、拟合后的Eps′曲线、初始的Eps′曲线和拟合后的Eps′′曲线。 拟合频率：设置用户想要查看的拟合范围，点击“更新结果”，可以看到用户自定义的拟合曲线。

## 图片资源

1. `./images/Dielectric_Dispersion_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Bkg_Mat\images\Dielectric_Dispersion_1.png`
2. `./images/Dielectric_Dispersion_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Bkg_Mat\images\Dielectric_Dispersion_2.png`
3. `./images/Dielectric_Dispersion_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Bkg_Mat\images\Dielectric_Dispersion_3.png`

## 页内/相关链接

- - 电介质色散: `#电介质色散`
- - 电介质色散 - 拟合: `#拟合`
