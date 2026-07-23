---
title: 直接改 .tsp — 改频率范围
category: scripting
tags: [tsp, 工具, 频率, 代码]
indexing: true
---

# change_frequency.m — 改频率范围

```matlab
src_tsp   = 'E:\your_path\model.tsp';
dst_tsp   = 'E:\your_path\model_new.tsp';
new_max   = '10';       % max freq (GHz), set '' to skip
new_min   = '0.01';     % min freq (GHz), set '' to skip
new_center = '5';       % center freq (GHz), set '' to skip

tree = xmlread(src_tsp); root = tree.item(0);
fps = root.getElementsByTagName('frequency-pulse');
for f = 1:fps.getLength
    node = fps.item(f-1);
    if strcmp(node.getAttribute('physics-type'), 'EM')
        if ~isempty(new_max)
            old = node.getAttribute('max-freq');
            node.setAttribute('max-freq', new_max);
            fprintf('[OK] max-freq: %s -> %s GHz\n', old, new_max);
        end
        if ~isempty(new_min)
            old = node.getAttribute('min-freq');
            node.setAttribute('min-freq', new_min);
            fprintf('[OK] min-freq: %s -> %s GHz\n', old, new_min);
        end
        if ~isempty(new_center)
            old = node.getAttribute('freq');
            node.setAttribute('freq', new_center);
            fprintf('[OK] center-freq: %s -> %s GHz\n', old, new_center);
        end
    end
end
xmlwrite(dst_tsp, tree);
fprintf('[SAVED] %s\n', dst_tsp);
```
