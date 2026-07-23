"""
WavEDA 脚本自动生成引擎
从统一 task_config.json 生成可直接运行的 XML / MATLAB / Python / README 文件包。
"""
from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any

# ── XML 转义 ─────────────────────────────────────────
_XML_ESCAPE_TABLE = str.maketrans({
    "&": "&amp;", "<": "&lt;", ">": "&gt;",
    '"': "&quot;", "'": "&apos;",
})


def _xml_escape(text: str) -> str:
    return text.translate(_XML_ESCAPE_TABLE)


def _safe_filename(value: float) -> str:
    """将参数值转为合法文件名，处理负号和小数点。"""
    s = f"{value:.6g}"
    return s.replace("-", "m").replace(".", "p")


# ── XML 模板生成 ──────────────────────────────────────

def generate_xml_template(config: dict[str, Any]) -> str:
    """生成单参数外部循环的 XML 模板。"""
    project_file = _xml_escape(config.get("project_file", "<PROJECT_FILE>"))
    port_name = _xml_escape(config["results"][0]["name"]) if config.get("results") else "Port_S_data_1"
    port_file = _xml_escape(config.get("output_dir", "<OUTPUT_DIR>") + "/port_data_<INDEX>.txt")

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<script version="1.0">',
        f'    <command cmdType="load" obj1="project" file="{project_file}" />',
    ]
    # 为每个扫描变量生成 modify 占位
    sweep_vars = config.get("sweep", {}).get("variables", {})
    for var_name in sweep_vars:
        lines.append(f'    <command cmdType="modify" obj1="var" name="{var_name}" value="<{var_name}_VALUE>" />')

    lines.extend([
        '    <command cmdType="delete" obj1="mesh" />',
        '    <command cmdType="sim" solver="auto" />',
    ])

    for result in config.get("results", []):
        rtype = result.get("type", "port")
        rname = _xml_escape(result["name"])
        if rtype in ("port",):
            lines.append(f'    <command cmdType="export" obj1="result" obj2="port" name="{rname}" file="<PORT_FILE>" />')
        elif rtype in ("observer", "obv"):
            lines.append(f'    <command cmdType="export" obj1="result" obj2="observer" name="{rname}" file="<OBSERVER_FILE>" />')

    lines.extend([
        '    <command cmdType="close" obj1="project" />',
        '    <command cmdType="close" obj1="gui" />',
        '</script>',
    ])
    return "\n".join(lines) + "\n"


def _generate_matlab_modify_script(config: dict[str, Any]) -> str:
    """生成 modify_script.m 子程序（通用，支持多变量和 observer/port 路径替换）。"""
    sweep_vars = list(config.get("sweep", {}).get("variables", {}).keys())
    has_observer = any(r.get("type") in ("observer", "obv") for r in config.get("results", []))
    has_port = any(r.get("type") == "port" for r in config.get("results", []))
    obv_name = ""
    port_name = ""
    for r in config.get("results", []):
        if r.get("type") in ("observer", "obv") and not obv_name:
            obv_name = r["name"]
        if r.get("type") == "port" and not port_name:
            port_name = r["name"]

    var_modify_lines = []
    for var_name in sweep_vars:
        var_modify_lines.append(
            f'        if strcmpi(cmdNode.getAttribute(\'name\'), \'{var_name}\')\n'
            f'            cmdNode.setAttribute(\'value\', var_values{{strcmp(var_names, \'{var_name}\')}});\n'
            f'            ret = ret + 1;\n'
            f'        end'
        )

    return f'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  modify_script.m — 通用 XML 修改子程序（自动生成，不需要改动）
%  功能：读模板 XML → 修改变量值 + 输出文件名 → 写出新 XML
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  输入:
%     src_file   - 模板 XML 路径
%     dst_file   - 目标 XML 路径
%     var_names  - 变量名 cell array
%     var_values - 变量新值 cell array（字符串）
%     obv_set    - Observer 数据集名称（不需要则传 ''）
%     obv_file   - Observer 输出文件路径（不需要则传 ''）
%     port_set   - Port S参数数据集名称
%     port_file  - Port 输出文件路径
%  返回:
%     ret        - 修改成功的变量个数
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function ret = modify_script(src_file, dst_file, var_names, var_values, ...
                              obv_set, obv_file, port_set, port_file)
    ret = 0;
    xmlTree = xmlread(src_file);
    root = xmlTree.item(0);
    cmd_nodes = root.getChildNodes;
    nCmd = cmd_nodes.getLength;

    for count = 1:nCmd
        cmdNode = cmd_nodes.item(count - 1);
        if ~cmdNode.hasAttributes; continue; end

        cmdType  = cmdNode.getAttribute('cmdType');
        obj1Type = cmdNode.getAttribute('obj1');
        obj2Type = cmdNode.getAttribute('obj2');

        % modify:var → 修改变量值
        if strcmpi(cmdType, 'modify') && strcmpi(obj1Type, 'var')
{chr(10).join(var_modify_lines)}
        end

        % export:result → 修改输出文件路径
        if strcmpi(cmdType, 'export') && strcmpi(obj1Type, 'result')
            nodeName = cmdNode.getAttribute('name');
{_gen_matlab_export_block(has_observer, has_port, obv_name, port_name)}
        end
    end
    xmlwrite(dst_file, xmlTree);
