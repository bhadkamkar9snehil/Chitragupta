"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import { Activity, ArrowRight, CalendarClock, Gauge, GitFork, Hourglass, Radio, Timer, Trophy } from "lucide-react";
import { ops, type AttentionTicket, type Overview } from "@/lib/api";
import { ago, clock, outcomeLabel, ticketLabel } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/primitives";
import { Headline, IconTile, Legend, OUTCOMES, Panel, Segmented, Stat, type VizTone } from "@/components/ui/viz";
import { DotLanes, FlowGraph, HourHeat, StackColumns, type Column, type FlowLink, type FlowNode } from "@/components/ui/charts";

type Go = {
  live: () => void;
  l1: () => void;
  runs: () => void;
  l3: () => void;
  tickets: () => void;
  ticket: (id: string) => void;
  run: (id: string) => void;
};


const pct = (n: number, d: number) => (d ? `${Math.round((n / d) * 100)}%` : "—");

export function OverviewView({ go }: { go: Go }) {
  const [data, setData] = useState<Overview | null>(null);
  const [error, setError] = useState<string | null>(null);
  // Day and hour axes are anchored to when this data arrived, not to each render.
  const [now, setNow] = useState(0);

  const refresh = useCallback(() => {
    ops.overview()
      .then((next) => {
        setData(next);
        setNow(Date.now());
        setError(null);
      })
      .catch((reason: Error) => setError(reason.message));
  }, []);

  useEffect(() => {
    refresh();
    const poll = setInterval(refresh, 15_000);
    return () => clearInterval(poll);
  }, [refresh]);

  if (!data && error)
    return (
      <div className="grid flex-1 place-items-center p-6">
        <section role="alert" className="max-w-sm text-center">
          <IconTile icon={Gauge} className="mx-auto" />
          <h2 className="mt-3 text-sm font-semibold">Could not load the command centre</h2>
          <p className="mt-1 text-meta text-muted-foreground">{error}</p>
          <Button size="sm" variant="outline" className="mt-4" onClick={refresh}>Try again</Button>
        </section>
      </div>
    );

  return (
    <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
      <div className="space-y-3 px-4 py-3 lg:px-6">
        <header className="flex flex-wrap items-center gap-3">
          <IconTile icon={Gauge} />
          <div className="min-w-0 flex-1">
            <h1 className="text-title font-semibold tracking-tight">Command centre</h1>
            <p className="text-xs text-subtle-foreground">L1 assistant, L2 engineer and L3 people · refreshes every 15 s</p>
          </div>
          {data && error && <p role="status" className="text-xs text-warning">Refresh failed · showing the last data</p>}
        </header>

        <div className="grid gap-3 xl:grid-cols-12">
          <FlowPanel data={data} now={now} go={go} className="xl:col-span-8" />
          <LivePanel data={data} now={now} go={go} className="xl:col-span-4" />
          <OpenPanel data={data} now={now} go={go} className="xl:col-span-7" />
          <OutcomesPanel data={data} now={now} go={go} className="xl:col-span-5" />
          <IntakePanel data={data} now={now} className="xl:col-span-6" />
          <DurationPanel data={data} now={now} go={go} className="xl:col-span-6" />
          <ActivityPanel data={data} now={now} go={go} className="xl:col-span-12" />
        </div>
      </div>
    </div>
  );
}

type PanelProps = { data: Overview | null; now: number; go: Go; className?: string };

// ---------- Support flow ----------

