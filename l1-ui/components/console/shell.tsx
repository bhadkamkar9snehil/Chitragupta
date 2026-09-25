"use client";

import { useEffect, useState } from "react";
import { Command } from "cmdk";
import {
  BarChart3, Bot, Gauge, Inbox, KanbanSquare, MessagesSquare, Moon, Radio, Search, Settings as SettingsIcon, ShieldAlert, Sun,
  Ticket as TicketIcon, UserRound, Wrench,
} from "lucide-react";
import { api, type Ticket, type User } from "@/lib/api";
import { displayName, ticketLabel } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Avatar, Dialog, Kbd, SearchInput, StatePill, Tip, TooltipProvider } from "@/components/ui/primitives";
import { applyBrand, BrandMark } from "@/components/helpdesk/app";
import { InboxView } from "./inbox";
import { ConversationsView } from "./conversations";
import { ReportsView } from "./reports";
import { SettingsView } from "./settings";
import { OverviewView } from "./overview";
import { LiveView } from "./live";
import { BoardView } from "./board";
import { RunsView } from "./runs";
import { L3View } from "./l3";
import { AgentsView } from "./agents";

// One route shape for the whole suite: #/<view>/<id>
export type View = "overview" | "live" | "board" | "inbox" | "conversations" | "runs" | "l3" | "agents" | "reports" | "settings";
export type ConsoleRoute = { view: View; id?: string | null };

const GROUPS: { label: string; items: { view: View; label: string; icon: typeof Inbox }[] }[] = [
  { label: "Operate", items: [
    { view: "overview", label: "Command centre", icon: Gauge },
    { view: "live", label: "Live engineer", icon: Radio },
    { view: "board", label: "Board", icon: KanbanSquare },
  ] },
  { label: "Desks", items: [
    { view: "inbox", label: "All tickets", icon: Inbox },
    { view: "conversations", label: "L1 · conversations", icon: MessagesSquare },
    { view: "runs", label: "L2 · runs", icon: Bot },
    { view: "l3", label: "L3 · escalations", icon: ShieldAlert },
  ] },
  { label: "System", items: [
    { view: "agents", label: "Agents & tools", icon: Wrench },
    { view: "reports", label: "Reports", icon: BarChart3 },
    { view: "settings", label: "Settings", icon: SettingsIcon },
  ] },
];
const ALL = GROUPS.flatMap((g) => g.items);

