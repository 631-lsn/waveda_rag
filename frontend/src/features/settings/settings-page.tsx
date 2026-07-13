import { KeyRound, Languages, MonitorCog, Save } from "lucide-react";
import { useEffect, useState } from "react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import type { BootstrapPayload, Locale, SettingsUpdate, Theme } from "@/lib/contracts";
import { t } from "@/lib/i18n";
import { cn } from "@/lib/utils";

interface SettingsPageProps {
  locale: Locale;
  theme: Theme;
  bootstrap: BootstrapPayload;
  onSave(update: SettingsUpdate): void;
}

export function SettingsPage(props: SettingsPageProps) {
  const [tab, setTab] = useState<"api" | "interface" | "language">("api");
  const [baseUrl, setBaseUrl] = useState(props.bootstrap.baseUrl);
  const [model, setModel] = useState(props.bootstrap.model);
  const [apiKey, setApiKey] = useState("");
  const [theme, setTheme] = useState<Theme>(props.theme);
  const [locale, setLocale] = useState<Locale>(props.locale);
  useEffect(() => { setTheme(props.theme); setLocale(props.locale); }, [props.theme, props.locale]);

  const tabs = [
    { id: "api" as const, label: t(props.locale, "modelApi"), icon: KeyRound },
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
          {tab === "interface" && <div className="option-grid">{(["dark", "light"] as Theme[]).map((value) => <button key={value} onClick={() => setTheme(value)} className={cn("theme-option", theme === value && "selected")}><span className={cn("theme-preview", value)} />{t(props.locale, value)}</button>)}</div>}
          {tab === "language" && <div className="option-grid"><button onClick={() => setLocale("zh")} className={cn("theme-option", locale === "zh" && "selected")}>中文</button><button onClick={() => setLocale("en")} className={cn("theme-option", locale === "en" && "selected")}>English</button></div>}
          <div className="mt-8"><Button onClick={() => props.onSave({ baseUrl, model, ...(apiKey ? { apiKey } : {}), theme, locale })}><Save className="size-4" />{t(props.locale, "save")}</Button></div>
        </div>
      </div>
    </section>
  );
}