function FlowPanel({ data, go, className }: PanelProps) {
  const f = data?.flow;
  const t = Object.fromEntries((data?.ticketOutcomes ?? []).map((o) => [o.Label, o.Count])) as Record<string, number>;
  const fixKnown = t.NEEDS_HUMAN_ACTION ?? 0, causeOpen = t.L3_ESCALATION ?? 0, handed = fixKnown + causeOpen;
  const graph = useMemo(() => {
    if (!f) return null;
    const answered = Math.max(0, f.Chats - f.ChatsToTicket), direct = Math.max(0, f.Tickets - f.ChatsToTicket);
    const l3 = f.L3Open + f.L3Resolved;
    const nodes: FlowNode[] = [
      { id: "chats", col: 0, value: f.Chats, label: "Conversations", tone: "mid", onClick: go.l1 },
      { id: "direct", col: 0, value: direct, label: "Raised directly", sub: "portal or email", tone: "faint", onClick: go.tickets },
      { id: "answered", col: 1, value: answered, label: "Answered by assistant", tone: "signal", onClick: go.l1 },
      { id: "tickets", col: 1, value: f.Tickets, label: "Tickets", tone: "strong", onClick: go.tickets },
      { id: "resolved", col: 2, value: t.RESOLUTION ?? 0, label: "Resolved by L2", tone: "signal", onClick: go.runs },
      { id: "update", col: 2, value: t.UPDATE ?? 0, label: "Update posted", tone: "faint", onClick: go.runs },
      { id: "active", col: 2, value: t.ACTIVE ?? 0, label: "L2 working", tone: "signal", onClick: go.live },
      { id: "unclaimed", col: 2, value: t.UNCLAIMED ?? 0, label: "Not claimed yet", tone: "danger", onClick: go.tickets },
      { id: "none", col: 2, value: t.NO_OUTCOME ?? 0, label: "No outcome", tone: "faint", onClick: go.runs },
      { id: "handed", col: 2, value: handed, label: "Handed to people", sub: `${fixKnown} fix known · ${causeOpen} cause open`, tone: "warn", onClick: go.l3 },
      { id: "l3open", col: 3, value: f.L3Open, label: "L3 open", tone: "warn", onClick: go.l3 },
      { id: "l3done", col: 3, value: f.L3Resolved, label: "L3 resolved", tone: "signal", onClick: go.l3 },
    ].filter((n) => n.value > 0) as FlowNode[];
    const share = (v: number) => (l3 ? Math.round((v / l3) * handed) : 0);
    const links: FlowLink[] = ([
      { from: "chats", to: "answered", value: answered, tone: "signal" },
      { from: "chats", to: "tickets", value: f.ChatsToTicket, tone: "mid" },
      { from: "direct", to: "tickets", value: direct, tone: "faint" },
      { from: "tickets", to: "resolved", value: t.RESOLUTION ?? 0, tone: "signal" },
      { from: "tickets", to: "update", value: t.UPDATE ?? 0, tone: "faint" },
      { from: "tickets", to: "active", value: t.ACTIVE ?? 0, tone: "signal" },
      { from: "tickets", to: "unclaimed", value: t.UNCLAIMED ?? 0, tone: "danger" },
      { from: "tickets", to: "none", value: t.NO_OUTCOME ?? 0, tone: "faint" },
      { from: "tickets", to: "handed", value: handed, tone: "warn" },
      { from: "handed", to: "l3open", value: share(f.L3Open), tone: "warn" },
      { from: "handed", to: "l3done", value: share(f.L3Resolved), tone: "signal" },
    ] satisfies FlowLink[]).filter((l) => l.value > 0 && nodes.some((n) => n.id === l.from) && nodes.some((n) => n.id === l.to));
    return { nodes, links, answered };
  }, [f, t.RESOLUTION, t.UPDATE, t.ACTIVE, t.UNCLAIMED, t.NO_OUTCOME, handed, fixKnown, causeOpen, go]);

  return (
    <Panel icon={GitFork} title="Support flow" meta="Every conversation and ticket, where it went · all time" className={className}>
      {!f || !graph ? <Skeleton className="h-72" /> : (
        <div className="space-y-4">
          <Headline value={f.Tickets} unit="tickets" note={`from ${f.Chats} conversations · ${pct(graph.answered, f.Chats)} answered without a ticket`} />
          <FlowGraph nodes={graph.nodes} links={graph.links} label="Support flow" />
          <div className="grid grid-cols-2 gap-3 border-t pt-3 sm:grid-cols-4">
            <Stat label="Assistant containment" value={pct(graph.answered, f.Chats)} tone="signal" />
            <Stat label="Resolved by L2 alone" value={pct(t.RESOLUTION ?? 0, f.Tickets)} />
            <Stat label="With people now" value={f.L3Open} tone={f.L3Open ? "warn" : undefined} />
            <Stat label="Tickets closed" value={`${f.TicketsClosed} of ${f.Tickets}`} />
          </div>
        </div>
      )}
    </Panel>
  );
}

// ---------- Live engineer ----------