end
'''


def _gen_matlab_export_block(has_observer: bool, has_port: bool, obv_name: str, port_name: str) -> str:
    lines = []
    if has_observer:
        lines.append(f'            if strcmpi(obj2Type, \'obv\') || strcmpi(obj2Type, \'observer\')')
        lines.append(f'                if strcmpi(nodeName, \'{obv_name}\')')
        lines.append( '                    cmdNode.setAttribute(\'file\', obv_file);')
        lines.append( '                end')
        lines.append( '            end')
    if has_port:
        lines.append(f'            if strcmpi(obj2Type, \'port\')')
        lines.append(f'                if strcmpi(nodeName, \'{port_name}\')')
        lines.append( '                    cmdNode.setAttribute(\'file\', port_file);')
        lines.append( '                end')
        lines.append( '            end')
    return "\n".join(lines)


def generate_matlab_sweep(config: dict[str, Any]) -> str:
    """生成完整的 MATLAB 单参数扫参主控程序。"""
    work_path = config.get("output_dir", "<OUTPUT_DIR>")
    waveda_exe = config.get("waveda_exe", '"C:\\Program Files\\WavEDA\\WavEDA.exe"')
    sweep_vars = list(config.get("sweep", {}).get("variables", {}).items())
    if not sweep_vars:
        return "% ERROR: No sweep variables defined\n"

    var_name = sweep_vars[0][0]
    var_values = sweep_vars[0][1]
    var_start = var_values[0]
    var_end = var_values[-1]
    var_step = var_values[1] - var_values[0] if len(var_values) > 1 else 1

    has_observer = any(r.get("type") in ("observer", "obv") for r in config.get("results", []))
    obv_name = ""
    port_name = "Port_S_data_1"
    for r in config.get("results", []):
        if r.get("type") in ("observer", "obv") and not obv_name:
            obv_name = r["name"]
        if r.get("type") == "port" and port_name == "Port_S_data_1":
            port_name = r["name"]

    target_freq = config.get("target_freq", 2.45)
    s11_threshold = config.get("s11_threshold", -10)

    # Observer block
    observer_init = ""
    observer_load = ""
    observer_plot = ""
    observer_summary = ""
    if has_observer:
        observer_init = "all_e_max = zeros(num_params,1); all_e_max_time = zeros(num_params,1);\nall_obv = {};"
        observer_load = '''
    % --- Observer ---
    if exist(obv_file, 'file')
        o = load(obv_file); t_vec = o(:,1); e_vec = o(:,2); all_obv{i} = o;
        [all_e_max(i), e_idx] = max(abs(e_vec));
        all_e_max_time(i) = t_vec(e_idx);
    else t_vec=[]; e_vec=[];
    end'''
        observer_plot = '''
    if ~isempty(t_vec)
        subplot(2, num_params, i); plot(t_vec, e_vec, 'b-'); hold on;
        plot(all_e_max_time(i), all_e_max(i)*sign(e_vec(e_idx)), 'ro', 'MarkerSize',6,'MarkerFaceColor','r');
        title(sprintf('%s=%.2f',var_name,current_val),'FontSize',9); xlabel('Time');
    end'''
        observer_summary = "% E场指标"

    modify_script = _generate_matlab_modify_script(config)

    # Dual param mode
    is_dual = len(sweep_vars) == 2
    if is_dual:
        return _generate_matlab_dual_sweep(config)

    return f'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  sweep_main.m — WavEDA 单参数扫参 (自动生成)
%  生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
%  使用前只改下方【用户配置区】（已根据你的设置预填）
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear; clc; close all;

fprintf('===============================================================\\n');
fprintf('    WavEDA 单参数扫参\\n');
fprintf('===============================================================\\n\\n');


%% ╔══════════════════════════════════════════════════════════════╗
%% ║                    【用户配置区】 改这里！                      ║
%% ╚══════════════════════════════════════════════════════════════╝

% ---- 路径 ----
work_path  = '{work_path}\\';
waveda_exe = '{waveda_exe}';

waveda_exe_clean = strrep(waveda_exe, '"', '');
[waveda_dir, waveda_name, waveda_ext] = fileparts(waveda_exe_clean);
waveda_cmd = [waveda_name waveda_ext];

% ---- 文件 ----
template_xml    = [work_path 'template.xml'];
temp_script_xml = [work_path 'temp_script.xml'];

% ---- 扫描参数 ----
var_name  = '{var_name}';
var_start = {var_start};  var_step = {var_step};  var_end = {var_end};

% ---- 数据集名称（.tsp 工程里定义的，不区分大小写） ----
obv_dataset_name  = '{obv_name}';    % 不需要Observer则传 ''
port_dataset_name = '{port_name}';

% ---- S参数分析目标 ----
target_freq   = {target_freq};   % 关心的频率 (GHz)
s11_threshold = {s11_threshold};    % 带宽判定门限 (dB)


%% ╔══════════════════════════════════════════════════════════════╗
%% ║                    初始化                                    ║
%% ╚══════════════════════════════════════════════════════════════╝

param_list = var_start : var_step : var_end;
num_params = length(param_list);
fprintf('扫描变量: %s  (%.2f~%.2f, %d组)\\n\\n', var_name, var_start, var_end, num_params);

% S参数存储
all_s11_min = zeros(num_params,1); all_freq_min = zeros(num_params,1);
all_bw = nan(num_params,1); all_center_f = nan(num_params,1);
all_s11_target = zeros(num_params,1);
all_s11 = {{}}; all_freq = {{}};
{observer_init}


%% ╔══════════════════════════════════════════════════════════════╗
%% ║              预热跑（解决第一次启动慢/易崩的问题）             ║
%% ╚══════════════════════════════════════════════════════════════╝

fprintf('>>> 预热跑: 启动 WavEDA 初始化引擎...\\n');
port_warmup = [work_path 'port_warmup.txt'];

modify_script(template_xml, temp_script_xml, ...
              {{'{var_name}'}}, {{num2str(param_list(1))}}, ...
              obv_dataset_name, [work_path 'obv_warmup.txt'], ...
              port_dataset_name, port_warmup);

bat_file = [work_path 'run_waveda.bat'];
fid = fopen(bat_file, 'w');
fprintf(fid, 'cd /d "%s"\\r\\n', waveda_dir);
fprintf(fid, '%s "script=%s"\\r\\n', waveda_cmd, temp_script_xml);
fclose(fid);

max_retries = 5;
warm_ok = false;
for retry = 1:max_retries
    tic; system(bat_file); elapsed = toc;
    fprintf('          预热尝试 %d/%d, 耗时: %.1f 秒\\n', retry, max_retries, elapsed);
    pause(5);
    if exist(port_warmup, 'file') == 2
        fprintf('          ✅ 预热成功\\n\\n');
        warm_ok = true;
        break;
    else
        fprintf('          ⚠ 预热失败，重试...\\n');
    end
end
if ~warm_ok; fprintf('          ❌ 预热跑 %d 次均失败，脚本终止\\n', max_retries); return; end


%% ╔══════════════════════════════════════════════════════════════╗
%% ║                   扫参主循环                                  ║
%% ╚══════════════════════════════════════════════════════════════╝

for i = 1:num_params
    current_val = param_list(i);
    fprintf('─────────────────────────────────────────────\\n');
    fprintf('[%d/%d] %s = %.2f\\n', i, num_params, var_name, current_val);

    % ===== Part I: 生成脚本 =====
    fprintf('  [Part I] 生成脚本...\\n');
    obv_file  = sprintf('%sobv_data_%%d.txt',  work_path, i);
    port_file = sprintf('%sport_data_%%d.txt', work_path, i);

    ret = modify_script(template_xml, temp_script_xml, ...
                         {{'{var_name}'}}, {{num2str(current_val)}}, ...
                         obv_dataset_name, obv_file, port_dataset_name, port_file);
    fprintf('          修改变量数: %%d\\n', ret);

    % ===== Part II: 运行仿真 =====
    fprintf('  [Part II] 运行仿真...\\n');

    fid = fopen(bat_file, 'w');
    fprintf(fid, 'cd /d "%s"\\r\\n', waveda_dir);
    fprintf(fid, '%s "script=%s"\\r\\n', waveda_cmd, temp_script_xml);
    fclose(fid);

    max_retries = 3;
    success = false;
    for retry = 1:max_retries
        tic; [status, cmdout] = system(bat_file); elapsed = toc;
        fprintf('          尝试 %d/%d, 耗时: %.1f 秒\\n', retry, max_retries, elapsed);
        pause(5);
        if exist(port_file, 'file') == 2
            fprintf('          ✅ 数据文件已生成\\n');
            success = true;
            break;
        else
            fprintf('          ⚠ 文件未生成，重试...\\n');
        end
    end
    if ~success; fprintf('          ❌ 重试失败\\n'); continue; end

    % ===== Part III: 读数据 & 算指标 =====
    fprintf('  [Part III] 提取数据...\\n');

    % --- S参数 ---
    if exist(port_file, 'file')
        p = load(port_file); freq = p(:,1); s11_db = p(:,2);
        all_freq{{i}} = freq; all_s11{{i}} = s11_db;
    else continue; end

    [all_s11_min(i), idx] = min(s11_db); all_freq_min(i) = freq(idx);

    bw_idx = find(s11_db <= s11_threshold);
    if ~isempty(bw_idx) && length(bw_idx) >= 2
        all_bw(i) = freq(bw_idx(end)) - freq(bw_idx(1));
        all_center_f(i) = (freq(bw_idx(1)) + freq(bw_idx(end))) / 2;
    end

    [~, t_idx] = min(abs(freq - target_freq));
    all_s11_target(i) = s11_db(t_idx);
{observer_load}

    % 打印
    fprintf('          S11: min=%.3fdB @%.4fGHz', all_s11_min(i), all_freq_min(i));
    if ~isnan(all_bw(i)); fprintf('  %ddB BW=%.4fGHz', s11_threshold, all_bw(i));
    else fprintf('  BW=未达到'); end
    fprintf('  @%.2fGHz=%.2fdB\\n', target_freq, all_s11_target(i));
    if ~isempty(e_vec); fprintf('          E场: max|E|=%.4f @t=%.4f\\n', all_e_max(i), all_e_max_time(i)); end

    % --- 单组图 ---
    figure(1);
{observer_plot}
    subplot(2, num_params, num_params+i);
    plot(freq, s11_db, 'b-'); hold on;
    plot(all_freq_min(i), all_s11_min(i), 'ro', 'MarkerSize',6,'MarkerFaceColor','r');
    yline(s11_threshold,'r--'); xline(target_freq,'g--');
    title(sprintf('%s=%.2f',var_name,current_val),'FontSize',9); xlabel('Freq(GHz)');
    fprintf('\\n');
end


%% ╔══════════════════════════════════════════════════════════════╗
%% ║           汇总图表                                           ║
%% ╚══════════════════════════════════════════════════════════════╝

fprintf('===============================================================\\n');
fprintf('    生成汇总图表...\\n\\n');

% --- 图2: 全部S11叠加 ---
figure(2); clf; set(gcf,'Position',[50 50 900 500]); hold on;
colors = lines(num_params); v_leg = {{}};
for i = 1:num_params
    if ~isempty(all_freq{{i}})
        plot(all_freq{{i}}, all_s11{{i}}, 'LineWidth',1.5, 'Color',colors(i,:));
        v_leg{{end+1}}=sprintf('%s=%.2f (min=%.2fdB)',var_name,param_list(i),all_s11_min(i));
    end
end
yline(s11_threshold,'r--'); xline(target_freq,'g--');
if ~isempty(v_leg); legend(v_leg,'Location','best','FontSize',8); end
xlabel('频率(GHz)'); ylabel('|S_{{11}}|(dB)'); title(sprintf('S_{{11}} 对比 — %s',var_name)); grid on;

% --- 图3: 指标面板 ---
figure(4); clf; set(gcf,'Position',[150 150 900 700]);
subplot(2,4,1); plot(param_list,all_s11_min,'bo-','LineWidth',1.5,'MarkerSize',8,'MarkerFaceColor','b');
xlabel(var_name); ylabel('Min|S11|(dB)'); title('最小S11'); grid on;
subplot(2,4,2); plot(param_list,all_freq_min,'ro-','LineWidth',1.5,'MarkerSize',8,'MarkerFaceColor','r');
xlabel(var_name); ylabel('Freq(GHz)'); title('谐振频率'); grid on;
subplot(2,4,3); v=~isnan(all_bw); if any(v); plot(param_list(v),all_bw(v),'go-','LineWidth',1.5,'MarkerSize',8,'MarkerFaceColor','g'); end
xlabel(var_name); ylabel('BW(GHz)'); title(sprintf('%ddB带宽',s11_threshold)); grid on;
subplot(2,4,4); plot(param_list,all_s11_target,'co-','LineWidth',1.5,'MarkerSize',8,'MarkerFaceColor','c'); yline(s11_threshold,'r--');
xlabel(var_name); ylabel('S11(dB)'); title(sprintf('@%.2fGHz',target_freq)); grid on;
subplot(2,4,[7 8]); axis off;
[~,bi]=min(all_s11_min);
txt={{'====== 扫参汇总 ======', ...
    sprintf('变量:%s (%.2f~%.2f,%d组)',var_name,var_start,var_end,num_params),'', ...
    sprintf('★ S最优:%s=%.2f  min|S11|=%.3fdB @%.4fGHz',var_name,param_list(bi),all_s11_min(bi),all_freq_min(bi)),''}};
if ~isnan(all_bw(bi)); txt{{end+1}}=sprintf('  (S最优) %ddB BW=%.4fGHz',s11_threshold,all_bw(bi)); end
txt{{end+1}}=sprintf('  (S最优) S11@%.2fGHz=%.3fdB',target_freq,all_s11_target(bi));
text(0,0.5,txt,'FontSize',10,'VerticalAlignment','middle','FontName','FixedWidth');


%% ╔══════════════════════════════════════════════════════════════╗
%% ║              导出汇总表                                      ║
%% ╚══════════════════════════════════════════════════════════════╝

sf=[work_path 'sweep_summary.txt']; fid=fopen(sf,'w');
fprintf(fid,'=====================================================\\n');
fprintf(fid,'  WavEDA 单参数扫参 汇总报告\\n  %s\\n',datestr(now));
fprintf(fid,'=====================================================\\n\\n');
fprintf(fid,'  变量:%s (%.2f~%.2f, %d组)\\n\\n',var_name,var_start,var_end,num_params);
fprintf(fid,'  %-8s | %-10s | %-12s | %-10s | %-10s\\n', ...
    var_name,'Min|S11|','Freq@Min','BW','S11@Tgt');
fprintf(fid,'  %s\\n',repmat('-',1,75));
for i=1:num_params
    bw_s='N/A'; if ~isnan(all_bw(i)); bw_s=sprintf('%.4f',all_bw(i)); end
    fprintf(fid,'  %-8.2f | %-10.3f | %-12.4f | %-10s | %-10.3f\\n', ...
        param_list(i),all_s11_min(i),all_freq_min(i),bw_s,all_s11_target(i));
end
[~,bi]=min(all_s11_min);
fprintf(fid,'\\n  ★ Best(by S11): %s=%.2f\\n',var_name,param_list(bi));
fclose(fid);
fprintf('\\n✅ 汇总表: %s\\n',sf);
fprintf('===============================================================\\n    完成！\\n===============================================================\\n');
'''


