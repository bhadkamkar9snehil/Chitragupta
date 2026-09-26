"use client";

import { useEffect, useMemo, useState } from "react";
import { AlertCircle, ArrowLeft, ArrowRight, Bot, CheckCircle2, Clock, Headset, Inbox, Layers, PanelLeftClose, PanelLeftOpen, RefreshCw, User as UserIcon } from "lucide-react";
import { toast } from "sonner";
import { api, type Message, type SourceRef, type Ticket } from "@/lib/api";
import { ago, human, outcomeLabel, pageTitle, plain, RESPONSE_KIND, ticketLabel, when, whenShort } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Avatar, Empty, QueueRow, SearchInput, Skeleton, StatePill, Tag, Tip } from "@/components/ui/primitives";
import { RichText } from "@/components/helpdesk/rich-text";
import { PageTitle } from "@/components/ui/viz";

const VIEWS = [
  { id: "", label: "All", icon: Layers },
  { id: "attention", label: "Waiting on requester", icon: AlertCircle },
  { id: "pending", label: "Being investigated", icon: Clock },
  { id: "progress", label: "With support team", icon: Headset },
  { id: "done", label: "Resolved", icon: CheckCircle2 },
];

export function InboxView({ ticketId, onSelect, onOpenRun }: { ticketId: string | null; onSelect: (id: string | null) => void; onOpenRun: (id: string) => void }) {
  const [view, setView] = useState("");
  const [q, setQ] = useState("");
  const [area, setArea] = useState("");
  const [source, setSource] = useState("");
  const [rows, setRows] = useState<Ticket[] | null>(null);
  const [all, setAll] = useState<Ticket[]>([]);
  const [lookups, setLookups] = useState<{ areas: string[]; sources: string[] }>({ areas: [], sources: [] });
  const [tick, setTick] = useState(0);
  const [collapsedTicketId, setCollapsedTicketId] = useState<string | null>(null);
  const drawerOpen = !ticketId || collapsedTicketId !== ticketId;

  useEffect(() => {
    api.admin.lookups().then(setLookups).catch(() => {});
  }, []);


  useEffect(() => {
    const t = setTimeout(() => {
      api.admin.tickets({ q: q || undefined, area: area || undefined, source: source || undefined }).then((r) => {
        setAll(r);
        setRows(r);
      }).catch((e: Error) => toast.error(e.message));
    }, 200);
    return () => clearTimeout(t);
  }, [q, area, source, tick]);

  useEffect(() => {
    const poll = setInterval(() => setTick((n) => n + 1), 60_000);
    return () => clearInterval(poll);
  }, []);

  const shown = useMemo(() => (rows ?? []).filter((t) => !view || t.StateTone === view), [rows, view]);
  const count = (id: string) => all.filter((t) => !id || t.StateTone === id).length;

  return (
    <div className="flex min-h-0 flex-1">
      <section aria-label="Tickets" className={cn("flex min-h-0 w-full flex-col border-r bg-canvas md:w-80 md:shrink-0 xl:w-96", ticketId && "hidden", drawerOpen && "md:flex", !drawerOpen && "md:hidden")}>
        <div className="space-y-2 border-b px-3 py-3">
          <PageTitle icon={Inbox} title={VIEWS.find((v) => v.id === view)!.label}>
            <Tip label="Refresh">
              <Button variant="ghost" size="icon-sm" aria-label="Refresh" onClick={() => setTick((n) => n + 1)}>
                <RefreshCw />
              </Button>
            </Tip>
          </PageTitle>
          <div className="scrollbar-thin flex gap-1 overflow-x-auto pb-0.5" role="tablist" aria-label="Ticket status views">
            {VIEWS.map((v) => (
              <button
                key={v.id || "all"}
                role="tab"
                aria-selected={view === v.id}
                onClick={() => setView(v.id)}
                className={cn("flex h-8 shrink-0 items-center gap-1.5 rounded-md px-2 text-xs text-muted-foreground hover:bg-surface-2 hover:text-foreground", view === v.id && "bg-surface-3 font-medium text-foreground")}
              >
                <v.icon className="size-3.5" aria-hidden />
                {v.label}
                <span className="text-2xs tabular-nums text-subtle-foreground">{count(v.id)}</span>
              </button>
            ))}
          </div>
          <SearchInput value={q} onChange={(e) => setQ(e.target.value)} placeholder="Search tickets, requesters…" aria-label="Search tickets" />
          <div className="flex gap-2">
            <select value={area} onChange={(e) => setArea(e.target.value)} aria-label="Area" className="h-8 min-w-0 flex-1 rounded-md border bg-surface px-2 text-meta">
              <option value="">All areas</option>
              {lookups.areas.map((a) => <option key={a}>{a}</option>)}
            </select>
            <select value={source} onChange={(e) => setSource(e.target.value)} aria-label="Channel" className="h-8 min-w-0 flex-1 rounded-md border bg-surface px-2 text-meta">
              <option value="">All channels</option>
              {lookups.sources.map((s) => <option key={s}>{s}</option>)}
            </select>
          </div>
        </div>
        <ul className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
          {!rows && [0, 1, 2, 3].map((i) => <li key={i} className="border-b p-3"><Skeleton className="h-14" /></li>)}
          {shown.map((t) => (
            <QueueRow key={t.ID} selected={ticketId === t.ID} onClick={() => onSelect(t.ID)} avatar={<Avatar name={t.FirstLastName || t.EmailID || "?"} className="mt-0.5 size-7" />}>
                  <span className="flex items-baseline gap-2">
                    <span className="truncate text-meta font-medium">{t.FirstLastName || t.EmailID}</span>
                    <span className="ml-auto shrink-0 text-2xs text-subtle-foreground">{ago(t.ModifiedOn ?? t.CreatedOn)}</span>
                  </span>
                  <span className="mt-0.5 line-clamp-2 text-meta leading-snug text-muted-foreground">
                    <span className="font-mono text-2xs text-subtle-foreground">{ticketLabel(t.TicketNo)}</span> {t.BriefDetails}
                  </span>
                  <span className="mt-1.5 flex flex-wrap items-center gap-1.5">
                    <StatePill tone={t.StateTone}>{t.StateLabel}</StatePill>
                    {t.Priority && !t.Priority.startsWith("Standard") && <Tag>{t.Priority.replace(" Priority", "")}</Tag>}
                  </span>
            </QueueRow>
          ))}
          {rows && !shown.length && (
            <li><Empty icon={<Inbox className="size-5" />} title="No tickets here">Change the view or filters.</Empty></li>
          )}
        </ul>
      </section>

      <div className={cn("min-h-0 min-w-0 flex-1 flex-col", ticketId ? "flex" : "hidden md:flex")}>
        {ticketId ? (
          <TicketWorkspace key={ticketId} id={ticketId} onOpenRun={onOpenRun} onBack={() => onSelect(null)} drawerOpen={drawerOpen} onDrawerToggle={() => setCollapsedTicketId((current) => current === ticketId ? null : ticketId)} />
        ) : (
          <Empty className="m-auto" icon={<Inbox className="size-5" />} title="Pick a ticket">Its activity, the chat that raised it, and the L2 runs appear here.</Empty>
        )}
      </div>
    </div>
  );
}

