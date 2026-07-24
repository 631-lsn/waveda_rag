"""
WavEDA 脚本自动生成引擎
基于 07_scripting_automation_all 知识库中已验证的模板代码，
只替换用户配置区，保持核心逻辑不变。
"""
from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any

# ═══════════════════════════════════════════════════════════════
#  已验证的代码模板（来自 knowledge_base/07_.../templates/）
#  标记 <<<CONFIG_START>>> ... <<<CONFIG_END>>> 为用户配置区
# ═══════════════════════════════════════════════════════════════

# ── modify_script.m（单参数，来自 01_single_param/modify_script_m.md）──
MODIFY_SCRIPT_M = r"""%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  modify_script.m — 通用子程序（不需要改动）
%  功能：读模板 XML → 修改变量值 + 输出文件名 → 写出新 XML
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  输入:
%     src_file   - 模板 XML 路径
%     dst_file   - 目标 XML 路径
%     var_name   - 变量名
%     var_value  - 变量新值 (字符串)
%     obv_set    - Observer 数据集名称（不需要则传 ''）
%     obv_file   - Observer 输出文件路径（不需要则传 ''）
%     port_set   - Port S参数数据集名称
%     port_file  - Port 输出文件路径
%  返回:
%     ret        - 修改成功的变量个数
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function ret = modify_script(src_file, dst_file, var_name, var_value, ...
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
            if strcmpi(cmdNode.getAttribute('name'), var_name)
                cmdNode.setAttribute('value', var_value);
                ret = ret + 1;
            end
        end

        % export:result → 修改输出文件路径
        if strcmpi(cmdType, 'export') && strcmpi(obj1Type, 'result')
            nodeName = cmdNode.getAttribute('name');
            if strcmpi(obj2Type, 'obv') || strcmpi(obj2Type, 'observer')
                if strcmpi(nodeName, obv_set)
                    cmdNode.setAttribute('file', obv_file);
                end
            end
            if strcmpi(obj2Type, 'port')
                if strcmpi(nodeName, port_set)
                    cmdNode.setAttribute('file', port_file);
                end
            end
        end
    end
    xmlwrite(dst_file, xmlTree);
end
"""

