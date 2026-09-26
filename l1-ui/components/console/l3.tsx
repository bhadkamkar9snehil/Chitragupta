"use client";

import { useEffect, useState } from "react";
import { ArrowLeft, CheckCircle2, ExternalLink, Hand, PanelLeftClose, PanelLeftOpen, ShieldAlert, UserRound } from "lucide-react";
import { toast } from "sonner";
import { api, ops, type Escalation, type Ticket, type User } from "@/lib/api";
import { ago, displayName, ticketLabel, when } from "@/lib/format";
import { cn } from "@/lib/utils";
import { PageTitle } from "@/components/ui/viz";
import { Button } from "@/components/ui/button";
import { Empty, Label, QueueRow, Skeleton, Switch, Tag, Textarea } from "@/components/ui/primitives";
import { Outcome } from "./runs";
import { RichText } from "@/components/helpdesk/rich-text";

const STATUSES = ["Open", "In progress", "Resolved"];

// Open escalations speak L2's outcome words ("fix known" / "cause open"); a person's progress replaces them.
// UNRESOLVED is how the escalation table records an L3_ESCALATION outcome.
function EscalationState({ e }: { e: Escalation }) {
  if (e.L3Status === "Resolved" || e.L3Status === "In progress")
    return <span className={cn("inline-flex h-6 items-center whitespace-nowrap rounded-md px-2 text-xs font-medium", e.L3Status === "Resolved" ? "bg-success-soft text-success" : "bg-signal-soft text-signal")}>{e.L3Status}</span>;
  return <Outcome type={e.EscalationCategory === "UNRESOLVED" ? "L3_ESCALATION" : e.EscalationCategory} short />;
}

function StepHeading({ n, done, title, children }: { n: number; done?: boolean; title: string; children?: React.ReactNode }) {
  return (
    <div className="flex gap-2.5">
      <span className={cn("mt-px grid size-5 shrink-0 place-items-center rounded-full font-mono text-2xs font-semibold", done ? "bg-success-soft text-success" : "bg-surface-3 text-muted-foreground")}>
        {done ? <CheckCircle2 className="size-3" aria-label="Done" /> : n}
      </span>
      <div className="min-w-0 flex-1">
        <p className="text-sm font-semibold">{title}</p>
        {children && <p className="mt-0.5 text-xs text-muted-foreground">{children}</p>}
      </div>
    </div>
  );
}

