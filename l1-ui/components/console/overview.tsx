"use client";

import { useCallback, useEffect, useState } from "react";
import { Activity, ArrowRight, BellRing, Gauge, Radio, Trophy } from "lucide-react";
import { ops, type AttentionTicket, type Overview } from "@/lib/api";
import { ago, clock, outcomeLabel, ticketLabel } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/primitives";
import { Headline, IconTile, Legend, Panel, SegmentBar, Stat, type VizTone } from "@/components/ui/viz";

type Go = {
  live: () => void;
  l1: () => void;
  runs: () => void;
  l3: () => void;
  tickets: () => void;
  ticket: (id: string) => void;
  run: (id: string) => void;
};

const OUTCOME_TONE: Record<string, VizTone> = { RESOLUTION: "signal", NEEDS_HUMAN_ACTION: "strong", L3_ESCALATION: "warn", UPDATE: "mid", QUESTION: "faint" };

export function OverviewView({ go }: { go: Go }) {
  const [data, setData] = useState<Overview | null>(null);
  const [error, setError] = useState<string | null>(null);

  const refresh = useCallback(() => {
    ops.overview()
      .then((next) => {
        setData(next);
        setError(null);
      })
      .catch((reason: Error) => setError(reason.message));
  }, []);

  useEffect(() => {
    refresh();
    const poll = setInterval(refresh, 10_000);
    return () => clearInterval(poll);
  }, [refresh]);

  const c = data?.counts;
  const attention = data?.attention ?? [];
  const outcomes = [...(data?.outcomes ?? [])].sort((a, b) => b.Count - a.Count);
  const outcomeTotal = outcomes.reduce((n, o) => n + o.Count, 0);
  const resolved = outcomes.find((o) => o.Label === "RESOLUTION")?.Count ?? 0;
  const other = c ? Math.max(0, c.OpenTickets - c.NewTickets - c.ActiveRuns - c.WaitingOnRequester - c.L3Open) : 0;
  const live = data?.live?.IsActive ? data.live : null;

  if (!data && error)
    return (
      <div className="grid flex-1 place-items-center p-6">
        <section role="alert" className="max-w-sm text-center">
          <IconTile icon={Gauge} className="mx-auto" />
          <h2 className="mt-3 text-sm font-semibold">Could not load the command centre</h2>
          <p className="mt-1 text-meta text-muted-foreground">Check that the helpdesk service is running, then try again.</p>
          <Button size="sm" variant="outline" className="mt-4" onClick={refresh}>Try again</Button>
        </section>
      </div>
    );

  return (
    <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
      <div className="mx-auto max-w-7xl space-y-3 px-4 py-3 lg:px-6">
        <header className="flex flex-wrap items-center gap-3">
          <IconTile icon={Gauge} />
          <div className="min-w-0 flex-1">
            <h1 className="text-title font-semibold tracking-tight">Command centre</h1>
          </div>
          {data && error && <p role="status" className="font-mono text-xs text-warning">refresh failed · showing last data</p>}
        </header>

        <div className="grid gap-3 lg:grid-cols-3 lg:items-start">
          <Panel icon={Gauge} title="Open tickets" className="lg:col-span-2"
            actions={<Button size="sm" variant="ghost" onClick={go.tickets}>All tickets <ArrowRight /></Button>}>
            {c ? (
              <div className="space-y-4">
                <Headline value={c.OpenTickets} unit="open" note={`${c.ResolvedLast24h ?? 0} resolved in 24 h`} />
                <SegmentBar label="Open tickets by owner" segments={[
                  { label: "L2 working", value: c.ActiveRuns, tone: "signal" },
                  { label: "Waiting on requester", value: c.WaitingOnRequester, tone: "strong" },
                  { label: "L3 people", value: c.L3Open, tone: "warn" },
                  { label: "Unclaimed", value: c.NewTickets, tone: "danger" },
                  { label: "Other", value: other, tone: "hatch" },
                ]} />
                <Legend inline rows={[
                  { label: "L2 working", value: c.ActiveRuns, tone: "signal", onClick: go.live },
                  { label: "waiting on requester", value: c.WaitingOnRequester, tone: "strong", onClick: go.tickets },
                  { label: "with L3", value: c.L3Open, tone: "warn", onClick: go.l3 },
                  { label: "unclaimed", value: c.NewTickets, tone: "danger", onClick: go.tickets },
                  ...(other ? [{ label: "other", value: other, tone: "hatch" as const }] : []),
                ]} />
              </div>
            ) : <Skeleton className="h-28" />}
          </Panel>

          <Panel icon={Radio} title="Live engineer" meta={!data ? undefined : live ? "investigating now" : c?.LastClaimOn ? `last claim ${ago(c.LastClaimOn)}` : undefined}
            actions={!live ? <Button size="sm" variant="ghost" onClick={go.live}>Replay <ArrowRight /></Button> : undefined}>
            {data && <ModelServer sample={data.lmStudio} />}
            {!data ? <Skeleton className="h-28" /> : live ? (
              <div className="flex flex-col">
                <p className="flex items-center gap-2 font-mono text-xs text-signal"><span className="size-2 rounded-full bg-signal motion-safe:animate-pulse" aria-hidden />{ticketLabel(live.TicketNo)} · {ago(live.ClaimedOn)}</p>
                <p className="mt-1.5 line-clamp-2 text-sm font-medium">{live.BriefDetails}</p>
                <div className="flex flex-wrap gap-2 pt-4">
                  <button onClick={go.live} className="flex h-9 items-center gap-2 rounded-full bg-foreground px-4 text-sm font-medium text-background hover:opacity-90">Watch it work <ArrowRight className="size-4" aria-hidden /></button>
                  <Button size="sm" variant="ghost" onClick={() => go.ticket(live.TicketID)}>Ticket</Button>
                </div>
              </div>
            ) : (
              <div className="flex flex-col">
                <p className="text-sm text-muted-foreground">No ticket is being investigated. The engineer claims the next one within two minutes.</p>
                <div className="grid grid-cols-3 gap-3 pt-4">
                  <Stat label="Runs · 24 h" value={c?.RunsLast24h ?? 0} />
                  <Stat label="Jev · 24 h" value={c?.JevCallsLast24h ?? 0} tone="signal" />
                  <Stat label="Model · 24 h" value={c?.ModelCallsLast24h ?? 0} />
                </div>
              </div>
            )}
          </Panel>
        </div>

        <div className="grid gap-3 lg:grid-cols-3 lg:items-start">
          <Panel icon={BellRing} title="Needs attention" meta={data ? `${attention.length} of ${c?.OpenTickets ?? 0} open` : undefined} className="lg:col-span-2" pad="none">
            {!data ? <div className="space-y-2 p-4"><Skeleton className="h-14" /><Skeleton className="h-14" /><Skeleton className="h-14" /></div> : attention.length ? (
              <ol className="divide-y">{attention.map((t) => <AttentionRow key={t.ID} ticket={t} onOpen={() => go.ticket(t.ID)} />)}</ol>
            ) : (
              <p className="p-8 text-center text-sm text-muted-foreground">{data.attention === undefined ? "Attention tickets are unavailable right now." : "Nothing needs attention. Every open ticket is moving."}</p>
            )}
          </Panel>

          <Panel icon={Trophy} title="L2 outcomes" meta={data ? `${outcomeTotal} replies` : undefined} actions={<Button size="sm" variant="ghost" onClick={go.runs}>Runs <ArrowRight /></Button>}>
            {!data ? <Skeleton className="h-40" /> : outcomeTotal ? (
              <div className="space-y-4">
                <Headline value={`${Math.round((resolved / outcomeTotal) * 100)}%`} unit="resolved" note="by L2 alone" />
                <SegmentBar label="L2 outcomes" segments={outcomes.map((o) => ({ label: outcomeLabel(o.Label), value: o.Count, tone: OUTCOME_TONE[o.Label] ?? "faint" }))} />
                <Legend rows={outcomes.map((o) => ({ label: outcomeLabel(o.Label).toLowerCase(), value: o.Count, tone: OUTCOME_TONE[o.Label] ?? "faint" }))} />
                <div className="grid grid-cols-3 gap-3 border-t pt-3">
                  <Stat label="Resolved · 24 h" value={c?.ResolvedLast24h ?? 0} tone="signal" />
                  <Stat label="To L3 · 24 h" value={c?.L3OpenedLast24h ?? 0} />
                  <Stat label="Failed · 24 h" value={c?.FailedRunsLast24h ?? 0} tone={c?.FailedRunsLast24h ? "danger" : undefined} />
                </div>
              </div>
            ) : <p className="text-sm text-muted-foreground">No L2 replies recorded yet.</p>}
          </Panel>
        </div>

        <Panel icon={Activity} title="Recent activity" meta={c ? `${c.ChatsLast24h} chats · ${c.RunsLast24h} investigations · 24 h` : undefined} pad="tight"
          actions={<Legend inline rows={[{ label: "L1", tone: "faint" }, { label: "L2", tone: "signal" }, { label: "L3", tone: "warn" }]} className="hidden sm:flex" />}>
          {!data ? <Skeleton className="m-2 h-40" /> : (
            <ol>
              {(data.activity ?? []).slice(0, 12).map((item, i) => (
                <li key={`${item.At}-${item.Lane}-${i}`}>
                  <button
                    disabled={!item.RunID && !item.TicketNo}
                    onClick={() => (item.RunID ? go.run(item.RunID) : go.tickets())}
                    className="flex w-full items-start gap-3 rounded-lg px-2 py-2 text-left enabled:hover:bg-surface-2"
                  >
                    <span className="w-16 shrink-0 pt-px font-mono text-xs text-subtle-foreground">{clock(item.At)}</span>
                    <span className={cn("mt-1.5 size-2 shrink-0 rounded-full", item.Lane === "l1" ? "bg-border-strong" : item.Lane === "l2" ? "bg-signal" : "bg-warning")} aria-label={item.Lane.toUpperCase()} />
                    <span className="min-w-0 flex-1">
                      <span className="block text-meta">
                        {item.Title.replace(/NEEDS_HUMAN_ACTION|L3_ESCALATION|RESOLUTION|UPDATE/, (value) => outcomeLabel(value).toLowerCase())}
                        {item.TicketNo && <span className="ml-1.5 font-mono text-xs text-muted-foreground">{ticketLabel(item.TicketNo)}</span>}
                      </span>
                      {item.Detail && <span className="block truncate text-xs text-subtle-foreground">{item.Detail}</span>}
                    </span>
                    <span className="shrink-0 font-mono text-2xs text-subtle-foreground">{ago(item.At)}</span>
                  </button>
                </li>
              ))}
              {!data.activity?.length && <li className="p-6 text-center text-sm text-muted-foreground">No support activity yet.</li>}
            </ol>
          )}
        </Panel>
      </div>
    </div>
  );
}