def _generate_matlab_dual_sweep(config: dict[str, Any]) -> str:
    """生成双参数 MATLAB 扫参程序。"""
    work_path = config.get("output_dir", "<OUTPUT_DIR>")
    waveda_exe = config.get("waveda_exe", '"C:\\Program Files\\WavEDA\\WavEDA.exe"')
    sweep_vars = list(config.get("sweep", {}).get("variables", {}).items())
    var1_name, var1_vals = sweep_vars[0]
    var2_name, var2_vals = sweep_vars[1]
    n1, n2 = len(var1_vals), len(var2_vals)
    port_name = config["results"][0]["name"] if config.get("results") else "Port_S_data_1"
    target_freq = config.get("target_freq", 2.45)
    s11_threshold = config.get("s11_threshold", -10)

    return f'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  sweep_main_2var.m — WavEDA 双参数扫参 (自动生成)
%  生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
%  总组合: {n1}×{n2}={n1 * n2}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear; clc; close all;

fprintf('===============================================================\\n');
fprintf('    WavEDA 双参数扫参\\n');
fprintf('===============================================================\\n\\n');

% ---- 路径 ----
work_path  = '{work_path}\\';
waveda_exe = '{waveda_exe}';

waveda_exe_clean = strrep(waveda_exe, '"', '');
[waveda_dir, waveda_name, waveda_ext] = fileparts(waveda_exe_clean);
waveda_cmd = [waveda_name waveda_ext];

