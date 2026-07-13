import { Heart } from "lucide-react";
import ReactMarkdown from "react-markdown";
import rehypeKatex from "rehype-katex";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";

import { Button } from "@/components/ui/button";
import { PromptInput } from "@/components/ui/ai-chat-input";
import { ScrollArea } from "@/components/ui/scroll-area";
import type { ConversationMessage, Locale, ModelProvider } from "@/lib/contracts";
import { t } from "@/lib/i18n";
import { cn } from "@/lib/utils";

interface ChatPageProps {
  locale: Locale;
  messages: ConversationMessage[];
  question: string;
  busy: boolean;
  providers: ModelProvider[];
  providerId: string;
  modelSwitching: boolean;
  onQuestionChange(value: string): void;
  onAsk(): void;
  onStop(): void;
  onModelChange(providerId: string): void;
  onSaveFavorite(): void;
}

export function ChatPage(props: ChatPageProps) {
  const lastMessage = props.messages.at(-1);

  return (
    <div className="chat-layout">
      <ScrollArea className="chat-scroll">
        <div className="mx-auto w-full max-w-4xl px-5 pb-36 pt-8 sm:px-8">
          {props.messages.length === 0 ? (
            <div className="welcome-card">
              <div className="welcome-orb" />
              <p className="eyebrow">RESEARCH COPILOT</p>
              <h1>{t(props.locale, "welcome")}</h1>
              <p>{t(props.locale, "welcomeBody")}</p>
              <div className="mt-8 grid gap-3 sm:grid-cols-3">
                {["波端口怎么设置？", "PML 边界为什么报错？", "如何导出 S 参数？"].map((sample) => (
                  <button key={sample} className="sample-card" onClick={() => props.onQuestionChange(sample)}>{sample}</button>
                ))}
              </div>
            </div>
          ) : (
            <div className="space-y-7">
              {props.messages.map((message) => (
                <article key={message.id} className={cn("message-row", message.role === "user" && "message-row-user")}>
                  <div className={cn("message-bubble", message.role === "user" ? "message-user" : "message-assistant")}>
                    {message.role === "assistant" ? (
                      <div className="markdown-body">
                        <ReactMarkdown remarkPlugins={[remarkGfm, remarkMath]} rehypePlugins={[rehypeKatex]}>
                          {message.content}
                        </ReactMarkdown>
                        {message.warning && <p className="warning-note">{message.warning}</p>}
                      </div>
                    ) : (
                      <p className="whitespace-pre-wrap">{message.content}</p>
                    )}
                  </div>
                </article>
              ))}
              {lastMessage?.role === "assistant" && (
                <div className="flex justify-start">
                  <Button variant="ghost" size="sm" onClick={props.onSaveFavorite}>
                    <Heart className="size-3.5" />
                    {t(props.locale, "saveFavorite")}
                  </Button>
                </div>
              )}
            </div>
          )}
        </div>
      </ScrollArea>

      <div className="composer-wrap">
        <PromptInput
          className="mx-auto max-w-[760px]"
          value={props.question}
          onChange={props.onQuestionChange}
          onSubmit={props.onAsk}
          busy={props.busy}
          onStop={props.onStop}
          placeholder={t(props.locale, "placeholder")}
          models={props.providers}
          selectedModelId={props.providerId}
          onModelChange={props.onModelChange}
          modelSwitching={props.modelSwitching}
          labels={{
            input: t(props.locale, "askLabel"),
            open: t(props.locale, "placeholder"),
            selectModel: props.locale === "zh" ? "选择模型" : "Select model",
            current: props.locale === "zh" ? "当前" : "Current",
            send: t(props.locale, "send"),
            stop: t(props.locale, "stop"),
          }}
        />
        <p className="mt-2 text-center text-[11px] text-[var(--subtle)]">Enter {props.locale === "zh" ? "发送，Shift + Enter 换行" : "to send, Shift + Enter for a new line"}</p>
      </div>
    </div>
  );
}
