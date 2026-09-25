"use client";

import { useEffect, useMemo, useState } from "react";
import { AlertCircle, ArrowLeft, Bot, CheckCircle2, Clock, Copy, Headset, Inbox, Layers, PanelLeftClose, PanelLeftOpen, RefreshCw, User as UserIcon } from "lucide-react";
import { toast } from "sonner";
import { api, type Message, type SourceRef, type Ticket } from "@/lib/api";
import { ago, human, outcomeLabel, pageTitle, RESPONSE_KIND, ticketLabel, when, whenShort } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Avatar, Empty, SearchInput, Skeleton, StatePill, Tag, Tip } from "@/components/ui/primitives";
import { RichText } from "@/components/helpdesk/rich-text";

const VIEWS = [
  { id: "", label: "All", icon: Layers },
  { id: "attention", label: "Waiting on requester", icon: AlertCircle },
  { id: "pending", label: "Being investigated", icon: Clock },
  { id: "progress", label: "With support team", icon: Headset },
  { id: "done", label: "Resolved", icon: CheckCircle2 },
];

export function InboxView({ ticketId, onSelect }: { ticketId: string | null; onSelect: (id: string | null) => void }) {
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
      <section aria-label="Tickets" className={cn("flex min-h-0 w-full flex-col border-r bg-surface md:w-80 md:shrink-0 xl:w-96", ticketId && "hidden", drawerOpen && "md:flex", !drawerOpen && "md:hidden")}>
        <div className="space-y-2 border-b px-3 py-3">
          <div className="flex items-center gap-2">
            <h1 className="flex-1 text-title font-semibold tracking-tight">{VIEWS.find((v) => v.id === view)!.label}</h1>
            {ticketId && <Button variant="ghost" size="icon-sm" className="hidden md:inline-flex" onClick={() => setCollapsedTicketId(ticketId)} aria-label="Hide ticket list"><PanelLeftClose /></Button>}
            <Tip label="Refresh">
              <Button variant="ghost" size="icon-sm" aria-label="Refresh" onClick={() => setTick((n) => n + 1)}>
                <RefreshCw />
              </Button>
            </Tip>
          </div>
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
            <li key={t.ID} className="border-b">
              <button
                onClick={() => onSelect(t.ID)}
                aria-current={ticketId === t.ID ? "true" : undefined}
                className={cn("relative flex w-full gap-3 px-3 py-3 text-left hover:bg-surface-2", ticketId === t.ID && "bg-primary-soft/60 hover:bg-primary-soft/60")}
              >
                {ticketId === t.ID && <span className="absolute inset-y-2 left-0 w-0.5 rounded-full bg-primary" aria-hidden />}
                <Avatar name={t.FirstLastName || t.EmailID || "?"} className="mt-0.5 size-7" />
                <span className="min-w-0 flex-1">
                  <span className="flex items-baseline gap-2">
                    <span className="truncate text-meta font-medium">{t.FirstLastName || t.EmailID}</span>
                    <span className="ml-auto shrink-0 text-2xs text-subtle-foreground">{ago(t.ModifiedOn ?? t.CreatedOn)}</span>
                  </span>
                  <span className="mt-0.5 line-clamp-2 text-meta leading-snug text-muted-foreground">
                    <span className="font-mono text-2xs text-subtle-foreground">{ticketLabel(t.TicketNo)}</span> {t.BriefDetails}
                  </span>
                  <span className="mt-1.5 flex flex-wrap items-center gap-1.5">
                    <StatePill tone={t.StateTone}>{t.StateLabel}</StatePill>
                    {t.Channel === "Helpdesk chat" && <Tag>Chat</Tag>}
                    {t.Priority && !t.Priority.startsWith("Standard") && <Tag>{t.Priority.replace(" Priority", "")}</Tag>}
                  </span>
                </span>
              </button>
            </li>
          ))}
          {rows && !shown.length && (
            <li><Empty icon={<Inbox className="size-5" />} title="No tickets here">Change the view or filters.</Empty></li>
          )}
        </ul>
      </section>

      <div className={cn("min-h-0 min-w-0 flex-1 flex-col", ticketId ? "flex" : "hidden md:flex")}>
        {ticketId ? (
          <TicketWorkspace key={ticketId} id={ticketId} onBack={() => onSelect(null)} drawerOpen={drawerOpen} onDrawerToggle={() => setCollapsedTicketId((current) => current === ticketId ? null : ticketId)} />
        ) : (
          <Empty className="m-auto" icon={<Inbox className="size-5" />} title="Pick a ticket">Its activity, the chat that raised it, and the L2 runs appear here.</Empty>
        )}
      </div>
    </div>
  );
}

