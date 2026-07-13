import { AlertCircle, RefreshCw, X } from "lucide-react";
import { lazy, Suspense, useCallback, useEffect, useMemo, useRef, useState } from "react";

import { Button } from "@/components/ui/button";
import { Component as AiLoader } from "@/components/ui/ai-loader";
import { FavoritesPage } from "@/features/favorites/favorites-page";
import { HistoryPage } from "@/features/history/history-page";
import { KnowledgePage } from "@/features/knowledge/knowledge-page";
import { AppShell, type ViewName } from "@/features/layout/app-shell";
import { SettingsPage } from "@/features/settings/settings-page";
import { SourcePanel } from "@/features/sources/source-panel";
import type { DesktopBridgeClient } from "@/lib/bridge";
import type {
  BootstrapPayload,
  BridgeEvent,
  ConversationMessage,
  ConversationSummary,
  SettingsUpdate,
  SourceItem,
} from "@/lib/contracts";
import { t } from "@/lib/i18n";

const ChatPage = lazy(() =>
  import("@/features/chat/chat-page").then((module) => ({ default: module.ChatPage })),
);

interface AppProps {
  bridge: DesktopBridgeClient;
}

function requestId() {
  return globalThis.crypto?.randomUUID?.() ?? `request-${Date.now()}-${Math.random()}`;
}

