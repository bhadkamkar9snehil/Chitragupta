"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import {
  ArrowLeft, ArrowUp, BookOpen, Check, CheckCircle2, Copy, Headset, MoreHorizontal, Pencil, Plus, Square,
  ThumbsDown, ThumbsUp, Trash2, MessageCircle, ChevronRight,
} from "lucide-react";
import { toast } from "sonner";
import { api, turn, type Message, type Session, type SourceRef, type Ticket } from "@/lib/api";
import { ago, clock, dayGroup, plain, ticketLabel } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Dialog, Empty, Input, SearchInput, Menu, MenuContent, MenuItem, MenuSeparator, MenuTrigger, Skeleton, StatePill, Tip } from "@/components/ui/primitives";
import { BrandMark, useHelpdesk } from "./app";
import { RichText } from "./rich-text";

export function Messages() {
  const { route } = useHelpdesk();
  const r = route.tab === "messages" ? route : { sessionId: null, draft: undefined };
  const [composing, setComposing] = useState(false);
  const showThread = !!r.sessionId || !!r.draft || composing;

  return (
    <div className="flex min-h-0 flex-1">
      <div className={cn("flex min-h-0 w-full flex-col border-r bg-surface lg:w-80 lg:shrink-0", showThread && "hidden lg:flex")}>
        <ConversationList onNew={() => setComposing(true)} />
      </div>
      <div className={cn("min-h-0 min-w-0 flex-1 flex-col", showThread ? "flex" : "hidden lg:flex")}>
        <Thread key={r.sessionId ?? `new-${r.draft ?? ""}`} sessionId={r.sessionId} draft={r.draft} onBack={() => setComposing(false)} />
      </div>
    </div>
  );
}

function ConversationList({ onNew }: { onNew: () => void }) {
  const { sessions, loaded, route, go } = useHelpdesk();
  const [q, setQ] = useState("");
  const active = route.tab === "messages" ? route.sessionId : null;
  const groups = useMemo(() => {
    const shown = sessions.filter((s) => !q || `${s.Title} ${s.TicketNo} ${plain(s.LastMessage)}`.toLowerCase().includes(q.toLowerCase()));
    const map = new Map<string, Session[]>();
    for (const s of shown) map.set(dayGroup(s.ModifiedOn), [...(map.get(dayGroup(s.ModifiedOn)) ?? []), s]);
    return [...map.entries()];
  }, [sessions, q]);

  return (
    <>
      <div className="flex items-center justify-between px-4 pb-2 pt-4">
        <h1 className="text-title font-semibold tracking-tight">Messages</h1>
        <Button size="sm" onClick={() => { go({ tab: "messages", sessionId: null }); onNew(); }}>
          <Plus /> New
        </Button>
      </div>
      <div className="px-4 pb-3">
        <SearchInput value={q} onChange={(e) => setQ(e.target.value)} placeholder="Search conversations" aria-label="Search conversations" />
      </div>
      <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto border-t">
        {!loaded && (
          <div className="space-y-3 p-4">
            {[0, 1, 2].map((i) => <Skeleton key={i} className="h-14" />)}
          </div>
        )}
        {loaded && groups.length === 0 && (
          <Empty icon={<MessageCircle className="size-5" />} title={q ? "No conversations match" : "No conversations yet"}>
            {q ? "Try a different word or ticket number." : "Start one and we'll take it from there."}
          </Empty>
        )}
        {groups.map(([label, items]) => (
          <section key={label} aria-label={label}>
            <p className="sticky top-0 z-10 bg-surface/95 px-4 pb-1 pt-3 text-2xs font-semibold uppercase tracking-wider text-subtle-foreground backdrop-blur">{label}</p>
            <ul>
              {items.map((s) => (
                <li key={s.ID}>
                  <button
                    onClick={() => go({ tab: "messages", sessionId: s.ID })}
                    aria-current={active === s.ID ? "true" : undefined}
                    className={cn("relative flex w-full gap-3 px-4 py-3 text-left hover:bg-surface-2", active === s.ID && "bg-primary-soft/60 hover:bg-primary-soft/60")}
                  >
                    {active === s.ID && <span className="absolute inset-y-2 left-0 w-0.5 rounded-full bg-primary" aria-hidden />}
                    <span className="min-w-0 flex-1">
                      <span className="flex items-baseline justify-between gap-2">
                        <span className="truncate text-sm font-medium">{s.Title || "New conversation"}</span>
                        <span className="shrink-0 text-2xs text-subtle-foreground">{ago(s.ModifiedOn)}</span>
                      </span>
                      <span className="mt-0.5 line-clamp-1 text-meta text-muted-foreground">{plain(s.LastMessage) || "No messages yet"}</span>
                      {(s.TicketNo || s.Status === "resolved") && (
                        <span className="mt-1.5 flex gap-1.5">
                          {s.TicketNo && <span className="rounded bg-surface-3 px-1.5 py-0.5 font-mono text-2xs text-muted-foreground">{ticketLabel(s.TicketNo)}</span>}
                          {s.Status === "resolved" && <span className="rounded bg-success-soft px-1.5 py-0.5 text-2xs font-medium text-success">Solved</span>}
                        </span>
                      )}
                    </span>
                  </button>
                </li>
              ))}
            </ul>
          </section>
        ))}
      </div>
    </>
  );
}

