# 新建端口结果

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\New_Port.html`
- 原始相对路径: `Post_Processing/New_Port.html`
- 知识模块: `后处理`

## 正文抽取
## 新建端口结果

- 选择参数 - 选择显示格式 - 选择具体参数 - 绘制曲线 - 查看绘制结果

仿真完成后，可通过右键EM结果中端口新建端口结果查看仿真端口结果信息。

> 图片: `./images/New_Port_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\images\New_Port_1.png`

选择新建端口后，将进入新建端口结果界面。

> 图片: `./images/New_Port_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\images\New_Port_2.png`

### 选择参数

左上侧参数列表中，可以选择想要查看的参数类型。

- S参数：查看仿真散射参数，其中针对波端口激励模型，需要考虑激励模式与接收模式问题，因此结果选择为S(接收端口:接收模式,激励端口:激励模式)形式。

- 差分对：涉及差分对时，可查看差分共模结果信息。

- Z参数：查看阻抗参数。

> 图片: `./images/New_Port_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\images\New_Port_3.png`

- TDR和TDT：用于时域反射和透射分析，点击TDR或TDT后，再点击端口框处TDR参数进行脉冲绘制，选择想要的时长、采样时间、窗类型进行输入信号的绘制，绘制完成后可根据需要查看对应TDR和TDT结果。

- 电压和电流：可查看随频率变化的电压电流信息。

- Y参数：查看导纳参数(仅在波端口离散或快速扫描情况下)。

- 参考阻抗：查看Modal模式下或Terminal模式下的随频率变化的波端口线阻抗参数(仅在波端口离散或快速扫描情况下)。

- Gamma参数：查看随频率变化的Gamma参数(仅在波端口离散或快速扫描情况下)。

### 选择显示格式

左下侧参数列表中，可以选择要查看参数的表示形式，有dB、real、imag、mag、phase。

### 选择具体参数

根据需要选择具体要查看的参数，例如，想要查看S参数，可以选择要查看的具体参数，在端口数量较多时，可以进行定量选择。

> 图片: `./images/New_Port_4.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\images\New_Port_4.png`

如图所示，可通过选择全部、选择自身的参数、选择相互的参数、选择(*,1)和(1,*)的参数。

### 绘制曲线

> 图片: `./images/New_Port_5.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\images\New_Port_5.png`

如图选择好需要查看的参数后，点击添加曲线，该曲线将会进入到绘制数据框中，若添加错了曲线，也可以通过选择绘制数据中相应的数据进行删除曲线，最后点击应用，曲线绘制完毕。

### 查看绘制结果

上述步骤操作完成后，即可绘制出想要查看的参数。

> 图片: `./images/New_Port_6.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\images\New_Port_6.png`

在绘制完成后的图像中，点击鼠标右键，可以对图片数据进行修改结果图、图标设置、重置坐标轴、mark点标记、复制数据、复制图像、导出数据、导入数据、计算曲线误差功能设置。

> 图片: `./images/New_Port_7.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\images\New_Port_7.png`

有关图表设置如下图所示，可进行X、Y轴名称修改，坐标值标签字体和大小修改，X/Y轴范围修改(注意X轴范围不能超过仿真频率范围)，图例名称、曲线颜色、样式、标识、宽度、是否显示修改。

> 图片: `./images/New_Port_8.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\images\New_Port_8.png`

注意改变X轴范围仅改变了显示，导出数据时还是导出全范围X轴数据。

新建端口结果还可以通过后处理处端口结果进行设置。

## 图片资源

1. `./images/New_Port_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\images\New_Port_1.png`
2. `./images/New_Port_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\images\New_Port_2.png`
3. `./images/New_Port_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\images\New_Port_3.png`
4. `./images/New_Port_4.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\images\New_Port_4.png`
5. `./images/New_Port_5.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\images\New_Port_5.png`
6. `./images/New_Port_6.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\images\New_Port_6.png`
7. `./images/New_Port_7.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\images\New_Port_7.png`
8. `./images/New_Port_8.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Post_Processing\images\New_Port_8.png`

## 页内/相关链接

- - 选择参数: `#选择参数`
- - 选择参数 - 选择显示格式: `#选择显示格式`
- - 选择参数 - 选择显示格式 - 选择具体参数: `#选择具体参数`
- - 选择参数 - 选择显示格式 - 选择具体参数 - 绘制曲线: `#绘制曲线`
- - 选择参数 - 选择显示格式 - 选择具体参数 - 绘制曲线 - 查看绘制结果: `#查看绘制结果`
- 新建端口结果还可以通过后处理: `./Post_Processing.html`
