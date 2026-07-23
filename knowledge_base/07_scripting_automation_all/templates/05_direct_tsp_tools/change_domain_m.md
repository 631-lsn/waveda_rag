---
title: 直接改 .tsp — 改计算域大小
category: scripting
tags: [tsp, 工具, 计算域, 代码]
indexing: true
---

# change_domain.m — 改计算域边界

```matlab
src_tsp = 'E:\your_path\model.tsp';
dst_tsp = 'E:\your_path\model_new.tsp';
% gap format: "xmin, ymin, zmin, xmax, ymax, zmax"
new_gap = '-10, -10, -l-20, 10, 10, l+20';

tree = xmlread(src_tsp); root = tree.item(0);
dms = root.getElementsByTagName('domain-space');
for d = 1:dms.getLength
    node = dms.item(d-1);
    old = node.getAttribute('gap');
    node.setAttribute('gap', new_gap);
    fprintf('[OK] domain: (%s) -> (%s)\n', old, new_gap);
end
xmlwrite(dst_tsp, tree);
fprintf('[SAVED] %s\n', dst_tsp);
```
