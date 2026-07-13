export type Locale = "zh" | "en";
export type Theme = "dark" | "light";
export type Personality = "normal" | "mature" | "sweet" | "dog" | "cat" | "workhorse";
export type AnswerPhase = "retrieving" | "generating";

export interface SourceItem {
  id: string;
  title: string;
  section: string;
  path: string;
  sourceType: string;
  score: number;
  excerpt: string;
  content?: string;
  images?: Array<{ src: string; title: string }>;
}

export interface ConversationMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  createdAt: string;
  sources?: SourceItem[];
  warning?: string | null;
}

export interface ConversationSummary {
  id: string;
  title: string;
  createdAt: string;
  updatedAt: string;
  messages?: ConversationMessage[];
}

export interface FavoriteItem {
  id: string;
  question: string;
  answer: string;
  createdAt: string;
}

export interface ModelProvider {
  id: string;
  label: string;
  baseUrl: string;
  model: string;
}

export interface BootstrapPayload {
  locale: Locale;
  theme: Theme;
  personality: Personality;
  apiConfigured: boolean;
  model: string;
  baseUrl: string;
  providerId: string;
  providers: ModelProvider[];
  chunkCount: number;
  indexStatus: "ready" | "missing" | "building" | "error";
  watcherStatus: "active" | "idle" | "changed" | "rebuilding" | "error";
  conversations: ConversationSummary[];
  favorites: FavoriteItem[];
}

export interface SettingsUpdate {
  providerId?: string;
  baseUrl?: string;
  model?: string;
  apiKey?: string;
  theme?: Theme;
  locale?: Locale;
  personality?: Personality;
  wavedaRoot?: string;
  wavedaHelpRoot?: string;
  wavedaExampleRoot?: string;
}

export type BridgeEvent =
  | {
      type: "answer_progress";
      requestId: string;
      phase: AnswerPhase;
    }
  | {
      type: "answer_completed";
      requestId: string;
      conversation: ConversationSummary;
      answer: string;
      sources: SourceItem[];
      warning?: string | null;
    }
  | {
      type: "answer_failed";
      requestId: string;
      message: string;
    }
  | {
      type: "import_progress";
      requestId: string;
      phase: "selecting" | "importing" | "rebuilding";
    }
  | {
      type: "import_completed";
      requestId: string;
      fileName: string;
      chunkCount: number;
    }
  | {
      type: "import_cancelled";
      requestId: string;
    }
  | {
      type: "import_failed" | "index_failed";
      requestId: string;
      message: string;
    }
  | {
      type: "index_changed";
      chunkCount: number;
      status: BootstrapPayload["indexStatus"];
    }
  | {
      type: "watcher_changed";
      status: BootstrapPayload["watcherStatus"];
    }
  | {
      type: "bridge_error";
      message: string;
    };
