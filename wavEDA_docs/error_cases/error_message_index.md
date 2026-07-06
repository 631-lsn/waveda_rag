# 真实 UI 报错/警告文案索引

本文件从 `resources/language/*.ts` 抽取，包含软件真实弹窗、日志、验证失败和 UI 错误提示。解决建议为基于文案类别生成的初筛检查项，需要结合具体模型和日志确认。

- UI 文案总数: 13050
- 错误/警告候选数: 1402

## 分类统计

| 分类 | 数量 |
| --- | --- |
| 仿真/求解 | 26 |
| 其他 | 559 |
| 几何/选择 | 122 |
| 参数/输入格式 | 412 |
| 文件/导入导出 | 97 |
| 材料 | 25 |
| 端口/激励 | 133 |
| 网格 | 27 |
| 连接/许可 | 1 |

## 仿真/求解
| 文件 | 英文/原文 | 中文提示 | 初筛检查建议 |
| --- | --- | --- | --- |
| st_Chinese.ts | Unable to create boundary condition during simulation. | 仿真过程中不允许创建边界面。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | Offset surface operations are not allowed in the simulation. | 仿真中不允许偏移面操作。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | Blend is not allowed in simulation. | 转圆角不允许。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | Chamfer is not allowed in simulation. | 倒角不能包含中文。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | Unable to create during simulation. | 仿真过程中无法创建。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | Unable to create surface during simulation. | 仿真过程中不允许创建面。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | The far-fields simulation frequency points does not exist. | 远场仿真频率点不存在。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | The far-field simulation result failed to be read because the far-field simulation data was deleted or was not generated | 读取远场仿真结果失败，请检查远场仿真数据是否被删除，或未生成远场仿真数据。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | Failed to read observer simulation results. Possible reasons: Observer simulation data was deleted or not generated. | 读取接收器仿真结果失败，原因可能是：接收器仿真数据被删除，或未生成接收器仿真数据。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | Failed to extract far-field data from simulation results. | 从仿真结果中提取远场数据失败。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | The snapshot simulation frequency points does not exist. | 快照仿真频率点不存在。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | Select a uniform medium for simulation background. The default is air. | 仿真背景请选择均匀介质，默认为空气。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | The subcircuit can't  be simulated. | 该子电路无法进行仿真。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | Parameters validation failed before simulation. | 仿真前参数验证失败。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | solver error | 求解器错误 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | The far-field simulation result failed to be read because the far-field simulation data was deleted or was not generated | 读取远场仿真结果失败，请检查远场仿真数据是否被删除，或未生成远场仿真数据。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | Unable to create boundary condition during simulation. | 仿真过程中不允许创建边界面。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | The observer simulation result does not exist, please check whether the receiver simulation result is cleared, or the re | 接收器仿真结果不存在，请检查接收器仿真结果是否被清除，或未生成接收器仿真结果。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | The current and voltage simulation results cannot be obtained by interpolation sweep method. | 插值扫频方法无法获取电流和电压仿真结果。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_Chinese.ts | The variable "%1" is being used by other variables, or geometry, or SEM solver setup, etc., can not be deleted | 变量%1正被其他变量、几何体或SEM求解器设置等使用，无法删除 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_core_Chinese.ts | The sweep type of the simulation control is incorrect and exceeds the selectable range. | 仿真控件的扫频类型错误，超出可选择范围。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_core_Chinese.ts | arpack solve KO. | arpck求解器失败。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_core_Chinese.ts | Parameters validation failed before simulation. | 仿真前参数校验失败。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_core_Chinese.ts | Failed to read far-field simulation data. Check whether far-field simulation data is deleted or not generated. | 读取远场仿真数据失败，请检查远场仿真数据是否被删除，或未生成远场仿真数据。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_simulator_Chinese.ts | Parameters validation failed before simulation. | 仿真前参数校验失败。 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |
| st_simulator_Chinese.ts | error:failed to prepare simulation parameter | 错误：准备仿真参数失败 | 先运行验证，检查频率、求解器、Domain、材料、端口/激励是否完整；查看详细日志定位失败阶段。 |

