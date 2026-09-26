"use client";

import { useEffect, useState } from "react";
import { ArrowDown, ArrowRight, Bot, Clock3, Cpu, Database, MessageSquare, ShieldCheck, Sparkles, Waypoints, Wrench } from "lucide-react";
import { api, ops, type AiSettings, type Board, type ToolStats } from "@/lib/api";
import { ago, describeEvent, human, ticketLabel, when } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/primitives";
import { Legend, PageTitle, Panel, Segmented, Stat, ms as fmtMs } from "@/components/ui/viz";
import { FanOut, VolumeBar, type FanRow } from "@/components/ui/charts";
import { AGENT } from "./board";

const LEVELS = [
  { id: "Autonomous", label: "Autonomous", tone: "signal" as const, note: "the agent acts on its own" },
  { id: "RequiresApproval", label: "Needs approval", tone: "warn" as const, note: "a person must approve first" },
  { id: "Prohibited", label: "Prohibited", tone: "danger" as const, note: "never allowed" },
];

// Respect the OS setting: SMIL animation ignores CSS media queries, so the graph asks directly.
function useReducedMotion() {
  const [reduced, setReduced] = useState(false);
  useEffect(() => {
    const q = window.matchMedia("(prefers-reduced-motion: reduce)");
    const sync = () => setReduced(q.matches);
    sync();
    q.addEventListener("change", sync);
    return () => q.removeEventListener("change", sync);
  }, []);
  return reduced;
}

export function AgentsView({ onOpenRun }: { onOpenRun: (id: string) => void }) {
  const [tools, setTools] = useState<ToolStats | null>(null);
  const [failed, setFailed] = useState<string | null>(null);
  const [board, setBoard] = useState<Board | null>(null);
  const [ai, setAi] = useState<AiSettings | null>(null);
  const [focus, setFocus] = useState("jev");

  const load = () => {
    ops.tools().then((t) => { setTools(t); setFailed(null); }).catch((e: Error) => setFailed(e.message));
    ops.board().then(setBoard).catch(() => {});
    api.admin.settings().then((s) => setAi(s.ai)).catch(() => {});
  };
  useEffect(() => {
    const first = setTimeout(load, 0);
    return () => clearTimeout(first);
  }, []);

  const jevCalls = tools?.jev.reduce((n, j) => n + j.Calls, 0) ?? 0;

  return (
    <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
      <div className="space-y-3 px-4 py-3 lg:px-6">
        <PageTitle icon={Wrench} title="Agents & tools" meta="Who does the work, which tools they call, and what they are allowed to do" />

        {failed && !tools && (
          <div role="alert" className="flex flex-wrap items-center gap-3 rounded-xl border border-destructive/40 bg-destructive-soft p-3 text-sm text-destructive">
            <span className="min-w-0 flex-1">{failed}</span>
            <Button size="sm" variant="outline" onClick={load}>Try again</Button>
          </div>
        )}

        <div className="grid gap-3 xl:grid-cols-12">
          <Panel icon={Waypoints} title="Who does the work" meta="How a problem moves between them · select one to inspect" className="xl:col-span-12">
            <AgentFlow focus={focus} onFocus={setFocus} tools={tools} board={board} ai={ai} />
            <AgentInspector focus={focus} tools={tools} board={board} ai={ai} />
          </Panel>

          <ToolGraph tools={tools} className="xl:col-span-8" />

          <Panel icon={Sparkles} title="Jev decisions" meta={tools ? `${jevCalls.toLocaleString("en-IN")} typed judgments · by kind` : "Loading"} className="xl:col-span-4">
            {!tools ? <Skeleton className="h-72" /> : <JevBars tools={tools} />}
          </Panel>

          <Permissions tools={tools} className="xl:col-span-12" />
          <AuditedReads tools={tools} onOpenRun={onOpenRun} className="xl:col-span-12" />
        </div>
      </div>
    </div>
  );
}

