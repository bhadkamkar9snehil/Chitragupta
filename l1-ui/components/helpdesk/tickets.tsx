"use client";

import { useEffect, useState } from "react";
import { ArrowLeft, Inbox } from "lucide-react";
import { api, when, type Ticket, type Tone } from "@/lib/api";
import { cn } from "@/lib/utils";
import { RichText } from "./rich-text";

const TONE: Record<Tone, string> = {
  attention: "bg-primary text-primary-foreground",
  progress: "bg-accent text-accent-foreground",
  pending: "bg-muted text-muted-foreground",
  done: "bg-[var(--success-bg)] text-[var(--success-fg)]",
};

const FILTERS: { id: string; label: string; test: (t: Ticket) => boolean }[] = [
  { id: "all", label: "All", test: () => true },
  { id: "reply", label: "Needs your reply", test: (t) => t.StateTone === "attention" },
  { id: "open", label: "Open", test: (t) => t.StateTone !== "done" },
  { id: "resolved", label: "Resolved", test: (t) => t.StateTone === "done" },
];

const KIND: Record<string, string> = {
  RESOLUTION: "Resolution",
  NEEDS_HUMAN_ACTION: "Action needed by the team",
  L3_ESCALATION: "Escalated to specialist",
  UPDATE: "Update",
  QUESTION: "Question for you",
};

export function StateBadge({ ticket }: { ticket: Ticket }) {
  return <span className={cn("inline-flex rounded-full px-2 py-0.5 text-xs font-medium", TONE[ticket.StateTone])}>{ticket.StateLabel}</span>;
}

type Props = { tickets: Ticket[]; selected: string | null; onSelect: (id: string | null) => void; onChanged: () => void };

export function Tickets({ tickets, selected, onSelect, onChanged }: Props) {
  const [filter, setFilter] = useState("all");
  const shown = tickets.filter(FILTERS.find((f) => f.id === filter)!.test);

  return (
    <div className="flex min-h-0 flex-1">
      <section aria-label="Tickets" className={cn("flex min-h-0 w-full flex-col border-r lg:w-95 lg:shrink-0", selected && "hidden lg:flex")}>
        <div className="shrink-0 px-4 pb-3 pt-5">
          <h1 className="text-lg font-semibold">My tickets</h1>
          <div className="-mx-1 mt-3 flex gap-1 overflow-x-auto px-1" role="tablist" aria-label="Filter tickets">
            {FILTERS.map((f) => {
              const n = tickets.filter(f.test).length;
              return (
                <button
                  key={f.id}
                  role="tab"
                  aria-selected={filter === f.id}
                  onClick={() => setFilter(f.id)}
                  className={cn("h-9 shrink-0 rounded-full border px-3 text-sm", filter === f.id ? "border-primary bg-primary text-primary-foreground" : "hover:bg-accent")}
                >
                  {f.label} <span className="opacity-70">{n}</span>
                </button>
              );
            })}
          </div>
        </div>
        <ul className="min-h-0 flex-1 divide-y overflow-y-auto border-t">
          {shown.map((t) => (
            <li key={t.ID}>
              <button onClick={() => onSelect(t.ID)} aria-current={selected === t.ID ? "true" : undefined} className={cn("w-full px-4 py-3.5 text-left hover:bg-accent/50", selected === t.ID && "bg-accent")}>
                <div className="flex items-center justify-between gap-2">
                  <span className="text-sm font-semibold">{t.TicketNo.replace("_", " ")}</span>
                  <span className="text-xs text-muted-foreground">{when(t.CreatedOn)}</span>
                </div>
                <p className="mt-1 line-clamp-2 text-sm text-muted-foreground">{t.BriefDetails}</p>
                <div className="mt-2">
                  <StateBadge ticket={t} />
                </div>
              </button>
            </li>
          ))}
          {!shown.length && (
            <li className="flex flex-col items-center gap-2 px-6 py-16 text-center text-sm text-muted-foreground">
              <Inbox className="size-5" aria-hidden />
              {tickets.length ? "No tickets in this view." : "You have not raised any tickets yet. Describe a problem in a chat and I will raise one."}
            </li>
          )}
        </ul>
      </section>
      {selected ? (
        <TicketDetail key={selected} id={selected} onBack={() => onSelect(null)} onChanged={onChanged} />
      ) : (
        <div className="hidden flex-1 place-items-center text-sm text-muted-foreground lg:grid">Select a ticket to see the support team&apos;s replies.</div>
      )}
    </div>
  );
}

