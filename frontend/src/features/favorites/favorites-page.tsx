import { Star, Trash2 } from "lucide-react";

import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import type { FavoriteItem, Locale } from "@/lib/contracts";
import { t } from "@/lib/i18n";

export function FavoritesPage({ locale, favorites, onDelete }: { locale: Locale; favorites: FavoriteItem[]; onDelete(id: string): void }) {
  return (
    <section className="page-section">
      <div className="page-heading"><div><p className="eyebrow">SAVED ANSWERS</p><h1>{t(locale, "favorites")}</h1></div></div>
      <ScrollArea className="min-h-0 flex-1">
        <div className="card-grid">
          {favorites.length === 0 ? <div className="empty-page"><Star className="size-10" /><p>{t(locale, "noFavorites")}</p></div> : [...favorites].reverse().map((favorite) => (
            <article key={favorite.id} className="favorite-card">
              <div className="flex items-start gap-3"><Star className="mt-0.5 size-4 shrink-0 fill-amber-300 text-amber-300" /><h2 className="font-medium">{favorite.question}</h2></div>
              <p className="mt-4 line-clamp-5 whitespace-pre-wrap text-sm leading-6 text-[var(--muted)]">{favorite.answer}</p>
              <div className="mt-5 flex items-center justify-between text-xs text-[var(--subtle)]"><span>{favorite.createdAt}</span><Button variant="ghost" size="icon" aria-label={t(locale, "delete")} onClick={() => { if (window.confirm(locale === "zh" ? "确定删除这一条收藏吗？" : "Delete this favorite?")) onDelete(favorite.id); }}><Trash2 className="size-4" /></Button></div>
            </article>
          ))}
        </div>
      </ScrollArea>
    </section>
  );
}
