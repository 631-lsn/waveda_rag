# 波端口

- 来源 HTML: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\Wave_Port.html`
- 原始相对路径: `Modeling/Stimulate/Wave_Port.html`
- 知识模块: `建模总览`

## 正文抽取
## 波端口

WavEDA中波端口通常用于模拟传输线或波导结构中的信号输入，用于处理传播模式（如TE模式、TM模式等）输入情况下的电磁问题求解。 在WavEDA中利用波端口激励时，可先进行波端口模式分析求解，查看波端口各个模式的模式图，以确定模式的正确性以及模式的传播特性，为之后的分析节省时间。

- 波端口创建 - 波端口设置 - 波端口模式分析

> 图片: `./images/Wave_Port_6.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_6.png`

### 波端口创建

WavEDA中，波端口创建的方法十分灵活，波端口所在面可以是创建好的实体面，也选中物体某个面进行创建。 波端口面的材料需为非金属，且目前只支持贴在Domain上的波端口(下图左)，不支持不在Domain上的波端口(下图右)。

> 图片: `./images/Wave_Port_1.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_1.png`

> 图片: `./images/Wave_Port_2.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_2.png`

选中波端口面后分别在以下三处地方点击，可进入波端口设置界面

- 菜单栏-模型

> 图片: `./images/Wave_Port_3.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_3.png`

- 工程树列表-波端口-右击

> 图片: `./images/Wave_Port_4.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_4.png`

- 选面模式-建模界面-右击

> 图片: `./images/Wave_Port_5.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_5.png`

### 波端口设置

WavEDA在波端口创建好后，默认波端口图形被ABC边界包围。在波端口设置界面可以对波端口名称，模式数等进行设置，分别介绍如下：

- WavEDA会自动给端口依次命名，用户也可自行修改端口名称，注意端口名称只能为数字。

- 用户可自定义波端口仿真的模式数，模式数量默认为1，最多可设置30个。

- 波端口积分线用于模式对齐以及极性设置，详细设置见波端口积分线。

- 当波端口存在多个导体时，需要给出每个模式下各个导体的电势，详细设置见波端口多导体。

### 波端口模式分析

创建好波端口后，在三维全波仿真前，可先对波端口模式进行初步分析，确定波端口设置的正确性并可以初步判断设计合理性。

波端口分析的步骤为波端口网格剖分-波端口分析-查看结果，下面将分别进行介绍。

- 在网格菜单栏中点击下图图标，可进行波端口网格剖分，波端口网格设置可见波端口网格

> 图片: `./images/Wave_Port_7.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_7.png`

- 在仿真菜单栏点击运行波端口图标，进行波端口分析。

> 图片: `./images/Wave_Port_8.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_8.png`

> 图片: `./images/Wave_Port_9.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_9.png`

- 结果显示如下显示。具体设置可见场结果

> 图片: `./images/Wave_Port_12.png`  
> 原始路径: `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_12.png`

## 图片资源

1. `./images/Wave_Port_6.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_6.png`
2. `./images/Wave_Port_1.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_1.png`
3. `./images/Wave_Port_2.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_2.png`
4. `./images/Wave_Port_3.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_3.png`
5. `./images/Wave_Port_4.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_4.png`
6. `./images/Wave_Port_5.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_5.png`
7. `./images/Wave_Port_7.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_7.png`
8. `./images/Wave_Port_8.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_8.png`
9. `./images/Wave_Port_9.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_9.png`
10. `./images/Wave_Port_12.png` -> `D:\Staid\app\waveda\documentation\helpHtml\Modeling\Stimulate\images\Wave_Port_12.png`

## 页内/相关链接

- - 波端口创建: `#General`
- - 波端口创建 - 波端口设置: `#Electromagnetic`
- - 波端口创建 - 波端口设置 - 波端口模式分析: `#Results`
- 波端口积分线用于模式对齐以及极性设置，详细设置见波端口积分线: `./Integration_Line.html`
- 当波端口存在多个导体时，需要给出每个模式下各个导体的电势，详细设置见波端口多导体: `./Multi_Conductors.html`
- 在网格菜单栏中点击下图图标，可进行波端口网格剖分，波端口网格设置可见波端口网格: `../../Mesh/Waveport_Mesh.html`
- 结果显示如下显示。具体设置可见场结果: `../../EM_Project/Field_Result.html`