template_xml    = [work_path 'template.xml'];
temp_script_xml = [work_path 'temp_script.xml'];

var1_name = '{var1_name}';
var2_name = '{var2_name}';
p1 = [{', '.join(str(v) for v in var1_vals)}];
p2 = [{', '.join(str(v) for v in var2_vals)}];
n1 = length(p1); n2 = length(p2); N = n1 * n2;

port_dataset_name = '{port_name}';
target_freq = {target_freq};
s11_threshold = {s11_threshold};

fprintf('变量1:%s (%d组)\\n', var1_name, n1);
fprintf('变量2:%s (%d组)\\n', var2_name, n2);
fprintf('总组合:%d×%d=%d\\n\\n', n1, n2, N);

all_s11_min = zeros(n1,n2); all_freq_min = zeros(n1,n2);
all_bw = nan(n1,n2); all_s11_target = zeros(n1,n2);
all_s11 = cell(n1,n2); all_freq = cell(n1,n2);

% 预热跑
fprintf('>>> 预热跑...\\n');
pw = [work_path 'port_warmup.txt'];
modify_script(template_xml, temp_script_xml, ...
              {{var1_name, var2_name}}, {{num2str(p1(1)), num2str(p2(1))}}, ...
              '', '', port_dataset_name, pw);

bf = [work_path 'run_waveda.bat'];
fid = fopen(bf, 'w');
fprintf(fid, 'cd /d "%s"\\r\\n%s "script=%s"\\r\\n', waveda_dir, waveda_cmd, temp_script_xml);
fclose(fid);

