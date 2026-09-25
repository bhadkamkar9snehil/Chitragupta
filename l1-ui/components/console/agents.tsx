"use client";

import { useEffect, useState } from "react";
import { ArrowRight, Bot, Clock3, Cpu, Database, MessageSquare, ShieldCheck, Sparkles, Waypoints, Wrench } from "lucide-react";
import { toast } from "sonner";
import { api, ops, type AiSettings, type Board, type ToolStats } from "@/lib/api";
import { ago, describeEvent, human, ticketLabel, when } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Skeleton, Tag } from "@/components/ui/primitives";
import { IconTile, Legend, Panel, Segmented, Stat, ms as fmtMs } from "@/components/ui/viz";
import { AGENT } from "./board";

const ms = (v?: number | null) => (v == null ? "—" : v < 1000 ? `${Math.round(v)}ms` : `${(v / 1000).toFixed(1)}s`);
const PERMISSION: Record<string, string> = { Autonomous: "bg-success-soft text-success", RequiresApproval: "bg-warning-soft text-warning", Prohibited: "bg-destructive-soft text-destructive" };

export function AgentsView({ onOpenRun }: { onOpenRun: (id: string) => void }) {
  const [tools, setTools] = useState<ToolStats | null>(null);
  const [board, setBoard] = useState<Board | null>(null);
  const [ai, setAi] = useState<AiSettings | null>(null);
  const [focus, setFocus] = useState("jev");

  useEffect(() => {
    ops.tools().then(setTools).catch((e: Error) => toast.error(e.message));
    ops.board().then(setBoard).catch(() => {});
    api.admin.settings().then((s) => setAi(s.ai)).catch(() => {});
  }, []);

  return (
    <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
      <div className="mx-auto max-w-7xl space-y-6 px-4 py-6 lg:px-8">
        <header className="flex items-center gap-3">
          <IconTile icon={Wrench} />
          <div>
            <h1 className="text-title font-semibold tracking-tight">Agents &amp; tools</h1>
          </div>
        </header>

        <div className="space-y-4">
          <Panel icon={Waypoints} title="Who does the work" meta="how a problem moves between them · select one">
            <AgentFlow focus={focus} onFocus={setFocus} tools={tools} board={board} ai={ai} />
          </Panel>
          <AgentInspector focus={focus} tools={tools} board={board} ai={ai} />
        </div>

        <div className="grid gap-4 xl:grid-cols-3">
          <ToolGraph tools={tools} className="xl:col-span-2" />
          <Panel icon={Sparkles} title="Jev decisions" meta={tools ? `${tools.jev.reduce((n, j) => n + j.Calls, 0)} typed judgments by kind` : "loading"}>
            {!tools ? <Skeleton className="h-60" /> : (
              <Legend rows={[...tools.jev].sort((x, y) => y.Calls - x.Calls).map((j) => ({
                label: describeEvent({ EventType: "jev_system_one", ToolName: j.Stage, Model: null }).title.toLowerCase(),
                value: j.Errors ? `${j.Calls} · ${j.Errors} failed` : j.Calls,
                tone: j.Errors ? "danger" as const : "signal" as const,
              }))} />
            )}
          </Panel>
        </div>

        <Panel icon={ShieldCheck} title="What agents may do" meta="every action is autonomous, needs approval, or is prohibited" pad="none">
          <ul className="divide-y">
            {tools?.catalog.map((c) => (
              <li key={c.ActionName} className="flex flex-wrap items-center gap-3 px-4 py-2.5 text-meta">
                <span className={cn("rounded px-1.5 py-0.5 text-2xs font-semibold", PERMISSION[c.PermissionLevel] ?? "bg-surface-3")}>{human(c.PermissionLevel.replace(/([a-z])([A-Z])/g, "$1 $2"))}</span>
                <span className="font-medium">{c.ActionCategory}</span>
                <span className="min-w-0 flex-1 truncate font-mono text-xs text-muted-foreground">{c.ActionName}</span>
              </li>
            ))}
          </ul>
        </Panel>

        <Panel icon={Database} title="Recent audited reads" meta="read-only XBatch queries the engineer ran, newest first" pad="none">
          <div className="scrollbar-thin max-h-96 overflow-auto rounded-xl">
            <table className="w-full min-w-160 text-meta">
              <thead className="sticky top-0 z-10 bg-surface text-left text-2xs uppercase tracking-wider text-subtle-foreground">
                <tr>{["When", "Ticket", "Object", "Purpose", "Rows", "Time"].map((h) => <th key={h} className="px-4 py-2 font-semibold">{h}</th>)}</tr>
              </thead>
              <tbody className="divide-y">
                {tools?.sql.map((a) => (
                  <tr key={`${a.RunID}-${a.ActionNo}`}>
                    <td className="whitespace-nowrap px-4 py-2 text-2xs text-subtle-foreground">{when(a.StartedOn)}</td>
                    <td className="px-4 py-2">{a.RunID ? <button className="font-mono text-xs hover:underline" onClick={() => onOpenRun(a.RunID!)}>{ticketLabel(a.TicketNo)}</button> : "—"}</td>
                    <td className="px-4 py-2 font-mono text-xs">{a.ObjectName ?? a.OperationName}</td>
                    <td className="max-w-xs truncate px-4 py-2 text-muted-foreground">{a.Purpose}</td>
                    <td className="px-4 py-2 tabular-nums">{a.RowsAffected ?? "—"}</td>
                    <td className={cn("px-4 py-2 tabular-nums", a.ErrorMessage && "text-destructive")}>{a.ErrorMessage ? "failed" : ms(a.Ms)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </Panel>
      </div>
    </div>
  );
}

// The workers as the path a problem takes: chat -> judgment -> investigation -> (writing) -> review.
function AgentFlow({ focus, onFocus, tools, board, ai }: { focus: string; onFocus: (f: string) => void; tools: ToolStats | null; board: Board | null; ai: AiSettings | null }) {
  const counts = (id: string) => board?.stats?.by_assignee[id] ?? {};
  const tally = (id: string) => (board?.stats ? Object.entries(counts(id)).map(([st, n]) => `${n} ${st}`).join(" · ") || "idle" : undefined);
  const model = tools?.models[0];
  const steps: { id: string; icon: typeof Bot; name: string; does: string; value?: string; optional?: boolean; accent?: boolean }[] = [
    { id: "l1", icon: MessageSquare, name: "L1 assistant", does: "answers or raises a ticket", value: ai?.model },
    { id: "jev", icon: Sparkles, name: "Jev", does: "decides every step", value: tools ? `${tools.jev.reduce((a, j) => a + j.Calls, 0)} decisions` : undefined, accent: true },
    { id: "agent:l2-jev-investigator", icon: Bot, name: "Investigator", does: "reads XBatch, proposes", value: tally("l2-jev-investigator") },
    ...(model ? [{ id: `model:${model.Model}`, icon: Cpu, name: "Writer", does: "only if reasoning is needed", value: `${model.Calls} calls`, optional: true }] : []),
    { id: "agent:l2-reviewer-primary", icon: ShieldCheck, name: "Reviewer", does: "checks before publishing", value: tally("l2-reviewer-primary") },
  ];
  return (
    <div className="dot-grid rounded-lg p-3">
      <ol className="flex flex-col items-stretch gap-2 sm:flex-row sm:flex-wrap sm:items-center">
        {steps.map((st, i) => (
          <li key={st.id} className="flex items-center gap-2 sm:flex-1">
            {i > 0 && <ArrowRight className={cn("hidden size-4 shrink-0 sm:block", st.optional ? "text-subtle-foreground" : "text-signal")} aria-hidden />}
            <button
              type="button"
              onClick={() => onFocus(st.id)}
              aria-pressed={focus === st.id}
              className={cn(
                "w-full min-w-32 rounded-xl border bg-surface p-3 text-left hover:border-border-strong",
                st.optional && "border-dashed",
                focus === st.id && "border-signal",
              )}
            >
              <span className="flex items-center gap-2">
                <st.icon className={cn("size-4 shrink-0", st.accent ? "text-signal" : "text-muted-foreground")} aria-hidden />
                <span className="truncate text-sm font-medium">{st.name}</span>
              </span>
              <span className="mt-1 block truncate text-xs text-subtle-foreground">{st.does}</span>
              <span className="mt-2 block truncate font-mono text-xs tabular-nums">{st.value ?? "—"}</span>
            </button>
          </li>
        ))}
      </ol>
      <button
        type="button"
        onClick={() => onFocus("agent:l2-investigator")}
        aria-pressed={focus === "agent:l2-investigator"}
        className={cn("mt-2 flex w-full items-center gap-2 rounded-lg border border-dashed px-3 py-2 text-left text-xs text-subtle-foreground hover:border-border-strong", focus === "agent:l2-investigator" && "border-signal")}
      >
        <Clock3 className="size-3.5 shrink-0" aria-hidden />
        <span className="font-medium text-foreground">Scheduler</span>
        <span className="truncate">runs the scout every 2 min and audits the board · {tally("l2-investigator") ?? "—"}</span>
      </button>
    </div>
  );
}

function AgentInspector({ focus, tools, board, ai }: { focus: string; tools: ToolStats | null; board: Board | null; ai: AiSettings | null }) {
  if (focus === "jev") {
    const calls = tools?.jev.reduce((n, j) => n + j.Calls, 0);
    const errors = tools?.jev.reduce((n, j) => n + j.Errors, 0);
    const avg = tools?.jev.length ? tools.jev.reduce((n, j) => n + (j.AvgMs ?? 0) * j.Calls, 0) / Math.max(1, calls ?? 0) : null;
    return <Inspector title="Jev · decision plane" description="Fast typed judgments used for route, evidence relevance, next-step choice and review.">
      <Metric label="Decisions" value={calls} /><Metric label="Failures" value={errors} attention={!!errors} /><Metric label="Weighted avg" value={ms(avg)} />
      <Metric label="Decision kinds" value={tools?.jev.length} />
    </Inspector>;
  }

  if (focus === "l1") {
    return <Inspector title="L1 assistant" description="Requester-facing assistant configuration currently loaded by the Helpdesk.">
      <Metric label="Provider" value={ai ? human(ai.provider) : undefined} /><Metric label="Model" value={ai?.model} />
      <Metric label="Mode" value={ai?.kind ? human(ai.kind) : undefined} />
    </Inspector>;
  }

  if (focus.startsWith("model:")) {
    const model = focus.slice(6);
    const m = tools?.models.find((x) => x.Model === model);
    return <Inspector title={`Writer · ${model}`} description="Reasoning/writer calls recorded by the observer trace.">
      <Metric label="Calls" value={m?.Calls} /><Metric label="Average latency" value={ms(m?.AvgMs)} />
      <Metric label="Provider" value={m?.Provider} /><Metric label="Last used" value={m ? ago(m.LastUsed) : undefined} />
    </Inspector>;
  }

  const id = focus.startsWith("agent:") ? focus.slice(6) : "";
  const agent = AGENT[id];
  const counts = board?.stats?.by_assignee[id] ?? {};
  const total = Object.values(counts).reduce((a, n) => a + n, 0);
  return <Inspector title={agent?.name ?? id} description={agent?.role ?? "Hermes worker profile"}>
    <Metric label="Profile" value={id || "—"} /><Metric label="Tasks on board" value={board?.stats ? total : undefined} />
    {Object.entries(counts).slice(0, 4).map(([status, count]) => <Metric key={status} label={human(status)} value={count} attention={status === "blocked" && count > 0} />)}
  </Inspector>;
}

function Inspector({ title, description, children }: { title: string; description: string; children: React.ReactNode }) {
  return (
    <section className="rounded-xl border bg-surface p-4" aria-live="polite">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div><h2 className="text-sm font-semibold">{title}</h2><p className="mt-1 text-meta text-muted-foreground">{description}</p></div>
        <span className="text-2xs font-semibold uppercase tracking-wider text-subtle-foreground">Selected agent</span>
      </div>
      <dl className="mt-4 grid grid-cols-2 gap-3 lg:grid-cols-4">{children}</dl>
    </section>
  );
}

function Metric({ label, value, attention }: { label: string; value: string | number | undefined | null; attention?: boolean }) {
  return (
    <div className="rounded-lg bg-surface-2 px-3 py-2.5">
      <dt className="text-2xs text-subtle-foreground">{label}</dt>
      <dd className={cn("mt-0.5 text-sm font-semibold tabular-nums", attention && "text-destructive")}>{value ?? "—"}</dd>
    </div>
  );
}

// Agent -> tools, one curve per tool. The tool with the worst error rate is the hot path.
function ToolGraph({ tools, className }: { tools: ToolStats | null; className?: string }) {
  const [metric, setMetric] = useState<"calls" | "latency" | "errors">("calls");
  const rows = [...(tools?.tools ?? [])]
    .sort((a, b) => metric === "calls" ? b.Calls - a.Calls : metric === "latency" ? (b.AvgMs ?? 0) - (a.AvgMs ?? 0) : b.Errors / Math.max(1, b.Calls) - a.Errors / Math.max(1, a.Calls))
    .slice(0, 6);
  const calls = (tools?.tools ?? []).reduce((n, t) => n + t.Calls, 0);
  const errors = (tools?.tools ?? []).reduce((n, t) => n + t.Errors, 0);
  const hot = [...rows].sort((a, b) => b.Errors / Math.max(1, b.Calls) - a.Errors / Math.max(1, a.Calls))[0];
  const hotName = hot && hot.Errors > 0 ? hot.ToolName : null;
  const H = Math.max(1, rows.length) * 72;
  const label = (name: string) => describeEvent({ EventType: "post_tool_call", ToolName: name, Model: null }).title.toLowerCase();
  return (
    <Panel icon={Waypoints} title="Tool call graph" meta={tools ? `L2 engineer · ${calls.toLocaleString("en-IN")} calls recorded` : "loading"} className={className}
      actions={<Segmented label="Measure" value={metric} onChange={setMetric} options={[{ id: "calls", label: "Calls" }, { id: "latency", label: "Latency" }, { id: "errors", label: "Errors" }]} />}>
      {!tools ? <Skeleton className="h-80" /> : !rows.length ? <p className="py-10 text-center text-sm text-muted-foreground">No tool calls recorded yet.</p> : (
        <div className="space-y-5">
          <div className="dot-grid flex flex-col items-stretch gap-3 rounded-lg p-3 sm:flex-row sm:items-center sm:gap-0">
            <div className="shrink-0 rounded-xl border border-signal bg-surface px-3 py-2.5 sm:w-44">
              <p className="font-mono text-sm">L2 engineer</p>
              <p className="font-mono text-xs text-subtle-foreground">{tools.tools.length} tools</p>
            </div>
            <svg viewBox={`0 0 100 ${H}`} preserveAspectRatio="none" className="hidden h-full min-h-40 w-24 shrink-0 self-stretch sm:block" aria-hidden>
              {rows.map((t, i) => {
                const y = i * 72 + 36;
                const isHot = t.ToolName === hotName;
                return <path key={t.ToolName} d={`M0 ${H / 2} C 50 ${H / 2}, 50 ${y}, 100 ${y}`} fill="none" vectorEffect="non-scaling-stroke" strokeWidth={isHot ? 2 : 1.25} strokeDasharray={isHot ? "5 4" : undefined} className={isHot ? "stroke-signal motion-safe:animate-flow" : "stroke-border-strong"} />;
              })}
            </svg>
            <ol className="min-w-0 flex-1 space-y-2">
              {rows.map((t) => {
                const isHot = t.ToolName === hotName;
                const rate = t.Errors / Math.max(1, t.Calls);
                return (
                  <li key={t.ToolName} className={cn("flex h-16 items-center gap-3 rounded-xl border bg-surface px-3", isHot && "border-signal")}>
                    <span className={cn("size-2 shrink-0 rounded-full", isHot ? "bg-signal" : "bg-subtle-foreground")} aria-hidden />
                    <span className="min-w-0 flex-1">
                      <span className="block truncate font-mono text-sm">{label(t.ToolName)}</span>
                      <span className="block truncate font-mono text-xs text-subtle-foreground">{t.Calls.toLocaleString("en-IN")} · avg {fmtMs(t.AvgMs)} · {ago(t.LastUsed)}</span>
                    </span>
                    <span className={cn("shrink-0 rounded-md px-2 py-1 font-mono text-xs", isHot ? "bg-signal-soft text-signal" : "bg-surface-2 text-subtle-foreground")}>
                      {metric === "latency" ? fmtMs(t.MaxMs) + " max" : `${(rate * 100).toFixed(1)}% err`}
                    </span>
                  </li>
                );
              })}
            </ol>
          </div>
          <div className="grid grid-cols-2 gap-4 sm:grid-cols-4">
            <Stat label="Calls" value={calls.toLocaleString("en-IN")} />
            <Stat label="Failed" value={errors} tone={errors ? "danger" : undefined} />
            <Stat label="Error rate" value={`${((errors / Math.max(1, calls)) * 100).toFixed(1)}%`} />
            <Stat label="Hot path" value={hotName ? label(hotName) : "none"} tone={hotName ? "signal" : undefined} />
          </div>
        </div>
      )}
    </Panel>
  );
}
