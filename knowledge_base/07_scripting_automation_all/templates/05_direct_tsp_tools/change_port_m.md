---
title: 直接改 .tsp — 改端口阻抗
category: scripting
tags: [tsp, 工具, 端口, 代码]
indexing: true
---

# change_port.m — 改集总端口阻抗

```matlab
src_tsp   = 'E:\your_path\model.tsp';
dst_tsp   = 'E:\your_path\model_new.tsp';
port_name = '1';
new_r     = '75';       % new resistance in Ohm

tree = xmlread(src_tsp); root = tree.item(0);
ports = root.getElementsByTagName('lumped-port');
for p = 1:ports.getLength
    node = ports.item(p-1);
    if strcmpi(node.getAttribute('name'), port_name)
        old = node.getAttribute('resistance');
        node.setAttribute('resistance', new_r);
        fprintf('[OK] port "%s" resistance: %s -> %s Ohm\n', port_name, old, new_r);
    end
end
xmlwrite(dst_tsp, tree);
fprintf('[SAVED] %s\n', dst_tsp);
```
