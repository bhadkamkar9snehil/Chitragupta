"use client";

import { useEffect, useMemo, useState } from "react";
import { ArrowLeft, Bot, Database, PanelLeftClose, PanelLeftOpen, Radio } from "lucide-react";
import { toast } from "sonner";
import { api, ops, type Run, type Ticket, type TraceEvent } from "@/lib/api";
import { ago, duration, human, outcomeLabel, ticketLabel, when, whenShort } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Empty, SearchInput, Skeleton, StatePill, Tag } from "@/components/ui/primitives";
import { RichText } from "@/components/helpdesk/rich-text";
import { Json } from "./live";
import { InspectorBlock } from "./inspect";
import { InvestigationCircuit } from "./circuit";
import { PageTitle } from "@/components/ui/viz";

const OUTCOME_TONE: Record<string, string> = {
  RESOLUTION: "bg-success-soft text-success",
  NEEDS_HUMAN_ACTION: "bg-surface-3 text-foreground",
  L3_ESCALATION: "bg-warning-soft text-warning",
  UPDATE: "bg-surface-3 text-muted-foreground",
};

export function Outcome({ type, active }: { type: string | null; active?: boolean }) {
  if (active)
    return (
      <span className="inline-flex h-6 items-center gap-1.5 rounded-md bg-signal-soft px-2 font-mono text-xs text-signal">
        <Radio className="size-3 motion-safe:animate-pulse" aria-hidden /> Working
      </span>
    );
  return <span className={cn("inline-flex h-6 items-center rounded-md px-2 font-mono text-xs", OUTCOME_TONE[type ?? ""] ?? "bg-surface-3 text-muted-foreground")}>{outcomeLabel(type)}</span>;
}

export function RunsView({ runId, onSelect, onLive, onOpenTicket, onOpenL3 }: { runId: string | null; onSelect: (id: string | null) => void; onLive: (id: string) => void; onOpenTicket: (id: string) => void; onOpenL3: () => void }) {
  const [q, setQ] = useState("");
  const [outcome, setOutcome] = useState("");
  const [runs, setRuns] = useState<Run[] | null>(null);
  const [collapsedRunId, setCollapsedRunId] = useState<string | null>(null);
  const drawerOpen = !runId || collapsedRunId !== runId;

  useEffect(() => {
    const t = setTimeout(() => ops.runs(q || undefined).then(setRuns).catch((e: Error) => toast.error(e.message)), 200);
    return () => clearTimeout(t);
  }, [q]);


  const outcomes = useMemo(() => [...new Set((runs ?? []).map((r) => r.ResponseType ?? ""))], [runs]);
  const shown = (runs ?? []).filter((r) => !outcome || (r.ResponseType ?? "") === outcome);

  return (
    <div className="flex min-h-0 flex-1">
      <section aria-label="L2 investigations" className={cn("flex min-h-0 w-full flex-col border-r bg-canvas md:w-96 md:shrink-0", runId && "hidden", drawerOpen && "md:flex", !drawerOpen && "md:hidden")}>
        <div className="space-y-2 border-b px-3 py-3">
          <PageTitle icon={Bot} title="L2 investigations" meta={runs ? `${runs.length} runs · newest first` : "loading"}>
          </PageTitle>
          <SearchInput value={q} onChange={(e) => setQ(e.target.value)} placeholder="Ticket, subject or route" aria-label="Search runs" />
          <div className="flex gap-1 overflow-x-auto" role="tablist">
            {["", ...outcomes].map((o) => (
              <button key={o || "all"} role="tab" aria-selected={outcome === o} onClick={() => setOutcome(o)} className={cn("min-h-11 shrink-0 rounded-md px-2 text-meta text-muted-foreground hover:bg-surface-2 sm:min-h-7", outcome === o && "bg-surface-3 font-medium text-foreground")}>
                {o ? outcomeLabel(o) : "All"} <span className="text-2xs text-subtle-foreground">{(runs ?? []).filter((r) => !o || (r.ResponseType ?? "") === o).length}</span>
              </button>
            ))}
          </div>
        </div>
        <ul className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
          {!runs && [0, 1, 2].map((i) => <li key={i} className="border-b p-3"><Skeleton className="h-14" /></li>)}
          {shown.map((r) => (
            <li key={r.ID} className="border-b">
              <button onClick={() => onSelect(r.ID)} aria-current={runId === r.ID ? "true" : undefined} className={cn("relative w-full px-3 py-3 text-left hover:bg-surface-2", runId === r.ID && "bg-surface-2 hover:bg-surface-2")}>
                {runId === r.ID && <span className="absolute inset-y-2 left-0 w-0.5 rounded-full bg-signal" aria-hidden />}
                <span className="flex items-center gap-2">
                  <span className="font-mono text-xs text-muted-foreground">{ticketLabel(r.TicketNo)}</span>
                  <Outcome type={r.ResponseType} active={r.IsActive} />
                  <span className="ml-auto text-2xs text-subtle-foreground">{ago(r.CompletedOn ?? r.ClaimedOn ?? r.CreatedOn)}</span>
                </span>
                <span className="mt-1 line-clamp-2 block text-meta leading-snug">{r.BriefDetails}</span>
                <span className="mt-1.5 flex flex-wrap gap-x-3 text-2xs text-subtle-foreground">
                  <span>{human(r.Route) || "No route"}</span>
                  <span>{r.JevCalls} Jev</span>
                  <span>{r.SqlActions} reads</span>
                  <span>{duration(r.Seconds)}</span>
                  {r.LocalModelState && <span>Writer used</span>}
                </span>
              </button>
            </li>
          ))}
          {runs && !shown.length && <li><Empty icon={<Bot className="size-5" />} title="No runs">Nothing matches.</Empty></li>}
        </ul>
      </section>
      <div className={cn("min-h-0 min-w-0 flex-1 flex-col", runId ? "flex" : "hidden md:flex")}>
        {runId ? <RunWorkspace key={runId} id={runId} onBack={() => onSelect(null)} onLive={onLive} onOpenTicket={onOpenTicket} onOpenL3={onOpenL3} drawerOpen={drawerOpen} onDrawerToggle={() => setCollapsedRunId((current) => current === runId ? null : runId)} /> : (
          <Empty className="m-auto" icon={<Bot className="size-5" />} title="Pick a run">See how the engineer walked XBatch, what Jev decided at each step, and what it read.</Empty>
        )}
      </div>
    </div>
  );
}

