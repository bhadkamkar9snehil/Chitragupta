"use client";

import { useEffect, useMemo, useState } from "react";
import { ArrowLeft, CircleDot, Ticket as TicketIcon, Headset, Inbox, MessageCircle, RotateCcw, Send, Star, User as UserIcon } from "lucide-react";
import { toast } from "sonner";
import { api, type Ticket, type TimelineItem } from "@/lib/api";
import { ago, RESPONSE_KIND, ticketLabel, when, whenShort } from "@/lib/format";
import { cn } from "@/lib/utils";
import { PageTitle } from "@/components/ui/viz";
import { Button } from "@/components/ui/button";
import { Dialog, Empty, SearchInput, Skeleton, StatePill, Tag, Textarea } from "@/components/ui/primitives";
import { useHelpdesk } from "./app";
import { RichText } from "./rich-text";

const FILTERS = [
  { id: "open", label: "Open", test: (t: Ticket) => t.StateTone !== "done" },
  { id: "reply", label: "Needs reply", test: (t: Ticket) => t.StateTone === "attention" },
  { id: "done", label: "Resolved", test: (t: Ticket) => t.StateTone === "done" },
  { id: "all", label: "All", test: () => true },
] as const;

export function Tickets() {
  const { route } = useHelpdesk();
  const selected = route.tab === "tickets" ? route.ticketId : null;
  return (
    <div className="flex min-h-0 flex-1">
      <div className={cn("flex min-h-0 w-full flex-col border-r bg-canvas lg:w-96 lg:shrink-0", selected && "hidden lg:flex")}>
        <TicketList selected={selected} />
      </div>
      <div className={cn("min-h-0 min-w-0 flex-1 flex-col", selected ? "flex" : "hidden lg:flex")}>
        {selected ? (
          <TicketDetail key={selected} id={selected} />
        ) : (
          <Empty className="m-auto" icon={<Inbox className="size-5" />} title="Select a ticket">
            Replies from the support team and anything they need from you appear here.
          </Empty>
        )}
      </div>
    </div>
  );
}

function TicketList({ selected }: { selected: string | null }) {
  const { tickets, loaded, go } = useHelpdesk();
  const [filter, setFilter] = useState<(typeof FILTERS)[number]["id"]>("open");
  const [q, setQ] = useState("");
  const shown = useMemo(
    () => tickets.filter(FILTERS.find((f) => f.id === filter)!.test).filter((t) => !q || `${t.TicketNo} ${t.BriefDetails} ${t.Area}`.toLowerCase().includes(q.toLowerCase())),
    [tickets, filter, q],
  );

  return (
    <>
      <PageTitle icon={TicketIcon} title="Tickets" meta={`${tickets.length} raised · ${tickets.filter((t) => t.StateTone !== "done").length} open`} className="mx-4 mb-3 mt-4" />
      <div className="px-4">
        <SearchInput value={q} onChange={(e) => setQ(e.target.value)} placeholder="Search number, subject, area" aria-label="Search tickets" />
      </div>
      <div className="flex gap-1 overflow-x-auto px-4 py-3" role="tablist" aria-label="Filter tickets">
        {FILTERS.map((f) => {
          const n = tickets.filter(f.test).length;
          return (
            <button
              key={f.id}
              role="tab"
              aria-selected={filter === f.id}
              onClick={() => setFilter(f.id)}
              className={cn(
                "flex h-8 shrink-0 items-center gap-1.5 rounded-md px-2.5 text-meta font-medium text-muted-foreground hover:bg-surface-2",
                filter === f.id && "bg-surface-3 text-foreground",
              )}
            >
              {f.label}
              <span className={cn("rounded px-1 text-2xs", f.id === "reply" && n > 0 ? "bg-warning text-white" : "text-subtle-foreground")}>{n}</span>
            </button>
          );
        })}
      </div>
      <ul className="scrollbar-thin min-h-0 flex-1 overflow-y-auto border-t">
        {!loaded && [0, 1, 2].map((i) => <li key={i} className="p-4"><Skeleton className="h-16" /></li>)}
        {shown.map((t) => (
          <li key={t.ID} className="border-b">
            <button
              onClick={() => go({ tab: "tickets", ticketId: t.ID })}
              aria-current={selected === t.ID ? "true" : undefined}
              className={cn("relative w-full px-4 py-3.5 text-left hover:bg-surface-2", selected === t.ID && "bg-surface-2 hover:bg-surface-2")}
            >
              {selected === t.ID && <span className="absolute inset-y-2 left-0 w-0.5 rounded-full bg-signal" aria-hidden />}
              <div className="flex items-center justify-between gap-2">
                <span className="font-mono text-xs text-muted-foreground">{ticketLabel(t.TicketNo)}</span>
                <span className="text-2xs text-subtle-foreground">{ago(t.ModifiedOn ?? t.CreatedOn)}</span>
              </div>
              <p className="mt-1 line-clamp-2 text-sm font-medium leading-snug">{t.BriefDetails}</p>
              <div className="mt-2 flex flex-wrap items-center gap-1.5">
                <StatePill tone={t.StateTone}>{t.StateLabel}</StatePill>
                {t.Area && t.Area !== "Common" && <Tag>{t.Area}</Tag>}
              </div>
            </button>
          </li>
        ))}
        {loaded && !shown.length && (
          <li>
            <Empty icon={<Inbox className="size-5" />} title={tickets.length ? "Nothing here" : "No tickets yet"}>
              {tickets.length ? "Try another filter." : "Describe a problem in Messages and we'll raise one if it needs investigation."}
            </Empty>
          </li>
        )}
      </ul>
    </>
  );
}

