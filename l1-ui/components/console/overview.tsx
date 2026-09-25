"use client";

import { useEffect, useState } from "react";
import { ArrowRight, Bot, CheckCircle2, Clock3, Headset, Radio, ShieldAlert, TriangleAlert, Users } from "lucide-react";
import { toast } from "sonner";
import { ops, type AttentionTicket, type Overview } from "@/lib/api";
import { ago, outcomeLabel, ticketLabel } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/primitives";
import { Ranked } from "./reports";

type Go = {
  live: () => void;
  l1: () => void;
  runs: () => void;
  l3: () => void;
  tickets: () => void;
  ticket: (id: string) => void;
  run: (id: string) => void;
};

export function OverviewView({ go }: { go: Go }) {
  const [data, setData] = useState<Overview | null>(null);

  useEffect(() => {
    const load = () => ops.overview().then(setData).catch((e: Error) => toast.error(e.message));
    load();
    const poll = setInterval(load, 10_000);
    return () => clearInterval(poll);
  }, []);

  const c = data?.counts;
  const attention = data?.attention ?? [];
  const activity = data?.activity ?? [];
  const outcomes = data?.outcomes ?? [];
  const lm = (() => {
    try {
      return data?.lmStudio ? (JSON.parse(data.lmStudio.ResultJson) as { latency_s?: number; models?: string[] }) : null;
    } catch {
      return null;
    }
  })();

  return (
    <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
      <div className="mx-auto max-w-7xl space-y-5 px-4 py-6 lg:px-8">
        <div className="flex flex-wrap items-end justify-between gap-3">
          <div>
            <h1 className="text-heading font-semibold tracking-tight">Command centre</h1>
            <p className="mt-0.5 text-sm text-muted-foreground">Workload, delays, hand-offs and system health across the helpdesk.</p>
          </div>
          {c && (
            <p className="flex items-center gap-2 text-meta text-muted-foreground">
              <span className={cn("size-2 rounded-full", c.ActiveRuns ? "bg-destructive" : "bg-success")} aria-hidden />
              {c.ActiveRuns ? `L2 working on ${c.ActiveRuns} ticket${c.ActiveRuns > 1 ? "s" : ""}` : "L2 idle"}
              {c.LastClaimOn && <> · last claim {ago(c.LastClaimOn)}</>}
            </p>
          )}
        </div>

        <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-4">
          <Lane icon={Users} title="Requesters" onOpen={go.tickets} rows={c && [["Open tickets", c.OpenTickets], ["Waiting on requester", c.WaitingOnRequester], ["Unclaimed", c.NewTickets]]} />
          <Lane icon={Headset} title="L1 · assistant" onOpen={go.l1} rows={c && [["Conversations, 24h", c.ChatsLast24h]]} note="Answers directly or raises a ticket" />
          <Lane icon={Bot} title="L2 · engineer" onOpen={go.runs} accent rows={c && [["Active now", c.ActiveRuns], ["Runs, 24h", c.RunsLast24h], ["Jev decisions, 24h", c.JevCallsLast24h], ["Writer calls, 24h", c.ModelCallsLast24h]]} />
          <Lane icon={ShieldAlert} title="L3 · people" onOpen={go.l3} rows={c && [["Open escalations", c.L3Open], ["Opened, 24h", c.L3OpenedLast24h]]} note="Human specialist attention" />
        </div>

        <section className="grid gap-px overflow-hidden rounded-xl border bg-border sm:grid-cols-3" aria-label="24 hour operational pulse">
          <Pulse icon={CheckCircle2} label="Resolved" value={c?.ResolvedLast24h} note="last 24h" />
          <Pulse icon={ShieldAlert} label="Escalated to L3" value={c?.L3OpenedLast24h} note="last 24h" />
          <Pulse icon={TriangleAlert} label="Failed L2 runs" value={c?.FailedRunsLast24h} note="last 24h" attention={!!c?.FailedRunsLast24h} />
        </section>

        <div className="grid gap-3 xl:grid-cols-3">
          <section className="overflow-hidden rounded-xl border bg-surface xl:col-span-2" aria-label="Tickets needing attention">
            <div className="flex flex-wrap items-center gap-2 border-b px-4 py-3">
              <div>
                <h2 className="text-sm font-semibold">Unresolved attention queue</h2>
                <p className="mt-0.5 text-2xs text-subtle-foreground">Escalated, unclaimed and stalled tickets. Delay is based on recorded progress, not an invented SLA.</p>
              </div>
              <Button variant="ghost" size="sm" className="ml-auto" onClick={go.tickets}>All tickets <ArrowRight /></Button>
            </div>
            {!data ? (
              <div className="space-y-2 p-4"><Skeleton className="h-16" /><Skeleton className="h-16" /><Skeleton className="h-16" /></div>
            ) : attention.length ? (
              <ol className="divide-y">
                {attention.map((t) => <AttentionRow key={t.ID} ticket={t} onOpen={() => go.ticket(t.ID)} />)}
              </ol>
            ) : (
              <p className="p-6 text-center text-sm text-muted-foreground">
                {data.attention === undefined ? "Attention data is not available yet." : "No unresolved tickets need attention."}
              </p>
            )}
          </section>

          <div className="space-y-3">
            <section className="rounded-xl border bg-surface p-4" aria-label="Current L2 work">
              <div className="flex items-center gap-2">
                <Radio className={cn("size-4", data?.live?.IsActive ? "text-destructive" : "text-subtle-foreground")} aria-hidden />
                <h2 className="text-sm font-semibold">Current L2 work</h2>
              </div>
              {!data ? (
                <Skeleton className="mt-3 h-20" />
              ) : data.live?.IsActive ? (
                <div className="mt-3">
                  <button className="block text-left" onClick={() => go.run(data.live!.ID)}>
                    <span className="font-mono text-xs text-muted-foreground">{ticketLabel(data.live.TicketNo)}</span>
                    <span className="mt-1 line-clamp-2 block text-meta font-medium">{data.live.BriefDetails}</span>
                  </button>
                  <div className="mt-3 flex gap-2">
                    <Button size="sm" onClick={go.live}>Watch live <ArrowRight /></Button>
                    <Button size="sm" variant="outline" onClick={() => go.run(data.live!.ID)}>Run details</Button>
                  </div>
                </div>
              ) : (
                <div className="mt-3">
                  <p className="text-meta text-muted-foreground">No L2 investigation is active.</p>
                  <Button size="sm" variant="outline" className="mt-3" onClick={go.runs}>Run history</Button>
                </div>
              )}
            </section>

            <section className="rounded-xl border bg-surface p-4" aria-label="Outcomes">
              <h2 className="text-sm font-semibold">L2 outcomes</h2>
              <div className="mt-4">{data ? <Ranked rows={outcomes.map((o) => ({ label: outcomeLabel(o.Label), count: o.Count }))} /> : <Skeleton className="h-32" />}</div>
            </section>

            <section className="rounded-xl border bg-surface p-4" aria-label="Writer model">
              <h2 className="text-sm font-semibold">Writer model</h2>
              {lm ? (
                <p className="mt-2 text-meta text-muted-foreground">
                  <span className="text-success">Reachable</span> · {Math.round((lm.latency_s ?? 0) * 1000)}ms · {lm.models?.length ?? 0} models loaded · checked {ago(data?.lmStudio?.EventOn)}
                </p>
              ) : (
                <p className="mt-2 text-meta text-muted-foreground">No recent health sample.</p>
              )}
            </section>
          </div>
        </div>

        <section className="rounded-xl border bg-surface" aria-label="Activity">
          <div className="flex items-center border-b px-4 py-3">
            <h2 className="text-sm font-semibold">Recent activity</h2>
            <span className="ml-auto text-2xs text-subtle-foreground">Across L1, L2 and L3</span>
          </div>
          <ol className="divide-y">
            {!data && <li className="p-4"><Skeleton className="h-40" /></li>}
            {activity.slice(0, 16).map((a, i) => (
              <li key={i} className="flex items-start gap-3 px-4 py-2.5">
                <span className={cn("mt-0.5 w-7 shrink-0 rounded px-1 py-0.5 text-center text-2xs font-bold uppercase", a.Lane === "l1" ? "bg-surface-3 text-muted-foreground" : a.Lane === "l2" ? "bg-primary-soft text-primary-soft-foreground" : "bg-warning-soft text-warning")}>{a.Lane}</span>
                <div className="min-w-0 flex-1">
                  <p className="text-meta">
                    <span className="font-medium">{a.Title.replace(/NEEDS_HUMAN_ACTION|L3_ESCALATION|RESOLUTION|UPDATE/, (m) => outcomeLabel(m).toLowerCase())}</span>
                    {a.TicketNo && (
                      <button className="ml-1.5 font-mono text-xs text-muted-foreground hover:text-foreground hover:underline" onClick={() => (a.RunID ? go.run(a.RunID) : go.tickets())}>{ticketLabel(a.TicketNo)}</button>
                    )}
                  </p>
                  {a.Detail && <p className="truncate text-xs text-muted-foreground">{a.Detail}</p>}
                </div>
                <span className="shrink-0 text-2xs text-subtle-foreground">{ago(a.At)}</span>
              </li>
            ))}
          </ol>
        </section>
      </div>
    </div>
  );
}