# ── 单参数 sweep_main.m（来自 01_single_param/sweep_main_m.md）──
SWEEP_MAIN_M = r"""%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  sweep_main.m — WavEDA 单参数扫参 + S参数 & Observer 双数据分析
%
%  功能：自动扫参数 → 算 S11 + E场指标 → 画汇总图 → 导出报告
%  使用前只改下方【用户配置区】
%  生成时间: $GEN_TIME
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear; clc; close all;

fprintf('===============================================================\n');
fprintf('    WavEDA 单参数扫参 — S参数 + Observer 分析\n');
fprintf('===============================================================\n\n');


%% ╔══════════════════════════════════════════════════════════════╗
%% ║                    【用户配置区】 改这里！                     ║
%% ╚══════════════════════════════════════════════════════════════╝
$USER_CONFIG
%% ╔══════════════════════════════════════════════════════════════╗
%% ║                    初始化                                    ║
%% ╚══════════════════════════════════════════════════════════════╝

param_list = var_start : var_step : var_end;
num_params = length(param_list);
fprintf('扫描变量: %s  (%.2f~%.2f, %d组)\n\n', var_name, var_start, var_end, num_params);

% S参数存储
all_s11_min = zeros(num_params,1); all_freq_min = zeros(num_params,1);
all_bw = nan(num_params,1); all_center_f = nan(num_params,1);
all_s11_target = zeros(num_params,1);
all_s11 = {{}}; all_freq = {{}};
$OBS_INIT

%% ╔══════════════════════════════════════════════════════════════╗
%% ║              预热跑（解决第一次启动慢/易崩的问题）             ║
%% ╚══════════════════════════════════════════════════════════════╝

fprintf('>>> 预热跑: 启动 WavEDA 初始化引擎...\n');
port_warmup = [work_path 'port_warmup.txt'];

modify_script(template_xml, temp_script_xml, var_name, num2str(param_list(1)), ...
              obv_dataset_name, [work_path 'obv_warmup.txt'], ...
              port_dataset_name, port_warmup);

bat_file = [work_path 'run_waveda.bat'];
fid = fopen(bat_file, 'w');
fprintf(fid, 'cd /d "%s"\r\n', waveda_dir);
fprintf(fid, '%s "script=%s"\r\n', waveda_cmd, temp_script_xml);
fclose(fid);

max_retries = 5;
warm_ok = false;
for retry = 1:max_retries
    tic; system(bat_file); elapsed = toc;
    fprintf('          预热尝试 %d/%d, 耗时: %.1f 秒\n', retry, max_retries, elapsed);
    pause(5);
    if exist(port_warmup, 'file') == 2
        fprintf('          ✅ 预热成功\n\n');
        warm_ok = true;
        break;
    else
        fprintf('          ⚠ 预热失败，重试...\n');
    end
end
if ~warm_ok; fprintf('          ❌ 预热跑 %d 次均失败，脚本终止\n', max_retries); return; end


%% ╔══════════════════════════════════════════════════════════════╗
%% ║                   扫参主循环                                  ║
%% ╚══════════════════════════════════════════════════════════════╝

for i = 1:num_params
    current_val = param_list(i);
    fprintf('─────────────────────────────────────────────\n');
    fprintf('[%d/%d] %s = %.2f\n', i, num_params, var_name, current_val);

    % ===== Part I: 生成脚本 =====
    fprintf('  [Part I] 生成脚本...\n');
    obv_file  = sprintf('%sobv_data_%d.txt',  work_path, i);
    port_file = sprintf('%sport_data_%d.txt', work_path, i);

    ret = modify_script(template_xml, temp_script_xml, var_name, num2str(current_val), ...
                         obv_dataset_name, obv_file, port_dataset_name, port_file);
    fprintf('          修改变量数: %d\n', ret);

    % ===== Part II: 运行仿真 =====
    fprintf('  [Part II] 运行仿真...\n');

    fid = fopen(bat_file, 'w');
    fprintf(fid, 'cd /d "%s"\r\n', waveda_dir);
    fprintf(fid, '%s "script=%s"\r\n', waveda_cmd, temp_script_xml);
    fclose(fid);

    max_retries = 3;
    success = false;
    for retry = 1:max_retries
        tic; [status, cmdout] = system(bat_file); elapsed = toc;
        fprintf('          尝试 %d/%d, 耗时: %.1f 秒\n', retry, max_retries, elapsed);
        pause(5);
        if exist(port_file, 'file') == 2
            fprintf('          ✅ 数据文件已生成\n');
            success = true;
            break;
        else
            fprintf('          ⚠ 文件未生成，重试...\n');
        end
    end
    if ~success; fprintf('          ❌ 重试失败\n'); continue; end

    % ===== Part III: 读数据 & 算指标 =====
    fprintf('  [Part III] 提取数据...\n');

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
$OBS_LOAD

    % 打印
    fprintf('          S11: min=%.3fdB @%.4fGHz', all_s11_min(i), all_freq_min(i));
    if ~isnan(all_bw(i)); fprintf('  %ddB BW=%.4fGHz', s11_threshold, all_bw(i));
    else fprintf('  BW=未达到'); end
    fprintf('  @%.2fGHz=%.2fdB\n', target_freq, all_s11_target(i));
$OBS_PRINT

    % --- 单组图 ---
    figure(1);
$OBS_PLOT_SINGLE
    subplot(2, num_params, num_params+i);
    plot(freq, s11_db, 'b-'); hold on;
    plot(all_freq_min(i), all_s11_min(i), 'ro', 'MarkerSize',6,'MarkerFaceColor','r');
    yline(s11_threshold,'r--'); xline(target_freq,'g--');
    title(sprintf('%s=%.2f',var_name,current_val),'FontSize',9); xlabel('Freq(GHz)');
    fprintf('\n');
end


%% ╔══════════════════════════════════════════════════════════════╗
%% ║           汇总图表                                            ║
%% ╚══════════════════════════════════════════════════════════════╝

fprintf('===============================================================\n');
fprintf('    生成汇总图表...\n\n');

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
xlabel('频率(GHz)'); ylabel('|S_{11}|(dB)'); title(sprintf('S_{11} 对比 — %s',var_name)); grid on;
$OBS_PLOT_OVERLAY

% --- 图4: 指标面板 ---
figure(4); clf; set(gcf,'Position',[150 150 900 700]);
subplot(2,4,1); plot(param_list,all_s11_min,'bo-','LineWidth',1.5,'MarkerSize',8,'MarkerFaceColor','b');
xlabel(var_name); ylabel('Min|S11|(dB)'); title('S: 最小S11'); grid on;
subplot(2,4,2); plot(param_list,all_freq_min,'ro-','LineWidth',1.5,'MarkerSize',8,'MarkerFaceColor','r');
xlabel(var_name); ylabel('Freq(GHz)'); title('S: 谐振频率'); grid on;
subplot(2,4,3); v=~isnan(all_bw); if any(v); plot(param_list(v),all_bw(v),'go-','LineWidth',1.5,'MarkerSize',8,'MarkerFaceColor','g'); end
xlabel(var_name); ylabel('BW(GHz)'); title(sprintf('S: %ddB带宽',s11_threshold)); grid on;
subplot(2,4,4); plot(param_list,all_s11_target,'co-','LineWidth',1.5,'MarkerSize',8,'MarkerFaceColor','c'); yline(s11_threshold,'r--');
xlabel(var_name); ylabel('S11(dB)'); title(sprintf('S: @%.2fGHz',target_freq)); grid on;
$OBS_PANEL
subplot(2,4,[7 8]); axis off;
[~,bi]=min(all_s11_min); [~,be]=max(all_e_max);
txt={{'====== 扫参汇总 ======', ...
    sprintf('变量:%s (%.2f~%.2f,%d组)',var_name,var_start,var_end,num_params),'', ...
    sprintf('★ S最优:%s=%.2f  min|S11|=%.3fdB @%.4fGHz',var_name,param_list(bi),all_s11_min(bi),all_freq_min(bi)), ...
    sprintf('★ E最优:%s=%.2f  max|E|=%.4f @t=%.4f',var_name,param_list(be),all_e_max(be),all_e_max_time(be)),''}};
if ~isnan(all_bw(bi)); txt{{end+1}}=sprintf('  (S最优) %ddB BW=%.4fGHz',s11_threshold,all_bw(bi)); end
txt{{end+1}}=sprintf('  (S最优) S11@%.2fGHz=%.3fdB',target_freq,all_s11_target(bi));
text(0,0.5,txt,'FontSize',10,'VerticalAlignment','middle','FontName','FixedWidth');


%% ╔══════════════════════════════════════════════════════════════╗
%% ║              导出汇总表                                      ║
%% ╚══════════════════════════════════════════════════════════════╝

sf=[work_path 'sweep_summary.txt']; fid=fopen(sf,'w');
fprintf(fid,'=====================================================\n');
fprintf(fid,'  WavEDA 单参数扫参 汇总报告\n  %s\n',datestr(now));
fprintf(fid,'=====================================================\n\n');
fprintf(fid,'  变量:%s (%.2f~%.2f, %d组)\n\n',var_name,var_start,var_end,num_params);
fprintf(fid,'  %-8s | %-10s | %-12s | %-10s | %-10s | %-10s | %-10s\n', ...
    var_name,'Min|S11|','Freq@Min','BW','S11@Tgt','|E|max','E@Time');
fprintf(fid,'  %s\n',repmat('-',1,95));
for i=1:num_params
    bw_s='N/A'; if ~isnan(all_bw(i)); bw_s=sprintf('%.4f',all_bw(i)); end
    fprintf(fid,'  %-8.2f | %-10.3f | %-12.4f | %-10s | %-10.3f | %-10.4f | %-10.4f\n', ...
        param_list(i),all_s11_min(i),all_freq_min(i),bw_s,all_s11_target(i),all_e_max(i),all_e_max_time(i));
end
[~,bi]=min(all_s11_min);
fprintf(fid,'\n  ★ Best(by S11): %s=%.2f\n',var_name,param_list(bi));
fclose(fid);
fprintf('\n✅ 汇总表: %s\n',sf);
fprintf('===============================================================\n    完成！\n===============================================================\n');
"""