type Live = { status: string | null; text: string; sources: SourceRef[] } | null;

function Thread({ sessionId, draft, onBack }: { sessionId: string | null; draft?: string; onBack: () => void }) {
  const { user, config, sessions, tickets, go, refresh } = useHelpdesk();
  const session = sessions.find((s) => s.ID === sessionId) ?? null;
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(!!sessionId);
  const [live, setLive] = useState<Live>(null);
  const [input, setInput] = useState("");
  const [renaming, setRenaming] = useState(false);
  const [confirmDelete, setConfirmDelete] = useState(false);
  const idRef = useRef(sessionId);
  const abortRef = useRef<AbortController | null>(null);
  const endRef = useRef<HTMLDivElement>(null);
  const boxRef = useRef<HTMLTextAreaElement>(null);
  const sentDraft = useRef(false);
  const busy = live !== null;
  const ticket = session?.TicketNo ? tickets.find((t) => t.TicketNo === session.TicketNo) : undefined;

  useEffect(() => {
    if (!sessionId) return;
    api.messages(sessionId).then(setMessages).catch((e: Error) => toast.error(e.message)).finally(() => setLoading(false));
  }, [sessionId]);

  useEffect(() => {
    endRef.current?.scrollIntoView({ block: "end" });
  }, [messages, live]);

  useEffect(() => {
    const box = boxRef.current;
    if (!box) return;
    box.style.height = "auto";
    box.style.height = `${Math.min(box.scrollHeight, 180)}px`;
  }, [input]);

  async function send(text: string, handoff = false) {
    text = text.trim();
    if ((!text && !handoff) || busy) return;
    setInput("");
    if (text) setMessages((m) => [...m, { ID: `local-${Date.now()}`, Role: "user", Content: text, CreatedOn: new Date().toISOString() }]);
    setLive({ status: handoff ? "Handing over to the support team" : "Reading your message", text: "", sources: [] });
    const controller = new AbortController();
    abortRef.current = controller;
    let created = false;
    let final: Message | null = null;
    let raised: Ticket | null = null;
    try {
      let id = idRef.current;
      if (!id) {
        id = (await api.newSession(user.ID)).ID;
        idRef.current = id;
        created = true;
      }
      let acc = "";
      let sources: SourceRef[] = [];
      for await (const ev of turn(id, { userId: user.ID, text, handoff }, controller.signal)) {
        if (ev.event === "status") setLive((l) => (l ? { ...l, status: ev.data.text } : l));
        if (ev.event === "sources") {
          sources = ev.data;
          setLive((l) => (l ? { ...l, sources } : l));
        }
        if (ev.event === "token") {
          acc += ev.data.text;
          setLive((l) => (l ? { ...l, status: null, text: acc } : l));
        }
        if (ev.event === "ticket") raised = ev.data;
        if (ev.event === "done")
          final = {
            ID: ev.data.id, Role: "assistant", Content: acc.trim(), Decision: ev.data.decision as Message["Decision"], TicketNo: ev.data.ticketNo,
            SourcesJson: sources.length ? JSON.stringify(sources) : null, CreatedOn: new Date().toISOString(),
          };
      }
    } catch (e) {
      if ((e as Error).name !== "AbortError") toast.error((e as Error).message);
    } finally {
      setLive(null);
      abortRef.current = null;
      if (final) setMessages((m) => [...m, final!]);
      if (raised) toast.success(`${ticketLabel(raised.TicketNo)} raised`, { description: "The support team has it now." });
      await refresh();
      if (created && idRef.current) go({ tab: "messages", sessionId: idRef.current });
      boxRef.current?.focus();
    }
  }

  useEffect(() => {
    if (draft && !sentDraft.current) {
      sentDraft.current = true;
      const t = setTimeout(() => send(draft), 0);
      return () => clearTimeout(t);
    }
  });

  const title = session?.Title || (sessionId ? "Conversation" : "New conversation");
  const empty = !loading && messages.length === 0 && !live;

  return (
    <div className="flex min-h-0 flex-1 flex-col bg-background">
      <header className="flex h-14 shrink-0 items-center gap-2 border-b bg-surface px-3 lg:px-5">
        <Button variant="ghost" size="icon-sm" className="lg:hidden" aria-label="Back to messages" onClick={() => { onBack(); go({ tab: "messages", sessionId: null }); }}>
          <ArrowLeft />
        </Button>
        <div className="min-w-0 flex-1">
          <h2 className="truncate text-sm font-semibold">{title}</h2>
          {session && (
            <p className="truncate text-xs text-muted-foreground">
              {session.Status === "resolved" ? "Solved" : "Open"} · started {ago(session.CreatedOn)}
            </p>
          )}
        </div>
        {ticket && (
          <button onClick={() => go({ tab: "tickets", ticketId: ticket.ID })} className="hidden items-center gap-2 rounded-md border px-2 py-1 hover:bg-surface-2 sm:flex">
            <span className="font-mono text-xs">{ticketLabel(ticket.TicketNo)}</span>
            <StatePill tone={ticket.StateTone}>{ticket.StateLabel}</StatePill>
          </button>
        )}
        {session && (
          <Menu>
            <MenuTrigger asChild>
              <Button variant="ghost" size="icon-sm" aria-label="Conversation options">
                <MoreHorizontal />
              </Button>
            </MenuTrigger>
            <MenuContent>
              <MenuItem onSelect={() => setRenaming(true)}>
                <Pencil /> Rename
              </MenuItem>
              {session.Status !== "resolved" && (
                <MenuItem onSelect={async () => { await api.updateSession(session.ID, { status: "resolved" }); await refresh(); }}>
                  <CheckCircle2 /> Mark as solved
                </MenuItem>
              )}
              {!session.TicketNo && (
                <MenuItem onSelect={() => send("", true)}>
                  <Headset /> Talk to support
                </MenuItem>
              )}
              <MenuSeparator />
              <MenuItem destructive onSelect={() => setConfirmDelete(true)}>
                <Trash2 /> Delete conversation
              </MenuItem>
            </MenuContent>
          </Menu>
        )}
      </header>

      <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
        <div className="mx-auto w-full max-w-3xl px-4 py-6 sm:px-6">
          {loading && (
            <div className="space-y-4">
              <Skeleton className="ml-auto h-10 w-2/3" />
              <Skeleton className="h-20 w-3/4" />
            </div>
          )}
          {empty && (
            <div className="flex flex-col items-center pt-10 text-center animate-rise">
              <BrandMark name={config.name} compact />
              <h3 className="mt-4 text-lg font-semibold tracking-tight">How can we help?</h3>
              <p className="mt-1 max-w-sm text-sm text-muted-foreground">
                Ask about XBatch or describe what went wrong. If it needs investigation, we&apos;ll raise a ticket with the support team.
              </p>
              <div className="mt-6 grid w-full max-w-lg gap-2 sm:grid-cols-2">
                {config.suggestions.map((s) => (
                  <button key={s} onClick={() => send(s)} className="rounded-xl border bg-surface px-3.5 py-3 text-left text-sm shadow-lift hover:border-border-strong">
                    {s}
                  </button>
                ))}
              </div>
            </div>
          )}

          <ol className="space-y-6" aria-live="polite">
            {messages.map((m) => (
              <MessageItem key={m.ID} m={m} tickets={tickets} onOpenTicket={(id) => go({ tab: "tickets", ticketId: id })} />
            ))}
            {live && (
              <li className="flex gap-3">
                <AssistantAvatar />
                <div className="min-w-0 flex-1 pt-1">
                  {live.status && (
                    <p className="flex items-center gap-2 text-sm text-muted-foreground">
                      <span className="flex gap-0.5" aria-hidden>
                        {[0, 1, 2].map((i) => (
                          <span key={i} className={cn("size-1 rounded-full bg-primary motion-safe:animate-pulse", i === 1 && "delay-150", i === 2 && "delay-300")} />
                        ))}
                      </span>
                      {live.status}…
                    </p>
                  )}
                  {live.text && (
                    <div className="text-foreground">
                      <RichText>{live.text}</RichText>
                      <span className="ml-0.5 inline-block h-4 w-0.5 translate-y-0.5 bg-primary animate-caret" aria-hidden />
                    </div>
                  )}
                  {live.sources.length > 0 && <Sources sources={live.sources} />}
                </div>
              </li>
            )}
          </ol>

          {session?.Status === "resolved" && <RateConversation session={session} onRated={refresh} />}
          <div ref={endRef} />
        </div>
      </div>

      <div className="shrink-0 bg-background px-3 pb-3 sm:px-6 sm:pb-4">
        <form
          className="mx-auto w-full max-w-3xl"
          onSubmit={(e) => {
            e.preventDefault();
            send(input);
          }}
        >
          <div className="rounded-2xl border bg-surface p-2 shadow-lift focus-within:border-border-strong focus-within:ring-2 focus-within:ring-ring">
            <textarea
              ref={boxRef}
              value={input}
              rows={1}
              autoFocus
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey && !e.nativeEvent.isComposing) {
                  e.preventDefault();
                  send(input);
                }
              }}
              placeholder={ticket ? `Ask about ${ticketLabel(ticket.TicketNo)} or anything else…` : "Message the helpdesk…"}
              aria-label="Message"
              className="max-h-45 min-h-10 w-full resize-none bg-transparent px-2 py-2 text-base outline-none focus-visible:outline-none placeholder:text-subtle-foreground sm:text-body"
            />
            <div className="flex items-center justify-between gap-2 pl-1">
              {!ticket ? (
                <Tip label="Raise a ticket with this conversation">
                  <Button type="button" variant="ghost" size="sm" disabled={busy || (!messages.length && !input.trim())} onClick={() => send(input, true)}>
                    <Headset /> Talk to support
                  </Button>
                </Tip>
              ) : (
                <span className="px-2 text-xs text-subtle-foreground">Linked to {ticketLabel(ticket.TicketNo)}</span>
              )}
              {busy ? (
                <Button type="button" size="icon-sm" variant="outline" aria-label="Stop" onClick={() => abortRef.current?.abort()}>
                  <Square className="size-3 fill-current" />
                </Button>
              ) : (
                <Button type="submit" size="icon-sm" disabled={!input.trim()} aria-label="Send">
                  <ArrowUp />
                </Button>
              )}
            </div>
          </div>
          <p className="mt-1.5 hidden px-2 text-2xs text-subtle-foreground sm:block">Enter to send · Shift+Enter for a new line · Answers can be wrong; the support team checks everything on tickets.</p>
        </form>
      </div>

      {session && (
        <RenameDialog open={renaming} onOpenChange={setRenaming} initial={session.Title ?? ""} onSave={async (t) => { await api.updateSession(session.ID, { title: t }); await refresh(); }} />
      )}
      <Dialog open={confirmDelete} onOpenChange={setConfirmDelete} title="Delete this conversation?" description="The messages are removed for good. Any ticket it raised stays open with the support team.">
        <div className="flex justify-end gap-2">
          <Button variant="outline" onClick={() => setConfirmDelete(false)}>Cancel</Button>
          <Button
            variant="destructive"
            onClick={async () => {
              if (!session) return;
              await api.deleteSession(session.ID);
              setConfirmDelete(false);
              await refresh();
              go({ tab: "messages", sessionId: null });
            }}
          >
            Delete
          </Button>
        </div>
      </Dialog>
    </div>
  );
}