function AttentionRow({ ticket, onOpen }: { ticket: AttentionTicket; onOpen: () => void }) {
  const tone = ticket.AttentionState === "L3 attention"
    ? "bg-warning-soft text-warning"
    : ticket.AttentionState === "Unclaimed" || ticket.AttentionState === "No active work"
      ? "bg-destructive-soft text-destructive"
      : ticket.AttentionState === "L2 working"
        ? "bg-primary-soft text-primary-soft-foreground"
        : "bg-surface-3 text-muted-foreground";

  return (
    <li>
      <button onClick={onOpen} className="flex w-full flex-col gap-2 px-4 py-3 text-left hover:bg-surface-2 sm:flex-row sm:items-center sm:justify-between">
        <div className="min-w-0 flex-1">
          <span className="flex flex-wrap items-center gap-2">
            <span className="font-mono text-xs text-muted-foreground">{ticketLabel(ticket.TicketNo)}</span>
            <span className={cn("rounded px-1.5 py-0.5 text-2xs font-medium", tone)}>{ticket.AttentionState}</span>
            {ticket.Priority && <span className="text-2xs text-subtle-foreground">{ticket.Priority}</span>}
          </span>
          <span className="mt-1 line-clamp-2 block text-meta font-medium">{ticket.BriefDetails}</span>
        </div>
        <span className="flex shrink-0 gap-4 text-2xs text-subtle-foreground sm:text-right">
          <span><Clock3 className="mr-1 inline size-3" aria-hidden />open {ago(ticket.CreatedOn)}</span>
          <span>progress {ago(ticket.LastProgressOn)}</span>
        </span>
      </button>
    </li>
  );
}

