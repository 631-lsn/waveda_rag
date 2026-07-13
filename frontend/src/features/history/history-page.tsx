import { MessageSquare, Pencil, Search, Trash2 } from "lucide-react";
import { useMemo, useState } from "react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";
import type { ConversationSummary, Locale } from "@/lib/contracts";
import { t } from "@/lib/i18n";

interface HistoryPageProps {
  locale: Locale;
  conversations: ConversationSummary[];
  onOpen(id: string): void;
  onRename(id: string, title: string): void;
  onDelete(id: string): void;
}

export function HistoryPage(props: HistoryPageProps) {
  const [query, setQuery] = useState("");
  const visible = useMemo(
    () => props.conversations.filter((item) => item.title.toLowerCase().includes(query.toLowerCase())),
    [props.conversations, query],
  );

  return (
    <section className="page-section">
      <div className="page-heading">
        <div><p className="eyebrow">CONVERSATIONS</p><h1>{t(props.locale, "history")}</h1></div>
        <div className="relative w-full max-w-xs"><Search className="absolute left-3 top-3 size-4 text-[var(--subtle)]" /><Input value={query} onChange={(e) => setQuery(e.target.value)} className="pl-9" placeholder={props.locale === "zh" ? "搜索会话" : "Search conversations"} /></div>
      </div>
      <ScrollArea className="min-h-0 flex-1">
        <div className="card-grid">
          {visible.length === 0 ? <div className="empty-page"><MessageSquare className="size-10" /><p>{t(props.locale, "noHistory")}</p></div> : visible.map((conversation) => (
            <article key={conversation.id} className="list-card">
              <button className="min-w-0 flex-1 text-left" onClick={() => props.onOpen(conversation.id)}>
                <h2 className="truncate font-medium">{conversation.title}</h2>
                <p className="mt-2 text-xs text-[var(--subtle)]">{new Date(conversation.updatedAt).toLocaleString()}</p>
                <p className="mt-3 text-sm text-[var(--muted)]">{conversation.messages?.length || 0} messages</p>
              </button>
              <div className="flex gap-1">
                <Button variant="ghost" size="icon" aria-label={t(props.locale, "rename")} onClick={() => {
                  const title = window.prompt(props.locale === "zh" ? "新标题" : "New title", conversation.title);
                  if (title?.trim()) props.onRename(conversation.id, title);
                }}><Pencil className="size-4" /></Button>
                <Button variant="ghost" size="icon" aria-label={t(props.locale, "delete")} onClick={() => {
                  if (window.confirm(props.locale === "zh" ? "确定删除这一个会话吗？" : "Delete this conversation?")) props.onDelete(conversation.id);
                }}><Trash2 className="size-4" /></Button>
              </div>
            </article>
          ))}
        </div>
      </ScrollArea>
    </section>
  );
}