# ── modify_script_2var.m（双参数，来自 02_dual_param/modify_script_2var_m.md）──
MODIFY_SCRIPT_2VAR_M = r"""%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  modify_script_2var.m — 通用子程序（不需要改动）
%  功能：读模板 XML → 修改两个变量值 + Port输出文件名 → 写出新 XML
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function ret = modify_script_2var(src, dst, v1n, v1v, v2n, v2v, pset, pfile)
    ret = 0;
    t = xmlread(src); r = t.item(0);
    for c = 1:r.getChildNodes.getLength
        n = r.getChildNodes.item(c-1);
        if ~n.hasAttributes; continue; end
        ct = n.getAttribute('cmdType'); o1 = n.getAttribute('obj1'); o2 = n.getAttribute('obj2');
        if strcmpi(ct,'modify') && strcmpi(o1,'var')
            nn = n.getAttribute('name');
            if strcmpi(nn,v1n); n.setAttribute('value',v1v); ret=ret+1; end
            if strcmpi(nn,v2n); n.setAttribute('value',v2v); ret=ret+1; end
        end
        if strcmpi(ct,'export') && strcmpi(o1,'result') && strcmpi(o2,'port')
            if strcmpi(n.getAttribute('name'),pset); n.setAttribute('file',pfile); end
        end
    end
    xmlwrite(dst,t);
end
"""

