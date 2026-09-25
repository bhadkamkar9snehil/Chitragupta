"use client";

import { useEffect, useMemo, useState } from "react";
import { Bot, BookOpen, Check, Code2, Copy, Loader2, Palette, Plus, RefreshCw, Trash2 } from "lucide-react";
import { toast } from "sonner";
import { api, type AiSettings, type AllSettings } from "@/lib/api";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Input, Label, Skeleton, Switch, Textarea } from "@/components/ui/primitives";
import { applyBrand } from "@/components/helpdesk/app";

type Preset = { id: string; name: string; kind: AiSettings["kind"]; baseUrl: string; key: boolean; note: string };

// Every option here is an officially supported API. A ChatGPT plan can only be used through the Codex CLI.
const PRESETS: Preset[] = [
  { id: "lmstudio", name: "LM Studio", kind: "openai", baseUrl: "http://100.111.69.102:1235/v1", key: false, note: "Local models over LM Studio's OpenAI-compatible server." },
  { id: "ollama", name: "Ollama", kind: "openai", baseUrl: "http://localhost:11434/v1", key: false, note: "Local models through Ollama's OpenAI-compatible endpoint." },
  { id: "openai", name: "OpenAI", kind: "openai", baseUrl: "https://api.openai.com/v1", key: true, note: "OpenAI API key from platform.openai.com." },
  { id: "anthropic", name: "Anthropic", kind: "anthropic", baseUrl: "https://api.anthropic.com/v1", key: true, note: "Claude models with an Anthropic API key." },
  { id: "gemini", name: "Google Gemini", kind: "openai", baseUrl: "https://generativelanguage.googleapis.com/v1beta/openai", key: true, note: "Gemini API key from Google AI Studio." },
  { id: "groq", name: "Groq", kind: "openai", baseUrl: "https://api.groq.com/openai/v1", key: true, note: "Fast hosted open models." },
  { id: "openrouter", name: "OpenRouter", kind: "openai", baseUrl: "https://openrouter.ai/api/v1", key: true, note: "Many providers behind one key." },
  { id: "codex", name: "ChatGPT plan", kind: "codex", baseUrl: "", key: false, note: "Runs through the Codex CLI signed in with `codex login`. Slower; no streaming." },
  { id: "custom", name: "Custom", kind: "openai", baseUrl: "", key: true, note: "Any server that speaks the OpenAI chat completions API." },
];

const TABS = [
  { id: "ai", label: "AI provider", icon: Bot },
  { id: "knowledge", label: "Knowledge", icon: BookOpen },
  { id: "appearance", label: "Appearance", icon: Palette },
  { id: "embed", label: "Embed", icon: Code2 },
];

