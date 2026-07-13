"use client";

import * as React from "react";
import { Bot, ChevronDown, LoaderCircle, Send, Square } from "lucide-react";

import { cn } from "@/lib/utils";

const SPRING = "0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275)";
const SMOOTH = "0.15s ease-out";

export interface ModelOption {
  id: string;
  label: string;
  model: string;
}

export interface PromptInputProps {
  value: string;
  onChange(value: string): void;
  onSubmit(): void;
  busy: boolean;
  onStop(): void;
  placeholder?: string;
  models: ModelOption[];
  selectedModelId: string;
  onModelChange(modelId: string): void;
  modelSwitching?: boolean;
  className?: string;
}

function MorphingText({ text }: { text: string }) {
  const spanRef = React.useRef<HTMLSpanElement>(null);
  const [width, setWidth] = React.useState<number | "auto">("auto");

  React.useEffect(() => {
    if (spanRef.current) setWidth(spanRef.current.offsetWidth);
  }, [text]);

  return (
    <span
      className="relative inline-flex items-center overflow-hidden transition-all duration-300"
      style={{ width }}
    >
      <span ref={spanRef} className="invisible whitespace-nowrap px-0.5">
        {text}
      </span>
      <span
        key={text}
        className="absolute inset-0 flex animate-in items-center whitespace-nowrap fade-in zoom-in-95 duration-300"
      >
        {text}
      </span>
    </span>
  );
}

