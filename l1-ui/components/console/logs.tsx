"use client";

import { Fragment, useCallback, useEffect, useMemo, useState } from "react";
import { ChevronRight, CirclePause, FileJson2, ListTree, Radio, RefreshCw, Rows3, Search, Timer } from "lucide-react";
import { toast } from "sonner";
import { ops, type RuntimeLogs } from "@/lib/api";
import { describeEvent, ticketLabel } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Empty, Skeleton, Switch } from "@/components/ui/primitives";
import { Legend, PageTitle, Panel, Segmented, Stat, Waterfall, ms as fmtMs, type Span, type VizTone } from "@/components/ui/viz";
import { Swimlanes, type LaneMark } from "@/components/ui/charts";
import { Json } from "./live";
import { AGENT } from "./board";

// Runtime logs, readable: the observer JSONL becomes one row per tool call / model request / health check,
// grouped by investigation run and drawn as a timeline; the scheduler's function trace becomes a waterfall.

type D = Record<string, unknown>;
type Kind = "tool" | "model" | "check" | "walk" | "context";
type Status = "ok" | "failed" | "blocked" | "running" | "info";
type Ev = {
  key: string; kind: Kind; start: number; end: number; atText: string; actor: string; profile: string | null; run: string | null;
  title: string; detail: string; status: Status; ms: number | null; records: D[];
};

const str = (v: unknown) => (v == null ? "" : typeof v === "string" ? v : JSON.stringify(v));
const clockText = (ts: string) => ts.match(/T(\d\d:\d\d:\d\d)/)?.[1] ?? ts;
const parseJson = (v: unknown): D | null => { if (v && typeof v === "object") return v as D; try { return JSON.parse(String(v)) as D; } catch { return null; } };
const actorOf = (p: unknown) => (p ? AGENT[String(p)]?.name ?? String(p) : "System");
const toolTitle = (name: string) => describeEvent({ EventType: "post_tool_call", ToolName: name, Model: null }).title;
const short = (v: unknown, n = 48) => { const s = str(v); return s.length > n ? `${s.slice(0, n)}…` : s; };

const KINDS: { id: "all" | Kind | "failed"; label: string }[] = [
  { id: "all", label: "All" }, { id: "tool", label: "Tool calls" }, { id: "model", label: "Model requests" },
  { id: "failed", label: "Problems" }, { id: "check", label: "Health checks" },
];
const STATUS_TONE: Record<Status, VizTone> = { ok: "signal", failed: "danger", blocked: "warn", running: "mid", info: "faint" };
const STATUS_TEXT: Record<Status, string> = { ok: "OK", failed: "Failed", blocked: "Blocked", running: "Running", info: "—" };

