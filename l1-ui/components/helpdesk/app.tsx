"use client";

import { createContext, useCallback, useContext, useEffect, useMemo, useState } from "react";
import { Home as HomeIcon, LogOut, MessageCircle, Moon, Sun, Ticket as TicketIcon } from "lucide-react";
import { api, ApiError, type Session, type Ticket, type User, type WidgetConfig } from "@/lib/api";
import { displayName } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Avatar, Menu, MenuContent, MenuItem, MenuSeparator, MenuTrigger, SearchInput, TooltipProvider } from "@/components/ui/primitives";
import { Home } from "./home";
import { Messages } from "./conversation";
import { Tickets } from "./tickets";

export type Route = { tab: "home" } | { tab: "messages"; sessionId: string | null; draft?: string } | { tab: "tickets"; ticketId: string | null };

type Ctx = {
  user: User;
  config: WidgetConfig;
  sessions: Session[];
  tickets: Ticket[];
  loaded: boolean;
  route: Route;
  go: (r: Route) => void;
  refresh: () => Promise<void>;
};

const HelpdeskContext = createContext<Ctx | null>(null);
export const useHelpdesk = () => useContext(HelpdeskContext)!;

const USER_KEY = "l1.user";
const safe = <T,>(fn: () => T, fallback: T) => {
  try {
    return fn();
  } catch {
    return fallback;
  }
};

export const DEFAULT_CONFIG: WidgetConfig = {
  name: "XBatch Helpdesk",
  greeting: "Tell us what is going wrong. We will answer straight away or hand it to the support team.",
  accent: "#4ceea8",
  suggestions: [],
};

export function applyBrand(accent?: string) {
  if (accent && /^#[0-9a-f]{3,8}$/i.test(accent)) document.documentElement.style.setProperty("--brand", accent);
}

export function HelpdeskApp() {
  const [config, setConfig] = useState<WidgetConfig>(DEFAULT_CONFIG);
  const [user, setUser] = useState<User | null>(null);
  const [state, setState] = useState<"booting" | "ready" | "offline">("booting");
  const [attempt, setAttempt] = useState(0);

  useEffect(() => {
    api.config().then((c) => {
      setConfig({ ...DEFAULT_CONFIG, ...c.widget });
      applyBrand(c.widget.accent);
    }).catch(() => {});
  }, []);

  useEffect(() => {
    // XStudio will pass the signed-in user as ?user=<XStudio user ID>; until then the pick is remembered per browser.
    const fromUrl = new URLSearchParams(location.search).get("user");
    const id = fromUrl || safe(() => localStorage.getItem(USER_KEY), null);
    Promise.resolve(id ? api.user(id).then(setUser) : null)
      .then(() => setState("ready"))
      .catch((e: Error) => {
        if (e instanceof ApiError && e.status === 404) {
          safe(() => localStorage.removeItem(USER_KEY), undefined);
          setState("ready");
        } else setState("offline");
      });
  }, [attempt]);

  if (state === "booting")
    return (
      <div className="grid h-dvh place-items-center">
        <span className="size-2 rounded-full bg-signal motion-safe:animate-ping" aria-label="Loading" />
      </div>
    );
  if (state === "offline")
    return (
      <div className="grid h-dvh place-items-center px-6 text-center">
        <div>
          <p className="font-medium">We can&apos;t reach the helpdesk right now.</p>
          <p className="mt-1 text-sm text-muted-foreground">Check your connection, then try again.</p>
          <Button className="mt-4" variant="outline" onClick={() => { setState("booting"); setAttempt((n) => n + 1); }}>
            Try again
          </Button>
        </div>
      </div>
    );
  if (!user)
    return (
      <SignIn
        config={config}
        onPick={(u) => {
          safe(() => localStorage.setItem(USER_KEY, u.ID), undefined);
          setUser(u);
        }}
      />
    );
  return (
    <TooltipProvider>
      <Workspace
        user={user}
        config={config}
        onSignOut={() => {
          safe(() => localStorage.removeItem(USER_KEY), undefined);
          setUser(null);
        }}
      />
    </TooltipProvider>
  );
}

function SignIn({ config, onPick }: { config: WidgetConfig; onPick: (u: User) => void }) {
  const [q, setQ] = useState("");
  const [users, setUsers] = useState<User[] | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const t = setTimeout(() => {
      api.users(q).then((u) => { setUsers(u); setError(""); }).catch((e: Error) => setError(e.message));
    }, 180);
    return () => clearTimeout(t);
  }, [q]);

  return (
    <main className="flex min-h-dvh flex-col items-center justify-center px-4 py-10">
      <div className="w-full max-w-sm animate-rise">
        <BrandMark name={config.name} />
        <h1 className="mt-6 text-heading font-semibold tracking-tight">Who&apos;s asking?</h1>
        <p className="mt-1 text-sm text-muted-foreground">Choose your XBatch account. Your conversations and tickets stay with it.</p>
        <SearchInput autoFocus size="lg" className="mt-5" value={q} onChange={(e) => setQ(e.target.value)} placeholder="Search name or email" aria-label="Search name or email" />
        {error && <p role="alert" className="mt-3 text-sm text-destructive">{error}</p>}
        <ul className="scrollbar-thin mt-2 max-h-96 overflow-y-auto rounded-lg border bg-surface" aria-label="Accounts">
          {users?.map((u) => (
            <li key={u.ID} className="border-b last:border-0">
              <button onClick={() => onPick(u)} className="flex min-h-13 w-full items-center gap-3 px-3 py-2.5 text-left hover:bg-surface-2 focus-visible:bg-surface-2 focus-visible:outline-none">
                <Avatar name={displayName(u)} />
                <span className="min-w-0">
                  <span className="block truncate text-sm font-medium">{displayName(u)}</span>
                  <span className="block truncate text-xs text-muted-foreground">{u.EmailID || u.Name}</span>
                </span>
              </button>
            </li>
          ))}
          {users && !users.length && <li className="px-3 py-8 text-center text-sm text-muted-foreground">No account matches &ldquo;{q}&rdquo;.</li>}
          {!users && !error && <li className="px-3 py-8 text-center text-sm text-muted-foreground">Loading accounts…</li>}
        </ul>
      </div>
    </main>
  );
}

