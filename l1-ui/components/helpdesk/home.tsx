"use client";

import { useState } from "react";
import { AlertCircle, ArrowRight, ArrowUp, ChevronRight, MessageCircle } from "lucide-react";
import { ago, displayName, plain, ticketLabel } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Skeleton, StatePill } from "@/components/ui/primitives";
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
      <header className="border-b bg-surface">
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
            className="mt-5 flex items-end gap-2 rounded-xl border bg-background p-2 shadow-lift focus-within:border-border-strong focus-within:ring-2 focus-within:ring-ring"
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
            <button type="submit" disabled={!draft.trim()} aria-label="Start conversation" className="grid size-10 shrink-0 place-items-center rounded-lg bg-primary text-primary-foreground disabled:bg-surface-3 disabled:text-subtle-foreground">
              <ArrowUp className="size-4" />
            </button>
          </form>
          {config.suggestions.length > 0 && (
            <div className="mt-3 flex flex-wrap gap-2">
              {config.suggestions.map((s) => (
                <button key={s} onClick={() => start(s)} className="rounded-full border bg-surface px-3 py-1.5 text-left text-meta text-muted-foreground hover:border-border-strong hover:text-foreground">
                  {s}
                </button>
              ))}
            </div>
          )}
        </div>
      </header>

      <div className="mx-auto max-w-3xl space-y-8 px-5 py-7 md:px-8">
        {waiting.length > 0 && (
          <section aria-labelledby="waiting" className="animate-rise">
            <h2 id="waiting" className="flex items-center gap-2 text-sm font-semibold">
              <AlertCircle className="size-4 text-warning" aria-hidden /> The support team is waiting for you
            </h2>
            <ul className="mt-3 space-y-2">
              {waiting.map((t) => (
                <li key={t.ID}>
                  <button onClick={() => go({ tab: "tickets", ticketId: t.ID })} className="flex w-full items-center gap-4 rounded-xl border border-warning/40 bg-warning-soft/60 p-4 text-left hover:border-warning">
                    <div className="min-w-0 flex-1">
                      <p className="text-sm font-medium">{ticketLabel(t.TicketNo)} · {t.BriefDetails}</p>
                      <p className="mt-1 line-clamp-2 text-sm text-muted-foreground">{t.ReplyText}</p>
                    </div>
                    <span className="flex shrink-0 items-center gap-1 text-sm font-medium text-warning">
                      Reply <ArrowRight className="size-4" />
                    </span>
                  </button>
                </li>
              ))}
            </ul>
          </section>
        )}

        <section aria-labelledby="open-tickets">
          <SectionHead id="open-tickets" title="Open tickets" action={tickets.length > 0 ? () => go({ tab: "tickets", ticketId: null }) : undefined} />
          {!loaded ? (
            <CardSkeletons />
          ) : open.length ? (
            <ul className="mt-3 grid gap-2 sm:grid-cols-2">
              {open.map((t) => (
                <li key={t.ID}>
                  <button onClick={() => go({ tab: "tickets", ticketId: t.ID })} className="flex h-full w-full flex-col rounded-xl border bg-surface p-4 text-left shadow-lift hover:border-border-strong">
                    <div className="flex w-full items-center justify-between gap-2">
                      <span className="font-mono text-xs text-muted-foreground">{ticketLabel(t.TicketNo)}</span>
                      <span className="text-xs text-subtle-foreground">{ago(t.ModifiedOn ?? t.CreatedOn)}</span>
                    </div>
                    <p className="mt-1.5 line-clamp-2 text-sm font-medium">{t.BriefDetails}</p>
                    <div className="mt-auto pt-3">
                      <StatePill tone={t.StateTone}>{t.StateLabel}</StatePill>
                    </div>
                  </button>
                </li>
              ))}
            </ul>
          ) : (
            <p className="mt-3 rounded-xl border border-dashed px-4 py-5 text-sm text-muted-foreground">No open tickets. When something needs investigation, it will be tracked here.</p>
          )}
        </section>

        <section aria-labelledby="recent">
          <SectionHead id="recent" title="Recent conversations" action={sessions.length > 0 ? () => go({ tab: "messages", sessionId: null }) : undefined} />
          {!loaded ? (
            <CardSkeletons />
          ) : recent.length ? (
            <ul className="mt-3 divide-y rounded-xl border bg-surface">
              {recent.map((s) => (
                <li key={s.ID}>
                  <button onClick={() => go({ tab: "messages", sessionId: s.ID })} className="flex w-full items-center gap-3 px-4 py-3 text-left hover:bg-surface-2 first:rounded-t-xl last:rounded-b-xl">
                    <span className="grid size-8 shrink-0 place-items-center rounded-full bg-primary-soft text-primary-soft-foreground">
                      <MessageCircle className="size-4" aria-hidden />
                    </span>
                    <span className="min-w-0 flex-1">
                      <span className="block truncate text-sm font-medium">{s.Title || "New conversation"}</span>
                      <span className="block truncate text-meta text-muted-foreground">{plain(s.LastMessage)}</span>
                    </span>
                    <span className="shrink-0 text-xs text-subtle-foreground">{ago(s.ModifiedOn)}</span>
                    <ChevronRight className="size-4 shrink-0 text-subtle-foreground" aria-hidden />
                  </button>
                </li>
              ))}
            </ul>
          ) : (
            <p className="mt-3 rounded-xl border border-dashed px-4 py-5 text-sm text-muted-foreground">Your conversations will show up here.</p>
          )}
        </section>
      </div>
    </div>
  );
}

function SectionHead({ id, title, action }: { id: string; title: string; action?: () => void }) {
  return (
    <div className="flex items-center justify-between">
      <h2 id={id} className="text-sm font-semibold">{title}</h2>
      {action && (
        <button onClick={action} className="text-meta font-medium text-primary hover:underline">
          View all
        </button>
      )}
    </div>
  );
}

function CardSkeletons() {
  return (
    <div className={cn("mt-3 grid gap-2 sm:grid-cols-2")}>
      <Skeleton className="h-28" />
      <Skeleton className="h-28" />
    </div>
  );
}
