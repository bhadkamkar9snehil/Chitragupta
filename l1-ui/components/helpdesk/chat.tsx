"use client";

import { useEffect, useRef, useState } from "react";
import { ArrowUp, ChevronRight } from "lucide-react";
import { api, type Message, type Session, type Ticket, type User } from "@/lib/api";
import { cn } from "@/lib/utils";
import { RichText } from "./rich-text";
import { StateBadge } from "./tickets";

const EXAMPLES = [
  "GR not happening for heat 1603945, SAP shows an order status error",
  "CCM report shows 12 billets for a heat but billet tracking shows 11",
  "The shift delay report is not showing last night's delays",
  "What is the status of my tickets?",
];

type Props = {
  user: User;
  sessionId: string | null;
  session: Session | null;
  tickets: Ticket[];
  onSessionCreated: (id: string) => void;
  onTurn: () => void;
  onOpenTicket: (ticketId: string) => void;
};

export function Chat({ user, sessionId, session, tickets, onSessionCreated, onTurn, onOpenTicket }: Props) {
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(!!sessionId);
  const [pending, setPending] = useState(false);
  const [error, setError] = useState("");
  const [draft, setDraft] = useState("");
  const idRef = useRef(sessionId);
  const endRef = useRef<HTMLDivElement>(null);
  const boxRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    if (!sessionId) return;
    api.messages(sessionId).then(setMessages).catch((e: Error) => setError(e.message)).finally(() => setLoading(false));
  }, [sessionId]);

  useEffect(() => {
    endRef.current?.scrollIntoView({ block: "end" });
  }, [messages, pending]);

  useEffect(() => {
    const box = boxRef.current;
    if (!box) return;
    box.style.height = "auto";
    box.style.height = `${Math.min(box.scrollHeight, 200)}px`;
  }, [draft]);

  const ticket = session?.TicketNo ? tickets.find((t) => t.TicketNo === session.TicketNo) : undefined;

  async function send(text: string) {
    text = text.trim();
    if (!text || pending) return;
    setError("");
    setDraft("");
    setPending(true);
    setMessages((m) => [...m, { Role: "user", Content: text, CreatedOn: new Date().toISOString() }]);
    try {
      let id = idRef.current;
      if (!id) {
        id = (await api.newSession(user.ID)).ID;
        idRef.current = id;
      }
      const turn = await api.send(id, user.ID, text);
      setMessages((m) => [...m, { Role: "assistant", Content: turn.reply, CreatedOn: new Date().toISOString() }]);
      if (!sessionId) onSessionCreated(id);
      else onTurn();
      if (turn.ticket) onTurn();
    } catch (e) {
      setError((e as Error).message);
      setDraft(text);
      setMessages((m) => m.slice(0, -1));
    } finally {
      setPending(false);
      boxRef.current?.focus();
    }
  }

  const empty = !loading && messages.length === 0;
  const firstName = (user.FullName || user.Name).split(" ")[0];

  return (
    <div className="flex min-h-0 flex-1 flex-col">
      {session && (
        <div className="hidden h-14 shrink-0 items-center gap-3 border-b px-6 md:flex">
          <h1 className="min-w-0 truncate text-sm font-medium">{session.Title || "New chat"}</h1>
        </div>
      )}
      <div className="min-h-0 flex-1 overflow-y-auto">
        <div className="mx-auto w-full max-w-3xl px-4 py-6 sm:px-6">
          {loading && <p className="text-sm text-muted-foreground">Loading conversation…</p>}
          {empty && (
            <div className="pt-16">
              <h1 className="text-2xl font-semibold tracking-tight">Hi {firstName}, what is going wrong?</h1>
              <p className="mt-2 max-w-xl text-sm text-muted-foreground">
                Describe the problem the way you would to a colleague. Mention the heat, billet, work order or screen if you know it. If it needs investigation, I will raise a ticket for the support team.
              </p>
              <div className="mt-6 grid gap-2 sm:grid-cols-2">
                {EXAMPLES.map((e) => (
                  <button key={e} onClick={() => send(e)} className="rounded-lg border bg-card px-3.5 py-3 text-left text-sm hover:border-ring/50 hover:bg-accent/40">
                    {e}
                  </button>
                ))}
              </div>
            </div>
          )}
          <ol className="space-y-5">
            {messages.map((m, i) => (
              <li key={i} className={cn("flex", m.Role === "user" ? "justify-end" : "justify-start")}>
                <div
                  className={cn(
                    "max-w-xl whitespace-pre-wrap break-words text-base leading-relaxed",
                    m.Role === "user" ? "rounded-2xl rounded-br-md bg-primary px-4 py-2.5 text-primary-foreground" : "text-foreground",
                  )}
                >
                  {m.Role === "user" ? m.Content : <RichText>{m.Content}</RichText>}
                </div>
              </li>
            ))}
            {pending && (
              <li className="flex items-center gap-2 text-sm text-muted-foreground" aria-live="polite">
                <span className="size-2 rounded-full bg-primary motion-safe:animate-pulse" aria-hidden />
                Looking into it…
              </li>
            )}
          </ol>
          {ticket && (
            <button onClick={() => onOpenTicket(ticket.ID)} className="mt-6 flex w-full items-center gap-4 rounded-lg border bg-card p-4 text-left hover:border-ring/50">
              <div className="min-w-0 flex-1">
                <div className="flex flex-wrap items-center gap-2">
                  <span className="text-sm font-semibold">{ticket.TicketNo.replace("_", " ")}</span>
                  <StateBadge ticket={ticket} />
                </div>
                <p className="mt-1 line-clamp-2 text-sm text-muted-foreground">{ticket.BriefDetails}</p>
              </div>
              <ChevronRight className="size-4 text-muted-foreground" aria-hidden />
            </button>
          )}
          <div ref={endRef} />
        </div>
      </div>
      <div className="shrink-0 px-4 pb-4 sm:px-6">
        <form
          className="mx-auto w-full max-w-3xl"
          onSubmit={(e) => {
            e.preventDefault();
            send(draft);
          }}
        >
          {error && <p role="alert" className="mb-2 text-sm text-destructive">{error}</p>}
          <div className="flex items-end gap-2 rounded-2xl border bg-card p-2 shadow-sm focus-within:ring-2 focus-within:ring-ring/30">
            <textarea
              ref={boxRef}
              value={draft}
              rows={1}
              autoFocus
              onChange={(e) => setDraft(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey && !e.nativeEvent.isComposing) {
                  e.preventDefault();
                  send(draft);
                }
              }}
              placeholder={session?.TicketNo ? "Ask about this ticket…" : "Describe what happened…"}
              aria-label="Message"
              className="max-h-50 min-h-10 flex-1 resize-none bg-transparent px-2 py-2 text-base outline-none placeholder:text-muted-foreground sm:text-base"
            />
            <button
              type="submit"
              disabled={!draft.trim() || pending}
              className="grid size-10 shrink-0 place-items-center rounded-xl bg-primary text-primary-foreground disabled:opacity-40"
              aria-label="Send"
            >
              <ArrowUp className="size-4" />
            </button>
          </div>
          <p className="mt-1.5 px-1 text-xs text-muted-foreground">Enter to send · Shift+Enter for a new line</p>
        </form>
      </div>
    </div>
  );
}