function toEvents(records: D[]): Ev[] {
  const out: Ev[] = [];
  const pending = new Map<string, Ev>();
  const sorted = [...records].sort((a, b) => str(a.event_on_ist).localeCompare(str(b.event_on_ist)));
  sorted.forEach((d, i) => {
    const atText = str(d.event_on_ist);
    const at = Date.parse(atText) || 0;
    const base = { key: str(d.trace_event_id) || `e${i}`, atText, actor: actorOf(d.profile_name), profile: d.profile_name ? str(d.profile_name) : null, run: d.run_id ? str(d.run_id).toUpperCase() : null, records: [d] };
    const type = str(d.event_type);
    if (type === "pre_tool_call") {
      const ev: Ev = { ...base, kind: "tool", start: at, end: at, title: toolTitle(str(d.tool_name)), detail: argsText(d.args), status: "running", ms: null };
      if (d.tool_call_id) pending.set(str(d.tool_call_id), ev);
      out.push(ev);
      return;
    }
    if (type === "post_tool_call") {
      const ev = d.tool_call_id ? pending.get(str(d.tool_call_id)) ?? null : null;
      const res = parseJson(d.result);
      const status: Status = d.status === "ok" && res?.ok !== false ? "ok" : d.status === "blocked" ? "blocked" : "failed";
      const error = str(d.error_message) || str(res?.error);
      const ms = d.duration_ms != null ? Number(d.duration_ms) : null;
      if (ev) {
        Object.assign(ev, { end: at, status, ms: ms ?? at - ev.start, detail: status === "ok" ? ev.detail : error || ev.detail });
        ev.records.push(d);
        pending.delete(str(d.tool_call_id));
      } else {
        out.push({ ...base, kind: "tool", start: at - (ms ?? 0), end: at, title: toolTitle(str(d.tool_name)), detail: status === "ok" ? "" : error, status, ms });
      }
      return;
    }
    if (type === "post_api_request") {
      const ms = Number(d.api_duration_ms ?? 0);
      const u = (d.usage ?? {}) as D;
      out.push({
        ...base, kind: "model", start: at - ms, end: at, title: `Model request · ${str(d.model).split("/").pop()}`, status: "ok", ms,
        detail: [`${(Number(u.input_tokens ?? u.prompt_tokens ?? 0) / 1000).toFixed(1)}k tokens in`, `${u.output_tokens ?? 0} out`, d.ttft_ms != null && `first token ${fmtMs(Number(d.ttft_ms))}`, d.finish_reason && `then ${str(d.finish_reason).replace(/_/g, " ")}`].filter(Boolean).join(" · "),
      });
      return;
    }
    const r = (d.result ?? {}) as D;
    if (type === "lmstudio_sample" || type === "compute_sample") {
      const model = type === "lmstudio_sample";
      out.push({
        ...base, kind: "check", start: at, end: at, ms: null, title: model ? "Model server check" : "Compute check",
        status: r.error ? (model ? "failed" : "blocked") : "ok",
        detail: r.error ? str(r.error) : model ? `${Math.round(Number(r.latency_s ?? 0) * 1000)} ms · ${(r.models as unknown[] | undefined)?.length ?? 0} models loaded` : `GPU ${str(r.gpu_util_pct ?? "—")}% · CPU ${str(r.cpu_util_pct ?? "—")}%`,
      });
      return;
    }
    if (type === "world_walk") {
      const ms = d.duration_ms != null ? Number(d.duration_ms) : null;
      out.push({ ...base, kind: "walk", start: at - (ms ?? 0), end: at, ms, title: "XBatch world walk", status: d.status === "ok" ? "ok" : "failed",
        detail: `route ${str(r.route)} · ${str(r.stopped).replace(/_/g, " ")} · ${(r.survey as unknown[] | undefined)?.length ?? 0} records surveyed` });
      return;
    }
    out.push({ ...base, kind: "context", start: at, end: at, ms: null, title: type === "trace_context" ? "Run context" : type.replace(/_/g, " "), status: "info", detail: str(d.status) });
  });
  return out;
}

function argsText(args: unknown) {
  const a = parseJson(args);
  if (!a) return "";
  return Object.entries(a).filter(([, v]) => v != null && v !== "").slice(0, 2).map(([k, v]) => `${k.replace(/_/g, " ")} ${short(v, 40)}`).join(" · ");
}

type Run = { id: string; ticket: string | null; start: number; end: number; events: number; failed: number; actors: string[] };

