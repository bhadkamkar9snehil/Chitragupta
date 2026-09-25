"use client";

import { useEffect, useMemo, useState } from "react";
import { Activity, AlertTriangle, CornerDownRight, KanbanSquare, RefreshCw, Users } from "lucide-react";
import { toast } from "sonner";
import { api, ops, type Board, type KanbanTask, type Ticket } from "@/lib/api";
import { ago, duration, outcomeLabel, ticketLabel } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Attributes, Headline, Legend, PageTitle, Panel, SegmentBar, Segmented } from "@/components/ui/viz";
import { Button } from "@/components/ui/button";
import { Dialog, Empty, Skeleton, Tip } from "@/components/ui/primitives";
import { InspectorBlock } from "./inspect";

const COLUMNS = ["triage", "todo", "ready", "running", "review", "blocked", "done"];
const LIFECYCLE = ["Being investigated", "Update posted", "With the support team", "Escalated to specialist", "Waiting for your reply", "Resolved"];
const LIFECYCLE_NAME: Record<string, string> = {
  "Being investigated": "New / L2 working", "Update posted": "Update posted", "With the support team": "Needs human action",
  "Escalated to specialist": "L3 escalated", "Waiting for your reply": "Waiting on requester", Resolved: "Resolved",
};
export const AGENT: Record<string, { name: string; role: string }> = {
  "l2-jev-investigator": { name: "Jev investigator", role: "Walks XBatch and proposes the answer" },
  "l2-reviewer-primary": { name: "Primary reviewer", role: "Checks the frozen proposal before publishing" },
  "l2-investigator": { name: "Scheduler", role: "Hosts the scout and audit cron jobs" },
};

const kindOf = (title: string) => (/^REVIEW/.test(title) ? "Review" : /^REWORK/.test(title) ? "Rework" : "Investigation");
const ticketOf = (title: string) => /Ticket_\d+/.exec(title)?.[0] ?? null;
const age = (unix: number | null) => (unix ? ago(new Date(unix * 1000).toISOString().replace("Z", "")) : "");

// Keep the last successful snapshots across route unmounts. Revisiting Board should
// paint immediately, then reconcile with Hermes in the background.
let boardSnapshot: Board | null = null;
let ticketSnapshot: Ticket[] | null = null;
let boardRequest: Promise<Board> | null = null;
let ticketRequest: Promise<Ticket[]> | null = null;

function readBoard() {
  if (boardRequest) return boardRequest;
  boardRequest = ops.board().finally(() => { boardRequest = null; });
  return boardRequest;
}

function readTickets() {
  if (ticketRequest) return ticketRequest;
  ticketRequest = api.admin.tickets({}).finally(() => { ticketRequest = null; });
  return ticketRequest;
}

