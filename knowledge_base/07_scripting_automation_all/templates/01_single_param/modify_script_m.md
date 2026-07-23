---
title: 单参数扫参 — modify_script 子程序
category: scripting
tags: [代码, MATLAB, XML修改, 子程序]
indexing: true
---

# modify_script.m — 通用 XML 修改子程序（单参数版）

```matlab
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  modify_script.m — 通用子程序（不需要改动）
%  功能：读模板 XML → 修改变量值 + 输出文件名 → 写出新 XML
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  输入:
%     src_file   - 模板 XML 路径
%     dst_file   - 目标 XML 路径
%     var_name   - 变量名
%     var_value  - 变量新值 (字符串)
%     obv_set    - Observer 数据集名称（不需要则传 ''）
%     obv_file   - Observer 输出文件路径（不需要则传 ''）
%     port_set   - Port S参数数据集名称
%     port_file  - Port 输出文件路径
%  返回:
%     ret        - 修改成功的变量个数
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function ret = modify_script(src_file, dst_file, var_name, var_value, ...
                              obv_set, obv_file, port_set, port_file)
    ret = 0;
    xmlTree = xmlread(src_file);
    root = xmlTree.item(0);
    cmd_nodes = root.getChildNodes;
    nCmd = cmd_nodes.getLength;

    for count = 1:nCmd
        cmdNode = cmd_nodes.item(count - 1);
        if ~cmdNode.hasAttributes; continue; end

        cmdType  = cmdNode.getAttribute('cmdType');
        obj1Type = cmdNode.getAttribute('obj1');
        obj2Type = cmdNode.getAttribute('obj2');

        % modify:var → 修改变量值
        if strcmpi(cmdType, 'modify') && strcmpi(obj1Type, 'var')
            if strcmpi(cmdNode.getAttribute('name'), var_name)
                cmdNode.setAttribute('value', var_value);
                ret = ret + 1;
            end
        end

        % export:result → 修改输出文件路径
        if strcmpi(cmdType, 'export') && strcmpi(obj1Type, 'result')
            nodeName = cmdNode.getAttribute('name');
            if strcmpi(obj2Type, 'obv') || strcmpi(obj2Type, 'observer')
                if strcmpi(nodeName, obv_set)
                    cmdNode.setAttribute('file', obv_file);
                end
            end
            if strcmpi(obj2Type, 'port')
                if strcmpi(nodeName, port_set)
                    cmdNode.setAttribute('file', port_file);
                end
            end
        end
    end
    xmlwrite(dst_file, xmlTree);
end
```