const STATE_PILL: Record<AttentionTicket["AttentionState"], string> = {
  "L3 attention": "bg-warning-soft text-warning",
  Unclaimed: "bg-destructive-soft text-destructive",
  "No active work": "bg-destructive-soft text-destructive",
  "L2 working": "bg-signal-soft text-signal",
  "Waiting on requester": "bg-surface-3 text-muted-foreground",
};

function AttentionRow({ ticket, onOpen }: { ticket: AttentionTicket; onOpen: () => void }) {
  return (
    <li>
      <button onClick={onOpen} className="flex w-full flex-col gap-2 px-4 py-3 text-left hover:bg-surface-2 sm:flex-row sm:items-center sm:gap-4">
        <span className="min-w-0 flex-1">
          <span className="block truncate font-mono text-sm">{ticketLabel(ticket.TicketNo)} <span className="font-sans text-meta text-foreground">{ticket.BriefDetails}</span></span>
          <span className="mt-0.5 block font-mono text-xs text-subtle-foreground">open {ago(ticket.CreatedOn)} · last progress {ago(ticket.LastProgressOn)}</span>
        </span>
        <span className={cn("shrink-0 self-start rounded-md px-2.5 py-1 text-xs font-medium sm:self-center", STATE_PILL[ticket.AttentionState])}>{ticket.AttentionState}</span>
      </button>
    </li>
  );
}

// Last health sample of the local model server (LM Studio on the desktop): reachable, how fast, what is loaded.
function ModelServer({ sample }: { sample: Overview["lmStudio"] }) {
  let parsed: { latency_s?: number; models?: string[]; error?: string } | null = null;
  try { parsed = sample ? JSON.parse(sample.ResultJson) : null; } catch { parsed = null; }
  const ok = !!parsed && !parsed.error && (parsed.models?.length ?? 0) > 0;
  return (
    <p className="mb-3 flex items-center gap-2 border-b pb-3 font-mono text-2xs text-subtle-foreground" title={parsed?.models?.join(", ")}>
      <span className={cn("size-1.5 shrink-0 rounded-full", !sample ? "bg-border-strong" : ok ? "bg-signal" : "bg-destructive")} aria-hidden />
      <span className="min-w-0 truncate">
        {!sample ? "local model server · never sampled" : ok
          ? `local model server · ${Math.round((parsed!.latency_s ?? 0) * 1000)} ms · ${parsed!.models!.length} models · checked ${ago(sample.EventOn)}`
          : `local model server unreachable · checked ${ago(sample.EventOn)}`}
      </span>
    </p>
  );
}
