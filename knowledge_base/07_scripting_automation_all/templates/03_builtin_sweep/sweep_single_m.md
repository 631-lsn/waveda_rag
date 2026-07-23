---
title: 工程内置扫描 — 主控程序
category: scripting
tags: [代码, MATLAB, 主控程序, 内置扫描, 完整]
indexing: true
---

# sweep_single.m — 工程内置扫描主控程序

```matlab
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  sweep_single.m — 工程内置参数扫描版（WavEDA 只跑一次）
%
%  适用：.tsp 工程已在 GUI 参数扫描模块中配好参数范围
%        WavEDA 一次跑完全部组合，结果全在同一个文件中
%  特点：无循环调 WavEDA，不依赖 modify_script
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear; clc; close all;

fprintf('===============================================================\n');
fprintf('    WavEDA 工程内置扫描 — 单次运行 + 多列数据提取\n');
fprintf('===============================================================\n\n');


%% ╔══════════════════════════════════════════════════════════════╗
%% ║                    【用户配置区】 改这里！                     ║
%% ╚══════════════════════════════════════════════════════════════╝

% ---- 路径 ----
work_path  = '你的工作目录\';
tsp_path   = '你的.tsp工程路径';                      % .tsp 全路径
waveda_exe = '"C:\Program Files\WavEDA\WavEDA.exe"';

waveda_exe_clean = strrep(waveda_exe, '"', '');
[waveda_dir, waveda_name, waveda_ext] = fileparts(waveda_exe_clean);
waveda_cmd = [waveda_name waveda_ext];

% ---- 数据集 ----
port_dataset_name = '你的Port_S参数数据集名';

% ---- 参数列表（必须与 .tsp 工程内置扫描的设定一致！） ----
param_name = '变量名';
param_vals = [30, 32, 34, 36, 38, 40];   % 手动列出所有扫描值

% ---- 分析目标 ----
target_freq   = 2.45;  s11_threshold = -10;


%% ╔══════════════════════════════════════════════════════════════╗
%% ║              生成脚本 & 运行（只跑一次）                       ║
%% ╚══════════════════════════════════════════════════════════════╝

fprintf('工程: %s\n', tsp_path);
fprintf('参数列表: %.2f~%.2f (%d组)\n\n', param_vals(1), param_vals(end), length(param_vals));

fprintf('[准备] 生成脚本...\n');
port_file = [work_path 'port_data.txt'];
script_xml = [work_path 'script.xml'];

fid = fopen(script_xml, 'w');
fprintf(fid, '<?xml version="1.0" encoding="utf-8"?>\n<script version="1.0">\n');
fprintf(fid, '<command cmdType="load" file="%s" obj1="project"/>\n', tsp_path);
fprintf(fid, '<command cmdType="delete" obj1="mesh"/>\n');
fprintf(fid, '<command cmdType="sim" solver="auto"/>\n');
fprintf(fid, '<command cmdType="export" file="%s" name="%s" obj1="result" obj2="port"/>\n', port_file, port_dataset_name);
fprintf(fid, '<command cmdType="close" obj1="project"/>\n');
fprintf(fid, '<command cmdType="close" obj1="gui"/>\n');
fprintf(fid, '</script>\n');
fclose(fid);

fprintf('[运行] 启动 WavEDA...\n');
bat_file = [work_path 'run_waveda.bat'];
fid = fopen(bat_file, 'w');
fprintf(fid, 'cd /d "%s"\r\n', waveda_dir);
fprintf(fid, '%s "script=%s"\r\n', waveda_cmd, script_xml);
fclose(fid);

ok = false;
for r = 1:3
    tic; system(bat_file); elapsed = toc;
    fprintf('          尝试 %d/3, 耗时: %.1f 秒\n', r, elapsed); pause(5);
    if exist(port_file, 'file') == 2
        fprintf('          ✅ 数据文件已生成\n'); ok = true; break;
    else fprintf('          ⚠ 文件未生成，重试...\n'); end
end
if ~ok; fprintf('          ❌ 重试失败\n'); return; end


%% ╔══════════════════════════════════════════════════════════════╗
%% ║              读数据 & 逐列分析（每列 = 一组参数）               ║
%% ╚══════════════════════════════════════════════════════════════╝

fprintf('[分析] 读取数据...\n');
data = load(port_file);
freq = data(:, 1);
n_cols = size(data, 2);
num_params = min(length(param_vals), n_cols - 1);
if num_params < length(param_vals)
    param_vals = param_vals(1:num_params);
end

s11_min=zeros(1,num_params); freq_min=zeros(1,num_params);
bw=nan(1,num_params); cf=nan(1,num_params); s11_t=zeros(1,num_params);

for i = 1:num_params
    s=data(:,i+1);
    [s11_min(i),idx]=min(s); freq_min(i)=freq(idx);
    bi=find(s<=s11_threshold);
    if ~isempty(bi)&&length(bi)>=2; bw(i)=freq(bi(end))-freq(bi(1)); cf(i)=(freq(bi(1))+freq(bi(end)))/2; end
    [~,ti]=min(abs(freq-target_freq)); s11_t(i)=s(ti);
    fprintf('  %s=%.2f  minS11=%.3fdB @%.4fGHz',param_name,param_vals(i),s11_min(i),freq_min(i));
    if ~isnan(bw(i)); fprintf('  BW=%.4fGHz\n',bw(i)); else fprintf('  BW=未达到\n'); end
end


%% ╔══════════════════════════════════════════════════════════════╗
%% ║           汇总图表                                            ║
%% ╚══════════════════════════════════════════════════════════════╝

fprintf('\n===============================================================\n    生成图表...\n\n');

% 图1: 全部S11叠加
figure(1);clf;set(gcf,'Position',[50 50 900 500]);hold on;
C=lines(num_params); vl={};
for i=1:num_params
    plot(freq,data(:,i+1),'LineWidth',1.5,'Color',C(i,:));
    vl{end+1}=sprintf('%s=%.2f (min=%.2fdB)',param_name,param_vals(i),s11_min(i));
end
yline(s11_threshold,'r--');xline(target_freq,'g--');legend(vl,'Location','best','FontSize',8);
xlabel('Freq(GHz)');ylabel('|S11|(dB)');title(sprintf('S11对比 — %s',param_name));grid on;

% 图2: 指标面板
figure(2);clf;set(gcf,'Position',[100 100 900 700]);
subplot(2,3,1);plot(param_vals,s11_min,'bo-','LineWidth',1.5,'MarkerSize',8,'MarkerFaceColor','b');
xlabel(param_name);ylabel('Min|S11|(dB)');title('最小S11');grid on;
subplot(2,3,2);plot(param_vals,freq_min,'ro-','LineWidth',1.5,'MarkerSize',8,'MarkerFaceColor','r');
xlabel(param_name);ylabel('Freq(GHz)');title('谐振频率');grid on;
subplot(2,3,3);v=~isnan(bw);if any(v);plot(param_vals(v),bw(v),'go-','LineWidth',1.5,'MarkerSize',8,'MarkerFaceColor','g');end
xlabel(param_name);ylabel('BW(GHz)');title(sprintf('%ddB带宽',s11_threshold));grid on;
subplot(2,3,4);if any(v);plot(param_vals(v),cf(v),'mo-','LineWidth',1.5,'MarkerSize',8,'MarkerFaceColor','m');end
xlabel(param_name);ylabel('CenterFreq');title('中心频率');grid on;
subplot(2,3,5);plot(param_vals,s11_t,'co-','LineWidth',1.5,'MarkerSize',8,'MarkerFaceColor','c');yline(s11_threshold,'r--');
xlabel(param_name);ylabel(sprintf('S11@%.2fGHz',target_freq));title('目标频率处S11');grid on;
subplot(2,3,6);axis off;
[~,be]=min(s11_min);
txt={'====== 扫描汇总 ======',sprintf('%s:[%s]',param_name,num2str(param_vals)),'',sprintf('★最优:%s=%.2f',param_name,param_vals(be)),sprintf('  min|S11|=%.3fdB @%.4fGHz',s11_min(be),freq_min(be)),''};
if ~isnan(bw(be));txt{end+1}=sprintf('  %ddB BW=%.4fGHz',s11_threshold,bw(be));end
txt{end+1}=sprintf('  S11@%.2fGHz=%.3fdB',target_freq,s11_t(be));
text(0,0.5,txt,'FontSize',10,'VerticalAlignment','middle','FontName','FixedWidth');

% 导出
sf=[work_path 'sweep_summary.txt'];fid=fopen(sf,'w');
fprintf(fid,'=====================================================\n');
fprintf(fid,'  WavEDA 工程内置扫描 报告\n  %s\n',datestr(now));
fprintf(fid,'=====================================================\n\n');
fprintf(fid,'  %s:[%s]  %d组\n\n',param_name,num2str(param_vals),num_params);
fprintf(fid,'  %-8s | %-10s | %-12s | %-10s | %-10s | %-12s\n',param_name,'Min|S11|','Freq@Min','BW','CenterF',sprintf('S11@%.2f',target_freq));
fprintf(fid,'  %s\n',repmat('-',1,80));
for i=1:num_params
    bw_s='N/A'; cf_s='N/A'; if ~isnan(bw(i)); bw_s=sprintf('%.4f',bw(i)); cf_s=sprintf('%.4f',cf(i)); end
    fprintf(fid,'  %-8.2f | %-10.3f | %-12.4f | %-10s | %-10s | %-12.3f\n',param_vals(i),s11_min(i),freq_min(i),bw_s,cf_s,s11_t(i));
end
[~,be]=min(s11_min);
fprintf(fid,'\n  ★ Best: %s=%.2f (min|S11|=%.3fdB @%.4fGHz)\n',param_name,param_vals(be),s11_min(be),freq_min(be));
fclose(fid);
fprintf('\n✅ 汇总表:%s\n',sf);
fprintf('===============================================================\n    完成！\n===============================================================\n');
```