export function SettingsView({ tab, onTab }: { tab?: string; onTab: (t: string) => void }) {
  const [settings, setSettings] = useState<AllSettings | null>(null);
  const current = TABS.some((t) => t.id === tab) ? tab! : "ai";

  useEffect(() => {
    api.admin.settings().then(setSettings).catch((e: Error) => toast.error(e.message));
  }, []);

  return (
    <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
      <div className="mx-auto max-w-5xl px-4 py-6 lg:px-8">
        <h1 className="text-heading font-semibold tracking-tight">Settings</h1>
        <div className="mt-5 flex flex-col gap-6 md:flex-row">
          <nav className="flex gap-1 overflow-x-auto md:w-48 md:shrink-0 md:flex-col" aria-label="Settings sections">
            {TABS.map((t) => (
              <button
                key={t.id}
                onClick={() => onTab(t.id)}
                aria-current={current === t.id ? "page" : undefined}
                className={cn("flex h-9 shrink-0 items-center gap-2.5 rounded-md px-2.5 text-meta font-medium text-muted-foreground hover:bg-surface-2 hover:text-foreground", current === t.id && "bg-surface-2 text-foreground")}
              >
                <t.icon className="size-4" aria-hidden /> {t.label}
              </button>
            ))}
          </nav>
          <div className="min-w-0 flex-1">
            {!settings ? (
              <Skeleton className="h-96" />
            ) : current === "ai" ? (
              <AiForm key={JSON.stringify(settings.ai)} initial={settings.ai} onSaved={setSettings} />
            ) : current === "knowledge" ? (
              <KnowledgeForm initial={settings.knowledge} onSaved={setSettings} />
            ) : current === "appearance" ? (
              <AppearanceForm initial={settings.widget} onSaved={setSettings} />
            ) : (
              <Embed />
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

function Card({ title, description, children, footer }: { title: string; description?: string; children: React.ReactNode; footer?: React.ReactNode }) {
  return (
    <section className="rounded-xl border bg-surface">
      <div className="p-5">
        <h2 className="text-sm font-semibold">{title}</h2>
        {description && <p className="mt-1 text-meta text-muted-foreground">{description}</p>}
        <div className="mt-5 space-y-5">{children}</div>
      </div>
      {footer && <div className="flex items-center justify-end gap-2 rounded-b-xl border-t bg-surface-2 px-5 py-3">{footer}</div>}
    </section>
  );
}

function Field({ label, hint, htmlFor, children }: { label: string; hint?: string; htmlFor?: string; children: React.ReactNode }) {
  return (
    <div>
      <Label htmlFor={htmlFor}>{label}</Label>
      <div className="mt-1.5">{children}</div>
      {hint && <p className="mt-1.5 text-xs text-subtle-foreground">{hint}</p>}
    </div>
  );
}

function AiForm({ initial, onSaved }: { initial: AiSettings; onSaved: (s: AllSettings) => void }) {
  const [draft, setDraft] = useState<AiSettings>({ ...initial, apiKey: "" });
  const [models, setModels] = useState<string[] | null>(null);
  const [modelsError, setModelsError] = useState("");
  const [busy, setBusy] = useState<"" | "models" | "test" | "save">("");
  const [test, setTest] = useState<{ ok: boolean; text: string } | null>(null);
  const preset = PRESETS.find((p) => p.id === draft.provider) ?? PRESETS.at(-1)!;
  const payload = () => ({ ...draft, apiKey: draft.apiKey ? draft.apiKey : "__keep__" });
  const dirty = JSON.stringify({ ...draft, apiKey: undefined }) !== JSON.stringify({ ...initial, apiKey: undefined }) || !!draft.apiKey;

  const pick = (p: Preset) => {
    setDraft((d) => ({ ...d, provider: p.id, kind: p.kind, baseUrl: p.baseUrl || d.baseUrl, model: p.id === d.provider ? d.model : "", apiKey: "" }));
    setModels(null);
    setTest(null);
  };

  const loadModels = async () => {
    setBusy("models");
    setModelsError("");
    try {
      const r = await api.admin.models(payload());
      if (Array.isArray(r)) setModels(r);
      else setModelsError(r.error);
    } finally {
      setBusy("");
    }
  };

  return (
    <div className="space-y-4">
      <Card title="Provider" description="Which model writes the assistant's replies. Jev still decides what to do on every turn.">
        <div className="grid gap-2 sm:grid-cols-3" role="radiogroup" aria-label="Provider">
          {PRESETS.map((p) => (
            <button
              key={p.id}
              role="radio"
              aria-checked={draft.provider === p.id}
              onClick={() => pick(p)}
              className={cn(
                "relative rounded-lg border bg-background p-3 text-left hover:border-border-strong",
                draft.provider === p.id && "border-primary ring-2 ring-ring",
              )}
            >
              <span className="block text-sm font-medium">{p.name}</span>
              <span className="mt-0.5 block text-xs text-muted-foreground">{p.kind === "anthropic" ? "Anthropic API" : p.kind === "codex" ? "Codex CLI" : "OpenAI-compatible"}</span>
              {draft.provider === p.id && <Check className="absolute right-2.5 top-2.5 size-4 text-primary" aria-hidden />}
            </button>
          ))}
        </div>
        <p className="text-meta text-muted-foreground">{preset.note}</p>
      </Card>

      <Card
        title="Connection"
        footer={
          <>
            {test && <span className={cn("mr-auto text-meta", test.ok ? "text-success" : "text-destructive")} role="status">{test.text}</span>}
            <Button
              variant="outline"
              disabled={!!busy}
              onClick={async () => {
                setBusy("test");
                setTest(null);
                try {
                  const r = await api.admin.test(payload());
                  setTest({ ok: r.ok, text: r.ok ? `Connected · replied in ${(r.ms / 1000).toFixed(1)}s` : r.error ?? "No reply" });
                } finally {
                  setBusy("");
                }
              }}
            >
              {busy === "test" && <Loader2 className="animate-spin" />} Test connection
            </Button>
            <Button
              disabled={!dirty || !!busy || !draft.model.trim()}
              onClick={async () => {
                setBusy("save");
                try {
                  onSaved(await api.admin.save("ai", payload()));
                  toast.success("AI provider saved", { description: "New conversations use it straight away." });
                } catch (e) {
                  toast.error((e as Error).message);
                } finally {
                  setBusy("");
                }
              }}
            >
              Save
            </Button>
          </>
        }
      >
        {draft.kind !== "codex" ? (
          <Field label="Server URL" htmlFor="baseUrl" hint="The API base, ending before /chat/completions or /messages.">
            <Input id="baseUrl" value={draft.baseUrl} onChange={(e) => setDraft({ ...draft, baseUrl: e.target.value })} placeholder="https://…/v1" spellCheck={false} />
          </Field>
        ) : (
          <Field label="Codex command" htmlFor="cmd" hint="Install with `npm i -g @openai/codex`, then run `codex login` once on the API server and choose Sign in with ChatGPT.">
            <Input id="cmd" value={draft.command ?? "codex"} onChange={(e) => setDraft({ ...draft, command: e.target.value })} spellCheck={false} />
          </Field>
        )}
        {(preset.key || draft.kind === "anthropic") && (
          <Field label="API key" htmlFor="key" hint={initial.hasApiKey && initial.provider === draft.provider ? "A key is stored (encrypted). Leave empty to keep it." : "Stored encrypted on the server; never sent back to the browser."}>
            <Input id="key" type="password" autoComplete="off" value={draft.apiKey ?? ""} onChange={(e) => setDraft({ ...draft, apiKey: e.target.value })} placeholder={initial.hasApiKey && initial.provider === draft.provider ? "••••••••••••" : "Paste key"} />
          </Field>
        )}
        <Field label="Model" htmlFor="model">
          <div className="flex gap-2">
            <Input id="model" list="models" value={draft.model} onChange={(e) => setDraft({ ...draft, model: e.target.value })} placeholder="Model id" spellCheck={false} />
            <Button variant="outline" onClick={loadModels} disabled={!!busy} aria-label="Load models from the server">
              {busy === "models" ? <Loader2 className="animate-spin" /> : <RefreshCw />} <span className="hidden sm:inline">Load models</span>
            </Button>
          </div>
          <datalist id="models">{models?.map((m) => <option key={m} value={m} />)}</datalist>
          {modelsError && <p className="mt-1.5 text-xs text-destructive">{modelsError}</p>}
          {models && (
            <div className="mt-2 flex max-h-32 flex-wrap gap-1.5 overflow-y-auto">
              {models.map((m) => (
                <button key={m} onClick={() => setDraft({ ...draft, model: m })} className={cn("rounded-md border px-2 py-1 font-mono text-xs hover:border-border-strong", draft.model === m && "border-primary bg-primary-soft text-primary-soft-foreground")}>
                  {m}
                </button>
              ))}
            </div>
          )}
        </Field>
        <div className="grid gap-5 sm:grid-cols-2">
          <Field label={`Temperature · ${draft.temperature}`} htmlFor="temp" hint="Lower is more consistent.">
            <input id="temp" type="range" min={0} max={1} step={0.05} value={draft.temperature} onChange={(e) => setDraft({ ...draft, temperature: Number(e.target.value) })} className="w-full accent-primary" />
          </Field>
          <Field label="Max reply length (tokens)" htmlFor="max">
            <Input id="max" type="number" min={100} max={4000} value={draft.maxTokens} onChange={(e) => setDraft({ ...draft, maxTokens: Number(e.target.value) })} />
          </Field>
        </div>
      </Card>
    </div>
  );
}

function KnowledgeForm({ initial, onSaved }: { initial: AllSettings["knowledge"]; onSaved: (s: AllSettings) => void }) {
  const [draft, setDraft] = useState(initial);
  const [q, setQ] = useState("");
  const [hits, setHits] = useState<{ Slug: string; Title: string; Type: string; Snippet: string }[] | null>(null);
  const [searching, setSearching] = useState(false);
  return (
    <div className="space-y-4">
      <Card
        title="XBatch world knowledge"
        description="The assistant searches the same generated XBatch world L2 investigates with (GBrain). Jev keeps only pages that help with the user's message."
        footer={<Button disabled={JSON.stringify(draft) === JSON.stringify(initial)} onClick={async () => { onSaved(await api.admin.save("knowledge", draft)); toast.success("Knowledge settings saved"); }}>Save</Button>}
      >
        <div className="flex items-center justify-between gap-4">
          <div>
            <Label htmlFor="gb">Use XBatch knowledge in answers</Label>
            <p className="text-xs text-subtle-foreground">Screens, reports and how XBatch behaves.</p>
          </div>
          <Switch id="gb" checked={draft.gbrain} onCheckedChange={(v) => setDraft({ ...draft, gbrain: v })} />
        </div>
        <div className="grid gap-5 sm:grid-cols-2">
          <Field label="GBrain source" htmlFor="src">
            <Input id="src" value={draft.source} onChange={(e) => setDraft({ ...draft, source: e.target.value })} spellCheck={false} />
          </Field>
          <Field label="Pages considered per message" htmlFor="lim">
            <Input id="lim" type="number" min={1} max={10} value={draft.limit} onChange={(e) => setDraft({ ...draft, limit: Number(e.target.value) })} />
          </Field>
        </div>
      </Card>
      <Card title="Try a search" description="See what the assistant would find for a question.">
        <form
          className="flex gap-2"
          onSubmit={async (e) => {
            e.preventDefault();
            if (!q.trim()) return;
            setSearching(true);
            try { setHits(await api.admin.searchKnowledge(q)); } finally { setSearching(false); }
          }}
        >
          <Input value={q} onChange={(e) => setQ(e.target.value)} placeholder="e.g. which screen shows billets on the charging bed" aria-label="Question" />
          <Button type="submit" variant="outline" disabled={searching}>{searching ? <Loader2 className="animate-spin" /> : "Search"}</Button>
        </form>
        {hits && (
          <ul className="divide-y rounded-lg border">
            {hits.map((h) => (
              <li key={h.Slug} className="p-3">
                <p className="text-sm font-medium">{h.Title} <span className="ml-1 text-xs font-normal text-subtle-foreground">{h.Type}</span></p>
                <p className="mt-1 line-clamp-2 text-xs text-muted-foreground">{h.Snippet.replace(/[#*`]/g, "")}</p>
              </li>
            ))}
            {!hits.length && <li className="p-3 text-sm text-muted-foreground">No pages found.</li>}
          </ul>
        )}
      </Card>
    </div>
  );
}

const SWATCHES = ["#c2410c", "#b45309", "#0f766e", "#1d4ed8", "#6d28d9", "#be123c", "#334155"];

function AppearanceForm({ initial, onSaved }: { initial: AllSettings["widget"]; onSaved: (s: AllSettings) => void }) {
  const [draft, setDraft] = useState(initial);
  const [newSuggestion, setNewSuggestion] = useState("");
  useEffect(() => {
    applyBrand(draft.accent);
    return () => applyBrand(initial.accent);
  }, [draft.accent, initial.accent]);

  return (
    <div className="grid gap-4 xl:grid-cols-5">
      <div className="xl:col-span-3">
        <Card
          title="Look and feel"
          footer={<Button disabled={JSON.stringify(draft) === JSON.stringify(initial)} onClick={async () => { onSaved(await api.admin.save("widget", draft)); toast.success("Appearance saved"); }}>Save</Button>}
        >
          <Field label="Helpdesk name" htmlFor="name">
            <Input id="name" value={draft.name} onChange={(e) => setDraft({ ...draft, name: e.target.value })} maxLength={60} />
          </Field>
          <Field label="Greeting" htmlFor="greet" hint="Shown under the greeting on the home screen.">
            <Textarea id="greet" rows={2} value={draft.greeting} onChange={(e) => setDraft({ ...draft, greeting: e.target.value })} maxLength={240} />
          </Field>
          <Field label="Accent colour">
            <div className="flex flex-wrap items-center gap-2">
              {SWATCHES.map((c) => (
                <button
                  key={c}
                  onClick={() => setDraft({ ...draft, accent: c })}
                  aria-label={`Use ${c}`}
                  aria-pressed={draft.accent === c}
                  className={cn("size-8 rounded-full ring-offset-2 ring-offset-surface", draft.accent === c && "ring-2 ring-foreground")}
                  ref={(el) => {
                    el?.style.setProperty("background", c);
                  }}
                />
              ))}
              <input type="color" value={draft.accent} onChange={(e) => setDraft({ ...draft, accent: e.target.value })} aria-label="Custom colour" className="size-8 cursor-pointer rounded-full border bg-transparent" />
              <span className="font-mono text-xs text-muted-foreground">{draft.accent}</span>
            </div>
          </Field>
          <Field label="Suggested questions" hint="Offered on the home screen and in new conversations.">
            <ul className="space-y-1.5">
              {draft.suggestions.map((s, i) => (
                <li key={i} className="flex items-center gap-2">
                  <Input value={s} onChange={(e) => setDraft({ ...draft, suggestions: draft.suggestions.map((x, j) => (j === i ? e.target.value : x)) })} aria-label={`Suggestion ${i + 1}`} />
                  <Button variant="ghost" size="icon-sm" aria-label="Remove suggestion" onClick={() => setDraft({ ...draft, suggestions: draft.suggestions.filter((_, j) => j !== i) })}>
                    <Trash2 />
                  </Button>
                </li>
              ))}
            </ul>
            {draft.suggestions.length < 6 && (
              <form
                className="mt-2 flex gap-2"
                onSubmit={(e) => {
                  e.preventDefault();
                  if (!newSuggestion.trim()) return;
                  setDraft({ ...draft, suggestions: [...draft.suggestions, newSuggestion.trim()] });
                  setNewSuggestion("");
                }}
              >
                <Input value={newSuggestion} onChange={(e) => setNewSuggestion(e.target.value)} placeholder="Add a suggestion" aria-label="New suggestion" />
                <Button type="submit" variant="outline" aria-label="Add suggestion"><Plus /></Button>
              </form>
            )}
          </Field>
        </Card>
      </div>
      <div className="xl:col-span-2">
        <p className="mb-2 text-2xs font-semibold uppercase tracking-wider text-subtle-foreground">Preview</p>
        <div className="overflow-hidden rounded-xl border bg-background shadow-pop">
          <div className="border-b bg-surface p-4">
            <div className="flex items-center gap-2">
              <span className="size-6 rounded-md bg-primary" aria-hidden />
              <span className="text-sm font-semibold">{draft.name}</span>
            </div>
            <p className="mt-4 text-lg font-semibold tracking-tight">Good morning, Krishna</p>
            <p className="mt-1 text-meta text-muted-foreground">{draft.greeting}</p>
            <div className="mt-3 flex h-10 items-center justify-between rounded-lg border bg-background px-3 text-meta text-subtle-foreground">
              Describe the problem…
              <span className="size-6 rounded-md bg-primary" aria-hidden />
            </div>
            <div className="mt-2 flex flex-wrap gap-1.5">
              {draft.suggestions.slice(0, 3).map((s) => <span key={s} className="rounded-full border px-2 py-1 text-2xs text-muted-foreground">{s}</span>)}
            </div>
          </div>
          <div className="space-y-2 p-4">
            <div className="ml-auto w-fit rounded-2xl rounded-br-md bg-primary px-3 py-2 text-meta text-primary-foreground">GR not happening for heat 1603945</div>
            <div className="w-fit max-w-full rounded-xl border bg-surface px-3 py-2 text-meta">I&apos;ve raised #35 for the support team.</div>
          </div>
        </div>
      </div>
    </div>
  );
}

function Embed() {
  const origin = typeof location === "undefined" ? "" : location.origin;
  const iframe = useMemo(
    () => `<iframe src="${origin}/?user={XStudioUserID}" title="XBatch Helpdesk" style="width:100%;height:100%;border:0" allow="clipboard-write"></iframe>`,
    [origin],
  );
  const launcher = useMemo(() => `<script src="${origin}/embed.js" data-user="{XStudioUserID}" defer></script>`, [origin]);
  return (
    <div className="space-y-4">
      <Card title="Full-page embed" description="For an XStudio page control with Load URL as iFrame. Replace {XStudioUserID} with the signed-in user's ID when XStudio can pass it; until then users pick their account once per browser.">
        <Snippet code={iframe} />
        <ul className="space-y-1.5 text-meta text-muted-foreground">
          <li><code className="font-mono text-xs text-foreground">#/tickets</code> or <code className="font-mono text-xs text-foreground">#/tickets/&lt;id&gt;</code> opens tickets directly; <code className="font-mono text-xs text-foreground">#/messages</code> opens conversations.</li>
          <li><code className="font-mono text-xs text-foreground">&amp;theme=light</code> or <code className="font-mono text-xs text-foreground">dark</code> fixes the theme; otherwise it follows the device.</li>
        </ul>
      </Card>
      <Card title="Floating launcher" description="Adds a help button to the corner of any page that opens the helpdesk in a panel.">
        <Snippet code={launcher} />
      </Card>
    </div>
  );
}

function Snippet({ code }: { code: string }) {
  const [copied, setCopied] = useState(false);
  return (
    <div className="relative">
      <pre className="scrollbar-thin overflow-x-auto rounded-lg border bg-surface-2 p-3 pr-12 font-mono text-xs leading-relaxed">{code}</pre>
      <Button
        variant="ghost"
        size="icon-sm"
        className="absolute right-1.5 top-1.5"
        aria-label="Copy"
        onClick={async () => {
          await navigator.clipboard.writeText(code).catch(() => {});
          setCopied(true);
          setTimeout(() => setCopied(false), 1500);
        }}
      >
        {copied ? <Check /> : <Copy />}
      </Button>
    </div>
  );
}

