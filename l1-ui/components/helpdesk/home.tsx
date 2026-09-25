"use client";

import { useState } from "react";
import { ArrowRight, ArrowUp, BellRing, ChevronRight, MessageCircle, Ticket as TicketIcon } from "lucide-react";
import { ago, displayName, plain, ticketLabel } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Skeleton, StatePill } from "@/components/ui/primitives";
import { Button } from "@/components/ui/button";
import { Panel } from "@/components/ui/viz";
import { AccountMenu, BrandMark, useHelpdesk } from "./app";

function greeting() {
  const h = new Date().getHours();
  return h < 12 ? "Good morning" : h < 17 ? "Good afternoon" : "Good evening";
}

export function Home() {
  const { user, config, tickets, sessions, loaded, go } = useHelpdesk();
  const [draft, setDraft] = useState("");
  const first = displayName(user).split(" ")[0];
  const waiting = tickets.filter((t) => t.StateTone === "attention");
  const open = tickets.filter((t) => t.StateTone !== "done" && t.StateTone !== "attention").slice(0, 4);
  const recent = sessions.slice(0, 4);
  const start = (text: string) => text.trim() && go({ tab: "messages", sessionId: null, draft: text.trim() });

  return (
    <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
      <header className="border-b bg-canvas">
        <div className="mx-auto flex max-w-3xl items-center justify-between px-5 pt-4 md:hidden">
          <BrandMark name={config.name} />
          <AccountMenu user={user} compact />
        </div>
        <div className="mx-auto max-w-3xl px-5 pb-7 pt-6 md:px-8 md:pt-12">
          <h1 className="text-2xl font-semibold tracking-tight md:text-display">
            {greeting()}, {first}
          </h1>
          <p className="mt-1.5 max-w-xl text-pretty text-body text-muted-foreground">{config.greeting}</p>
          <form
            className="mt-5 flex items-end gap-2 rounded-2xl border bg-canvas p-2 focus-within:border-signal focus-within:ring-2 focus-within:ring-ring"
            onSubmit={(e) => {
              e.preventDefault();
              start(draft);
            }}
          >
            <textarea
              value={draft}
              onChange={(e) => setDraft(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey && !e.nativeEvent.isComposing) {
                  e.preventDefault();
                  start(draft);
                }
              }}
              rows={2}
              placeholder="Describe the problem — heat, work order or screen if you know it"
              aria-label="Describe the problem"
              className="max-h-40 min-h-12 flex-1 resize-none bg-transparent px-2 py-1.5 text-base outline-none focus-visible:outline-none placeholder:text-subtle-foreground sm:text-body"
            />
            <button type="submit" disabled={!draft.trim()} aria-label="Start conversation" className="grid size-10 shrink-0 place-items-center rounded-lg bg-foreground text-background disabled:bg-surface-3 disabled:text-subtle-foreground">
              <ArrowUp className="size-4" />
            </button>
          </form>
          {config.suggestions.length > 0 && (
            <div className="mt-3 flex flex-wrap gap-2">
              {config.suggestions.map((s) => (
                <button key={s} onClick={() => start(s)} className="rounded-lg border bg-canvas px-3 py-1.5 text-left font-mono text-xs text-muted-foreground hover:border-signal/60 hover:text-foreground">
                  {s}
                </button>
              ))}
            </div>
          )}
        </div>
      </header>

      <div className="mx-auto max-w-3xl space-y-4 px-5 py-6 md:px-8">
        {waiting.length > 0 && (
          <Panel icon={BellRing} title="The support team is waiting for you" meta={`${waiting.length} ticket${waiting.length === 1 ? "" : "s"} need your reply`} pad="tight">
            <ul className="space-y-1.5">
              {waiting.map((t) => (
                <li key={t.ID}>
                  <button onClick={() => go({ tab: "tickets", ticketId: t.ID })} className="flex w-full items-center gap-4 rounded-lg border border-warning/40 bg-warning-soft px-3 py-3 text-left hover:border-warning">
                    <div className="min-w-0 flex-1">
                      <p className="text-sm font-medium"><span className="font-mono">{ticketLabel(t.TicketNo)}</span> · {t.BriefDetails}</p>
                      <p className="mt-1 line-clamp-2 text-sm text-muted-foreground">{plain(t.ReplyText)}</p>
                    </div>
                    <span className="flex shrink-0 items-center gap-1 text-sm font-medium text-warning">Reply <ArrowRight className="size-4" /></span>
                  </button>
                </li>
              ))}
            </ul>
          </Panel>
        )}

        <Panel icon={TicketIcon} title="Open tickets" meta={loaded ? `${open.length} open · the support team is on them` : "loading"} pad="tight"
          actions={tickets.length > 0 ? <Button size="sm" variant="ghost" onClick={() => go({ tab: "tickets", ticketId: null })}>View all <ArrowRight /></Button> : undefined}>
          {!loaded ? <CardSkeletons /> : open.length ? (
            <ul className="grid gap-1.5 sm:grid-cols-2">
              {open.map((t) => (
                <li key={t.ID}>
                  <button onClick={() => go({ tab: "tickets", ticketId: t.ID })} className="flex h-full w-full flex-col rounded-lg border bg-canvas p-3 text-left hover:border-border-strong">
                    <span className="flex w-full items-center justify-between gap-2 font-mono text-xs text-subtle-foreground">
                      <span>{ticketLabel(t.TicketNo)}</span>
                      <span>{ago(t.ModifiedOn ?? t.CreatedOn)}</span>
                    </span>
                    <span className="mt-1.5 line-clamp-2 text-sm font-medium">{t.BriefDetails}</span>
                    <span className="mt-auto pt-3"><StatePill tone={t.StateTone}>{t.StateLabel}</StatePill></span>
                  </button>
                </li>
              ))}
            </ul>
          ) : <p className="px-2 py-5 text-sm text-muted-foreground">No open tickets. When something needs investigation, it is tracked here.</p>}
        </Panel>

        <Panel icon={MessageCircle} title="Recent conversations" meta={loaded ? `${sessions.length} with the assistant` : "loading"} pad="tight"
          actions={sessions.length > 0 ? <Button size="sm" variant="ghost" onClick={() => go({ tab: "messages", sessionId: null })}>View all <ArrowRight /></Button> : undefined}>
          {!loaded ? <CardSkeletons /> : recent.length ? (
            <ul>
              {recent.map((s) => (
                <li key={s.ID}>
                  <button onClick={() => go({ tab: "messages", sessionId: s.ID })} className="flex w-full items-center gap-3 rounded-lg px-2 py-2.5 text-left hover:bg-surface-2">
                    <span className="min-w-0 flex-1">
                      <span className="block truncate text-sm font-medium">{s.Title || "New conversation"}</span>
                      <span className="block truncate text-meta text-muted-foreground">{plain(s.LastMessage)}</span>
                    </span>
                    {s.TicketNo && <span className="shrink-0 font-mono text-xs text-signal">{ticketLabel(s.TicketNo)}</span>}
                    <span className="shrink-0 font-mono text-xs text-subtle-foreground">{ago(s.ModifiedOn)}</span>
                    <ChevronRight className="size-4 shrink-0 text-subtle-foreground" aria-hidden />
                  </button>
                </li>
              ))}
            </ul>
          ) : <p className="px-2 py-5 text-sm text-muted-foreground">Your conversations will show up here.</p>}
        </Panel>
      </div>
    </div>
  );
}

function CardSkeletons() {
  return (
    <div className={cn("grid gap-2 sm:grid-cols-2")}>
      <Skeleton className="h-28" />
      <Skeleton className="h-28" />
    </div>
  );
}
