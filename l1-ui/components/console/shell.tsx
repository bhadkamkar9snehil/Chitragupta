"use client";

import { useCallback, useEffect, useState } from "react";
import { Command } from "cmdk";
import {
  BarChart3, Bot, MoreHorizontal, FileJson2, HeartPulse, MessageSquarePlus, Gauge, Inbox, KanbanSquare, MessagesSquare, Moon, PanelLeftClose, PanelLeftOpen, Radio, Search, Settings as SettingsIcon, ShieldAlert, Sun,
  Ticket as TicketIcon, UserRound, Wrench,
} from "lucide-react";
import { api, type Ticket, type User } from "@/lib/api";
import { displayName, ticketLabel } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Avatar, Dialog, Kbd, SearchInput, StatePill, Tip, TooltipProvider } from "@/components/ui/primitives";
import { applyBrand, BrandMark } from "@/components/helpdesk/app";
import { InboxView } from "./inbox";
import { ConversationsView, VIEWS as CONVERSATION_VIEWS, type ViewId } from "./conversations";
import { ReportsView } from "./reports";
import { SettingsView } from "./settings";
import { OverviewView } from "./overview";
import { LiveView } from "./live";
import { BoardView } from "./board";
import { RunsView } from "./runs";
import { L3View } from "./l3";
import { AgentsView } from "./agents";
import { LogsView } from "./logs";
import { HealthView } from "./health";

// One route shape for the whole suite: #/<view>/<id>
export type View = "overview" | "live" | "board" | "inbox" | "conversations" | "runs" | "l3" | "agents" | "health" | "logs" | "reports" | "settings";
export type ConsoleRoute = { view: View; id?: string | null };

const GROUPS: { label: string; items: { view: View; label: string; icon: typeof Inbox }[] }[] = [
  { label: "Operate", items: [
    { view: "overview", label: "Command centre", icon: Gauge },
    { view: "live", label: "Live engineer", icon: Radio },
    { view: "board", label: "Board", icon: KanbanSquare },
  ] },
  { label: "Desks", items: [
    { view: "inbox", label: "Tickets", icon: Inbox },
    { view: "conversations", label: "L1 · Conversations", icon: MessagesSquare },
    { view: "runs", label: "L2 · Investigations", icon: Bot },
    { view: "l3", label: "L3 · Escalations", icon: ShieldAlert },
  ] },
  { label: "System", items: [
    { view: "health", label: "Pipeline health", icon: HeartPulse },
    { view: "agents", label: "Agents & tools", icon: Wrench },
    { view: "logs", label: "Runtime logs", icon: FileJson2 },
    { view: "reports", label: "Reports", icon: BarChart3 },
    { view: "settings", label: "Settings", icon: SettingsIcon },
  ] },
];
const ALL = GROUPS.flatMap((g) => g.items);

