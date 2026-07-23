---
title: 直接改 .tsp — 改激励
category: scripting
tags: [tsp, 工具, 激励, 代码]
indexing: true
---

# change_excitation.m — 改激励幅度/相位

```matlab
src_tsp    = 'E:\your_path\model.tsp';
dst_tsp    = 'E:\your_path\model_new.tsp';
exc_name   = '1';       % excitation name
new_mag    = '2';       % new magnitude (set '' to skip)
new_phase  = '90';      % new phase in degrees (set '' to skip)

tree = xmlread(src_tsp); root = tree.item(0);
excs = root.getElementsByTagName('excitation');
for e = 1:excs.getLength
    node = excs.item(e-1);
    if strcmpi(node.getAttribute('name'), exc_name)
        if ~isempty(new_mag)
            old = node.getAttribute('mag');
            node.setAttribute('mag', new_mag);
            fprintf('[OK] magnitude: %s -> %s\n', old, new_mag);
        end
        if ~isempty(new_phase)
            old = node.getAttribute('phase');
            node.setAttribute('phase', new_phase);
            fprintf('[OK] phase: %s -> %s deg\n', old, new_phase);
        end
    end
end
xmlwrite(dst_tsp, tree);
fprintf('[SAVED] %s\n', dst_tsp);
```
