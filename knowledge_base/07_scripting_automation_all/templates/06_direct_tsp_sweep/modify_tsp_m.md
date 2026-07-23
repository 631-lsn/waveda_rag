---
title: 直改 .tsp 扫参 — modify_tsp 核心工具
category: scripting
tags: [代码, MATLAB, tsp, 直接修改, 子程序]
indexing: true
---

# modify_tsp.m — 直接修改 .tsp 工程文件（核心工具）

支持 10 种直接修改类型：变量、实体材料、背景材料、激励、端口、频率、求解器、网格、观测点、计算域。

```matlab
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  modify_tsp.m — 直接修改 .tsp 工程文件（通用子程序，不需改动）
%
%  功能：读 .tsp -> 改变量值/材料/激励等 -> 写出新 .tsp
%        绕过 XML 脚本的 modify 命令，变量直接写在工程文件里
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  输入:
%     src_tsp    - 源 .tsp 文件路径
%     dst_tsp    - 目标 .tsp 文件路径
%     changes    - struct 数组，每个元素描述一项修改：
%         changes(k).target   - 要改什么（见下方支持列表）
%         changes(k).name     - 目标名称（变量名/材料名/端口名等）
%         changes(k).attr     - 要改的属性名
%         changes(k).value    - 新值（字符串）
%
%  支持的直接修改类型：
%    'var'           - 变量：expression, origin
%    'material-ref'  - 实体材料引用：<solid material="...">
%    'excitation'    - 激励：mag, phase
%    'port'          - 端口：resistance
%    'background'    - 背景材料：<bkg material="...">
%    'freq-pulse'    - 频域脉冲：freq, max-freq, min-freq
%    'solver'        - 求解器：tolerance, max-iterations
%    'mesh-3d'       - 3D网格：ppw
%    'observer'      - 观测点：pos
%    'domain'        - 计算域：gap
%
%  返回:
%     ret - 修改成功的个数
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function ret = modify_tsp(src_tsp, dst_tsp, changes)

    ret = 0;
    if isempty(changes); xmlwrite(dst_tsp, xmlread(src_tsp)); return; end
    tree = xmlread(src_tsp); root = tree.item(0);

    for k = 1:length(changes)
        target = changes(k).target;
        name   = changes(k).name;
        attr   = changes(k).attr;
        value  = changes(k).value;

        switch lower(target)
            case 'var'
                vars = root.getElementsByTagName('var');
                for v = 1:vars.getLength
                    node = vars.item(v-1);
                    if strcmpi(node.getAttribute('name'), name)
                        node.setAttribute(attr, value); ret = ret + 1;
                    end
                end
            case 'material-ref'
                solids = root.getElementsByTagName('solid');
                for s = 1:solids.getLength
                    node = solids.item(s-1);
                    if strcmpi(node.getAttribute('name'), name)
                        node.setAttribute('material', value); ret = ret + 1;
                    end
                end
            case 'background'
                bkgs = root.getElementsByTagName('bkg');
                for b = 1:bkgs.getLength
                    node = bkgs.item(b-1);
                    node.setAttribute('material', value); ret = ret + 1;
                end
            case 'excitation'
                excs = root.getElementsByTagName('excitation');
                for e = 1:excs.getLength
                    node = excs.item(e-1);
                    if strcmpi(node.getAttribute('name'), name)
                        node.setAttribute(attr, value); ret = ret + 1;
                    end
                end
            case 'port'
                ports = root.getElementsByTagName('lumped-port');
                for p = 1:ports.getLength
                    node = ports.item(p-1);
                    if strcmpi(node.getAttribute('name'), name)
                        node.setAttribute(attr, value); ret = ret + 1;
                    end
                end
            case 'freq-pulse'
                fps = root.getElementsByTagName('frequency-pulse');
                for f = 1:fps.getLength
                    node = fps.item(f-1);
                    if strcmpi(node.getAttribute('physics-type'), 'EM')
                        node.setAttribute(attr, value); ret = ret + 1;
                    end
                end
            case 'solver'
                svrs = root.getElementsByTagName('project-solver');
                for s = 1:svrs.getLength
                    node = svrs.item(s-1);
                    node.setAttribute(attr, value); ret = ret + 1;
                end
            case 'mesh-3d'
                meshes = root.getElementsByTagName('mesh-3d-setting');
                for m = 1:meshes.getLength
                    node = meshes.item(m-1);
                    node.setAttribute(attr, value); ret = ret + 1;
                end
            case 'observer'
                pts = root.getElementsByTagName('point');
                for p = 1:pts.getLength
                    node = pts.item(p-1);
                    if strcmpi(node.getAttribute('name'), name)
                        node.setAttribute('pos', value); ret = ret + 1;
                    end
                end
            case 'domain'
                dms = root.getElementsByTagName('domain-space');
                for d = 1:dms.getLength
                    node = dms.item(d-1);
                    node.setAttribute('gap', value); ret = ret + 1;
                end
        end
    end
    xmlwrite(dst_tsp, tree);
end
```