export function L3View({ escalationId, onSelect, engineer, askEngineer, onOpenRun, onOpenTicket }: {
  escalationId: string | null;
  onSelect: (id: string | null) => void;
  engineer: User | null;
  askEngineer: () => void;
  onOpenRun: (id: string) => void;
  onOpenTicket: (id: string) => void;
}) {
  // Arriving from a ticket or investigation ("ticket:<no>") filters the queue to that ticket until cleared.
  const [ticketFilter, setTicketFilter] = useState<string | null>(escalationId?.startsWith("ticket:") ? escalationId.slice(7) : null);
  const [status, setStatus] = useState("Open");
  const [rows, setRows] = useState<Escalation[] | null>(null);
  const [tick, setTick] = useState(0);
  const [collapsedEscalationId, setCollapsedEscalationId] = useState<string | null>(null);
  const drawerOpen = !escalationId || collapsedEscalationId !== escalationId;

  useEffect(() => {
    ops.l3().then(setRows).catch((e: Error) => toast.error(e.message));
  }, [tick]);


  const shown = (rows ?? []).filter((r) => (ticketFilter ? r.TicketNo === ticketFilter : (r.L3Status ?? "Open") === status));
  const selected = rows?.find((r) => r.ID === escalationId) ?? (ticketFilter && escalationId?.startsWith("ticket:") ? shown[0] ?? null : null);
  const mine = engineer ? (rows ?? []).filter((r) => r.AssignedToUserID?.toUpperCase() === engineer.ID.toUpperCase() && r.L3Status !== "Resolved").length : 0;

  return (
    <div className="flex min-h-0 flex-1">
      <section aria-label="L3 queue" className={cn("flex min-h-0 w-full flex-col border-r bg-canvas md:w-96 md:shrink-0", escalationId && !escalationId.startsWith("ticket:") && "hidden", drawerOpen && "md:flex", !drawerOpen && "md:hidden")}>
        <div className="space-y-2 border-b px-3 py-3">
          <PageTitle icon={ShieldAlert} title="L3 escalations" meta={`handed over by L2 for a person${engineer && mine ? ` · ${mine} assigned to you` : ""}`}>
          </PageTitle>
          {ticketFilter ? (
            <div className="flex items-center gap-2 rounded-lg border border-signal/40 bg-signal-soft px-3 py-2 text-meta text-signal">
              <span className="min-w-0 flex-1 truncate">Showing {ticketLabel(ticketFilter)} only · {shown.length} escalation{shown.length === 1 ? "" : "s"}</span>
              <button onClick={() => { setTicketFilter(null); onSelect(null); }} className="font-medium underline-offset-4 hover:underline">Clear filter</button>
            </div>
          ) : (
          <div className="flex gap-1" role="group" aria-label="Filter by status">
            {STATUSES.map((s) => (
              <button key={s} aria-pressed={status === s} onClick={() => setStatus(s)} className={cn("min-h-11 rounded-md px-2 text-meta text-muted-foreground hover:bg-surface-2 sm:min-h-7", status === s && "bg-surface-3 font-medium text-foreground")}>
                {s} <span className="text-2xs text-subtle-foreground">{(rows ?? []).filter((r) => (r.L3Status ?? "Open") === s).length}</span>
              </button>
            ))}
          </div>
          )}
        </div>
        <ul className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
          {!rows && [0, 1, 2].map((i) => <li key={i} className="border-b p-3"><Skeleton className="h-16" /></li>)}
          {shown.map((r) => (
            <QueueRow key={r.ID} selected={selected?.ID === r.ID} onClick={() => onSelect(r.ID)}>
                <span className="flex items-center gap-2">
                  <span className="font-mono text-xs text-muted-foreground">{ticketLabel(r.TicketNo)}</span>
                  <EscalationState e={r} />
                  <span className="ml-auto text-2xs text-subtle-foreground">{ago(r.EscalatedOn)}</span>
                </span>
                <span className="mt-1 line-clamp-2 block text-meta leading-snug">{r.BriefDetails}</span>
                <span className="mt-1.5 flex flex-wrap gap-x-3 text-2xs text-subtle-foreground">
                  <span>{r.FirstLastName}</span>
                  {r.Area && <span>{r.Area}</span>}
                  {r.AssignedToUserID && <span className="flex items-center gap-1"><UserRound className="size-3" aria-hidden /> Assigned</span>}
                </span>
            </QueueRow>
          ))}
          {rows && !shown.length && <li><Empty icon={<ShieldAlert className="size-5" />} title={ticketFilter ? `No escalation for ${ticketLabel(ticketFilter)}` : `Nothing ${status.toLowerCase()}`}>The queue is clear here.</Empty></li>}
        </ul>
      </section>
      <div className={cn("min-h-0 min-w-0 flex-1 flex-col", escalationId ? "flex" : "hidden md:flex")}>
        {selected ? (
          <Detail key={selected.ID} e={selected} engineer={engineer} askEngineer={askEngineer} onBack={() => onSelect(null)} onChanged={(updated) => {
            if (updated) setRows((current) => current?.map((x) => x.ID === updated.ID ? updated : x) ?? null);
            setTick((n) => n + 1);
          }} onOpenRun={onOpenRun} onOpenTicket={onOpenTicket} drawerOpen={drawerOpen} onDrawerToggle={() => setCollapsedEscalationId((current) => current === escalationId ? null : escalationId)} />
        ) : (
          <Empty className="m-auto" icon={<ShieldAlert className="size-5" />} title="Pick an escalation">What L2 found, what it suggests, and the actions a person needs to take.</Empty>
        )}
      </div>
    </div>
  );
}