function TicketWorkspace({ id, onBack, drawerOpen, onDrawerToggle }: { id: string; onBack: () => void; drawerOpen: boolean; onDrawerToggle: () => void }) {
  const [t, setT] = useState<Ticket | null>(null);
  const [tab, setTab] = useState<"activity" | "chat" | "runs">("activity");

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
  const tabs = [
    { id: "activity" as const, label: "Activity", n: t.Timeline?.length ?? 0 },
    { id: "chat" as const, label: "Chat transcript", n: t.Transcript?.length ?? 0 },
    { id: "runs" as const, label: "L2 runs", n: t.Runs?.length ?? 0 },
  ];

  return (
    <div className="flex min-h-0 flex-1">
      <div className="flex min-h-0 min-w-0 flex-1 flex-col">
        <header className="shrink-0 border-b bg-surface px-4 pt-3">
          <div className="flex items-start gap-2">
            <Button variant="ghost" size="icon-sm" className="md:hidden" aria-label="Back" onClick={onBack}>
              <ArrowLeft />
            </Button>
            <Button variant="ghost" size="icon-sm" className="hidden md:inline-flex" aria-label={drawerOpen ? "Hide ticket list" : "Show ticket list"} onClick={onDrawerToggle}>
              {drawerOpen ? <PanelLeftClose /> : <PanelLeftOpen />}
            </Button>
            <div className="min-w-0 flex-1">
              <div className="flex flex-wrap items-center gap-2">
                <button
                  className="font-mono text-xs text-muted-foreground hover:text-foreground"
                  onClick={() => {
                    navigator.clipboard.writeText(t.TicketNo).catch(() => {});
                    toast.success("Ticket number copied");
                  }}
                >
                  {t.TicketNo} <Copy className="inline size-3" aria-hidden />
                </button>
                <StatePill tone={t.StateTone}>{t.StateLabel}</StatePill>
              </div>
              <h2 className="mt-1 text-title font-semibold leading-snug tracking-tight">{t.BriefDetails}</h2>
              <p className="mt-1 flex flex-wrap gap-x-3 text-xs text-muted-foreground 2xl:hidden">
                <span>{t.FirstLastName || t.EmailID}</span>
                <span>{t.Area ?? "No area"} · {t.Type ?? "No type"}</span>
                <span>{t.Priority?.replace(" Priority", "") ?? "Standard"}</span>
                <span>Raised {when(t.CreatedOn)}</span>
              </p>
            </div>
          </div>
          <div className="-mb-px mt-3 flex gap-4" role="tablist">
            {tabs.map((x) => (
              <button
                key={x.id}
                role="tab"
                aria-selected={tab === x.id}
                onClick={() => setTab(x.id)}
                className={cn("flex h-9 items-center gap-1.5 border-b-2 border-transparent text-meta font-medium text-muted-foreground hover:text-foreground", tab === x.id && "border-primary text-foreground")}
              >
                {x.label}
                <span className="rounded bg-surface-3 px-1.5 text-2xs tabular-nums">{x.n}</span>
              </button>
            ))}
          </div>
        </header>
        <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto px-4 py-5 lg:px-8">
          <div className={cn(tab === "runs" ? "w-full" : "mx-auto max-w-3xl")}>
            {tab === "activity" && (
              <ol className="space-y-5">
                {t.Timeline?.map((item, i) => {
                  const support = item.Actor === "support";
                  return (
                    <li key={i} className="flex gap-3">
                      <span className={cn("grid size-8 shrink-0 place-items-center rounded-full", support ? "bg-primary text-primary-foreground" : "border bg-surface text-muted-foreground")} aria-hidden>
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
            {tab === "runs" && (
              t.Runs?.length ? (
                <div className="overflow-x-auto rounded-xl border bg-surface">
                  <table className="w-full min-w-4xl text-meta">
                    <thead className="bg-surface-2 text-left text-2xs uppercase tracking-wider text-subtle-foreground">
                      <tr>
                        <th className="w-20 px-4 py-3 font-semibold">Attempt</th>
                        <th className="w-32 px-4 py-3 font-semibold">State</th>
                        <th className="w-44 px-4 py-3 font-semibold">Outcome</th>
                        <th className="px-4 py-3 font-semibold">Route</th>
                        <th className="w-48 px-4 py-3 font-semibold">Claimed</th>
                        <th className="w-48 px-4 py-3 font-semibold">Completed</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y">
                      {t.Runs.map((r) => (
                        <tr key={r.ID} className="align-top">
                          <td className="px-4 py-3 font-mono text-xs tabular-nums">{r.AttemptNo}</td>
                          <td className="px-4 py-3">{human(r.ProcessStatus)}</td>
                          <td className="px-4 py-3 font-medium">{outcomeLabel(r.ResponseType)}</td>
                          <td className="px-4 py-3 text-muted-foreground">{human(r.Route) || "—"}</td>
                          <td className="whitespace-nowrap px-4 py-3 text-muted-foreground">{when(r.ClaimedOn)}</td>
                          <td className="whitespace-nowrap px-4 py-3 text-muted-foreground">{when(r.CompletedOn)}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              ) : (
                <Empty icon={<Clock className="size-5" />} title="Not picked up yet">The L2 pipeline claims new tickets within a couple of minutes.</Empty>
              )
            )}
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
            <span className={cn("grid size-7 shrink-0 place-items-center rounded-full", m.Role === "user" ? "border bg-surface text-muted-foreground" : "bg-primary text-primary-foreground")} aria-hidden>
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
