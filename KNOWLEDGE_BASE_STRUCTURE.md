# WavEDA RAG 知识库完整结构

## 总览

```
waveda_rag/
│
├── knowledge_base/          ← 知识库源文件（Markdown）
├── wavEDA_docs/helpHtml/    ← 官方 HTML 帮助 + 截图（GUI 渲染用）
├── data/index/              ← 检索索引（chunks.json + vectors.npy）
├── config/                  ← 配置文件
├── scripts/                 ← 工具脚本
├── src/raggg/               ← RAG 引擎源码
├── app/                     ← 桌面应用入口
└── runtime/                 ← 便携 Python 运行时
```

---

## 一、knowledge_base/ — 知识库源文件

> **167 个 Markdown 文件，覆盖 4974 个检索 chunk**

```
knowledge_base/
│
├── 01_team_tutorials/              ← 团队自编教程（11 个文件）
│   │   用途：团队原创的 WavEDA 操作教程，适合新手入门
│   │   来源：原 knowledge_base/ 顶层文件 + tutorials/ 子目录
│   │
│   ├── 00_软件概述.md              功能对比、算法介绍、网格参数、文件格式
│   ├── 01_快速入门.md              从建模到后处理的完整工作流
│   ├── 03_常见问题FAQ.md           网格失败、算法选择、S参数导出、与COMSOL对比
│   ├── 04_错误排查指南.md          常见错误的诊断与修复
│   │
│   └── tutorials/
│       ├── 02_电磁模块/             （5 个文件）
│       │   ├── 01_端口设置.md       集总端口、波端口、模式分析、S参数导出
│       │   ├── 02_激励源配置.md     点源、平面波、集总/波端口激励配置
│       │   ├── 03_边界条件.md       PML、阻抗、周期、开放边界、PEC/PMC
│       │   ├── 04_求解器设置.md     频域/时域求解器、扫频方式、收敛控制
│       │   └── 05_结果后处理.md     S参数查看、远场、快照、场图导出
│       │
│       └── 03_案例/                 （2 个文件）
│           ├── 01_微环谐振器仿真.md 光学微环谐振器的完整仿真流程
│           └── 02_Y分支波导仿真.md   Y分支波导的完整仿真流程
│
├── 02_software_manual/             ← 软件功能手册（98 个文件）
│   │   用途：官方帮助文档提取，覆盖 WavEDA 全部功能
│   │   来源：原 wavEDA_docs/extracted_pages/ + merged KB
│   │
│   ├── Introduction.md             WavEDA 软件介绍（混合有限元、区域分解、降阶）
│   ├── Invalid_Doc.md              无效文档索引（占位页）
│   │
│   ├── EM_Project/                 电磁工程模块（13 个文件）
│   │   ├── Boundary.md             边界条件设置（ABC/PML/PEC/PMC/阻抗/周期）
│   │   ├── Create_A_New_RCLD.md    创建 RCLD（集总元件）
│   │   ├── EM_Results.md           电磁仿真结果查看
│   │   ├── Far_field.md            远场计算结果
│   │   ├── Field_Result.md         场分布结果查看
│   │   ├── HotKey.md               快捷键汇总
│   │   ├── Snapshot.md             场快照设置与查看
│   │   ├── Sweep_Along_Axis.md     沿轴扫参
│   │   ├── Sweep_Along_Path.md     沿路径扫参
│   │   ├── Tree_Curves.md          曲线树管理
│   │   ├── Tree_Faces.md           面树管理
│   │   ├── Tree_Solids.md          体树管理
│   │   └── Observer/
│   │       ├── Observer.md         观测器概述
│   │       ├── Create_Line_Observer.md  线观测器
│   │       └── Create_Point_Observer.md 点观测器
│   │
│   ├── File/                       文件菜单（3 个文件）
│   │   ├── File.md                 文件操作（新建/打开/保存/导入/导出）
│   │   ├── Homepage.md             主页/欢迎页
│   │   └── Options.md              全局选项设置
│   │
│   ├── Mesh/                       网格模块（7 个文件）
│   │   ├── 3D_Mesh.md              3D 网格划分
│   │   ├── Adaptive_Mesh.md        自适应网格迭代
│   │   ├── Import_Mesh.md          导入网格
│   │   ├── Import_Adaptive_Mesh.md 导入自适应网格
│   │   ├── Mesh.md                 网格总览
│   │   ├── Show_Mesh.md            网格显示控制
│   │   └── Waveport_Mesh.md        波端口网格
│   │
│   ├── Modeling/                   建模模块（64 个文件）
│   │   ├── Modeling.md             建模总览
│   │   ├── Import_Export.md        模型导入导出（STEP/IGES/STL 等）
│   │   ├── LCS.md                  局部坐标系设置
│   │   │
│   │   ├── Bkg_Mat/                背景与材料（4 个文件）
│   │   │   ├── Background.md       背景介质设置（默认空气）
│   │   │   ├── Materials.md        材料库（导体/介质/磁介质）
│   │   │   ├── Dielectric_Dispersion.md  电色散材料模型
│   │   │   └── Magnetic_Dispersion.md    磁色散材料模型
│   │   │
│   │   ├── Create_3D_Geometry/     3D 几何体（11 个文件）
│   │   │   ├── Box.md              长方体
│   │   │   ├── Sphere.md           球体
│   │   │   ├── Cylinder.md         圆柱体
│   │   │   ├── Cone.md             圆锥体
│   │   │   ├── Prism.md            棱柱体
│   │   │   ├── Torus.md            圆环体
│   │   │   ├── Bondwire.md         键合线
│   │   │   ├── Archimedean_Spiral.md  阿基米德螺旋线
│   │   │   ├── Toroidal_Spiral.md  环形螺旋
│   │   │   ├── Solid_Intersection.md  实体布尔交集
│   │   │   └── History_Tree_Solid.md  几何历史树
│   │   │
│   │   ├── Create_Curve/           曲线创建（5 个文件）
│   │   │   ├── Line.md             直线
│   │   │   ├── Circular_Arc.md     圆弧
│   │   │   ├── Polyline.md         多段线
│   │   │   ├── Parametric_Curve.md  参数曲线
│   │   │   └── History_Tree_Curve.md 曲线历史树
│   │   │
│   │   ├── Create_Face/            面创建（8 个文件）
│   │   │   ├── Rectangle.md        矩形面
│   │   │   ├── Polygon.md          多边形面
│   │   │   ├── Edit_Polygon.md     编辑多边形
│   │   │   ├── Ellipse.md          椭圆面
│   │   │   ├── Cone_Face.md        锥面
│   │   │   ├── Parametric_Face.md  参数化面
│   │   │   ├── Semiellipsoid_Face.md 半椭球面
│   │   │   └── History_Tree_Face.md  面历史树
│   │   │
│   │   ├── Design/                 设计设置（4 个文件）
│   │   │   ├── Domain.md           计算区域/Domain 设置
│   │   │   ├── Frequency.md        频率设置（单频点/扫频范围）
│   │   │   ├── Solver.md           求解器设置（FEM/扫频方式）
│   │   │   └── Unit.md             单位制设置
│   │   │
│   │   ├── Model_Editing/          模型编辑（16 个文件）
│   │   │   ├── Boolean.md          布尔运算（并/交/差）
│   │   │   ├── Extrusion.md        拉伸
│   │   │   ├── Rotate.md           旋转
│   │   │   ├── Mirror.md           镜像
│   │   │   ├── Scale.md            缩放
│   │   │   ├── Translate.md        平移
│   │   │   ├── Align.md            对齐
│   │   │   ├── Array_Copy.md       阵列复制
│   │   │   ├── Blend_Edges.md      倒圆角边
│   │   │   ├── Chamfer_Edges.md    倒角边
│   │   │   ├── Shell.md            抽壳
│   │   │   ├── Split.md            分割
│   │   │   ├── Enlarge.md          扩大/偏移
│   │   │   ├── Face_Thicken.md     面加厚
│   │   │   ├── Extended_Operations.md  扩展操作
│   │   │   └── Move_Face_To_Modify_Solid.md  面移动修改体
│   │   │
│   │   └── Stimulate/              激励源（6 个文件）
│   │       ├── Lumped_Port.md      集总端口
│   │       ├── Wave_Port.md        波端口
│   │       ├── Plane_Wave.md       平面波激励
│   │       ├── Create_Point_Source.md  点源
│   │       ├── Integration_Line.md  积分线（用于端口 S 参数提取）
│   │       └── Multi_Conductors.md  多导体设置
│   │
│   ├── Post_Processing/            后处理（3 个文件）
│   │   ├── Post_Processing.md      后处理总览
│   │   ├── New_Port.md             新建端口结果
│   │   └── New_Observers.md        新建观测器结果
│   │
│   ├── Simulation/                 仿真（2 个文件）
│   │   ├── Simulation.md           仿真控制（运行/停止/监控）
│   │   └── Parameter_Sweep.md      参数扫描
│   │
│   ├── Tool/                       工具（7 个文件）
│   │   ├── Tool.md                 工具总览
│   │   ├── Design_Setting.md       设计设置工具
│   │   ├── Variables.md            变量管理
│   │   ├── Details_logs.md         详细日志
│   │   ├── Export_Figure.md        导出图片
│   │   ├── Export_Snp.md           导出 S 参数（SnP 格式）
│   │   └── Vector_Fitting.md       矢量拟合工具
│   │
│   └── View/                       视图（2 个文件）
│       ├── View.md                 视图设置
│       └── Design_list.md          设计列表
│
├── 03_examples/                    ← 仿真案例库（32 个文件）
│   │   用途：29 个完整仿真案例，含工程参数、材料、设置、截图
│   │   来源：软件自带 Example 目录的 HTML + .tsp 工程文件解析
│   │
│   ├── index.md                    案例总索引
│   ├── example_manifest.csv.md     案例清单（分类/变量数/材料数/截图数）
│   │
│   ├── Circuit/                     电路仿真案例（3 个）
│   │   ├── LC_LPF/                  LC 低通滤波器
│   │   ├── Filter/                  WavEDA 滤波器
│   │   └── Wilkinson power divider/ 威尔金森功分器
│   │
│   ├── EM/                          电磁仿真案例（16 个）
│   │   ├── Antenna/
│   │   │   ├── dual_band_antenna/   双频带微带天线
│   │   │   ├── patch_array_ant/     阵列贴片天线
│   │   │   └── Wideband_slot_antenna/ 超宽带缝隙天线
│   │   ├── Coupler/
│   │   │   ├── HMSIW_Coupler/       基片集成波导耦合器
│   │   │   └── Tight_Coupled_coupler/ 紧耦合定向耦合器
│   │   ├── Divider/
│   │   │   └── triband_power_divider/ 三频带功分器
│   │   ├── Filter/
│   │   │   ├── 4-2_DR/              双腔介质波导滤波器
│   │   │   ├── SIW_dual_band_filter/ SIW 双频带滤波器
│   │   │   └── mmwave_bpf_IPD/      毫米波 IPD 滤波器
│   │   ├── PBC/（周期边界条件）
│   │   │   ├── AMC/                 人工磁体单元胞
│   │   │   ├── FSS/                 频率选择表面
│   │   │   └── Antenna/             微带贴片天线（周期结构）
│   │   ├── Plane_Wave/
│   │   │   └── Sphere/              球体平面波散射
│   │   ├── SI_PI/（信号/电源完整性）
│   │   │   └── Commom-Mode_Filter/  蘑菇形共模低通滤波器
│   │   └── geological exploration/
│   │       └── porous_medium/       孔隙介质
│   │
│   ├── Mech/                        力学仿真案例（3 个）
│   │   ├── Stool/                   凳子模型（弹性力学）
│   │   ├── Bolt/                    螺栓（弹性力学）
│   │   └── ruler/                   梯面尺（弹性力学）
│   │
│   ├── Multi-Physics/               多物理场案例（6 个）
│   │   ├── Gis insulator/           GIS 绝缘子
│   │   ├── PBGA/                    PBGA 封装
│   │   ├── PKG_WB_Model/           封装键合线模型
│   │   ├── Quarter_Chip_Layout_Pillar_Model/  芯片布局铜柱模型
│   │   ├── Resistor/                电阻器
│   │   └── Wirebonds_model/         键合线模型
│   │
│   └── Thermal/                     热学仿真案例（3 个）
│       ├── Radiator/                散热器
│       ├── Light_bulb/              灯泡
│       └── Silicon_sub_copper_pillar_array/  硅基底铜柱阵列
│
├── 04_error_cases/                 ← 错误排查（3 个文件）
│   │   用途：从软件源码 TypeScript 国际化文件抽取的 1402 条错误/警告
│   │   来源：原 wavEDA_docs/error_cases/ + merged KB
│   │
│   ├── error_message_index.md       按类别索引（仿真/几何/参数/文件/材料/端口/网格）
│   ├── error_message_index.csv.md   CSV 格式索引
│   └── raw_ui_messages.csv.md       原始 UI 文案（13050 条）
│
├── 05_reference/                   ← 参考资料（23 个文件）
│   │   用途：索引、专题卡片、材料库、模板等辅助资料
│   │   来源：原 merged KB 的 20-90 系列子目录
│   │
│   ├── indexes/                     功能与约束索引（5 个文件）
│   │   ├── knowledge_map.md         知识地图
│   │   ├── module_capability_index.md  模块能力索引
│   │   ├── module_page_index.md     模块页面索引
│   │   ├── button_location_function_index.md  按钮位置与功能索引
│   │   └── constraint_warning_index.md  约束与警告索引
│   │
│   ├── topic_cards/                 专题知识卡（6 个文件）
│   │   ├── beginner_simulation_workflow.md  新手仿真工作流
│   │   ├── ports_and_excitations.md  端口与激励专题
│   │   ├── post_processing_results.md 后处理结果专题
│   │   ├── simulation_methods_comparison.md 求解方法对比
│   │   ├── troubleshooting_and_constraints.md 排错与约束
│   │   └── module_selection_guide.md  模块选择指南
│   │
│   ├── material_library/            材料库（3 个文件）
│   │   ├── materials.md             材料清单
│   │   ├── material_selection_guide.md  材料选择指导
│   │   └── material_index.csv.md    材料索引表
│   │
│   ├── circuit_components/          电路元件（2 个文件）
│   │   ├── component_index.md       元件索引
│   │   └── component_icon_index.csv.md  元件图标索引
│   │
│   ├── ui_icons/                    工具栏图标（2 个文件）
│   │   ├── toolbar_icon_index.md    图标索引
│   │   └── toolbar_icon_index.csv.md 图标 CSV 索引
│   │
│   ├── maintenance_templates/       维护模板（3 个文件）
│   │   ├── beginner_task_flow_template.md  新手任务流模板
│   │   ├── button_entry_template.md  按钮条目模板
│   │   └── error_case_template.md    错误案例模板
│   │
│   ├── external_papers/             外部论文（1 个文件）
│   │   └── SFgen_prcv.pdf.md        PDF 论文转 Markdown（信号生成/接收）
│   │
│   └── user_experience_sources/     教学 Agent 资料（1 个文件）
│       └── WavEDA_操作教学型Agent_知识库.md  Ted 的教学 Agent 知识库
│
└── 06_theory_notes/                ← 理论笔记（预留，当前为空）
       用途：多物理场理论（Maxwell 方程、FEM、FDTD 等）
       来源：Obsidian vault（D:\暑期实践\多物理场仿真知识库\）
       说明：此目录内容不在 Git 仓库中，通过外部 Obsidian vault 索引
```