## 其他
| 文件 | 英文/原文 | 中文提示 | 初筛检查建议 |
| --- | --- | --- | --- |
| st_cad_Chinese.ts | LCS U/V Axis are not ortho, please check it. | LCS U/V轴不是正交的，请检查。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | An error occurred in the OCC model library. | OCC模型库发生错误。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Point P is too close to P1. | P点不能过于接近P1。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The offset of Ang0 & Ang1 > 360 or Ang0 = Ang1 | 角1和角2的偏移不能大于360，且角1不能等于角2 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The value of t0 cannot be empty. | t0的值不能为空。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The value of t0 cannot contain Chinese characters. | t0的值不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The value of t0 cannot contain other characters. | t0的值不能包含其他字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The value of t1 cannot be empty. | t1的值不能为空。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The value of t1 cannot contain Chinese characters. | t1的值不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The value of t1 cannot contain other characters. | t1的值不能包含其他字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The definition of U(t) cannot be empty. | U(t)的定义不能为空。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The definition of U(t) cannot contain Chinese characters. | U(t)的定义不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The definition of V(t) cannot be empty. | V(t)的定义不能为空。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The definition of W(t) cannot be empty. | W(t)的定义不能为空。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The definition of W(t) cannot contain Chinese characters. | W(t)的定义不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The definition of U(t) cannot contain other characters. | U(t)的定义不能包含其他字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The definition of V(t) cannot contain other characters. | V(t)的定义不能包含其他字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The definition of W(t) cannot contain other characters. | W(t)的定义不能包含其他字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | User-defined discrete points cannot contain Chinese characters. | 用户自定义离散点数不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | User-defined discrete points cannot contain characters other than numbers. | 用户自定义离散点数不能包含除数字外的其他字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The height value cannot be 0. | 高度值不能为0。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Corner point 1 cannot contain Chinese characters. | 角点1不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Corner point 2 cannot contain Chinese characters. | 角点2不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Rectangle dimensions cannot be 0. | 矩形尺寸不能为0。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Length cannot contain Chinese characters. | 长度不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Width cannot contain Chinese characters. | 宽度不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The length of the rectangle cannot be 0. | 矩形的长不能为0。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The width of the rectangle cannot be 0. | 矩形的宽不能为0。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The length of the rectangle cannot be <= 0. | 矩形的长不能<=0。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The width of the rectangle cannot be <= 0. | 矩形的宽不能<=0。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The radius (U-axis direction) cannot contain Chinese characters. | 半径（U轴方向）不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The radius (V-axis direction) cannot contain Chinese characters. | 半径（V轴方向）不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Edges Count  cannot contain Chinese characters. | 边数不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Start Point cannot contain Chinese characters. | 起始点不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The starting point cannot be the origin. | 起始点不能是原点。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Vertices cannot contain Chinese characters. | 顶点不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | '%1' cannot contain Chinese characters. | '%1' 不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | t1 range error. t1_0 must be less than t1_1. | t1的范围错误，t1_0需 < t1_1。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | t2 range error. t1_0 must be less than t1_1. | t2的范围错误，t2_0必须小于t2_1。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Ru cannot contain other characters. | Ru不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Rv cannot contain other characters. | Rv不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Rw cannot contain other characters. | Rw不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Corner points cannot contain Chinese characters. | 角点不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The lower corner point cannot contain Chinese characters. | 下角点不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The upper corner point cannot contain Chinese characters. | 上角点不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The distance between the upper and lower corner points in the x direction cannot be 0. | 上下角点在x方向上的距离不能为0。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The distance between the upper and lower corner points in the y direction cannot be 0. | 上下角点在y方向上的距离不能为0。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The distance between the upper and lower corner points in the z direction cannot be 0. | 上下角点在z方向上的距离不能为0。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Height cannot contain Chinese characters. | 高度不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The number of sides cannot contain Chinese. | 边数不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The bottom and top radius cannot be 0. | 底部和顶部的半径不能为0。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Major radius cannot contain Chinese characters. | 外圆半径不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Outer major radius cannot contain Chinese characters. | 外椭圆半长轴不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Outer minor radius cannot contain Chinese characters. | 外椭圆半短轴不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Inner major radius cannot contain Chinese characters. | 外椭圆半长轴不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Inner minor radius cannot contain Chinese characters. | 外椭圆半短轴不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Angle1 cannot contain Chinese characters. | 角度1不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Angle2 cannot contain Chinese characters. | 角度2不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The start angle and end angle cannot be the same. | 起始角度与终止角度不能相同。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The starting circle radius cannot contain Chinese characters. | 起始圆半径不能包含中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | End The radius of the circle cannot contain Chinese characters. | 结束圆半径不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The height cannot be empty. | 高度不能为空。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The value of height cannot be 0. | 高度的值不能为0。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The taper cannot contain Chinese characters. | 锥度不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The taper cannot contain other characters. | 锥度不能包含其他字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | '%1' cannot be null. | '%1' 不能为空。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Error arc instruction: '%1'. Skip. | 错误的arc指令：'%1‘，跳过。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | Error | 错误 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The twist cannot contain Chinese characters. | 扭曲不能包含中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_cad_Chinese.ts | The twist cannot contain other characters. | 扭曲不能包含其他字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Error | 错误 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | " is in use and cannot be deleted. Please exit. | 已经被使用，不能删除。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | " is being used, can't be deleted, quit. | " 已经被使用，不能删除，退出。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | The default boundary condition cannot be deleted. Please double-click to modify the boundary condition. | 默认边界不能删除，请双击修改边界条件。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | After deleting the snapshot frequency point, the snapshot results will be cleared and the operation cannot be undone. Do | 删除快照频点后，快照结果将被清空且无法撤回该操作，是否继续？ | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Filter Error Messages | 过滤错误信息 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Warning | 警告 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Filter Warning Messages | 筛选警告信息 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | warning | 警告 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Unknown error, unable to obtain LCS. | 位置错误，不能获取LCS坐标。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | contains unparseable string. | 包含无法解析的字符串。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Preview failed. | 预览失败。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | The angle range of arc is error, fabs(theta0 - theta1) should be in the range of [1e-4, 360]. | 圆弧的角度范围错误，theta0-theta1的绝对值应该在[1e-1,360]范围内。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | range of t1 error | t1范围错误，需满足 t1_0 < t1_1 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | range of t2 error | t2范围错误，需满足 t2_0 < t2_1 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | error | 错误 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Corner is not allowed to contain Chinese characters. | 角度不允许填写中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Length is not allowed to contain Chinese characters. | 长度不允许填写中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Lower corner is not allowed to contain Chinese characters. | 角落坐标不允许填入中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Upper corner is not allowed to contain Chinese characters. | 角落坐标不允许填入中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | The minimum value on the x-axis cannot be equal to the maximum value. | x轴方向最小坐标值不能等于最大坐标值。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | The minimum value on the y-axis cannot be equal to the maximum value. | y轴方向最小坐标值不能等于最大坐标值。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | The minimum value on the z-axis cannot be equal to the maximum value. | z轴方向最小坐标值不能等于最大坐标值。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Ru is not allowed to contain Chinese characters. | Ru不允许填入中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Rv is not allowed to contain Chinese characters. | Rv不允许填入中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Rw is not allowed to contain Chinese characters. | Rw不允许填入中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Bottom center is not allowed to contain Chinese characters. | 底部中心值不允许填入中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Bottom radius is not allowed to contain Chinese characters. | 底部半径不允许填入中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Top radius is not allowed to contain Chinese characters. | 顶部半径不允许填入中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Height is not allowed to contain Chinese characters. | 高度不允许填入中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Corn edge is not allowed to contain Chinese characters. | 不允许填入中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | The ratio of radius to height cannot exceed 1e6:1, please modify the radius or height. | 半径与高度之比不能大于1e6，请修正半径或者高度。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Outer major radius is not allowed to contain Chinese characters. | 内部的长半径不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Outer minor radius is not allowed to contain Chinese characters. | 外部的短半径不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Inner major radius is not allowed to contain Chinese characters. | 内部的长半径不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Inner minor radius is not allowed to contain Chinese characters. | 内部的短半径不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Angle is not allowed to contain Chinese characters. | 角度不允许填入中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Arc angles cannot be the same. | 弧角不能一样。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Major radius is not allowed to contain Chinese characters. | 主半径不允许填入中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Sub radius is not allowed to contain Chinese characters. | 半径不能包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Origin is not allowed to contain Chinese characters. | 原点不允许填写中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | U axis is not allowed to contain Chinese characters. | U轴不允许填入中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | V axis is not allowed to contain Chinese characters. | V轴不允许填入中文字符。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Selections can't make rect! | 所选不能创造矩形！ | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | The length is not allowed to contain Chinese characters. | 长度不允许包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | The width is not allowed to contain Chinese characters. | 宽度不允许包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | The ratio of length to width cannot exceed 1e6:1, please modify the length or width. | 长度和宽度比例不能超过1e6：1，请修改长或宽。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | The length of the rectangle cannot be 0. | 矩形的长不能为0。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | The width of the rectangle cannot be 0. | 矩形的宽不能为0。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |
| st_Chinese.ts | Radius (in U axis) is not allowed to contain Chinese characters. | U轴上半径不允许包含中文。 | 结合原始提示、当前操作阶段和帮助文档限制进一步排查。 |

该分类还有 439 条，完整内容见 `error_message_index.csv`。

