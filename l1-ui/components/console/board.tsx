"use client";

import { useEffect, useMemo, useState } from "react";
import { AlertTriangle, KanbanSquare, RefreshCw } from "lucide-react";
import { toast } from "sonner";
import { api, ops, type Board, type KanbanTask, type Ticket } from "@/lib/api";
import { ago, ticketLabel } from "@/lib/format";
import { cn } from "@/lib/utils";
import { PageTitle, Segmented } from "@/components/ui/viz";
import { Button } from "@/components/ui/button";
import { Dialog, Empty, Skeleton, StatePill, Tip } from "@/components/ui/primitives";
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
  const [open, setOpen] = useState<KanbanTask | null>(null);
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

  const columns = useMemo(() => {
    const tasks = board?.tasks ?? [];
    return COLUMNS.filter((c) => ["ready", "running", "review", "blocked", "done"].includes(c) || tasks.some((t) => t.status === c))
      .map((c) => ({ id: c, tasks: tasks.filter((t) => t.status === c).sort((a, b) => (b.completedAt ?? b.createdAt ?? 0) - (a.completedAt ?? a.createdAt ?? 0)) }));
  }, [board]);

  const runOf = (t: KanbanTask) => /run_id:\s*([0-9A-F-]{36})/i.exec(t.body)?.[1] ?? null;

  return (
    <div className="flex min-h-0 flex-1 flex-col">
      <header className="flex shrink-0 flex-wrap items-center gap-3 border-b bg-canvas px-4 py-3 lg:px-6">
        <PageTitle icon={KanbanSquare} className="flex-1" title="Board" meta={view === "kanban" ? "L2 task queue · investigations, rework and reviews" : "tickets grouped by support state"} />
        <Segmented label="Board view" value={view} onChange={setView} options={[{ id: "kanban", label: "Agent tasks" }, { id: "lifecycle", label: "Ticket lifecycle" }]} />
        <Tip label="Refresh">
          <Button variant="ghost" size="icon-sm" aria-label="Refresh" onClick={refresh} disabled={refreshing}><RefreshCw className={cn(refreshing && "animate-spin")} /></Button>
        </Tip>
      </header>

      {view === "kanban" && board?.stats && (
        <div className="flex shrink-0 gap-3 overflow-x-auto border-b bg-canvas px-4 py-2.5 lg:px-6">
          {Object.entries(board.stats.by_assignee).map(([agent, counts]) => (
            <div key={agent} className="flex items-center gap-2.5 rounded-lg border bg-background px-3 py-1.5">
              <span className="grid size-7 place-items-center rounded-md bg-signal-soft text-2xs font-bold text-signal" aria-hidden>{(AGENT[agent]?.name ?? agent).split(" ").map((w) => w[0]).join("").slice(0, 2)}</span>
              <span>
                <span className="block text-meta font-medium leading-tight">{AGENT[agent]?.name ?? agent}</span>
                <span className="block text-2xs text-subtle-foreground">{Object.entries(counts).map(([s, n]) => `${n} ${s}`).join(" · ")}</span>
              </span>
            </div>
          ))}
        </div>
      )}

      <div className="scrollbar-thin min-h-0 flex-1 overflow-auto">
        {!board && <div className="flex gap-3 p-4">{[0, 1, 2, 3].map((i) => <Skeleton key={i} className="h-96 w-72 shrink-0" />)}</div>}
        {board && !board.available && view === "kanban" && (
          <Empty icon={<KanbanSquare className="size-5" />} title="Board unavailable">The Hermes Kanban board could not be read from WSL.</Empty>
        )}
        {view === "kanban" && board?.available && (
          <div className="flex h-full gap-3 p-4 lg:px-6">
            {columns.map((c) => (
              <section key={c.id} className="flex w-72 shrink-0 flex-col rounded-xl bg-surface-2" aria-label={c.id}>
                <div className="flex items-center gap-2 px-3 py-2.5">
                  <span className={cn("size-2 rounded-full", c.id === "running" ? "bg-signal motion-safe:animate-pulse" : c.id === "blocked" ? "bg-warning" : c.id === "done" ? "bg-signal-muted" : c.id === "review" ? "bg-muted-foreground" : "bg-border-strong")} aria-hidden />
                  <h2 className="text-meta font-semibold capitalize">{c.id}</h2>
                  <span className="ml-auto text-2xs tabular-nums text-subtle-foreground">{c.tasks.length}</span>
                </div>
                <ul className="scrollbar-thin min-h-0 flex-1 space-y-2 overflow-y-auto px-2 pb-2">
                  {c.tasks.map((t) => (
                    <li key={t.id}>
                      <button onClick={() => setOpen(t)} className="w-full rounded-lg border bg-surface p-3 text-left hover:border-border-strong">
                        <span className="flex items-center gap-2">
                          <span className={cn("rounded px-1.5 py-0.5 font-mono text-2xs", kindOf(t.title) === "Review" ? "bg-surface-3 text-foreground" : kindOf(t.title) === "Rework" ? "bg-warning-soft text-warning" : "bg-signal-soft text-signal")}>{kindOf(t.title)}</span>
                          <span className="font-mono text-xs text-muted-foreground">{ticketLabel(ticketOf(t.title))}</span>
                          <span className="ml-auto text-2xs text-subtle-foreground">{age(t.completedAt ?? t.startedAt ?? t.createdAt)}</span>
                        </span>
                        <span className="mt-2 block text-2xs text-muted-foreground">{AGENT[t.assignee ?? ""]?.name ?? t.assignee ?? "Unassigned"}</span>
                        {t.status === "blocked" && (
                          <span className="mt-2 flex items-start gap-1.5 text-2xs text-warning">
                            <AlertTriangle className="mt-px size-3 shrink-0" aria-hidden />
                            <span className="line-clamp-2">{t.error && t.error !== "None" ? t.error : "Blocked: waiting on a human or evidence"}</span>
                          </span>
                        )}
                      </button>
                    </li>
                  ))}
                  {!c.tasks.length && <li className="px-2 py-6 text-center text-2xs text-subtle-foreground">Empty</li>}
                </ul>
              </section>
            ))}
          </div>
        )}
        {view === "lifecycle" && (
          <div className="flex h-full gap-3 p-4 lg:px-6">
            {LIFECYCLE.map((stage) => {
              const items = (tickets ?? []).filter((t) => t.StateLabel === stage);
              return (
                <section key={stage} className="flex w-72 shrink-0 flex-col rounded-xl bg-surface-2" aria-label={stage}>
                  <div className="flex items-center gap-2 px-3 py-2.5">
                    <h2 className="text-meta font-semibold">{LIFECYCLE_NAME[stage]}</h2>
                    <span className="ml-auto text-2xs tabular-nums text-subtle-foreground">{items.length}</span>
                  </div>
                  <ul className="scrollbar-thin min-h-0 flex-1 space-y-2 overflow-y-auto px-2 pb-2">
                    {items.map((t) => (
                      <li key={t.ID}>
                        <button onClick={() => onOpenTicket(t.ID)} className="w-full rounded-lg border bg-surface p-3 text-left hover:border-border-strong">
                          <span className="flex items-center gap-2">
                            <span className="font-mono text-xs text-muted-foreground">{ticketLabel(t.TicketNo)}</span>
                            <span className="ml-auto text-2xs text-subtle-foreground">{ago(t.ModifiedOn ?? t.CreatedOn)}</span>
                          </span>
                          <span className="mt-1.5 line-clamp-2 block text-meta leading-snug">{t.BriefDetails}</span>
                          <span className="mt-2 block text-2xs text-subtle-foreground">{t.FirstLastName}{t.Area && t.Area !== "Common" ? ` · ${t.Area}` : ""}</span>
                        </button>
                      </li>
                    ))}
                    {!items.length && <li className="px-2 py-6 text-center text-2xs text-subtle-foreground">None</li>}
                  </ul>
                </section>
              );
            })}
          </div>
        )}
      </div>

      <Dialog open={!!open} onOpenChange={(o) => !o && setOpen(null)} title={open?.title ?? ""} description={open ? `${AGENT[open.assignee ?? ""]?.name ?? open.assignee} · ${open.status} · ${open.id}` : undefined} className="max-w-2xl">
        {open && (
          <>
            <div className="flex flex-wrap gap-2">
              {open.status && <StatePill tone={open.status === "done" ? "done" : open.status === "blocked" ? "attention" : "progress"}>{open.status}</StatePill>}
              {runOf(open) && <Button size="sm" variant="outline" onClick={() => { onOpenRun(runOf(open)!); setOpen(null); }}>Open the run</Button>}
            </div>
            <InspectorBlock className="mt-3" label="Task payload" text={open.body} />
          </>
        )}
      </Dialog>
    </div>
  );
}