function TicketDetail({ id }: { id: string }) {
  const { user, go, refresh } = useHelpdesk();
  const [ticket, setTicket] = useState<Ticket | null>(null);
  const [error, setError] = useState("");
  const [answer, setAnswer] = useState("");
  const [sending, setSending] = useState(false);
  const [followUp, setFollowUp] = useState(false);

  const load = () => api.ticket(id).then(setTicket).catch((e: Error) => setError(e.message));
  useEffect(() => {
    api.ticket(id).then(setTicket).catch((e: Error) => setError(e.message));
  }, [id]);

  async function submit() {
    if (!answer.trim()) return;
    setSending(true);
    try {
      await api.answer(id, user.ID, answer.trim());
      setAnswer("");
      toast.success("Sent to the support team");
      await Promise.all([load(), refresh()]);
    } catch (e) {
      toast.error((e as Error).message);
    } finally {
      setSending(false);
    }
  }

  if (error) return <p role="alert" className="m-auto text-sm text-destructive">{error}</p>;
  if (!ticket)
    return (
      <div className="space-y-4 p-6">
        <Skeleton className="h-7 w-1/3" />
        <Skeleton className="h-4 w-1/2" />
        <Skeleton className="h-32" />
      </div>
    );

  const done = ticket.StateTone === "done";
  const rated = ticket.Timeline?.some((i) => i.Kind === "rating");
  const identifiers: string[] = (() => {
    try {
      return JSON.parse(ticket.ExtractedEntitiesJson ?? "{}").identifiers ?? [];
    } catch {
      return [];
    }
  })();

  return (
    <div className="flex min-h-0 flex-1 flex-col bg-background">
      <header className="shrink-0 border-b bg-canvas px-3 py-3 lg:px-6">
        <div className="flex items-start gap-2">
          <Button variant="ghost" size="icon-sm" className="lg:hidden" aria-label="Back to tickets" onClick={() => go({ tab: "tickets", ticketId: null })}>
            <ArrowLeft />
          </Button>
          <div className="min-w-0 flex-1">
            <div className="flex flex-wrap items-center gap-2">
              <span className="font-mono text-xs text-muted-foreground">{ticketLabel(ticket.TicketNo)}</span>
              <StatePill tone={ticket.StateTone}>{ticket.StateLabel}</StatePill>
            </div>
            <h2 className="mt-1 text-title font-semibold leading-snug tracking-tight">{ticket.BriefDetails}</h2>
          </div>
          {ticket.SessionID && (
            <Button variant="outline" size="sm" onClick={() => go({ tab: "messages", sessionId: ticket.SessionID! })}>
              <MessageCircle /> <span className="hidden sm:inline">Conversation</span>
            </Button>
          )}
        </div>
      </header>

      <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
        <div className="mx-auto grid max-w-5xl gap-8 px-4 py-6 lg:grid-cols-4 lg:px-6">
          <div className="min-w-0 lg:col-span-3">
            {ticket.StateTone === "attention" && (
              <div className="mb-6 rounded-xl border border-warning/40 bg-warning-soft/60 p-4">
                <p className="text-sm font-semibold">The support team needs your answer</p>
                <p className="mt-1 text-sm text-muted-foreground">Reply below; the ticket goes straight back to them.</p>
              </div>
            )}

            <ol className="relative space-y-6 before:absolute before:bottom-2 before:left-3.75 before:top-2 before:w-px before:bg-border">
              {ticket.Timeline?.map((item, i) => <TimelineEntry key={i} item={item} />)}
              {!ticket.Timeline?.some((t) => t.Kind === "reply") && (
                <li className="relative flex gap-3">
                  <span className="relative z-10 grid size-8 shrink-0 place-items-center rounded-full border bg-surface text-subtle-foreground">
                    <CircleDot className="size-4 motion-safe:animate-pulse" aria-hidden />
                  </span>
                  <p className="pt-1.5 text-sm text-muted-foreground">The support team is investigating. Their reply will appear here, usually within a few hours.</p>
                </li>
              )}
            </ol>

            {!done ? (
              <form
                className="mt-8 rounded-xl border bg-surface p-3 focus-within:border-border-strong focus-within:ring-2 focus-within:ring-ring"
                onSubmit={(e) => {
                  e.preventDefault();
                  submit();
                }}
              >
                <label htmlFor="answer" className="sr-only">Reply to the support team</label>
                <textarea
                  id="answer"
                  value={answer}
                  onChange={(e) => setAnswer(e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) submit();
                  }}
                  rows={3}
                  placeholder={ticket.StateTone === "attention" ? "Answer the support team's question…" : "Add information: heat numbers, times, what you see on screen…"}
                  className="w-full resize-none bg-transparent px-1 text-base outline-none focus-visible:outline-none placeholder:text-subtle-foreground sm:text-body"
                />
                <div className="flex items-center justify-between">
                  <span className="hidden text-2xs text-subtle-foreground sm:inline">Ctrl+Enter to send</span>
                  <Button type="submit" size="sm" disabled={!answer.trim() || sending}>
                    <Send /> {sending ? "Sending…" : "Send reply"}
                  </Button>
                </div>
              </form>
            ) : (
              <div className="mt-8 space-y-3">
                {!rated && <RateTicket ticket={ticket} onDone={load} />}
                <div className="flex flex-wrap items-center justify-between gap-3 rounded-xl border bg-surface p-4">
                  <p className="text-sm text-muted-foreground">Problem back, or not really fixed?</p>
                  <Button variant="outline" size="sm" onClick={() => setFollowUp(true)}>
                    <RotateCcw /> Still not fixed
                  </Button>
                </div>
              </div>
            )}
          </div>

          <aside className="space-y-5 text-sm lg:border-l lg:pl-6" aria-label="Ticket details">
            <Detail label="Raised">{whenShort(ticket.CreatedOn)}</Detail>
            <Detail label="Last update">{whenShort(ticket.ModifiedOn ?? ticket.CreatedOn)}</Detail>
            {ticket.FirstReplyOn && <Detail label="First reply">{whenShort(ticket.FirstReplyOn)}</Detail>}
            <Detail label="Area">{ticket.Area ?? "—"}</Detail>
            <Detail label="Type">{ticket.Type ?? "—"}</Detail>
            <Detail label="Priority">{ticket.Priority?.replace(" Priority", "") ?? "Standard"}</Detail>
            {identifiers.length > 0 && (
              <Detail label="Identifiers">
                <div className="flex flex-wrap gap-1">
                  {identifiers.map((i) => <Tag key={i} mono>{i}</Tag>)}
                </div>
              </Detail>
            )}
          </aside>
        </div>
      </div>

      <FollowUpDialog
        open={followUp}
        onOpenChange={setFollowUp}
        ticket={ticket}
        onCreated={async (t) => {
          toast.success(`${ticketLabel(t.TicketNo)} raised`, { description: `Linked to ${ticketLabel(ticket.TicketNo)}.` });
          await refresh();
          go({ tab: "tickets", ticketId: t.ID });
        }}
      />
    </div>
  );
}