---

## 二、wavEDA_docs/helpHtml/ — 原始 HTML 帮助

> **153 MB，655 个文件（HTML + CSS + 100+ PNG 截图）**

```
wavEDA_docs/
└── helpHtml/
    └── helpHtml/
        ├── Introduction.html         介绍页
        ├── EM_Project/              电磁模块 HTML
        ├── File/                    文件菜单 HTML
        ├── Mesh/                    网格模块 HTML
        ├── Modeling/                建模模块 HTML
        ├── Post_Processing/         后处理 HTML
        ├── Simulation/              仿真 HTML
        ├── Tool/                    工具 HTML
        ├── View/                    视图 HTML
        ├── *.css                    样式表
        └── images/                  100+ 张界面截图（PNG）
```

**用途**：GUI 中用户点击 `ragsrc://` 链接时，渲染原始帮助页面。

---

## 三、data/index/ — 检索索引

> **4974 个 chunk，2,064K 字符，4974×384 向量矩阵**

```
data/index/
├── chunks.json        2.4 MB    4974 个知识块（含完整文本 + 元数据）
└── vectors.npy        5.7 MB    4974×384 float32 哈希向量矩阵
```

| 来源 | chunk 数 | 比例 |
|------|---------|------|
| 仓库内文件（新建） | 3,566 | 72% |
| 外部 Obsidian vault | 1,284 | 26% |
| 外部 helpHtml | 124 | 2% |
| **总计** | **4,974** | 100% |

---

## 四、config/ — 配置文件

```
config/
├── .env                 API 密钥等（Git 忽略，不提交）
├── .env.example         环境变量模板
└── kb_sources.yaml      知识库数据源路径配置
```

---

## 五、scripts/ — 工具脚本

```
scripts/
├── build_knowledge_base.py     全量重建索引
├── add_document.py             单文件增量添加
├── rebuild_index_merge.py      合并式索引重建（保留外部 chunk + 重建仓库内）
├── debug_retrieval.py          检索调试工具
└── smoke_test.py               冒烟测试（3 个问答）
```