function Pulse({ icon: Icon, label, value, note, attention }: { icon: typeof CheckCircle2; label: string; value: number | undefined; note: string; attention?: boolean }) {
  return (
    <div className="flex items-center gap-3 bg-surface px-4 py-3">
      <Icon className={cn("size-4 text-subtle-foreground", attention && "text-destructive")} aria-hidden />
      <div>
        <p className="text-2xs text-subtle-foreground">{label} · {note}</p>
        {value === undefined ? <Skeleton className="mt-1 h-5 w-10" /> : <p className={cn("text-title font-semibold tabular-nums", attention && "text-destructive")}>{value}</p>}
      </div>
    </div>
  );
}

function Lane({ icon: Icon, title, rows, note, onOpen, accent }: { icon: typeof Bot; title: string; rows: (string | number)[][] | undefined; note?: string; onOpen: () => void; accent?: boolean }) {
  return (
    <button onClick={onOpen} className={cn("group relative flex flex-col rounded-xl border bg-surface p-4 text-left hover:border-border-strong", accent && "border-primary/40")}>
      <span className="flex items-center gap-2">
        <span className={cn("grid size-8 place-items-center rounded-lg", accent ? "bg-primary text-primary-foreground" : "bg-surface-3 text-muted-foreground")}>
          <Icon className="size-4" aria-hidden />
        </span>
        <span className="text-sm font-semibold">{title}</span>
        <ArrowRight className="ml-auto size-4 text-subtle-foreground opacity-0 transition-opacity group-hover:opacity-100" aria-hidden />
      </span>
      {rows ? (
        <dl className="mt-4 space-y-1.5">
          {rows.map(([k, v], i) => (
            <div key={k} className="flex items-baseline justify-between gap-3">
              <dt className="text-meta text-muted-foreground">{k}</dt>
              <dd className={cn("tabular-nums", i === 0 ? "text-heading font-semibold" : "text-sm")}>{v}</dd>
            </div>
          ))}
        </dl>
      ) : (
        <Skeleton className="mt-4 h-16" />
      )}
      {note && <p className="mt-auto pt-3 text-2xs text-subtle-foreground">{note}</p>}
    </button>
  );
}
