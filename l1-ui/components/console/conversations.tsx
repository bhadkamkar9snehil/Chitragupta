"use client";

import { useEffect, useMemo, useState } from "react";
import { ArrowLeft, Bot, CheckCircle2, Inbox, MessagesSquare, ThumbsDown, Ticket as TicketIcon, UserRound } from "lucide-react";
import { toast } from "sonner";
import { api, type Message, type Session, type Ticket, type User } from "@/lib/api";
import { ago, outcomeLabel, ticketLabel, whenShort } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Avatar, Empty, SearchInput, Skeleton, StatePill } from "@/components/ui/primitives";
import { Attributes, IconTile } from "@/components/ui/viz";
import { ConsoleChat } from "@/components/helpdesk/app";
import { Transcript } from "./inbox";

// One place for every L1 conversation, laid out like a support inbox:
// views -> conversation list -> the conversation -> who it is and what it led to.
// Your own chats (as the acting engineer) are live and can be continued; everyone else's are read-only.

type ViewId = "mine" | "all" | "open" | "ticket" | "answered" | "negative" | "solved";
const VIEWS: { id: ViewId; label: string; icon: typeof Inbox; match: (s: Session, me: string | null) => boolean }[] = [
  { id: "mine", label: "My chats", icon: UserRound, match: (s, me) => !!me && s.UserID?.toUpperCase() === me },
  { id: "all", label: "All conversations", icon: Inbox, match: () => true },
  { id: "open", label: "Open", icon: MessagesSquare, match: (s) => s.Status !== "resolved" },
  { id: "ticket", label: "Raised a ticket", icon: TicketIcon, match: (s) => !!s.TicketNo },
  { id: "answered", label: "Answered by assistant", icon: Bot, match: (s) => !s.TicketNo },
  { id: "negative", label: "Marked not helpful", icon: ThumbsDown, match: (s) => (s.Negative ?? 0) > 0 },
  { id: "solved", label: "Solved", icon: CheckCircle2, match: (s) => s.Status === "resolved" },
];