function AssistantAvatar() {
  return (
    <span className="grid size-7 shrink-0 place-items-center rounded-lg bg-primary text-primary-foreground" aria-hidden>
      <svg viewBox="0 0 24 24" className="size-3.5" fill="none" stroke="currentColor" strokeWidth="2.4" strokeLinecap="round">
        <path d="M4 17c3-6 5-9 8-9s5 3 8 9" />
      </svg>
    </span>
  );
}

function MessageItem({ m, tickets, onOpenTicket }: { m: Message; tickets: Ticket[]; onOpenTicket: (id: string) => void }) {
  const [feedback, setFeedback] = useState<number | null>(m.Feedback ?? null);
  const [copied, setCopied] = useState(false);
  const sources: SourceRef[] = m.SourcesJson ? JSON.parse(m.SourcesJson) : [];
  const ticket = m.TicketNo ? tickets.find((t) => t.TicketNo === m.TicketNo) : undefined;
  const persisted = typeof m.ID === "number";

  if (m.Role === "user")
    return (
      <li className="flex justify-end animate-rise">
        <div className="max-w-xs sm:max-w-md">
          <div className="whitespace-pre-wrap break-words rounded-2xl rounded-br-md bg-primary px-4 py-2.5 text-body leading-relaxed text-primary-foreground">{m.Content}</div>
          <p className="mt-1 text-right text-2xs text-subtle-foreground">{clock(m.CreatedOn)}</p>
        </div>
      </li>
    );

  const rate = async (v: number) => {
    const next = feedback === v ? 0 : v;
    setFeedback(next || null);
    if (persisted) await api.feedback(m.ID, next).catch(() => {});
  };

  return (
    <li className="group flex gap-3 animate-rise">
      <AssistantAvatar />
      <div className="min-w-0 flex-1 pt-0.5">
        <RichText>{m.Content}</RichText>
        {ticket && (
          <button onClick={() => onOpenTicket(ticket.ID)} className="mt-3 flex w-full max-w-md items-center gap-3 rounded-xl border bg-surface p-3.5 text-left shadow-lift hover:border-border-strong">
            <span className="grid size-9 shrink-0 place-items-center rounded-lg bg-primary-soft text-primary-soft-foreground">
              <Headset className="size-4" aria-hidden />
            </span>
            <span className="min-w-0 flex-1">
              <span className="flex items-center gap-2">
                <span className="font-mono text-xs text-muted-foreground">{ticketLabel(ticket.TicketNo)}</span>
                <StatePill tone={ticket.StateTone}>{ticket.StateLabel}</StatePill>
              </span>
              <span className="mt-1 block truncate text-sm font-medium">{ticket.BriefDetails}</span>
            </span>
            <ChevronRight className="size-4 text-subtle-foreground" aria-hidden />
          </button>
        )}
        {sources.length > 0 && <Sources sources={sources} />}
        {m.Decision !== "ticket" && (
          <div className="mt-1.5 flex items-center gap-0.5 opacity-100 transition-opacity sm:opacity-0 sm:group-focus-within:opacity-100 sm:group-hover:opacity-100">
            <span className="mr-1.5 text-2xs text-subtle-foreground">{clock(m.CreatedOn)}</span>
            <Tip label="Helpful">
              <button onClick={() => rate(1)} aria-pressed={feedback === 1} aria-label="Helpful" className={cn("grid size-7 place-items-center rounded-md text-subtle-foreground hover:bg-surface-2 hover:text-foreground", feedback === 1 && "text-success")}>
                <ThumbsUp className="size-3.5" />
              </button>
            </Tip>
            <Tip label="Not helpful">
              <button onClick={() => rate(-1)} aria-pressed={feedback === -1} aria-label="Not helpful" className={cn("grid size-7 place-items-center rounded-md text-subtle-foreground hover:bg-surface-2 hover:text-foreground", feedback === -1 && "text-destructive")}>
                <ThumbsDown className="size-3.5" />
              </button>
            </Tip>
            <Tip label={copied ? "Copied" : "Copy"}>
              <button
                onClick={async () => {
                  await navigator.clipboard.writeText(m.Content).catch(() => {});
                  setCopied(true);
                  setTimeout(() => setCopied(false), 1500);
                }}
                aria-label="Copy reply"
                className="grid size-7 place-items-center rounded-md text-subtle-foreground hover:bg-surface-2 hover:text-foreground"
              >
                {copied ? <Check className="size-3.5" /> : <Copy className="size-3.5" />}
              </button>
            </Tip>
          </div>
        )}
      </div>
    </li>
  );
}