# ── 双参数 sweep_main_2var.m（来自 02_dual_param/sweep_main_2var_m.md）──
SWEEP_MAIN_2VAR_M = r"""%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  sweep_main_2var.m — WavEDA 双参数扫参（嵌套循环遍历所有组合）
%
%  功能：两变量嵌套循环 → S参数分析 → 1D对比 + 2D热力图 + 3D曲面
%  使用前只改下方【用户配置区】
%  生成时间: $GEN_TIME
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear; clc; close all;

fprintf('===============================================================\n');
fprintf('    WavEDA 双参数扫参\n');
fprintf('===============================================================\n\n');


%% ╔══════════════════════════════════════════════════════════════╗
%% ║                    【用户配置区】 改这里！                     ║
%% ╚══════════════════════════════════════════════════════════════╝
$USER_CONFIG
%% ╔══════════════════════════════════════════════════════════════╗
%% ║                    初始化                                    ║
%% ╚══════════════════════════════════════════════════════════════╝

p1 = var1_start:var1_step:var1_end; p2 = var2_start:var2_step:var2_end;
n1=length(p1); n2=length(p2); N=n1*n2;
fprintf('变量1:%s (%.2f~%.2f,%d组)\n',var1_name,var1_start,var1_end,n1);
fprintf('变量2:%s (%.2f~%.2f,%d组)\n',var2_name,var2_start,var2_end,n2);
fprintf('总组合:%d×%d=%d\n\n',n1,n2,N);

all_s11_min=zeros(n1,n2); all_freq_min=zeros(n1,n2);
all_bw=nan(n1,n2); all_center_f=nan(n1,n2); all_s11_target=zeros(n1,n2);
all_s11=cell(n1,n2); all_freq=cell(n1,n2);


%% ╔══════════════════════════════════════════════════════════════╗
%% ║              预热跑                                          ║
%% ╚══════════════════════════════════════════════════════════════╝

fprintf('>>> 预热跑...\n');
pw=[work_path 'port_warmup.txt'];
modify_script_2var(template_xml,temp_script_xml,var1_name,num2str(p1(1)),var2_name,num2str(p2(1)),port_dataset_name,pw);

bf=[work_path 'run_waveda.bat']; fid=fopen(bf,'w');
fprintf(fid,'cd /d "%s"\r\n%s "script=%s"\r\n',waveda_dir,waveda_cmd,temp_script_xml); fclose(fid);

wo=false;
for r=1:5
    tic; system(bf); elapsed=toc;
    fprintf('          预热尝试 %d/5, 耗时: %.1f 秒\n',r,elapsed); pause(5);
    if exist(pw,'file')==2; fprintf('          ✅ 预热成功\n\n'); wo=true; break;
    else fprintf('          ⚠ 预热失败，重试...\n'); end
end
if ~wo; fprintf('          ❌ 预热失败，脚本终止\n'); return; end


%% ╔══════════════════════════════════════════════════════════════╗
%% ║              双参数扫参主循环（嵌套）                          ║
%% ╚══════════════════════════════════════════════════════════════╝

k=0;
for i=1:n1
  for j=1:n2
    k=k+1; v1=p1(i); v2=p2(j);
    fprintf('─────────────────────────────────────────────\n');
    fprintf('[%d/%d] %s=%.2f, %s=%.2f\n',k,N,var1_name,v1,var2_name,v2);

    % Part I
    fprintf('  [Part I] 生成脚本...\n');
    pf=sprintf('%sport_%d_%d.txt',work_path,i,j);
    ret=modify_script_2var(template_xml,temp_script_xml,var1_name,num2str(v1),var2_name,num2str(v2),port_dataset_name,pf);
    fprintf('          修改变量数:%d\n',ret);

    % Part II
    fprintf('  [Part II] 运行仿真...\n');
    fid=fopen(bf,'w'); fprintf(fid,'cd /d "%s"\r\n%s "script=%s"\r\n',waveda_dir,waveda_cmd,temp_script_xml); fclose(fid);

    ok=false;
    for r=1:3
        tic; system(bf); elapsed=toc;
        fprintf('          尝试 %d/3, 耗时: %.1f 秒\n',r,elapsed); pause(5);
        if exist(pf,'file')==2; fprintf('          ✅ 数据文件已生成\n'); ok=true; break;
        else fprintf('          ⚠ 文件未生成，重试...\n'); end
    end
    if ~ok; fprintf('          ❌ 重试失败\n'); continue; end

    % Part III
    fprintf('  [Part III] 提取数据...\n');
    if exist(pf,'file')
        d=load(pf); freq=d(:,1); s11=d(:,2); all_freq{{i,j}}=freq; all_s11{{i,j}}=s11;
    else continue; end

    [all_s11_min(i,j),idx]=min(s11); all_freq_min(i,j)=freq(idx);
    bi=find(s11<=s11_threshold);
    if ~isempty(bi)&&length(bi)>=2; all_bw(i,j)=freq(bi(end))-freq(bi(1)); all_center_f(i,j)=(freq(bi(1))+freq(bi(end)))/2; end
    [~,ti]=min(abs(freq-target_freq)); all_s11_target(i,j)=s11(ti);

    fprintf('          最小S11:%.3fdB @%.4fGHz',all_s11_min(i,j),all_freq_min(i,j));
    if ~isnan(all_bw(i,j)); fprintf('  %ddB BW=%.4fGHz\n',s11_threshold,all_bw(i,j));
    else fprintf('  BW=未达到\n'); end
    fprintf('\n');
  end
end


%% ╔══════════════════════════════════════════════════════════════╗
%% ║           图1: 全部S11叠加                                   ║
%% ╚══════════════════════════════════════════════════════════════╝

fprintf('===============================================================\n    生成汇总图表...\n\n');
figure(1);clf;set(gcf,'Position',[50 50 900 600]);hold on;
C=lines(N); vl={{}}; ci=0;
for i=1:n1 for j=1:n2; if ~isempty(all_freq{{i,j}})
    ci=ci+1; plot(all_freq{{i,j}},all_s11{{i,j}},'LineWidth',1.5,'Color',C(ci,:));
    vl{{end+1}}=sprintf('%s=%.2f %s=%.2f',var1_name,p1(i),var2_name,p2(j));
end; end; end
yline(s11_threshold,'r--'); xline(target_freq,'g--');
if ~isempty(vl); legend(vl,'Location','bestoutside','FontSize',7); end
xlabel('Freq(GHz)');ylabel('|S11|(dB)');title(sprintf('S11对比 — %s×%s(%d组)',var1_name,var2_name,N));grid on;

% --- 图2: 2D热力图 ---
figure(2);clf;set(gcf,'Position',[100 100 1000 750]);
subplot(2,2,1); imagesc(p2,p1,all_s11_min); xlabel(var2_name);ylabel(var1_name);title('Min|S11|(dB)');colorbar;colormap jet;set(gca,'YDir','normal');
for i=1:n1 for j=1:n2; if all_s11_min(i,j)~=0; text(p2(j),p1(i),sprintf('%.1f',all_s11_min(i,j)),'HorizontalAlignment','center','Color','w','FontSize',8,'FontWeight','bold');end;end;end
subplot(2,2,2); imagesc(p2,p1,all_freq_min); xlabel(var2_name);ylabel(var1_name);title('谐振频率(GHz)');colorbar;colormap jet;set(gca,'YDir','normal');
for i=1:n1 for j=1:n2; if all_freq_min(i,j)~=0; text(p2(j),p1(i),sprintf('%.2f',all_freq_min(i,j)),'HorizontalAlignment','center','Color','w','FontSize',7,'FontWeight','bold');end;end;end
subplot(2,2,3); imagesc(p2,p1,all_bw); xlabel(var2_name);ylabel(var1_name);title(sprintf('%ddB带宽(GHz)',s11_threshold));colorbar;colormap jet;set(gca,'YDir','normal');
for i=1:n1 for j=1:n2; if ~isnan(all_bw(i,j)); text(p2(j),p1(i),sprintf('%.3f',all_bw(i,j)),'HorizontalAlignment','center','Color','w','FontSize',7,'FontWeight','bold');end;end;end
subplot(2,2,4); imagesc(p2,p1,all_s11_target); xlabel(var2_name);ylabel(var1_name);title(sprintf('S11@%.2fGHz(dB)',target_freq));colorbar;colormap jet;set(gca,'YDir','normal');
for i=1:n1 for j=1:n2; if all_s11_target(i,j)~=0; text(p2(j),p1(i),sprintf('%.2f',all_s11_target(i,j)),'HorizontalAlignment','center','Color','w','FontSize',7,'FontWeight','bold');end;end;end

% --- 图3: 3D曲面 + 切片 ---
figure(3);clf;set(gcf,'Position',[150 150 900 600]);
[mv,mi]=min(all_s11_min(:)); [bi,bj]=ind2sub([n1 n2],mi);
subplot(2,3,1); surf(p2,p1,all_s11_min,'EdgeColor','none'); xlabel(var2_name);ylabel(var1_name);zlabel('Min|S11|');title('Min|S11| 3D');colorbar;
subplot(2,3,2); for j=1:n2; plot(p1,all_s11_min(:,j),'o-','LineWidth',1.5);hold on;end; xlabel(var1_name);ylabel('Min|S11|');title(sprintf('vs %s',var1_name));legend(string(p2));grid on;
subplot(2,3,3); for i=1:n1; plot(p2,all_s11_min(i,:),'o-','LineWidth',1.5);hold on;end; xlabel(var2_name);ylabel('Min|S11|');title(sprintf('vs %s',var2_name));legend(string(p1));grid on;
subplot(2,3,4); surf(p2,p1,all_freq_min,'EdgeColor','none'); xlabel(var2_name);ylabel(var1_name);zlabel('Freq');title('谐振频率 3D');colorbar;
subplot(2,3,5); surf(p2,p1,all_bw,'EdgeColor','none'); xlabel(var2_name);ylabel(var1_name);zlabel('BW');title(sprintf('%ddB BW 3D',s11_threshold));colorbar;
subplot(2,3,6);axis off;
txt={{'====== 双参数扫参 ======',sprintf('%s:%.2f~%.2f',var1_name,var1_start,var1_end),sprintf('%s:%.2f~%.2f',var2_name,var2_start,var2_end),sprintf('共%d组',N),'',sprintf('★最优:%s=%.2f, %s=%.2f',var1_name,p1(bi),var2_name,p2(bj)),sprintf('  min|S11|=%.3fdB @%.4fGHz',all_s11_min(bi,bj),all_freq_min(bi,bj)),''}};
if ~isnan(all_bw(bi,bj)); txt{{end+1}}=sprintf('  %ddB BW=%.4fGHz',s11_threshold,all_bw(bi,bj)); end
text(0,0.5,txt,'FontSize',10,'VerticalAlignment','middle','FontName','FixedWidth');


%% ╔══════════════════════════════════════════════════════════════╗
%% ║              导出汇总表                                      ║
%% ╚══════════════════════════════════════════════════════════════╝

sf=[work_path 'sweep_summary_2var.txt']; fid=fopen(sf,'w');
fprintf(fid,'=====================================================\n');
fprintf(fid,'  WavEDA 双参数扫参 汇总报告\n  %s\n',datestr(now));
fprintf(fid,'=====================================================\n\n');
fprintf(fid,'  %s:%.2f~%.2f  %s:%.2f~%.2f  共%d组\n\n',var1_name,var1_start,var1_end,var2_name,var2_start,var2_end,N);
fprintf(fid,'  %-8s | %-8s | %-10s | %-12s | %-10s | %-10s | %-12s\n',var1_name,var2_name,'Min|S11|','Freq@Min','BW','CenterF',sprintf('S11@%.2f',target_freq));
fprintf(fid,'  %s\n',repmat('-',1,95));
for i=1:n1 for j=1:n2
    bw='N/A';cf='N/A'; if ~isnan(all_bw(i,j)); bw=sprintf('%.4f',all_bw(i,j)); cf=sprintf('%.4f',all_center_f(i,j)); end
    fprintf(fid,'  %-8.2f | %-8.2f | %-10.3f | %-12.4f | %-10s | %-10s | %-12.3f\n',p1(i),p2(j),all_s11_min(i,j),all_freq_min(i,j),bw,cf,all_s11_target(i,j));
end; end
fprintf(fid,'\n  ★ Best: %s=%.2f, %s=%.2f  (min|S11|=%.3fdB @%.4fGHz)\n',var1_name,p1(bi),var2_name,p2(bj),all_s11_min(bi,bj),all_freq_min(bi,bj));
fclose(fid);
fprintf('\n✅ 汇总表:%s\n',sf);
fprintf('===============================================================\n    完成！\n===============================================================\n');
"""