export function BoardView({ onOpenTicket, onOpenRun }: { onOpenTicket: (ticketNo: string) => void; onOpenRun: (runId: string) => void }) {
  const [view, setView] = useState<"kanban" | "lifecycle">("kanban");
  const [board, setBoard] = useState<Board | null>(() => boardSnapshot);
  const [tickets, setTickets] = useState<Ticket[] | null>(() => ticketSnapshot);
  const [open, setOpen] = useState<Task | null>(null);
  const [refreshing, setRefreshing] = useState(false);

  useEffect(() => {
    let alive = true;
    const load = () => {
      readBoard()
        .then((next) => {
          boardSnapshot = next;
          if (alive) setBoard(next);
        })
        .catch((e: Error) => {
          if (alive && !boardSnapshot) toast.error(e.message);
        });
    };
    load();
    const poll = setInterval(load, 15_000);
    return () => {
      alive = false;
      clearInterval(poll);
    };
  }, []);

  useEffect(() => {
    if (view !== "lifecycle") return;
    let alive = true;
    readTickets()
      .then((next) => {
        ticketSnapshot = next;
        if (alive) setTickets(next);
      })
      .catch(() => {});
    return () => { alive = false; };
  }, [view]);

  const refresh = async () => {
    setRefreshing(true);
    try {
      if (view === "kanban") {
        const next = await readBoard();
        boardSnapshot = next;
        setBoard(next);
      } else {
        const next = await readTickets();
        ticketSnapshot = next;
        setTickets(next);
      }
    } catch (e) {
      toast.error((e as Error).message);
    } finally {
      setRefreshing(false);
    }
  };

  const tasks = useMemo(() => (board?.tasks ?? []).map((t) => ({ ...t, ...parseTask(t) })), [board]);
  const later = (t: Task) => tasks.find((o) => o.ticket === t.ticket && o.id !== t.id && (o.createdAt ?? 0) > (t.createdAt ?? 0));
  const columns = COLUMNS.filter((c) => ["ready", "running", "review", "blocked", "done"].includes(c) || tasks.some((t) => t.status === c))
    .map((c) => ({ id: c, tasks: tasks.filter((t) => t.status === c).sort((x, y) => (y.completedAt ?? y.createdAt ?? 0) - (x.completedAt ?? x.createdAt ?? 0)) }));
  const active = tasks.filter((t) => !["done", "blocked", "archived"].includes(t.status));
  const blocked = tasks.filter((t) => t.status === "blocked");
  const superseded = blocked.filter((t) => later(t));
  const stuck = blocked.filter((t) => !later(t));
  const finished = tasks.filter((t) => t.completedAt && t.startedAt);
  const avgTook = finished.length ? Math.round(finished.reduce((n, t) => n + ((t.completedAt ?? 0) - (t.startedAt ?? 0)), 0) / finished.length) : null;
  const done = tasks.filter((t) => t.status === "done").length;

  return (
    <div className="flex min-h-0 flex-1 flex-col">
      <header className="flex shrink-0 flex-wrap items-center gap-3 border-b bg-canvas px-4 py-3 lg:px-6">
        <PageTitle icon={KanbanSquare} className="flex-1" title="Board" meta={view === "kanban" ? "L2 task queue · one active run at a time · review 30 › rework 20 › new 10" : "open tickets grouped by support state"} />
        <Segmented label="Board view" value={view} onChange={setView} options={[{ id: "kanban", label: "Agent tasks" }, { id: "lifecycle", label: "Ticket lifecycle" }]} />
        <Tip label="Refresh">
          <Button variant="ghost" size="icon-sm" aria-label="Refresh" onClick={refresh} disabled={refreshing}><RefreshCw className={cn(refreshing && "animate-spin")} /></Button>
        </Tip>
      </header>

      <div className="scrollbar-thin min-h-0 flex-1 overflow-auto">
        {view === "kanban" && board?.available && (
          <div className="grid gap-3 px-4 pt-4 md:grid-cols-3 lg:px-6">
            <Panel icon={Activity} title="Queue" meta={active.length ? `${active.length} task${active.length === 1 ? "" : "s"} in flight` : "idle · nothing in flight"}>
              <Headline value={active.length} unit="active" note={`${done} done`} />
              <SegmentBar className="mt-3" label="Tasks by state" segments={[
                { label: "Running", value: tasks.filter((t) => t.status === "running").length, tone: "signal" },
                { label: "Waiting", value: active.filter((t) => t.status !== "running").length, tone: "strong" },
                { label: "Stuck", value: stuck.length, tone: "warn" },
                { label: "Superseded", value: superseded.length, tone: "hatch" },
                { label: "Done", value: done, tone: "faint" },
              ]} />
            </Panel>
            <Panel icon={AlertTriangle} title="Blocked" meta="a blocked review is expected when a rework replaced it">
              <Legend rows={[
                { label: "stuck · needs a person", value: stuck.length, tone: stuck.length ? "warn" : "faint", onClick: stuck[0] ? () => setOpen(stuck[0]) : undefined },
                { label: "superseded by a later cycle", value: superseded.length, tone: "hatch" },
              ]} />
              <p className="mt-2 truncate font-mono text-2xs text-subtle-foreground">{stuck[0]?.error && stuck[0].error !== "None" ? stuck[0].error : stuck.length ? "no error recorded" : "nothing is stuck"}</p>
            </Panel>
            <Panel icon={Users} title="Workers" meta={avgTook != null ? `avg ${duration(avgTook)} per finished task` : "worker profiles"}>
              <Legend rows={Object.entries(board.stats?.by_assignee ?? {}).map(([agent, counts]) => ({
                label: AGENT[agent]?.name.toLowerCase() ?? agent,
                value: Object.entries(counts).map(([st, n]) => `${n} ${st}`).join(" · "),
                tone: Object.keys(counts).some((st) => !["done", "blocked"].includes(st)) ? "signal" as const : "faint" as const,
              }))} />
            </Panel>
          </div>
        )}

        {!board && <div className="flex gap-3 p-4">{[0, 1, 2, 3].map((i) => <Skeleton key={i} className="h-96 w-72 shrink-0" />)}</div>}
        {board && !board.available && view === "kanban" && (
          <Empty icon={<KanbanSquare className="size-5" />} title="Board unavailable">The Hermes Kanban board could not be read from WSL.</Empty>
        )}
        {view === "kanban" && board?.available && (
          <div className="flex min-h-128 gap-3 p-4 lg:px-6">
            {columns.map((c) => c.tasks.length ? (
              <Column key={c.id} name={c.id} count={c.tasks.length} dot={STATUS_DOT[c.id]} hint={c.id === "blocked" ? `${superseded.length} superseded` : c.id === "running" ? "wip 1" : undefined}>
                {c.tasks.map((t) => <TaskCard key={t.id} task={t} next={later(t)} onOpen={() => setOpen(t)} />)}
              </Column>
            ) : (
              <section key={c.id} aria-label={`${c.id}, empty`} className="flex w-12 shrink-0 flex-col items-center gap-3 rounded-2xl border border-dashed py-3">
                <span className={cn("size-2 rounded-full", STATUS_DOT[c.id])} aria-hidden />
                <span className="font-mono text-xs text-subtle-foreground vertical-text">{c.id} · 0</span>
              </section>
            ))}
          </div>
        )}
        {view === "lifecycle" && (
          <div className="flex min-h-128 gap-3 p-4 lg:px-6">
            {LIFECYCLE.map((stage) => {
              const items = (tickets ?? []).filter((t) => t.StateLabel === stage);
              return (
                <Column key={stage} name={LIFECYCLE_NAME[stage]} count={items.length} dot={STAGE_DOT[stage] ?? "bg-border-strong"}>
                  {items.map((t) => (
                    <li key={t.ID}>
                      <button onClick={() => onOpenTicket(t.ID)} className="w-full rounded-xl border bg-canvas p-3 text-left hover:border-border-strong">
                        <span className="flex items-center gap-2 font-mono text-xs">
                          <span className="text-foreground">{ticketLabel(t.TicketNo)}</span>
                          <span className="ml-auto text-subtle-foreground">{ago(t.ModifiedOn ?? t.CreatedOn)}</span>
                        </span>
                        <span className="mt-1.5 line-clamp-2 block text-meta leading-snug">{t.BriefDetails}</span>
                        <span className="mt-2 block truncate font-mono text-2xs text-subtle-foreground">{t.FirstLastName}{t.Area && t.Area !== "Common" ? ` · ${t.Area}` : ""}</span>
                      </button>
                    </li>
                  ))}
                  {!items.length && <li className="py-8 text-center font-mono text-2xs text-subtle-foreground">none</li>}
                </Column>
              );
            })}
          </div>
        )}
      </div>

      <Dialog open={!!open} onOpenChange={(o) => !o && setOpen(null)} title={open ? `${open.kind}${open.kind !== "Investigation" ? ` · cycle ${open.cycle}` : ""} · ${ticketLabel(open.ticket)}` : ""} description={open ? `${AGENT[open.assignee ?? ""]?.name ?? open.assignee ?? "Unassigned"} · ${open.status}` : undefined} className="max-w-2xl">
        {open && (
          <div className="space-y-4">
            <div className="flex flex-wrap gap-2">
              {open.run && <Button size="sm" onClick={() => { onOpenRun(open.run!); setOpen(null); }}>How it happened</Button>}
              {open.ticketId && <Button size="sm" variant="outline" onClick={() => { onOpenTicket(open.ticketId!); setOpen(null); }}>Open ticket</Button>}
            </div>
            {open.response && (
              <div className="rounded-xl border bg-surface p-3">
                <p className="font-mono text-xs"><span className="text-signal">proposes {outcomeLabel(open.response).toLowerCase()}</span><span className="text-subtle-foreground"> · evidence {(open.evidence ?? "unknown").toLowerCase()}</span></p>
                {open.reply && <p className="mt-2 line-clamp-6 whitespace-pre-line text-meta text-muted-foreground">{open.reply}</p>}
              </div>
            )}
            <Attributes rows={[
              { k: "task", v: open.id, copy: open.id },
              { k: "status", v: open.status, tone: open.status === "blocked" ? "warn" : open.status === "done" ? undefined : "signal" },
              { k: "priority", v: `${open.priority ?? "—"} · ${PRIORITY[open.priority ?? ""] ?? "other"}` },
              { k: "created", v: age(open.createdAt) },
              { k: "took", v: open.startedAt && open.completedAt ? duration(open.completedAt - open.startedAt) : open.startedAt ? `started ${age(open.startedAt)}` : "not started" },
              ...(open.error && open.error !== "None" ? [{ k: "error", v: open.error, tone: "warn" as const }] : []),
            ]} />
            <details>
              <summary className="cursor-pointer text-xs text-subtle-foreground hover:text-foreground">Task payload</summary>
              <InspectorBlock className="mt-2" label="Task payload" text={open.body} />
            </details>
          </div>
        )}
      </Dialog>
    </div>
  );
}

