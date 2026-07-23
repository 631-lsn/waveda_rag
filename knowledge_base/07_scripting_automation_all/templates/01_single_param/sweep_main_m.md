---
title: 单参数扫参 — 主控程序
category: scripting
tags: [代码, MATLAB, 主控程序, 单参数, 完整]
indexing: true
---

# sweep_main.m — 单参数扫参主控程序

```matlab
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  sweep_main.m — WavEDA 单参数扫参 + S参数 & Observer 双数据分析
%
%  功能：自动扫参数 → 算 S11 + E场指标 → 画汇总图 → 导出报告
%  使用前只改下方【用户配置区】
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear; clc; close all;

fprintf('===============================================================\n');
fprintf('    WavEDA 单参数扫参 — S参数 + Observer 分析\n');
fprintf('===============================================================\n\n');


%% ╔══════════════════════════════════════════════════════════════╗
%% ║                    【用户配置区】 改这里！                     ║
%% ╚══════════════════════════════════════════════════════════════╝

% ---- 路径 ----
work_path  = '你的工作目录\';
waveda_exe = '"C:\Program Files\WavEDA\WavEDA.exe"';

waveda_exe_clean = strrep(waveda_exe, '"', '');
[waveda_dir, waveda_name, waveda_ext] = fileparts(waveda_exe_clean);
waveda_cmd = [waveda_name waveda_ext];

% ---- 文件 ----
template_xml    = [work_path 'template.xml'];
temp_script_xml = [work_path 'temp_script.xml'];

% ---- 扫描参数 ----
var_name  = '你的变量名';
var_start = 30;  var_step = 2;  var_end = 40;

% ---- 数据集名称（.tsp 工程里定义的，不区分大小写） ----
obv_dataset_name  = '你的Observer数据集名';    % 不需要Observer则传 ''
port_dataset_name = '你的Port_S参数数据集名';

% ---- S参数分析目标 ----
target_freq   = 2.45;   % 关心的频率 (GHz)
s11_threshold = -10;    % 带宽判定门限 (dB)


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
all_s11 = {}; all_freq = {};

% Observer存储
all_e_max = zeros(num_params,1); all_e_max_time = zeros(num_params,1);
all_obv = {};


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
        all_freq{i} = freq; all_s11{i} = s11_db;
    else continue; end

    [all_s11_min(i), idx] = min(s11_db); all_freq_min(i) = freq(idx);

    bw_idx = find(s11_db <= s11_threshold);
    if ~isempty(bw_idx) && length(bw_idx) >= 2
        all_bw(i) = freq(bw_idx(end)) - freq(bw_idx(1));
        all_center_f(i) = (freq(bw_idx(1)) + freq(bw_idx(end))) / 2;
    end

    [~, t_idx] = min(abs(freq - target_freq));
    all_s11_target(i) = s11_db(t_idx);

    % --- Observer ---
    if exist(obv_file, 'file')
        o = load(obv_file); t_vec = o(:,1); e_vec = o(:,2); all_obv{i} = o;
        [all_e_max(i), e_idx] = max(abs(e_vec));
        all_e_max_time(i) = t_vec(e_idx);
    else t_vec=[]; e_vec=[];
    end

    % 打印
    fprintf('          S11: min=%.3fdB @%.4fGHz', all_s11_min(i), all_freq_min(i));
    if ~isnan(all_bw(i)); fprintf('  %ddB BW=%.4fGHz', s11_threshold, all_bw(i));
    else fprintf('  BW=未达到'); end
    fprintf('  @%.2fGHz=%.2fdB\n', target_freq, all_s11_target(i));
    if ~isempty(e_vec); fprintf('          E场: max|E|=%.4f @t=%.4f\n', all_e_max(i), all_e_max_time(i)); end

    % --- 单组图 ---
    figure(1);
    if ~isempty(t_vec)
        subplot(2, num_params, i); plot(t_vec, e_vec, 'b-'); hold on;
        plot(all_e_max_time(i), all_e_max(i)*sign(e_vec(e_idx)), 'ro', 'MarkerSize',6,'MarkerFaceColor','r');
        title(sprintf('%s=%.2f',var_name,current_val),'FontSize',9); xlabel('Time');
    end
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
colors = lines(num_params); v_leg = {};
for i = 1:num_params
    if ~isempty(all_freq{i})
        plot(all_freq{i}, all_s11{i}, 'LineWidth',1.5, 'Color',colors(i,:));
        v_leg{end+1}=sprintf('%s=%.2f (min=%.2fdB)',var_name,param_list(i),all_s11_min(i));
    end
end
yline(s11_threshold,'r--'); xline(target_freq,'g--');
if ~isempty(v_leg); legend(v_leg,'Location','best','FontSize',8); end
xlabel('频率(GHz)'); ylabel('|S_{11}|(dB)'); title(sprintf('S_{11} 对比 — %s',var_name)); grid on;

% --- 图3: 全部Observer叠加 ---
figure(3); clf; set(gcf,'Position',[100 100 900 500]); hold on;
o_leg = {};
for i = 1:num_params
    if ~isempty(all_obv{i})
        plot(all_obv{i}(:,1), all_obv{i}(:,2), 'LineWidth',1.5, 'Color',colors(i,:));
        o_leg{end+1}=sprintf('%s=%.2f',var_name,param_list(i));
    end
end
if ~isempty(o_leg); legend(o_leg,'Location','best','FontSize',8); end
xlabel('Time'); ylabel('E Field'); title(sprintf('Observer E场 对比 — %s',var_name)); grid on;

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
subplot(2,4,5); plot(param_list,all_e_max,'mo-','LineWidth',1.5,'MarkerSize',8,'MarkerFaceColor','m');
xlabel(var_name); ylabel('|E|max'); title('O: 最大|E|'); grid on;
subplot(2,4,6); plot(param_list,all_e_max_time,'ko-','LineWidth',1.5,'MarkerSize',8,'MarkerFaceColor','k');
xlabel(var_name); ylabel('Time'); title('O: |E|max时刻'); grid on;
subplot(2,4,[7 8]); axis off;
[~,bi]=min(all_s11_min); [~,be]=max(all_e_max);
txt={'====== 扫参汇总 ======', ...
    sprintf('变量:%s (%.2f~%.2f,%d组)',var_name,var_start,var_end,num_params),'', ...
    sprintf('★ S最优:%s=%.2f  min|S11|=%.3fdB @%.4fGHz',var_name,param_list(bi),all_s11_min(bi),all_freq_min(bi)), ...
    sprintf('★ E最优:%s=%.2f  max|E|=%.4f @t=%.4f',var_name,param_list(be),all_e_max(be),all_e_max_time(be)),''};
if ~isnan(all_bw(bi)); txt{end+1}=sprintf('  (S最优) %ddB BW=%.4fGHz',s11_threshold,all_bw(bi)); end
txt{end+1}=sprintf('  (S最优) S11@%.2fGHz=%.3fdB',target_freq,all_s11_target(bi));
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
```