## 几何/选择
| 文件 | 英文/原文 | 中文提示 | 初筛检查建议 |
| --- | --- | --- | --- |
| st_cad_Chinese.ts | Curve creation failed. Please check. | 曲线创建失败，请检查。（可能有各种各样的原因导致失败）。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_cad_Chinese.ts | The bottom radius cannot contain Chinese characters. | 底面半径不能包含中文。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_cad_Chinese.ts | The top radius cannot contain Chinese characters. | 顶面半径不能包含中文。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_cad_Chinese.ts | Sub radius cannot contain Chinese characters. | 截面圆半径不能包含中文。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_cad_Chinese.ts | The wire diameter cannot contain Chinese characters. | 线圈截面半径不能包含中文。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_cad_Chinese.ts | The helix section radius cannot contain Chinese characters. | 螺旋线截面半径不能包含中文。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_cad_Chinese.ts | The number of coils cannot be empty. | 线圈圈数不能为空。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_cad_Chinese.ts | The number of coils cannot include Chinese characters. | 线圈圈数不能包含中文。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_cad_Chinese.ts | The error occurred when'%1' was loaded, replacing it with a 100x100x100 cube. | 错误发生在加载 '%1' 时，替换为一个100x100x100的正方体。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Wrong point selection, please select a point. | 选点错误，请选择一个点。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Line receiver selection point error, please select two points. | 线接收器选点错误，请选择两个点。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Fail in covering edges to a face. | 从线生面失败。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Solid (%1) separating failed, unknown reason. | 实体(%1)分离失败，原因未知。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The object cannot be split | 该物体不能被分割 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Two points cannot be on the same solid. | 两点不能位于同一物体上。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Start angle of arc is not allowed to contain Chinese characters | 弧线的起始角不允许包含中文 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | End angle of arc is not allowed to contain Chinese characters. | 弧线的终止角不允许包含中文。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | These vertices cannot create a polygon, please make sure the vertices are on the same plane. | 这些顶点无法创建一个多边形，请确认顶点在同一平面。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Start angle of arc is not allowed to contain Chinese characters. | 弧线的起始角不允许包含中文。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Solid does not exist | 物体不存在 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Plane wave exist in the project. The result cannot be viewed. | 项目中已存在平面波。无法查看结果。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Incorrect chart selection. | 图表选择错误。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Create Dimension Line | 写入几何数据失败 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The two integral lines are not perpendicular to each other. | 两条积分线不能相互垂直。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | failed to write geometry data | 错误写几何数据 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | create curve error | 创建线错误 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | create face error | 创建面错误 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | create solid error | 创建体错误 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Fail to sperate one face to sub-face! | 无法从一个面分割为一个子面！ | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The spiral name is empty. | 该螺旋线名称为空。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The number of user-defined faces is empty, please select a face. | 用户定义的面数量为空，请选择一个面。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The number of user-defined faces is empty, please select a face. | 用户定义的面数量为空，请选择一个面。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The number of user-defined edges is empty, please select a edge. | 用户自定义的边数量为空，请选择一条边。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The number of user-defined points is empty, please select a point. | 用户自定义点数量为空，请选择一个点。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The number of user-defined faces is empty, please select a face. | 用户定义的面数量为空，请选择一个面。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The number of user-defined edges is empty, please select a edge. | 用户自定义的边数量为空，请选择一条边。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The number of user-defined points is empty, please select a point. | 用户自定义点数量为空，请选择一个点。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The number of user-defined faces is empty, please select a face. | 用户定义的面数量为空，请选择一个面。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The number of user-defined edges is empty, please select a edge. | 用户自定义线数量为空，请选择一条边。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The number of user-defined points is empty, please select a point. | 用户自定义点数量为空，请选择一个点。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Solid (%1) separation failed, unknown reason. | 体(%1)分离失败，原因未知。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Only solids are allowed to align X plane. Please check if points, lines, and faces have been selected. | 仅体可对齐 X 平面，请检查是否选择了点、线或面。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Only solids are allowed to align Y plane. Please check if points, lines, and faces have been selected. | 仅体可对齐 Y 平面，请检查是否选择了点、线或面。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Only solids are allowed to align Z plane. Please check if points, lines, and faces have been selected. | 仅体可对齐 Z 平面，请检查是否选择点、线或面。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Only faces are allowed be thickened. Please check if other points, lines, or bodies have been selected. | 仅面可加厚，请检查是否选择点、线或体。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Solid separation failed, unknown reason. | 体分离失败，原因未知。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Face separation failed, unknown reason. | 面分离失败，原因未知。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Cannot copy group and objects at the same time. | 不能同时复制组和物体。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The face name is empty. | 面名称为空。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The plane position is empty. | 平面位置为空。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The plane normal is empty. | 平面法线为空。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The face name is empty. | 面名称为空。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The curve name is empty. | 该曲线名称为空。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The start and end points of the linear observer cannot be the same, it is recommended to use a point observer instead. | 这个线接收器的起点与终点名称不能相同，建议使用一个点接收器来代替。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Adaptive Error Convergence Curve |  | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Wirebond can not be inserted, need to define the wirebond layer. | 键合线不能插入，需要定义键合线层。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Only faces can be converted into face excitation sources. Please check if points, lines, and faces have been selected. | 仅面可转换为面激励源，请检查是否选择了点、线或面。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Only curves can be selected in reverse. Please check if points, lines, and faces have been selected. | 仅曲线可反选，请检查是否选择了点、线或面。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Only curves can enclose faces. Please check if points, lines, and faces have been selected. | 仅曲线可围成面，请检查是否选择了点、线或面。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Only faces are allowed be thickened. Please check if other points, lines, or bodies have been selected. | 仅面可加厚，请检查是否选择点、线或体。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | This is merging solid faces, cannot be edited. | 合并操作后的面无法编辑。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Calculate The Curve Error | 计算曲线误差 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Calcuate The Curve Error | 计算曲线误差 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Curve Error Comparison | 比较曲线差异 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Failed to add a solid initial value. Please select a solid | 无法为实体添加初始值，请选择一个实体 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Wire Bond cannot be inserted because there are no wire bond layer definitions availabled. | 键合线不能插入，因为没有定义可用的键合线层。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Solid separation failed, unknown reason. | 体分离失败，原因未知。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Face separation failed, unknown reason. | 面分离失败，原因未知。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Cannot copy group and objects at the same time. | 不能同时复制组和物体。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Wire Bond cannot be inserted because there are no wire bond layer definitions availabled. | 键合线不能插入，因为没有定义可用的键合线层。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Wire Bond cannot be inserted because there are no die layer definitions availabled. | 键合线不能插入，因为没有定义可用的裸片层。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The cutting reference face must not be transform and boolean. | 切割参考面不能被变换和布尔操作。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | These objects' boundingbox is not valid. | 这些物体的边界框无效。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Failed to add a solid source. Please select a solid | 添加体源失败，请选择一个体 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | After deleting the snapshot plane will permanently delete the results. This action cannot be undone. Do you want to cont | 删除snapshot面将永久删除结果。此操作无法撤销。是否要继续？ | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Start angle of arc is not allowed to contain Chinese characters | 弧线的起始角不允许包含中文 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | End angle of arc is not allowed to contain Chinese characters. | 弧线的终止角不允许包含中文。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | These vertices cannot create a polygon, please make sure the vertices are on the same plane. | 这些顶点无法创建一个多边形，请确认顶点在同一平面。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Start angle of arc is not allowed to contain Chinese characters. | 弧线的起始角不允许包含中文。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Line receiver selection point error, please select two points. | 线接收器选点错误，请选择两个点。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Failed to create lumped element, the selected face not rectangle. |  | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Failed to create lumped element, the selected face not connect with metal. |  | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The number of user-defined faces is empty, please select a face. | 用户定义的面数量为空，请选择一个面。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The number of user-defined points is empty, please select a point. | 用户自定义点数量为空，请选择一个点。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Repair All Error Objects | 修复所有错误物体 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The selected points cannot form a valid closed polygon face. | 所选择的点不能形成有效的闭合多边形面。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The selected points cannot form a valid closed polygon face. | 所选择的点不能形成有效的闭合多边形面。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The curve name cannot be empty. | 曲线名称不能为空。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Failed to generate curve, unknown reason. | 生成曲线失败，未知原因。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The curve name cannot contain "::part". | 曲线名称不能包含：：部分。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Curve Error List | 曲线误差列表 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | StPlotCurveErrorDialog |  | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Point selection error. Please choose only one point! | 选点错误，请仅选择一个点！ | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Calculate The Curve Error | 计算曲线误差 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Calcuate The Curve Error | 计算曲线误差 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Curve Error Comparison | 比较曲线差异 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The curve name cannot be empty. | 曲线名称不能为空。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The curve name cannot contain "::part". | 曲线名称不能包含”：：部分“。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The selected data cannot be empty, please add at least one data for curve drawing. | 选择的数据不能为空，请至少添加一条数据以进行曲线绘制。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Point selection error. Select only one point from the canvas as the source location! | 选点错误，仅能选择一个点作为激励源位置！ | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The bondwire name is empty. | 键合线名称不能为空。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The page does not have enough width to add the table,please reduce the table's name or close other tables. | 页面宽度不足，无法添加表，请减小表名或关闭其他表。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The plane cannot be perpendicular to the rotation axis. | 平面不能垂直于旋转轴。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | The plane normal vector cannot be less than or equal to 1e-6. | 平面法向向量不能小于等于1e-6 。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Selected face can't split target | 所选面无法分割目标 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Face magnification failure, unknown reason | 面放大失败，未知原因 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_Chinese.ts | Fail to sperate one face to sub-face! | 无法从一个面分割为一个子面！ | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_core_Chinese.ts | Component pin Id is abnormal. (Line id is abnormal) | 组件引脚Id异常。(线的id异常) | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_core_Chinese.ts | The 'Model' name selected for the component does not exist. Please check the existing 'Model' component name or select a | 组件选择的'Model'名称不存在，请检查当前已存在的‘Model’组件名称或重新选择一个'Model'组件。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_core_Chinese.ts | Multiple lines named %1. Please check and modify duplicate node names. | 多条线的节点名%1重复，请检查并修改重复的节点名。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_core_Chinese.ts | Share face error! | 共享面错误！ | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_core_Chinese.ts | faild to assemble coupled solid - fuid model. | 装配固液耦合模式失败。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_core_Chinese.ts | init Bd face faild. | 初始化边界面失败。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_core_Chinese.ts | Conductor number detection error. | 导体编号检测错误。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_core_Chinese.ts | Amplitude of Plane wave should not be zero or nonexistent ! | 平面波的赋值不能为0或不存在！ | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_core_Chinese.ts | The selected field type does not exist and cannot be plotted. | 所选场类型不存在，无法绘制。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_core_Chinese.ts | failed to assemble coupled solid - fluid model. | 装配固液耦合模式失败。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_core_Chinese.ts | init Bd face failed. |  | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_core_Chinese.ts | %1 cannot pass through PEC or conductor. | %1不能穿过完美电导体(PEC)或者导体。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |
| st_core_Chinese.ts | The set boundary conditions cannot eliminate rigid body displacement, resulting in singular matrices and non convergent  | 设置的边界条件无法消除刚体位移，导致矩阵歧义且不收敛。 | 检查当前选择模式和对象类型；面/线/点数量是否满足操作要求，曲面、非共面或非闭合曲线常会导致失败。 |

