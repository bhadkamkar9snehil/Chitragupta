"use client";

import { useEffect, useState } from "react";
import { Bot, Cpu, Sparkles, Wrench } from "lucide-react";
import { toast } from "sonner";
import { api, ops, type AiSettings, type Board, type ToolStats } from "@/lib/api";
import { ago, describeEvent, human, ticketLabel, when } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Skeleton, Tag } from "@/components/ui/primitives";
import { AGENT } from "./board";

const ms = (v?: number | null) => (v == null ? "—" : v < 1000 ? `${Math.round(v)}ms` : `${(v / 1000).toFixed(1)}s`);
const PERMISSION: Record<string, string> = { Autonomous: "bg-success-soft text-success", RequiresApproval: "bg-warning-soft text-warning", Prohibited: "bg-destructive-soft text-destructive" };

export function AgentsView({ onOpenRun }: { onOpenRun: (id: string) => void }) {
  const [tools, setTools] = useState<ToolStats | null>(null);
  const [board, setBoard] = useState<Board | null>(null);
  const [ai, setAi] = useState<AiSettings | null>(null);

  useEffect(() => {
    ops.tools().then(setTools).catch((e: Error) => toast.error(e.message));
    ops.board().then(setBoard).catch(() => {});
    api.admin.settings().then((s) => setAi(s.ai)).catch(() => {});
  }, []);

  const maxCalls = Math.max(1, ...(tools?.tools ?? []).map((t) => t.Calls));

  return (
    <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
      <div className="mx-auto max-w-7xl space-y-6 px-4 py-6 lg:px-8">
        <div>
          <h1 className="text-heading font-semibold tracking-tight">Agents &amp; tools</h1>
          <p className="mt-0.5 text-sm text-muted-foreground">Who does the work, what each one may touch, and how the tools are behaving.</p>
        </div>

        <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-4">
          <AgentCard icon={Sparkles} name="Jev" role="Decides every step: route, which records matter, what happens next. Never writes text or SQL." accent
            lines={tools ? [`${tools.jev.reduce((a, j) => a + j.Calls, 0)} decisions`, `${tools.jev.length} kinds of decision`] : undefined} />
          {Object.entries(AGENT).map(([id, a]) => (
            <AgentCard key={id} icon={Bot} name={a.name} role={a.role}
              lines={board?.stats ? [Object.entries(board.stats.by_assignee[id] ?? {}).map(([s, n]) => `${n} ${s}`).join(" · ") || "No tasks on the board", id] : undefined} />
          ))}
          <AgentCard icon={Cpu} name="L1 assistant" role="Talks to requesters, finds XBatch knowledge, raises tickets." lines={ai ? [`Writes with ${human(ai.provider)}`, ai.model] : undefined} />
          {tools?.models.map((m) => (
            <AgentCard key={m.Model} icon={Cpu} name={`L2 writer · ${m.Model}`} role="Only phrases replies when the evidence needs reasoning." lines={[`${m.Calls} calls via ${m.Provider}`, `last ${ago(m.LastUsed)}`]} />
          ))}
        </div>

        <div className="grid gap-3 xl:grid-cols-2">
          <section className="rounded-xl border bg-surface" aria-label="Tools">
            <h2 className="flex items-center gap-2 border-b px-4 py-3 text-sm font-semibold"><Wrench className="size-4 text-subtle-foreground" aria-hidden /> Tool calls</h2>
            {!tools ? <Skeleton className="m-4 h-60" /> : (
              <table className="w-full text-meta">
                <thead className="text-left text-2xs uppercase tracking-wider text-subtle-foreground">
                  <tr><th className="px-4 py-2 font-semibold">Tool</th><th className="px-2 py-2 font-semibold">Calls</th><th className="px-2 py-2 font-semibold">Errors</th><th className="px-2 py-2 font-semibold">Avg</th><th className="px-4 py-2 text-right font-semibold">Last</th></tr>
                </thead>
                <tbody className="divide-y">
                  {tools.tools.map((t) => (
                    <tr key={t.ToolName}>
                      <td className="px-4 py-2">
                        <p>{describeEvent({ EventType: "post_tool_call", ToolName: t.ToolName, Model: null }).title}</p>
                        <div className="mt-1 h-1 rounded-full bg-surface-3"><div className="h-full rounded-full bg-primary" ref={(el) => { el?.style.setProperty("width", `${(t.Calls / maxCalls) * 100}%`); }} /></div>
                      </td>
                      <td className="px-2 py-2 tabular-nums">{t.Calls}</td>
                      <td className={cn("px-2 py-2 tabular-nums", t.Errors > 0 && "text-destructive")}>{t.Errors}</td>
                      <td className="px-2 py-2 tabular-nums">{ms(t.AvgMs)}</td>
                      <td className="px-4 py-2 text-right text-2xs text-subtle-foreground">{ago(t.LastUsed)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            )}
          </section>

          <section className="rounded-xl border bg-surface" aria-label="Jev decisions">
            <h2 className="flex items-center gap-2 border-b px-4 py-3 text-sm font-semibold"><Sparkles className="size-4 text-primary" aria-hidden /> Jev decisions by kind</h2>
            {!tools ? <Skeleton className="m-4 h-60" /> : (
              <ul className="divide-y">
                {tools.jev.map((j) => (
                  <li key={j.Stage} className="flex items-center gap-3 px-4 py-2.5 text-meta">
                    <span className="min-w-0 flex-1 truncate">{describeEvent({ EventType: "jev_system_one", ToolName: j.Stage, Model: null }).title}</span>
                    <span className="tabular-nums">{j.Calls}</span>
                    {j.Errors > 0 && <span className="text-2xs text-destructive">{j.Errors} failed</span>}
                    <span className="w-16 text-right text-2xs text-subtle-foreground">{ago(j.LastUsed)}</span>
                  </li>
                ))}
              </ul>
            )}
          </section>
        </div>

        <section className="rounded-xl border bg-surface" aria-label="Permissions">
          <h2 className="border-b px-4 py-3 text-sm font-semibold">What agents may do</h2>
          <ul className="divide-y">
            {tools?.catalog.map((c) => (
              <li key={c.ActionName} className="flex flex-wrap items-center gap-3 px-4 py-2.5 text-meta">
                <span className={cn("rounded px-1.5 py-0.5 text-2xs font-semibold", PERMISSION[c.PermissionLevel] ?? "bg-surface-3")}>{human(c.PermissionLevel.replace(/([a-z])([A-Z])/g, "$1 $2"))}</span>
                <span className="font-medium">{c.ActionCategory}</span>
                <span className="min-w-0 flex-1 truncate font-mono text-xs text-muted-foreground">{c.ActionName}</span>
              </li>
            ))}
          </ul>
        </section>

        <section className="rounded-xl border bg-surface" aria-label="SQL reads">
          <h2 className="border-b px-4 py-3 text-sm font-semibold">Recent audited SQL reads</h2>
          <div className="scrollbar-thin max-h-96 overflow-auto">
            <table className="w-full min-w-160 text-meta">
              <thead className="sticky top-0 z-10 bg-surface text-left text-2xs uppercase tracking-wider text-subtle-foreground">
                <tr>{["When", "Ticket", "Object", "Purpose", "Rows", "Time"].map((h) => <th key={h} className="px-4 py-2 font-semibold">{h}</th>)}</tr>
              </thead>
              <tbody className="divide-y">
                {tools?.sql.map((a) => (
                  <tr key={`${a.RunID}-${a.ActionNo}`}>
                    <td className="whitespace-nowrap px-4 py-2 text-2xs text-subtle-foreground">{when(a.StartedOn)}</td>
                    <td className="px-4 py-2">{a.RunID ? <button className="font-mono text-xs hover:underline" onClick={() => onOpenRun(a.RunID!)}>{ticketLabel(a.TicketNo)}</button> : "—"}</td>
                    <td className="px-4 py-2 font-mono text-xs">{a.ObjectName ?? a.OperationName}</td>
                    <td className="max-w-xs truncate px-4 py-2 text-muted-foreground">{a.Purpose}</td>
                    <td className="px-4 py-2 tabular-nums">{a.RowsAffected ?? "—"}</td>
                    <td className={cn("px-4 py-2 tabular-nums", a.ErrorMessage && "text-destructive")}>{a.ErrorMessage ? "failed" : ms(a.Ms)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      </div>
    </div>
  );
}

function AgentCard({ icon: Icon, name, role, lines, accent }: { icon: typeof Bot; name: string; role: string; lines?: string[]; accent?: boolean }) {
  return (
    <div className={cn("rounded-xl border bg-surface p-4", accent && "border-primary/40")}>
      <div className="flex items-center gap-2.5">
        <span className={cn("grid size-8 place-items-center rounded-lg", accent ? "bg-primary text-primary-foreground" : "bg-surface-3 text-muted-foreground")}><Icon className="size-4" aria-hidden /></span>
        <p className="min-w-0 truncate text-sm font-semibold">{name}</p>
      </div>
      <p className="mt-2 text-meta text-muted-foreground">{role}</p>
      {lines ? <div className="mt-3 flex flex-wrap gap-1.5">{lines.map((l) => <Tag key={l}>{l}</Tag>)}</div> : <Skeleton className="mt-3 h-6" />}
    </div>
  );
}
