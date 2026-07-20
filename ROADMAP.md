# WavEDA RAG 优化路线图

> 更新于 2026-07-20。✅ = 已完成，🔧 = 进行中，⏳ = 待开始。

---

## 已完成项（划掉）

- ✅ **流式输出**：LLM 回答逐 token 显示（`llm_client.py` → `complete_stream()`）
- ✅ **B1 拆分 main_window**：`settings_dialog.py`、`widgets.py`、`workers.py`、`source_viewer.py`、`favorites.py`、`rendering.py`、`image_index.py`、`sessions.py`、`views.py`
- ✅ **A1/A2 检索评测**：41 题评测集 + 评测脚本，hit@5 = 0.78（hash）基线
- ✅ **A4 BM25 升级**：`retriever.py` 词袋改为真 BM25（IDF+长度归一化）
- ✅ **C1 LLM 错误分类**：401/429/5xx/超时/断网 五类错误 + 友好提示
- ✅ **C2 配置校验**：`.env` 缺失时启动弹出修复指引
- ✅ **C3 CI/CD**：tag 推送自动打包 EXE + 发布 Release
- ✅ **C4 测试**：检索/Prompt/会话共 21 个单元测试
- ✅ **C5 文档更新**：本文档

---

## 嵌入方案（A3 — 进行中 🔧）

**路线已改为 ONNX/fastembed**，不使用 sentence-transformers（避免 PyTorch 导致 EXE 体积爆炸）。

- 语义模型：`BAAI/bge-small-zh-v1.5`（512 维，~100MB）
- 框架：fastembed（ONNX Runtime，零 PyTorch 依赖）
- 代码已完成（`semantic_embeddings.py`），待装依赖后重建索引验证
- 预期 hit@5：0.85-0.92（当前 hash 基线 0.78）

---


---

## 当前进度（2026-07-20）

详见 `TEAM_PLAN.md`。

| 线 | 已完成 | 进行中 | 待开始 |
|----|-------|--------|--------|
| A（检索） | A1/A2 评测 + A4 BM25 | A3 ONNX 语义嵌入 | A5-A7 |
| B（桌面） | B1 拆分 main_window | | B2-B4 |
| C（基建） | C1/C2/C3/C4/C5 全部 | | |

### 下一步关键动作

1. **A3**：`pip install fastembed` → 重建索引 → 验证 hit@5 提升
2. **B2**：继续拆分 main_window，收藏夹和会话面板
3. **A5-A7**：优化检索查询 + 分数门槛 + 删除硬编码加分