// The workers as the path a problem takes: chat -> judgment -> investigation -> (writing) -> review.
// Vertical on phones and tablets, a row on wide screens.
function AgentFlow({ focus, onFocus, tools, board, ai }: { focus: string; onFocus: (f: string) => void; tools: ToolStats | null; board: Board | null; ai: AiSettings | null }) {
  const counts = (id: string) => board?.stats?.by_assignee[id] ?? {};
  const tally = (id: string) => (board?.stats ? Object.entries(counts(id)).map(([st, n]) => `${n} ${st}`).join(" · ") || "idle" : undefined);
  const model = tools?.models[0];
  const steps: { id: string; icon: typeof Bot; name: string; does: string; value?: string; optional?: boolean; accent?: boolean }[] = [
    { id: "l1", icon: MessageSquare, name: "L1 assistant", does: "answers or raises a ticket", value: ai?.model },
    { id: "jev", icon: Sparkles, name: "Jev", does: "decides every step", value: tools ? `${tools.jev.reduce((a, j) => a + j.Calls, 0).toLocaleString("en-IN")} decisions` : undefined, accent: true },
    { id: "agent:l2-jev-investigator", icon: Bot, name: "Investigator", does: "reads XBatch, proposes", value: tally("l2-jev-investigator") },
    ...(model ? [{ id: `model:${model.Model}`, icon: Cpu, name: "Writer", does: "only if reasoning is needed", value: `${model.Calls} calls`, optional: true }] : []),
    { id: "agent:l2-reviewer-primary", icon: ShieldCheck, name: "Reviewer", does: "checks before publishing", value: tally("l2-reviewer-primary") },
  ];
  return (
    <div className="dot-grid rounded-lg p-3">
      <ol className="flex flex-col gap-1 xl:flex-row xl:items-center xl:gap-2">
        {steps.map((st, i) => (
          <li key={st.id} className="flex flex-col items-stretch gap-1 xl:flex-1 xl:flex-row xl:items-center xl:gap-2">
            {i > 0 && <>
              <ArrowDown className={cn("mx-auto size-4 shrink-0 xl:hidden", st.optional ? "text-subtle-foreground" : "text-signal")} aria-hidden />
              <ArrowRight className={cn("hidden size-4 shrink-0 xl:block", st.optional ? "text-subtle-foreground" : "text-signal")} aria-hidden />
            </>}
            <button type="button" onClick={() => onFocus(st.id)} aria-pressed={focus === st.id}
              className={cn("flex w-full min-w-0 flex-wrap items-center gap-x-3 gap-y-0.5 rounded-xl border bg-surface p-3 text-left hover:border-border-strong xl:block", st.optional && "border-dashed", focus === st.id && "border-signal ring-1 ring-signal/40")}>
              <span className="flex min-w-0 flex-1 items-center gap-2 xl:mb-1">
                <st.icon className={cn("size-4 shrink-0", st.accent ? "text-signal" : "text-muted-foreground")} aria-hidden />
                <span className="truncate text-sm font-medium">{st.name}</span>
              </span>
              <span className="order-last w-full truncate pl-6 text-xs text-subtle-foreground xl:order-none xl:block xl:pl-0">{st.does}</span>
              <span className="max-w-1/2 shrink-0 truncate font-mono text-xs tabular-nums xl:mt-2 xl:block xl:max-w-none">{st.value ?? "—"}</span>
            </button>
          </li>
        ))}
      </ol>
      <button type="button" onClick={() => onFocus("agent:l2-investigator")} aria-pressed={focus === "agent:l2-investigator"}
        className={cn("mt-3 flex w-full items-center gap-2 rounded-lg border border-dashed bg-surface/60 px-3 py-2 text-left text-xs text-subtle-foreground hover:border-border-strong", focus === "agent:l2-investigator" && "border-signal")}>
        <Clock3 className="size-3.5 shrink-0" aria-hidden />
        <span className="font-medium text-foreground">Scheduler</span>
        <span className="min-w-0 truncate">runs the scout every 2 min and audits the board · {tally("l2-investigator") ?? "—"}</span>
      </button>
    </div>
  );
}