export function LogsView() {
  const [data, setData] = useState<RuntimeLogs | null>(null);
  const [view, setView] = useState<"agents" | "scheduler">("agents");
  const [follow, setFollow] = useState(true);
  const [pickedRun, setPickedRun] = useState<string | null>(null);
  const [kind, setKind] = useState<(typeof KINDS)[number]["id"]>("all");
  const [q, setQ] = useState("");
  const [open, setOpen] = useState<string | null>(null);
  const [tickets, setTickets] = useState<Record<string, string>>({});

  const load = useCallback(async () => {
    try { setData(await ops.logs(500)); }
    catch (e) { toast.error((e as Error).message); }
  }, []);

  useEffect(() => {
    const initial = setTimeout(load, 0);
    const runs = setTimeout(() => ops.runs().then((rs) => setTickets(Object.fromEntries(rs.map((r) => [r.ID.toUpperCase(), r.TicketNo ?? ""])))).catch(() => {}), 0);
    return () => { clearTimeout(initial); clearTimeout(runs); };
  }, [load]);
  useEffect(() => {
    if (!follow) return;
    const id = setInterval(load, 2500);
    return () => clearInterval(id);
  }, [follow, load]);

  const observer = data?.sources.find((s) => s.name === "Observer events");
  const trace = data?.sources.find((s) => s.name === "Call trace");
  const events = useMemo(() => toEvents((observer?.records ?? []).map((r) => r.data ?? {}).filter((d) => d.event_type)), [observer]);

  const runs: Run[] = useMemo(() => {
    const m = new Map<string, Run>();
    for (const e of events) {
      if (!e.run) continue;
      const r = m.get(e.run) ?? { id: e.run, ticket: null, start: e.start, end: e.end, events: 0, failed: 0, actors: [] };
      r.start = Math.min(r.start, e.start); r.end = Math.max(r.end, e.end); r.events++;
      if (e.status === "failed") r.failed++;
      if (!r.actors.includes(e.actor)) r.actors.push(e.actor);
      m.set(e.run, r);
    }
    return [...m.values()].sort((a, b) => b.end - a.end);
  }, [events]);

  // Follow the newest run until the operator picks one.
  const runId = pickedRun ?? runs[0]?.id ?? null;
  const run = runs.find((r) => r.id === runId) ?? null;
  const inRun = run ? events.filter((e) => e.run === run.id) : events;
  const latest = events.at(-1);
  const liveNow = !!latest && latest.end > 0 && data ? Date.parse(data.at) - latest.end < 120_000 : false;

  const shown = inRun
    .filter((e) => kind === "all" || (kind === "failed" ? e.status === "failed" || e.status === "blocked" : kind === "check" ? e.kind === "check" : e.kind === kind))
    .filter((e) => !q || `${e.title} ${e.detail} ${e.actor}`.toLowerCase().includes(q.toLowerCase()))
    .slice()
    .reverse()
    .slice(0, 300);

  const reveal = (key: string) => {
    setOpen(key);
    setKind("all");
    setQ("");
    requestAnimationFrame(() => document.getElementById(`ev-${key}`)?.scrollIntoView({ block: "center", behavior: "smooth" }));
  };

  return (
    <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
      <div className="space-y-3 px-4 py-3 lg:px-6">
        <div className="flex flex-wrap items-center gap-3">
          <PageTitle icon={FileJson2} className="flex-1" title="Runtime logs" meta={data ? `What the L2 workers did, from the observer log in WSL · ${observer?.records.length ?? 0} events tailed` : "Reading the logs in WSL"} />
          <label className="flex items-center gap-2 text-meta text-muted-foreground">
            <Switch checked={follow} onCheckedChange={setFollow} aria-label="Follow runtime logs" />
            {follow ? <><Radio className="size-3 text-signal" aria-hidden /> Follow live</> : <><CirclePause className="size-3" aria-hidden /> Paused</>}
          </label>
          <Button variant="outline" size="sm" onClick={load}><RefreshCw /> Refresh</Button>
        </div>

        <Segmented label="Log" value={view} onChange={setView} className="w-full sm:w-fit" options={[
          { id: "agents", label: <span className="inline-flex items-center gap-1.5"><Rows3 className="size-3.5" aria-hidden /> Agent activity</span> },
          { id: "scheduler" as const, label: <span className="inline-flex items-center gap-1.5"><ListTree className="size-3.5" aria-hidden /> Harness trace</span> },
        ]} />

        {!data ? <div className="space-y-3"><Skeleton className="h-40" /><Skeleton className="h-80" /></div> : view === "scheduler" ? (
          <SchedulerRun records={(trace?.records ?? []).map((r) => r.data ?? {})} available={!!trace?.available} />
        ) : !observer?.available ? (
          <Empty icon={<FileJson2 className="size-5" />} title="Observer log unavailable">The runtime could not read the observer JSONL inside WSL.</Empty>
        ) : (
          <>
            {runs.length > 0 && (
              <div className="flex flex-wrap gap-2" role="group" aria-label="Investigation runs">
                {runs.slice(0, 8).map((r) => {
                  const t = tickets[r.id];
                  return (
                    <button key={r.id} type="button" aria-pressed={r.id === runId} onClick={() => { setPickedRun(r.id); setOpen(null); }}
                      className={cn("rounded-xl border bg-canvas px-3 py-2 text-left hover:border-border-strong", r.id === runId && "border-signal bg-signal-soft/30")}>
                      <span className="flex items-center gap-2 text-xs">
                        <span className="font-mono font-medium">{t ? ticketLabel(t) : r.id.slice(0, 8)}</span>
                        {r.failed > 0 && <span className="rounded bg-destructive-soft px-1 font-mono text-2xs text-destructive">{r.failed} failed</span>}
                      </span>
                      <span className="mt-0.5 block font-mono text-2xs text-subtle-foreground">{clockOf(r.start)} · {fmtMs(r.end - r.start)} · {r.events} events</span>
                    </button>
                  );
                })}
              </div>
            )}

            <RunPanel run={run} ticket={run ? tickets[run.id] : undefined} events={inRun} live={liveNow && run?.id === runs[0]?.id} onPick={reveal} />

            <Panel icon={Rows3} title="Events" meta={`${shown.length} shown · newest first · select a row for details`} pad="none"
              actions={<label className="relative block w-full sm:w-56"><Search className="pointer-events-none absolute left-2.5 top-1/2 size-3.5 -translate-y-1/2 text-subtle-foreground" aria-hidden />
                <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="Filter events" aria-label="Filter events" className="h-9 w-full rounded-lg border bg-surface pl-8 pr-2 text-sm outline-none focus:border-signal focus:ring-2 focus:ring-ring" /></label>}>
              <div className="flex flex-wrap gap-1 border-b px-3 py-2" role="group" aria-label="Event type">
                {KINDS.map((k) => {
                  const n = k.id === "all" ? inRun.length : k.id === "failed" ? inRun.filter((e) => e.status === "failed" || e.status === "blocked").length : inRun.filter((e) => e.kind === k.id).length;
                  return (
                    <button key={k.id} aria-pressed={kind === k.id} onClick={() => setKind(k.id)}
                      className={cn("min-h-9 rounded-md px-2.5 text-meta text-muted-foreground hover:bg-surface-2 sm:min-h-7", kind === k.id && "bg-surface-3 font-medium text-foreground", k.id === "failed" && n > 0 && kind !== k.id && "text-destructive")}>
                      {k.label} <span className="font-mono text-2xs tabular-nums text-subtle-foreground">{n}</span>
                    </button>
                  );
                })}
              </div>
              {shown.length ? <EventTable events={shown} open={open} onToggle={(k) => setOpen(open === k ? null : k)} /> : <p className="p-8 text-center text-sm text-muted-foreground">No events match.</p>}
            </Panel>
          </>
        )}
      </div>
      <div className="sr-only" aria-live="polite">{follow ? "Following runtime logs" : "Runtime log following paused"}</div>
    </div>
  );
}