function TicketDetail({ id, onBack, onChanged }: { id: string; onBack: () => void; onChanged: () => void }) {
  const [ticket, setTicket] = useState<Ticket | null>(null);
  const [error, setError] = useState("");
  const [answer, setAnswer] = useState("");
  const [sending, setSending] = useState(false);
  const [sent, setSent] = useState(false);

  useEffect(() => {
    api.ticket(id).then(setTicket).catch((e: Error) => setError(e.message));
  }, [id]);

  async function submit() {
    if (!answer.trim()) return;
    setSending(true);
    try {
      await api.answer(id, answer.trim());
      setSent(true);
      setAnswer("");
      setTicket(await api.ticket(id));
      onChanged();
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setSending(false);
    }
  }

  return (
    <section aria-label="Ticket detail" className="min-h-0 flex-1 overflow-y-auto">
      <div className="mx-auto max-w-3xl px-4 py-5 sm:px-8">
        <button onClick={onBack} className="-ml-2 mb-3 flex h-10 items-center gap-1.5 rounded-md px-2 text-sm text-muted-foreground hover:bg-accent lg:hidden">
          <ArrowLeft className="size-4" /> All tickets
        </button>
        {error && <p role="alert" className="text-sm text-destructive">{error}</p>}
        {!ticket && !error && <p className="text-sm text-muted-foreground">Loading ticket…</p>}
        {ticket && (
          <>
            <div className="flex flex-wrap items-center gap-2">
              <h1 className="text-xl font-semibold">{ticket.TicketNo.replace("_", " ")}</h1>
              <StateBadge ticket={ticket} />
            </div>
            <dl className="mt-2 flex flex-wrap gap-x-6 gap-y-1 text-sm text-muted-foreground">
              <div className="flex gap-1.5"><dt>Raised</dt><dd className="text-foreground">{when(ticket.CreatedOn)}</dd></div>
              {ticket.Area && <div className="flex gap-1.5"><dt>Area</dt><dd className="text-foreground">{ticket.Area}</dd></div>}
              {ticket.ModifiedOn && <div className="flex gap-1.5"><dt>Last change</dt><dd className="text-foreground">{when(ticket.ModifiedOn)}</dd></div>}
            </dl>

            <h2 className="mt-8 text-xs font-semibold uppercase tracking-wide text-muted-foreground">Your report</h2>
            <p className="mt-2 whitespace-pre-wrap break-words text-base leading-relaxed">{ticket.Description || ticket.BriefDetails}</p>

            <h2 className="mt-8 text-xs font-semibold uppercase tracking-wide text-muted-foreground">Support team</h2>
            {ticket.Replies?.length ? (
              <ol className="mt-3 space-y-4 border-l pl-5">
                {ticket.Replies.map((r) => (
                  <li key={r.ID} className="relative">
                    <span aria-hidden className="absolute -left-6.25 top-1.5 size-2 rounded-full bg-primary" />
                    <p className="text-xs text-muted-foreground">
                      <span className="font-medium text-foreground">{KIND[r.ResponseType] ?? r.ResponseType}</span> · {when(r.CompletedOn)}
                    </p>
                    <div className="mt-1.5"><RichText>{r.ReplyText}</RichText></div>
                  </li>
                ))}
              </ol>
            ) : (
              <p className="mt-2 text-sm text-muted-foreground">The support team is investigating. Their reply will appear here.</p>
            )}

            {ticket.ReplyRemarks && (
              <>
                <h2 className="mt-8 text-xs font-semibold uppercase tracking-wide text-muted-foreground">Your last answer</h2>
                <p className="mt-2 whitespace-pre-wrap break-words text-base">{ticket.ReplyRemarks}</p>
              </>
            )}

            {ticket.StateTone !== "done" && (
              <form
                className="mt-8 rounded-lg border bg-card p-4"
                onSubmit={(e) => {
                  e.preventDefault();
                  submit();
                }}
              >
                <label htmlFor="answer" className="text-sm font-medium">
                  {ticket.StateTone === "attention" ? "The support team needs your answer" : "Add information for the support team"}
                </label>
                <textarea
                  id="answer"
                  value={answer}
                  onChange={(e) => {
                    setAnswer(e.target.value);
                    setSent(false);
                  }}
                  rows={3}
                  placeholder="Heat numbers, times, what you see on screen…"
                  className="mt-2 w-full resize-y rounded-md border bg-background px-3 py-2 text-base outline-none focus:ring-2 focus:ring-ring/30 sm:text-sm"
                />
                <div className="mt-2 flex items-center justify-end gap-3">
                  {sent && <span className="text-sm text-muted-foreground" role="status">Sent. The ticket is back with the support team.</span>}
                  <button type="submit" disabled={!answer.trim() || sending} className="h-10 rounded-md bg-primary px-4 text-sm font-medium text-primary-foreground disabled:opacity-40">
                    {sending ? "Sending…" : "Send"}
                  </button>
                </div>
              </form>
            )}
          </>
        )}
      </div>
    </section>
  );
}
