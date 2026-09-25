"use client";

import { useEffect, useMemo, useState } from "react";
import { AlertTriangle, KanbanSquare, RefreshCw } from "lucide-react";
import { toast } from "sonner";
import { api, ops, type Board, type KanbanTask, type Ticket } from "@/lib/api";
import { ago, ticketLabel } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Dialog, Empty, Skeleton, StatePill, Tip } from "@/components/ui/primitives";

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

export function BoardView({ onOpenTicket, onOpenRun }: { onOpenTicket: (ticketNo: string) => void; onOpenRun: (runId: string) => void }) {
  const [view, setView] = useState<"kanban" | "lifecycle">("kanban");
  const [board, setBoard] = useState<Board | null>(null);
  const [tickets, setTickets] = useState<Ticket[] | null>(null);
  const [open, setOpen] = useState<KanbanTask | null>(null);
  const [tick, setTick] = useState(0);

  useEffect(() => {
    ops.board().then(setBoard).catch((e: Error) => toast.error(e.message));
    api.admin.tickets({}).then(setTickets).catch(() => {});
  }, [tick]);

  useEffect(() => {
    const poll = setInterval(() => setTick((n) => n + 1), 15_000);
    return () => clearInterval(poll);
  }, []);

  const columns = useMemo(() => {
    const tasks = board?.tasks ?? [];
    return COLUMNS.filter((c) => ["ready", "running", "review", "blocked", "done"].includes(c) || tasks.some((t) => t.status === c))
      .map((c) => ({ id: c, tasks: tasks.filter((t) => t.status === c).sort((a, b) => (b.completedAt ?? b.createdAt ?? 0) - (a.completedAt ?? a.createdAt ?? 0)) }));
  }, [board]);

  const runOf = (t: KanbanTask) => /run_id:\s*([0-9A-F-]{36})/i.exec(t.body)?.[1] ?? null;

  return (
    <div className="flex min-h-0 flex-1 flex-col">
      <header className="flex shrink-0 flex-wrap items-center gap-3 border-b bg-surface px-4 py-3 lg:px-6">
        <div className="min-w-0 flex-1">
          <h1 className="text-title font-semibold tracking-tight">Board</h1>
          <p className="text-2xs text-subtle-foreground">{view === "kanban" ? "The L2 task queue, including investigations, rework and reviews." : "Tickets grouped by their current support state."}</p>
        </div>
        <div className="flex rounded-lg border bg-background p-0.5" role="radiogroup" aria-label="Board view">
          {(["kanban", "lifecycle"] as const).map((v) => (
            <button key={v} role="radio" aria-checked={view === v} onClick={() => setView(v)} className={cn("min-h-11 rounded-md px-3 text-meta font-medium text-muted-foreground sm:min-h-8", view === v && "bg-surface-3 text-foreground")}>
              {v === "kanban" ? "Agent tasks" : "Ticket lifecycle"}
            </button>
          ))}
        </div>
        <Tip label="Refresh">
          <Button variant="ghost" size="icon-sm" aria-label="Refresh" onClick={() => setTick((n) => n + 1)}><RefreshCw /></Button>
        </Tip>
      </header>

      {view === "kanban" && board?.stats && (
        <div className="flex shrink-0 gap-3 overflow-x-auto border-b bg-surface px-4 py-2.5 lg:px-6">
          {Object.entries(board.stats.by_assignee).map(([agent, counts]) => (
            <div key={agent} className="flex items-center gap-2.5 rounded-lg border bg-background px-3 py-1.5">
              <span className="grid size-7 place-items-center rounded-md bg-primary-soft text-2xs font-bold text-primary-soft-foreground" aria-hidden>{(AGENT[agent]?.name ?? agent).split(" ").map((w) => w[0]).join("").slice(0, 2)}</span>
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
                  <span className={cn("size-2 rounded-full", c.id === "running" ? "bg-destructive motion-safe:animate-pulse" : c.id === "blocked" ? "bg-warning" : c.id === "done" ? "bg-success" : c.id === "review" ? "bg-info" : "bg-border-strong")} aria-hidden />
                  <h2 className="text-meta font-semibold capitalize">{c.id}</h2>
                  <span className="ml-auto text-2xs tabular-nums text-subtle-foreground">{c.tasks.length}</span>
                </div>
                <ul className="scrollbar-thin min-h-0 flex-1 space-y-2 overflow-y-auto px-2 pb-2">
                  {c.tasks.map((t) => (
                    <li key={t.id}>
                      <button onClick={() => setOpen(t)} className="w-full rounded-lg border bg-surface p-3 text-left shadow-lift hover:border-border-strong">
                        <span className="flex items-center gap-2">
                          <span className={cn("rounded px-1.5 py-0.5 text-2xs font-semibold", kindOf(t.title) === "Review" ? "bg-info-soft text-info" : kindOf(t.title) === "Rework" ? "bg-warning-soft text-warning" : "bg-primary-soft text-primary-soft-foreground")}>{kindOf(t.title)}</span>
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
                        <button onClick={() => onOpenTicket(t.ID)} className="w-full rounded-lg border bg-surface p-3 text-left shadow-lift hover:border-border-strong">
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
            <pre className="scrollbar-thin mt-3 max-h-96 overflow-auto whitespace-pre-wrap break-words rounded-lg border bg-surface-2 p-3 font-mono text-2xs leading-relaxed text-muted-foreground">{open.body}</pre>
          </>
        )}
      </Dialog>
    </div>
  );
}