const clockOf = (t: number) => new Date(t).toLocaleTimeString("en-IN", { hour: "2-digit", minute: "2-digit", hour12: false, timeZone: "Asia/Kolkata" });

function RunPanel({ run, ticket, events, live, onPick }: { run: Run | null; ticket?: string; events: Ev[]; live: boolean; onPick: (key: string) => void }) {
  if (!events.length) return null;
  const t0 = Math.min(...events.map((e) => e.start)), t1 = Math.max(...events.map((e) => e.end));
  const pad = Math.max(500, (t1 - t0) * 0.02);
  // Workers in the order they acted; health checks without a profile go last.
  const actors = [...new Set(events.map((e) => e.actor))].sort((a, b) => Number(a === "System") - Number(b === "System"));
  const tools = events.filter((e) => e.kind === "tool");
  const models = events.filter((e) => e.kind === "model");
  const failed = tools.filter((e) => e.status === "failed").length;
  const slow = [...tools].sort((a, b) => (b.ms ?? 0) - (a.ms ?? 0))[0];
  const tokens = models.reduce((n, e) => n + Number(((e.records[0].usage ?? {}) as D).input_tokens ?? 0), 0);
  const marks: LaneMark[] = events.map((e) => ({
    key: e.key, lane: e.actor, track: e.kind === "model" ? 0 : e.kind === "tool" || e.kind === "walk" ? 1 : 2,
    start: e.start, end: e.kind === "model" || e.kind === "tool" || e.kind === "walk" ? Math.max(e.end, e.start + 1) : undefined,
    tone: e.kind === "model" ? "mid" : STATUS_TONE[e.status], onClick: () => onPick(e.key),
    tip: <>{clockText(e.atText)} · {e.actor}<br /><b>{e.title}</b>{e.ms != null ? ` · ${fmtMs(e.ms)}` : ""}{e.status === "failed" || e.status === "blocked" ? ` · ${STATUS_TEXT[e.status]}` : ""}{e.detail ? <><br /><span className="text-muted-foreground">{short(e.detail, 70)}</span></> : null}</>,
  }));
  return (
    <Panel icon={Timer} title={run ? `Run ${ticket ? ticketLabel(ticket) : run.id.slice(0, 8)}` : "Recent activity"}
      meta={run ? `${run.actors.filter((a) => a !== "System").join(" then ") || "System"} · ${clockOf(run.start)}–${clockOf(run.end)}` : "Events without a run"}
      actions={live ? <span className="flex items-center gap-1.5 rounded-md bg-signal-soft px-2 py-1 text-xs text-signal"><span className="size-1.5 rounded-full bg-signal motion-safe:animate-pulse" aria-hidden />Live</span> : undefined}>
      <div className="space-y-4">
        <div className="grid grid-cols-2 gap-3 md:grid-cols-5">
          <Stat label="Duration" value={fmtMs(t1 - t0)} />
          <Stat label="Model requests" value={`${models.length} · ${(tokens / 1000).toFixed(0)}k tokens`} />
          <Stat label="Tool calls" value={tools.length} />
          <Stat label="Failed tool calls" value={failed} tone={failed ? "danger" : undefined} />
          <Stat label="Slowest tool" value={slow ? `${slow.title} · ${fmtMs(slow.ms)}` : "—"} />
        </div>
        <Swimlanes label="Run timeline: model requests, tool calls and checks per worker" domain={[t0 - pad, t1 + pad]}
          lanes={actors.map((a) => ({ id: a, label: a, sub: `${events.filter((e) => e.actor === a).length} events` }))} tracks={["Model requests", "Tool calls", "Checks"]} marks={marks} />
        <Legend inline rows={[
          { label: "model request (top row)", tone: "mid" }, { label: "tool call ok", tone: "signal" }, { label: "tool call failed", tone: "danger" },
          { label: "blocked / monitoring gap", tone: "warn" }, { label: "check (bottom row)", tone: "faint" },
        ]} />
      </div>
    </Panel>
  );
}