function Detail({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div>
      <p className="text-2xs font-semibold uppercase tracking-wider text-subtle-foreground">{label}</p>
      <div className="mt-1 whitespace-nowrap">{children}</div>
    </div>
  );
}

function TimelineEntry({ item }: { item: TimelineItem }) {
  const support = item.Actor === "support";
  const heading =
    item.Kind === "created" ? "You reported" :
    item.Kind === "reply" ? RESPONSE_KIND[item.ResponseType ?? ""] ?? "Support team" :
    item.Kind === "answer" ? "You replied" :
    item.Kind === "rating" ? "You rated the resolution" : "You reported it again";
  return (
    <li className="relative flex gap-3 animate-rise">
      <span
        className={cn(
          "relative z-10 grid size-8 shrink-0 place-items-center rounded-full border",
          support ? "border-transparent bg-signal-soft text-signal" : "bg-surface text-muted-foreground",
        )}
        aria-hidden
      >
        {support ? <Headset className="size-4" /> : item.Kind === "rating" ? <Star className="size-4" /> : <UserIcon className="size-4" />}
      </span>
      <div className="min-w-0 flex-1">
        <p className="flex flex-wrap items-baseline gap-x-2 text-meta">
          <span className="font-semibold">{support ? "Support team" : "You"}</span>
          <span className="text-muted-foreground">{heading.replace(/^You /, "")}</span>
          <span className="text-2xs text-subtle-foreground">{when(item.At)}</span>
        </p>
        {item.Kind === "rating" ? (
          <p className="mt-1 text-warning" aria-label={`${item.Rating} of 5`}>{"★".repeat(item.Rating ?? 0)}<span className="text-border-strong">{"★".repeat(5 - (item.Rating ?? 0))}</span></p>
        ) : item.Text ? (
          <div className={cn("mt-1.5 rounded-xl border p-3.5", support ? "bg-surface" : "bg-surface-2")}>
            <RichText>{item.Text}</RichText>
          </div>
        ) : null}
      </div>
    </li>
  );
}