function Detail({ e, engineer, askEngineer, onBack, onChanged, onOpenRun, onOpenTicket, drawerOpen, onDrawerToggle }: {
  e: Escalation; engineer: User | null; askEngineer: () => void; onBack: () => void; onChanged: (updated?: Escalation) => void; onOpenRun: (id: string) => void; onOpenTicket: (id: string) => void;
  drawerOpen: boolean; onDrawerToggle: () => void;
}) {
  const [note, setNote] = useState("");
  const [visible, setVisible] = useState(false);
  const [summary, setSummary] = useState("");
  const [close, setClose] = useState(true);
  const [busy, setBusy] = useState(false);
  const [showTicket, setShowTicket] = useState(false);
  const [ticket, setTicket] = useState<Ticket | null>(null);
  const [ticketLoading, setTicketLoading] = useState(false);
  const resolved = e.L3Status === "Resolved";

  async function toggleTicketContext() {
    if (showTicket) {
      setShowTicket(false);
      return;
    }
    setShowTicket(true);
    if (ticket) return;
    setTicketLoading(true);
    try {
      setTicket(await api.admin.ticket(e.TicketID));
    } catch (err) {
      toast.error((err as Error).message);
    } finally {
      setTicketLoading(false);
    }
  }

  async function act(action: "assign" | "note" | "resolve" | "reopen", text?: string) {
    if (!engineer) return askEngineer();
    setBusy(true);
    try {
      const result = await ops.l3Act(e.ID, { userId: engineer.ID, action, text, public: visible, closeTicket: close });
      toast.success({ assign: "Picked up", note: "Note added", resolve: close ? "Escalation resolved and ticket closed" : "Escalation resolved", reopen: "Reopened" }[action]);
      setNote("");
      setSummary("");
      setTicket(result.ticket);
      onChanged(result.escalation);
    } catch (err) {
      toast.error((err as Error).message);
    } finally {
      setBusy(false);
    }
  }

  // The requester's words are already the heading; L2's summary only earns a section when it says something new.
  const sameAsTitle = (v: string | null) => !v || v.trim() === (e.BriefDetails ?? "").trim();
  const sections = [["L2's problem summary", sameAsTitle(e.ProblemSummary) ? null : e.ProblemSummary], ["Findings", e.Findings], ["Root cause", e.RootCause], ["Suggested action", e.SuggestedAction], ["What the requester was told", e.ReplyText]] as const;

  return (
    <div className="flex min-h-0 flex-1 flex-col">
      <header className="shrink-0 border-b bg-canvas px-4 py-3">
        <div className="flex items-start gap-2">
          <Button variant="ghost" size="icon-sm" className="md:hidden" aria-label="Back" onClick={onBack}><ArrowLeft /></Button>
          <Button variant="ghost" size="icon-sm" className="hidden md:inline-flex" aria-label={drawerOpen ? "Hide escalation list" : "Show escalation list"} onClick={onDrawerToggle}>
            {drawerOpen ? <PanelLeftClose /> : <PanelLeftOpen />}
          </Button>
          <div className="min-w-0 flex-1">
            <div className="flex flex-wrap items-center gap-2">
              <span className="font-mono text-xs text-muted-foreground">{ticketLabel(e.TicketNo)}</span>
              <EscalationState e={e} />
              <span className="text-2xs text-subtle-foreground">Escalated {when(e.EscalatedOn)}</span>
            </div>
            <h2 className="mt-1 text-title font-semibold leading-snug tracking-tight">{e.BriefDetails}</h2>
            <p className="mt-1 break-words text-xs text-muted-foreground">{e.FirstLastName} · {e.EmailID}{e.Area ? ` · ${e.Area}` : ""} · ticket {e.TicketStatus === "Closed" ? "closed" : "open"}</p>
            <div className="mt-3 flex flex-wrap gap-2">
              <Button variant={showTicket ? "soft" : "outline"} size="sm" onClick={toggleTicketContext}>
                {showTicket ? "Hide ticket context" : "Ticket context"}
              </Button>
              {e.RunID && <Button variant="outline" size="sm" onClick={() => onOpenRun(e.RunID!)}>View L2 investigation</Button>}
              <Button variant="ghost" size="sm" onClick={() => onOpenTicket(e.TicketID)}>Open full ticket <ExternalLink /></Button>
            </div>
          </div>
        </div>
      </header>
      <div className="scrollbar-thin @container min-h-0 flex-1 overflow-y-auto">
        {showTicket && (
          <TicketContext ticket={ticket} loading={ticketLoading} onOpenFull={() => onOpenTicket(e.TicketID)} />
        )}
        <div className="mx-auto grid max-w-6xl gap-6 p-4 @3xl:grid-cols-5 @3xl:p-6">
          <div className="min-w-0 space-y-5 @3xl:col-span-3">
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
          <aside className="space-y-4 @3xl:col-span-2" aria-label="Actions">
            <div className="rounded-xl border bg-surface p-4">
              <StepHeading n={1} done={!!e.AssignedToUserID} title="Pick up">
                {e.AssignedToUserID
                  ? `${engineer && e.AssignedToUserID.toUpperCase() === engineer.ID.toUpperCase() ? "You own this" : "Another engineer owns this"} · since ${when(e.AssignedOn)}`
                  : "Nobody owns this yet. Pick it up so the team knows who is acting."}
              </StepHeading>
              {!resolved && (!e.AssignedToUserID || !engineer || e.AssignedToUserID.toUpperCase() !== engineer.ID.toUpperCase()) && (
                <Button className="mt-3 w-full" variant="soft" disabled={busy} onClick={() => act("assign")}>
                  <Hand /> {engineer ? `Pick up as ${displayName(engineer).split(" ")[0]}` : "Choose who you are to pick up"}
                </Button>
              )}
            </div>

            <form className="rounded-xl border bg-surface p-4" onSubmit={(ev) => { ev.preventDefault(); if (note.trim()) act("note", note.trim()); }}>
              <StepHeading n={2} title="Update if needed">Send the requester an update, or keep an internal note.</StepHeading>
              <Label htmlFor="note" className="sr-only">Update or internal note</Label>
              <Textarea id="note" rows={3} className="mt-3" value={note} onChange={(ev) => setNote(ev.target.value)} placeholder="What you checked, who you contacted…" />
              <div className="mt-2 flex items-center justify-between gap-2">
                <label className="flex items-center gap-2 text-meta text-muted-foreground">
                  <Switch checked={visible} onCheckedChange={setVisible} aria-label="Send update to requester" /> {visible ? "Send to requester" : "Internal only"}
                </label>
                <Button type="submit" size="sm" variant="outline" disabled={!note.trim() || busy}>{visible ? "Send update" : "Save note"}</Button>
              </div>
            </form>

            {resolved ? (
              <div className="rounded-xl border border-success/40 bg-success-soft/50 p-4">
                <StepHeading n={3} done title="Resolved">{when(e.ResolvedOn)}</StepHeading>
                {e.L3ResolutionSummary && <p className="mt-2 whitespace-pre-wrap text-sm">{e.L3ResolutionSummary}</p>}
                <Button className="mt-3" size="sm" variant="outline" disabled={busy} onClick={() => act("reopen")}>Reopen</Button>
              </div>
            ) : (
              <form className="rounded-xl border bg-surface p-4" onSubmit={(ev) => { ev.preventDefault(); if (summary.trim()) act("resolve", summary.trim()); }}>
                <StepHeading n={3} title="Resolve">The requester sees this. Close the ticket when no further support action is needed.</StepHeading>
                <Label htmlFor="resolve" className="sr-only">Resolution</Label>
                <Textarea id="resolve" rows={4} className="mt-3" value={summary} onChange={(ev) => setSummary(ev.target.value)} placeholder="What was done, what the requester should know, and any next step." />
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

function TicketContext({ ticket, loading, onOpenFull }: { ticket: Ticket | null; loading: boolean; onOpenFull: () => void }) {
  return (
    <section className="border-b bg-surface-2 px-4 py-4 lg:px-6" aria-label="Ticket context">
      <div className="mx-auto max-w-6xl">
        <div className="flex flex-wrap items-center gap-2">
          <div className="min-w-0 flex-1">
            <p className="text-2xs font-semibold uppercase tracking-wider text-subtle-foreground">Ticket context · stays inside L3</p>
            {loading ? <Skeleton className="mt-2 h-6 w-64" /> : ticket ? (
              <>
                <div className="mt-1 flex flex-wrap items-center gap-2">
                  <span className="font-mono text-xs text-muted-foreground">{ticketLabel(ticket.TicketNo)}</span>
                  <Tag>{ticket.StateLabel}</Tag>
                  <span className="text-xs text-muted-foreground">{ticket.FirstLastName || ticket.EmailID} · {ticket.Channel ?? "Other"}</span>
                </div>
                <p className="mt-1 text-sm font-medium">{ticket.BriefDetails}</p>
              </>
            ) : <p className="mt-1 text-sm text-muted-foreground">Ticket context could not be loaded.</p>}
          </div>
          <Button variant="outline" size="sm" onClick={onOpenFull}>Open full ticket <ExternalLink /></Button>
        </div>
        {ticket?.Timeline?.length ? (
          <ol className="mt-3 grid gap-2 @3xl:grid-cols-3">
            {ticket.Timeline.slice(-3).map((item, i) => (
              <li key={i} className="rounded-lg border bg-surface p-3">
                <p className="text-2xs text-subtle-foreground">{item.Actor === "support" ? "Support" : "Requester"} · {when(item.At)}</p>
                <p className="mt-1 line-clamp-3 text-xs">{item.Text || "No text"}</p>
              </li>
            ))}
          </ol>
        ) : null}
      </div>
    </section>
  );
}