type Task = KanbanTask & ReturnType<typeof parseTask>;

// The task body is "key: value" lines plus a proposal digest; read just what a person needs.
function parseTask(t: KanbanTask) {
  const field = (k: string) => new RegExp(`^-? ?${k}:\\s*(.+)$`, "m").exec(t.body)?.[1]?.trim() ?? null;
  return {
    kind: kindOf(t.title),
    cycle: Number(/\[(\d+)\]/.exec(t.title)?.[1] ?? field("review_cycle") ?? 0),
    ticket: field("ticket_no") ?? ticketOf(t.title),
    ticketId: field("ticket_id"),
    run: field("run_id"),
    response: field("response_type"),
    evidence: field("evidence_status"),
    reply: /- reply_text:\s*([\s\S]*?)(?:\n- \w+:|$)/.exec(t.body)?.[1]?.trim() ?? null,
  };
}

const PRIORITY: Record<string, string> = { "30": "review", "20": "rework", "10": "new investigation" };
const STATUS_DOT: Record<string, string> = {
  triage: "bg-border-strong", todo: "bg-border-strong", ready: "bg-muted-foreground", running: "bg-signal motion-safe:animate-pulse",
  review: "bg-muted-foreground", blocked: "bg-warning", done: "bg-signal-muted",
};
const STAGE_DOT: Record<string, string> = {
  "Being investigated": "bg-signal motion-safe:animate-pulse", "Update posted": "bg-muted-foreground", "With the support team": "bg-muted-foreground",
  "Escalated to specialist": "bg-warning", "Waiting for your reply": "bg-muted-foreground", Resolved: "bg-signal-muted",
};