function TicketWorkspace({ id, onBack, onOpenRun, drawerOpen, onDrawerToggle }: { id: string; onBack: () => void; onOpenRun: (id: string) => void; drawerOpen: boolean; onDrawerToggle: () => void }) {
  const [t, setT] = useState<Ticket | null>(null);
  const [tab, setTab] = useState<"activity" | "chat">("activity");

  useEffect(() => {
    api.admin.ticket(id).then(setT).catch((e: Error) => toast.error(e.message));
  }, [id]);

  if (!t)
    return (
      <div className="space-y-3 p-6">
        <Skeleton className="h-6 w-1/3" />
        <Skeleton className="h-40" />
      </div>
    );

  const ids: string[] = (() => {
    try {
      return JSON.parse(t.ExtractedEntitiesJson ?? "{}").identifiers ?? [];
    } catch {
      return [];
    }
  })();
  // The first entry only repeats the title when the requester wrote nothing more.
  const activity = (t.Timeline?.filter((item) => !(item.Kind === "created" && plain(item.Text).toLowerCase() === plain(t.BriefDetails).toLowerCase()))) ?? [];
  const tabs = [
    { id: "activity" as const, label: "Activity", n: activity.length },
    ...(t.Transcript?.length ? [{ id: "chat" as const, label: "Chat", n: t.Transcript.length }] : []),
  ];

  return (
    <div className="flex min-h-0 flex-1">
      <div className="flex min-h-0 min-w-0 flex-1 flex-col">
        <header className="shrink-0 border-b bg-canvas px-4 py-3">
          <div className="flex items-start gap-2">
            <Button variant="ghost" size="icon-sm" className="md:hidden" aria-label="Back" onClick={onBack}>
              <ArrowLeft />
            </Button>
            <Button variant="ghost" size="icon-sm" className="hidden md:inline-flex" aria-label={drawerOpen ? "Hide ticket list" : "Show ticket list"} onClick={onDrawerToggle}>
              {drawerOpen ? <PanelLeftClose /> : <PanelLeftOpen />}
            </Button>
            <div className="min-w-0 flex-1">
              <div className="flex flex-col-reverse items-start gap-2 sm:flex-row sm:gap-3">
                <h2 className="min-w-0 flex-1 text-body font-semibold leading-snug tracking-tight sm:text-title">
                  <button
                    className="mr-2 font-mono text-muted-foreground hover:text-foreground"
                    title="Copy ticket number"
                    onClick={() => { navigator.clipboard.writeText(t.TicketNo).catch(() => {}); toast.success("Ticket number copied"); }}
                  >{ticketLabel(t.TicketNo)}</button>
                  {t.BriefDetails}
                </h2>
                <StatePill tone={t.StateTone} className="shrink-0 sm:mt-0.5">{t.StateLabel}</StatePill>
              </div>
              <Trail ticket={t} onChat={() => setTab("chat")} onRun={onOpenRun} />
            </div>
          </div>
          <div className={cn("scrollbar-thin mt-3 flex w-fit max-w-full gap-1 overflow-x-auto rounded-xl border bg-canvas p-1", tabs.length < 2 && "hidden")} role="tablist">
            {tabs.map((x) => (
              <button
                key={x.id}
                role="tab"
                aria-selected={tab === x.id}
                onClick={() => setTab(x.id)}
                className={cn("flex h-10 shrink-0 items-center gap-2 whitespace-nowrap rounded-lg px-3 text-meta font-medium text-muted-foreground hover:bg-surface-2 hover:text-foreground sm:h-9", tab === x.id && "bg-foreground text-background hover:bg-foreground hover:text-background")}
              >
                {x.label}
                <span className={cn("rounded px-1.5 font-mono text-2xs tabular-nums", tab === x.id ? "bg-background/15" : "bg-surface-3")}>{x.n}</span>
              </button>
            ))}
          </div>
        </header>
        <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto px-4 py-5 lg:px-8">
          <div className="mx-auto max-w-3xl">
            {tab === "activity" && (
              <ol className="space-y-5">
                {activity.map((item, i) => {
                  const support = item.Actor === "support";
                  return (
                    <li key={i} className="flex gap-3">
                      <span className={cn("grid size-8 shrink-0 place-items-center rounded-full", support ? "bg-signal-soft text-signal" : "border bg-surface text-muted-foreground")} aria-hidden>
                        {support ? <Headset className="size-4" /> : <UserIcon className="size-4" />}
                      </span>
                      <div className="min-w-0 flex-1">
                        <p className="text-meta">
                          <span className="font-semibold">{support ? "L2 support" : t.FirstLastName || "Requester"}</span>{" "}
                          <span className="text-muted-foreground">
                            {item.Kind === "created" ? "raised the ticket" : item.Kind === "reply" ? (RESPONSE_KIND[item.ResponseType ?? ""] ?? "replied").toLowerCase() : item.Kind === "answer" ? "replied" : item.Kind === "rating" ? `rated ${item.Rating}/5` : "reported it again"}
                          </span>{" "}
                          <span className="text-2xs text-subtle-foreground">{when(item.At)}</span>
                        </p>
                        {item.Text && (
                          <div className={cn("mt-1.5 rounded-xl border p-3.5", support ? "bg-surface" : "bg-surface-2")}>
                            <RichText compact>{item.Text}</RichText>
                          </div>
                        )}
                      </div>
                    </li>
                  );
                })}
              </ol>
            )}
            {tab === "chat" && (t.Transcript?.length ? <Transcript messages={t.Transcript} /> : <Empty icon={<Bot className="size-5" />} title="No chat">This ticket was not raised from the helpdesk chat.</Empty>)}
          </div>
        </div>
      </div>

      <aside className="scrollbar-thin hidden w-72 shrink-0 space-y-5 overflow-y-auto border-l bg-surface p-4 text-sm 2xl:block" aria-label="Properties">
        <div className="flex items-center gap-3">
          <Avatar name={t.FirstLastName || t.EmailID || "?"} className="size-10" />
          <div className="min-w-0">
            <p className="truncate font-medium">{t.FirstLastName || "Requester"}</p>
            <p className="truncate text-xs text-muted-foreground">{t.EmailID}</p>
          </div>
        </div>
        <Props
          rows={[
            ["Area", t.Area ?? "—"],
            ["Type", t.Type ?? "—"],
            ["Priority", t.Priority?.replace(" Priority", "") ?? "Standard"],
            ["Channel", t.Channel ?? "—"],
            ["Created", whenShort(t.CreatedOn)],
            ["First reply", t.FirstReplyOn ? whenShort(t.FirstReplyOn) : "—"],
            ["Updated", whenShort(t.ModifiedOn)],
            ["Rating", t.Rating ? "★".repeat(t.Rating) : "—"],
          ]}
        />
        {ids.length > 0 && (
          <div>
            <p className="text-2xs font-semibold uppercase tracking-wider text-subtle-foreground">Identifiers</p>
            <div className="mt-2 flex flex-wrap gap-1">{ids.map((i) => <Tag key={i} mono>{i}</Tag>)}</div>
          </div>
        )}
        <p className="rounded-lg bg-surface-2 p-3 text-xs text-muted-foreground">
          Status is owned by the L2 pipeline. The requester answers from the helpdesk; the ticket returns to L2 automatically.
        </p>
      </aside>
    </div>
  );
}