function RateTicket({ ticket, onDone }: { ticket: Ticket; onDone: () => void }) {
  const { user } = useHelpdesk();
  const [rating, setRating] = useState(0);
  const [comment, setComment] = useState("");
  return (
    <div className="rounded-xl border bg-surface p-4">
      <p className="text-sm font-medium">How was the support on this ticket?</p>
      <div className="mt-2 flex gap-1" role="radiogroup" aria-label="Rating">
        {[1, 2, 3, 4, 5].map((n) => (
          <button key={n} role="radio" aria-checked={rating === n} aria-label={`${n} of 5`} onClick={() => setRating(n)} className={cn("grid size-9 place-items-center rounded-md text-xl hover:bg-surface-2", n <= rating ? "text-warning" : "text-border-strong")}>
            ★
          </button>
        ))}
      </div>
      {rating > 0 && (
        <div className="mt-3 animate-rise">
          <Textarea rows={2} value={comment} onChange={(e) => setComment(e.target.value)} placeholder="Anything we should know? (optional)" aria-label="Comment" />
          <div className="mt-2 flex justify-end">
            <Button
              size="sm"
              onClick={async () => {
                await api.rate(ticket.ID, user.ID, rating, comment.trim() || undefined);
                toast.success("Thanks for rating");
                onDone();
              }}
            >
              Submit rating
            </Button>
          </div>
        </div>
      )}
    </div>
  );
}

function FollowUpDialog({ open, onOpenChange, ticket, onCreated }: { open: boolean; onOpenChange: (o: boolean) => void; ticket: Ticket; onCreated: (t: Ticket) => void }) {
  const { user } = useHelpdesk();
  const [text, setText] = useState("");
  const [busy, setBusy] = useState(false);
  return (
    <Dialog open={open} onOpenChange={onOpenChange} title="Report it again" description={`We'll raise a new ticket linked to ${ticketLabel(ticket.TicketNo)} so the support team sees the history.`}>
      <form
        onSubmit={async (e) => {
          e.preventDefault();
          if (!text.trim()) return;
          setBusy(true);
          try {
            const t = await api.followUp(ticket.ID, user.ID, text.trim());
            setText("");
            onOpenChange(false);
            onCreated(t);
          } catch (err) {
            toast.error((err as Error).message);
          } finally {
            setBusy(false);
          }
        }}
      >
        <Textarea autoFocus rows={4} value={text} onChange={(e) => setText(e.target.value)} placeholder="What's still wrong? Include the heat, time, or screen." aria-label="What's still wrong" />
        <div className="mt-4 flex justify-end gap-2">
          <Button type="button" variant="outline" onClick={() => onOpenChange(false)}>Cancel</Button>
          <Button type="submit" disabled={!text.trim() || busy}>{busy ? "Raising…" : "Raise ticket"}</Button>
        </div>
      </form>
    </Dialog>
  );
}
