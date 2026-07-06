# 频率

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\Frequency.html`
- 原始相对路径: `Modeling/Design/Frequency.html`
- 知识模块: `建模总览`

## 正文抽取
## 频率

在电磁仿真中，通过连续或离散方式改变激励信号的频率参数记录并分析被测器件(DUT)的频域响应特性（如S参数、阻抗匹配、场分布等）。

可以双击左侧工程树下“设计”->“频率”打开对话框。 也可以点击上方主菜单栏中“建模”->“设计”->“频率”

> 图片: `./images/Frequency_13.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Frequency_13.png`

图标打开对话框。

### 扫频设置

软件提供多种设置方法，可以设置扫频范围，给定起始频率和终止频率。

- 单频点：用户定义单个频点查看。

> 图片: `./images/Frequency_8.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Frequency_8.png`

- 步长：控制每次频率增量，决定频率扫描的步长。注意：输入步长必须在扫频范围内。

> 图片: `./images/Frequency_9.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Frequency_9.png`

- 频点数：确定在频率范围内需要仿真多少个频率点。只支持实数输入。注意：对于一般模型而言，扫频的点数不需要设置太多，最多设置为301即可。根据模型复杂度酌情增减。

> 图片: `./images/Frequency_10.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Frequency_10.png`

- 对数型：频率按对数规律分布，适用于宽频范围的扫频情况。

> 图片: `./images/Frequency_11.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Frequency_11.png`

- 多频点：设置多个频点扫频，多个频点输入必须为英文逗号字符","分隔，只有离散扫频方法支持多频点扫频。

> 图片: `./images/Frequency_12.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Frequency_12.png`

### 扫频

这里可以选择不同的扫频方法，可以选择三种扫频方法。

- 离散扫频：利用当前网格剖分，逐点求解各个频点的电磁场。如果插值和快速的方法结果有异议时可以使用离散方法仿真。 此方法是最准确但是仿真速度较慢的方法，适用于需要的频点数不多，想要关注各个频点的场分布的情况。

- 插值扫频：在给定的频率范围内，由软件利用当前网格，自动确定电磁场求解的频点，然后通过内插，获得整个扫频范围内的频率响应。 其中，软件最大插值点数为250，默认插值误差为1%，当插值误差减少到1%时插值扫频结束，结果收敛，若达到最大插值点后误差大干1%、则插值扫频结束，结果不收敛。 用户可以修改最大插值点数以及插值误差，插值误差设置越小，最大插值点数设置越大，插值结果越精确，但仿真时间会相应增加。 建议插值误差不要小于0.5%。插值方法的频点由算法决定的，收敛后会根据插值结果计算用户设置频点的S参数。 需要注意的是，应用插值扫频时，用户无法查看选定频点的Snapshot； 若设置远场频点，WaVEDA会强行将该频点插入计算列表，但查看效率频率曲线等结果时，也无法保证频点个数。 WaVEDA插值扫频支持用户自定义插值最大点数以及插值误差，当插值过程中满足任意一项即视为插值收敛。

> 图片: `./images/Frequency_14.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Frequency_14.png`

- 快速扫频：采用基于krylov子空间的模型降阶技术进行快速扫频，相较于离散扫频以及插值扫频， 仿真速度大幅提升，对于宽频带仿真建议优先采用快速扫频方法。快速扫频方法中需要设置迭代次数， 表示降阶模型采用的阶数，默认是100，用户可以修改，一般设置越大，结果越准确，但相应的仿真时间会增加。 针对毫米波段的仿真，建议迭代次数设置成300，一般设置不要超过500。平面波源目前不支持快速扫频。

> 图片: `./images/Frequency_7.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Frequency_7.png`

## 图片资源

1. `./images/Frequency_13.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Frequency_13.png`
2. `./images/Frequency_8.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Frequency_8.png`
3. `./images/Frequency_9.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Frequency_9.png`
4. `./images/Frequency_10.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Frequency_10.png`
5. `./images/Frequency_11.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Frequency_11.png`
6. `./images/Frequency_12.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Frequency_12.png`
7. `./images/Frequency_14.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Frequency_14.png`
8. `./images/Frequency_7.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Design\images\Frequency_7.png`
