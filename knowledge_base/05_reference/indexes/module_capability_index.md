---
title: "模块能力索引"
merged_source: "current_waveda_agent_kb"
source_relative_path: "20_indexes/module_capability_index.md"
original_path: "D:\RAGGG\knowledge_sources\waveda_agent_kb\20_indexes\module_capability_index.md"
content_kind: "markdown"
merged_at: "2026-07-07"
---

# 模块能力索引

- 来源目录: `D:\Staid\app\waveda\resources\module_description`

## circuit
WavEDA Circuit Modules integrate schematic modeling, subcircuit simulation, multi-solver types (DC/AC/TRANS/SP), and parameter tuning, covering the entire design workflow from fundamental RLC components to complex nonlinear systems.

Featuring an extensive built-in component library and simulation templates, it supports specialized tools such as parametric scanning, variable linkage, real-time probe monitoring, and Smith charts. One-click netlist generation and verification are enabled, along with integrated transmission line calculation tools. Combined with open/short circuit simulation capabilities, it delivers high-precision circuit analysis and optimization. Furthermore, it supports circuit-electromagnetic co-simulation, providing an integrated solution from modeling and simulation through to result export.

## circuit_CN
WaVEDA 电路模块集成原理图建模、子电路仿真、多类型求解器(DC/AC/TRANS/SP)及参数调谐功能，覆盖从基础RLC元件到复杂非线性系统的全流程设计需求。
       内置丰富元件库与仿真模板，支持参数化扫描、变量联动、探针实时监测及史密斯圆图等专业工具，可一键生成网表并验证，内置传输线计算工具，结合开路/短路仿真功能，实现高精度电路分析与优化。同时支持通过电路-电磁协同仿真，提供从建模、仿真到结果导出一体化解决方案。

## em
WavEDA Electromagnetic Module, with its innovative mixed finite element method at the core, integrates adaptive mesh iteration and model order reduction technologies. It overcomes the limitations of traditional electromagnetic and circuit simulators in chip-package-system level, RF integrated microsystems, RFIC, and MMIC domains, effectively addressing complex challenges such as large-scale, multi-scale, high-density break-down, and high-frequency electromagnetic effects, and provides users with unprecedented simulation accuracy and efficiency.

The module achieves precise 3D modeling and supports a variety of complex boundary conditions (including PEC, PMC, impedance, periodic, and open boundaries), multiple excitation types (such as point source, plane wave, lumped port, and wave port), and complex materials like high-loss dielectric dispersion, magnetic dispersion, and anisotropy. Moreover, it possesses powerful post-processing capabilities, allowing users to easily view S-parameters, near-field/far-field results, snapshots and wave port modes.

## em_CN
WavEDA电磁模块以革新性的混合有限元算法为核心，融合自适应网格迭代与模型降阶技术，突破了传统电磁与电路仿真在芯片-封装-系统级、射频集成微系统、RFIC及MMIC领域的局限，有效应对了大规模、多尺度、高密度崩溃及高频电磁效应等复杂挑战，为用户提供了前所未有的仿真精度与效率。
       WavEDA电磁模块实现了对目标系统的精准3D建模，支持多样化的复杂边界条件（包括完美电导体、完美磁导体、 阻抗、 周期及开放边界等），多种激励类型（如点源、平面波、集总及波端口），并能高效仿真高损耗电色散、磁色散及各向异性等复杂材料。同时拥有强大的后处理能力，方便用户查看S参数，近场/远场结果，快照，波端口模式等。

## Layout
The Layout Module of WavEDA is compatible with various mainstream layout formats, including ODB++, DXF, and GDS, enabling fast file import and visual editing. It also supports manual creation of PCB and DIE stack-up structures for circuits and provides configuration options for custom polygonal pads and via templates. For complex chip packaging scenarios, the module can create bonding wires, scripts, components, and other elements, and offers network configuration options for differential signals, grounding, power supply, and single-ended signals, meeting diverse circuit design requirements. 

After completing 2D layout drawing, multi-physics excitation types can be quickly defined within the Layout module, enabling the seamless and rapid construction and simulation of 3D multi-physics models from 2D layouts. The software is adapted to complex scenarios such as high-density integrated circuits, chip packaging, and RF and millimeter-wave components, reduces precision loss in cross-tool data transmission, and integrates layout design and 3D simulation.

## Layout_CN
WavEDA的Layout模块兼容ODB++、DXF、GDS等多种主流ECAD格式，可实现文件快速导入与可视化编辑，同时能够手动创建电路的PCB和DIE层叠结构，提供自定义多边形焊盘与通孔模版配置功能。针对复杂芯片封装场景，该模块可完成键合线、脚本、组件等内容创建，并提供差分信号、接地、电源及单端信号等网络类配置选项，满足多样化电路设计需求。
       2D版图绘制完成后，可在Layout模块内快速定义多物理场激励类型进而无缝完成2D版图到3D多物理场模型的快速建立与仿真。软件适配高密度集成电路、芯片封装、射频及毫米波组件等复杂场景，降低跨工具数据传输精度损耗，实现版图设计与三维仿真一体化。

## mechnical
WavEDA Mechanics Module based on advanced FEM and DDM with adaptive meshing overcomes simulation limitations in complex downhole structures, multilayer casings, and highly attenuative boundaries. It delivers high-precision, efficient solutions for cross-scale wave propagation, heterogeneous media coupling, and multi-source excitation.

