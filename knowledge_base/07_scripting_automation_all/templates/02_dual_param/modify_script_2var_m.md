---
title: 双参数扫参 — modify_script_2var 子程序
category: scripting
tags: [代码, MATLAB, XML修改, 双参数, 子程序]
indexing: true
---

# modify_script_2var.m — 双参数 XML 修改子程序

```matlab
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  modify_script_2var.m — 通用子程序（不需要改动）
%  功能：读模板 XML → 修改两个变量值 + Port输出文件名 → 写出新 XML
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function ret = modify_script_2var(src, dst, v1n, v1v, v2n, v2v, pset, pfile)
    ret = 0;
    t = xmlread(src); r = t.item(0);
    for c = 1:r.getChildNodes.getLength
        n = r.getChildNodes.item(c-1);
        if ~n.hasAttributes; continue; end
        ct = n.getAttribute('cmdType'); o1 = n.getAttribute('obj1'); o2 = n.getAttribute('obj2');
        if strcmpi(ct,'modify') && strcmpi(o1,'var')
            nn = n.getAttribute('name');
            if strcmpi(nn,v1n); n.setAttribute('value',v1v); ret=ret+1; end
            if strcmpi(nn,v2n); n.setAttribute('value',v2v); ret=ret+1; end
        end
        if strcmpi(ct,'export') && strcmpi(o1,'result') && strcmpi(o2,'port')
            if strcmpi(n.getAttribute('name'),pset); n.setAttribute('file',pfile); end
        end
    end
    xmlwrite(dst,t);
end
```