function AgentInspector({ focus, tools, board, ai }: { focus: string; tools: ToolStats | null; board: Board | null; ai: AiSettings | null }) {
  let title = "", description = "", metrics: { label: string; value: string | number | undefined | null; attention?: boolean }[] = [];
  if (focus === "jev") {
    const calls = tools?.jev.reduce((n, j) => n + j.Calls, 0);
    const errors = tools?.jev.reduce((n, j) => n + j.Errors, 0);
    const avg = tools?.jev.length ? tools.jev.reduce((n, j) => n + (j.AvgMs ?? 0) * j.Calls, 0) / Math.max(1, calls ?? 0) : null;
    title = "Jev · decision plane";
    description = "Fast typed judgments used for route, evidence relevance, next-step choice and review.";
    metrics = [{ label: "Decisions", value: calls?.toLocaleString("en-IN") }, { label: "Failures", value: errors, attention: !!errors }, { label: "Weighted average", value: fmtMs(avg) }, { label: "Decision kinds", value: tools?.jev.length }];
  } else if (focus === "l1") {
    title = "L1 assistant";
    description = "Requester-facing assistant configuration currently loaded by the Helpdesk.";
    metrics = [{ label: "Provider", value: ai ? human(ai.provider) : undefined }, { label: "Model", value: ai?.model }, { label: "Mode", value: ai?.kind ? human(ai.kind) : undefined }];
  } else if (focus.startsWith("model:")) {
    const model = focus.slice(6);
    const m = tools?.models.find((x) => x.Model === model);
    title = `Writer · ${model}`;
    description = "Reasoning/writer calls recorded by the observer trace.";
    metrics = [{ label: "Calls", value: m?.Calls }, { label: "Average latency", value: fmtMs(m?.AvgMs) }, { label: "Provider", value: m?.Provider }, { label: "Last used", value: m ? ago(m.LastUsed) : undefined }];
  } else {
    const id = focus.startsWith("agent:") ? focus.slice(6) : "";
    const counts = board?.stats?.by_assignee[id] ?? {};
    title = AGENT[id]?.name ?? id;
    description = AGENT[id]?.role ?? "Hermes worker profile";
    metrics = [{ label: "Profile", value: id || "—" }, { label: "Tasks on board", value: board?.stats ? Object.values(counts).reduce((a, n) => a + n, 0) : undefined },
      ...Object.entries(counts).slice(0, 4).map(([status, count]) => ({ label: human(status), value: count, attention: status === "blocked" && count > 0 }))];
  }
  return (
    <section className="mt-4 border-t pt-4" aria-live="polite" aria-label={`Selected: ${title}`}>
      <h3 className="text-sm font-semibold">{title}</h3>
      <p className="mt-0.5 text-meta text-muted-foreground">{description}</p>
      <dl className="mt-3 grid grid-cols-2 gap-2 md:grid-cols-4">
        {metrics.map((m) => (
          <div key={m.label} className="min-w-0 rounded-lg bg-surface-2 px-3 py-2.5">
            <dt className="truncate text-2xs text-subtle-foreground">{m.label}</dt>
            <dd className={cn("mt-0.5 truncate text-sm font-semibold tabular-nums", m.attention && "text-destructive")}>{m.value ?? "—"}</dd>
          </div>
        ))}
      </dl>
    </section>
  );
}