function LivePanel({ data, now, go, className }: PanelProps) {
  const c = data?.counts;
  const live = data?.live?.IsActive ? data.live : null;
  const byAgo = Object.fromEntries((data?.hourly ?? []).map((h) => [h.HoursAgo, h]));
  const columns: Column[] = Array.from({ length: 24 }, (_, i) => {
    const ago = 23 - i, h = byAgo[ago], at = new Date(now - ago * 3_600_000).getHours();
    const label = `${String(at).padStart(2, "0")}h`;
    return {
      key: String(ago), label,
      tip: <>{ago ? `${ago} h ago` : "this hour"} · Jev <b>{h?.Jev ?? 0}</b> · model <b>{h?.Model ?? 0}</b></>,
      segments: [{ id: "jev", value: h?.Jev ?? 0, tone: "signal" }, { id: "model", value: h?.Model ?? 0, tone: "mid" }],
    };
  });
  return (
    <Panel icon={Radio} title="Live engineer" meta={!data ? undefined : live ? "investigating now" : c?.LastClaimOn ? `idle · last claim ${ago(c.LastClaimOn)}` : "idle"} className={className}
      actions={<Button size="sm" variant="ghost" onClick={go.live}>{live ? "Watch" : "Replay"} <ArrowRight /></Button>}>
      {!data || !c ? <Skeleton className="h-72" /> : (
        <div className="flex h-full flex-col gap-4">
          <ModelServer sample={data.lmStudio} />
          {live ? (
            <button onClick={go.live} className="rounded-xl border border-signal/40 bg-signal-soft/40 p-3 text-left hover:border-signal">
              <p className="flex items-center gap-2 text-xs text-signal"><span className="size-2 rounded-full bg-signal motion-safe:animate-pulse" aria-hidden /><span className="font-mono">{ticketLabel(live.TicketNo)}</span> · claimed {ago(live.ClaimedOn)}</p>
              <p className="mt-1 line-clamp-2 text-sm font-medium">{live.BriefDetails}</p>
            </button>
          ) : (
            <Headline value={c.RunsLast24h} unit="runs" note="in the last 24 h" noteTone="faint" />
          )}
          <div>
            <p className="mb-2 flex items-center justify-between text-xs text-subtle-foreground">Decisions per hour · 24 h</p>
            <StackColumns columns={columns} label="Jev and model calls per hour, last 24 hours" height={96} tickEvery={6} />
          </div>
          <Legend inline rows={[{ label: "Jev decisions", value: c.JevCallsLast24h, tone: "signal" }, { label: "local model calls", value: c.ModelCallsLast24h, tone: "mid" }]} />
        </div>
      )}
    </Panel>
  );
}

// Last health sample of the local model server (LM Studio on the desktop): reachable, how fast, what is loaded.
function ModelServer({ sample }: { sample: Overview["lmStudio"] }) {
  let parsed: { latency_s?: number; models?: string[]; error?: string } | null = null;
  try { parsed = sample ? JSON.parse(sample.ResultJson) : null; } catch { parsed = null; }
  const ok = !!parsed && !parsed.error && (parsed.models?.length ?? 0) > 0;
  return (
    <p className="flex items-center gap-2 rounded-lg bg-surface-2 px-3 py-2 text-xs text-muted-foreground" title={parsed?.models?.join(", ")}>
      <span className={cn("size-2 shrink-0 rounded-full", !sample ? "bg-border-strong" : ok ? "bg-signal" : "bg-destructive")} aria-hidden />
      <span className="min-w-0 truncate">
        {!sample ? "Local model server never sampled" : ok
          ? <>Local model server · <span className="font-mono">{Math.round((parsed!.latency_s ?? 0) * 1000)} ms</span> · {parsed!.models!.length} models · checked {ago(sample.EventOn)}</>
          : <>Local model server unreachable · checked {ago(sample.EventOn)}</>}
      </span>
    </p>
  );
}

// ---------- Open tickets ----------

const LANES: { id: AttentionTicket["AttentionState"]; label: string; tone: VizTone }[] = [
  { id: "Unclaimed", label: "Not claimed", tone: "danger" },
  { id: "No active work", label: "No active work", tone: "strong" },
  { id: "L2 working", label: "L2 working", tone: "signal" },
  { id: "Waiting on requester", label: "Waiting on requester", tone: "mid" },
  { id: "L3 attention", label: "With L3 people", tone: "warn" },
];
const AGE_BINS = ["< 6 h", "6–24 h", "1–3 d", "3–7 d", "> 7 d"];
const ageBin = (h: number) => (h < 6 ? 0 : h < 24 ? 1 : h < 72 ? 2 : h < 168 ? 3 : 4);
const hours = (h: number) => (h < 48 ? `${h} h` : `${Math.round(h / 24)} d`);