function EventTable({ events, open, onToggle }: { events: Ev[]; open: string | null; onToggle: (key: string) => void }) {
  return (
    <div className="scrollbar-thin max-h-160 overflow-auto">
      <table className="w-full table-fixed text-meta">
        <thead className="sticky top-0 z-10 bg-surface text-left text-xs text-subtle-foreground">
          <tr className="border-b">
            <th className="w-24 px-3 py-2 font-medium sm:w-28">Time</th>
            <th className="hidden w-36 px-3 py-2 font-medium lg:table-cell">Worker</th>
            <th className="px-3 py-2 font-medium">Event</th>
            <th className="hidden px-3 py-2 font-medium md:table-cell">Detail</th>
            <th className="w-20 px-3 py-2 font-medium">Result</th>
            <th className="w-20 px-3 py-2 text-right font-medium">Took</th>
          </tr>
        </thead>
        <tbody>
          {events.map((e) => {
            const isOpen = open === e.key;
            const bad = e.status === "failed" || e.status === "blocked";
            return (
              <Fragment key={e.key}>
                <tr id={`ev-${e.key}`} onClick={() => onToggle(e.key)} className={cn("cursor-pointer border-b align-top hover:bg-surface-2", isOpen && "bg-surface-2", e.status === "failed" && "bg-destructive-soft/30")}>
                  <td className="px-3 py-2 font-mono text-xs tabular-nums text-subtle-foreground">
                    <button type="button" aria-expanded={isOpen} aria-label={`${isOpen ? "Hide" : "Show"} details for ${e.title}`} className="inline-flex items-center gap-1 outline-none focus-visible:ring-2 focus-visible:ring-ring">
                      <ChevronRight className={cn("size-3 shrink-0 transition-transform", isOpen && "rotate-90")} aria-hidden />{clockText(e.atText)}
                    </button>
                  </td>
                  <td className="hidden truncate px-3 py-2 text-xs text-muted-foreground lg:table-cell">{e.actor}</td>
                  <td className="px-3 py-2">
                    <span className="block truncate font-medium">{e.title}</span>
                    <span className="block truncate text-xs text-subtle-foreground md:hidden">{e.detail}</span>
                  </td>
                  <td className={cn("hidden truncate px-3 py-2 text-xs md:table-cell", bad ? "text-destructive" : "text-muted-foreground")} title={e.detail}>{e.detail}</td>
                  <td className="px-3 py-2">
                    <span className={cn("inline-flex items-center gap-1.5 text-xs", bad ? "text-destructive" : e.status === "running" ? "text-signal" : "text-muted-foreground")}>
                      <span className={cn("size-1.5 rounded-full", e.status === "ok" ? "bg-signal" : e.status === "failed" ? "bg-destructive" : e.status === "blocked" ? "bg-warning" : e.status === "running" ? "bg-signal motion-safe:animate-pulse" : "bg-border-strong")} aria-hidden />
                      {STATUS_TEXT[e.status]}
                    </span>
                  </td>
                  <td className={cn("px-3 py-2 text-right font-mono text-xs tabular-nums", (e.ms ?? 0) >= 10_000 ? "text-warning" : "text-subtle-foreground")}>{e.ms != null ? fmtMs(e.ms) : ""}</td>
                </tr>
                {isOpen && (
                  <tr className="border-b bg-surface-2/60">
                    <td colSpan={6} className="px-3 py-3"><EventDetail e={e} /></td>
                  </tr>
                )}
              </Fragment>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

function EventDetail({ e }: { e: Ev }) {
  const first = e.records[0], last = e.records.at(-1)!;
  const facts: [string, string][] = [["Worker", e.actor], ["When", e.atText.replace("T", " ").slice(0, 23)]];
  if (e.run) facts.push(["Run", e.run]);
  if (e.kind === "tool") {
    const args = parseJson(first.args);
    if (args) Object.entries(args).forEach(([k, v]) => facts.push([k.replace(/_/g, " "), short(v, 400)]));
    if (e.status !== "ok" && e.detail) facts.push(["Problem", e.detail]);
    if (e.ms != null) facts.push(["Took", fmtMs(e.ms)]);
  } else if (e.kind === "model") {
    const u = (first.usage ?? {}) as D;
    facts.push(["Model", `${str(first.model)} · ${str(first.provider)}`], ["Tokens", `${u.input_tokens ?? 0} in · ${u.output_tokens ?? 0} out`], ["First token", fmtMs(Number(first.ttft_ms ?? 0))], ["Total", fmtMs(e.ms)], ["Ended with", str(first.finish_reason).replace(/_/g, " ")], ["Tool calls asked", str(first.assistant_tool_call_count)]);
  } else if (e.detail) facts.push(["Summary", e.detail]);
  return (
    <div className="grid gap-3 lg:grid-cols-2">
      <dl className="min-w-0 space-y-1 text-xs">
        {facts.map(([k, v]) => (
          <div key={k} className="flex gap-3">
            <dt className="w-28 shrink-0 capitalize text-subtle-foreground">{k}</dt>
            <dd className={cn("min-w-0 flex-1 break-words font-mono", k === "Problem" && "text-destructive")}>{v || "—"}</dd>
          </div>
        ))}
      </dl>
      <details className="min-w-0 rounded-lg border bg-surface">
        <summary className="cursor-pointer px-3 py-2 text-xs font-medium">Raw record{e.records.length > 1 ? "s" : ""}</summary>
        <div className="space-y-3 border-t p-3">{(e.records.length > 1 ? [first, last] : [first]).map((r, i) => <Json key={i} label={i === 0 && e.records.length > 1 ? "Call" : e.records.length > 1 ? "Return" : "Record"} text={JSON.stringify(r)} />)}</div>
      </details>
    </div>
  );
}

// The harness's Python function trace (scout, tool bridge, …) for one process, as a waterfall of calls.
function SchedulerRun({ records, available }: { records: D[]; available: boolean }) {
  const byPid = new Map<string, D[]>();
  records.forEach((d) => { const k = str(d.pid); byPid.set(k, [...(byPid.get(k) ?? []), d]); });
  const pids = [...byPid.keys()];
  const [picked, setPicked] = useState<string | null>(null);
  const pid = picked && byPid.has(picked) ? picked : pids.at(-1) ?? null;
  const rows = pid ? byPid.get(pid)! : [];
  const t0 = rows.length ? Date.parse(str(rows[0].ts)) : 0;
  const spans: Span[] = [];
  const stack: { fn: string; depth: number; start: number; at: string; idx: number }[] = [];
  let exceptions = 0;
  rows.forEach((d) => {
    const t = Date.parse(str(d.ts)) - t0;
    if (d.event === "call") {
      stack.push({ fn: str(d.fn), depth: Number(d.depth ?? 1), start: t, at: str(d.at), idx: spans.length });
      spans.push({ id: `${spans.length}`, label: `${"· ".repeat(Math.max(0, Number(d.depth ?? 1) - 1))}${str(d.fn)}()`, sub: str(d.at), start: t, end: t, tone: "signal", right: "…" });
    } else if (d.event === "return") {
      const i = stack.map((s) => s.fn).lastIndexOf(str(d.fn));
      if (i >= 0) {
        const s = stack.splice(i, 1)[0];
        const ms = Number(d.ms ?? t - s.start);
        Object.assign(spans[s.idx], { end: s.start + ms, right: fmtMs(ms) });
      }
    } else if (d.event === "exception") {
      exceptions++;
      const s = stack.at(-1);
      if (s) Object.assign(spans[s.idx], { tone: "danger", right: str(d.error_type) || "error" });
    }
  });
  const total = Math.max(1, ...spans.map((s) => s.end));
  if (!available) return <Empty icon={<ListTree className="size-5" />} title="Harness trace unavailable">The call trace JSONL could not be read inside WSL.</Empty>;
  if (!rows.length) return <Empty icon={<ListTree className="size-5" />} title="No process traced">The harness has not written a call trace yet.</Empty>;
  return (
    <Panel icon={ListTree} title={str(rows[0].at).split(":")[0] || "Harness process"} meta={`Every function this harness process called · started ${clockText(str(rows[0].ts))} · process ${pid}`}
      actions={pids.length > 1 ? <Segmented label="Traced process" value={pid!} onChange={setPicked} options={pids.slice(-4).map((p) => ({ id: p, label: clockText(str(byPid.get(p)![0].ts)) }))} /> : undefined}>
      <div className="space-y-4">
        <div className="grid grid-cols-2 gap-3 md:grid-cols-4">
          <Stat label="Took" value={fmtMs(total)} />
          <Stat label="Function calls" value={spans.length} />
          <Stat label="Deepest nesting" value={Math.max(...rows.map((d) => Number(d.depth ?? 1)))} />
          <Stat label="Exceptions" value={exceptions} tone={exceptions ? "danger" : undefined} />
        </div>
        <div className="scrollbar-thin max-h-160 overflow-y-auto">
          <Waterfall spans={spans.slice(0, 150)} total={total} />
        </div>
        {spans.length > 150 && <p className="text-xs text-subtle-foreground">Showing the first 150 of {spans.length} calls.</p>}
      </div>
    </Panel>
  );
}