export default function App({ bridge }: AppProps) {
  const [bootstrap, setBootstrap] = useState<BootstrapPayload | null>(null);
  const [booting, setBooting] = useState(true);
  const [fatalError, setFatalError] = useState("");
  const [notice, setNotice] = useState("");
  const [activeView, setActiveView] = useState<ViewName>("chat");
  const [messages, setMessages] = useState<ConversationMessage[]>([]);
  const [sources, setSources] = useState<SourceItem[]>([]);
  const [question, setQuestion] = useState("");
  const [conversationId, setConversationId] = useState<string | undefined>();
  const [busyText, setBusyText] = useState("");
  const [navOpen, setNavOpen] = useState(false);
  const [sourceOpen, setSourceOpen] = useState(false);
  const activeRequest = useRef<string | null>(null);

  const locale = bootstrap?.locale ?? "zh";

  const loadBootstrap = useCallback(async () => {
    setBooting(true);
    setFatalError("");
    try {
      const payload = await bridge.bootstrap();
      setBootstrap(payload);
      document.documentElement.classList.toggle("dark", payload.theme === "dark");
      document.documentElement.lang = payload.locale === "zh" ? "zh-CN" : "en";
    } catch (error) {
      setFatalError(error instanceof Error ? error.message : String(error));
    } finally {
      setBooting(false);
    }
  }, [bridge]);

  const handleEvent = useCallback((event: BridgeEvent) => {
    if (event.type === "answer_progress" && event.requestId === activeRequest.current) {
      setBusyText(t(locale, event.phase));
      return;
    }
    if (event.type === "answer_completed" && event.requestId === activeRequest.current) {
      activeRequest.current = null;
      setBusyText("");
      setConversationId(event.conversation.id);
      setMessages(event.conversation.messages ?? []);
      setSources(event.sources);
      setBootstrap((current) => current ? {
        ...current,
        conversations: [event.conversation, ...current.conversations.filter((item) => item.id !== event.conversation.id)],
      } : current);
      return;
    }
    if (event.type === "answer_failed" && event.requestId === activeRequest.current) {
      activeRequest.current = null;
      setBusyText("");
      setNotice(event.message);
      return;
    }
    if (event.type === "import_progress") {
      setBusyText(t(locale, event.phase === "rebuilding" ? "rebuilding" : "importing"));
      return;
    }
    if (event.type === "import_cancelled") {
      setBusyText("");
      return;
    }
    if (event.type === "import_completed") {
      setBusyText("");
      setBootstrap((current) => current ? { ...current, chunkCount: event.chunkCount, indexStatus: "ready" } : current);
      setNotice(locale === "zh" ? `已导入 ${event.fileName}` : `Imported ${event.fileName}`);
      return;
    }
    if (event.type === "import_failed" || event.type === "index_failed") {
      setBusyText("");
      setNotice(event.message);
      return;
    }
    if (event.type === "index_changed") {
      setBusyText("");
      setBootstrap((current) => current ? { ...current, chunkCount: event.chunkCount, indexStatus: event.status } : current);
      return;
    }
    if (event.type === "watcher_changed") {
      setBootstrap((current) => current ? { ...current, watcherStatus: event.status } : current);
      return;
    }
    if (event.type === "bridge_error") setNotice(event.message);
  }, [locale]);

  useEffect(() => {
    const unsubscribe = bridge.subscribe(handleEvent);
    void loadBootstrap();
    return unsubscribe;
  }, [bridge, handleEvent, loadBootstrap]);

  const ask = async () => {
    const text = question.trim();
    if (!text || activeRequest.current) return;
    const id = requestId();
    activeRequest.current = id;
    setQuestion("");
    setMessages((current) => [...current, {
      id: `local-${id}`,
      role: "user",
      content: text,
      createdAt: new Date().toISOString(),
    }]);
    setBusyText(t(locale, "retrieving"));
    try {
      await bridge.ask(id, text, conversationId);
    } catch (error) {
      activeRequest.current = null;
      setBusyText("");
      setNotice(error instanceof Error ? error.message : String(error));
    }
  };

  const stop = async () => {
    const id = activeRequest.current;
    if (!id) return;
    await bridge.stopAnswer(id);
    activeRequest.current = null;
    setBusyText("");
  };

  const newChat = () => {
    setActiveView("chat");
    setConversationId(undefined);
    setMessages([]);
    setSources([]);
    setQuestion("");
  };

  const importDocument = async () => {
    const id = requestId();
    setBusyText(t(locale, "importing"));
    try {
      const result = await bridge.selectAndImportDocument(id);
      if (!result.accepted) setBusyText("");
    } catch (error) {
      setBusyText("");
      setNotice(error instanceof Error ? error.message : String(error));
    }
  };

  const rebuildIndex = async () => {
    const id = requestId();
    setBusyText(t(locale, "rebuilding"));
    try {
      await bridge.rebuildIndex(id);
    } catch (error) {
      setBusyText("");
      setNotice(error instanceof Error ? error.message : String(error));
    }
  };

  const openConversation = async (id: string) => {
    try {
      const conversation = await bridge.getConversation(id);
      setConversationId(id);
      setMessages(conversation.messages ?? []);
      const lastAssistant = [...(conversation.messages ?? [])].reverse().find((item) => item.role === "assistant");
      setSources(lastAssistant?.sources ?? []);
      setActiveView("chat");
    } catch (error) {
      setNotice(error instanceof Error ? error.message : String(error));
    }
  };

  const renameConversation = async (id: string, title: string) => {
    try {
      const updated = await bridge.renameHistory(id, title);
      setBootstrap((current) => current ? { ...current, conversations: current.conversations.map((item) => item.id === id ? updated : item) } : current);
    } catch (error) { setNotice(error instanceof Error ? error.message : String(error)); }
  };

  const deleteConversation = async (id: string) => {
    try {
      const result = await bridge.deleteHistory(id);
      if (result.deleted) setBootstrap((current) => current ? { ...current, conversations: current.conversations.filter((item) => item.id !== id) } : current);
    } catch (error) { setNotice(error instanceof Error ? error.message : String(error)); }
  };

  const saveFavorite = async () => {
    const assistantIndex = [...messages].map((item) => item.role).lastIndexOf("assistant");
    if (assistantIndex < 0) return;
    const assistant = messages[assistantIndex];
    const user = [...messages.slice(0, assistantIndex)].reverse().find((item) => item.role === "user");
    if (!user) return;
    try {
      const favorite = await bridge.saveFavorite(user.content, assistant.content);
      setBootstrap((current) => current ? { ...current, favorites: [...current.favorites, favorite] } : current);
      setNotice(locale === "zh" ? "已收藏回答" : "Answer saved");
    } catch (error) { setNotice(error instanceof Error ? error.message : String(error)); }
  };

  const deleteFavorite = async (id: string) => {
    try {
      const result = await bridge.deleteFavorite(id);
      if (result.deleted) setBootstrap((current) => current ? { ...current, favorites: current.favorites.filter((item) => item.id !== id) } : current);
    } catch (error) { setNotice(error instanceof Error ? error.message : String(error)); }
  };

  const saveSettings = async (update: SettingsUpdate) => {
    try {
      const payload = await bridge.saveSettings(update);
      setBootstrap(payload);
      document.documentElement.classList.toggle("dark", payload.theme === "dark");
      document.documentElement.lang = payload.locale === "zh" ? "zh-CN" : "en";
      setNotice(payload.locale === "zh" ? "设置已保存" : "Settings saved");
    } catch (error) { setNotice(error instanceof Error ? error.message : String(error)); }
  };

  const quickPreference = (update: SettingsUpdate) => void saveSettings(update);

  const content = useMemo(() => {
    if (!bootstrap) return null;
    if (activeView === "history") return <HistoryPage locale={locale} conversations={bootstrap.conversations} onOpen={openConversation} onRename={renameConversation} onDelete={deleteConversation} />;
    if (activeView === "favorites") return <FavoritesPage locale={locale} favorites={bootstrap.favorites} onDelete={deleteFavorite} />;
    if (activeView === "knowledge") return <KnowledgePage locale={locale} chunkCount={bootstrap.chunkCount} indexStatus={bootstrap.indexStatus} watcherStatus={bootstrap.watcherStatus} onImport={importDocument} onRebuild={rebuildIndex} />;
    if (activeView === "settings") return <SettingsPage locale={locale} theme={bootstrap.theme} bootstrap={bootstrap} onSave={saveSettings} />;
    return (
      <Suspense fallback={<div className="grid h-full place-items-center text-sm text-[var(--muted)]">{t(locale, "loading")}</div>}>
        <ChatPage locale={locale} messages={messages} question={question} busy={Boolean(busyText)} onQuestionChange={setQuestion} onAsk={ask} onImport={importDocument} onStop={stop} onSaveFavorite={saveFavorite} />
      </Suspense>
    );
  }, [activeView, bootstrap, busyText, locale, messages, question]);

  if (booting) return <AiLoader text={t(locale, "loading")} />;

  if (fatalError || !bootstrap) {
    return (
      <div className="error-screen">
        <div className="error-card">
          <AlertCircle className="size-8 text-rose-300" />
          <h1>{t(locale, "reconnectTitle")}</h1>
          <p>{t(locale, "reconnectBody")}</p>
          {fatalError && <code>{fatalError}</code>}
          <Button onClick={() => void loadBootstrap()}><RefreshCw className="size-4" />{t(locale, "reconnect")}</Button>
        </div>
      </div>
    );
  }

  return (
    <>
      <AppShell
        activeView={activeView}
        locale={bootstrap.locale}
        theme={bootstrap.theme}
        model={bootstrap.model}
        apiConfigured={bootstrap.apiConfigured}
        indexStatus={bootstrap.indexStatus}
        watcherStatus={bootstrap.watcherStatus}
        navOpen={navOpen}
        sourceOpen={sourceOpen}
        onNavOpenChange={setNavOpen}
        onSourceOpenChange={setSourceOpen}
        onViewChange={setActiveView}
        onNewChat={newChat}
        onThemeToggle={() => quickPreference({ theme: bootstrap.theme === "dark" ? "light" : "dark" })}
        onLocaleToggle={() => quickPreference({ locale: bootstrap.locale === "zh" ? "en" : "zh" })}
        sourcePanel={<SourcePanel locale={bootstrap.locale} sources={sources} />}
      >
        {content}
      </AppShell>
      {busyText && <AiLoader size={180} text={busyText} />}
      {notice && (
        <div className="notice-toast" role="status">
          <span>{notice}</span>
          <button onClick={() => setNotice("")} aria-label="关闭提示"><X className="size-4" /></button>
        </div>
      )}
    </>
  );
}
