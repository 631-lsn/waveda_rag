---
title: 直接改 .tsp — 改变量值
category: scripting
tags: [tsp, 工具, 变量, 代码]
indexing: true
---

# change_variable.m — 改变 .tsp 工程中的变量值

```matlab
src_tsp  = 'E:\your_path\model.tsp';
dst_tsp  = 'E:\your_path\model_new.tsp';
var_name = 'l';
new_value = '50';

tree = xmlread(src_tsp); root = tree.item(0);
vars = root.getElementsByTagName('var'); found = false;
for v = 1:vars.getLength
    node = vars.item(v-1);
    if strcmpi(node.getAttribute('name'), var_name)
        old = node.getAttribute('expression');
        node.setAttribute('expression', new_value);
        node.setAttribute('origin', new_value);
        found = true;
        fprintf('[OK] %s: %s -> %s\n', var_name, old, new_value);
    end
end
if ~found; fprintf('[WARN] variable "%s" not found\n', var_name); end
xmlwrite(dst_tsp, tree);
fprintf('[SAVED] %s\n', dst_tsp);
```
