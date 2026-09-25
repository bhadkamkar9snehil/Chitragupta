"use client";

import { useEffect, useState } from "react";
import { Command } from "cmdk";
import { BarChart3, Inbox, MessagesSquare, Moon, Search, Settings as SettingsIcon, Sun, Ticket as TicketIcon } from "lucide-react";
import { api, type Ticket } from "@/lib/api";
import { ticketLabel } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Kbd, StatePill, TooltipProvider } from "@/components/ui/primitives";
import { applyBrand, BrandMark } from "@/components/helpdesk/app";
import { InboxView } from "./inbox";
import { ConversationsView } from "./conversations";
import { ReportsView } from "./reports";
import { SettingsView } from "./settings";

export type ConsoleRoute = { view: "inbox"; ticketId?: string | null } | { view: "conversations"; sessionId?: string | null } | { view: "reports" } | { view: "settings"; tab?: string };

const NAV = [
  { view: "inbox" as const, label: "Inbox", icon: Inbox, key: "1" },
  { view: "conversations" as const, label: "Conversations", icon: MessagesSquare, key: "2" },
  { view: "reports" as const, label: "Reports", icon: BarChart3, key: "3" },
  { view: "settings" as const, label: "Settings", icon: SettingsIcon, key: "4" },
];

function parse(): ConsoleRoute {
  const [, view, id] = location.hash.replace(/^#\/?/, "/").split("/");
  if (view === "conversations") return { view, sessionId: id || null };
  if (view === "reports") return { view };
  if (view === "settings") return { view, tab: id };
  return { view: "inbox", ticketId: id || null };
}

function hash(r: ConsoleRoute) {
  if (r.view === "inbox") return r.ticketId ? `#/inbox/${r.ticketId}` : "#/inbox";
  if (r.view === "conversations") return r.sessionId ? `#/conversations/${r.sessionId}` : "#/conversations";
  if (r.view === "settings") return r.tab ? `#/settings/${r.tab}` : "#/settings";
  return `#/${r.view}`;
}

export function Console() {
  const [route, setRoute] = useState<ConsoleRoute>({ view: "inbox" });
  const [palette, setPalette] = useState(false);
  const [brand, setBrand] = useState("XBatch Helpdesk");

  useEffect(() => {
    const sync = () => setRoute(parse());
    const first = setTimeout(sync, 0);
    window.addEventListener("hashchange", sync);
    api.config().then((c) => {
      setBrand(c.widget.name);
      applyBrand(c.widget.accent);
    }).catch(() => {});
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

  const go = (r: ConsoleRoute) => {
    setRoute(r);
    history.replaceState(null, "", hash(r));
  };

  return (
    <TooltipProvider>
      <div className="flex h-dvh overflow-hidden bg-background">
        <nav aria-label="Console" className="flex w-14 shrink-0 flex-col items-center border-r bg-surface py-3 xl:w-56 xl:items-stretch xl:px-2">
          <div className="px-1 pb-4 xl:px-2">
            <div className="flex items-center gap-2.5">
              <BrandMark name={brand} compact />
              <span className="hidden min-w-0 xl:block">
                <span className="block truncate text-sm font-semibold leading-tight">Support console</span>
                <span className="block truncate text-2xs text-subtle-foreground">{brand}</span>
              </span>
            </div>
          </div>
          <button
            onClick={() => setPalette(true)}
            className="mb-3 hidden h-9 items-center gap-2 rounded-md border bg-background px-2.5 text-meta text-subtle-foreground hover:border-border-strong xl:flex"
          >
            <Search className="size-4" aria-hidden /> Search
            <span className="ml-auto flex gap-0.5"><Kbd>Ctrl</Kbd><Kbd>K</Kbd></span>
          </button>
          <div className="space-y-0.5">
            {NAV.map((n) => (
              <button
                key={n.view}
                onClick={() => go({ view: n.view } as ConsoleRoute)}
                aria-current={route.view === n.view ? "page" : undefined}
                aria-label={n.label}
                className={cn(
                  "flex size-10 items-center justify-center gap-2.5 rounded-md text-sm font-medium text-muted-foreground hover:bg-surface-2 hover:text-foreground xl:h-9 xl:w-full xl:justify-start xl:px-2.5",
                  route.view === n.view && "bg-surface-2 text-foreground",
                )}
              >
                <n.icon className="size-4.5 xl:size-4" aria-hidden />
                <span className="hidden xl:inline">{n.label}</span>
              </button>
            ))}
          </div>
          <button
            onClick={() => {
              const dark = !document.documentElement.classList.contains("dark");
              document.documentElement.classList.toggle("dark", dark);
              try { localStorage.setItem("l1.theme", dark ? "dark" : "light"); } catch {}
            }}
            aria-label="Switch theme"
            className="mt-auto flex size-10 items-center justify-center gap-2.5 rounded-md text-sm text-muted-foreground hover:bg-surface-2 xl:h-9 xl:w-full xl:justify-start xl:px-2.5"
          >
            <Moon className="size-4 dark:hidden" aria-hidden />
            <Sun className="hidden size-4 dark:block" aria-hidden />
            <span className="hidden xl:inline">Theme</span>
          </button>
        </nav>

        <main className="flex min-w-0 flex-1 flex-col">
          {route.view === "inbox" && <InboxView ticketId={route.ticketId ?? null} onSelect={(id) => go({ view: "inbox", ticketId: id })} />}
          {route.view === "conversations" && <ConversationsView sessionId={route.sessionId ?? null} onSelect={(id) => go({ view: "conversations", sessionId: id })} onOpenTicket={(id) => go({ view: "inbox", ticketId: id })} />}
          {route.view === "reports" && <ReportsView />}
          {route.view === "settings" && <SettingsView tab={route.tab} onTab={(tab) => go({ view: "settings", tab })} />}
        </main>
      </div>
      <Palette open={palette} onOpenChange={setPalette} go={go} />
    </TooltipProvider>
  );
}

function Palette({ open, onOpenChange, go }: { open: boolean; onOpenChange: (o: boolean) => void; go: (r: ConsoleRoute) => void }) {
  const [q, setQ] = useState("");
  const [hits, setHits] = useState<Ticket[]>([]);

  useEffect(() => {
    if (!open) return;
    const t = setTimeout(() => {
      api.admin.tickets({ q: q || undefined }).then((r) => setHits(r.slice(0, 8))).catch(() => {});
    }, 150);
    return () => clearTimeout(t);
  }, [q, open]);

  const run = (r: ConsoleRoute) => {
    onOpenChange(false);
    setQ("");
    go(r);
  };

  return (
    <Command.Dialog
      open={open}
      onOpenChange={onOpenChange}
      label="Search the console"
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
          <Command.Group heading="Tickets" className="[&_[cmdk-group-heading]]:px-2 [&_[cmdk-group-heading]]:py-1.5 [&_[cmdk-group-heading]]:text-2xs [&_[cmdk-group-heading]]:font-semibold [&_[cmdk-group-heading]]:uppercase [&_[cmdk-group-heading]]:tracking-wider [&_[cmdk-group-heading]]:text-subtle-foreground">
            {hits.map((t) => (
              <Command.Item key={t.ID} value={t.ID} onSelect={() => run({ view: "inbox", ticketId: t.ID })} className="flex h-11 cursor-default items-center gap-3 rounded-md px-2 text-sm data-[selected=true]:bg-surface-2">
                <TicketIcon className="size-4 text-subtle-foreground" aria-hidden />
                <span className="w-12 font-mono text-xs text-muted-foreground">{ticketLabel(t.TicketNo)}</span>
                <span className="min-w-0 flex-1 truncate">{t.BriefDetails}</span>
                <StatePill tone={t.StateTone}>{t.StateLabel}</StatePill>
              </Command.Item>
            ))}
          </Command.Group>
        )}
        <Command.Group heading="Go to" className="[&_[cmdk-group-heading]]:px-2 [&_[cmdk-group-heading]]:py-1.5 [&_[cmdk-group-heading]]:text-2xs [&_[cmdk-group-heading]]:font-semibold [&_[cmdk-group-heading]]:uppercase [&_[cmdk-group-heading]]:tracking-wider [&_[cmdk-group-heading]]:text-subtle-foreground">
          {[...NAV.map((n) => ({ label: n.label, icon: n.icon, r: { view: n.view } as ConsoleRoute })),
            { label: "AI provider settings", icon: SettingsIcon, r: { view: "settings", tab: "ai" } as ConsoleRoute },
            { label: "Embed code", icon: SettingsIcon, r: { view: "settings", tab: "embed" } as ConsoleRoute }]
            .filter((n) => !q || n.label.toLowerCase().includes(q.toLowerCase()))
            .map((n) => (
              <Command.Item key={n.label} value={n.label} onSelect={() => run(n.r)} className="flex h-10 cursor-default items-center gap-3 rounded-md px-2 text-sm data-[selected=true]:bg-surface-2">
                <n.icon className="size-4 text-subtle-foreground" aria-hidden />
                {n.label}
              </Command.Item>
            ))}
        </Command.Group>
      </Command.List>
    </Command.Dialog>
  );
}