# ── Python sweep_main.py（来自 04_python/sweep_main_py.md）──
SWEEP_MAIN_PY = r"""##################################################################
#  sweep_main.py — WavEDA 单参数扫参 (Python 版)
#  生成时间: $GEN_TIME
#  pip install matplotlib
##################################################################

import subprocess
import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from datetime import datetime
import time


# ================================================================
#  数据提取函数（不依赖 pandas/numpy）
# ================================================================

def extract_col(filepath, marker, col_idx):
    '''从空格分隔的文本文件中提取第 col_idx 列数据，跳过注释行'''
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
        print(f'  WARNING 文件不存在: {{filepath}}')
    return vals


# ================================================================
#  【用户配置区】
# ================================================================
$USER_CONFIG_PY
# ================================================================
#  初始化
# ================================================================

num_steps = round((var_end - var_start) / var_step) + 1
param_list = [var_start + i * var_step for i in range(num_steps)]
num_params = len(param_list)

print(f'扫描变量: {$TSP_VAR_NAME}  ({{var_start:.2f}}~{{var_end:.2f}}, {{num_params}}组)\n')

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

    print(f'[{{i+1}}/{{num_params}}] {$TSP_VAR_NAME} = {{current_val:.2f}}')

    # ---- Part I: 修改 XML ----
    port_file = os.path.join(work_path, f'port_data_{{i+1}}.txt')

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
                cmd.set('value', f'{{current_val:.2f}}')

        elif ct_lower == 'export' and o1.lower() == 'result' and o2.lower() == 'port':
            if cmd.get('name', '').lower() == port_dataset_name.lower():
                cmd.set('file', port_file)

    tree.write(temp_script_xml, encoding='utf-8', xml_declaration=True)

    # ---- Part II: 运行仿真 ----
    bat_file = os.path.join(work_path, 'run_waveda.bat')
    waveda_dir = os.path.dirname(waveda_exe)
    waveda_name = os.path.basename(waveda_exe)
    with open(bat_file, 'w') as f:
        f.write(f'cd /d "{{waveda_dir}}"\n')
        f.write(f'{{waveda_name}} "script={{temp_script_xml}}"\n')

    for retry in range(3):
        subprocess.run(bat_file, shell=True, capture_output=True)
        time.sleep(5)
        if os.path.exists(port_file):
            print(f'  ✅ 文件已生成 (try {{retry+1}})')
            break
        print(f'  WARNING 文件未生成，重试 ({{retry+1}}/3)')

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

    print(f'  min S11: {{all_s11_min[i]:.3f}} dB @ {{all_freq_min[i]:.4f}} GHz')


# ================================================================
#  汇总图表
# ================================================================

# 图1: 全部 S11 叠加
fig1, ax1 = plt.subplots(figsize=(10, 6))
for i in range(num_params):
    if all_freq[i] is not None:
        ax1.plot(all_freq[i], all_s11[i], linewidth=1.5,
                 label=f'{$TSP_VAR_NAME}={{param_list[i]:.2f}} (min={{all_s11_min[i]:.2f}} dB)')
ax1.axhline(y=s11_threshold, color='r', linestyle='--')
ax1.axvline(x=target_freq, color='g', linestyle='--')
ax1.set_xlabel('Frequency (GHz)'); ax1.set_ylabel('|S11| (dB)')
ax1.set_title(f'S11 Comparison — {$TSP_VAR_NAME}')
ax1.legend(loc='best', fontsize=8); ax1.grid(True)
fig1.tight_layout()

# 图2: 指标面板
fig2, axes = plt.subplots(2, 3, figsize=(14, 8))
axes[0,0].plot(param_list, all_s11_min, 'bo-'); axes[0,0].set_title('Min |S11|')
axes[0,1].plot(param_list, all_freq_min, 'ro-'); axes[0,1].set_title('Resonant Freq')
valid = [(j,v) for j,v in enumerate(all_bw) if not (isinstance(v,float) and v!=v)]
if valid:
    axes[0,2].plot([param_list[j] for j,_ in valid], [v for _,v in valid], 'go-')
axes[0,2].set_title(f'{{s11_threshold}}dB BW')
axes[1,0].plot(param_list, all_s11_target, 'co-'); axes[1,0].set_title(f'S11@{{target_freq}}GHz')
axes[1,1].axis('off'); axes[1,2].axis('off')
fig2.tight_layout()

plt.show()
"""

