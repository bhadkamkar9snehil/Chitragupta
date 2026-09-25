"use client";

import { useEffect, useState } from "react";
import { ArrowLeft, CheckCircle2, Hand, ShieldAlert, UserRound } from "lucide-react";
import { toast } from "sonner";
import { ops, type Escalation, type User } from "@/lib/api";
import { ago, displayName, outcomeLabel, ticketLabel, when } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Empty, Label, Skeleton, Switch, Tag, Textarea } from "@/components/ui/primitives";
import { RichText } from "@/components/helpdesk/rich-text";

const STATUSES = ["Open", "In progress", "Resolved"];

export function L3View({ escalationId, onSelect, engineer, askEngineer, onOpenRun, onOpenTicket }: {
  escalationId: string | null;
  onSelect: (id: string | null) => void;
  engineer: User | null;
  askEngineer: () => void;
  onOpenRun: (id: string) => void;
  onOpenTicket: (id: string) => void;
}) {
  const [status, setStatus] = useState("Open");
  const [rows, setRows] = useState<Escalation[] | null>(null);
  const [tick, setTick] = useState(0);

  useEffect(() => {
    ops.l3().then(setRows).catch((e: Error) => toast.error(e.message));
  }, [tick]);

  const shown = (rows ?? []).filter((r) => (r.L3Status ?? "Open") === status);
  const selected = rows?.find((r) => r.ID === escalationId) ?? null;
  const mine = engineer ? (rows ?? []).filter((r) => r.AssignedToUserID?.toUpperCase() === engineer.ID.toUpperCase() && r.L3Status !== "Resolved").length : 0;

  return (
    <div className="flex min-h-0 flex-1">
      <section aria-label="L3 queue" className={cn("flex min-h-0 w-full flex-col border-r bg-surface md:w-96 md:shrink-0", escalationId && "hidden md:flex")}>
        <div className="space-y-2 border-b px-3 py-3">
          <div>
            <h1 className="text-title font-semibold tracking-tight">L3 escalations</h1>
            <p className="text-2xs text-subtle-foreground">Handed over by the L2 engineer for a person to act on.{engineer && mine ? ` ${mine} assigned to you.` : ""}</p>
          </div>
          <div className="flex gap-1" role="tablist">
            {STATUSES.map((s) => (
              <button key={s} role="tab" aria-selected={status === s} onClick={() => setStatus(s)} className={cn("min-h-11 rounded-md px-2 text-meta text-muted-foreground hover:bg-surface-2 sm:min-h-7", status === s && "bg-surface-3 font-medium text-foreground")}>
                {s} <span className="text-2xs text-subtle-foreground">{(rows ?? []).filter((r) => (r.L3Status ?? "Open") === s).length}</span>
              </button>
            ))}
          </div>
        </div>
        <ul className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
          {!rows && [0, 1, 2].map((i) => <li key={i} className="border-b p-3"><Skeleton className="h-16" /></li>)}
          {shown.map((r) => (
            <li key={r.ID} className="border-b">
              <button onClick={() => onSelect(r.ID)} aria-current={escalationId === r.ID ? "true" : undefined} className={cn("relative w-full px-3 py-3 text-left hover:bg-surface-2", escalationId === r.ID && "bg-primary-soft/60 hover:bg-primary-soft/60")}>
                {escalationId === r.ID && <span className="absolute inset-y-2 left-0 w-0.5 rounded-full bg-primary" aria-hidden />}
                <span className="flex items-center gap-2">
                  <span className="font-mono text-xs text-muted-foreground">{ticketLabel(r.TicketNo)}</span>
                  <span className={cn("rounded px-1.5 py-0.5 text-2xs font-semibold", r.EscalationCategory === "UNRESOLVED" ? "bg-warning-soft text-warning" : "bg-info-soft text-info")}>
                    {r.EscalationCategory === "UNRESOLVED" ? "Unresolved by L2" : outcomeLabel(r.EscalationCategory)}
                  </span>
                  <span className="ml-auto text-2xs text-subtle-foreground">{ago(r.EscalatedOn)}</span>
                </span>
                <span className="mt-1 line-clamp-2 block text-meta leading-snug">{r.BriefDetails}</span>
                <span className="mt-1.5 flex gap-3 text-2xs text-subtle-foreground">
                  <span>{r.FirstLastName}</span>
                  {r.Area && <span>{r.Area}</span>}
                  {r.AssignedToUserID && <span className="flex items-center gap-1"><UserRound className="size-3" aria-hidden /> Assigned</span>}
                </span>
              </button>
            </li>
          ))}
          {rows && !shown.length && <li><Empty icon={<ShieldAlert className="size-5" />} title={`Nothing ${status.toLowerCase()}`}>The queue is clear here.</Empty></li>}
        </ul>
      </section>
      <div className={cn("min-h-0 min-w-0 flex-1 flex-col", escalationId ? "flex" : "hidden md:flex")}>
        {selected ? (
          <Detail key={selected.ID} e={selected} engineer={engineer} askEngineer={askEngineer} onBack={() => onSelect(null)} onChanged={() => setTick((n) => n + 1)} onOpenRun={onOpenRun} onOpenTicket={onOpenTicket} />
        ) : (
          <Empty className="m-auto" icon={<ShieldAlert className="size-5" />} title="Pick an escalation">What L2 found, what it suggests, and the actions a person needs to take.</Empty>
        )}
      </div>
    </div>
  );
}