export const PromptInput = React.forwardRef<HTMLDivElement, PromptInputProps>(
  (
    {
      value,
      onChange,
      onSubmit,
      busy,
      onStop,
      placeholder = "Ask anything",
      models,
      selectedModelId,
      onModelChange,
      modelSwitching = false,
      className,
    },
    forwardedRef,
  ) => {
    const [expanded, setExpanded] = React.useState(Boolean(value || busy));
    const [smoothResize, setSmoothResize] = React.useState(false);
    const [modelMenuOpen, setModelMenuOpen] = React.useState(false);
    const [textareaHeight, setTextareaHeight] = React.useState(68);
    const rootRef = React.useRef<HTMLDivElement>(null);
    const textareaRef = React.useRef<HTMLTextAreaElement>(null);
    const currentModel = models.find((model) => model.id === selectedModelId) ?? models[0];
    const canSubmit = value.trim().length > 0 && !modelSwitching;

    React.useImperativeHandle(forwardedRef, () => rootRef.current as HTMLDivElement);

    React.useEffect(() => {
      if ((value.trim() || busy) && !expanded) {
        setSmoothResize(false);
        setExpanded(true);
      }
    }, [busy, expanded, value]);

    React.useEffect(() => {
      const textarea = textareaRef.current;
      if (!textarea) return;
      textarea.style.height = "0px";
      const nextHeight = Math.max(68, Math.min(textarea.scrollHeight, 160));
      textarea.style.height = `${nextHeight}px`;
      setTextareaHeight(nextHeight);
    }, [expanded, value]);

    React.useEffect(() => {
      if (!expanded || busy) return;
      const timer = window.setTimeout(() => textareaRef.current?.focus(), 40);
      return () => window.clearTimeout(timer);
    }, [busy, expanded]);

    const expand = () => {
      setSmoothResize(false);
      setExpanded(true);
    };

    const collapseIfEmpty = (event: React.FocusEvent<HTMLDivElement>) => {
      if (rootRef.current?.contains(event.relatedTarget as Node)) return;
      if (!value.trim() && !busy) {
        setSmoothResize(false);
        setExpanded(false);
        setModelMenuOpen(false);
      }
    };

    const submit = () => {
      if (canSubmit && !busy) onSubmit();
    };

    return (
      <div
        ref={rootRef}
        onBlur={collapseIfEmpty}
        onKeyDown={(event) => {
          if (event.key === "Escape") setModelMenuOpen(false);
        }}
        className={cn("relative flex w-full flex-col", className)}
      >
        <div
          className={cn(
            "relative z-10 w-full border border-border bg-card shadow-lg",
            "focus-within:border-ring/60 focus-within:ring-2 focus-within:ring-ring/15",
          )}
          style={{
            height: expanded ? Math.max(116, textareaHeight + 48) : 48,
            borderRadius: expanded ? 24 : 9999,
            transition: `height ${smoothResize ? SMOOTH : SPRING}, border-radius ${SPRING}`,
            overflow: expanded ? "visible" : "hidden",
          }}
        >
          <textarea
            ref={textareaRef}
            aria-label="Prompt"
            value={value}
            onChange={(event) => {
              setSmoothResize(true);
              onChange(event.target.value);
            }}
            onKeyDown={(event) => {
              if (event.key === "Enter" && !event.shiftKey) {
                event.preventDefault();
                submit();
              }
              if (event.key === "Escape" && !value.trim()) {
                setExpanded(false);
                setModelMenuOpen(false);
              }
            }}
            placeholder={placeholder}
            disabled={busy}
            className={cn(
              "prompt-scrollbar absolute inset-x-0 top-0 z-[1] w-full resize-none overflow-y-auto bg-transparent",
              "px-4 pb-3 pr-14 pt-3.5 text-sm leading-[22px] text-foreground outline-none placeholder:text-muted-foreground",
              "transition-all duration-300",
              expanded
                ? "pointer-events-auto translate-y-0 scale-100 opacity-100"
                : "pointer-events-none -translate-y-1 scale-95 opacity-0",
            )}
          />

          <button
            type="button"
            onClick={expand}
            aria-label="Open prompt input"
            className={cn(
              "absolute inset-x-0 top-0 z-[1] h-12 px-5 pr-14 text-left text-sm font-medium text-muted-foreground outline-none",
              "transition-all duration-300",
              expanded
                ? "pointer-events-none translate-y-1 scale-105 opacity-0"
                : "translate-y-0 scale-100 opacity-100",
            )}
          >
            {placeholder}
          </button>

          <div
            className={cn(
              "absolute bottom-2 left-3 right-12 z-10 flex items-center gap-1 transition-all duration-300",
              expanded
                ? "pointer-events-auto translate-y-0 opacity-100"
                : "pointer-events-none translate-y-2 opacity-0 blur-sm",
            )}
          >
            <div className="relative min-w-0">
              <button
                type="button"
                disabled={modelSwitching || models.length === 0}
                onMouseDown={(event) => event.preventDefault()}
                onClick={() => setModelMenuOpen((open) => !open)}
                aria-label={`Select model. Current: ${currentModel?.label ?? "Unavailable"}`}
                className={cn(
                  "flex max-w-52 items-center gap-1.5 rounded-full px-2 py-1 text-xs font-semibold text-muted-foreground",
                  "transition-colors hover:bg-accent hover:text-accent-foreground disabled:pointer-events-none disabled:opacity-50",
                  modelMenuOpen && "bg-accent text-accent-foreground",
                )}
              >
                {modelSwitching ? (
                  <LoaderCircle className="size-3.5 shrink-0 animate-spin" />
                ) : (
                  <Bot className="size-3.5 shrink-0" />
                )}
                <span className="min-w-0 truncate">
                  <MorphingText text={currentModel?.label ?? "No model"} />
                </span>
                <ChevronDown className="size-3 shrink-0" />
              </button>

              <div
                className={cn(
                  "absolute bottom-full left-0 z-50 mb-2.5 w-64 origin-bottom-left rounded-2xl border border-border bg-popover/95 p-1.5 shadow-2xl backdrop-blur-xl",
                  "transition-all duration-300",
                  modelMenuOpen
                    ? "pointer-events-auto translate-y-0 scale-100 opacity-100"
                    : "pointer-events-none translate-y-3 scale-95 opacity-0",
                )}
              >
                {models.map((model) => (
                  <button
                    key={model.id}
                    type="button"
                    onMouseDown={(event) => event.preventDefault()}
                    onClick={() => {
                      setModelMenuOpen(false);
                      if (model.id !== selectedModelId) onModelChange(model.id);
                    }}
                    aria-label={`${model.label} · ${model.model}`}
                    className={cn(
                      "flex w-full items-center gap-2 rounded-xl px-2.5 py-2 text-left text-xs transition-colors",
                      "hover:bg-accent hover:text-accent-foreground",
                      model.id === selectedModelId
                        ? "bg-accent/70 text-accent-foreground"
                        : "text-popover-foreground",
                    )}
                  >
                    <Bot className="size-3.5 shrink-0" />
                    <span className="min-w-0 flex-1">
                      <span className="block truncate font-semibold">{model.label}</span>
                      <span className="block truncate text-[10px] text-muted-foreground">{model.model}</span>
                    </span>
                  </button>
                ))}
              </div>
            </div>
          </div>

          <button
            type="button"
            onMouseDown={(event) => event.preventDefault()}
            onClick={() => (busy ? onStop() : submit())}
            disabled={!busy && !canSubmit}
            aria-label={busy ? "Stop generation" : "Send prompt"}
            className={cn(
              "absolute bottom-2 right-2 z-20 flex size-8 items-center justify-center rounded-full",
              "bg-primary text-primary-foreground transition-all duration-300 hover:opacity-90",
              "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-40",
            )}
          >
            {busy ? <Square className="size-3.5 fill-current" /> : <Send className="size-3.5" />}
          </button>
        </div>
      </div>
    );
  },
);

PromptInput.displayName = "PromptInput";