// Agent -> tools. Every line is live: width is share of calls, dots travel at the tool's average latency,
// and the red share of dots is its failure rate.
function ToolGraph({ tools, className }: { tools: ToolStats | null; className?: string }) {
  const [metric, setMetric] = useState<"calls" | "latency" | "errors">("calls");
  const [all, setAll] = useState(false);
  const reduced = useReducedMotion();
  const list = tools?.tools ?? [];
  const calls = list.reduce((n, t) => n + t.Calls, 0);
  const errors = list.reduce((n, t) => n + t.Errors, 0);
  const rate = (t: ToolStats["tools"][number]) => t.Errors / Math.max(1, t.Calls);
  const sorted = [...list].sort((a, b) => metric === "calls" ? b.Calls - a.Calls : metric === "latency" ? (b.AvgMs ?? 0) - (a.AvgMs ?? 0) : rate(b) - rate(a) || b.Calls - a.Calls);
  const busiest = [...list].sort((a, b) => b.Calls - a.Calls)[0];
  const worst = [...list].sort((a, b) => rate(b) - rate(a) || b.Calls - a.Calls)[0];
  const slowest = [...list].sort((a, b) => (b.AvgMs ?? 0) - (a.AvgMs ?? 0))[0];
  const label = (name: string) => describeEvent({ EventType: "post_tool_call", ToolName: name, Model: null }).title.toLowerCase();
  const rows: FanRow[] = (all ? sorted : sorted.slice(0, 6)).map((t) => {
    const r = rate(t);
    return {
      id: t.ToolName, label: label(t.ToolName), sub: `${t.Calls.toLocaleString("en-IN")} calls · avg ${fmtMs(t.AvgMs)} · ${ago(t.LastUsed)}`,
      share: t.Calls / Math.max(1, calls), errRate: r, latencyMs: t.AvgMs, hot: t.ToolName === busiest?.ToolName,
      chip: metric === "calls" ? `${((t.Calls / Math.max(1, calls)) * 100).toFixed(0)}% of calls` : metric === "latency" ? `max ${fmtMs(t.MaxMs)}` : `${(r * 100).toFixed(1)}% failed`,
      chipTone: metric === "errors" && r > 0.1 ? "danger" : metric === "calls" && t.ToolName === busiest?.ToolName ? "signal" : "muted",
    };
  });
  return (
    <Panel icon={Waypoints} title="Tool call graph" meta={tools ? `L2 engineer · ${calls.toLocaleString("en-IN")} calls recorded` : "Loading"} className={className}
      actions={<Segmented label="Order tools by" value={metric} onChange={setMetric} options={[{ id: "calls", label: "Calls" }, { id: "latency", label: "Latency" }, { id: "errors", label: "Errors" }]} />}>
      {!tools ? <Skeleton className="h-96" /> : !rows.length ? <p className="py-10 text-center text-sm text-muted-foreground">No tool calls recorded yet.</p> : (
        <div className="space-y-4">
          <FanOut source="L2 engineer" sub={`${list.length} tools`} rows={rows} reduced={reduced} />
          <div className="flex flex-wrap items-center justify-between gap-3">
            <Legend inline rows={[
              { label: "line width = share of calls", tone: "faint" },
              { label: "dot speed = average latency", tone: "signal" },
              { label: "red dots = failed share", tone: "danger" },
            ]} />
            {list.length > 6 && <Button size="sm" variant="ghost" onClick={() => setAll((v) => !v)}>{all ? "Show top 6" : `Show all ${list.length}`}</Button>}
          </div>
          <div className="grid grid-cols-2 gap-3 border-t pt-3 md:grid-cols-4">
            <Stat label="Failed" value={`${errors} of ${calls.toLocaleString("en-IN")} · ${((errors / Math.max(1, calls)) * 100).toFixed(1)}%`} tone={errors ? "danger" : undefined} />
            <Stat label="Busiest" value={busiest ? label(busiest.ToolName) : "—"} tone="signal" />
            <Stat label="Most failures" value={worst && worst.Errors ? `${label(worst.ToolName)} · ${(rate(worst) * 100).toFixed(0)}%` : "none"} tone={worst?.Errors ? "danger" : undefined} />
            <Stat label="Slowest" value={slowest ? `${label(slowest.ToolName)} · ${fmtMs(slowest.AvgMs)}` : "—"} />
          </div>
        </div>
      )}
    </Panel>
  );
}

function JevBars({ tools }: { tools: ToolStats }) {
  const rows = [...tools.jev].sort((x, y) => y.Calls - x.Calls);
  const max = Math.max(1, ...rows.map((r) => r.Calls));
  return (
    <ul className="space-y-2.5">
      {rows.map((j) => (
        <li key={j.Stage} className="text-xs">
          <p className="mb-1 flex items-baseline gap-2">
            <span className="min-w-0 flex-1 truncate">{describeEvent({ EventType: "jev_system_one", ToolName: j.Stage, Model: null }).title}</span>
            <span className="shrink-0 font-mono tabular-nums text-foreground">{j.Calls}</span>
            <span className="w-14 shrink-0 text-right font-mono tabular-nums text-subtle-foreground">{fmtMs(j.AvgMs)}</span>
          </p>
          <VolumeBar share={j.Calls / max} label={`${j.Stage}: ${j.Calls} decisions, ${j.Errors} failed`}
            segments={[{ label: "failed", value: j.Errors, tone: "danger" }, { label: "ok", value: j.Calls - j.Errors, tone: "signal" }]} />
        </li>
      ))}
    </ul>
  );
}