export function ConversationsView({ sessionId, onSelect, onOpenTicket, onOpenRun, engineer, askEngineer }: {
  sessionId: string | null;
  onSelect: (id: string | null) => void;
  onOpenTicket: (id: string) => void;
  onOpenRun: (id: string) => void;
  engineer: User | null;
  askEngineer: () => void;
}) {
  const me = engineer?.ID.toUpperCase() ?? null;
  const [view, setView] = useState<ViewId>(me ? "mine" : "all");
  const [person, setPerson] = useState<string | null>(null);
  const [q, setQ] = useState("");
  const [rows, setRows] = useState<Session[] | null>(null);
  const [started, setStarted] = useState<string[]>([]);

  // Reload when the open conversation changes, so a chat you just started appears in the list.
  useEffect(() => {
    const load = () => api.admin.conversations({}).then(setRows).catch((e: Error) => toast.error(e.message));
    const first = setTimeout(load, sessionId === "new" ? 0 : 150);
    const poll = setInterval(load, 20_000);
    return () => { clearTimeout(first); clearInterval(poll); };
  }, [sessionId]);

  const all = useMemo(() => rows ?? [], [rows]);
  const current = VIEWS.find((v) => v.id === view)!;
  const shown = all.filter((s) => current.match(s, me) && (!person || s.UserID?.toUpperCase() === person)
    && (!q || `${s.Title} ${s.TicketNo} ${s.UserName} ${s.LastMessage}`.toLowerCase().includes(q.toLowerCase())));
  const people = Object.values(all.reduce<Record<string, { id: string; name: string; n: number }>>((m, s) => {
    const id = s.UserID?.toUpperCase() ?? "?";
    m[id] = { id, name: s.UserName ?? "Unknown", n: (m[id]?.n ?? 0) + 1 };
    return m;
  }, {})).sort((a, b) => b.n - a.n).slice(0, 6);
  const selected = all.find((s) => s.ID === sessionId) ?? null;
  const composing = sessionId === "new";
  const own = composing || (!!sessionId && started.includes(sessionId)) || (!!selected && !!me && selected.UserID?.toUpperCase() === me);

  return (
    <div className="flex min-h-0 flex-1">
      <aside aria-label="Conversation views" className="scrollbar-thin hidden w-60 shrink-0 flex-col overflow-y-auto border-r bg-canvas p-3 lg:flex">
        <div className="flex items-center gap-3 px-1 pb-3">
          <IconTile icon={MessagesSquare} />
          <div className="min-w-0">
            <h1 className="truncate text-title font-semibold tracking-tight">Conversations</h1>
            <p className="truncate font-mono text-2xs text-subtle-foreground">{rows ? `${all.length} with the assistant` : "loading"}</p>
          </div>
        </div>
        <p className="px-2 pb-1 pt-2 font-mono text-2xs uppercase tracking-wider text-subtle-foreground">Views</p>
        <ul className="space-y-0.5">
          {VIEWS.map((v) => (
            <li key={v.id}>
              <button
                onClick={() => { setView(v.id); setPerson(null); }}
                aria-current={view === v.id && !person ? "page" : undefined}
                className={cn("flex h-9 w-full items-center gap-2.5 rounded-lg px-2.5 text-left text-meta text-muted-foreground hover:bg-surface-2 hover:text-foreground", view === v.id && !person && "bg-surface-3 text-foreground")}
              >
                <v.icon className="size-4 shrink-0" aria-hidden />
                <span className="min-w-0 flex-1 truncate">{v.label}</span>
                <span className="font-mono text-2xs tabular-nums text-subtle-foreground">{v.id === "mine" && !me ? "—" : all.filter((s) => v.match(s, me)).length}</span>
              </button>
            </li>
          ))}
        </ul>
        {people.length > 0 && (
          <>
            <p className="px-2 pb-1 pt-5 font-mono text-2xs uppercase tracking-wider text-subtle-foreground">Requesters</p>
            <ul className="space-y-0.5">
              {people.map((p) => (
                <li key={p.id}>
                  <button
                    onClick={() => { setView("all"); setPerson(p.id); }}
                    aria-current={person === p.id ? "page" : undefined}
                    className={cn("flex h-9 w-full items-center gap-2.5 rounded-lg px-2 text-left text-meta text-muted-foreground hover:bg-surface-2 hover:text-foreground", person === p.id && "bg-surface-3 text-foreground")}
                  >
                    <Avatar name={p.name} className="size-6" />
                    <span className="min-w-0 flex-1 truncate">{p.name}</span>
                    <span className="font-mono text-2xs tabular-nums text-subtle-foreground">{p.n}</span>
                  </button>
                </li>
              ))}
            </ul>
          </>
        )}
      </aside>

      <section aria-label="Conversations" className={cn("flex min-h-0 w-full flex-col border-r bg-canvas md:w-80 md:shrink-0", sessionId && "hidden md:flex")}>
        <div className="space-y-2 border-b px-3 py-3">
          <div className="flex items-center gap-2">
            <h2 className="min-w-0 flex-1 truncate text-sm font-semibold">{person ? people.find((p) => p.id === person)?.name : current.label}</h2>
            <span className="font-mono text-2xs text-subtle-foreground">{shown.length}</span>
          </div>
          <select value={view} onChange={(e) => { setView(e.target.value as ViewId); setPerson(null); }} aria-label="View" className="h-10 w-full rounded-lg border bg-canvas px-2 text-meta lg:hidden">
            {VIEWS.map((v) => <option key={v.id} value={v.id}>{v.label}</option>)}
          </select>
          <SearchInput value={q} onChange={(e) => setQ(e.target.value)} placeholder="Search title, ticket, person" aria-label="Search conversations" />
        </div>
        <ul className="scrollbar-thin min-h-0 flex-1 overflow-y-auto p-1.5">
          {!rows && [0, 1, 2].map((i) => <li key={i} className="p-1.5"><Skeleton className="h-16" /></li>)}
          {shown.map((s) => (
            <li key={s.ID}>
              <button onClick={() => onSelect(s.ID)} aria-current={sessionId === s.ID ? "true" : undefined} className={cn("relative flex w-full gap-3 rounded-xl px-3 py-2.5 text-left hover:bg-surface-2", sessionId === s.ID && "bg-surface-3 hover:bg-surface-3")}>
                {sessionId === s.ID && <span className="absolute inset-y-2.5 left-0 w-0.5 rounded-full bg-signal" aria-hidden />}
                <Avatar name={s.UserName || "?"} className="mt-0.5 size-7" />
                <span className="min-w-0 flex-1">
                  <span className="flex items-baseline gap-2">
                    <span className="truncate text-meta font-medium">{s.Title || "New conversation"}</span>
                    <span className="ml-auto shrink-0 font-mono text-2xs text-subtle-foreground">{ago(s.ModifiedOn)}</span>
                  </span>
                  <span className="block truncate text-xs text-muted-foreground">{s.UserName ?? "Unknown"} · {s.LastMessage}</span>
                  <span className="mt-1.5 flex flex-wrap gap-1 font-mono text-2xs">
                    {s.TicketNo ? <span className="rounded bg-signal-soft px-1.5 py-0.5 text-signal">{ticketLabel(s.TicketNo)}</span> : <span className="rounded bg-surface-3 px-1.5 py-0.5 text-muted-foreground">answered</span>}
                    {s.Status === "resolved" && <span className="rounded bg-surface-3 px-1.5 py-0.5 text-muted-foreground">solved{s.Rating ? ` · ${s.Rating}★` : ""}</span>}
                    {(s.Negative ?? 0) > 0 && <span className="rounded bg-destructive-soft px-1.5 py-0.5 text-destructive">{s.Negative} not helpful</span>}
                  </span>
                </span>
              </button>
            </li>
          ))}
          {rows && !shown.length && <li><Empty icon={<MessagesSquare className="size-5" />} title="Nothing here">{view === "mine" && !me ? "Choose who you are to see your own chats." : "No conversation matches this view."}</Empty></li>}
        </ul>
      </section>

      <div className={cn("min-h-0 min-w-0 flex-1 flex-col", sessionId ? "flex" : "hidden md:flex")}>
        {composing && !engineer ? (
          <Empty className="m-auto" icon={<UserRound className="size-5" />} title="Choose who is chatting">
            Chats and the tickets they raise are recorded against an XBatch account.
            <Button size="sm" className="mt-4" onClick={askEngineer}>Choose who you are</Button>
          </Empty>
        ) : own && engineer ? (
          <ConsoleChat key={sessionId} user={engineer} embed={{ sessionId: composing ? null : sessionId, threadOnly: true, onSession: (id) => { if (id) setStarted((ids) => [...ids, id]); onSelect(id); }, onOpenTicket: (id) => (id ? onOpenTicket(id) : undefined) }} />
        ) : sessionId ? (
          <ReadOnly key={sessionId} id={sessionId} session={selected} onBack={() => onSelect(null)} />
        ) : (
          <Empty className="m-auto" icon={<MessagesSquare className="size-5" />} title="Pick a conversation">Your own chats can be continued here; anyone else&apos;s show what the assistant decided and which knowledge it used.</Empty>
        )}
      </div>

      {selected && <Details session={selected} others={all.filter((s) => s.UserID === selected.UserID && s.ID !== selected.ID).slice(0, 5)} onSelect={onSelect} onOpenTicket={onOpenTicket} onOpenRun={onOpenRun} />}
    </div>
  );
}

