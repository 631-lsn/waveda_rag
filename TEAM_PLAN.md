# WavEDA RAG 三人分工计划

> 优化方向的三人并行分工。切分原则是**文件边界不重叠**，避免并行开发时频繁冲突。
> 背景分析见对话记录与 `ROADMAP.md`；本文件以可执行任务为准。

## 核心结论（为什么先做这些）

- 项目的价值 = 检索命中率。当前嵌入是 MD5 哈希袋词（`src/raggg/indexing/embeddings.py`），无语义能力，靠 `retriever.py` 里的硬编码加分兜底，这条路不可持续。
- 换语义嵌入时**不要用 sentence-transformers**（会引入 PyTorch，EXE 体积爆炸，且 all-MiniLM-L6-v2 是英文模型）。走本地 ONNX 中文小模型（fastembed 类）路线。
- 动手改检索之前必须先有评测集，否则所有改动无法量化验证。
- numpy 暴力搜索在当前规模（~5000 chunk）是毫秒级，**不需要 FAISS**。

---

## 同学 A：检索质量（主战场）

**负责文件**：`src/raggg/indexing/`、`src/raggg/retrieval/`、`src/raggg/pipeline/rag_pipeline.py`、`scripts/` 下评测脚本

| # | 任务 | 验收标准 |
|---|---|---|
| A1 | 建检索评测集：25~30 个真实问题 + 每题标注应命中的文档，存 `tests/fixtures/retrieval_eval.json`；把 `scripts/debug_retrieval.py` 扩成 hit-rate@5 评测脚本 | 跑一条命令输出命中率数字 |
| A2 | 用评测集测出当前哈希嵌入的基线命中率 | 数字记录在评测脚本注释或本文档 |
| A3 | 接入本地 ONNX 语义嵌入（fastembed + 中文小模型），接口与 `HashedEmbeddingModel` 一致，缺依赖时自动回退哈希 | 评测集命中率显著高于基线；`EMBEDDING_SCHEMA_VERSION` 加一 |
| A4 | `_lexical_overlap` 升级为真 BM25（IDF + 长度归一，复用现有 `tokenize()`，零新依赖） | 评测集命中率不降 |
| A5 | 修 `_build_retrieval_query`：只有追问（极短句/含指代）才带上一条问题，不无脑拼 3 轮历史 | 追问场景检索不脱靶 |
| A6 | 检索加分数门槛：低于阈值时明说"知识库没找到相关内容"，不硬塞 6 条噪声进 prompt | 无关问题不再得到编造答案 |
| A7 | 验证通过后删除 retriever 硬编码加分（PML +0.3 等） | 评测集命中率不低于删除前 |

**约束**：A1/A2 必须先做，是后续每一步的裁判。对外承诺 `Retriever.search(query, top_k) -> list[SearchResult]` 签名不变。

## 同学 B：桌面与交互

**负责文件**：`src/raggg/desktop/`（含 `main_window.py`）、`src/raggg/generation/prompt_builder.py`

| # | 任务 | 验收标准 |
|---|---|---|
| B1 | 拆 `main_window.py`（~1990 行）第一步：Markdown/LaTeX 渲染、图片索引（`_build_image_index` 一系）拆出 | 启动正常，功能无回归 |
| B2 | 第二步：收藏夹（`_open_favorites` 约 180 行）、会话面板拆出 | 主窗口 <800 行 |
| B3 | 引用标注：prompt 要求模型句末标 `[1][2]`；渲染层把 `[N]` 渲染为可点上标，点击联动侧边来源 | 回答中 `[1]` 可点击跳转 |
| B4 | 构建索引进度反馈：builder 分阶段报进度，loader 动画下显示实时进度文字 | 导入大文件时有进度提示 |

**约束**：`main_window.py` 同期只允许 B 一个人修改。B3 的 prompt 改动独立成 commit，便于回滚。

## 同学 C：工程基建与发布

**负责文件**：`src/raggg/generation/llm_client.py`、`src/raggg/config.py`、`tests/`、`.github/`、打包脚本

| # | 任务 | 验收标准 |
|---|---|---|
| C1 | LLM 错误分类：401=Key 无效、429=限流/额度、超时、500 各自给出可读提示；加一次超时重试 | 断网/错 Key/限流三种场景提示各不同 |
| C2 | 配置校验：`config/.env` 缺失或损坏时启动给出修复指引，而非静默降级 | 删掉 `.env` 启动能看到明确提示 |
| C3 | 版本号 + GitHub Actions：tag 触发自动打 EXE、自动传 Release | 测试 tag 能产出 Release |
| C4 | 补测试：检索打分、prompt 构建、会话管理 | `pytest` 全绿，覆盖核心路径 |
| C5 | 更新 `ROADMAP.md`：划掉已完成项（流式输出、部分拆分），嵌入方案改为 ONNX 路线 | 文档与代码现状一致 |