function parse(): ConsoleRoute {
  const [, raw, id] = location.hash.replace(/^#\/?/, "/").split("/");
  if (raw === "chat") return { view: "conversations", id: id ? decodeURIComponent(id) : "new" };
  const view = raw;
  return ALL.some((n) => n.view === view) ? { view: view as View, id: id ? decodeURIComponent(id) : null } : { view: "overview" };
}

const ENGINEER_KEY = "desk.engineer";


const safe = <T,>(fn: () => T, fallback: T) => {
  try {
    return fn();
  } catch {
    return fallback;
  }
};

export function Console() {
  const [route, setRoute] = useState<ConsoleRoute>({ view: "overview" });
  const [palette, setPalette] = useState(false);
  const [brand, setBrand] = useState("XBatch Helpdesk");
  const [engineer, setEngineer] = useState<User | null>(null);
  const [picking, setPicking] = useState(false);
  const [more, setMore] = useState(false);
  const [navCollapsed, setNavCollapsed] = useState(false);
  const [convView, setConvView] = useState<ViewId>("all");
  const [convCounts, setConvCounts] = useState<Partial<Record<ViewId, number>>>({});
  const onConvCounts = useCallback((c: Partial<Record<ViewId, number>>) => setConvCounts(c), []);

  useEffect(() => {
    const sync = () => setRoute(parse());
    const first = setTimeout(sync, 0);
    window.addEventListener("hashchange", sync);
    api.config().then((c) => {
      setBrand(c.widget.name);
      applyBrand(c.widget.accent);
    }).catch(() => {});
    const id = safe(() => localStorage.getItem(ENGINEER_KEY), null);
    if (id) api.user(id).then(setEngineer).catch(() => {});
    const navTimer = setTimeout(() => setNavCollapsed(safe(() => localStorage.getItem("desk.nav.collapsed") === "1", false)), 0);
    const onKey = (e: KeyboardEvent) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        setPalette((p) => !p);
      }
    };
    window.addEventListener("keydown", onKey);
    return () => {
      clearTimeout(first);
      clearTimeout(navTimer);
      window.removeEventListener("hashchange", sync);
      window.removeEventListener("keydown", onKey);
    };
  }, []);

  const go = (view: View, id?: string | null) => {
    setRoute({ view, id: id ?? null });
    history.replaceState(null, "", `#/${view}${id ? `/${encodeURIComponent(id)}` : ""}`);
  };
  const setId = (id: string | null) => go(route.view, id);

  return (
    <TooltipProvider>
      <div className="flex h-dvh overflow-hidden bg-background">
        <nav aria-label="Suite" className={cn("scrollbar-thin hidden w-16 shrink-0 flex-col md:flex items-center overflow-y-auto border-r bg-canvas py-3 *:shrink-0", !navCollapsed && "xl:w-60 xl:items-stretch xl:px-2")}>
          <div className={cn("flex w-full items-center justify-center gap-2.5 pb-3", !navCollapsed && "xl:justify-start xl:px-3")}>
            <BrandMark name={brand} compact />
            {!navCollapsed && (
              <span className="hidden min-w-0 flex-1 xl:block">
                <span className="block truncate text-sm font-semibold leading-tight">Helpdesk suite</span>
                <span className="block truncate text-2xs text-subtle-foreground">{brand}</span>
              </span>
            )}
          </div>
          {navCollapsed ? (
            <Tip label="Search" side="right">
              <button onClick={() => setPalette(true)} className="mb-2 hidden size-10 place-items-center rounded-lg bg-surface-2 text-subtle-foreground hover:bg-surface-3 hover:text-foreground xl:grid" aria-label="Search">
                <Search className="size-4" aria-hidden />
              </button>
            </Tip>
          ) : (
            <button onClick={() => setPalette(true)} className="mb-2 hidden h-9 items-center gap-2 rounded-md border bg-background px-2.5 text-meta text-subtle-foreground hover:border-border-strong xl:flex">
              <Search className="size-4" aria-hidden /> Search
              <span className="ml-auto flex gap-0.5"><Kbd>Ctrl</Kbd><Kbd>K</Kbd></span>
            </button>
          )}
          <Tip label="Start a chat in the helpdesk" side="right">
            <button
              onClick={() => go("conversations", "new")}
              aria-label="New chat"
              aria-current={route.view === "conversations" && route.id === "new" ? "page" : undefined}
              className={cn("mx-auto mb-1 flex size-10 items-center justify-center gap-2 rounded-lg bg-foreground text-sm font-medium text-background hover:opacity-90", !navCollapsed && "xl:h-9 xl:w-full xl:rounded-full", route.view === "conversations" && route.id === "new" && "ring-2 ring-ring ring-offset-2 ring-offset-canvas")}
            >
              <MessageSquarePlus className="size-4" aria-hidden />
              {!navCollapsed && <span className="hidden xl:inline">New chat</span>}
            </button>
          </Tip>
          {GROUPS.map((g, groupIndex) => (
            <div key={g.label} className={cn("w-full", navCollapsed ? "py-1" : "mt-2", navCollapsed && groupIndex > 0 && "mt-1 border-t pt-2")}>
              {!navCollapsed && <p className="hidden px-2.5 pb-1 pt-2 text-2xs font-semibold uppercase tracking-wider text-subtle-foreground xl:block">{g.label}</p>}
              <div className="space-y-0.5">
                {g.items.flatMap((n) => [
                  <Tip key={n.view} label={n.label} side="right">
                    <button
                      onClick={() => go(n.view)}
                      aria-current={route.view === n.view ? "page" : undefined}
                      aria-label={n.label}
                      className={cn(
                        "mx-auto flex size-10 items-center justify-center gap-2.5 rounded-lg text-sm font-medium text-muted-foreground hover:bg-surface-2 hover:text-foreground",
                        !navCollapsed && "xl:h-9 xl:w-full xl:justify-start xl:px-2.5",
                        route.view === n.view && (navCollapsed ? "bg-signal-soft text-signal" : "bg-surface-2 text-foreground"),
                      )}
                    >
                      <n.icon className={cn("size-4.5 xl:size-4", n.view === "live" && "text-signal")} aria-hidden />
                      {!navCollapsed && <span className="hidden xl:inline">{n.label}</span>}
                    </button>
                  </Tip>,
                ].concat(n.view === "conversations" && route.view === "conversations" && !navCollapsed ? [
                  // Conversation views nest under their nav item (one sidebar, as in Libredesk).
                  <ul key="conv-views" className="ml-4 hidden space-y-0.5 border-l pl-2 xl:block" aria-label="Conversation views">
                    {CONVERSATION_VIEWS.map((v) => (
                      <li key={v.id}>
                        <button
                          onClick={() => { setConvView(v.id); go("conversations"); }}
                          aria-current={convView === v.id ? "page" : undefined}
                          className={cn("flex h-8 w-full items-center gap-2 rounded-md px-2 text-left text-meta text-muted-foreground hover:bg-surface-2 hover:text-foreground", convView === v.id && "bg-surface-3 text-foreground")}
                        >
                          <span className="min-w-0 flex-1 truncate">{v.label}</span>
                          <span className="font-mono text-2xs tabular-nums text-subtle-foreground">{v.id === "mine" && !engineer ? "—" : convCounts[v.id] ?? ""}</span>
                        </button>
                      </li>
                    ))}
                  </ul>,
                ] : []))}
              </div>
            </div>
          ))}
          <div className="mt-auto w-full space-y-0.5 pt-3">
            <button onClick={() => setPicking(true)} className={cn("mx-auto flex size-10 items-center justify-center gap-2.5 rounded-lg text-left hover:bg-surface-2", !navCollapsed && "xl:h-auto xl:w-full xl:justify-start xl:p-2")} aria-label="Choose who you are">
              {engineer ? <Avatar name={displayName(engineer)} className="size-7" /> : <UserRound className="size-4 text-muted-foreground" aria-hidden />}
              {!navCollapsed && <span className="hidden min-w-0 xl:block">
                <span className="block truncate text-meta font-medium">{engineer ? displayName(engineer) : "Choose who you are"}</span>
                <span className="block text-2xs text-subtle-foreground">{engineer ? "Acting engineer" : "Needed for L3 actions"}</span>
              </span>}
            </button>
            <button
              onClick={() => {
                setNavCollapsed(!navCollapsed);
                safe(() => localStorage.setItem("desk.nav.collapsed", navCollapsed ? "0" : "1"), undefined);
              }}
              aria-label={navCollapsed ? "Expand navigation" : "Collapse navigation"}
              className={cn("mx-auto hidden size-10 items-center justify-center gap-2.5 rounded-lg text-sm text-muted-foreground hover:bg-surface-2 xl:flex", !navCollapsed && "xl:h-9 xl:w-full xl:justify-start xl:px-2.5")}
            >
              {navCollapsed ? <PanelLeftOpen className="size-4" aria-hidden /> : <PanelLeftClose className="size-4" aria-hidden />}
              {!navCollapsed && <span>Collapse</span>}
            </button>
            <button
              onClick={() => {
                const dark = !document.documentElement.classList.contains("dark");
                document.documentElement.classList.toggle("dark", dark);
                safe(() => localStorage.setItem("l1.theme", dark ? "dark" : "light"), undefined);
              }}
              aria-label="Switch theme"
              className={cn("mx-auto flex size-10 items-center justify-center gap-2.5 rounded-lg text-sm text-muted-foreground hover:bg-surface-2", !navCollapsed && "xl:h-9 xl:w-full xl:justify-start xl:px-2.5")}
            >
              <Moon className="size-4 dark:hidden" aria-hidden />
              <Sun className="hidden size-4 dark:block" aria-hidden />
              {!navCollapsed && <span className="hidden xl:inline">Theme</span>}
            </button>
          </div>
        </nav>

        <main className="flex min-w-0 flex-1 flex-col pb-16 md:pb-0">
          {route.view === "overview" && (
            <OverviewView go={{ live: () => go("live"), l1: () => go("conversations"), runs: () => go("runs"), l3: () => go("l3"), tickets: () => go("inbox"), ticket: (id) => go("inbox", id), run: (id) => go("runs", id) }} />
          )}
          {route.view === "live" && <LiveView key={route.id ? "replay" : "live"} runId={route.id ?? null} onRun={setId} onOpenRun={(id) => go("runs", id)} />}
          {route.view === "board" && <BoardView onOpenTicket={(id) => go("inbox", id)} onOpenRun={(id) => go("runs", id)} />}
          {route.view === "inbox" && <InboxView ticketId={route.id ?? null} onSelect={setId} onOpenRun={(id) => go("runs", id)} />}
          {route.view === "conversations" && <ConversationsView view={convView} onView={setConvView} onCounts={onConvCounts} showPicker={navCollapsed} sessionId={route.id ?? null} onSelect={setId} onOpenTicket={(id) => go("inbox", id)} onOpenRun={(id) => go("runs", id)} engineer={engineer} askEngineer={() => setPicking(true)} />}
          {route.view === "runs" && <RunsView runId={route.id ?? null} onSelect={setId} onLive={(id) => go("live", id)} onOpenTicket={(id) => go("inbox", id)} onOpenL3={() => go("l3")} />}
          {route.view === "l3" && (
            <L3View escalationId={route.id ?? null} onSelect={setId} engineer={engineer} askEngineer={() => setPicking(true)} onOpenRun={(id) => go("runs", id)} onOpenTicket={(id) => go("inbox", id)} />
          )}
          {route.view === "agents" && <AgentsView onOpenRun={(id) => go("runs", id)} />}
          {route.view === "health" && <HealthView onOpenRun={(id) => go("runs", id)} />}
          {route.view === "logs" && <LogsView />}
          {route.view === "reports" && <ReportsView />}
          {route.view === "settings" && <SettingsView tab={route.id ?? undefined} onTab={setId} />}
        </main>
        <MobileTabs view={route.view} go={go} onMore={() => setMore(true)} />
      </div>
      <Dialog open={more} onOpenChange={setMore} title="Menu" description={engineer ? `Acting as ${displayName(engineer)}` : "Choose who you are for L3 actions and chats"}>
        <div className="space-y-4">
          <div className="grid grid-cols-2 gap-2">
            <button onClick={() => { setMore(false); go("conversations", "new"); }} className="flex h-11 items-center justify-center gap-2 rounded-lg bg-foreground text-sm font-medium text-background"><MessageSquarePlus className="size-4" aria-hidden />New chat</button>
            <button onClick={() => { setMore(false); setPalette(true); }} className="flex h-11 items-center justify-center gap-2 rounded-lg border bg-surface text-sm"><Search className="size-4" aria-hidden />Search</button>
          </div>
          {GROUPS.map((g) => (
            <div key={g.label}>
              <p className="pb-1 font-mono text-2xs uppercase tracking-wider text-subtle-foreground">{g.label}</p>
              <div className="grid grid-cols-2 gap-1">
                {g.items.map((n) => (
                  <button key={n.view} onClick={() => { setMore(false); go(n.view); }} aria-current={route.view === n.view ? "page" : undefined}
                    className={cn("flex h-11 items-center gap-2 rounded-lg px-2.5 text-left text-sm text-muted-foreground hover:bg-surface-2", route.view === n.view && "bg-surface-3 text-foreground")}>
                    <n.icon className="size-4 shrink-0" aria-hidden /><span className="leading-tight">{n.label}</span>
                  </button>
                ))}
              </div>
            </div>
          ))}
          <div className="grid grid-cols-2 gap-2 border-t pt-3">
            <button onClick={() => { setMore(false); setPicking(true); }} className="flex h-11 items-center gap-2 rounded-lg px-2.5 text-sm text-muted-foreground hover:bg-surface-2"><UserRound className="size-4" aria-hidden />Who you are</button>
            <button onClick={() => { const dark = !document.documentElement.classList.contains("dark"); document.documentElement.classList.toggle("dark", dark); safe(() => localStorage.setItem("l1.theme", dark ? "dark" : "light"), undefined); }} className="flex h-11 items-center gap-2 rounded-lg px-2.5 text-sm text-muted-foreground hover:bg-surface-2"><Moon className="size-4 dark:hidden" aria-hidden /><Sun className="hidden size-4 dark:block" aria-hidden />Theme</button>
          </div>
        </div>
      </Dialog>
      <Palette open={palette} onOpenChange={setPalette} go={go} onChat={() => go("conversations", "new")} />
      <EngineerPicker
        open={picking}
        onOpenChange={setPicking}
        onPick={(u) => {
          safe(() => localStorage.setItem(ENGINEER_KEY, u.ID), undefined);
          setEngineer(u);
          setPicking(false);
        }}
      />
    </TooltipProvider>
  );
}

