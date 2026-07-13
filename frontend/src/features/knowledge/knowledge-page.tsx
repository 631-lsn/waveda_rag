import { Activity, Database, FilePlus2, RefreshCw, ShieldCheck } from "lucide-react";

import { Button } from "@/components/ui/button";
import type { BootstrapPayload, Locale } from "@/lib/contracts";
import { t } from "@/lib/i18n";

interface KnowledgePageProps {
  locale: Locale;
  chunkCount: number;
  indexStatus: BootstrapPayload["indexStatus"];
  watcherStatus: BootstrapPayload["watcherStatus"];
  onImport(): void;
  onRebuild(): void;
}

export function KnowledgePage(props: KnowledgePageProps) {
  const cards = [
    { icon: Database, label: t(props.locale, "documents"), value: props.chunkCount.toLocaleString() },
    { icon: ShieldCheck, label: props.locale === "zh" ? "索引状态" : "Index status", value: props.indexStatus },
    { icon: Activity, label: props.locale === "zh" ? "文件监听" : "File watcher", value: props.watcherStatus },
  ];
  return (
    <section className="page-section">
      <div className="page-heading"><div><p className="eyebrow">LOCAL KNOWLEDGE</p><h1>{t(props.locale, "knowledge")}</h1></div><div className="flex gap-2"><Button variant="secondary" onClick={props.onImport}><FilePlus2 className="size-4" />{t(props.locale, "import")}</Button><Button onClick={props.onRebuild}><RefreshCw className="size-4" />{t(props.locale, "rebuild")}</Button></div></div>
      <div className="grid gap-4 md:grid-cols-3">{cards.map(({ icon: Icon, label, value }) => <article className="metric-card" key={label}><Icon className="size-5 text-cyan-300" /><p>{label}</p><strong>{value}</strong></article>)}</div>
      <div className="mt-5 rounded-2xl border border-[var(--border)] bg-[var(--surface-1)] p-6"><h2 className="font-medium">{props.locale === "zh" ? "索引说明" : "Index behavior"}</h2><p className="mt-3 max-w-3xl text-sm leading-7 text-[var(--muted)]">{props.locale === "zh" ? "知识库文件发生稳定变化后会自动后台重建。手动导入仅处理你选择的单个文件；旧索引会保留到新索引成功生成。" : "Stable knowledge-base changes trigger a background rebuild. Import handles one selected file, and the current index remains available until a replacement succeeds."}</p></div>
    </section>
  );
}