function OpenPanel({ data, go, className }: PanelProps) {
  const c = data?.counts;
  const open = data?.attention ?? [];
  const stalled = [...open].sort((a, b) => b.StalledHours - a.StalledHours);
  const over24 = open.filter((t) => t.StalledHours >= 24).length;
  return (
    <Panel icon={Hourglass} title="Open tickets" meta="Each dot is a ticket · by who holds it and time since last progress" className={className}
      actions={<Button size="sm" variant="ghost" onClick={go.tickets}>All tickets <ArrowRight /></Button>}>
      {!c ? <Skeleton className="h-72" /> : (
        <div className="space-y-4">
          <Headline value={c.OpenTickets} unit="open" note={over24 ? `${over24} without progress for over a day` : "all moving within a day"} noteTone={over24 ? "warn" : "signal"} />
          <DotLanes label="Open tickets by owner and time since last progress" lanes={LANES} bins={AGE_BINS}
            dots={open.map((t) => ({
              id: t.ID, lane: t.AttentionState, bin: ageBin(t.StalledHours), onClick: () => go.ticket(t.ID),
              label: `${ticketLabel(t.TicketNo)}, ${t.StalledHours} hours without progress`,
              tip: <><b>{ticketLabel(t.TicketNo)}</b> · {hours(t.StalledHours)} without progress<br /><span className="text-muted-foreground">{(t.BriefDetails ?? "").slice(0, 60)}</span></>,
            }))} />
          {stalled.length > 0 && (
            <div>
              <p className="mb-1 text-xs text-subtle-foreground">Longest without progress</p>
              <ol className="divide-y">
                {stalled.slice(0, 3).map((t) => (
                  <li key={t.ID}>
                    <button onClick={() => go.ticket(t.ID)} className="flex w-full items-baseline gap-3 rounded-md px-1 py-1.5 text-left hover:bg-surface-2">
                      <span className="font-mono text-xs text-muted-foreground">{ticketLabel(t.TicketNo)}</span>
                      <span className="min-w-0 flex-1 truncate text-meta">{t.BriefDetails}</span>
                      <span className="shrink-0 font-mono text-xs tabular-nums text-warning">{hours(t.StalledHours)}</span>
                    </button>
                  </li>
                ))}
              </ol>
            </div>
          )}
        </div>
      )}
    </Panel>
  );
}

// ---------- L2 outcomes ----------

function OutcomesPanel({ data, now, go, className }: PanelProps) {
  const c = data?.counts;
  const all = data?.outcomes ?? [];
  const total = all.reduce((n, o) => n + o.Count, 0);
  const resolved = all.find((o) => o.Label === "RESOLUTION")?.Count ?? 0;
  const days = Array.from({ length: 14 }, (_, i) => {
    const d = new Date(now - (13 - i) * 86_400_000);
    return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
  });
  const columns: Column[] = days.map((day) => {
    const rows = (data?.daily ?? []).filter((r) => r.Day === day);
    const label = new Date(`${day}T00:00`).toLocaleDateString("en-IN", { day: "numeric", month: "short" });
    return {
      key: day, label,
      tip: rows.length ? <>{label}<br />{rows.map((r) => <span key={r.Label} className="block">{outcomeLabel(r.Label)} · <b>{r.Count}</b></span>)}</> : <>{label} · no replies</>,
      segments: OUTCOMES.map((o) => ({ id: o.id, value: rows.find((r) => r.Label === o.id)?.Count ?? 0, tone: o.tone })),
    };
  });
  return (
    <Panel icon={Trophy} title="L2 outcomes" meta={`${total} replies · last 14 days by day`} className={className}
      actions={<Button size="sm" variant="ghost" onClick={go.runs}>Runs <ArrowRight /></Button>}>
      {!data || !c ? <Skeleton className="h-72" /> : total ? (
        <div className="space-y-4">
          <Headline value={pct(resolved, total)} unit="resolved" note={`by L2 alone · ${resolved} of ${total}`} noteTone={resolved ? "signal" : "faint"} />
          <StackColumns columns={columns} label="L2 replies per day by outcome, last 14 days" height={120} tickEvery={3} />
          <Legend rows={OUTCOMES.map((o) => ({ label: outcomeLabel(o.id), value: all.find((x) => x.Label === o.id)?.Count ?? 0, tone: o.tone }))} />
          <div className="grid grid-cols-3 gap-3 border-t pt-3">
            <Stat label="Closed · 24 h" value={c.ResolvedLast24h ?? 0} tone={c.ResolvedLast24h ? "signal" : undefined} />
            <Stat label="To L3 · 24 h" value={c.L3OpenedLast24h ?? 0} />
            <Stat label="Failed runs · 24 h" value={c.FailedRunsLast24h ?? 0} tone={c.FailedRunsLast24h ? "danger" : undefined} />
          </div>
        </div>
      ) : <p className="text-sm text-muted-foreground">No L2 replies recorded yet.</p>}
    </Panel>
  );
}