function EngineerPicker({ open, onOpenChange, onPick }: { open: boolean; onOpenChange: (o: boolean) => void; onPick: (u: User) => void }) {
  const [q, setQ] = useState("");
  const [users, setUsers] = useState<User[]>([]);
  useEffect(() => {
    if (!open) return;
    const t = setTimeout(() => api.users(q).then(setUsers).catch(() => {}), 150);
    return () => clearTimeout(t);
  }, [q, open]);
  return (
    <Dialog open={open} onOpenChange={onOpenChange} title="Who is working the desk?" description="Your XBatch account is recorded on L3 pick-ups, notes and resolutions.">
      <SearchInput autoFocus value={q} onChange={(e) => setQ(e.target.value)} placeholder="Search name or email" aria-label="Search accounts" />
      <ul className="scrollbar-thin mt-2 max-h-72 overflow-y-auto rounded-lg border">
        {users.map((u) => (
          <li key={u.ID} className="border-b last:border-0">
            <button onClick={() => onPick(u)} className="flex w-full items-center gap-3 px-3 py-2 text-left hover:bg-surface-2">
              <Avatar name={displayName(u)} className="size-7" />
              <span className="min-w-0">
                <span className="block truncate text-sm">{displayName(u)}</span>
                <span className="block truncate text-2xs text-muted-foreground">{u.EmailID ?? u.Name}</span>
              </span>
            </button>
          </li>
        ))}
      </ul>
    </Dialog>
  );
}

