# 自适应网格

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Mesh\Adaptive_Mesh.html`
- 原始相对路径: `Mesh/Adaptive_Mesh.html`
- 知识模块: `网格`

## 正文抽取
## 自适应网格

WavEDA通过自适应网格剖分技术均衡仿真效率和准确度，首先生成初始网格并求解，随后在电磁场变化较大的区域细化网格，再次求解并计算误差，直至获得精确解。在电磁场强度大或梯度高的区域，网格会更为细密以确保精度，而在其他区域则采用较粗网格以减少计算量，从而在保证高效仿真的同时获得高精度解。

#### 自适应网格设置：

- 频率：自适应网格剖分迭代的频点，频率越高网格剖分越密，建议大于或等于中心频点；

- 最大迭代次数：自适应网格迭代的最大次数；

- 残差：第n次自适应网格和第n-1次自适应网格计算的S参数的相对误差，残差设置为0.02可以得到较为准确的结果，若需要更精确的结果可设置为0.01。

勾选“自适应网格”表示启动自适应网格剖分。若需进一步提升解的准确性，用户可以通过减小残差设定值或增加迭代次数来促使WavEDA进行更细致的网格剖分。当连续自适应迭代网格计算的S参数的误差小于预设的残差值或者达到最大迭代次数，自适应网格剖分则停止。

> 图片: `./images/Adaptive_Mesh_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\Adaptive_Mesh_1.png`

如下图所示，从左至右分别为模型图、初始网格划分结果和自适应网格剖分结果，以微带贴片天线为例展示WavEDA自适应网格剖分的优势。在初始网格的基础上对电磁场强度变化大的地方不断细化，对电磁场变化较小的地方粗化网格，直至满足收敛标准，并生成合适的最终网格。

> 图片: `./images/Adaptive_Mesh_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\Adaptive_Mesh_2.png`

> 图片: `./images/Adaptive_Mesh_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\Adaptive_Mesh_3.png`

> 图片: `./images/Adaptive_Mesh_4.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\Adaptive_Mesh_4.png`

## 图片资源

1. `./images/Adaptive_Mesh_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\Adaptive_Mesh_1.png`
2. `./images/Adaptive_Mesh_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\Adaptive_Mesh_2.png`
3. `./images/Adaptive_Mesh_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\Adaptive_Mesh_3.png`
4. `./images/Adaptive_Mesh_4.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Mesh\images\Adaptive_Mesh_4.png`