function Column({ name, count, dot, hint, children }: { name: string; count: number; dot: string; hint?: string; children: React.ReactNode }) {
  return (
    <section aria-label={name} className="flex w-76 min-w-76 max-w-md shrink-0 grow flex-col rounded-2xl border bg-canvas p-1.5">
      <header className="flex items-center gap-2 px-2.5 pb-2 pt-1.5">
        <span className={cn("size-2 rounded-full", dot)} aria-hidden />
        <h2 className="text-meta font-semibold capitalize">{name}</h2>
        {hint && <span className="font-mono text-2xs text-subtle-foreground">{hint}</span>}
        <span className="ml-auto font-mono text-xs tabular-nums text-muted-foreground">{count}</span>
      </header>
      <ul className="scrollbar-thin min-h-0 flex-1 space-y-1.5 overflow-y-auto rounded-xl border bg-surface p-1.5">{children}</ul>
    </section>
  );
}

function TaskCard({ task: t, next, onOpen }: { task: Task; next?: Task; onOpen: () => void }) {
  const took = t.startedAt && t.completedAt ? t.completedAt - t.startedAt : null;
  const stale = t.status === "blocked" && !!next;
  return (
    <li>
      <button onClick={onOpen} className={cn("w-full rounded-xl border bg-canvas p-3 text-left hover:border-border-strong", t.status === "running" && "border-signal", t.status === "blocked" && !stale && "border-warning/50", stale && "opacity-60 hover:opacity-100")}>
        <span className="flex items-center gap-2 font-mono text-xs">
          <span className={cn("rounded px-1.5 py-0.5 text-2xs", t.kind === "Review" ? "bg-surface-3 text-foreground" : t.kind === "Rework" ? "bg-warning-soft text-warning" : "bg-signal-soft text-signal")}>
            {t.kind.toLowerCase()}{t.kind !== "Investigation" ? ` · c${t.cycle}` : ""}
          </span>
          <span className="text-foreground">{ticketLabel(t.ticket)}</span>
          <span className="ml-auto text-subtle-foreground">{age(t.completedAt ?? t.startedAt ?? t.createdAt)}</span>
        </span>
        {t.response && (
          <span className="mt-2 block truncate font-mono text-2xs">
            <span className="text-subtle-foreground">proposes </span>
            <span className="text-foreground">{outcomeLabel(t.response).toLowerCase()}</span>
            {t.evidence && <span className={t.evidence === "COMPLETE" ? "text-signal" : "text-warning"}> · {t.evidence.toLowerCase()}</span>}
          </span>
        )}
        <span className="mt-2 flex items-center gap-2 font-mono text-2xs text-subtle-foreground">
          <span className="truncate">{AGENT[t.assignee ?? ""]?.name.toLowerCase() ?? t.assignee ?? "unassigned"}</span>
          {took != null && <span className="ml-auto shrink-0">took {duration(took)}</span>}
        </span>
        {t.status === "blocked" && (
          <span className={cn("mt-2 flex items-start gap-1.5 text-2xs", stale ? "text-subtle-foreground" : "text-warning")}>
            {stale ? <CornerDownRight className="mt-px size-3 shrink-0" aria-hidden /> : <AlertTriangle className="mt-px size-3 shrink-0" aria-hidden />}
            <span className="line-clamp-2">{stale ? `superseded by ${next!.kind.toLowerCase()} · c${next!.cycle}` : t.error && t.error !== "None" ? t.error : "blocked · waiting on a person"}</span>
          </span>
        )}
      </button>
    </li>
  );
}