const JEV_FIELDS: [keyof Run, string][] = [
  ["JevTriageJson", "Triage"], ["JevInvestigationJson", "Investigation"], ["JevReviewJson", "Review"], ["JevTraceJson", "Trace assessment"], ["JevKBCurationJson", "Knowledge curation"], ["ActionsTakenJson", "Actions taken"],
];

function RunWorkspace({ id, onBack, onLive, onOpenTicket, onOpenL3, drawerOpen, onDrawerToggle }: { id: string; onBack: () => void; onLive: (id: string) => void; onOpenTicket: (id: string) => void; onOpenL3: () => void; drawerOpen: boolean; onDrawerToggle: () => void }) {
  const [run, setRun] = useState<(Run & { Events: TraceEvent[] }) | null>(null);
  const [tab, setTab] = useState<"story" | "circuit" | "sql">("story");

  useEffect(() => {
    ops.run(id).then(setRun).catch((e: Error) => toast.error(e.message));
  }, [id]);

  if (!run) return <div className="space-y-3 p-6"><Skeleton className="h-6 w-1/3" /><Skeleton className="h-96" /></div>;

  const tabs = [
    { id: "story" as const, label: "Outcome" },
    { id: "circuit" as const, label: "How it happened" },
    { id: "sql" as const, label: "Audited reads", n: run.SqlActionList?.length ?? 0 },
  ];

  return (
    <div className="flex min-h-0 flex-1 flex-col">
      <header className="shrink-0 space-y-3 border-b bg-canvas px-4 pt-3">
        <div className="flex items-start gap-2">
          <Button variant="ghost" size="icon-sm" className="md:hidden" aria-label="Back" onClick={onBack}><ArrowLeft /></Button>
          <Button variant="ghost" size="icon-sm" className="hidden md:inline-flex" aria-label={drawerOpen ? "Hide run list" : "Show run list"} onClick={onDrawerToggle}>
            {drawerOpen ? <PanelLeftClose /> : <PanelLeftOpen />}
          </Button>
          <div className="min-w-0 flex-1">
            <div className="flex flex-wrap items-center gap-2">
              <span className="font-mono text-xs text-muted-foreground">{ticketLabel(run.TicketNo)} · attempt {run.AttemptNo}</span>
              <Outcome type={run.ResponseType} active={run.IsActive} />
            </div>
            <h2 className="mt-1 text-title font-semibold leading-snug tracking-tight">{run.BriefDetails}</h2>
            <p className="mt-1 flex flex-wrap gap-x-3 text-xs text-muted-foreground">
              <span>Route {human(run.Route) || "—"}</span>
              <span>Claimed {when(run.ClaimedOn)}</span>
              <span>Took {duration(run.Seconds)}</span>
              {run.JevReviewDecision && <span>Jev review {outcomeLabel(run.JevReviewDecision)}{run.JevReviewConfidence != null ? ` · ${Math.round(run.JevReviewConfidence * 100)}%` : ""}</span>}
              {run.LocalModelPurpose && <span>Writer · {human(run.LocalModelPurpose)}</span>}
            </p>
          </div>
          <div className="flex shrink-0 gap-2">
            {run.IsActive && <Button size="sm" variant="outline" onClick={() => onLive(run.ID)}>Follow live</Button>}
            <Button size="sm" variant="outline" onClick={() => onOpenTicket(run.TicketID)}>Open ticket</Button>
          </div>
        </div>
        <div className="scrollbar-thin my-3 flex w-fit max-w-full gap-1 overflow-x-auto rounded-xl border bg-canvas p-1" role="tablist">
          {tabs.map((x) => (
            <button key={x.id} role="tab" aria-selected={tab === x.id} onClick={() => setTab(x.id)} className={cn("flex h-10 shrink-0 items-center gap-2 whitespace-nowrap rounded-lg px-3 text-meta font-medium text-muted-foreground hover:bg-surface-2 hover:text-foreground sm:h-9", tab === x.id && "bg-foreground text-background hover:bg-foreground hover:text-background")}>
              {x.label}
              {x.n !== undefined && <span className={cn("rounded px-1.5 font-mono text-2xs tabular-nums", tab === x.id ? "bg-background/15" : "bg-surface-3")}>{x.n}</span>}
            </button>
          ))}
        </div>
      </header>
      <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
        {tab === "story" && <RunStory run={run} onOpenTicket={onOpenTicket} onOpenL3={onOpenL3} onHow={() => setTab("circuit")} />}
        {tab === "circuit" && (
          <div className="p-4 lg:p-6">
            <InvestigationCircuit run={run} events={run.Events} trail={run.Trail ?? null} live={false} titled={false} />
            {JEV_FIELDS.some(([k]) => run[k]) && (
              <details className="mt-4 rounded-xl border bg-surface">
                <summary className="cursor-pointer px-4 py-3 text-sm font-medium">Stored Jev decisions (raw)</summary>
                <div className="space-y-4 border-t p-4 text-xs">
                  {JEV_FIELDS.filter(([k]) => run[k]).map(([k, label]) => <Json key={k} label={label} text={String(run[k])} />)}
                </div>
              </details>
            )}
          </div>
        )}
        {tab === "sql" && (
          run.SqlActionList?.length ? (
            <div className="overflow-x-auto p-4 lg:p-6">
              <table className="w-full min-w-160 text-meta">
                <thead className="text-left text-2xs uppercase tracking-wider text-subtle-foreground">
                  <tr>{["#", "Object", "Purpose", "Rows", "Status", "Time"].map((h) => <th key={h} className="px-2 py-2 font-semibold">{h}</th>)}</tr>
                </thead>
                <tbody className="divide-y">
                  {run.SqlActionList.map((a) => (
                    <tr key={a.ActionNo} className="align-top">
                      <td className="px-2 py-2 tabular-nums text-subtle-foreground">{a.ActionNo}</td>
                      <td className="px-2 py-2">
                        <details>
                          <summary className="cursor-pointer font-mono text-xs">{a.ObjectName ?? a.OperationName ?? a.ActionType}</summary>
                          {a.SqlText && <InspectorBlock className="mt-2 max-w-xl" label="Executed query" text={a.SqlText} kind="sql" />}
                        </details>
                      </td>
                      <td className="px-2 py-2 text-muted-foreground">{a.Purpose}</td>
                      <td className="px-2 py-2 tabular-nums">{a.RowsAffected ?? "—"}</td>
                      <td className={cn("px-2 py-2", a.ErrorMessage && "text-destructive")}>{human(a.Status)}</td>
                      <td className="px-2 py-2 whitespace-nowrap text-subtle-foreground">{when(a.StartedOn)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : <Empty icon={<Database className="size-5" />} title="No SQL reads">This run answered without reading XBatch.</Empty>
        )}

      </div>
    </div>
  );
}

// The investigation as a story, outcome first: what happened, where it came from, what L2 found,
// what happens next. "How" (the circuit, Jev decisions, audited reads) is the next tab.
function RunStory({ run, onOpenTicket, onOpenL3, onHow }: { run: Run; onOpenTicket: (id: string) => void; onOpenL3: () => void; onHow: () => void }) {
  const [ticket, setTicket] = useState<Ticket | null>(null);
  useEffect(() => {
    let alive = true;
    api.admin.ticket(run.TicketID).then((t) => { if (alive) setTicket(t); }).catch(() => {});
    return () => { alive = false; };
  }, [run.TicketID]);

  const chat = (ticket?.Transcript ?? []).filter((m) => m.Role === "user");
  const next = run.IsActive
    ? { text: "L2 is still working on it.", tone: "signal" as const }
    : run.RequiresUserInput
      ? { text: `Waiting for ${run.FirstLastName ?? "the requester"} to answer the question in the reply.`, tone: "warn" as const }
      : run.EscalateToL3
        ? { text: "With L3 people: someone needs to pick it up and act on the findings.", tone: "warn" as const }
        : run.IsResolved
          ? { text: "Resolved. The ticket is closed unless the requester reports it again.", tone: "signal" as const }
          : run.ResponseType === "UPDATE"
            ? { text: "L2 will look again when it is next eligible.", tone: undefined }
            : { text: "No further action is recorded.", tone: undefined };

  return (
    <div className="mx-auto max-w-3xl space-y-3 p-4 lg:p-6">
      <Step n={1} title="Outcome">
        <div className="flex flex-wrap items-center gap-2">
          <Outcome type={run.ResponseType} active={run.IsActive} />
          {ticket && <StatePill tone={ticket.StateTone}>{ticket.StateLabel}</StatePill>}
          {run.CompletedOn && <span className="font-mono text-2xs text-subtle-foreground">{when(run.CompletedOn)} · took {duration(run.Seconds)}</span>}
        </div>
        {run.ReplyText ? (
          <div className="mt-3 rounded-xl border bg-canvas p-4">
            <p className="mb-2 text-xs text-subtle-foreground">What {run.FirstLastName ?? "the requester"} was told</p>
            <RichText compact>{run.ReplyText}</RichText>
          </div>
        ) : <p className="mt-3 text-sm text-muted-foreground">No reply has been published yet.</p>}
        {run.ErrorMessage && <p className="mt-3 rounded-lg bg-destructive-soft p-3 text-sm text-destructive">{run.ErrorMessage}</p>}
      </Step>

      <Step n={2} title="Where it started">
        <p className="text-sm">
          <span className="font-medium">{run.FirstLastName ?? "The requester"}</span>
          <span className="text-muted-foreground"> {chat.length ? "asked the L1 assistant" : "raised a ticket"}{ticket ? ` · ${whenShort(ticket.CreatedOn)}` : ""}</span>
        </p>
        {chat.length ? (
          <ul className="mt-2 space-y-1.5">
            {chat.slice(0, 3).map((m) => <li key={m.ID} className="rounded-lg bg-surface-3 px-3 py-2 text-sm">{m.Content}</li>)}
          </ul>
        ) : (
          <p className="mt-2 rounded-lg bg-surface-3 px-3 py-2 text-sm">{ticket?.Description || run.BriefDetails}</p>
        )}
        {chat.length > 0 && <p className="mt-2 font-mono text-2xs text-subtle-foreground">L1 raised {ticketLabel(run.TicketNo)} for L2</p>}
      </Step>

      <Step n={3} title="What L2 found">
        {run.Findings || run.RootCause ? (
          <div className="space-y-3">
            {run.RootCause && <div><p className="mb-1 text-xs text-subtle-foreground">Root cause</p><RichText compact>{run.RootCause}</RichText></div>}
            {run.Findings && <div><p className="mb-1 text-xs text-subtle-foreground">Findings</p><RichText compact>{run.Findings}</RichText></div>}
          </div>
        ) : <p className="text-sm text-muted-foreground">{run.IsActive ? "Still investigating." : "No findings were recorded."}</p>}
        <button onClick={onHow} className="mt-3 font-mono text-xs text-signal hover:underline">How it found this →</button>
      </Step>

      <Step n={4} title="What happens next" last>
        <p className={cn("text-sm", next.tone === "warn" ? "text-warning" : next.tone === "signal" ? "text-signal" : "text-foreground")}>{next.text}</p>
        {run.Resolution && <div className="mt-3"><p className="mb-1 text-xs text-subtle-foreground">Recommended action</p><RichText compact>{run.Resolution}</RichText></div>}
        <div className="mt-3 flex flex-wrap gap-2">
          <Button size="sm" variant="outline" onClick={() => onOpenTicket(run.TicketID)}>Open ticket</Button>
          {run.EscalateToL3 && <Button size="sm" onClick={onOpenL3}>Go to L3 escalations</Button>}
        </div>
      </Step>
    </div>
  );
}

function Step({ n, title, children, last }: { n: number; title: string; children: React.ReactNode; last?: boolean }) {
  return (
    <section className="relative flex gap-4">
      <div className="flex flex-col items-center">
        <span className="grid size-7 shrink-0 place-items-center rounded-full border bg-canvas font-mono text-xs">{n}</span>
        {!last && <span className="mt-1 w-px flex-1 bg-border-strong" aria-hidden />}
      </div>
      <div className="min-w-0 flex-1 pb-4">
        <h3 className="mb-2 pt-0.5 text-sm font-semibold">{title}</h3>
        {children}
      </div>
    </section>
  );
}