该分类还有 2 条，完整内容见 `error_message_index.csv`。

## 参数/输入格式
| 文件 | 英文/原文 | 中文提示 | 初筛检查建议 |
| --- | --- | --- | --- |
| st_cad_Chinese.ts | The following variables do not exist: | 以下变量不存在： | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Corner point 1 format error. The correct format is: value1, value2. | 角点1格式错误，正确格式：value1，value2。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Corner point 2 format error. The correct format is: value1, value2. | 角点2格式错误，正确格式：value1，value2。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Length format error. It cannot contain other symbols. Please enter a valid number directly. | 长度格式错误，不能包含其他符号，请直接输入合理的数字。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Width format error. It cannot contain other symbols. Please enter a valid number directly. | 宽度格式错误，不能包含其他符号，请直接输入合理的数字。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Width format error. The width cannot be 0. | 宽度格式错误，宽度不能为0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Corner point 1 format error. The correct format is: x, y. | 角点1格式错误，正确格式：x，y。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Corner point 2 format error. The correct format is: x, y. | 角点2格式错误，正确格式：x，y。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Radius (U-axis direction) format error. It cannot contain other symbols. Please enter a valid number directly. | 半径（U轴方向）格式错误，不能包含其他符号，请直接输入合理的数字。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Radius (V-axis direction) format error. It cannot contain other symbols. Please enter a valid number directly. | 半径（VV轴方向）格式错误，不能包含其他符号，请直接输入合理的数字。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | The number of sides cannot be empty. If it is a variable, please ensure the variable exists. | 边的个数不能为空，若为变量则请确保变量存在。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | The starting point cannot be empty. If it is a variable, please ensure the variable exists. | 起始点不能为空，若为变量则请确保变量存在。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Vertex format error. The correct format is: x, y. | 顶点格式错误，正确格式：x，y。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | U,V,W format is incorrect, please check. | U,V,W 格式错误，请检查。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Ru cannot be empty. If it is a variable, please ensure the variable exists. | Ru不能为空，若为变量则请确保变量存在。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Rv cannot be empty. If it is a variable, please ensure the variable exists. | Rv不能为空，若为变量则请确保变量存在。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Rw cannot be empty. If it is a variable, please ensure the variable exists. | Rw不能为空，若为变量则请确保变量存在。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Corner point format error. The correct format is: x, y, z. | 角点格式错误，正确格式：x,y,z。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Length format error. The correct format is: l, w, h. | 长度格式错误，正确格式：l,w,h。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Lower corner point format error. The correct format is: x, y, z. | 下角点格式错误，正确格式：x,y,z。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Upper corner point format error. The correct format is: x, y, z. | 上角点格式错误，正确格式：x,y,z。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | The bottom radius cannot be empty. If it is a variable, please ensure the variable exists and its value must be greater  | 底面半径不能为空，若为变量则请确保变量存在，且值必须>0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | The top radius cannot be empty. If it is a variable, please ensure the variable exists and its value must be greater tha | 顶面半径不能为空，若为变量则请确保变量存在，且值必须>0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | The height cannot be empty. If it is a variable, please ensure the variable exists and its value must be greater than 0. | 高度不能为空，若为变量则请确保变量存在，且值必须大于0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | The number of sides cannot be empty, if it is a variable, make sure the variable exists and the value must be >0. | 边数不能为空，若为变量则请确保变量存在，且值必须>0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Major radius cannot be empty. If it is a variable, please ensure the variable exists and its value must be greater than  | 外圆半径不能为空，若为变量则请确保变量存在，且值必须>0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Sub radius cannot be empty. If it is a variable, please ensure the variable exists and its value must be greater than 0. | 截面圆半径不能为空，若为变量则请确保变量存在，且值必须>0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Outer major radius cannot be empty. If it is a variable, please ensure the variable exists and its value must be greater | 外椭圆半长轴不能为空，若为变量则请确保变量存在，且值必须>0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Outer minor radius cannot be empty. If it is a variable, please ensure the variable exists and its value must be greater | 外椭圆半短轴不能为空，若为变量则请确保变量存在，且值必须>0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Inner major radius cannot be empty. If it is a variable, please ensure the variable exists and its value must be greater | 内椭圆半长轴不能为空，若为变量则请确保变量存在，且值必须>0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Inner minor radius cannot be empty. If it is a variable, please ensure the variable exists and its value must be greater | 内椭圆半短轴不能为空，若为变量则请确保变量存在，且值必须>0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Angle1 cannot be empty. If it is a variable, please ensure the variable exists and its value must be greater than 0. | 角度1不能为空，若为变量则请确保变量存在，且值必须>=0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | Angle2 cannot be empty. If it is a variable, please ensure the variable exists and its value must be greater than 0. | 角度2不能为空，若为变量则请确保变量存在，且值必须>=0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | '%1'Encountered an error at the minimum parameter. | '%1' 在最小参数处遇到错误。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_cad_Chinese.ts | '%1' Format error. It cannot contain other characters. | '%1' 形式错误。不能包含其他字符。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Data format error! | 数据格式错误！ | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The project name is empty. Please enter a valid name. | 工程名称为空，请输入有效的名称。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The group name is empty, please enter a valid name. | 组名称为空，请输入有效的名称。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | variable Name format error | 变量名称格式错误 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Variable name can't start with "or" | 变量名不能以“or"开头 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Variable name can't start with "and" | 变量名不能以“and"开头 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Variable name can't start with "xor" | 变量名不能以“xor"开头 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The variable can not be evaluated, please check the input. | 该变量无法计算，请检查输入。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Variable name format error | 变量名称格式错误 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Parameter error | 参数错误 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | is empty or variable not exist or format error. | 为空，变量不存在或格式错误。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | is empty or variable not exist or format error. | 为空，变量不存在或格式错误。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | format error. | 格式错误格式为 x, y | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | format error. | 格式错误格式为 x, y, z | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | format error. | 格式错误。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Center format error | 中点格式错误格式 = u, v, w | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Center format error | 中心格式错误，格式为u, v | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The center parameter is wrong. | 中心格式错误，正确的格式应该是(u,v) | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The corner parameter is wrong. | 角参数错误，正确的格式应该为（x,y,z）。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The length parameter is wrong. | 长度格式错误，正确的格式应该是(x,y,z)。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The length parameter is wrong. | 长度参数错误，长度值必须大于0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Lower corner input format is wrong. | 角落参数错误，正确的格式应该为（x,y,z） | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Upper corner input format is wrong. | 角落参数错误，正确的格式应该为（x,y,z） | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The center parameters is wrong. The correct format should be (u, v, w) | 中心格式错误，正确的格式应该是(u,v,w) | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The bottom center parameters is wrong. The correct format should be (u, v, w) | 底部中心格式错误，正确的格式应该是(u,v,w) | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Outer major radius is empty or variable not exist or value is less than 0. | 外主半径为空或者值不存在或者值小于0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Outer minor radius is empty or variable not exist or value is less than 0. | 外次半径为空或者值不存在或者值小于0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Inner major radius is empty or variable not exist or value is less than 0. | 内主半径为空或者值不存在或者值小于0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Inner minor radius is empty or variable not exist or value is less than 0. | 外次半径为空或者值不存在或者值小于0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Center is empty or variable not exist. | 中心值为空或者值不存在。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Height is empty or variable not exist or value is 0. | 中心值为空或者值不存在或者值为0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Angle is empty or variable not exist or value is less than 0. | 角度为空或者值不存在或者值小于0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The origin parameters is wrong. | 初始参量错误，正确的格式应该是(u,v,w) | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The U axis parameters is wrong. | U轴格式错误，正确的格式应该是 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The v axis parameters is wrong. The correct format should be | V轴格式错误，正确的格式应该是 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The number of corner 1 parameters is wrong. | 角1参量值错误，正确格式应该是（数值1，数值2） | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The number of corner 2 parameters is wrong. | 角2参量值错误，正确格式应该是（数值1，数值2） | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The length input format is wrong. | 长度输入格式错误。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The width input format is wrong. | 宽度输入格式错误。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The number of corner 1 parameters is wrong. | 角1参量值错误，正确格式应该是（数值1，数值2） | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The number of corner 2 parameters is wrong. | 角2参量值错误，正确格式应该是（数值1，数值2） | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The center parameter is wrong. | 中心格式错误，正确的格式应该是(u,v,w). | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Radius (in U axis) input format is wrong. | U轴上半径输入格式错误。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Radius (in V axis) input format is wrong. | V轴上半径输入格式错误。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Start angle of arc input format is wrong. | 弧度初始值输入格式错误。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | End angle of arc input format is wrong. | 弧度终止值输入格式错误。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Edges Count is empty or variable not exist. | 棱边数量为空或变量不存在 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Start Point is empty or variable not exist. | 起始点为空或者值不存在。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The vertex parameters is wrong. The correct format should be (value 1, value 2). | 顶点参数错误，正确的格式为 (值1， 值2) | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The center parameters is wrong. The correct format should be (u, v). | 中心格式错误，正确的格式应该是(u,v)。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The radius input format is wrong. | 半径输入格式错误。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The position parameters is wrong.The correct format should be(u, v). | 坐标参量错误，正确的格式应该是(u,v,w)。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Font Size input format is wrong. | 字号输入格式错误。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Cutoff Ratio is not allowed to contain Chinese characters. | 曲线半径不能输入中文 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Curve Radius is not allowed to contain Chinese characters. | 曲线半径不能输入中文 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Width input format is wrong. | 宽度格式输入错误。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Cutoff Ratio input format is wrong. | 截止值输入格式错误 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Curve Radius input format is wrong. | 曲线半径输入格式错误。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The center parameters is wrong.The correct format should be(u, v). | 中心格式错误，正确的格式应该是(u,v,w)。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | input format is wrong. | 格式输入错误。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The vertex parameter is wrong. | 顶点参量值错误，正确格式应该是（数值1，数值2）。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Ru is empty or variable not exist | Ru为空或变量不存在 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Rv is empty or variable not exist | Rv为空或变量不存在 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Rw is empty or variable not exist | Rw为空或变量不存在 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Bottom radius is empty or variable not exist or value <= 0 | 底半径为空，或变量不存在，或值<= 0 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Top radius is empty or variable not exist or value < 0 | 顶部半径为空，或变量不存在，或值<0 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Height is empty or variable not exist or value = 0 | 高度为空，或变量不存在/值0。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Corn edge is empty or variable not exist or value < 0 | 圆锥边缘为空或者变量不存在/值小于0 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Major radius is empty or variable not exist or value <= 0 | 半长轴为空，或变量不存在，或值<= 0 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Sub radius is empty or variable not exist or value <= 0 | 半短轴为空，或变量不存在，或值<= 0 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Variable %1 does not exist. | 变量%1不存在。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The data format must be consistent. | 数据格式不一致，请检查。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | [%1] Format error. | [%1] 格式错误。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The name is empty, please re-enter it. | 名称为空，请重新输入。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Height is empty or variable not exist. | 高度值为空或者值不存在。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The integration line's positive pole is empty or the format is incorrect, please input the coordinates of a point as the | 积分线正极为空或者格式错误，请输入适当的点作为正极。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The integration line's negative pole is empty or the format is incorrect, please input the coordinates of a point as the | 积分线负极为空或者格式错误，请输入适当的点作为负极。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | variables are not allowed to be pasted into the same project | 变量不允许被粘贴到同个项目内 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | create variable error | 创建变量错误 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Please enter a valid category label. Category labels cannot contain Spaces. | 请输入有效的分类标签，分类标签不能包含空格。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Please enter a valid category label, which cannot contain any of the following symbols (~#; ,//\$" ? ). | 请输入有效的分类标签，分类标签不能包含 (~#; ,//\$" ? )。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The minimum frequency cannot be empty. Please enter the minimum frequency. | 频率最小值不能为空，请输入频率最小值 。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | Frequency minimums cannot be converted to numerical values. | 频率最小值不能转化为数值。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The maximum frequency cannot be empty. Please enter the maximum frequency. | 频率最大值不能为空，请输入频率最大值 。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |
| st_Chinese.ts | The maximum frequency cannot be converted to a numerical value. | 频率最大值不能转化为数值。 | 按提示检查输入格式，例如坐标 `(u,v,w)`、数值范围、变量名和单位；不要在非单位界面额外带单位。 |

该分类还有 292 条，完整内容见 `error_message_index.csv`。

## 文件/导入导出
| 文件 | 英文/原文 | 中文提示 | 初筛检查建议 |
| --- | --- | --- | --- |
| st_Chinese.ts | snp file suffix error | snp文件后缀错误 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | File save failed. | 文件保存失败。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | The file is empty! | 文件为空 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Please check whether the project path already exists. | 请检查工程路径是否已存在。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | The compressed file path is empty, please select a new path. | 压缩文件路径不存在。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | There is no path curve, please check the number of cuves. | 无路径曲线，请检查曲线数量。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | The selected curves can't build a continuous path, quit. | 所选曲线无法构建连续路径，退出操作。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Edges Count is not allowed to contain Chinese characters. | 棱边数量不能保存中文 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | File Open Fail | 文件打开失败 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | The S-parameter result does not exist. Please check whether the S-parameter result file is deleted or no S-parameter res | S参数结果不存在，请检查S参数结果文件是否被删除，或未生成S参数结果。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | File does not exist. | 文件不存在。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Failed to create json file! | 无法创建json文件！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Project file cannot be written, the save path may not exist. | 工程文件无法写入，保存路径可能不存在。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Couldn't open json tsp file! | 无法打开json tsp文件！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Couldn't open xml tsp file! | 无法打开xml tsp文件！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Fail to load project file! please check file format. | 无法加载工程文档！请检查文件形式。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Couldn't get physic type info in file content! | 无法在文件内容中获得物理类型的信息！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Project file cannot be written, the file may be read-only. | 工程文件无法写入，文件可能为只读。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Content is invalid, missing project node! | 内容无效，丢失工程文件节点！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Content is invalid, please check file first! | 内容无效，请先检查文件！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Fail to create source backup file! | 创建源备份文件失败！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Fail to create tdr file,please check! | 创建tdr文件失败，请检查！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Couldn't open xml file! | 无法打开xml文件 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | S parameter file path is empty. | S参数文件路径为空。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | S parameter file path is empty. | S参数文件路径为空。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | The file path is incorrect! | 生成的网表路径不存在！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | The curves can't build a continuous path, quit. | 曲线不能创建一个连续路径，退出。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | File format error. | 文件格式错误。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Failed to read the excitation file. | 读取激励文件失败。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | The file name does not exist, please set the file name. | 文件名不存在，请设置文件名。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | The file suffix does not exist, please set the file suffix. | 文件后缀不存在，请设置文件后缀。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | The file path does not exist, please set the file path. | 文件路径不存在，请设置文件路径。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | The file directory path does not exist, please set the file directory path. | 文件目录路径不存在，请设置文件目录路径。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Far-field file does not exist. | 远场结果不存在。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | The FFmpeg path does not exist, please set it first. | FFmpeg路径不存在，请先设置。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | The FFmpeg executable does not exist, please check. | FFmpeg可执行文件不存在，请检查。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | S-parameters not found. The reason may be: the S-parameter file has been deleted or S-parameter results have not been ge | S参数不存在。原因可能是：S参数文件被删除或S参数结果未产生。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | File format error. | 文件格式错误。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Failed to save file. | 文件保存失败。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Failed to open file. | 打开文件失败。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | wrong layer tech file. | 层工艺文件错误。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | wrong die tech file. | 芯片工艺文件错误。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | wrong layer tech file. | 层工艺文件错误。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | wrong die tech file. | 芯片工艺文件错误。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | wrong layer tech file. | 层工艺文件错误。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | wrong die tech file. | 芯片工艺文件错误。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | wrong layer tech file. | 层工艺文件错误。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | wrong die tech file. | 芯片工艺文件错误。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Please input a valid data file name. | 输入的文件名不能为空。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Failed to read tgz file! | 无法读取tgz文件！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Failed to cover file! | 无法覆盖文件！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Wire Bond cannot be inserted because there are no wire bond profile definitions availabled. | 键合线不能插入，因为没有可用的引线键合配置文件定义。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | File opening failure. | 文件打开失败。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | The pad profile in row %1 is invalid. | %1中的焊盘配置文件无效。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Some layers did not find their corresponding layers.Please check tech file. | 一些层没有找到相应的层，请检查技术文件。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | File not exists, it has been deleted、 renamed or moved! | 文件不存在，它已被删除、重命名或移动！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | fail to copy the data foler from installed path to user home path! | 安装文件夹的数据文件复制到用户文件夹失败！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | the sourceFile does not exist! | 该激励源的文件不存在！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Unable to copy file! | 文件不可复制！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | copy file doesn't exist! | 复制文件不存在！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Edges Count is not allowed to contain Chinese characters. | 棱边数量不能保存中文。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | File save failed. | 文件保存失败。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Please check whether the project path already exists. | 请检查工程路径是否已存在。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | The file format is incorrect. Please refer to the template file. | 文件格式错误，请参考模板文件。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | File opening failed! | 文件打开失败！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | File does not exist. | 文件不存在。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | User defined pulse,file format error. | 使用定义脉冲，文件格式错误。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | S parameter file path is empty. | S参数文件路径为空。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | FFmepeg path does not exist, please reset it. | FFmepeg 路径不存在，请重新设置。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Subcircuit parsing error. Please check if the format of the subcircuits in the file is correct, or if the file contains  | 子电路解析出错。请检查文件中的子电路的格式是否正确，或者文件中包含多个未引用的子电路。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Failed to create json file! | 无法创建json文件！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Couldn't open json tsp file! | 无法打开json tsp文件！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Couldn't open xml tsp file! | 无法打开xml tsp文件！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Fail to load project file! please check file format. | 无法加载工程文档！请检查文件形式。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Couldn't get physic type info in file content! | 无法在文件内容中获得物理类型的信息！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Project file cannot be written, the file may be read-only. | 无法写入项目文件，该文件可能是只读的。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Content is invalid, missing project node! | 内容无效，丢失工程文件节点！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Content is invalid, please check file first! | 内容无效，请先检查文件！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Fail to create source backup file! | 创建源备份文件失败！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Fail to create tdr file,please check! | 创建tdr文件失败，请检查！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Circuit projects with higher version cannot be opened. Please install the lastest version. | 无法打开高版本的电路文件，请安装最新版本。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Auto save error, please reslove the problem, then turn on the Auto save again. | 自动保存错误，请解决问题，然后重新打开自动保存。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Project file cannot be written, the save path may not exist. | 无法写入项目文件，保存路径可能不存在。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | AutoSave Time is format error. | 自动保存时间格式错误。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | File not exists, it has been deleted、 renamed or moved! | 文件不存在，它已被删除、重命名或移动！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | fail to copy the data foler from installed path to user home path! | 安装文件夹的数据文件复制到用户文件夹失败！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | the sourceFile does not exist! | 该激励源的文件不存在！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | Unable to copy file! | 文件不可复制！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | copy file doesn't exist! | 复制文件不存在！ | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_Chinese.ts | The FFmpeg path does not exist, please set it first. | FFmpeg路径不存在，请重新设置。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_core_Chinese.ts | Snp file parse error. | SNP文件解析失败。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_core_Chinese.ts | Copy subcircuit file error from [%1] to [%2] . | 电路从[%1]复制到[%2],复制失败。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_core_Chinese.ts | Failed to retrieve SNP file, the file at that path does not exist. | 获取所有snp路径，检查后以下文件不存在。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_core_Chinese.ts | Far-field file does not exist. | 远场结果文件不存在。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_core_Chinese.ts | sFdFarFile open failed. |  | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_mesher_Chinese.ts | Failed to parse file parameters. | 解析文件参数失败。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |
| st_mesher_Chinese.ts | Failed to load file. | 加载文件失败。 | 检查文件路径、后缀、权限、文件是否为空或被占用；导入数据时检查格式与分隔符。 |

## 材料
| 文件 | 英文/原文 | 中文提示 | 初筛检查建议 |
| --- | --- | --- | --- |
| st_Chinese.ts | Grouping based on material failed, maybe the child node does not belong to root node | 按材料分组失败，子节点可能不属于根节点 | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_Chinese.ts | materials are not allowed to be pasted into the same project | 材料不允许被粘贴到同个项目内 | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_Chinese.ts | create material error | 创建材料错误 | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_Chinese.ts | Failed to fit the dispersion material. | 拟合色散材料失败。 | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_Chinese.ts | The PEC material can not be the material of impedance boundary condition! | 理想电导体材料不能作为阻抗边界条件的材料！ | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_Chinese.ts | The PMC material can not be the material of impedance boundary condition! | 完美磁导体材料不能作为阻抗边界条件的材料！ | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_Chinese.ts | The PEC material can not be the material of surface current boundary condition! | 理想电导体材料不能作为表面电流边界条件的材料！ | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_Chinese.ts | The PMC material can not be the material of surface current boundary condition! | 理想磁导体材料不能作为表面电流边界条件的材料！ | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_Chinese.ts | The material name is empty. Please input a material name. | 材料名称为空，请输入材料名。 | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_Chinese.ts | Elastic material density may be wrong! | 声波材料密度错误！ | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_Chinese.ts | Acoustic material is wrong! Vp is too small! | 声波材料错误！Vp太小了！ | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_Chinese.ts | Elastic material is wrong! Vp is too small! | 弹性力学材料错误！Vp太小了！ | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_Chinese.ts | The material name is empty. Please input a material name. | 材料名称为空，请输入材料名。 | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_Chinese.ts | The PEC material can not be the material of impedance boundary condition! | 理想电导体材料不能作为阻抗边界条件的材料！ | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_Chinese.ts | The PMC material can not be the material of impedance boundary condition! | 完美磁导体材料不能作为阻抗边界条件的材料！ | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_Chinese.ts | The PEC material can not be the material of surface current boundary condition! | 理想电导体材料不能作为表面电流边界条件的材料！ | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_Chinese.ts | The PMC material can not be the material of surface current boundary condition! | 理想磁导体材料不能作为表面电流边界条件的材料！ | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_Chinese.ts | Elastic material Wrong! Vp is too small! |  | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_Chinese.ts | Elastic material Wrong! Vp < 1.155 * VS! |  | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_core_Chinese.ts | Solid %1: material is invalid. | 体%1：材料是无效的。 | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_core_Chinese.ts | Internal error, the material of the solid is non-conductive, but it is treated as an IBC body. | 内部错误，物体的材料是非导体，但被当作阻抗边界(IBC)体。 | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_core_Chinese.ts | Face %1: material is invalid. | 面%1：材料是无效的。 | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_core_Chinese.ts | Curve %1: material is invalid. | 线%1：材料是无效的。 | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_core_Chinese.ts | Background material cannot be PEC or PMC. | 背景材料不能是完美电导体或者完美磁导体。 | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |
| st_core_Chinese.ts | Material validation failed, using pec material in Electric current field | 材料验证失败，在电流场内使用PEC材料 | 检查材料名称是否重复、材料模块是否支持当前物理场、参数格式和损耗设置是否正确。 |

## 端口/激励
| 文件 | 英文/原文 | 中文提示 | 初筛检查建议 |
| --- | --- | --- | --- |
| st_Chinese.ts | The selected information is empty. Unable to create a lumped element. | 所选信息为空，不能创建集总元件。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Curved face cannot be used to create a lumped element. | 曲线无法用于创建集总元件。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Unable to create wave port during simulation. | 仿真过程中不允许创建波端口。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to create wave port, the selected face is not a planar face. | 创建波端口失败，所选面不是平面。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to create wave port, the selected faces are not in the same plane. | 创建波端口失败，所选面不在同一平面。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The wave port is disabled and the mode cannot be viewed! | 波端口已被禁用，模式无法查看！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to parse the point source file, please re-import. | 解析点源文件失败，请重新导入。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The selected information is empty. Unable to create a lumped port. | 所选信息为空，无法创建集成端口。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The selected unable to create a lumped port. | 所选对象不能创建集总端口。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The selected unable to create a lumped element. | 所选对象不能创建集总元件。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to create lumped port, the selected face is not a planar face. | 创建集总元件失败，所选面不在同一平面。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to create lumped element, the selected face is not a planar face. | 创建集总元件失败，所选面非平面。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to create lumped port, the selected faces are not in the same plane. | 创建集总端口失败，所选面不在同一平面。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to create lumped element, the selected faces are not in the same plane. | 创建集总元件失败，所选面不在同一平面。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Curved face cannot be used to create a lumped port. | 所选曲面无法创建集总端口。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Selections can't create lumped port! Lumped port face must be rect or ring. | 所有几何不能创建集总端口，端口必须是矩形或圆环。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Create Face Lumped Port | 不能创建集总面端口 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The selected information is empty. Unable to create a wave port. | 所选信息为空。不能创建波端口。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Selections can't create wave port! | 选择的面不能创建波端口！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Selections can't create lumped port! | 所选对象无法创建集总端口！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Selections can't create lumped element! | 所选对象无法创建集总元件！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Export figure failed. Path: %1.(%2) | 导出图形失败：%1.(%2) | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Import failed, material already exists. | 导入失败，材料已存在。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Can't split port face. | 无法切割端口面。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Restore failed, please check if the objects are external import files. | 恢复失败，请检查模型是否为外部导入。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Cannot export to column format, ensure all data series share the same X-axis array. | 无法导出为列格式，请确保所有的数据序列共享相同的X轴数组。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Imported data has been deleted. | 导入的数据已被删除，请检查。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to read port simulation results. Possible reasons: Port simulation data was deleted or not generated. | 读取端口仿真结果失败，原因可能是：端口仿真数据被删除，或未生成端口仿真数据。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to read the imported file, please check the file format. | 导入文件读取失败，请检查文件格式。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Exporting S parameter failed! S parameter size is 0, unable to export. | S参数导出失败！S参数数据为0，无法导出。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to import mesh: | 导入网格错误： | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Wave port meshing failed, please check the port. | 波端口网格划分失败，请检查端口。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The data in the figure is too small to export | 图片数据过小，无法导出 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The format of the imported receiver file is incorrect. | 导入的接收器文件格式错误。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to save imported model data. | 保存导入模型数据失败。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Fail to open import file pcb! | 无法打开导入的pcb文件！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Missing key of ports,please check! | 缺少端口的关键字，请检查！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Missing array of ports,please check! | 缺少端口数组，请检查！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Missing ports of signal net,please check! | 信号网的端口丢失，请检查！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | That is not one xy value in signal net port,please check! | 在信号网络端口中没有一个xy值，请检查！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Missing the net [GND] in ports or in objects, please check! | 在端口或对象中缺少GND，请检查！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Missing key of layer in port,please check! | 端口中缺少层的关键字，请检查！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Missing key of nets in port,please check! | 端口中缺少网络的关键字，请检查！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Missing key of name in port, please check! | 端口中缺少名字的关键字，请检查！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Port label is empty, idenify ports by label failed | 端口标签为空，按标签识别端口失败 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | There are identical port labels, idenify ports by label failed | 存在重复的端口标签，按标签识别端口失败 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Importing %1 mesh failed. | 导入%1网格失败 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Cannot export to column format, ensure all data series share the same X-axis array. | 无法按列格式导出，请确保所有数据序列共享相同的X轴数组。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Not support or parameter error | 不支持或参数错误 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Import file reading failed, please check the file format. | 导入文件读取失败，请检查文件格式。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Export failed! Please check if the file path has write permissions. | 导出失败！请检查该文件路径是否有写入权限。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Export snp error | 导出snp错误 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Port name is empty. | 端口名称为空。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The port name cannot be empty. | 端口的名称不能为空。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to read the imported file, please check the file format. | 导入文件读取失败，请检查文件格式。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Cannot export to column format, ensure all data series share the same X-axis array. | 无法导出为列格式，请确保所有数据系列共享相同的X轴数组。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Port name is empty. | 端口名称为空。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The lumped port name cannot be empty. Please enter a name. | 集总端口名称不能为空，请输入名称。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to read the imported file, please check the file format. | 导入文件读取失败，请检查文件格式。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Component is in use by port, cannot be deleted. | 元件正在被端口使用，无法删除。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The pin port layer can not be same with reference plane. | 引脚端口层不能与参考平面相同。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The number of ports in differential net %1 is not one for each, making it impossible to create differential pair ports. | 差分网络%1中的端口数量不是每个端口一个，因此无法创建差分对端口。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | This pin is used by port, can not be deleted. | 该引脚被端口使用，无法删除。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | created port, can not create agian. | 创建端口，不能重复创建。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to parse the point source file, please re-import. | 解析点源文件失败，请重新导入。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The selected information is empty. Unable to create a lumped port. | 所选信息为空，无法创建集总端口。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The selected information is empty. Unable to create a lumped element. | 所选信息为空，不能创建集总元件。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to create lumped port, the selected face is not a planar face. | 创建集总元件失败，所选面不在同一平面。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to create lumped element, the selected face is not a planar face. | 创建集总元件失败，所选面非平面。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to create lumped port, the selected faces are not in the same plane. | 创建集总端口失败，所选面不在同一平面。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to create lumped element, the selected faces are not in the same plane. | 创建集总元件失败，所选面不在同一平面。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The selected unable to create a lumped port. | 所选对象不能创建集总端口。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The selected unable to create a lumped element. | 所选对象不能创建集总元件。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Curved face cannot be used to create a lumped port. | 所选曲面无法创建集总端口。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Curved face cannot be used to create a lumped element. | 曲线无法用于创建集总元件。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Selections can't create lumped port! | 所选对象无法创建集总端口！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Selections can't create lumped element! | 所选对象无法创建集总元件！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The selected information is empty. Unable to create a bridge port. |  | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to create bridge port, the selected face not rectangle. |  | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to create bridge port, the selected face not connect with metal. |  | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Unable to create wave port during simulation. | 仿真过程中不允许创建波端口。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to create wave port, the selected face is not a planar face. | 创建波端口失败，所选面不是平面。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to create wave port, the selected faces are not in the same plane. | 创建波端口失败，所选面不在同一平面。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The selected information is empty. Unable to create a wave port. | 所选信息为空，不能创建波端口。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Selections can't create wave port! | 选择的面不能创建波端口！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The port label cannot be empty, because results identify ports is by port label. | 端口标签不能为空，因为结果通过端口标签识别端口。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | There are identical port labels, idenify ports by label failed. |  | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to create bridge port, the selected face cannot be metallic. | 创建桥端口失败，所选面的材料不能为金属。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to create lumped element, the selected face cannot be metallic. | 创建集总端口失败，所选面的材料不能为金属。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The component port type can not be changed. | 无法更改元件端口类型。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Pin port name is empty, please give a pin port name. | 引脚端口名字为空，请输入名称。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | No polar data can be exported! | 无法导出极坐标数据！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The port simulation result does not exist. Check whether the port simulation result is cleared or not generated. | 端口仿真结果数据不存在，请检查端口仿真结果是否被清除，或未生成端口仿真结果。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | does not exist. Check whether the port simulation result is cleared or not generated. | 请勿关闭，请检查端口仿真结果是否被清除，或未生成端口仿真结果。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The port simulation result does not exist. The possible cause is that the port simulation result is cleared or not gener | 端口仿真结果数据不存在，原因可能是：端口仿真结果被清除，或未生成端口仿真结果。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Port result does not exist, port data is missing or not generated. | 端口结果不存在，可能是数据丢失或没有生成。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Port name cannot be empty. | 端口名称不能为空。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Lumped port does not exist! | 集总端口不存在！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Wave port does not exist! | 波端口不存在！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | No smith data can be exported! | 无法导出史密斯圆图数据！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | This is an imported solid, cannot be edited. | 导入的面无法编辑。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Failed to save imported model data. | 保存导入模型数据失败。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Project file version error, application support | 工程文件版本错误，应用程序支持 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Fail to open import file pcb! | 无法打开导入的pcb文件！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Missing key of ports,please check! | 缺少端口的关键字，请检查！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Missing array of ports,please check! | 缺少端口数组，请检查！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Missing ports of signal net,please check! | 信号网的端口丢失，请检查！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | That is not one xy value in signal net port,please check! | 在信号网络端口中没有一个xy值，请检查！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Missing the net [GND] in ports or in objects, please check! | 在端口或对象中缺少GND，请检查！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Missing key of layer in port,please check! | 端口中缺少层的关键字，请检查！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Missing key of nets in port,please check! | 端口中缺少网络的关键字，请检查！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Missing key of name in port, please check! | 端口中缺少名字的关键字，请检查！ | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Export failed! Please check if the file path has write permissions. | 导出失败！请检查该文件路径是否有写入权限。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The coordinate input for the wave port surface is incorrect. Please create a rectangle parallel to the xoy/yoz/xoz plane | 波端口面的坐标输入错误，请建立平行于xoy/yoz/xoz平面的矩形。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | The port label cannot be empty, because results identify ports is by port label. | 端口标签不能为空，因为结果通过端口标签识别端口。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_Chinese.ts | Import failed, material already exists. | 导入失败，材料已存在。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_core_Chinese.ts | Subcircuit analysis failed. The file contains multiple sub circuits or no sub circuits, and the software only supports i | 子电路解析失败。文件中包含多个子电路或无子电路，软件只支持识别唯一对应的子电路。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_core_Chinese.ts | Lumped port cannot pass through PEC or conductor. | 集总端口不能穿过完美电导体(PEC)或者导体。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_core_Chinese.ts | Lumped element cannot pass through PEC or conductor. | 集总元件不能穿过完美电导体(PEC)或者导体。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |
| st_core_Chinese.ts | Lumped element validation failed. | 集总元件校验失败。 | 检查端口创建时的选择对象、端口面是否为平面、是否贴合 Domain、导体数量/电势设置是否变化；必要时重新创建端口或重新运行波端口。 |

该分类还有 13 条，完整内容见 `error_message_index.csv`。

## 网格
| 文件 | 英文/原文 | 中文提示 | 初筛检查建议 |
| --- | --- | --- | --- |
| st_cad_Chinese.ts | Mesh Fail | 网格化失败 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_Chinese.ts | Cannot paste while simulating or meshing. | 正在仿真或者剖分网格中，不能粘贴。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_Chinese.ts | Cannot paste while simulating or meshing. | 正在仿真或者剖分网格中，不能粘贴。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_Chinese.ts | Cannot paste while simulating or meshing. | 正在仿真或者剖分网格中，不能粘贴。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_Chinese.ts | Cannot paste while simulating or meshing. | 正在仿真或者剖分网格中，不能粘贴。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_Chinese.ts | Cannot paste while simulating or meshing. | 正在仿真或者剖分网格中，不能粘贴。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_Chinese.ts | (If the size <= 0, it will not be used) | (若网格尺寸<=0 将被视为无效） | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_Chinese.ts | Cannot paste while simulating or meshing. | 正在仿真或者剖分网格中，不能粘贴。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_core_Chinese.ts | Mesh type is invalid. | 网格类型无效。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_core_Chinese.ts | the Jacobian matrix is singular. | 雅可比矩阵奇异, 请检查网格质量。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_core_Chinese.ts | Unpaired mesh cannot set in fluid material. | 未配对的网格不能设置在流体材料内。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_mesher_Chinese.ts | Parameters validation failed before meshing. | 网格剖分前参数校验失败。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_mesher_Chinese.ts | Mesh failed. | 网格剖分失败. | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_mesher_Chinese.ts | Failed to generating volume mesh. | 创建体网格失败。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_mesher_Chinese.ts | Failed to generate volume mesh. | 创建体网格失败。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_mesher_Chinese.ts | Warning: There is a pathological tetrahedral grid. | 警告：存在病态四面体网格。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_mesher_Chinese.ts | -------- Warnings in grid profiling -------- | --------网格剖分中的警告信息-------- | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_mesher_Chinese.ts | Warning, the determinant of the mesh is less than 1e-9. | 警告，网格的行列式小于1e-9。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_mesher_Chinese.ts | Failed to generate prism mesh. | 创建棱柱网格失败。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_mesher_Chinese.ts | Mesh post-process failed. | 网格后处理失败. | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_mesher_Chinese.ts | Failed in Generating Prism Mesh. | 创建棱柱网格失败。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_mesher_Chinese.ts | Failed to Generating Tetrahedron Mesh. | 创建四面体网格失败。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_mesher_Chinese.ts | Failed to Generating Prism Mesh | 创建棱柱网格失败 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_mesher_Chinese.ts | Failed to Generate Tetrahedron Mesh | 创建四面体网格失败 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_mesher_Chinese.ts | xxx Fail in generating hexahedron mesh. | xxx生成六面体网格失败。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_mesher_Chinese.ts | Could not recover boundary, try to cancel multiple pass meshing. | 不能复原边界，尝试减少网格剖分次数。 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |
| st_simulator_Chinese.ts | error:The grid type and the solver type are different | 错误：网格类型和求解器不一致 | 检查网格类型、求解器是否匹配，查看病态网格；适当调整 3D 网格、波端口网格或自适应网格参数。 |

## 连接/许可
| 文件 | 英文/原文 | 中文提示 | 初筛检查建议 |
| --- | --- | --- | --- |
| st_Chinese.ts | Connection failed, please check. | 连接失败，请检查。 | 检查许可证服务、网络连接、软件配置路径和服务是否运行。 |