# ── single-param XML template（来自 01_single_param/template_xml.md）──
XML_TEMPLATE_SINGLE = """<?xml version="1.0" encoding="UTF-8"?>
<script version="1.0" >
    <!--
    单参数扫参 基础脚本模板 — WavEDA 脚本自动生成器
    生成时间: $GEN_TIME

    【自动填充项】
    load 命令 file="..."    → .tsp 工程路径
    modify 命令 name="..."  → 变量名
    export obv 命令 name="..." → Observer 数据集名
    export port 命令 name="..." → Port S参数数据集名

    【运行时替换项】
    value="..."、file="..." → sweep_main 运行时通过 modify_script 替换
    -->
    <command cmdType="load"   obj1="project"    file="$TSP_PATH" />
    <command cmdType="modify" obj1="var"        name="$TSP_VAR_NAME"    value="$FIRST_VALUE" />
    <command cmdType="delete" obj1="mesh"       />
    <command cmdType="sim"                      solver="auto" />
$EXPORT_COMMANDS
    <command cmdType="close" obj1="project" />
    <command cmdType="close" obj1="gui" />
</script>
"""


# ═══════════════════════════════════════════════════════════════
#  配置区生成函数
# ═══════════════════════════════════════════════════════════════

def _build_single_user_config(config: dict[str, Any]) -> str:
    """生成本地跑单参数的用户配置区。"""
    work_path = config.get("output_dir", "")
    waveda_exe = config.get("waveda_exe", "")
    sweep_vars = list(config.get("sweep", {}).get("variables", {}).items())
    var_name = sweep_vars[0][0]
    var_values = sweep_vars[0][1]

    obv_name = config.get("observer_name", "")
    port_name = config["results"][0]["name"] if config.get("results") else "Port_S_data_1"
    target_freq = config.get("target_freq", 2.45)
    s11_threshold = config.get("s11_threshold", -10)

    return f"""% ---- 路径 ----
work_path  = '{work_path}\\';
waveda_exe = '"{waveda_exe}"';

waveda_exe_clean = strrep(waveda_exe, '"', '');
[waveda_dir, waveda_name, waveda_ext] = fileparts(waveda_exe_clean);
waveda_cmd = [waveda_name waveda_ext];

% ---- 文件 ----
template_xml    = [work_path 'template.xml'];
temp_script_xml = [work_path 'temp_script.xml'];

% ---- 扫描参数 ----
var_name  = '$TSP_VAR_NAME';
var_start = {var_values[0]};  var_step = {var_values[1] - var_values[0]};  var_end = {var_values[-1]};

% ---- 数据集名称（.tsp 工程里定义的，不区分大小写） ----
obv_dataset_name  = '{obv_name}';    % 不需要Observer则传 ''
port_dataset_name = '{port_name}';

% ---- S参数分析目标 ----
target_freq   = {target_freq};   % 关心的频率 (GHz)
s11_threshold = {s11_threshold};    % 带宽判定门限 (dB)"""


def _build_dual_user_config(config: dict[str, Any]) -> str:
    """生成双参数的用户配置区。"""
    work_path = config.get("output_dir", "")
    waveda_exe = config.get("waveda_exe", "")
    sweep_vars = list(config.get("sweep", {}).get("variables", {}).items())
    var1_name, var1_vals = sweep_vars[0]
    var2_name, var2_vals = sweep_vars[1]

    port_name = config["results"][0]["name"] if config.get("results") else "Port_S_data_1"
    target_freq = config.get("target_freq", 2.45)
    s11_threshold = config.get("s11_threshold", -10)

    return f"""% ---- 路径 ----
work_path  = '{work_path}\\';
waveda_exe = '"{waveda_exe}"';

waveda_exe_clean = strrep(waveda_exe, '"', '');
[waveda_dir, waveda_name, waveda_ext] = fileparts(waveda_exe_clean);
waveda_cmd = [waveda_name waveda_ext];

template_xml    = [work_path 'template.xml'];
temp_script_xml = [work_path 'temp_script.xml'];

% ---- 变量1 ----
var1_name  = '{var1_name}';  var1_start = {var1_vals[0]}; var1_step = {var1_vals[1] - var1_vals[0]}; var1_end = {var1_vals[-1]};
% ---- 变量2 ----
var2_name  = '{var2_name}';  var2_start = {var2_vals[0]}; var2_step = {var2_vals[1] - var2_vals[0]}; var2_end = {var2_vals[-1]};

% ---- 数据集 ----
port_dataset_name = '{port_name}';

% ---- 分析目标 ----
target_freq   = {target_freq};  s11_threshold = {s11_threshold};"""