function parse(): ConsoleRoute {
  const [, view, id] = location.hash.replace(/^#\/?/, "/").split("/");
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
    const onKey = (e: KeyboardEvent) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        setPalette((p) => !p);
      }
    };
    window.addEventListener("keydown", onKey);
    return () => {
      clearTimeout(first);
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
        <nav aria-label="Suite" className="scrollbar-thin flex w-14 shrink-0 flex-col items-center overflow-y-auto border-r bg-surface py-3 xl:w-60 xl:items-stretch xl:px-2">
          <div className="px-1 pb-3 xl:px-2">
            <div className="flex items-center gap-2.5">
              <BrandMark name={brand} compact />
              <span className="hidden min-w-0 xl:block">
                <span className="block truncate text-sm font-semibold leading-tight">Helpdesk suite</span>
                <span className="block truncate text-2xs text-subtle-foreground">{brand}</span>
              </span>
            </div>
          </div>
          <button onClick={() => setPalette(true)} className="mb-2 hidden h-9 items-center gap-2 rounded-md border bg-background px-2.5 text-meta text-subtle-foreground hover:border-border-strong xl:flex">
            <Search className="size-4" aria-hidden /> Search
            <span className="ml-auto flex gap-0.5"><Kbd>Ctrl</Kbd><Kbd>K</Kbd></span>
          </button>
          {GROUPS.map((g) => (
            <div key={g.label} className="mt-2 w-full">
              <p className="hidden px-2.5 pb-1 pt-2 text-2xs font-semibold uppercase tracking-wider text-subtle-foreground xl:block">{g.label}</p>
              <div className="space-y-0.5">
                {g.items.map((n) => (
                  <Tip key={n.view} label={n.label} side="right">
                    <button
                      onClick={() => go(n.view)}
                      aria-current={route.view === n.view ? "page" : undefined}
                      aria-label={n.label}
                      className={cn(
                        "mx-auto flex size-11 items-center justify-center gap-2.5 rounded-md text-sm font-medium text-muted-foreground hover:bg-surface-2 hover:text-foreground xl:h-9 xl:w-full xl:justify-start xl:px-2.5",
                        route.view === n.view && "bg-surface-2 text-foreground",
                      )}
                    >
                      <n.icon className={cn("size-4.5 xl:size-4", n.view === "live" && "text-destructive")} aria-hidden />
                      <span className="hidden xl:inline">{n.label}</span>
                    </button>
                  </Tip>
                ))}
              </div>
            </div>
          ))}
          <div className="mt-auto w-full space-y-0.5 pt-3">
            <button onClick={() => setPicking(true)} className="mx-auto flex size-11 items-center justify-center gap-2.5 rounded-md text-left hover:bg-surface-2 xl:h-auto xl:w-full xl:justify-start xl:p-2" aria-label="Choose who you are">
              {engineer ? <Avatar name={displayName(engineer)} className="size-7" /> : <UserRound className="size-4 text-muted-foreground" aria-hidden />}
              <span className="hidden min-w-0 xl:block">
                <span className="block truncate text-meta font-medium">{engineer ? displayName(engineer) : "Choose who you are"}</span>
                <span className="block text-2xs text-subtle-foreground">{engineer ? "Acting engineer" : "Needed for L3 actions"}</span>
              </span>
            </button>
            <button
              onClick={() => {
                const dark = !document.documentElement.classList.contains("dark");
                document.documentElement.classList.toggle("dark", dark);
                safe(() => localStorage.setItem("l1.theme", dark ? "dark" : "light"), undefined);
              }}
              aria-label="Switch theme"
              className="mx-auto flex size-11 items-center justify-center gap-2.5 rounded-md text-sm text-muted-foreground hover:bg-surface-2 xl:h-9 xl:w-full xl:justify-start xl:px-2.5"
            >
              <Moon className="size-4 dark:hidden" aria-hidden />
              <Sun className="hidden size-4 dark:block" aria-hidden />
              <span className="hidden xl:inline">Theme</span>
            </button>
          </div>
        </nav>

        <main className="flex min-w-0 flex-1 flex-col">
          {route.view === "overview" && (
            <OverviewView go={{ live: () => go("live"), l1: () => go("conversations"), runs: () => go("runs"), l3: () => go("l3"), tickets: () => go("inbox"), ticket: (id) => go("inbox", id), run: (id) => go("runs", id) }} />
          )}
          {route.view === "live" && <LiveView runId={route.id ?? null} onRun={setId} onOpenRun={(id) => go("runs", id)} />}
          {route.view === "board" && <BoardView onOpenTicket={(id) => go("inbox", id)} onOpenRun={(id) => go("runs", id)} />}
          {route.view === "inbox" && <InboxView ticketId={route.id ?? null} onSelect={setId} />}
          {route.view === "conversations" && <ConversationsView sessionId={route.id ?? null} onSelect={setId} onOpenTicket={(id) => go("inbox", id)} />}
          {route.view === "runs" && <RunsView runId={route.id ?? null} onSelect={setId} onLive={(id) => go("live", id)} />}
          {route.view === "l3" && (
            <L3View escalationId={route.id ?? null} onSelect={setId} engineer={engineer} askEngineer={() => setPicking(true)} onOpenRun={(id) => go("runs", id)} onOpenTicket={(id) => go("inbox", id)} />
          )}
          {route.view === "agents" && <AgentsView onOpenRun={(id) => go("runs", id)} />}
          {route.view === "reports" && <ReportsView />}
          {route.view === "settings" && <SettingsView tab={route.id ?? undefined} onTab={setId} />}
        </main>
      </div>
      <Palette open={palette} onOpenChange={setPalette} go={go} />
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

function Palette({ open, onOpenChange, go }: { open: boolean; onOpenChange: (o: boolean) => void; go: (v: View, id?: string | null) => void }) {
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