wo = false;
for r = 1:5
    tic; system(bf); elapsed = toc;
    fprintf('          预热尝试 %d/5, 耗时: %.1f 秒\\n', r, elapsed); pause(5);
    if exist(pw, 'file') == 2; fprintf('          ✅ 预热成功\\n\\n'); wo = true; break;
    else fprintf('          ⚠ 预热失败，重试...\\n'); end
end
if ~wo; fprintf('          ❌ 预热失败，脚本终止\\n'); return; end

% 双参数扫参主循环
k = 0;
for i = 1:n1
  for j = 1:n2
    k = k + 1; v1 = p1(i); v2 = p2(j);
    fprintf('─────────────────────────────────────────────\\n');
    fprintf('[%d/%d] %s=%.2f, %s=%.2f\\n', k, N, var1_name, v1, var2_name, v2);

    pf = sprintf('%sport_%%d_%%d.txt', work_path, i, j);
    ret = modify_script(template_xml, temp_script_xml, ...
                         {{var1_name, var2_name}}, {{num2str(v1), num2str(v2)}}, ...
                         '', '', port_dataset_name, pf);
    fprintf('          修改变量数: %d\\n', ret);

    fid = fopen(bf, 'w');
    fprintf(fid, 'cd /d "%s"\\r\\n%s "script=%s"\\r\\n', waveda_dir, waveda_cmd, temp_script_xml);
    fclose(fid);

    ok = false;
    for r = 1:3
        tic; system(bf); elapsed = toc;
        fprintf('          尝试 %d/3, 耗时: %.1f 秒\\n', r, elapsed); pause(5);
        if exist(pf, 'file') == 2; fprintf('          ✅ 数据文件已生成\\n'); ok = true; break;
        else fprintf('          ⚠ 文件未生成，重试...\\n'); end
    end
    if ~ok; fprintf('          ❌ 重试失败\\n'); continue; end

    if exist(pf, 'file')
        d = load(pf); freq = d(:,1); s11 = d(:,2);
        all_freq{{i,j}} = freq; all_s11{{i,j}} = s11;
    else continue; end

    [all_s11_min(i,j), idx] = min(s11); all_freq_min(i,j) = freq(idx);
    bi = find(s11 <= s11_threshold);
    if ~isempty(bi) && length(bi) >= 2
        all_bw(i,j) = freq(bi(end)) - freq(bi(1));
    end
    [~, ti] = min(abs(freq - target_freq));
    all_s11_target(i,j) = s11(ti);

    fprintf('          最小S11:%.3fdB @%.4fGHz\\n', all_s11_min(i,j), all_freq_min(i,j));
    if ~isnan(all_bw(i,j)); fprintf('          %ddB BW=%.4fGHz\\n', s11_threshold, all_bw(i,j));
    else fprintf('          BW=未达到\\n'); end
  end
end

% 汇总图
fprintf('===============================================================\\n    生成汇总图表...\\n\\n');
figure(1); clf; set(gcf, 'Position', [50 50 900 600]); hold on;
C = lines(N); vl = {{}}; ci = 0;
for i = 1:n1; for j = 1:n2; if ~isempty(all_freq{{i,j}})
    ci = ci + 1; plot(all_freq{{i,j}}, all_s11{{i,j}}, 'LineWidth', 1.5, 'Color', C(ci,:));
    vl{{end+1}} = sprintf('%s=%.2f %s=%.2f', var1_name, p1(i), var2_name, p2(j));
