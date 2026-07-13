import { KeyRound, Languages, MonitorCog, Save, Sparkles } from "lucide-react";
import { useEffect, useState } from "react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import type { BootstrapPayload, Locale, Personality, SettingsUpdate, Theme } from "@/lib/contracts";
import { t } from "@/lib/i18n";
import { PERSONALITY_OPTIONS } from "@/lib/personality";
import { cn } from "@/lib/utils";

interface SettingsPageProps {
  locale: Locale;
  theme: Theme;
  bootstrap: BootstrapPayload;
  onSave(update: SettingsUpdate): void;
}

export function SettingsPage(props: SettingsPageProps) {
  const [tab, setTab] = useState<"api" | "personality" | "interface" | "language">("api");
  const [baseUrl, setBaseUrl] = useState(props.bootstrap.baseUrl);
  const [model, setModel] = useState(props.bootstrap.model);
  const [apiKey, setApiKey] = useState("");
  const [theme, setTheme] = useState<Theme>(props.theme);
  const [locale, setLocale] = useState<Locale>(props.locale);
  const [personality, setPersonality] = useState<Personality>(props.bootstrap.personality);
  useEffect(() => {
    setTheme(props.theme);
    setLocale(props.locale);
    setPersonality(props.bootstrap.personality);
  }, [props.bootstrap.personality, props.theme, props.locale]);

  const tabs = [
    { id: "api" as const, label: t(props.locale, "modelApi"), icon: KeyRound },
    { id: "personality" as const, label: props.locale === "zh" ? "人格" : "Personality", icon: Sparkles },
    { id: "interface" as const, label: t(props.locale, "interface"), icon: MonitorCog },
    { id: "language" as const, label: t(props.locale, "language"), icon: Languages },
  ];

  return (
    <section className="page-section">
      <div className="page-heading"><div><p className="eyebrow">PREFERENCES</p><h1>{t(props.locale, "settings")}</h1></div></div>
      <div className="settings-card">
        <div className="settings-tabs">{tabs.map(({ id, label, icon: Icon }) => <button key={id} onClick={() => setTab(id)} className={cn(tab === id && "active")}><Icon className="size-4" />{label}</button>)}</div>
        <div className="settings-content">
          {tab === "api" && <div className="settings-form"><label>Base URL<Input value={baseUrl} onChange={(e) => setBaseUrl(e.target.value)} /></label><label>Model<Input value={model} onChange={(e) => setModel(e.target.value)} /></label><label>API Key<Input type="password" value={apiKey} onChange={(e) => setApiKey(e.target.value)} placeholder={t(props.locale, "apiKeyHint")} /></label><p className="text-xs text-[var(--subtle)]">{props.bootstrap.apiConfigured ? t(props.locale, "apiConfigured") : t(props.locale, "apiMissing")}</p></div>}
          {tab === "personality" && (
            <div>
              <div className="mb-5">
                <h2 className="text-base font-semibold">{props.locale === "zh" ? "选择助手人格" : "Choose assistant personality"}</h2>
                <p className="mt-1 text-sm text-[var(--muted)]">{props.locale === "zh" ? "欢迎语与模型回答语气会保持一致，保存后立即生效。" : "Welcome copy and answer tone stay in sync and update immediately."}</p>
              </div>
              <div className="grid max-w-2xl gap-3 sm:grid-cols-2">
                {PERSONALITY_OPTIONS.map((option) => (
                  <button
                    key={option.id}
                    type="button"
                    onClick={() => setPersonality(option.id)}
                    aria-label={`${option.label[props.locale]} — ${option.description[props.locale]}`}
                    className={cn(
                      "flex min-h-24 items-start gap-3 rounded-2xl border bg-[var(--surface-2)] p-4 text-left transition",
                      personality === option.id
                        ? "border-cyan-400 shadow-[0_0_0_2px_rgba(34,211,238,.1)]"
                        : "border-[var(--border)] hover:border-cyan-400/50",
                    )}
                  >
                    <span
                      className="mt-1 size-3 shrink-0 rounded-full shadow-[0_0_14px_currentColor]"
                      style={{ backgroundColor: option.accent, color: option.accent }}
                    />
                    <span>
                      <span className="block text-sm font-semibold text-[var(--text)]">{option.label[props.locale]}</span>
                      <span className="mt-1 block text-xs leading-5 text-[var(--muted)]">{option.description[props.locale]}</span>
                    </span>
                  </button>
                ))}
              </div>
            </div>
          )}
          {tab === "interface" && <div className="option-grid">{(["dark", "light"] as Theme[]).map((value) => <button key={value} onClick={() => setTheme(value)} className={cn("theme-option", theme === value && "selected")}><span className={cn("theme-preview", value)} />{t(props.locale, value)}</button>)}</div>}
          {tab === "language" && <div className="option-grid"><button onClick={() => setLocale("zh")} className={cn("theme-option", locale === "zh" && "selected")}>中文</button><button onClick={() => setLocale("en")} className={cn("theme-option", locale === "en" && "selected")}>English</button></div>}
          <div className="mt-8"><Button onClick={() => props.onSave({ baseUrl, model, ...(apiKey ? { apiKey } : {}), theme, locale, personality })}><Save className="size-4" />{t(props.locale, "save")}</Button></div>
        </div>
      </div>
    </section>
  );
}