function Palette({ open, onOpenChange, go, onChat }: { open: boolean; onOpenChange: (o: boolean) => void; go: (v: View, id?: string | null) => void; onChat: () => void }) {
  const [q, setQ] = useState("");
  const [hits, setHits] = useState<Ticket[]>([]);

  useEffect(() => {
    if (!open) return;
    const t = setTimeout(() => {
      api.admin.tickets({ q: q || undefined }).then((r) => setHits(r.slice(0, 8))).catch(() => {});
    }, 150);
    return () => clearTimeout(t);
  }, [q, open]);

  const run = (v: View, id?: string) => {
    onOpenChange(false);
    setQ("");
    go(v, id);
  };
  const heading = "[&_[cmdk-group-heading]]:px-2 [&_[cmdk-group-heading]]:py-1.5 [&_[cmdk-group-heading]]:text-2xs [&_[cmdk-group-heading]]:font-semibold [&_[cmdk-group-heading]]:uppercase [&_[cmdk-group-heading]]:tracking-wider [&_[cmdk-group-heading]]:text-subtle-foreground";

  return (
    <Command.Dialog
      open={open}
      onOpenChange={onOpenChange}
      label="Search the suite"
      shouldFilter={false}
      overlayClassName="fixed inset-0 z-50 bg-black/40 animate-fade"
      contentClassName="fixed inset-x-4 top-24 z-50 mx-auto max-w-xl overflow-hidden rounded-xl border bg-surface shadow-pop animate-rise"
    >
      <div className="flex items-center gap-2 border-b px-3">
        <Search className="size-4 text-subtle-foreground" aria-hidden />
        <Command.Input value={q} onValueChange={setQ} placeholder="Ticket number, subject, requester, or a page…" className="h-12 flex-1 bg-transparent text-base outline-none placeholder:text-subtle-foreground focus-visible:outline-none sm:text-sm" />
        <Kbd>Esc</Kbd>
      </div>
      <Command.List className="scrollbar-thin max-h-96 overflow-y-auto p-1.5">
        <Command.Empty className="px-3 py-6 text-center text-sm text-muted-foreground">Nothing found.</Command.Empty>
        {hits.length > 0 && (
          <Command.Group heading="Tickets" className={heading}>
            {hits.map((t) => (
              <Command.Item key={t.ID} value={t.ID} onSelect={() => run("inbox", t.ID)} className="flex h-11 cursor-default items-center gap-3 rounded-md px-2 text-sm data-[selected=true]:bg-surface-2">
                <TicketIcon className="size-4 text-subtle-foreground" aria-hidden />
                <span className="w-12 font-mono text-xs text-muted-foreground">{ticketLabel(t.TicketNo)}</span>
                <span className="min-w-0 flex-1 truncate">{t.BriefDetails}</span>
                <StatePill tone={t.StateTone}>{t.StateLabel}</StatePill>
              </Command.Item>
            ))}
          </Command.Group>
        )}
        <Command.Group heading="Actions" className={heading}>
          <Command.Item value="new chat" onSelect={() => { onOpenChange(false); onChat(); }} className="flex h-10 cursor-default items-center gap-3 rounded-md px-2 text-sm data-[selected=true]:bg-surface-2">
            <MessageSquarePlus className="size-4 text-subtle-foreground" aria-hidden />
            Start a chat in the helpdesk
          </Command.Item>
        </Command.Group>
        <Command.Group heading="Go to" className={heading}>
          {ALL.filter((n) => !q || n.label.toLowerCase().includes(q.toLowerCase())).map((n) => (
            <Command.Item key={n.view} value={n.label} onSelect={() => run(n.view)} className="flex h-10 cursor-default items-center gap-3 rounded-md px-2 text-sm data-[selected=true]:bg-surface-2">
              <n.icon className="size-4 text-subtle-foreground" aria-hidden />
              {n.label}
            </Command.Item>
          ))}
        </Command.Group>
      </Command.List>
    </Command.Dialog>
  );
}

