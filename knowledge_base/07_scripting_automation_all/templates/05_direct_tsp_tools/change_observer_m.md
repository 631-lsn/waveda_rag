---
title: 直接改 .tsp — 改观测点位置
category: scripting
tags: [tsp, 工具, 观测点, 代码]
indexing: true
---

# change_observer.m — 改观测点位置

```matlab
src_tsp  = 'E:\your_path\model.tsp';
dst_tsp  = 'E:\your_path\model_new.tsp';
obs_name = 'obs_1';
new_pos  = '10, 10, 5';    % "x, y, z"

tree = xmlread(src_tsp); root = tree.item(0);
pts = root.getElementsByTagName('point');
for p = 1:pts.getLength
    node = pts.item(p-1);
    if strcmpi(node.getAttribute('name'), obs_name)
        old = node.getAttribute('pos');
        node.setAttribute('pos', new_pos);
        fprintf('[OK] observer "%s": (%s) -> (%s)\n', obs_name, old, new_pos);
    end
end
xmlwrite(dst_tsp, tree);
fprintf('[SAVED] %s\n', dst_tsp);
```