def _build_py_user_config(config: dict[str, Any]) -> str:
    """生成 Python 的用户配置区。"""
    work_path = config.get("output_dir", "")
    waveda_exe = config.get("waveda_exe", "")
    sweep_vars = list(config.get("sweep", {}).get("variables", {}).items())
    var_name = sweep_vars[0][0]
    var_values = sweep_vars[0][1]
    port_name = config["results"][0]["name"] if config.get("results") else "Port_S_data_1"
    target_freq = config.get("target_freq", 2.45)
    s11_threshold = config.get("s11_threshold", -10)

    return f"""work_path  = r'{work_path}'
waveda_exe = r'{waveda_exe}'

template_xml    = os.path.join(work_path, 'template.xml')
temp_script_xml = os.path.join(work_path, 'temp_script.xml')

var_name  = '$TSP_VAR_NAME'
var_start = {var_values[0]}
var_step  = {var_values[1] - var_values[0]}
var_end   = {var_values[-1]}

port_dataset_name = '{port_name}'
target_freq   = {target_freq}
s11_threshold = {s11_threshold}"""


def _build_observer_blocks(config: dict[str, Any]) -> dict[str, str]:
    """生成 Observer 相关的所有代码块。"""
    has_observer = any(r.get("type") in ("observer", "obv") for r in config.get("results", []))
    if not has_observer:
        return {
            "obs_init": "",
            "obs_load": "",
            "obs_print": "",
            "obs_plot_single": "",
            "obs_plot_overlay": "",
            "obs_panel": "",
        }

    return {
        "obs_init": "% Observer存储\nall_e_max = zeros(num_params,1); all_e_max_time = zeros(num_params,1);\nall_obv = {{}};",
        "obs_load": """
    % --- Observer ---
    if exist(obv_file, 'file')
        o = load(obv_file); t_vec = o(:,1); e_vec = o(:,2); all_obv{{i}} = o;
        [all_e_max(i), e_idx] = max(abs(e_vec));
        all_e_max_time(i) = t_vec(e_idx);
    else t_vec=[]; e_vec=[];
    end""",
        "obs_print": "    if ~isempty(e_vec); fprintf('          E场: max|E|=%.4f @t=%.4f\\n', all_e_max(i), all_e_max_time(i)); end",
        "obs_plot_single": """    if ~isempty(t_vec)
        subplot(2, num_params, i); plot(t_vec, e_vec, 'b-'); hold on;
        plot(all_e_max_time(i), all_e_max(i)*sign(e_vec(e_idx)), 'ro', 'MarkerSize',6,'MarkerFaceColor','r');
        title(sprintf('%s=%.2f',var_name,current_val),'FontSize',9); xlabel('Time');
    end""",
        "obs_plot_overlay": """% --- 图3: 全部Observer叠加 ---
figure(3); clf; set(gcf,'Position',[100 100 900 500]); hold on;
o_leg = {{}};
for i = 1:num_params
    if ~isempty(all_obv{{i}})
        plot(all_obv{{i}}(:,1), all_obv{{i}}(:,2), 'LineWidth',1.5, 'Color',colors(i,:));
        o_leg{{end+1}}=sprintf('%s=%.2f',var_name,param_list(i));
    end
end
if ~isempty(o_leg); legend(o_leg,'Location','best','FontSize',8); end
xlabel('Time'); ylabel('E Field'); title(sprintf('Observer E场对比 — %s',var_name)); grid on;""",
        "obs_panel": """subplot(2,4,5); plot(param_list,all_e_max,'mo-','LineWidth',1.5,'MarkerSize',8,'MarkerFaceColor','m');
xlabel(var_name); ylabel('|E|max'); title('O: 最大|E|'); grid on;
subplot(2,4,6); plot(param_list,all_e_max_time,'ko-','LineWidth',1.5,'MarkerSize',8,'MarkerFaceColor','k');
xlabel(var_name); ylabel('Time'); title('O: |E|max时刻'); grid on;""",
    }


def _build_export_commands(config: dict[str, Any]) -> str:
    """构建 XML 中的 export 命令。"""
    lines = []
    for r in config.get("results", []):
        rtype = r.get("type", "port")
        rname = r["name"]
        if rtype in ("observer", "obv"):
            lines.append(f'    <command cmdType="export" obj1="result"  obj2="obv"    name="{rname}"   file="./obv_data.txt" />')
        elif rtype == "port":
            lines.append(f'    <command cmdType="export" obj1="result"  obj2="port"   name="{rname}"        file="./port_data.txt" />')
    return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════
#  主入口
# ═══════════════════════════════════════════════════════════════

