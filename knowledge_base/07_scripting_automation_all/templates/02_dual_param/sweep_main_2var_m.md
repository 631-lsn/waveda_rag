---
title: 双参数扫参 — 主控程序
category: scripting
tags: [代码, MATLAB, 主控程序, 双参数, 完整]
indexing: true
---

# sweep_main_2var.m — 双参数扫参主控程序

```matlab
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  sweep_main_2var.m — WavEDA 双参数扫参（嵌套循环遍历所有组合）
%
%  功能：两变量嵌套循环 → S参数分析 → 1D对比 + 2D热力图 + 3D曲面
%  使用前只改下方【用户配置区】
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear; clc; close all;

fprintf('===============================================================\n');
fprintf('    WavEDA 双参数扫参\n');
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

template_xml    = [work_path 'template.xml'];
temp_script_xml = [work_path 'temp_script.xml'];

% ---- 变量1 ----
var1_name  = '变量1';  var1_start = 30; var1_step = 5; var1_end = 40;
% ---- 变量2 ----
var2_name  = '变量2';  var2_start = 5;  var2_step = 2; var2_end = 10;

% ---- 数据集 ----
port_dataset_name = '你的Port_S参数数据集名';

% ---- 分析目标 ----
target_freq   = 2.45;  s11_threshold = -10;


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
        d=load(pf); freq=d(:,1); s11=d(:,2); all_freq{i,j}=freq; all_s11{i,j}=s11;
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
C=lines(N); vl={}; ci=0;
for i=1:n1 for j=1:n2; if ~isempty(all_freq{i,j})
    ci=ci+1; plot(all_freq{i,j},all_s11{i,j},'LineWidth',1.5,'Color',C(ci,:));
    vl{end+1}=sprintf('%s=%.2f %s=%.2f',var1_name,p1(i),var2_name,p2(j));
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
txt={'====== 双参数扫参 ======',sprintf('%s:%.2f~%.2f',var1_name,var1_start,var1_end),sprintf('%s:%.2f~%.2f',var2_name,var2_start,var2_end),sprintf('共%d组',N),'',sprintf('★最优:%s=%.2f, %s=%.2f',var1_name,p1(bi),var2_name,p2(bj)),sprintf('  min|S11|=%.3fdB @%.4fGHz',all_s11_min(bi,bj),all_freq_min(bi,bj)),''};
if ~isnan(all_bw(bi,bj)); txt{end+1}=sprintf('  %ddB BW=%.4fGHz',s11_threshold,all_bw(bi,bj)); end
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
```
