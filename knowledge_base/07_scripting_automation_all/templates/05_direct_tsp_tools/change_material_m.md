---
title: 直接改 .tsp — 改材料
category: scripting
tags: [tsp, 工具, 材料, 代码]
indexing: true
---

# change_material.m — 改实体或背景材料

```matlab
src_tsp  = 'E:\your_path\model.tsp';
dst_tsp  = 'E:\your_path\model_new.tsp';
solid_name  = 'top';       % solid name (set '' to skip)
new_mat     = 'Copper';    % new material (must exist in <materials>)
bg_mat      = '';          % new background material (set '' to skip)

tree = xmlread(src_tsp); root = tree.item(0);

if ~isempty(solid_name)
    solids = root.getElementsByTagName('solid');
    for s = 1:solids.getLength
        node = solids.item(s-1);
        if strcmpi(node.getAttribute('name'), solid_name)
            old = node.getAttribute('material');
            node.setAttribute('material', new_mat);
            fprintf('[OK] solid "%s" material: %s -> %s\n', solid_name, old, new_mat);
        end
    end
end

if ~isempty(bg_mat)
    bkgs = root.getElementsByTagName('bkg');
    for b = 1:bkgs.getLength
        node = bkgs.item(b-1);
        old = node.getAttribute('material');
        node.setAttribute('material', bg_mat);
        fprintf('[OK] background: %s -> %s\n', old, bg_mat);
    end
end
xmlwrite(dst_tsp, tree);
fprintf('[SAVED] %s\n', dst_tsp);
```