end; end; end
yline(s11_threshold, 'r--'); xline(target_freq, 'g--');
if ~isempty(vl); legend(vl, 'Location', 'bestoutside', 'FontSize', 7); end
xlabel('Freq(GHz)'); ylabel('|S11|(dB)');
title(sprintf('S11对比 — %s×%s(%d组)', var1_name, var2_name, N)); grid on;

% 2D热力图
figure(2); clf; set(gcf, 'Position', [100 100 1000 750]);
subplot(2,2,1); imagesc(p2, p1, all_s11_min); xlabel(var2_name); ylabel(var1_name);
title('Min|S11|(dB)'); colorbar; colormap jet; set(gca, 'YDir', 'normal');
subplot(2,2,2); imagesc(p2, p1, all_freq_min); xlabel(var2_name); ylabel(var1_name);
title('谐振频率(GHz)'); colorbar; colormap jet; set(gca, 'YDir', 'normal');

% 导出
sf = [work_path 'sweep_summary_2var.txt'];
fid = fopen(sf, 'w');
fprintf(fid, 'WavEDA 双参数扫参 汇总报告\\n%s\\n', datestr(now));
fprintf(fid, '%s: [%s]  %s: [%s]  共%d组\\n\\n', var1_name, num2str(p1), var2_name, num2str(p2), N);
for i = 1:n1; for j = 1:n2
    bw_s = 'N/A';
    if ~isnan(all_bw(i,j)); bw_s = sprintf('%.4f', all_bw(i,j)); end
    fprintf(fid, '%-8.2f | %-8.2f | %-10.3f | %-12.4f | %-10s\\n', ...
        p1(i), p2(j), all_s11_min(i,j), all_freq_min(i,j), bw_s);
end; end
fclose(fid);
fprintf('\\n✅ 汇总表: %s\\n', sf);
fprintf('===============================================================\\n    完成！\\n===============================================================\\n');
'''


# ── Python 模板生成 ────────────────────────────────────

def generate_python_sweep(config: dict[str, Any]) -> str:
    """生成 Python 版单参数扫参程序（标准库 xml.etree + subprocess）。"""
    work_path = config.get("output_dir", "<OUTPUT_DIR>")
    waveda_exe = config.get("waveda_exe", "C:/Program Files/WavEDA/WavEDA.exe")
    sweep_vars = list(config.get("sweep", {}).get("variables", {}).items())
    if not sweep_vars:
        return "# ERROR: No sweep variables defined\n"

    var_name = sweep_vars[0][0]
    var_values = sweep_vars[0][1]
    var_start = var_values[0]
    var_end = var_values[-1]
    var_step = var_values[1] - var_values[0] if len(var_values) > 1 else 1
    port_name = config["results"][0]["name"] if config.get("results") else "Port_S_data_1"
    target_freq = config.get("target_freq", 2.45)
    s11_threshold = config.get("s11_threshold", -10)

    return f'''##################################################################
#  sweep_main.py — WavEDA 单参数扫参 (Python 版, 自动生成)
#  生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
#  依赖: pip install matplotlib
#  使用前只改下方【用户配置区】（已根据你的设置预填）
##################################################################

import subprocess
import os
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime as dt

try:
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False
    print("[WARN] matplotlib 未安装, 将跳过图表生成. pip install matplotlib")


# ================================================================
#  用户配置区
# ================================================================

WORK_PATH  = r'{work_path}'
WAVEDA_EXE = r'{waveda_exe}'

TEMPLATE_XML    = os.path.join(WORK_PATH, 'template.xml')
TEMP_SCRIPT_XML = os.path.join(WORK_PATH, 'temp_script.xml')

VAR_NAME  = '{var_name}'
VAR_START = {var_start}
VAR_STEP  = {var_step}
VAR_END   = {var_end}

PORT_DATASET_NAME = '{port_name}'
TARGET_FREQ   = {target_freq}
S11_THRESHOLD = {s11_threshold}


# ================================================================
#  初始化
# ================================================================

num_params = round((VAR_END - VAR_START) / VAR_STEP) + 1
param_list = [VAR_START + i * VAR_STEP for i in range(num_params)]

print(f'扫描变量: {{VAR_NAME}}  ({{VAR_START:.2f}}~{{VAR_END:.2f}}, {{num_params}}组)\\n')

all_s11_min = [0.0] * num_params
all_freq_min = [0.0] * num_params
all_bw = [float('nan')] * num_params
all_s11_target = [0.0] * num_params
all_s11 = [None] * num_params
all_freq = [None] * num_params


def extract_col(filepath, col_idx):
    """从空格分隔文本文件中提取列数据"""
    vals = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                s = line.strip()
                if not s or s.startswith('%'):
                    continue
                parts = s.split()
                if len(parts) > col_idx:
                    try:
                        vals.append(float(parts[col_idx]))
                    except ValueError:
                        pass
    except FileNotFoundError:
        pass
    return vals


# ================================================================
#  预热跑
# ================================================================

print('>>> 预热跑: 启动 WavEDA 初始化引擎...')
port_warmup = os.path.join(WORK_PATH, 'port_warmup.txt')
if os.path.exists(port_warmup):
    os.remove(port_warmup)

