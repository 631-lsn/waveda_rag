import type {
  BootstrapPayload,
  BridgeEvent,
  ConversationSummary,
  FavoriteItem,
  SettingsUpdate,
} from "./contracts";

export interface QtSignal {
  connect(listener: (payload: string) => void): void;
}

type QtMethod = (payload: string, done: (result: string) => void) => void;

export interface QtBackend {
  event_json: QtSignal;
  bootstrap?: QtMethod;
  ask?: QtMethod;
  stop_answer?: QtMethod;
  select_and_import_document?: QtMethod;
  list_history?: QtMethod;
  get_conversation?: QtMethod;
  rename_history?: QtMethod;
  delete_history?: QtMethod;
  list_favorites?: QtMethod;
  save_favorite?: QtMethod;
  delete_favorite?: QtMethod;
  save_settings?: QtMethod;
  select_provider?: QtMethod;
  rebuild_index?: QtMethod;
}

type BridgeListener = (event: BridgeEvent) => void;

function parseJson<T>(value: string): T {
  return JSON.parse(value) as T;
}

export class DesktopBridgeClient {
  private readonly listeners = new Set<BridgeListener>();

  constructor(private readonly backend: QtBackend) {
    backend.event_json.connect((payload) => {
      try {
        this.emit(parseJson<BridgeEvent>(payload));
      } catch {
        this.emit({
          type: "bridge_error",
          message: "Received an invalid desktop event.",
        });
      }
    });
  }

  subscribe(listener: BridgeListener): () => void {
    this.listeners.add(listener);
    return () => this.listeners.delete(listener);
  }

  bootstrap(): Promise<BootstrapPayload> {
    return this.invoke<BootstrapPayload>("bootstrap", {});
  }

  ask(requestId: string, question: string, conversationId?: string): Promise<{ accepted: boolean }> {
    return this.invoke("ask", { requestId, question, conversationId });
  }

  stopAnswer(requestId: string): Promise<{ stopped: boolean }> {
    return this.invoke("stop_answer", { requestId });
  }

  selectAndImportDocument(requestId: string): Promise<{ accepted: boolean }> {
    return this.invoke("select_and_import_document", { requestId });
  }

  listHistory(): Promise<ConversationSummary[]> {
    return this.invoke("list_history", {});
  }

  getConversation(id: string): Promise<ConversationSummary> {
    return this.invoke("get_conversation", { id });
  }

  renameHistory(id: string, title: string): Promise<ConversationSummary> {
    return this.invoke("rename_history", { id, title });
  }

  deleteHistory(id: string): Promise<{ deleted: boolean }> {
    return this.invoke("delete_history", { id });
  }

  listFavorites(): Promise<FavoriteItem[]> {
    return this.invoke("list_favorites", {});
  }

  saveFavorite(question: string, answer: string): Promise<FavoriteItem> {
    return this.invoke("save_favorite", { question, answer });
  }

  deleteFavorite(id: string): Promise<{ deleted: boolean }> {
    return this.invoke("delete_favorite", { id });
  }

  saveSettings(update: SettingsUpdate): Promise<BootstrapPayload> {
    return this.invoke("save_settings", update);
  }

  selectProvider(providerId: string): Promise<BootstrapPayload> {
    return this.invoke("select_provider", { providerId });
  }

  rebuildIndex(requestId: string): Promise<{ accepted: boolean }> {
    return this.invoke("rebuild_index", { requestId });
  }

  private invoke<T>(method: keyof QtBackend, payload: object): Promise<T> {
    const fn = this.backend[method];
    if (typeof fn !== "function") {
      return Promise.reject(new Error(`Desktop method is unavailable: ${String(method)}`));
    }
    return new Promise<T>((resolve, reject) => {
      try {
        fn.call(this.backend, JSON.stringify(payload), (result) => {
          try {
            const parsed = parseJson<T & { error?: string }>(result);
            if (typeof parsed === "object" && parsed !== null && "error" in parsed && parsed.error) {
              reject(new Error(parsed.error));
              return;
            }
            resolve(parsed);
          } catch {
            reject(new Error(`Desktop method returned invalid data: ${String(method)}`));
          }
        });
      } catch (error) {
        reject(error instanceof Error ? error : new Error(String(error)));
      }
    });
  }

  private emit(event: BridgeEvent) {
    this.listeners.forEach((listener) => listener(event));
  }
}

declare global {
  interface Window {
    qt?: { webChannelTransport?: unknown };
    QWebChannel?: new (
      transport: unknown,
      callback: (channel: { objects: { backend: QtBackend } }) => void,
    ) => unknown;
  }
}

async function loadWebChannelScript(): Promise<void> {
  if (window.QWebChannel) return;
  await new Promise<void>((resolve, reject) => {
    const script = document.createElement("script");
    script.src = "qrc:///qtwebchannel/qwebchannel.js";
    script.onload = () => resolve();
    script.onerror = () => reject(new Error("Unable to load the Qt WebChannel runtime."));
    document.head.append(script);
  });
}

export async function connectDesktopBridge(): Promise<DesktopBridgeClient> {
  const transport = window.qt?.webChannelTransport;
  if (!transport) {
    throw new Error("The desktop bridge is unavailable. Start the app with start.bat.");
  }
  await loadWebChannelScript();
  if (!window.QWebChannel) {
    throw new Error("The Qt WebChannel runtime is unavailable.");
  }
  return new Promise((resolve) => {
    new window.QWebChannel!(transport, (channel) => {
      resolve(new DesktopBridgeClient(channel.objects.backend));
    });
  });
}