---

## 协作规则

1. **分支**：每人从 `main` 拉 feature 分支，命名如 `feat/a3-onnx-embedding`，走 PR 合并。
2. **文件红线**：A 不碰 `desktop/`；B 不碰 `retrieval/`、`indexing/`；C 不碰 `desktop/`、`retrieval/`。共享文件：`prompt_builder.py` 归 B，`rag_pipeline.py` 归 A；C 需要改这两个文件时先同步。
3. **新依赖**：全项目唯一计划新增依赖是 A3 的 fastembed。加入前先在 C3 的 CI 流水线上验证 EXE 打包体积可接受。
4. **每日同步**：只同步"今天动了哪些文件"。

## 建议节奏

- **第 1 周**：A 做 A1+A2；B 做 B1；C 做 C1+C2。评测集出来之前不动检索逻辑。
- **第 2 周**：A 做 A3+A4（核心交付）；B 做 B2+B3；C 做 C3+C4。
- **第 3 周**：A 做 A5~A7 + 全量回归；B 做 B4；C 做 C5 并协助验证 EXE 体积。

## 人员建议

- A 线难度最高、对体验影响最大，建议组里最强的同学负责。
- B 线任务碎但立竿见影。
- C 线独立性强，适合时间不连续的同学。

---

## 进度记录

| 日期 | 事项 |
|---|---|
| 2026-07-20 | 分工计划创建 |
| 2026-07-20 | A 线全部完成（A1~A7），结论与数据如下 |

### A 线完成报告（2026-07-20，执行：Vera）

**评测基线**：41 题评测集（30 直白 + 11 改写），`tests/fixtures/retrieval_eval.json`；
评测脚本 `scripts/evaluate_retrieval.py`（hit@1 / hit@5 / MRR，支持 `--embedding`/`--index-dir` A/B）。
哈希嵌入基线：hit@1 0.756 / hit@5 0.878 / MRR 0.793。

**已落地的改动**：

1. **A3 语义嵌入（可选开启，非默认）**：新增 `src/raggg/indexing/semantic_embeddings.py`，
   走 fastembed/ONNX（无 PyTorch），默认模型 `BAAI/bge-small-zh-v1.5`（512 维，~100MB）。
   `RAG_EMBEDDING_MODEL=fastembed:BAAI/bge-small-zh-v1.5` 即可开启；缺依赖/下载失败自动回退哈希。
   **关键证据**：bge 在评测集上 0.780/0.854，与哈希（0.756/0.878）差异仅 1~2 题（噪声级）；
   7 倍大的 jina-v2-base-zh 同样 0.756/0.854。语义嵌入在此语料上无统计显著收益，
   故**哈希保持默认**，语义作为可选项交付。
2. **A4 BM25 已替换旧词袋重合度**（`retriever.py`，含 IDF + 长度归一 + min-max 归一化）。
   最终配比 **0.4×向量 + 0.6×BM25**（网格搜索标定），hash 下 hit@5 0.902（全配置最高）。
   heading 独立通道删除（BM25 语料已含标题+小节）。
3. **A5 历史拼接修复**：只有追问（指代词/≤6 字）才带上一条问题检索，不再无脑拼 3 轮。
4. **A6 分数门槛**：`SearchResult` 新增 `bm25_raw`；`RAGPipeline` 按 `RAG_RETRIEVAL_MIN_SCORE`
   （默认 20，0=关闭）过滤，全部低于门槛时直接回答"知识库没找到相关内容"，不再让 LLM 编造。
   标定依据：混合分/min-max 分有地板效应（in-scope 与 oos 完全重叠），
   BM25 原始分可分离（in-scope 最低 34.8 vs oos 最高 33.5），取保守值 20。
5. **A7 硬编码加分：保留**。消融实验证明它们是承重墙——全删后 hit@5 0.878→0.805、
   hit@1 0.78→0.66（bge）。已把实验结论写进 `retriever.py` 注释，**勿删**。

**回归**：`unittest discover` 56 项全绿（含新增 BM25/追问/门槛 3 组测试）；冒烟测试通过。

**后续建议（超出 A 线范围）**：
- 评测集只有 41 题，±2 题即噪声；团队使用中积累真实问题后继续扩充。
- 真正顽固的 miss（#4/#12/#38/#39）是结构性问题：金建铭教材 1684 chunk 占索引 49%
  淹没短文档。可考虑文档级两阶段检索或给巨型文档降 priority。
- fastembed 尚未写入 requirements.txt——若团队决定启用语义嵌入，需先在 CI 上验证 EXE 体积（A/C 线衔接点）。
