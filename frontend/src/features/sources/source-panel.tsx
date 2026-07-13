import { BookOpen, ChevronRight, FileText, Gauge } from "lucide-react";
import { useState } from "react";

import { ScrollArea } from "@/components/ui/scroll-area";
import type { Locale, SourceItem } from "@/lib/contracts";
import { t } from "@/lib/i18n";

export function SourcePanel({ locale, sources }: { locale: Locale; sources: SourceItem[] }) {
  const [selected, setSelected] = useState<SourceItem | null>(null);

  return (
    <div className="flex h-full flex-col">
      <div className="flex items-center gap-2 border-b border-[var(--border)] px-4 py-4">
        <BookOpen className="size-4 text-cyan-300" />
        <h2 className="text-sm font-semibold">{t(locale, "sources")}</h2>
        <span className="ml-auto rounded-full bg-[var(--surface-3)] px-2 py-0.5 text-[11px] text-[var(--muted)]">{sources.length}</span>
      </div>
      <ScrollArea className="min-h-0 flex-1">
        <div className="space-y-3 p-3">
          {selected ? (
            <div>
              <button className="mb-3 text-xs text-cyan-300 hover:underline" onClick={() => setSelected(null)}>← {t(locale, "sources")}</button>
              <div className="source-card">
                <h3 className="font-medium">{selected.title}</h3>
                <p className="mt-1 text-xs text-[var(--muted)]">{selected.section}</p>
                <p className="mt-4 whitespace-pre-wrap text-sm leading-7 text-[var(--muted)]">{selected.content || selected.excerpt}</p>
                <p className="mt-4 break-all text-[11px] text-[var(--subtle)]">{selected.path}</p>
              </div>
            </div>
          ) : sources.length === 0 ? (
            <div className="empty-panel">
              <FileText className="size-8" />
              <p>{t(locale, "noSources")}</p>
            </div>
          ) : (
            sources.map((source, index) => (
              <button key={`${source.id}-${index}`} className="source-card w-full text-left" onClick={() => setSelected(source)}>
                <div className="flex items-start gap-3">
                  <span className="grid size-7 shrink-0 place-items-center rounded-lg bg-cyan-400/10 text-xs font-semibold text-cyan-300">{index + 1}</span>
                  <div className="min-w-0 flex-1">
                    <h3 className="line-clamp-2 text-sm font-medium text-[var(--text)]">{source.title}</h3>
                    <p className="mt-1 line-clamp-2 text-xs leading-5 text-[var(--muted)]">{source.excerpt}</p>
                    <div className="mt-3 flex items-center gap-1.5 text-[11px] text-[var(--subtle)]">
                      <Gauge className="size-3" />
                      {Math.max(0, source.score * 100).toFixed(0)}%
                      <span>·</span>
                      {source.sourceType}
                    </div>
                  </div>
                  <ChevronRight className="mt-1 size-3.5 text-[var(--subtle)]" />
                </div>
              </button>
            ))
          )}
        </div>
      </ScrollArea>
    </div>
  );
}