// Phones: the four desks people use most, everything else in the More sheet.
const TABS: { view: View; label: string; icon: typeof Inbox }[] = [
  { view: "overview", label: "Home", icon: Gauge },
  { view: "inbox", label: "Tickets", icon: Inbox },
  { view: "conversations", label: "Chats", icon: MessagesSquare },
  { view: "live", label: "Live", icon: Radio },
];

function MobileTabs({ view, go, onMore }: { view: View; go: (v: View) => void; onMore: () => void }) {
  const inTabs = TABS.some((t) => t.view === view);
  return (
    <nav aria-label="Suite" className="pb-safe fixed inset-x-0 bottom-0 z-40 grid grid-cols-5 border-t bg-canvas md:hidden">
      {TABS.map((t) => (
        <button key={t.view} onClick={() => go(t.view)} aria-current={view === t.view ? "page" : undefined}
          className={cn("flex h-16 flex-col items-center justify-center gap-1 text-2xs font-medium text-subtle-foreground", view === t.view && "text-signal")}>
          <t.icon className="size-5" aria-hidden />{t.label}
        </button>
      ))}
      <button onClick={onMore} className={cn("flex h-16 flex-col items-center justify-center gap-1 text-2xs font-medium text-subtle-foreground", !inTabs && "text-signal")}>
        <MoreHorizontal className="size-5" aria-hidden />More
      </button>
    </nav>
  );
}