// ---------- Intake by hour ----------

type IntakeMode = "all" | "tickets" | "chats";
const SHIFTS = [{ label: "06–14 h", from: 6, to: 14 }, { label: "14–22 h", from: 14, to: 22 }, { label: "22–06 h", from: 22, to: 30 }];

function IntakePanel({ data, now, className }: Omit<PanelProps, "go">) {
  const [mode, setMode] = useState<IntakeMode>("all");
  const value = (r: { Tickets: number; Chats: number }) => (mode === "tickets" ? r.Tickets : mode === "chats" ? r.Chats : r.Tickets + r.Chats);
  const rows = Array.from({ length: 7 }, (_, i) => {
    const d = new Date(now - (6 - i) * 86_400_000);
    const key = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
    const cells = Array.from({ length: 24 }, (_, h) => { const r = data?.intake?.find((x) => x.Day === key && x.Hour === h); return r ? value(r) : 0; });
    return { key, label: d.toLocaleDateString("en-IN", { weekday: "short", day: "numeric" }), cells };
  });
  const total = rows.reduce((n, r) => n + r.cells.reduce((a, b) => a + b, 0), 0);
  const shift = (from: number, to: number) => rows.reduce((n, r) => n + r.cells.reduce((a, v, h) => a + ((h >= from && h < to) || (h + 24 >= from && h + 24 < to) ? v : 0), 0), 0);
  let busiest = { label: "", v: 0 };
  rows.forEach((r) => r.cells.forEach((v, h) => { if (v > busiest.v) busiest = { label: `${r.label} ${String(h).padStart(2, "0")}:00`, v }; }));
  const unit = mode === "tickets" ? "ticket" : mode === "chats" ? "conversation" : "arrival";
  return (
    <Panel icon={CalendarClock} title="Intake by hour" meta="New conversations and tickets · last 7 days × 24 h" className={className}
      actions={<Segmented label="Intake type" value={mode} onChange={setMode} options={[{ id: "all", label: "All" }, { id: "tickets", label: "Tickets" }, { id: "chats", label: "Chats" }]} />}>
      {!data ? <Skeleton className="h-60" /> : (
        <div className="space-y-4">
          <Headline value={total} unit={`${unit}s`} note={busiest.v ? `busiest ${busiest.label} · ${busiest.v}` : "none this week"} />
          <HourHeat rows={rows} unit={unit} label={`${unit}s by day and hour, last 7 days`} />
          <div className="grid grid-cols-3 gap-3 border-t pt-3">
            {SHIFTS.map((s) => <Stat key={s.label} label={s.label} value={shift(s.from, s.to)} />)}
          </div>
        </div>
      )}
    </Panel>
  );
}

// ---------- Time to outcome ----------

const DUR_BINS = [
  { label: "<30s", to: 30 }, { label: "30s", to: 60 }, { label: "1m", to: 120 }, { label: "2m", to: 300 }, { label: "5m", to: 600 },
  { label: "10m", to: 1200 }, { label: "20m", to: 2400 }, { label: "40m", to: 3600 }, { label: "1h+", to: Infinity },
];
const binOf = (s: number) => DUR_BINS.findIndex((b) => s < b.to);
const human = (s: number) => (s < 60 ? `${s}s` : s < 3600 ? `${Math.round(s / 60)}m` : `${(s / 3600).toFixed(1)}h`);

