"use client";

import { useEffect, useState } from "react";
import { ArrowRight, Bot, Headset, Radio, ShieldAlert, Users } from "lucide-react";
import { toast } from "sonner";
import { ops, type Overview, type Run } from "@/lib/api";
import { ago, outcomeLabel, ticketLabel } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/primitives";
import { Brain, type Trail } from "./brain";
import { Ranked } from "./reports";

type Go = { live: () => void; l1: () => void; runs: () => void; l3: () => void; tickets: () => void; run: (id: string) => void };

export function OverviewView({ go }: { go: Go }) {
  const [data, setData] = useState<Overview | null>(null);
  const [trail, setTrail] = useState<Trail | null>(null);

  useEffect(() => {
    const load = () => ops.overview().then(setData).catch((e: Error) => toast.error(e.message));
    load();
    const poll = setInterval(load, 10_000);
    return () => clearInterval(poll);
  }, []);

  const liveId = data?.live?.ID;
  useEffect(() => {
    if (liveId) ops.live(liveId).then((r) => setTrail((r.trail as Trail) ?? null)).catch(() => {});
  }, [liveId]);

  const c = data?.counts;
  const lm = (() => {
    try {
      return data?.lmStudio ? (JSON.parse(data.lmStudio.ResultJson) as { latency_s?: number; models?: string[] }) : null;
    } catch {
      return null;
    }
  })();

  return (
    <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
      <div className="mx-auto max-w-7xl space-y-6 px-4 py-6 lg:px-8">
        <div className="flex flex-wrap items-end justify-between gap-3">
          <div>
            <h1 className="text-heading font-semibold tracking-tight">Command centre</h1>
            <p className="mt-0.5 text-sm text-muted-foreground">Requesters, the L1 assistant, the L2 engineer and L3 people, in one place.</p>
          </div>
          {c && (
            <p className="flex items-center gap-2 text-meta text-muted-foreground">
              <span className={cn("size-2 rounded-full", c.ActiveRuns ? "bg-destructive motion-safe:animate-pulse" : "bg-success")} aria-hidden />
              {c.ActiveRuns ? `L2 is working on ${c.ActiveRuns} ticket${c.ActiveRuns > 1 ? "s" : ""}` : "L2 idle"} · last claim {ago(c.LastClaimOn)}
            </p>
          )}
        </div>

        <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-4">
          <Lane icon={Users} title="Requesters" onOpen={go.tickets} rows={c && [["Open tickets", c.OpenTickets], ["Waiting on them", c.WaitingOnRequester], ["New, not claimed", c.NewTickets]]} />
          <Lane icon={Headset} title="L1 · assistant" onOpen={go.l1} rows={c && [["Conversations, 24h", c.ChatsLast24h]]} note="Answers or raises a ticket" />
          <Lane icon={Bot} title="L2 · engineer" onOpen={go.runs} accent rows={c && [["Working now", c.ActiveRuns], ["Runs, 24h", c.RunsLast24h], ["Jev decisions, 24h", c.JevCallsLast24h], ["Writer calls, 24h", c.ModelCallsLast24h]]} />
          <Lane icon={ShieldAlert} title="L3 · people" onOpen={go.l3} rows={c && [["Open escalations", c.L3Open]]} note="Needs human action" />
        </div>

        <div className="grid gap-3 xl:grid-cols-3">
          <section className="overflow-hidden rounded-xl border bg-surface xl:col-span-2" aria-label="Live run">
            <div className="flex items-center gap-3 border-b px-4 py-3">
              <span className="flex items-center gap-2 text-sm font-semibold">
                <Radio className={cn("size-4", data?.live?.IsActive ? "text-destructive motion-safe:animate-pulse" : "text-subtle-foreground")} aria-hidden />
                {data?.live?.IsActive ? "L2 working now" : "Last L2 run"}
              </span>
              {data?.live && <LiveLabel run={data.live} onOpen={() => go.run(data.live!.ID)} />}
              <Button size="sm" variant="soft" className="ml-auto" onClick={go.live}>Watch live <ArrowRight /></Button>
            </div>
            <div className="h-105">{data ? <Brain trail={trail} ticketLabel={ticketLabel(data.live?.TicketNo) || "Ticket"} compact /> : <Skeleton className="m-4 h-96" />}</div>
          </section>

          <div className="space-y-3">
            <section className="rounded-xl border bg-surface p-4" aria-label="Outcomes">
              <h2 className="text-sm font-semibold">L2 outcomes</h2>
              <div className="mt-4">{data ? <Ranked rows={data.outcomes.map((o) => ({ label: outcomeLabel(o.Label), count: o.Count }))} /> : <Skeleton className="h-32" />}</div>
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
          <h2 className="border-b px-4 py-3 text-sm font-semibold">Activity</h2>
          <ol className="divide-y">
            {!data && <li className="p-4"><Skeleton className="h-40" /></li>}
            {data?.activity.map((a, i) => (
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

function LiveLabel({ run, onOpen }: { run: Run; onOpen: () => void }) {
  return (
    <button onClick={onOpen} className="min-w-0 truncate text-meta text-muted-foreground hover:text-foreground">
      <span className="font-mono">{ticketLabel(run.TicketNo)}</span> · {run.BriefDetails}
    </button>
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