function ReadOnly({ id, session, onBack }: { id: string; session: Session | null; onBack: () => void }) {
  const [messages, setMessages] = useState<Message[] | null>(null);
  useEffect(() => {
    api.admin.conversation(id).then(setMessages).catch((e: Error) => toast.error(e.message));
  }, [id]);
  return (
    <>
      <header className="flex h-16 shrink-0 items-center gap-2 border-b bg-canvas px-4">
        <Button variant="ghost" size="icon-sm" className="md:hidden" aria-label="Back" onClick={onBack}><ArrowLeft /></Button>
        <div className="min-w-0 flex-1">
          <h2 className="truncate text-sm font-semibold">{session?.Title || "Conversation"}</h2>
          <p className="truncate font-mono text-2xs text-subtle-foreground">{session?.UserName ?? "requester"} · read-only · started {whenShort(session?.CreatedOn)}</p>
        </div>
      </header>
      <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto px-4 py-6 lg:px-8">
        <div className="mx-auto max-w-3xl">{messages ? <Transcript messages={messages} /> : <Skeleton className="h-40" />}</div>
      </div>
    </>
  );
}

// Right rail: who this is and what the conversation led to.
function Details({ session, others, onSelect, onOpenTicket, onOpenRun }: { session: Session; others: Session[]; onSelect: (id: string) => void; onOpenTicket: (id: string) => void; onOpenRun: (id: string) => void }) {
  const [ticket, setTicket] = useState<Ticket | null>(null);
  useEffect(() => {
    let alive = true;
    if (!session.TicketNo) return;
    api.admin.tickets({ q: session.TicketNo })
      .then((r) => r.find((t) => t.TicketNo === session.TicketNo))
      .then((t) => (t ? api.admin.ticket(t.ID) : null))
      .then((t) => { if (alive) setTicket(t); })
      .catch(() => {});
    return () => { alive = false; };
  }, [session.TicketNo]);
  const last = ticket?.Runs?.at(-1);
  const shownTicket = session.TicketNo && ticket?.TicketNo === session.TicketNo ? ticket : null;
  return (
    <aside aria-label="Conversation details" className="scrollbar-thin hidden w-80 shrink-0 space-y-5 overflow-y-auto border-l bg-canvas p-4 xl:block">
      <div className="flex items-center gap-3">
        <Avatar name={session.UserName || "?"} className="size-10" />
        <div className="min-w-0">
          <p className="truncate text-sm font-medium">{session.UserName ?? "Unknown requester"}</p>
          <p className="truncate font-mono text-2xs text-subtle-foreground">{session.UserEmail ?? "no email"}</p>
        </div>
      </div>
      <Attributes rows={[
        { k: "status", v: session.Status === "resolved" ? "solved" : "open", tone: session.Status === "resolved" ? undefined : "signal" },
        { k: "messages", v: session.MessageCount ?? "—" },
        { k: "not helpful", v: session.Negative ?? 0, tone: session.Negative ? "danger" : undefined },
        { k: "rating", v: session.Rating ? `${session.Rating} / 5` : "—" },
        { k: "started", v: whenShort(session.CreatedOn) },
      ]} />
      <div>
        <p className="pb-2 font-mono text-2xs uppercase tracking-wider text-subtle-foreground">Led to</p>
        {!session.TicketNo ? (
          <p className="rounded-xl border border-dashed p-3 text-xs text-muted-foreground">Answered by the assistant. No ticket was raised.</p>
        ) : !shownTicket ? <Skeleton className="h-24" /> : (
          <div className="space-y-2 rounded-xl border bg-surface p-3">
            <p className="flex items-center gap-2 font-mono text-xs"><span>{ticketLabel(shownTicket.TicketNo)}</span><StatePill tone={shownTicket.StateTone} className="ml-auto">{shownTicket.StateLabel}</StatePill></p>
            <p className="line-clamp-2 text-meta">{shownTicket.BriefDetails}</p>
            {last && <p className="font-mono text-2xs text-subtle-foreground">L2 #{last.AttemptNo} · {last.CompletedOn ? outcomeLabel(last.ResponseType).toLowerCase() : "working"}</p>}
            <div className="flex flex-wrap gap-2 pt-1">
              <Button size="sm" variant="outline" onClick={() => onOpenTicket(shownTicket.ID)}>Open ticket</Button>
              {last && <Button size="sm" variant="ghost" onClick={() => onOpenRun(last.ID)}>How L2 handled it</Button>}
            </div>
          </div>
        )}
      </div>
      {others.length > 0 && (
        <div>
          <p className="pb-2 font-mono text-2xs uppercase tracking-wider text-subtle-foreground">Other conversations</p>
          <ul className="space-y-1">
            {others.map((s) => (
              <li key={s.ID}>
                <button onClick={() => onSelect(s.ID)} className="flex w-full items-center gap-2 rounded-lg px-2 py-1.5 text-left hover:bg-surface-2">
                  <span className="min-w-0 flex-1 truncate text-meta">{s.Title || "Conversation"}</span>
                  <span className="shrink-0 font-mono text-2xs text-subtle-foreground">{s.TicketNo ? ticketLabel(s.TicketNo) : ago(s.ModifiedOn)}</span>
                </button>
              </li>
            ))}
          </ul>
        </div>
      )}
    </aside>
  );
}