Supporting refined 3D modeling, it offers configurable boundary conditions (soft/hard, prescribed displacement, periodic, PML) and excitation types (point/surface/volume loads, monopole/dipole sources). It efficiently simulates anisotropic rock, poroelastic media, and structure‑acoustic coupling.

With robust post‑processing for stress/displacement field visualization and analysis, the module provides a reliable, high‑efficiency tool for advanced engineering challenges.

## mechnical_CN
WavEDA力学模块以先进的有限元算法以及区域分解技术为核心，融合自适应网格迭代方法，有效突破了传统固体力学与声波测井仿真在复杂井下环境、多层套管结构及复杂边界衰减等领域的局限，为用户应对跨尺度波动传播、强非均匀介质耦合及多源激励响应等工程挑战，提供了高精度与高效率并重的专业仿真解决方案。
       该模块实现了对目标系统的精细化三维建模，支持多样化的复杂边界条件，包括软硬边界、指定位移边界、周期边界及完美匹配层等。在激励方面，提供从固体力学中的点、面、体载荷，到声波测井中的偶极子、单极子等多种声源类型，并能高效模拟各向异性岩体、孔隙弹性介质及结构-声场耦合行为。拥有强大的后处理功能，可方便用户查看应力分布、位移场分布云图等结果。WavEDA力学模块通过严谨的算法基础、专业的工程问题配置与全面的分析能力，为前沿工程挑战提供了强大可靠的仿真工具支持。

## Multi-Physics
WavEDA Multi-Physics Module delivers a fully integrated electrical-thermal-mechanical simulation, enabling accurate 3D modeling of the target system in all dimensions. One-click coupling supports steady-state, time-domain, and frequency-domain simulations while seamlessly sharing boundary conditions across electromagnetic, thermal, and mechanical domains. 

It is compatible with multiple excitations such as point sources, plane waves, lumped ports, wave ports, currents, heat sources, and pressures; efficiently handle issues such as electrical-magnetic-thermal dispersion, anisotropy, and elastic media, and integrate chip packaging system level geometry across scales; built in grid partitioning, model reduction, real-time unidirectional coupling of electromagnetic heat, Joule heat, thermal expansion, electromagnetic force, piezoelectric and other effects, solving IC circuit packaging and reliability analysis problems; powerful post-processing with one click output of S-parameters, Z-parameters, VSWR, temperature cloud map, stress cloud map, displacement cloud map, far-field radiation, mode field, and parameterized scanning results effectively address the complex challenges of electrical-thermal-mechanical multi domain collaboration, providing users with unprecedented panoramic accuracy and one-stop design speed.

## Multi-Physics_CN
WavEDA多物理场模块集成电-热-力全流程仿真，实现对目标系统全维度精准3D建模，一键耦合电-热-力场稳态、时域、频域仿真，集成电磁模块、热模块、力学模块边界条件，实现工程内跨场边界条件设置。
       兼容点源、平面波、集总端口、波端口、电流、热源、压力等多元激励；高效处理电-磁-热色散、各向异性、弹性介质等问题，跨尺度融合芯片-封装-系统级几何；内置网格划分、模型降阶，实时单向耦合电磁热、焦耳热、热膨胀、电磁力、压电等效应，解决IC电路封装和可靠性分析问题；强大后处理一键输出S参数、Z参数、VSWR、温度云图、应力云图、位移云图、远场辐射、模式场及参数化扫描结果，有效应对了电-热-力多域协同复杂挑战，为用户提供了前所未有的全景精度与一站式设计速度。

## thermal
WavEDA Thermal Module uses efficient FEM for high-precision 3D modeling and accurate heat-conduction simulation. It supports diverse thermal boundary conditions including periodic boundaries, thermal insulation, temperature, and heat flux, and allows thermal excitation sources such as heat sources, heat rates, or temperature loads. Both steady-state and time-domain analyses are available, and heat sources can follow dynamic signals like pulses to simulate chip temperature rise.

The 3D discretized mesh, combined with adaptive meshing, refines areas of steep temperature gradients to balance efficiency and accuracy. Observers track temperature changes, snapshots record field distributions, and post-processing provides clear temperature cloud plots and observer curves. Importing third-party data enhances workflow consistency and verification efficiency.

Integrated seamlessly with EM and Mechanics modules, it enables high-fidelity EM-Thermal-Mechanics co-simulation for highly integrated electronic systems, forming an efficient platform for chip cooling optimization and thermal reliability evaluation.

## thermal_CN
WavEDA温度场求解基于高效的有限元算法，支持高精度三维建模，能够准确模拟复杂结构中的热传导过程。支持多样化的热学边界条件（包括周期性边界、热绝缘、固定温度及热对流等），灵活适应各种封装与散热场景。用户可设置不同形式的热激励源，如热源、热流密度或温度载荷。支持稳态与时域分析，在时域仿真中，热源可跟随脉冲等信号动态变化，模拟真实芯片工作的温升过程。网格系统采用三维离散，并可配合自适应网格技术，在温度梯度剧烈区域智能加密，平衡计算效率与精度。
       为便于结果监测与分析，模块支持设置接收器，追踪温度变化；快照功能可记录温度场分布；强大的后处理功能清晰呈现温度云图及接收器曲线；支持导入第三方软件的数据结果进行对比，显著提升了多工具工作流的一致性与设计验证效率。
       该模块可与WavEDA电磁、力学模块无缝协同,成为优化芯片散热设计、评估热可靠性的高效平台,最终实现高集成度电子系统的电-热-力一体化高保真仿真。
