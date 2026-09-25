"use client";

import { useEffect, useState } from "react";
import { ArrowLeft, MessagesSquare } from "lucide-react";
import { toast } from "sonner";
import { api, type Message, type Session } from "@/lib/api";
import { ago, ticketLabel } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Avatar, Empty, SearchInput, Skeleton, Tag } from "@/components/ui/primitives";
import { Transcript } from "./inbox";

const FILTERS = [
  { id: "", label: "All" },
  { id: "answered", label: "Answered" },
  { id: "ticket", label: "Ticket raised" },
  { id: "negative", label: "Not helpful" },
];

export function ConversationsView({ sessionId, onSelect, onOpenTicket }: { sessionId: string | null; onSelect: (id: string | null) => void; onOpenTicket: (id: string) => void }) {
  const [q, setQ] = useState("");
  const [filter, setFilter] = useState("");
  const [rows, setRows] = useState<Session[] | null>(null);

  useEffect(() => {
    const t = setTimeout(() => {
      api.admin.conversations({ q: q || undefined, filter: filter || undefined }).then(setRows).catch((e: Error) => toast.error(e.message));
    }, 200);
    return () => clearTimeout(t);
  }, [q, filter]);

  const selected = rows?.find((r) => r.ID === sessionId) ?? null;

  return (
    <div className="flex min-h-0 flex-1">
      <section aria-label="Conversations" className={cn("flex min-h-0 w-full flex-col border-r bg-surface md:w-96 md:shrink-0", sessionId && "hidden md:flex")}>
        <div className="space-y-2 border-b px-3 py-3">
          <h1 className="text-title font-semibold tracking-tight">Conversations</h1>
          <SearchInput value={q} onChange={(e) => setQ(e.target.value)} placeholder="Search titles or ticket numbers" aria-label="Search conversations" />
          <div className="flex gap-1 overflow-x-auto" role="tablist">
            {FILTERS.map((f) => (
              <button key={f.id} role="tab" aria-selected={filter === f.id} onClick={() => setFilter(f.id)} className={cn("h-7 shrink-0 rounded-md px-2 text-meta text-muted-foreground hover:bg-surface-2", filter === f.id && "bg-surface-3 font-medium text-foreground")}>
                {f.label}
              </button>
            ))}
          </div>
        </div>
        <ul className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
          {!rows && [0, 1, 2].map((i) => <li key={i} className="border-b p-3"><Skeleton className="h-12" /></li>)}
          {rows?.map((s) => (
            <li key={s.ID} className="border-b">
              <button onClick={() => onSelect(s.ID)} aria-current={sessionId === s.ID ? "true" : undefined} className={cn("relative flex w-full gap-3 px-3 py-3 text-left hover:bg-surface-2", sessionId === s.ID && "bg-primary-soft/60 hover:bg-primary-soft/60")}>
                {sessionId === s.ID && <span className="absolute inset-y-2 left-0 w-0.5 rounded-full bg-primary" aria-hidden />}
                <Avatar name={s.UserName || "?"} className="mt-0.5 size-7" />
                <span className="min-w-0 flex-1">
                  <span className="flex items-baseline gap-2">
                    <span className="truncate text-meta font-medium">{s.UserName ?? "Unknown user"}</span>
                    <span className="ml-auto shrink-0 text-2xs text-subtle-foreground">{ago(s.ModifiedOn)}</span>
                  </span>
                  <span className="mt-0.5 block truncate text-meta text-muted-foreground">{s.Title}</span>
                  <span className="mt-1.5 flex flex-wrap gap-1.5">
                    <Tag>{s.MessageCount} messages</Tag>
                    {s.TicketNo && <Tag mono>{ticketLabel(s.TicketNo)}</Tag>}
                    {s.Status === "resolved" && <Tag>Solved{s.Rating ? ` · ${s.Rating}★` : ""}</Tag>}
                    {(s.Negative ?? 0) > 0 && <span className="inline-flex h-6 items-center rounded-md bg-destructive-soft px-2 text-xs text-destructive">{s.Negative} not helpful</span>}
                  </span>
                </span>
              </button>
            </li>
          ))}
          {rows && !rows.length && <li><Empty icon={<MessagesSquare className="size-5" />} title="No conversations">Nothing matches these filters.</Empty></li>}
        </ul>
      </section>
      <div className={cn("min-h-0 min-w-0 flex-1 flex-col", sessionId ? "flex" : "hidden md:flex")}>
        {sessionId ? (
          <Detail key={sessionId} id={sessionId} session={selected} onBack={() => onSelect(null)} onOpenTicket={onOpenTicket} />
        ) : (
          <Empty className="m-auto" icon={<MessagesSquare className="size-5" />} title="Pick a conversation">Review what the assistant decided, which knowledge it used, and how long it took.</Empty>
        )}
      </div>
    </div>
  );
}

function Detail({ id, session, onBack, onOpenTicket }: { id: string; session: Session | null; onBack: () => void; onOpenTicket: (id: string) => void }) {
  const [messages, setMessages] = useState<Message[] | null>(null);
  useEffect(() => {
    api.admin.conversation(id).then(setMessages).catch((e: Error) => toast.error(e.message));
  }, [id]);
  return (
    <>
      <header className="flex h-14 shrink-0 items-center gap-2 border-b bg-surface px-4">
        <Button variant="ghost" size="icon-sm" className="md:hidden" aria-label="Back" onClick={onBack}>
          <ArrowLeft />
        </Button>
        <div className="min-w-0 flex-1">
          <h2 className="truncate text-sm font-semibold">{session?.Title ?? "Conversation"}</h2>
          <p className="truncate text-xs text-muted-foreground">{session?.UserName} · {session?.UserEmail}</p>
        </div>
        {session?.TicketNo && (
          <Button
            variant="outline"
            size="sm"
            onClick={async () => {
              const t = (await api.admin.tickets({ q: session.TicketNo! })).find((x) => x.TicketNo === session.TicketNo);
              if (t) onOpenTicket(t.ID);
            }}
          >
            Open {ticketLabel(session.TicketNo)}
          </Button>
        )}
      </header>
      <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto px-4 py-6 lg:px-8">
        <div className="mx-auto max-w-3xl">{messages ? <Transcript messages={messages} /> : <Skeleton className="h-40" />}</div>
      </div>
    </>
  );
}