tree = ET.parse(TEMPLATE_XML)
root = tree.getroot()
for cmd in root.iter('command'):
    ct = (cmd.get('cmdType') or '').lower()
    o1 = (cmd.get('obj1') or '').lower()
    o2 = (cmd.get('obj2') or '').lower()
    if ct == 'modify' and o1 in ('var', 'variable'):
        if (cmd.get('name') or '').lower() == VAR_NAME.lower():
            cmd.set('value', f'{{param_list[0]:.2f}}')
    elif ct == 'export' and o1 == 'result' and o2 == 'port':
        if (cmd.get('name') or '').lower() == PORT_DATASET_NAME.lower():
            cmd.set('file', port_warmup)
tree.write(TEMP_SCRIPT_XML, encoding='utf-8', xml_declaration=True)

waveda_dir = os.path.dirname(WAVEDA_EXE)
waveda_name = os.path.basename(WAVEDA_EXE)
bat_file = os.path.join(WORK_PATH, 'run_waveda.bat')
with open(bat_file, 'w') as f:
    f.write(f'cd /d "{{waveda_dir}}"\\n')
    f.write(f'{{waveda_name}} "script={{TEMP_SCRIPT_XML}}"\\n')

warm_ok = False
for retry in range(5):
    subprocess.run(bat_file, shell=True, capture_output=True)
    time.sleep(5)
    if os.path.exists(port_warmup):
        print(f'          ✅ 预热成功\\n')
        warm_ok = True
        break
    print(f'          ⚠ 预热失败, 重试 ({{retry+1}}/5)')
if not warm_ok:
    print(f'          ❌ 预热失败, 脚本终止')
    sys.exit(1)


# ================================================================
#  扫参主循环
# ================================================================

for i, current_val in enumerate(param_list):
    print(f'[{{i+1}}/{{num_params}}] {{VAR_NAME}} = {{current_val:.2f}}')

    # Part I: 生成 XML
    port_file = os.path.join(WORK_PATH, f'port_data_{{i+1}}.txt')
    if os.path.exists(port_file):
        os.remove(port_file)

    tree = ET.parse(TEMPLATE_XML)
    root = tree.getroot()
    for cmd in root.iter('command'):
        ct = (cmd.get('cmdType') or '').lower()
        o1 = (cmd.get('obj1') or '').lower()
        o2 = (cmd.get('obj2') or '').lower()
        if ct == 'modify' and o1 in ('var', 'variable'):
            if (cmd.get('name') or '').lower() == VAR_NAME.lower():
                cmd.set('value', f'{{current_val:.2f}}')
        elif ct == 'export' and o1 == 'result' and o2 == 'port':
            if (cmd.get('name') or '').lower() == PORT_DATASET_NAME.lower():
                cmd.set('file', port_file)
    tree.write(TEMP_SCRIPT_XML, encoding='utf-8', xml_declaration=True)

    # Part II: 运行仿真
    with open(bat_file, 'w') as f:
        f.write(f'cd /d "{{waveda_dir}}"\\n')
        f.write(f'{{waveda_name}} "script={{TEMP_SCRIPT_XML}}"\\n')

    ok = False
    for retry in range(3):
        subprocess.run(bat_file, shell=True, capture_output=True)
        time.sleep(5)
        if os.path.exists(port_file):
            print(f'  ✅ 文件已生成 (try {{retry+1}})')
            ok = True
            break
        print(f'  ⚠ 文件未生成, 重试 ({{retry+1}}/3)')
    if not ok:
        print('  ❌ 重试失败')
        continue

    # Part III: 读数据 & 算指标
    freq = extract_col(port_file, 0)
    s11_db = extract_col(port_file, 1)
    if not freq or not s11_db:
        continue

    all_freq[i] = freq
    all_s11[i] = s11_db

    min_idx = s11_db.index(min(s11_db))
    all_s11_min[i] = s11_db[min_idx]
    all_freq_min[i] = freq[min_idx]

    bw_idx = [j for j, v in enumerate(s11_db) if v <= S11_THRESHOLD]
    if len(bw_idx) >= 2:
        all_bw[i] = freq[bw_idx[-1]] - freq[bw_idx[0]]

    closest = min(range(len(freq)), key=lambda j: abs(freq[j] - TARGET_FREQ))
    all_s11_target[i] = s11_db[closest]

    print(f'  min S11: {{all_s11_min[i]:.3f}} dB @ {{all_freq_min[i]:.4f}} GHz')


# ================================================================
#  汇总图表
# ================================================================

if HAS_MPL:
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    for i in range(num_params):
        if all_freq[i] is not None:
            ax1.plot(all_freq[i], all_s11[i], linewidth=1.5,
                     label=f'{{VAR_NAME}}={{param_list[i]:.2f}} (min={{all_s11_min[i]:.2f}} dB)')
    ax1.axhline(y=S11_THRESHOLD, color='r', linestyle='--')
    ax1.axvline(x=TARGET_FREQ, color='g', linestyle='--')
    ax1.set_xlabel('Frequency (GHz)')
    ax1.set_ylabel('|S11| (dB)')
    ax1.set_title(f'S11 Comparison — {{VAR_NAME}}')
    ax1.legend(loc='best', fontsize=8)
    ax1.grid(True)
    fig1.tight_layout()
    plt.show()

