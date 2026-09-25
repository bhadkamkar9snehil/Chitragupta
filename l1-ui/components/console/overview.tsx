"use client";

import { useCallback, useEffect, useState } from "react";
import { ArrowRight, Clock3, Radio } from "lucide-react";
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
  const activity = data?.activity ?? [];
  const outcomes = data?.outcomes ?? [];

  return (
    <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
      <div className="mx-auto max-w-7xl space-y-5 px-4 py-6 lg:px-8">
        <header className="flex flex-wrap items-end justify-between gap-3">
          <div>
            <h1 className="text-heading font-semibold tracking-tight">Command centre</h1>
            <p className="mt-0.5 text-sm text-muted-foreground">Open requests, follow-ups and hand-offs across the support desks.</p>
          </div>
          {c && c.ActiveRuns > 1 && (
            <p className="flex items-center gap-2 text-meta text-muted-foreground">
              <span className="size-2 rounded-full bg-primary" aria-hidden />
              L2 handling {c.ActiveRuns} tickets
            </p>
          )}
        </header>

        {!data && error ? (
          <section role="alert" className="rounded-xl border bg-surface p-5">
            <h2 className="text-sm font-semibold">Could not load the helpdesk overview</h2>
            <p className="mt-1 text-meta text-muted-foreground">Check your connection, then try again.</p>
            <Button size="sm" variant="outline" className="mt-4 min-h-11 sm:min-h-8" onClick={refresh}>Try again</Button>
          </section>
        ) : (
          <>
        {data && error && (
          <div role="status" className="flex flex-wrap items-center justify-between gap-3 rounded-lg border bg-surface px-4 py-3 text-meta">
            <p className="text-muted-foreground">Could not refresh. Showing the last available overview.</p>
            <Button size="sm" variant="outline" className="min-h-11 sm:min-h-8" onClick={refresh}>Try again</Button>
          </div>
        )}

        <section className="grid grid-cols-2 gap-px overflow-hidden rounded-xl border bg-border sm:grid-cols-4" aria-label="Helpdesk workload">
          <SummaryMetric label="Open tickets" value={c?.OpenTickets} onClick={go.tickets} />
          <SummaryMetric label="Unclaimed" value={c?.NewTickets} onClick={go.tickets} />
          <SummaryMetric label="Waiting on requester" value={c?.WaitingOnRequester} onClick={go.tickets} />
          <SummaryMetric label="Open L3 escalations" value={c?.L3Open} onClick={go.l3} />
        </section>

        <div className="grid gap-4 xl:grid-cols-[minmax(0,2fr)_minmax(18rem,0.9fr)]">
          <section className="overflow-hidden rounded-xl border bg-surface" aria-label="Tickets needing attention">
            <div className="flex flex-wrap items-center gap-2 border-b px-4 py-3.5">
              <div>
                <h2 className="text-sm font-semibold">Tickets needing attention</h2>
                <p className="mt-0.5 max-w-2xl text-2xs text-subtle-foreground">Escalated, unclaimed and stalled tickets first. Time since last recorded progress is for triage, not an SLA.</p>
              </div>
              {data && <span className="ml-auto text-2xs text-subtle-foreground">Showing {attention.length} of {c?.OpenTickets ?? 0} open</span>}
              <Button variant="ghost" size="sm" className="min-h-11 sm:min-h-8" onClick={go.tickets}>All tickets <ArrowRight /></Button>
            </div>
            {!data ? (
              <div className="space-y-2 p-4"><Skeleton className="h-16" /><Skeleton className="h-16" /><Skeleton className="h-16" /></div>
            ) : attention.length ? (
              <ol className="divide-y">
                {attention.map((ticket) => <AttentionRow key={ticket.ID} ticket={ticket} onOpen={() => go.ticket(ticket.ID)} />)}
              </ol>
            ) : (
              <p className="p-6 text-center text-sm text-muted-foreground">
                {data.attention === undefined ? "Attention tickets are unavailable right now." : "No open tickets need attention."}
              </p>
            )}
          </section>

          <div className="space-y-4">
            <section className="rounded-xl border bg-surface p-4" aria-label="Ticket being handled by L2">
              <div className="flex items-center gap-2">
                <Radio className={cn("size-4", data?.live?.IsActive ? "text-primary" : "text-subtle-foreground")} aria-hidden />
                <h2 className="text-sm font-semibold">L2 handling now</h2>
              </div>
              {!data ? (
                <Skeleton className="mt-3 h-20" />
              ) : data.live?.IsActive ? (
                <div className="mt-3">
                  <button className="block min-h-11 text-left" onClick={() => go.ticket(data.live!.TicketID)}>
                    <span className="font-mono text-xs text-muted-foreground">{ticketLabel(data.live.TicketNo)}</span>
                    <span className="mt-1 line-clamp-2 block text-meta font-medium">{data.live.BriefDetails}</span>
                  </button>
                  <div className="mt-3 flex flex-wrap gap-2">
                    <Button size="sm" className="min-h-11 sm:min-h-8" onClick={go.live}>Follow progress <ArrowRight /></Button>
                    <Button size="sm" variant="outline" className="min-h-11 sm:min-h-8" onClick={() => go.ticket(data.live!.TicketID)}>Ticket details</Button>
                  </div>
                </div>
              ) : (
                <div className="mt-3">
                  <p className="text-meta text-muted-foreground">No ticket is being investigated right now.</p>
                  <Button size="sm" variant="outline" className="mt-3 min-h-11 sm:min-h-8" onClick={go.tickets}>View open tickets</Button>
                </div>
              )}
            </section>

            <section className="rounded-xl border bg-surface p-4" aria-label="Support activity in the last 24 hours">
              <h2 className="text-sm font-semibold">Last 24 hours</h2>
              <dl className="mt-3 divide-y">
                <PeriodMetric label="Resolved" value={c?.ResolvedLast24h} />
                <PeriodMetric label="Handed to L3" value={c?.L3OpenedLast24h} />
                <PeriodMetric label="New conversations" value={c?.ChatsLast24h} />
              </dl>
            </section>
          </div>
        </div>

        <div className="grid gap-4 xl:grid-cols-[minmax(0,2fr)_minmax(18rem,0.9fr)]">
          <section className="overflow-hidden rounded-xl border bg-surface" aria-label="Recent support activity">
            <div className="flex items-center border-b px-4 py-3.5">
              <h2 className="text-sm font-semibold">Recent support activity</h2>
              <span className="ml-auto text-2xs text-subtle-foreground">Conversations, investigations and escalations</span>
            </div>
            <ol className="divide-y">
              {!data && <li className="p-4"><Skeleton className="h-40" /></li>}
              {activity.slice(0, 12).map((item, i) => (
                <li key={`${item.At}-${item.Lane}-${i}`} className="flex items-start gap-3 px-4 py-3">
                  <span className={cn("mt-0.5 w-7 shrink-0 rounded px-1 py-0.5 text-center text-2xs font-bold uppercase", item.Lane === "l1" ? "bg-surface-3 text-muted-foreground" : item.Lane === "l2" ? "bg-primary-soft text-primary-soft-foreground" : "bg-warning-soft text-warning")}>{item.Lane}</span>
                  <div className="min-w-0 flex-1">
                    <p className="text-meta">
                      <span className="font-medium">{item.Title.replace(/NEEDS_HUMAN_ACTION|L3_ESCALATION|RESOLUTION|UPDATE/, (value) => outcomeLabel(value).toLowerCase())}</span>
                      {item.TicketNo && (
                        <button className="ml-1.5 inline-flex min-h-11 items-center font-mono text-xs text-muted-foreground hover:text-foreground hover:underline sm:min-h-0" onClick={() => (item.RunID ? go.run(item.RunID) : go.tickets())}>{ticketLabel(item.TicketNo)}</button>
                      )}
                    </p>
                    {item.Detail && <p className="truncate text-xs text-muted-foreground">{item.Detail}</p>}
                  </div>
                  <span className="shrink-0 text-2xs text-subtle-foreground">{ago(item.At)}</span>
                </li>
              ))}
              {data && !activity.length && <li className="p-6 text-center text-sm text-muted-foreground">No support activity to show yet.</li>}
            </ol>
          </section>

          <section className="rounded-xl border bg-surface p-4" aria-label="L2 support outcomes">
            <h2 className="text-sm font-semibold">L2 support outcomes</h2>
            <p className="mt-1 text-2xs text-subtle-foreground">Recorded responses across the helpdesk.</p>
            <div className="mt-4">{data ? <Ranked rows={outcomes.map((outcome) => ({ label: outcomeLabel(outcome.Label), count: outcome.Count }))} /> : <Skeleton className="h-32" />}</div>
          </section>
        </div>
          </>
        )}
      </div>
    </div>
  );
}