export function BrandMark({ name, compact }: { name: string; compact?: boolean }) {
  return (
    <div className="flex items-center gap-2.5">
      <span className="grid size-8 place-items-center rounded-lg bg-signal text-canvas">
        <svg viewBox="0 0 24 24" className="size-4.5" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" aria-hidden>
          <path d="M4 17c3-6 5-9 8-9s5 3 8 9" />
          <path d="M8 21h8" />
          <circle cx="12" cy="4" r="1.2" fill="currentColor" stroke="none" />
        </svg>
      </span>
      {!compact && <span className="text-body font-semibold tracking-tight">{name}</span>}
    </div>
  );
}

// Deep links the embedding page can use: #/messages, #/messages/<id>, #/tickets, #/tickets/<id>
function parseHash(): Route {
  if (typeof location === "undefined") return { tab: "home" };
  const [, tab, id] = location.hash.replace(/^#\/?/, "/").split("/");
  if (tab === "messages") return { tab: "messages", sessionId: id || null };
  if (tab === "tickets") return { tab: "tickets", ticketId: id || null };
  return { tab: "home" };
}

function toHash(r: Route) {
  if (r.tab === "messages") return r.sessionId ? `#/messages/${r.sessionId}` : "#/messages";
  if (r.tab === "tickets") return r.ticketId ? `#/tickets/${r.ticketId}` : "#/tickets";
  return "";
}

// Inside the support console the same chat runs embedded: the console owns the URL, and ticket links open the
// console's own ticket record instead of the requester view.
export type Embed = { sessionId: string | null; onSession: (id: string | null) => void; onOpenTicket: (ticketId: string | null) => void };

function Workspace({ user, config, onSignOut, embed }: { user: User; config: WidgetConfig; onSignOut?: () => void; embed?: Embed }) {
  const [sessions, setSessions] = useState<Session[]>([]);
  const [tickets, setTickets] = useState<Ticket[]>([]);
  const [loaded, setLoaded] = useState(false);
  const [route, setRouteState] = useState<Route>(() => (embed ? { tab: "messages", sessionId: embed.sessionId } : parseHash()));
  const setRoute = useCallback((r: Route) => {
    if (embed) {
      if (r.tab === "tickets") return embed.onOpenTicket(r.ticketId);
      setRouteState(r.tab === "messages" ? r : { tab: "messages", sessionId: null });
      if (r.tab === "messages") embed.onSession(r.sessionId);
      return;
    }
    setRouteState(r);
    const hash = toHash(r);
    if (location.hash !== hash) history.replaceState(null, "", hash || location.pathname + location.search);
  }, [embed]);

  useEffect(() => {
    if (embed) return;
    const onHash = () => setRouteState(parseHash());
    window.addEventListener("hashchange", onHash);
    return () => window.removeEventListener("hashchange", onHash);
  }, [embed]);

  const refresh = useCallback(async () => {
    const [s, t] = await Promise.allSettled([api.sessions(user.ID), api.tickets(user.ID)]);
    if (s.status === "fulfilled") setSessions(s.value);
    if (t.status === "fulfilled") setTickets(t.value);
    setLoaded(true);
  }, [user.ID]);

  useEffect(() => {
    const first = setTimeout(refresh, 0);
    const poll = setInterval(refresh, 30_000);
    return () => {
      clearTimeout(first);
      clearInterval(poll);
    };
  }, [refresh]);

  const ctx = useMemo<Ctx>(() => ({ user, config, sessions, tickets, loaded, route, go: setRoute, refresh }), [user, config, sessions, tickets, loaded, route, setRoute, refresh]);
  const waiting = tickets.filter((t) => t.StateTone === "attention").length;
  const open = tickets.filter((t) => t.StateTone !== "done").length;

  const nav = [
    { tab: "home" as const, label: "Home", icon: HomeIcon, badge: 0, to: { tab: "home" } as Route },
    { tab: "messages" as const, label: "Messages", icon: MessageCircle, badge: 0, to: { tab: "messages", sessionId: null } as Route },
    { tab: "tickets" as const, label: "Tickets", icon: TicketIcon, badge: waiting, hint: open, to: { tab: "tickets", ticketId: null } as Route },
  ];

  if (embed)
    return (
      <HelpdeskContext.Provider value={ctx}>
        <Messages />
      </HelpdeskContext.Provider>
    );

  return (
    <HelpdeskContext.Provider value={ctx}>
      <div className="flex h-dvh overflow-hidden bg-background">
        {/* Rail: tablets and up */}
        <nav aria-label="Helpdesk" className="hidden w-60 shrink-0 flex-col border-r bg-canvas md:flex">
          <div className="px-4 pb-2 pt-4">
            <BrandMark name={config.name} />
          </div>
          <div className="space-y-0.5 px-2 pt-3">
            {nav.map((n) => (
              <button
                key={n.tab}
                onClick={() => setRoute(n.to)}
                aria-current={route.tab === n.tab ? "page" : undefined}
                className={cn(
                  "flex h-9 w-full items-center gap-2.5 rounded-md px-2.5 text-sm font-medium text-muted-foreground hover:bg-surface-2 hover:text-foreground",
                  route.tab === n.tab && "bg-surface-2 text-foreground",
                )}
              >
                <n.icon className="size-4" aria-hidden />
                {n.label}
                {n.badge > 0 ? (
                  <span className="ml-auto grid h-5 min-w-5 place-items-center rounded-full bg-warning px-1.5 text-2xs font-semibold text-white" aria-label={`${n.badge} need your reply`}>
                    {n.badge}
                  </span>
                ) : n.hint ? (
                  <span className="ml-auto text-xs text-subtle-foreground">{n.hint}</span>
                ) : null}
              </button>
            ))}
          </div>
          <div className="mt-auto border-t p-2">
            <AccountMenu user={user} onSignOut={onSignOut} />
          </div>
        </nav>

        <div className="flex min-w-0 flex-1 flex-col">
          <main className="flex min-h-0 flex-1 flex-col">
            {route.tab === "home" && <Home />}
            {route.tab === "messages" && <Messages />}
            {route.tab === "tickets" && <Tickets />}
          </main>
          {/* Bottom tabs: widget / phone width */}
          <nav aria-label="Helpdesk" className="grid shrink-0 grid-cols-3 border-t bg-canvas pb-safe md:hidden">
            {nav.map((n) => (
              <button
                key={n.tab}
                onClick={() => setRoute(n.to)}
                aria-current={route.tab === n.tab ? "page" : undefined}
                className={cn("relative flex h-14 flex-col items-center justify-center gap-0.5 text-2xs font-medium text-subtle-foreground", route.tab === n.tab && "text-signal")}
              >
                <n.icon className="size-5" aria-hidden />
                {n.label}
                {n.badge > 0 && <span className="absolute left-1/2 ml-2 top-2 size-2 rounded-full bg-warning ring-2 ring-surface" aria-label={`${n.badge} need your reply`} />}
              </button>
            ))}
          </nav>
        </div>
      </div>
    </HelpdeskContext.Provider>
  );
}

// The requester chat, embedded in the support console as the acting engineer.
export function ConsoleChat({ user, embed }: { user: User; embed: Embed }) {
  const [config, setConfig] = useState<WidgetConfig>(DEFAULT_CONFIG);
  useEffect(() => {
    api.config().then((c) => setConfig({ ...DEFAULT_CONFIG, ...c.widget })).catch(() => {});
  }, []);
  return <Workspace user={user} config={config} embed={embed} />;
}

export function AccountMenu({ user, onSignOut, compact }: { user: User; onSignOut?: () => void; compact?: boolean }) {
  const toggleTheme = () => {
    const dark = !document.documentElement.classList.contains("dark");
    document.documentElement.classList.toggle("dark", dark);
    safe(() => localStorage.setItem("l1.theme", dark ? "dark" : "light"), undefined);
  };
  return (
    <Menu>
      <MenuTrigger asChild>
        <button className={cn("flex items-center gap-2.5 rounded-md text-left hover:bg-surface-2", compact ? "rounded-full p-0.5" : "w-full p-2")} aria-label={compact ? `Account: ${displayName(user)}` : undefined}>
        <Avatar name={displayName(user)} />
        <span className={cn("min-w-0 flex-1", compact && "sr-only")}>
          <span className="block truncate text-sm font-medium">{displayName(user)}</span>
          <span className="block truncate text-xs text-muted-foreground">{user.EmailID || user.Name}</span>
        </span>
        </button>
      </MenuTrigger>
      <MenuContent side={compact ? "bottom" : "top"} align={compact ? "end" : "start"} className="w-56">
        <MenuItem onSelect={toggleTheme}>
          <Sun className="hidden dark:block" />
          <Moon className="dark:hidden" />
          Switch theme
        </MenuItem>
        {onSignOut && (
          <>
            <MenuSeparator />
            <MenuItem onSelect={onSignOut}>
              <LogOut /> Switch account
            </MenuItem>
          </>
        )}
      </MenuContent>
    </Menu>
  );
}
