import {
  BookOpen,
  Bot,
  ChevronRight,
  Database,
  History,
  Languages,
  Menu,
  MessageSquarePlus,
  Moon,
  PanelRight,
  Settings,
  Star,
  Sun,
  X,
} from "lucide-react";
import type { ReactNode } from "react";

import { Button } from "@/components/ui/button";
import type { BootstrapPayload, Locale, Theme } from "@/lib/contracts";
import { t } from "@/lib/i18n";
import { cn } from "@/lib/utils";

export type ViewName = "chat" | "history" | "favorites" | "knowledge" | "settings";

interface AppShellProps {
  children: ReactNode;
  sourcePanel: ReactNode;
  activeView: ViewName;
  locale: Locale;
  theme: Theme;
  model: string;
  apiConfigured: boolean;
  indexStatus: BootstrapPayload["indexStatus"];
  watcherStatus: BootstrapPayload["watcherStatus"];
  navOpen: boolean;
  sourceOpen: boolean;
  onNavOpenChange(open: boolean): void;
  onSourceOpenChange(open: boolean): void;
  onViewChange(view: ViewName): void;
  onNewChat(): void;
  onThemeToggle(): void;
  onLocaleToggle(): void;
}

const navItems: Array<{ view: ViewName; icon: typeof History; label: "history" | "favorites" | "knowledge" | "settings" }> = [
  { view: "history", icon: History, label: "history" },
  { view: "favorites", icon: Star, label: "favorites" },
  { view: "knowledge", icon: Database, label: "knowledge" },
  { view: "settings", icon: Settings, label: "settings" },
];

export function AppShell(props: AppShellProps) {
  const nav = (
    <div className="flex h-full flex-col">
      <div className="flex items-center gap-3 px-3 pb-5 pt-2">
        <div className="grid size-10 place-items-center rounded-xl border border-cyan-300/25 bg-cyan-400/10 text-cyan-300 shadow-[0_0_28px_rgba(34,211,238,.12)]">
          <Bot className="size-5" />
        </div>
        <div className="min-w-0">
          <div className="truncate font-semibold tracking-tight">WavEDA</div>
          <div className="truncate text-xs text-[var(--subtle)]">Knowledge Workbench</div>
        </div>
        <button className="ml-auto rounded-lg p-2 text-[var(--muted)] lg:hidden" onClick={() => props.onNavOpenChange(false)} aria-label="关闭导航">
          <X className="size-4" />
        </button>
      </div>

      <Button className="mx-2 justify-start" onClick={props.onNewChat}>
        <MessageSquarePlus className="size-4" />
        {t(props.locale, "newChat")}
      </Button>

      <nav className="mt-5 space-y-1 px-2">
        {navItems.map(({ view, icon: Icon, label }) => (
          <button
            key={view}
            className={cn("nav-item", props.activeView === view && "nav-item-active")}
            onClick={() => {
              props.onViewChange(view);
              props.onNavOpenChange(false);
            }}
          >
            <Icon className="size-4" />
            <span>{t(props.locale, label)}</span>
            <ChevronRight className="ml-auto size-3.5 opacity-40" />
          </button>
        ))}
      </nav>

      <div className="mt-auto space-y-2 border-t border-[var(--border)] px-3 pt-4 text-xs">
        <div className="status-row">
          <span className={cn("status-dot", props.indexStatus !== "ready" && "bg-amber-400")} />
          <BookOpen className="size-3.5" />
          <span>{props.indexStatus === "ready" ? t(props.locale, "ready") : t(props.locale, "missing")}</span>
        </div>
        <div className="status-row">
          <span className="status-dot bg-emerald-400" />
          <Database className="size-3.5" />
          <span>{props.watcherStatus === "active" ? t(props.locale, "active") : props.watcherStatus}</span>
        </div>
        <div className="rounded-xl border border-[var(--border)] bg-[var(--surface-2)] p-3">
          <div className="truncate font-medium text-[var(--text)]">{props.model}</div>
          <div className="mt-1 text-[var(--subtle)]">
            {props.apiConfigured ? t(props.locale, "apiConfigured") : t(props.locale, "apiMissing")}
          </div>
        </div>
        <div className="grid grid-cols-2 gap-2 pt-1">
          <Button variant="ghost" size="sm" onClick={props.onThemeToggle} aria-label={props.theme === "dark" ? t(props.locale, "light") : t(props.locale, "dark")}>
            {props.theme === "dark" ? <Sun className="size-3.5" /> : <Moon className="size-3.5" />}
            {props.theme === "dark" ? t(props.locale, "light") : t(props.locale, "dark")}
          </Button>
          <Button variant="ghost" size="sm" onClick={props.onLocaleToggle}>
            <Languages className="size-3.5" />
            {props.locale === "zh" ? "EN" : "中文"}
          </Button>
        </div>
      </div>
    </div>
  );

  return (
    <div className="app-background">
      <div className="app-grid">
        <aside className="desktop-nav glass-panel">{nav}</aside>
        {props.navOpen && (
          <div className="drawer-layer lg:hidden" onClick={() => props.onNavOpenChange(false)}>
            <aside className="drawer-panel left-0" onClick={(event) => event.stopPropagation()}>{nav}</aside>
          </div>
        )}

        <main className="main-workspace">
          <header className="workspace-header">
            <Button variant="ghost" size="icon" className="lg:hidden" onClick={() => props.onNavOpenChange(true)} aria-label="打开导航">
              <Menu className="size-5" />
            </Button>
            <div className="min-w-0">
              <div className="truncate text-sm font-semibold text-[var(--text)]">
                {props.activeView === "chat" ? t(props.locale, "welcome") : t(props.locale, props.activeView)}
              </div>
              <div className="truncate text-xs text-[var(--subtle)]">{props.model}</div>
            </div>
            <Button variant="ghost" size="icon" className="ml-auto xl:hidden" onClick={() => props.onSourceOpenChange(true)} aria-label={t(props.locale, "sources")}>
              <PanelRight className="size-5" />
            </Button>
          </header>
          <div className="workspace-content">{props.children}</div>
        </main>

        <aside className="desktop-sources glass-panel">{props.sourcePanel}</aside>
        {props.sourceOpen && (
          <div className="drawer-layer xl:hidden" onClick={() => props.onSourceOpenChange(false)}>
            <aside className="drawer-panel right-0" onClick={(event) => event.stopPropagation()}>
              <div className="mb-2 flex justify-end">
                <Button variant="ghost" size="icon" onClick={() => props.onSourceOpenChange(false)} aria-label="关闭来源">
                  <X className="size-4" />
                </Button>
              </div>
              {props.sourcePanel}
            </aside>
          </div>
        )}
      </div>
    </div>
  );
}