// One quiet line: who raised it, when, and where it has been. The chat and each L2 attempt open their record.
function Trail({ ticket: t, onChat, onRun }: { ticket: Ticket; onChat: () => void; onRun: (id: string) => void }) {
  const link = "text-foreground underline-offset-4 hover:underline";
  const high = t.Priority && !/standard|normal|medium/i.test(t.Priority) ? t.Priority.replace(" Priority", "") : null;
  return (
    <p className="mt-1 flex flex-wrap items-center gap-x-2 gap-y-1 pb-1 text-xs text-muted-foreground">
      <span>{t.FirstLastName || t.EmailID}</span>
      <span aria-hidden>·</span>
      <span>{whenShort(t.CreatedOn)}</span>
      {high && <><span aria-hidden>·</span><span className="text-warning">{high}</span></>}
      {t.Transcript?.length ? <><span aria-hidden>·</span><button onClick={onChat} className={link}>from chat</button></> : null}
      <span aria-hidden>·</span>
      {t.Runs?.length ? t.Runs.map((r, i) => (
        <span key={r.ID} className="flex items-center gap-2">
          {i > 0 && <span aria-hidden>→</span>}
          <button onClick={() => onRun(r.ID)} className={cn(link, !r.CompletedOn && "text-signal")}>
            L2 #{r.AttemptNo} {r.CompletedOn ? outcomeLabel(r.ResponseType).toLowerCase() : "working"}
          </button>
        </span>
      )) : <span>not claimed by L2 yet</span>}
    </p>
  );
}

