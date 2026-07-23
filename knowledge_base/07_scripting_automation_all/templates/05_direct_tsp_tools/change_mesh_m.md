---
title: 直接改 .tsp — 改网格密度
category: scripting
tags: [tsp, 工具, 网格, 代码]
indexing: true
---

# change_mesh.m — 改网格密度

```matlab
src_tsp    = 'E:\your_path\model.tsp';
dst_tsp    = 'E:\your_path\model_new.tsp';
new_ppw    = '5';         % points per wavelength, set '' to skip
new_edge   = '0.001';     % min edge length (mm), set '' to skip
new_growth = '1.5';       % growth ratio, set '' to skip

tree = xmlread(src_tsp); root = tree.item(0);
meshes = root.getElementsByTagName('mesh-3d-setting');
for m = 1:meshes.getLength
    node = meshes.item(m-1);
    if strcmp(node.getAttribute('physics'), 'EM')
        if ~isempty(new_ppw)
            old = node.getAttribute('ppw');
            node.setAttribute('ppw', new_ppw);
            fprintf('[OK] ppw: %s -> %s\n', old, new_ppw);
        end
        if ~isempty(new_edge)
            node.setAttribute('min-1D-edge-length', new_edge);
            fprintf('[OK] min edge -> %s mm\n', new_edge);
        end
        if ~isempty(new_growth)
            node.setAttribute('growth-ratio-3d', new_growth);
            fprintf('[OK] growth ratio -> %s\n', new_growth);
        end
    end
end
xmlwrite(dst_tsp, tree);
fprintf('[SAVED] %s\n', dst_tsp);
```