function DurationPanel({ data, go, className }: PanelProps) {
  const runs = (data?.durations ?? []).filter((d) => d.Seconds >= 0);
  const sorted = runs.map((r) => r.Seconds).sort((a, b) => a - b);
  const q = (p: number) => sorted[Math.min(sorted.length - 1, Math.floor(p * sorted.length))] ?? 0;
  const p50 = q(0.5), p95 = q(0.95);
  // Marker position: the bin index plus how far into that bin the value falls.
  const at = (s: number) => { const i = binOf(s), lo = i ? DUR_BINS[i - 1].to : 0, hi = DUR_BINS[i].to; return i + (Number.isFinite(hi) ? (s - lo) / (hi - lo) : 0.5); };
  const columns: Column[] = DUR_BINS.map((b, i) => {
    const inBin = runs.filter((r) => binOf(r.Seconds) === i);
    return {
      key: b.label, label: b.label,
      tip: <>{i ? `${DUR_BINS[i - 1].label}–${b.label}` : "under 30 s"} · <b>{inBin.length}</b> runs{inBin.length ? <br /> : null}{OUTCOMES.map((o) => { const n = inBin.filter((r) => r.ResponseType === o.id).length; return n ? <span key={o.id} className="block">{outcomeLabel(o.id)} · {n}</span> : null; })}</>,
      segments: OUTCOMES.map((o) => ({ id: o.id, value: inBin.filter((r) => r.ResponseType === o.id).length, tone: o.tone })),
    };
  });
  const median = (id: string) => { const s = runs.filter((r) => r.ResponseType === id).map((r) => r.Seconds).sort((a, b) => a - b); return s.length ? human(s[Math.floor(s.length / 2)]) : "—"; };
  return (
    <Panel icon={Timer} title="Time to outcome" meta={`Claim to published reply · ${runs.length} runs · last 30 days`} className={className}
      actions={<Button size="sm" variant="ghost" onClick={go.runs}>Runs <ArrowRight /></Button>}>
      {!data ? <Skeleton className="h-60" /> : runs.length ? (
        <div className="space-y-4">
          <Headline value={human(p50)} unit="p50" note={`p95 ${human(p95)}`} />
          <StackColumns columns={columns} label="Runs by time from claim to published reply" height={128} markers={[{ at: at(p50), label: "p50" }, { at: at(p95), label: "p95" }]} />
          <div className="grid grid-cols-3 gap-3 border-t pt-3">
            <Stat label="Median · fix known" value={median("NEEDS_HUMAN_ACTION")} />
            <Stat label="Median · cause open" value={median("L3_ESCALATION")} />
            <Stat label="Median · resolved" value={median("RESOLUTION")} tone="signal" />
          </div>
        </div>
      ) : <p className="text-sm text-muted-foreground">No completed runs in the last 30 days.</p>}
    </Panel>
  );
}

// ---------- Recent activity ----------

const title = (t: string) => t.replace(/^L2 published\s*(\w*)/, (_, type: string) => `L2 reply · ${type ? outcomeLabel(type) : "published"}`);

function ActivityPanel({ data, go, className }: PanelProps) {
  const c = data?.counts;
  return (
    <Panel icon={Activity} title="Recent activity" meta={c ? `${c.ChatsLast24h} chats · ${c.RunsLast24h} investigations · 24 h` : undefined} pad="tight" className={className}
      actions={<Legend inline rows={[{ label: "L1", tone: "faint" }, { label: "L2", tone: "signal" }, { label: "L3", tone: "warn" }]} className="hidden sm:flex" />}>
      {!data ? <Skeleton className="m-2 h-40" /> : (
        <ol className="grid lg:grid-cols-2 lg:gap-x-4">
          {(data.activity ?? []).slice(0, 12).map((item, i) => (
            <li key={`${item.At}-${item.Lane}-${i}`} className="min-w-0">
              <button
                disabled={!item.RunID && !item.TicketNo}
                onClick={() => (item.RunID ? go.run(item.RunID) : go.tickets())}
                className="flex w-full items-start gap-3 rounded-lg px-2 py-2 text-left enabled:hover:bg-surface-2"
              >
                <span className="w-14 shrink-0 pt-px font-mono text-xs tabular-nums text-subtle-foreground">{clock(item.At)}</span>
                <span className={cn("mt-1.5 size-2 shrink-0 rounded-full", item.Lane === "l1" ? "bg-border-strong" : item.Lane === "l2" ? "bg-signal" : "bg-warning")} aria-label={item.Lane.toUpperCase()} />
                <span className="min-w-0 flex-1">
                  <span className="block truncate text-meta">
                    {title(item.Title)}
                    {item.TicketNo && <span className="ml-1.5 font-mono text-xs text-muted-foreground">{ticketLabel(item.TicketNo)}</span>}
                  </span>
                  {item.Detail && <span className="block truncate text-xs text-subtle-foreground">{item.Detail}</span>}
                </span>
                <span className="shrink-0 text-2xs tabular-nums text-subtle-foreground">{ago(item.At)}</span>
              </button>
            </li>
          ))}
          {!data.activity?.length && <li className="p-6 text-center text-sm text-muted-foreground">No support activity yet.</li>}
        </ol>
      )}
    </Panel>
  );
}