def build_task_config(
    project_file: str = "",
    waveda_exe: str = "",
    save_dir: str = "",
    work_dir: str = "",
    controller: str = "matlab",
    sweep_vars: dict[str, list[float]] | None = None,
    strategy: str = "explicit_values",
    results: list[dict[str, Any]] | None = None,
    observer_name: str = "",
    target_freq: float = 2.45,
    s11_threshold: float = -10.0,
    timeout_seconds: int = 1800,
    max_attempts: int = 3,
    force_remesh: bool = True,
) -> dict[str, Any]:
    """构建标准 task_config.json。

    save_dir: 本地保存目录，生成的文件实际写入这里
    work_dir: 目标工作目录，脚本里用的 work_path（异地跑填目标电脑路径）
    """
    if sweep_vars is None:
        sweep_vars = {}
    if results is None:
        results = [{"name": "Port_S_data_1", "type": "port", "traces": ["S11 dB"]}]

    if not work_dir:
        work_dir = save_dir

    return {
        "project_file": project_file,
        "waveda_exe": waveda_exe,
        "save_dir": save_dir,
        "output_dir": work_dir,  # 脚本中使用的 work_path
        "controller": controller,
        "observer_name": observer_name,
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
        self.save_dir = Path(config.get("save_dir", "."))
        self.work_dir = config.get("output_dir", str(self.save_dir))
        self._gen_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def generate_all(self) -> dict[str, str]:
        """生成所有文件，返回 {文件名: 内容} 字典。"""
        files: dict[str, str] = {}
        cfg = self.config
        gen_time = self._gen_time
        sweep_vars = cfg.get("sweep", {}).get("variables", {})
        is_dual = len(sweep_vars) >= 2
        controller = cfg.get("controller", "matlab")

        # task_config.json
        files["task_config.json"] = json.dumps(cfg, ensure_ascii=False, indent=2)

        # Observer blocks
        obs = _build_observer_blocks(cfg)

        # XML template
        export_cmds = _build_export_commands(cfg)
        first_var = list(sweep_vars.keys())[0] if sweep_vars else "VAR"
        first_val = sweep_vars[first_var][0] if sweep_vars else 0
        xml = (XML_TEMPLATE_SINGLE
               .replace("$GEN_TIME", gen_time)
               .replace("$TSP_PATH", cfg.get("project_file", "<PROJECT_FILE>"))
               .replace("$TSP_VAR_NAME", first_var)
               .replace("$FIRST_VALUE", str(first_val))
               .replace("$EXPORT_COMMANDS", export_cmds))
        files["template.xml"] = xml

        if controller == "matlab":
            if is_dual:
                files["modify_script_2var.m"] = MODIFY_SCRIPT_2VAR_M
                user_cfg = _build_dual_user_config(cfg)
                sweep_main = (SWEEP_MAIN_2VAR_M
                              .replace("$GEN_TIME", gen_time)
                              .replace("$USER_CONFIG", user_cfg))
                files["run_batch.m"] = sweep_main
            else:
                files["modify_script.m"] = MODIFY_SCRIPT_M
                user_cfg = _build_single_user_config(cfg)
                sweep_main = (SWEEP_MAIN_M
                              .replace("$GEN_TIME", gen_time)
                              .replace("$USER_CONFIG", user_cfg)
                              .replace("$OBS_INIT", obs.get("obs_init", ""))
                              .replace("$OBS_LOAD", obs.get("obs_load", ""))
                              .replace("$OBS_PRINT", obs.get("obs_print", ""))
                              .replace("$OBS_PLOT_SINGLE", obs.get("obs_plot_single", ""))
                              .replace("$OBS_PLOT_OVERLAY", obs.get("obs_plot_overlay", ""))
                              .replace("$OBS_PANEL", obs.get("obs_panel", "")))
                files["run_batch.m"] = sweep_main

        # Python (always generate)
        if not is_dual:
            py_user = _build_py_user_config(cfg)
            py = (SWEEP_MAIN_PY
                  .replace("$GEN_TIME", gen_time)
                  .replace("$USER_CONFIG_PY", py_user))
            files["run_batch.py"] = py

        # README
        files["README.md"] = self._build_readme()

        return files

    def _build_readme(self) -> str:
        cfg = self.config
        sweep_vars = cfg.get("sweep", {}).get("variables", {})
        total = 1
        for vals in sweep_vars.values():
            total *= len(vals)
        controller = cfg.get("controller", "matlab")

        var_lines = ""
        for vname, vvals in sweep_vars.items():
            var_lines += f"- **{vname}**: {vvals[0]} ~ {vvals[-1]} ({len(vvals)} 个值)\n"

        return f"""# WavEDA 自动化扫参任务

> 生成时间: {self._gen_time}

## 任务概览

| 项目 | 值 |
|------|-----|
| 工程文件 | `{cfg.get("project_file", "N/A")}` |
| 目标工作目录 | `{self.work_dir}` |
| 控制器 | {controller.upper()} |
| 总仿真次数 | {total} |

## 扫参变量

{var_lines}

## 文件说明

```
├── task_config.json       ← 任务配置
├── template.xml           ← XML 脚本模板
├── modify_script.m        ← MATLAB: XML 修改子程序
├── run_batch.m            ← MATLAB: 扫参主控
├── run_batch.py           ← Python: 扫参主控
├── README.md              ← 本文件
└── output/                ← 运行结果
```

## 使用步骤

### MATLAB
1. 把本目录拷贝到目标电脑的 `{self.work_dir}`
2. 打开 `run_batch.m`，检查顶部【用户配置区】的路径
3. 在 MATLAB 中运行 `run_batch`

### Python
```bash
pip install matplotlib
python run_batch.py
```

## 注意事项

- 运行前先在 GUI 中单点验证模型和结果节点
- 几何参数扫描必须强制删除旧网格（XML 已包含）
- 每轮用文件内容判断成功，不依赖 WavEDA 退出码
- 如果第二点闪退，检查上一轮 WavEDA 进程是否已结束
"""

    def write_all(self) -> Path:
        """生成并写入全部文件到本地保存目录。"""
        self.save_dir.mkdir(parents=True, exist_ok=True)
        (self.save_dir / "output").mkdir(exist_ok=True)

        files = self.generate_all()
        for filename, content in files.items():
            out_path = self.save_dir / filename
            out_path.write_text(content, encoding="utf-8")

        return self.save_dir