const SOURCE_KIND: Record<string, string> = { screen: "Screen", table: "Data", view: "Report", procedure: "Process", event: "Event", key: "Identifier", api: "Interface" };

function Sources({ sources }: { sources: SourceRef[] }) {
  return (
    <div className="mt-3 flex flex-wrap items-center gap-1.5">
      <span className="flex items-center gap-1 text-2xs font-medium text-subtle-foreground">
        <BookOpen className="size-3" aria-hidden /> From XBatch
      </span>
      {sources.map((s) => (
        <span key={s.Slug} className="inline-flex h-6 items-center gap-1 rounded-md border bg-surface px-2 text-xs">
          <span className="text-subtle-foreground">{SOURCE_KIND[s.Type] ?? s.Type}</span>
          <span className="max-w-56 truncate">{s.Title.replace(/^List_/, "").replace(/_/g, " ")}</span>
        </span>
      ))}
    </div>
  );
}

function RateConversation({ session, onRated }: { session: Session; onRated: () => void }) {
  const [rating, setRating] = useState(session.Rating ?? 0);
  return (
    <div className="mt-8 rounded-xl border bg-surface p-4 text-center animate-rise">
      <p className="text-sm font-medium">{rating ? "Thanks for the feedback" : "Glad it's solved. How did we do?"}</p>
      <div className="mt-2 flex justify-center gap-1" role="radiogroup" aria-label="Rate this conversation">
        {[1, 2, 3, 4, 5].map((n) => (
          <button
            key={n}
            role="radio"
            aria-checked={rating === n}
            aria-label={`${n} of 5`}
            onClick={async () => {
              setRating(n);
              await api.updateSession(session.ID, { rating: n });
              onRated();
            }}
            className={cn("grid size-9 place-items-center rounded-md text-lg hover:bg-surface-2", n <= rating ? "text-warning" : "text-border-strong")}
          >
            ★
          </button>
        ))}
      </div>
    </div>
  );
}

function RenameDialog({ open, onOpenChange, initial, onSave }: { open: boolean; onOpenChange: (o: boolean) => void; initial: string; onSave: (t: string) => Promise<void> }) {
  const [value, setValue] = useState(initial);
  return (
    <Dialog open={open} onOpenChange={(o) => { if (o) setValue(initial); onOpenChange(o); }} title="Rename conversation">
      <form
        onSubmit={async (e) => {
          e.preventDefault();
          if (!value.trim()) return;
          await onSave(value.trim());
          onOpenChange(false);
        }}
      >
        <Input autoFocus value={value} onChange={(e) => setValue(e.target.value)} aria-label="Conversation name" maxLength={200} />
        <div className="mt-4 flex justify-end gap-2">
          <Button type="button" variant="outline" onClick={() => onOpenChange(false)}>Cancel</Button>
          <Button type="submit" disabled={!value.trim()}>Save</Button>
        </div>
      </form>
    </Dialog>
  );
}
