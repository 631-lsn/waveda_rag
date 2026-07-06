# 导出Snp

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Tool\Export_Snp.html`
- 原始相对路径: `Tool/Export_Snp.html`
- 知识模块: `工具`

## 正文抽取
## 导出Snp

### SNP导出选项

导出前在该对话框内可以选择类型、格式、频率范围等。

其中， 类型分为：S参数、Y参数、Z参数。

格式分为：实虚部（RI）、幅度（MA）、DB（取dB值）。

归一化分为：不归一化、归一化（同时填写参考阻抗）、不归一化（同时填写参考阻抗，不改变S参数值）。

阻抗归一化的主要目的：

- 简化计算：通过将所有阻抗值转换为相对于某个参考阻抗的比例，可以简化复杂的电路分析。

- 标准化：使用统一的参考阻抗（如50Ω）使不同设计者之间更容易交流和比较结果。

- 归一化阻抗的具体过程： 将每个元件的实际阻抗除以选定的参考阻抗（例如50Ω或75Ω），得到的比值即为归一化阻抗。 例如，如果一个元件的实际阻抗是100Ω，在50Ω的参考阻抗下，其归一化阻抗就是2（100Ω/50Ω）。 归一化阻抗在射频设计中的应用： 在Smith圆图上，归一化阻抗使得不同阻抗值可以在同一图表上表示，便于观察和调整匹配网络。 使用归一化阻抗可以帮助设计师更好地理解反射系数、回波损耗和电压驻波比等参数，从而优化电路设计。 注意事项： 不同的应用场景可能需要不同的参考阻抗，例如通信系统中常用50Ω，而有线电视系统则使用75Ω。 在进行阻抗匹配时，归一化阻抗可以简化匹配网络的设计和调试过程，但必须注意实际工作条件下的差异。 频率范围设置包括：是否选择用系统单位、最小频率（频率输出起点）、最大频点（频率输出终点）、采样点个数。

> 图片: `images/Export_Snp1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Tool\images\Export_Snp1.png`

上述设置后点击完成，并填写导出路径，最后点击保存完成导出，如下图：

> 图片: `images/Export_Snp2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Tool\images\Export_Snp2.png`

## 图片资源

1. `images/Export_Snp1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Tool\images\Export_Snp1.png`
2. `images/Export_Snp2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Tool\images\Export_Snp2.png`