function Detail({ e, engineer, askEngineer, onBack, onChanged, onOpenRun, onOpenTicket }: {
  e: Escalation; engineer: User | null; askEngineer: () => void; onBack: () => void; onChanged: () => void; onOpenRun: (id: string) => void; onOpenTicket: (id: string) => void;
}) {
  const [note, setNote] = useState("");
  const [visible, setVisible] = useState(false);
  const [summary, setSummary] = useState("");
  const [close, setClose] = useState(true);
  const [busy, setBusy] = useState(false);
  const resolved = e.L3Status === "Resolved";

  async function act(action: "assign" | "note" | "resolve" | "reopen", text?: string) {
    if (!engineer) return askEngineer();
    setBusy(true);
    try {
      await ops.l3Act(e.ID, { userId: engineer.ID, action, text, public: visible, closeTicket: close });
      toast.success({ assign: "Picked up", note: "Note added", resolve: "Resolved", reopen: "Reopened" }[action]);
      setNote("");
      setSummary("");
      onChanged();
    } catch (err) {
      toast.error((err as Error).message);
    } finally {
      setBusy(false);
    }
  }

  const sections = [["What the requester reported", e.BriefDetails], ["L2's problem summary", e.ProblemSummary], ["Findings", e.Findings], ["Root cause", e.RootCause], ["Suggested action", e.SuggestedAction], ["What the requester was told", e.ReplyText]] as const;

  return (
    <div className="flex min-h-0 flex-1 flex-col">
      <header className="shrink-0 border-b bg-surface px-4 py-3">
        <div className="flex items-start gap-2">
          <Button variant="ghost" size="icon-sm" className="md:hidden" aria-label="Back" onClick={onBack}><ArrowLeft /></Button>
          <div className="min-w-0 flex-1">
            <div className="flex flex-wrap items-center gap-2">
              <span className="font-mono text-xs text-muted-foreground">{ticketLabel(e.TicketNo)}</span>
              <Tag>{e.L3Status ?? "Open"}</Tag>
              <span className="text-2xs text-subtle-foreground">Escalated {when(e.EscalatedOn)}</span>
            </div>
            <h2 className="mt-1 text-title font-semibold leading-snug tracking-tight">{e.BriefDetails}</h2>
            <p className="mt-1 break-words text-xs text-muted-foreground">{e.FirstLastName} · {e.EmailID}{e.Area ? ` · ${e.Area}` : ""} · ticket {e.TicketStatus === "Closed" ? "closed" : "open"}</p>
            <div className="mt-3 flex flex-wrap gap-2">
              {e.RunID && <Button variant="outline" size="sm" onClick={() => onOpenRun(e.RunID!)}>L2 run</Button>}
              <Button variant="outline" size="sm" onClick={() => onOpenTicket(e.TicketID)}>Ticket</Button>
            </div>
          </div>
        </div>
      </header>
      <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
        <div className="mx-auto grid max-w-5xl gap-6 p-4 lg:grid-cols-5 lg:p-6">
          <div className="space-y-5 lg:col-span-3">
            {sections.filter(([, v]) => v).map(([k, v]) => (
              <section key={k}>
                <h3 className="text-2xs font-semibold uppercase tracking-wider text-subtle-foreground">{k}</h3>
                <div className="mt-1.5 rounded-xl border bg-surface p-4"><RichText compact>{String(v)}</RichText></div>
              </section>
            ))}
            {e.L3Remarks && (
              <section>
                <h3 className="text-2xs font-semibold uppercase tracking-wider text-subtle-foreground">L3 notes</h3>
                <p className="mt-1.5 whitespace-pre-wrap rounded-xl border bg-surface-2 p-4 text-sm">{e.L3Remarks}</p>
              </section>
            )}
          </div>
          <aside className="space-y-4 lg:col-span-2" aria-label="Actions">
            <div className="rounded-xl border bg-surface p-4">
              <p className="text-sm font-semibold">Owner</p>
              {e.AssignedToUserID ? (
                <p className="mt-1 text-meta text-muted-foreground">
                  {engineer && e.AssignedToUserID.toUpperCase() === engineer.ID.toUpperCase() ? "You" : "Another engineer"} · since {when(e.AssignedOn)}
                </p>
              ) : (
                <p className="mt-1 text-meta text-muted-foreground">Nobody has picked this up.</p>
              )}
              {!resolved && (!e.AssignedToUserID || !engineer || e.AssignedToUserID.toUpperCase() !== engineer.ID.toUpperCase()) && (
                <Button className="mt-3 w-full" variant="soft" disabled={busy} onClick={() => act("assign")}>
                  <Hand /> {engineer ? `Pick up as ${displayName(engineer).split(" ")[0]}` : "Choose who you are to pick up"}
                </Button>
              )}
            </div>

            <form className="rounded-xl border bg-surface p-4" onSubmit={(ev) => { ev.preventDefault(); if (note.trim()) act("note", note.trim()); }}>
              <Label htmlFor="note">Add a note</Label>
              <Textarea id="note" rows={3} className="mt-1.5" value={note} onChange={(ev) => setNote(ev.target.value)} placeholder="What you checked, who you contacted…" />
              <div className="mt-2 flex items-center justify-between gap-2">
                <label className="flex items-center gap-2 text-meta text-muted-foreground">
                  <Switch checked={visible} onCheckedChange={setVisible} aria-label="Visible to the requester" /> Requester sees it
                </label>
                <Button type="submit" size="sm" variant="outline" disabled={!note.trim() || busy}>Add note</Button>
              </div>
            </form>

            {resolved ? (
              <div className="rounded-xl border border-success/40 bg-success-soft/50 p-4">
                <p className="flex items-center gap-2 text-sm font-semibold text-success"><CheckCircle2 className="size-4" aria-hidden /> Resolved {when(e.ResolvedOn)}</p>
                {e.L3ResolutionSummary && <p className="mt-2 whitespace-pre-wrap text-sm">{e.L3ResolutionSummary}</p>}
                <Button className="mt-3" size="sm" variant="outline" disabled={busy} onClick={() => act("reopen")}>Reopen</Button>
              </div>
            ) : (
              <form className="rounded-xl border bg-surface p-4" onSubmit={(ev) => { ev.preventDefault(); if (summary.trim()) act("resolve", summary.trim()); }}>
                <Label htmlFor="resolve">Resolve</Label>
                <Textarea id="resolve" rows={4} className="mt-1.5" value={summary} onChange={(ev) => setSummary(ev.target.value)} placeholder="What was done. The requester sees this on their ticket." />
                <label className="mt-2 flex items-center gap-2 text-meta text-muted-foreground">
                  <Switch checked={close} onCheckedChange={setClose} aria-label="Close the ticket" /> Close the ticket
                </label>
                <Button type="submit" className="mt-3 w-full" disabled={!summary.trim() || busy}>
                  <CheckCircle2 /> Resolve escalation
                </Button>
              </form>
            )}
          </aside>
        </div>
      </div>
    </div>
  );
}
