"""
脚本自动生成器弹窗 — 用户输入路径/变量/策略，一键生成完整扫参文件包。
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QSpinBox,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from raggg.config import Settings
from raggg.generation.script_generator import ScriptPackage, build_task_config
from raggg.i18n import get_text
from raggg.theme import get_colors

COLORS = get_colors()

_SWEEP_STRATEGIES = [
    ("single_param", "单参数外部循环 — 每个值独立 XML，逐点仿真，易于断点续跑（推荐）"),
    ("dual_param", "双参数嵌套循环 — N₁×N₂ 全组合，2D 热力图 + 3D 曲面"),
    ("builtin_sweep", "工程内置扫描 — .tsp 已配好参数扫描，WavEDA 只跑一次"),
    ("custom", "自定义描述 — 用自然语言描述想要的效果"),
]


class ScriptGeneratorDialog(QDialog):
    """WavEDA 脚本自动生成器"""

    def __init__(self, settings: Settings, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.settings = settings
        self.setWindowTitle("WavEDA 脚本自动生成器")
        self.setMinimumWidth(620)
        self.setMinimumHeight(520)
        self._var_rows: list[dict[str, QWidget]] = []
        self._build_ui()

    # ─── UI ────────────────────────────────────────
    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        # 顶部说明
        desc = QLabel(
            "根据你的工程和扫参需求，自动生成一套可直接运行的 XML / MATLAB / Python / README 文件。\n"
            "所有文件基于统一的 task_config.json 生成，确保参数一致。"
        )
        desc.setStyleSheet(f"color:{COLORS['muted']}; font-size:12px;")
        desc.setWordWrap(True)
        layout.addWidget(desc)

        # ── 路径配置 ──
        path_group = QGroupBox("路径配置")
        path_form = QFormLayout(path_group)
        path_form.setSpacing(6)

        row_exe = QHBoxLayout()
        self.exe_edit = QLineEdit()
        self.exe_edit.setPlaceholderText("例: C:\\Program Files\\WavEDA\\WavEDA.exe")
        exe_btn = QPushButton("浏览...")
        exe_btn.clicked.connect(lambda: self._browse_file(self.exe_edit, "WavEDA 可执行文件 (*.exe)"))
        row_exe.addWidget(self.exe_edit)
        row_exe.addWidget(exe_btn)
        path_form.addRow("WavEDA 路径:", row_exe)

        row_tsp = QHBoxLayout()
        self.tsp_edit = QLineEdit()
        self.tsp_edit.setPlaceholderText("例: D:\\Projects\\dipole\\dipole.tsp")
        tsp_btn = QPushButton("浏览...")
        tsp_btn.clicked.connect(lambda: self._browse_file(self.tsp_edit, "WavEDA 工程文件 (*.tsp)"))
        row_tsp.addWidget(self.tsp_edit)
        row_tsp.addWidget(tsp_btn)
        path_form.addRow("工程 .tsp:", row_tsp)

        row_save = QHBoxLayout()
        self.save_edit = QLineEdit()
        self.save_edit.setPlaceholderText("选一个本地目录存放生成的文件，留空则放到工程目录下")
        save_btn = QPushButton("选择...")
        save_btn.clicked.connect(self._browse_save_dir)
        row_save.addWidget(self.save_edit)
        row_save.addWidget(save_btn)
        path_form.addRow("本地保存目录:", row_save)

        row_work = QHBoxLayout()
        self.work_edit = QLineEdit()
        self.work_edit.setPlaceholderText("目标电脑上的工作目录，例如 E:\\sweep_exp2\\")
        row_work.addWidget(self.work_edit, stretch=1)
        path_form.addRow("目标工作目录:", row_work)
        path_form.addRow(
            QLabel("↑ 异地跑填目标电脑路径，本地跑跟上面一样即可。"),
        )

        layout.addWidget(path_group)

        # ── 变量 + 策略 ──
        var_group = QGroupBox("扫参变量与策略")
        var_layout = QVBoxLayout(var_group)
        var_layout.setSpacing(8)

        # 变量列表
        self._var_container = QVBoxLayout()
        var_layout.addLayout(self._var_container)
        self._add_variable_row()  # 默认一行

        add_var_btn = QPushButton("+ 添加变量（双参数扫参）")
        add_var_btn.clicked.connect(self._add_variable_row)
        var_layout.addWidget(add_var_btn)

        # 策略
        strat_row = QHBoxLayout()
        strat_row.addWidget(QLabel("循环策略:"))
        self.strategy_combo = QComboBox()
        for key, desc in _SWEEP_STRATEGIES:
            self.strategy_combo.addItem(desc, key)
        strat_row.addWidget(self.strategy_combo, stretch=1)
        var_layout.addLayout(strat_row)

        # 强制重建网格
        self.remesh_check = QCheckBox("改变几何时强制删除旧网格（推荐勾选）")
        self.remesh_check.setChecked(True)
        var_layout.addWidget(self.remesh_check)

        layout.addWidget(var_group)

        # ── 结果配置 ──
        result_group = QGroupBox("结果配置")
        result_form = QFormLayout(result_group)
        result_form.setSpacing(6)

        self.port_name_edit = QLineEdit("Port_S_data_1")
        result_form.addRow("Port S参数数据集名称:", self.port_name_edit)

        row_obs = QHBoxLayout()
        self.obs_check = QCheckBox("启用 Observer")
        self.obs_name_edit = QLineEdit()
        self.obs_name_edit.setPlaceholderText("Observer 数据集名称")
        self.obs_name_edit.setEnabled(False)
        self.obs_check.toggled.connect(lambda checked: self.obs_name_edit.setEnabled(checked))
        row_obs.addWidget(self.obs_check)
        row_obs.addWidget(self.obs_name_edit, stretch=1)
        result_form.addRow("Observer:", row_obs)

        self.target_freq_spin = QSpinBox()
        self.target_freq_spin.setRange(0, 1000)
        self.target_freq_spin.setValue(2)
        self.target_freq_spin.setSuffix(" GHz")
        result_form.addRow("目标频率:", self.target_freq_spin)

        self.s11_threshold_spin = QSpinBox()
        self.s11_threshold_spin.setRange(-100, 0)
        self.s11_threshold_spin.setValue(-10)
        self.s11_threshold_spin.setSuffix(" dB")
        result_form.addRow("S11 带宽门限:", self.s11_threshold_spin)

        layout.addWidget(result_group)

        # ── 控制器 + 超时 ──
        ctrl_group = QGroupBox("运行控制")
        ctrl_form = QFormLayout(ctrl_group)
        ctrl_form.setSpacing(6)

        self.controller_combo = QComboBox()
        self.controller_combo.addItem("MATLAB（.m 文件）", "matlab")
        self.controller_combo.addItem("Python（.py 文件）", "python")
        ctrl_form.addRow("主控制器:", self.controller_combo)

        self.timeout_spin = QSpinBox()
        self.timeout_spin.setRange(60, 7200)
        self.timeout_spin.setValue(1800)
        self.timeout_spin.setSuffix(" 秒")
        ctrl_form.addRow("单点超时:", self.timeout_spin)

        self.max_attempts_spin = QSpinBox()
        self.max_attempts_spin.setRange(1, 10)
        self.max_attempts_spin.setValue(3)
        ctrl_form.addRow("最大重试次数:", self.max_attempts_spin)

        layout.addWidget(ctrl_group)

        # ── 底部按钮 ──
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()

        preview_btn = QPushButton("预览文件清单")
        preview_btn.clicked.connect(self._preview)
        btn_layout.addWidget(preview_btn)

        generate_btn = QPushButton("生成文件包")
        generate_btn.setStyleSheet(
            f"QPushButton {{ background-color: {COLORS['accent']}; color: white; "
            "padding: 8px 24px; font-weight: bold; border-radius: 4px; }}"
        )
        generate_btn.clicked.connect(self._generate)
        btn_layout.addWidget(generate_btn)

        layout.addLayout(btn_layout)

    # ─── 变量行管理 ──────────────────────────────────
    def _add_variable_row(self) -> None:
        row_widget = QWidget()
        row = QHBoxLayout(row_widget)
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(6)

        name_edit = QLineEdit()
        name_edit.setPlaceholderText("变量名 (如 L_t2)")
        name_edit.setMaximumWidth(100)
        row.addWidget(QLabel("变量:"))
        row.addWidget(name_edit)

        row.addWidget(QLabel("起始:"))
        start_edit = QLineEdit("0")
        start_edit.setMaximumWidth(60)
        row.addWidget(start_edit)

        row.addWidget(QLabel("步长:"))
        step_edit = QLineEdit("1")
        step_edit.setMaximumWidth(60)
        row.addWidget(step_edit)

        row.addWidget(QLabel("终止:"))
        end_edit = QLineEdit("10")
        end_edit.setMaximumWidth(60)
        row.addWidget(end_edit)

        row.addWidget(QLabel("或值列表:"))
        values_edit = QLineEdit()
        values_edit.setPlaceholderText("如 4.5,5.0,5.5,6.0 （优先于起始/步长/终止）")
        row.addWidget(values_edit, stretch=1)

        del_btn = QPushButton("×")
        del_btn.setMaximumWidth(30)
        del_btn.clicked.connect(lambda: self._remove_variable_row(row_widget))
        row.addWidget(del_btn)

        self._var_container.addWidget(row_widget)
        self._var_rows.append({
            "widget": row_widget,
            "name": name_edit,
            "start": start_edit,
            "step": step_edit,
            "end": end_edit,
            "values": values_edit,
        })

    def _remove_variable_row(self, widget: QWidget) -> None:
        if len(self._var_rows) <= 1:
            return  # 至少保留一行
        self._var_container.removeWidget(widget)
        widget.deleteLater()
        self._var_rows = [r for r in self._var_rows if r["widget"] is not widget]

    # ─── 文件浏览 ────────────────────────────────────
    def _browse_file(self, target: QLineEdit, filter_str: str) -> None:
        path, _ = QFileDialog.getOpenFileName(self, "选择文件", "", filter_str)
        if path:
            target.setText(path)

    def _browse_save_dir(self) -> None:
        path = QFileDialog.getExistingDirectory(self, "选择本地保存目录")
        if path:
            self.save_edit.setText(path)

    # ─── 收集用户输入 → task_config ────────────────────
    def _collect_config(self) -> dict:
        sweep_vars: dict[str, list[float]] = {}
        for row in self._var_rows:
            name = row["name"].text().strip()
            if not name:
                continue
            values_text = row["values"].text().strip()
            if values_text:
                try:
                    vals = [float(v.strip()) for v in values_text.split(",") if v.strip()]
                except ValueError:
                    QMessageBox.warning(self, "格式错误", f"变量 '{name}' 的值列表格式不正确，请用逗号分隔数字。")
                    return {}
                sweep_vars[name] = vals
            else:
                try:
                    start = float(row["start"].text())
                    step = float(row["step"].text())
                    end = float(row["end"].text())
                except ValueError:
                    QMessageBox.warning(self, "格式错误", f"变量 '{name}' 的起始/步长/终止必须为数字。")
                    return {}
                num = round((end - start) / step) + 1
                if num < 1:
                    QMessageBox.warning(self, "范围错误", f"变量 '{name}' 范围无效，请检查起始/终止/步长。")
                    return {}
                sweep_vars[name] = [start + i * step for i in range(num)]

        project_file = self.tsp_edit.text().strip()
        waveda_exe = self.exe_edit.text().strip()
        save_dir = self.save_edit.text().strip()
        work_dir = self.work_edit.text().strip()

        if not save_dir:
            if project_file:
                save_dir = str(Path(project_file).parent / "automation_output")
            else:
                save_dir = str(Path.home() / "waveda_automation_output")

        # 目标工作目录默认等于本地保存目录（本地跑的场景）
        if not work_dir:
            work_dir = save_dir

        if not waveda_exe:
            # 尝试从 settings 推断
            pass

        results = [{"name": self.port_name_edit.text().strip() or "Port_S_data_1", "type": "port", "traces": ["S11 dB"]}]
        if self.obs_check.isChecked() and self.obs_name_edit.text().strip():
            results.append({"name": self.obs_name_edit.text().strip(), "type": "observer", "traces": []})

        strategy = self.strategy_combo.currentData()
        controller = self.controller_combo.currentData()

        return build_task_config(
            project_file=project_file,
            waveda_exe=waveda_exe,
            save_dir=save_dir,
            work_dir=work_dir,
            controller=controller,
            sweep_vars=sweep_vars,
            strategy=strategy,
            results=results,
            target_freq=float(self.target_freq_spin.value()),
            s11_threshold=float(self.s11_threshold_spin.value()),
            timeout_seconds=self.timeout_spin.value(),
            max_attempts=self.max_attempts_spin.value(),
            force_remesh=self.remesh_check.isChecked(),
        )

    # ─── 预览 ────────────────────────────────────────
    def _preview(self) -> None:
        config = self._collect_config()
        if not config:
            return

        pkg = ScriptPackage(config)
        files = pkg.generate_all()

        preview_text = f"本地保存目录: {pkg.save_dir}\n"
        preview_text += f"目标工作目录: {pkg.work_dir}\n\n"
        preview_text += f"将生成 {len(files)} 个文件:\n\n"
        for name, content in files.items():
            lines = content.count("\n") + 1
            preview_text += f"  📄 {name}  ({lines} 行)\n"

        sweep = config.get("sweep", {}).get("variables", {})
        if sweep:
            total = 1
            for vname, vvals in sweep.items():
                total *= len(vvals)
                preview_text += f"\n  变量 {vname}: {len(vvals)} 个值"
            preview_text += f"\n  总仿真次数: {total}"

        dlg = QDialog(self)
        dlg.setWindowTitle("文件清单预览")
        dlg.setMinimumSize(500, 350)
        layout = QVBoxLayout(dlg)
        preview_edit = QPlainTextEdit()
        preview_edit.setReadOnly(True)
        preview_edit.setPlainText(preview_text)
        layout.addWidget(preview_edit)
        btn = QPushButton("关闭")
        btn.clicked.connect(dlg.accept)
        layout.addWidget(btn)
        dlg.exec()

    # ─── 生成 ────────────────────────────────────────
    def _generate(self) -> None:
        config = self._collect_config()
        if not config:
            return

        sweep_vars = config.get("sweep", {}).get("variables", {})
        if not sweep_vars:
            QMessageBox.warning(self, "缺少变量", "请至少配置一个扫参变量。")
            return

        total = 1
        for vals in sweep_vars.values():
            total *= len(vals)

        reply = QMessageBox.question(
            self,
            "确认生成",
            f"本地保存: {config['save_dir']}\n"
            f"目标工作目录: {config['output_dir']}\n\n"
            f"总仿真次数: {total}\n\n"
            f"确认生成？",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply != QMessageBox.Yes:
            return

        try:
            pkg = ScriptPackage(config)
            out_dir = pkg.write_all()
            files = pkg.generate_all()

            # 构建文件清单
            file_list = "\n".join(f"  ✓ {name}" for name in sorted(files.keys()))

            QMessageBox.information(
                self,
                "生成完成 ✅",
                f"文件已保存到本地:\n{out_dir}\n\n"
                f"目标工作目录: {config['output_dir']}\n\n"
                f"生成 {len(files)} 个文件:\n{file_list}\n\n"
                "下一步:\n"
                "  1. 检查 task_config.json 中的路径\n"
                "  2. 在 GUI 中先单点验证模型\n"
                "  3. 运行 run_batch.m 或 run_batch.py",
            )
        except Exception as e:
            QMessageBox.critical(self, "生成失败", f"生成过程中出错:\n{e}")