print(f'\\n✅ 完成！结果目录: {{WORK_PATH}}')
'''


# ── README 生成 ────────────────────────────────────────

def generate_readme(config: dict[str, Any]) -> str:
    """生成运行说明 README.md"""
    sweep_vars = config.get("sweep", {}).get("variables", {})
    strategy = config.get("sweep", {}).get("strategy", "explicit_values")
    controller = config.get("controller", "matlab")
    is_dual = len(sweep_vars) == 2

    var_lines = ""
    for vname, vvals in sweep_vars.items():
        var_lines += f"- **{vname}**: {vvals[0]} ~ {vvals[-1]} ({len(vvals)} 个值)\n"

    strategy_desc = {
        "explicit_values": "显式值列表",
        "coarse_to_fine": "粗到细策略",
        "builtin_sweep": "工程内置扫描",
    }.get(strategy, strategy)

    return f'''# WavEDA 自动化扫参任务

> 生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## 任务概览

| 项目 | 值 |
|------|-----|
| 工程文件 | `{config.get("project_file", "N/A")}` |
| 控制器 | {controller.upper()} |
| 扫描策略 | {strategy_desc} |
| 总组合数 | {_count_combinations(sweep_vars)} |

## 扫参变量

{var_lines}

## 文件说明

```
automation_task/
├── README.md              ← 本文件
├── task_config.json       ← 任务配置（单一真相源）
├── template.xml           ← XML 脚本模板
├── run_batch.{'m' if controller == 'matlab' else 'py'}  ← 主控程序
├── modify_script.m        ← XML 修改子程序 (MATLAB only)
└── output/                ← 运行结果输出目录
    ├── progress.csv
    ├── raw/               ← 各参数点原始数据
    ├── figures/           ← 汇总图表
    └── logs/              ← 日志
```

## 使用方法

### MATLAB
1. 打开 MATLAB，`cd` 到本目录
2. 确认 WavEDA 可执行文件路径正确
3. 运行 `run_batch`

### Python
```bash
pip install matplotlib
python run_batch.py
```

## 注意事项

- 运行前建议先用 GUI 单点验证模型和结果节点
- 几何参数扫描必须强制删除旧网格（默认已启用）
- 每次改变参数后用文件内容判断成功，不依赖退出码
- 如果第二点闪退，检查上一轮 WavEDA 进程是否已结束

## 自定义

如需修改扫参策略、结果节点或目标指标，编辑 `task_config.json` 后重新生成。
'''


def _count_combinations(variables: dict[str, list[float]]) -> int:
    total = 1
    for vals in variables.values():
        total *= len(vals)
    return total


# ── 主入口：一键生成全部文件 ───────────────────────────

def build_task_config(
    project_file: str = "",
    waveda_exe: str = "",
    output_dir: str = "",
    controller: str = "matlab",
    sweep_vars: dict[str, list[float]] | None = None,
    strategy: str = "explicit_values",
    results: list[dict[str, Any]] | None = None,
    target_freq: float = 2.45,
    s11_threshold: float = -10.0,
    timeout_seconds: int = 1800,
    max_attempts: int = 3,
    force_remesh: bool = True,
) -> dict[str, Any]:
    """构建标准 task_config.json"""
    if sweep_vars is None:
        sweep_vars = {}
    if results is None:
        results = [{"name": "Port_S_data_1", "type": "port", "traces": ["S11 dB"]}]

    return {
        "project_file": project_file,
        "waveda_exe": waveda_exe,
        "output_dir": output_dir,
        "controller": controller,
        "sweep": {
            "variables": sweep_vars,
            "strategy": strategy,
            "force_remesh": force_remesh,
        },
        "results": results,
        "target_freq": target_freq,
        "s11_threshold": s11_threshold,
        "reliability": {
            "timeout_seconds": timeout_seconds,
            "max_attempts": max_attempts,
            "resume": True,
        },
    }


class ScriptPackage:
    """一次生成操作产生的完整文件包。"""

    def __init__(self, config: dict[str, Any]) -> None:
        self.config = config
        self.output_dir = Path(config["output_dir"])

    def generate_all(self) -> dict[str, str]:
        """生成所有文件，返回 {文件名: 内容} 字典。"""
        files: dict[str, str] = {}

        # task_config.json
        files["task_config.json"] = json.dumps(self.config, ensure_ascii=False, indent=2)

        # XML template
        files["template.xml"] = generate_xml_template(self.config)

        # MATLAB
        if self.config.get("controller", "matlab") == "matlab":
            modify_m = _generate_matlab_modify_script(self.config)
            files["modify_script.m"] = modify_m

            sweep_main = generate_matlab_sweep(self.config)
            ext = "m"
            files[f"run_batch.{ext}"] = sweep_main

        # Python
        python_sweep = generate_python_sweep(self.config)
        files["run_batch.py"] = python_sweep

        # README
        files["README.md"] = generate_readme(self.config)

        return files

    def write_all(self) -> Path:
        """生成并写入全部文件到输出目录。"""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        (self.output_dir / "generated_xml").mkdir(exist_ok=True)
        (self.output_dir / "output" / "raw").mkdir(parents=True, exist_ok=True)
        (self.output_dir / "output" / "figures").mkdir(parents=True, exist_ok=True)
        (self.output_dir / "output" / "logs").mkdir(parents=True, exist_ok=True)

        files = self.generate_all()
        for filename, content in files.items():
            out_path = self.output_dir / filename
            out_path.write_text(content, encoding="utf-8")

        return self.output_dir