function Props({ rows }: { rows: [string, string][] }) {
  return (
    <dl className="space-y-2.5">
      {rows.map(([k, v]) => (
        <div key={k} className="flex justify-between gap-3">
          <dt className="text-muted-foreground">{k}</dt>
          <dd className="truncate text-right">{v}</dd>
        </div>
      ))}
    </dl>
  );
}

const DECISION: Record<string, string> = { answer: "Answered", ask: "Asked for details", ticket: "Raised ticket" };

export function Transcript({ messages }: { messages: Message[] }) {
  return (
    <ol className="space-y-5">
      {messages.map((m) => {
        const sources: SourceRef[] = m.SourcesJson ? JSON.parse(m.SourcesJson) : [];
        return (
          <li key={m.ID} className={cn("flex gap-3", m.Role === "user" && "flex-row-reverse")}>
            <span className={cn("grid size-7 shrink-0 place-items-center rounded-full", m.Role === "user" ? "border bg-surface text-muted-foreground" : "bg-signal-soft text-signal")} aria-hidden>
              {m.Role === "user" ? <UserIcon className="size-3.5" /> : <Bot className="size-3.5" />}
            </span>
            <div className={cn("min-w-0 max-w-xl", m.Role === "user" && "text-right")}>
              <div className={cn("inline-block rounded-xl px-3.5 py-2.5 text-left", m.Role === "user" ? "bg-surface-3" : "border bg-surface")}>
                <RichText compact>{m.Content}</RichText>
              </div>
              <p className="mt-1 flex flex-wrap items-center gap-x-2 gap-y-1 text-2xs text-subtle-foreground">
                {when(m.CreatedOn)}
                {m.Decision && <Tag>{DECISION[m.Decision] ?? m.Decision}</Tag>}
                {m.Model && <span>{m.Model}</span>}
                {m.LatencyMs ? <span>{(m.LatencyMs / 1000).toFixed(1)}s</span> : null}
                {m.Feedback === 1 && <span className="text-success">Helpful</span>}
                {m.Feedback === -1 && <span className="text-destructive">Not helpful</span>}
                {sources.map((s) => <Tag key={s.Slug}>{pageTitle(s.Title)}</Tag>)}
              </p>
            </div>
          </li>
        );
      })}
    </ol>
  );
}