function SummaryMetric({ label, value, onClick }: { label: string; value?: number; onClick: () => void }) {
  return (
    <button onClick={onClick} className="flex min-h-[5.5rem] items-center justify-between gap-3 bg-surface px-4 py-3 text-left hover:bg-surface-2 focus-visible:z-10">
      <span className="text-meta text-muted-foreground">{label}</span>
      {value === undefined ? <Skeleton className="h-6 w-10" /> : <span className="text-title font-semibold tabular-nums">{value}</span>}
    </button>
  );
}

function PeriodMetric({ label, value }: { label: string; value?: number }) {
  return (
    <div className="flex items-center justify-between gap-3 py-2.5 first:pt-0 last:pb-0">
      <dt className="text-meta text-muted-foreground">{label}</dt>
      <dd className="text-meta font-medium tabular-nums">{value === undefined ? <Skeleton className="h-4 w-8" /> : value}</dd>
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
      <button onClick={onOpen} className="flex min-h-[4.5rem] w-full flex-col gap-2 px-4 py-3 text-left hover:bg-surface-2 sm:flex-row sm:items-center sm:justify-between">
        <span className="min-w-0 flex-1">
          <span className="flex flex-wrap items-center gap-2">
            <span className="font-mono text-xs text-muted-foreground">{ticketLabel(ticket.TicketNo)}</span>
            <span className={cn("rounded px-1.5 py-0.5 text-2xs font-medium", tone)}>{ticket.AttentionState}</span>
            {ticket.Priority && <span className="text-2xs text-subtle-foreground">{ticket.Priority}</span>}
          </span>
          <span className="mt-1 line-clamp-2 block text-meta font-medium">{ticket.BriefDetails}</span>
        </span>
        <span className="flex shrink-0 gap-4 text-2xs text-subtle-foreground sm:text-right">
          <span><Clock3 className="mr-1 inline size-3" aria-hidden />open {ago(ticket.CreatedOn)}</span>
          <span>updated {ago(ticket.LastProgressOn)}</span>
        </span>
      </button>
    </li>
  );
}