function Permissions({ tools, className }: { tools: ToolStats | null; className?: string }) {
  const catalog = tools?.catalog ?? [];
  return (
    <Panel icon={ShieldCheck} title="What agents may do" meta={tools ? `${catalog.length} actions · autonomous, needs approval, or prohibited` : "Loading"} className={className}>
      {!tools ? <Skeleton className="h-40" /> : (
        <div className="grid gap-4 md:grid-cols-3">
          {LEVELS.map((lvl) => {
            const items = catalog.filter((c) => c.PermissionLevel === lvl.id);
            return (
              <section key={lvl.id} className="min-w-0">
                <Legend rows={[{ label: <><span className="text-foreground">{lvl.label}</span> · {lvl.note}</>, value: items.length, tone: lvl.tone }]} />
                <ul className="mt-2 divide-y rounded-lg border">
                  {items.map((c) => (
                    <li key={c.ActionName} className="px-3 py-2.5">
                      <p className="text-meta font-medium">{c.ActionCategory}</p>
                      <p className="truncate font-mono text-2xs text-subtle-foreground" title={c.ActionName}>{c.ActionName}</p>
                      {c.Description && <p className="mt-1 text-xs text-muted-foreground">{c.Description}</p>}
                    </li>
                  ))}
                  {!items.length && <li className="px-3 py-2.5 text-xs text-subtle-foreground">None</li>}
                </ul>
              </section>
            );
          })}
        </div>
      )}
    </Panel>
  );
}

function AuditedReads({ tools, onOpenRun, className }: { tools: ToolStats | null; onOpenRun: (id: string) => void; className?: string }) {
  const rows = tools?.sql ?? [];
  const time = (a: ToolStats["sql"][number]) => (a.ErrorMessage ? "failed" : fmtMs(a.Ms));
  return (
    <Panel icon={Database} title="Recent audited reads" meta={tools ? `${rows.length} read-only XBatch queries, newest first` : "Loading"} className={className} pad="none">
      {!tools ? <Skeleton className="m-4 h-40" /> : !rows.length ? <p className="p-6 text-center text-sm text-muted-foreground">No audited reads yet.</p> : (
        <>
          {/* Phones: one card per read. */}
          <ul className="divide-y md:hidden">
            {rows.map((a) => (
              <li key={`${a.RunID}-${a.ActionNo}`} className="space-y-1 px-4 py-3">
                <p className="flex items-center gap-2 text-2xs text-subtle-foreground">
                  <span>{when(a.StartedOn)}</span>
                  {a.RunID && <button className="font-mono text-foreground underline-offset-4 hover:underline" onClick={() => onOpenRun(a.RunID!)}>{ticketLabel(a.TicketNo)}</button>}
                  <span className={cn("ml-auto font-mono tabular-nums", a.ErrorMessage ? "text-destructive" : "text-muted-foreground")}>{time(a)} · {a.RowsAffected ?? "—"} rows</span>
                </p>
                <p className="break-all font-mono text-xs">{a.ObjectName ?? a.OperationName}</p>
                {a.Purpose && <p className="text-xs text-muted-foreground">{a.Purpose}</p>}
              </li>
            ))}
          </ul>
          {/* Tablets and up: a table. */}
          <div className="scrollbar-thin hidden max-h-112 overflow-auto rounded-xl md:block">
            <table className="w-full text-meta">
              <thead className="sticky top-0 z-10 bg-surface text-left text-xs text-subtle-foreground">
                <tr className="border-b">{["When", "Ticket", "Object", "Purpose", "Rows", "Time"].map((h) => <th key={h} className="px-4 py-2 font-medium">{h}</th>)}</tr>
              </thead>
              <tbody className="divide-y">
                {rows.map((a) => (
                  <tr key={`${a.RunID}-${a.ActionNo}`} className="hover:bg-surface-2">
                    <td className="whitespace-nowrap px-4 py-2 text-2xs text-subtle-foreground">{when(a.StartedOn)}</td>
                    <td className="px-4 py-2">{a.RunID ? <button className="font-mono text-xs underline-offset-4 hover:underline" onClick={() => onOpenRun(a.RunID!)}>{ticketLabel(a.TicketNo)}</button> : "—"}</td>
                    <td className="max-w-56 truncate px-4 py-2 font-mono text-xs" title={a.ObjectName ?? a.OperationName ?? ""}>{a.ObjectName ?? a.OperationName}</td>
                    <td className="max-w-md truncate px-4 py-2 text-muted-foreground" title={a.Purpose ?? ""}>{a.Purpose}</td>
                    <td className="px-4 py-2 text-right font-mono tabular-nums">{a.RowsAffected ?? "—"}</td>
                    <td className={cn("whitespace-nowrap px-4 py-2 text-right font-mono tabular-nums", a.ErrorMessage && "text-destructive")}>{time(a)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </>
      )}
    </Panel>
  );
}
