---
title: Python 版扫参主控程序
category: scripting
tags: [代码, Python, 主控程序, 单参数, 完整]
indexing: true
---

# sweep_main.py — Python 版单参数扫参主控程序

不依赖 pandas/numpy，使用标准库 `xml.etree.ElementTree` + `subprocess` + 自定义数据读取函数。

```python
##################################################################
#  sweep_main.py — WavEDA 单参数扫参 (Python 版)
#  pip install matplotlib
##################################################################

import subprocess
import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from datetime import datetime


# ================================================================
#  数据提取函数（不依赖 pandas/numpy）
# ================================================================

def extract_col(filepath, marker, col_idx):
    """从空格分隔的文本文件中提取第 col_idx 列数据，跳过注释行"""
    vals = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                stripped = line.strip()
                if not stripped or stripped.startswith(marker):
                    continue
                parts = stripped.split()
                if len(parts) > col_idx:
                    try:
                        vals.append(float(parts[col_idx]))
                    except ValueError:
                        pass
    except FileNotFoundError:
        print(f'  ⚠ 文件不存在: {filepath}')
    return vals


# ================================================================
#  【用户配置区】
# ================================================================

work_path  = '你的工作目录/'
waveda_exe = 'C:/Program Files/WavEDA/WavEDA.exe'

template_xml    = os.path.join(work_path, 'template.xml')
temp_script_xml = os.path.join(work_path, 'temp_script.xml')

var_name  = '你的变量名'
var_start = 30
var_step  = 2
var_end   = 40

port_dataset_name = '你的Port_S参数数据集名'

target_freq   = 2.45
s11_threshold = -10


# ================================================================
#  初始化
# ================================================================

num_steps = round((var_end - var_start) / var_step) + 1
param_list = [var_start + i * var_step for i in range(num_steps)]
num_params = len(param_list)

print(f'扫描变量: {var_name}  ({var_start:.2f}~{var_end:.2f}, {num_params}组)\n')

all_s11_min = [0.0] * num_params
all_freq_min = [0.0] * num_params
all_bw = [float('nan')] * num_params
all_s11_target = [0.0] * num_params
all_s11 = [None] * num_params
all_freq = [None] * num_params


# ================================================================
#  Part I & II & III: 扫参主循环
# ================================================================

for i, current_val in enumerate(param_list):

    print(f'[{i+1}/{num_params}] {var_name} = {current_val:.2f}')

    # ---- Part I: 修改 XML ----
    port_file = os.path.join(work_path, f'port_data_{i+1}.txt')

    tree = ET.parse(template_xml)
    root = tree.getroot()

    for cmd in root.iter('command'):
        ct = cmd.get('cmdType')
        if ct is None:
            continue
        ct_lower = ct.lower()
        o1 = cmd.get('obj1', '')
        o2 = cmd.get('obj2', '')

        if ct_lower == 'modify' and o1.lower() in ('var', 'variable'):
            if cmd.get('name', '').lower() == var_name.lower():
                cmd.set('value', f'{current_val:.2f}')

        elif ct_lower == 'export' and o1.lower() == 'result' and o2.lower() == 'port':
            if cmd.get('name', '').lower() == port_dataset_name.lower():
                cmd.set('file', port_file)

    tree.write(temp_script_xml, encoding='utf-8', xml_declaration=True)

    # ---- Part II: 运行仿真 ----
    bat_file = os.path.join(work_path, 'run_waveda.bat')
    waveda_dir = os.path.dirname(waveda_exe)
    waveda_name = os.path.basename(waveda_exe)
    with open(bat_file, 'w') as f:
        f.write(f'cd /d "{waveda_dir}"\n')
        f.write(f'{waveda_name} "script={temp_script_xml}"\n')

    for retry in range(3):
        subprocess.run(bat_file, shell=True, capture_output=True)
        import time; time.sleep(5)
        if os.path.exists(port_file):
            print(f'  ✅ 文件已生成 (try {retry+1})')
            break
        print(f'  ⚠ 文件未生成，重试 ({retry+1}/3)')

    if not os.path.exists(port_file):
        print('  ❌ 重试失败')
        continue

    # ---- Part III: 读数据 & 算指标 ----
    freq = extract_col(port_file, '%', 0)
    s11_db = extract_col(port_file, '%', 1)

    if not freq or not s11_db:
        continue

    all_freq[i] = freq
    all_s11[i] = s11_db

    # 最小 S11
    min_idx = s11_db.index(min(s11_db))
    all_s11_min[i] = s11_db[min_idx]
    all_freq_min[i] = freq[min_idx]

    # 带宽
    bw_idx = [j for j, v in enumerate(s11_db) if v <= s11_threshold]
    if len(bw_idx) >= 2:
        all_bw[i] = freq[bw_idx[-1]] - freq[bw_idx[0]]

    # 目标频率
    closest = min(range(len(freq)), key=lambda j: abs(freq[j] - target_freq))
    all_s11_target[i] = s11_db[closest]

    print(f'  min S11: {all_s11_min[i]:.3f} dB @ {all_freq_min[i]:.4f} GHz')


# ================================================================
#  汇总图表
# ================================================================

# 图1: 全部 S11 叠加
fig1, ax1 = plt.subplots(figsize=(10, 6))
for i in range(num_params):
    if all_freq[i] is not None:
        ax1.plot(all_freq[i], all_s11[i], linewidth=1.5,
                 label=f'{var_name}={param_list[i]:.2f} (min={all_s11_min[i]:.2f} dB)')
ax1.axhline(y=s11_threshold, color='r', linestyle='--')
ax1.axvline(x=target_freq, color='g', linestyle='--')
ax1.set_xlabel('Frequency (GHz)'); ax1.set_ylabel('|S11| (dB)')
ax1.set_title(f'S11 Comparison — {var_name}')
ax1.legend(loc='best', fontsize=8); ax1.grid(True)
fig1.tight_layout()

# 图2: 指标面板
fig2, axes = plt.subplots(2, 3, figsize=(14, 8))
axes[0,0].plot(param_list, all_s11_min, 'bo-'); axes[0,0].set_title('Min |S11|')
axes[0,1].plot(param_list, all_freq_min, 'ro-'); axes[0,1].set_title('Resonant Freq')
valid = [(j,v) for j,v in enumerate(all_bw) if not (isinstance(v,float) and v!=v)]
if valid:
    axes[0,2].plot([param_list[j] for j,_ in valid], [v for _,v in valid], 'go-')
axes[0,2].set_title(f'{s11_threshold}dB BW')
axes[1,0].plot(param_list, all_s11_target, 'co-'); axes[1,0].set_title(f'S11@{target_freq}GHz')
axes[1,1].axis('off'); axes[1,2].axis('off')
fig2.tight_layout()

plt.show()
```
