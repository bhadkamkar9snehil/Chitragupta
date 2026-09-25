"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import { Check, LogOut, Menu, MessageSquarePlus, Pencil, Search, Ticket as TicketIcon, Trash2, X } from "lucide-react";
import { api, ApiError, type Session, type Ticket, type User } from "@/lib/api";
import { cn } from "@/lib/utils";
import { Chat } from "./chat";
import { Tickets } from "./tickets";

const USER_KEY = "l1.user";
type View = { kind: "chat"; sessionId: string | null } | { kind: "tickets"; ticketId: string | null };

function readStoredUser(): string | null {
  try {
    return localStorage.getItem(USER_KEY);
  } catch {
    return null;
  }
}

function storeUser(id: string | null) {
  try {
    if (id) localStorage.setItem(USER_KEY, id);
    else localStorage.removeItem(USER_KEY);
  } catch {}
}

export function Helpdesk() {
  const [user, setUser] = useState<User | null>(null);
  const [booting, setBooting] = useState(true);
  const [offline, setOffline] = useState("");
  const [attempt, setAttempt] = useState(0);

  useEffect(() => {
    const id = readStoredUser();
    Promise.resolve(id ? api.user(id).then(setUser) : null)
      .then(() => setOffline(""))
      .catch((e: Error) => (e instanceof ApiError && e.status === 404 ? storeUser(null) : setOffline(e.message)))
      .finally(() => setBooting(false));
  }, [attempt]);

  if (booting) return <div className="grid h-dvh place-items-center text-sm text-muted-foreground">Loading…</div>;
  if (offline)
    return (
      <div className="grid h-dvh place-items-center px-4 text-center">
        <div>
          <p role="alert" className="text-sm">{offline}</p>
          <button onClick={() => { setBooting(true); setAttempt((n) => n + 1); }} className="mt-3 h-10 rounded-md border bg-card px-4 text-sm font-medium hover:bg-accent">
            Try again
          </button>
        </div>
      </div>
    );
  if (!user)
    return (
      <SignIn
        onPick={(u) => {
          storeUser(u.ID);
          setUser(u);
        }}
      />
    );
  return (
    <Workspace
      user={user}
      onSignOut={() => {
        storeUser(null);
        setUser(null);
      }}
    />
  );
}

function SignIn({ onPick }: { onPick: (u: User) => void }) {
  const [q, setQ] = useState("");
  const [users, setUsers] = useState<User[]>([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const t = setTimeout(() => {
      api.users(q).then((u) => { setUsers(u); setError(""); }).catch((e: Error) => setError(e.message));
    }, 200);
    return () => clearTimeout(t);
  }, [q]);

  return (
    <main className="grid min-h-dvh place-items-center px-4 py-10">
      <div className="w-full max-w-md">
        <p className="text-sm font-semibold text-primary">XBatch Helpdesk</p>
        <h1 className="mt-2 text-2xl font-semibold tracking-tight">Who is asking?</h1>
        <p className="mt-1 text-sm text-muted-foreground">Pick your XBatch account so your chats and tickets stay with you.</p>
        <label className="mt-6 flex items-center gap-2 rounded-lg border bg-card px-3 focus-within:ring-2 focus-within:ring-ring/40">
          <Search className="size-4 text-muted-foreground" aria-hidden />
          <input
            autoFocus
            value={q}
            onChange={(e) => setQ(e.target.value)}
            placeholder="Search by name"
            aria-label="Search by name"
            className="h-11 w-full bg-transparent text-base outline-none sm:text-sm"
          />
        </label>
        {error && <p role="alert" className="mt-3 text-sm text-destructive">{error}</p>}
        <ul className="mt-3 max-h-96 divide-y overflow-y-auto rounded-lg border bg-card">
          {users.map((u) => (
            <li key={u.ID}>
              <button onClick={() => onPick(u)} className="flex min-h-12 w-full items-center gap-3 px-3 py-2 text-left hover:bg-accent focus-visible:bg-accent focus-visible:outline-none">
                <Avatar name={u.FullName || u.Name} />
                <span className="min-w-0">
                  <span className="block truncate text-sm font-medium">{u.FullName || u.Name}</span>
                  <span className="block truncate text-xs text-muted-foreground">{u.EmailID || u.Name}</span>
                </span>
              </button>
            </li>
          ))}
          {!users.length && !error && <li className="px-3 py-6 text-center text-sm text-muted-foreground">No matching accounts.</li>}
        </ul>
      </div>
    </main>
  );
}

export function Avatar({ name, className }: { name: string; className?: string }) {
  const initials = name.split(/\s+/).filter(Boolean).slice(0, 2).map((p) => p[0]?.toUpperCase()).join("");
  return (
    <span aria-hidden className={cn("grid size-8 shrink-0 place-items-center rounded-full bg-accent text-xs font-semibold text-accent-foreground", className)}>
      {initials || "?"}
    </span>
  );
}

function Workspace({ user, onSignOut }: { user: User; onSignOut: () => void }) {
  const [sessions, setSessions] = useState<Session[]>([]);
  const [tickets, setTickets] = useState<Ticket[]>([]);
  const [view, setView] = useState<View>({ kind: "chat", sessionId: null });
  const [drawer, setDrawer] = useState(false);
  const [filter, setFilter] = useState("");

  const loadSessions = useCallback(() => api.sessions(user.ID).then(setSessions).catch(() => {}), [user.ID]);
  const loadTickets = useCallback(() => api.tickets(user.ID).then(setTickets).catch(() => {}), [user.ID]);

  useEffect(() => {
    loadSessions();
    loadTickets();
    const t = setInterval(loadTickets, 30_000);
    return () => clearInterval(t);
  }, [loadSessions, loadTickets]);

  const waiting = tickets.filter((t) => t.StateTone === "attention").length;
  const shown = useMemo(
    () => sessions.filter((s) => !filter || (s.Title ?? "").toLowerCase().includes(filter.toLowerCase()) || (s.TicketNo ?? "").toLowerCase().includes(filter.toLowerCase())),
    [sessions, filter],
  );

  const go = (v: View) => {
    setView(v);
    setDrawer(false);
  };

  const sidebar = (
    <nav aria-label="Chats" className="flex h-full flex-col bg-card">
      <div className="flex items-center justify-between px-4 pt-4">
        <span className="text-sm font-semibold">XBatch Helpdesk</span>
        <button onClick={() => setDrawer(false)} className="grid size-10 place-items-center rounded-md hover:bg-accent md:hidden" aria-label="Close menu">
          <X className="size-4" />
        </button>
      </div>
      <div className="space-y-1 px-3 pt-4">
        <NavButton active={view.kind === "chat" && view.sessionId === null} onClick={() => go({ kind: "chat", sessionId: null })}>
          <MessageSquarePlus className="size-4" /> New chat
        </NavButton>
        <NavButton active={view.kind === "tickets"} onClick={() => go({ kind: "tickets", ticketId: null })}>
          <TicketIcon className="size-4" /> My tickets
          {waiting > 0 && (
            <span className="ml-auto rounded-full bg-primary px-2 py-0.5 text-xs font-semibold text-primary-foreground" aria-label={`${waiting} waiting for your reply`}>
              {waiting}
            </span>
          )}
        </NavButton>
      </div>
      <label className="mx-3 mt-4 flex items-center gap-2 rounded-md border px-2.5">
        <Search className="size-3.5 text-muted-foreground" aria-hidden />
        <input value={filter} onChange={(e) => setFilter(e.target.value)} placeholder="Search chats" aria-label="Search chats" className="h-9 w-full bg-transparent text-base outline-none sm:text-sm" />
      </label>
      <p className="px-4 pb-1 pt-4 text-xs font-medium text-muted-foreground">Recent</p>
      <ul className="min-h-0 flex-1 space-y-0.5 overflow-y-auto px-3 pb-3">
        {shown.map((s) => (
          <SessionRow
            key={s.ID}
            session={s}
            active={view.kind === "chat" && view.sessionId === s.ID}
            onOpen={() => go({ kind: "chat", sessionId: s.ID })}
            onRename={async (title) => {
              await api.renameSession(s.ID, title).catch(() => {});
              loadSessions();
            }}
            onDelete={async () => {
              if (!confirm("Delete this chat? Any ticket it raised stays open.")) return;
              await api.deleteSession(s.ID).catch(() => {});
              if (view.kind === "chat" && view.sessionId === s.ID) setView({ kind: "chat", sessionId: null });
              loadSessions();
            }}
          />
        ))}
        {!shown.length && <li className="px-2 py-3 text-sm text-muted-foreground">{filter ? "No chats match." : "Your chats will appear here."}</li>}
      </ul>
      <div className="flex items-center gap-3 border-t px-4 py-3">
        <Avatar name={user.FullName || user.Name} />
        <div className="min-w-0 flex-1">
          <p className="truncate text-sm font-medium">{user.FullName || user.Name}</p>
          <p className="truncate text-xs text-muted-foreground">{user.EmailID}</p>
        </div>
        <button onClick={onSignOut} className="grid size-10 place-items-center rounded-md text-muted-foreground hover:bg-accent hover:text-foreground" aria-label="Switch account">
          <LogOut className="size-4" />
        </button>
      </div>
    </nav>
  );

  return (
    <div className="flex h-dvh overflow-hidden">
      <aside className="hidden w-72 shrink-0 border-r md:block">{sidebar}</aside>
      {drawer && (
        <div className="fixed inset-0 z-40 md:hidden">
          <button className="absolute inset-0 bg-foreground/30" aria-label="Close menu" onClick={() => setDrawer(false)} />
          <aside className="relative h-full w-80 max-w-full shadow-xl">{sidebar}</aside>
        </div>
      )}
      <div className="flex min-w-0 flex-1 flex-col">
        <header className="flex h-14 shrink-0 items-center gap-2 border-b px-2 md:hidden">
          <button onClick={() => setDrawer(true)} className="grid size-10 place-items-center rounded-md hover:bg-accent" aria-label="Open menu">
            <Menu className="size-5" />
          </button>
          <span className="text-sm font-semibold">XBatch Helpdesk</span>
          {waiting > 0 && (
            <button onClick={() => go({ kind: "tickets", ticketId: null })} className="ml-auto rounded-full bg-primary px-3 py-1 text-xs font-semibold text-primary-foreground">
              {waiting} need your reply
            </button>
          )}
        </header>
        {view.kind === "chat" ? (
          <Chat
            key={view.sessionId ?? "new"}
            user={user}
            sessionId={view.sessionId}
            session={sessions.find((s) => s.ID === view.sessionId) ?? null}
            onSessionCreated={(id) => {
              setView({ kind: "chat", sessionId: id });
              loadSessions();
            }}
            onTurn={() => {
              loadSessions();
              loadTickets();
            }}
            onOpenTicket={(ticketId) => go({ kind: "tickets", ticketId })}
            tickets={tickets}
          />
        ) : (
          <Tickets
            tickets={tickets}
            selected={view.ticketId}
            onSelect={(ticketId) => setView({ kind: "tickets", ticketId })}
            onChanged={loadTickets}
          />
        )}
      </div>
    </div>
  );
}

function NavButton({ active, onClick, children }: { active: boolean; onClick: () => void; children: React.ReactNode }) {
  return (
    <button
      onClick={onClick}
      aria-current={active ? "page" : undefined}
      className={cn("flex h-10 w-full items-center gap-2.5 rounded-md px-2.5 text-sm font-medium hover:bg-accent", active && "bg-accent text-accent-foreground")}
    >
      {children}
    </button>
  );
}

function SessionRow({ session, active, onOpen, onRename, onDelete }: { session: Session; active: boolean; onOpen: () => void; onRename: (t: string) => void; onDelete: () => void }) {
  const [editing, setEditing] = useState(false);
  const [title, setTitle] = useState(session.Title ?? "");
  const label = session.Title || "New chat";

  if (editing)
    return (
      <li>
        <form
          className="flex items-center gap-1 rounded-md bg-accent px-1.5"
          onSubmit={(e) => {
            e.preventDefault();
            setEditing(false);
            if (title.trim() && title.trim() !== session.Title) onRename(title.trim());
          }}
        >
          <input autoFocus value={title} onChange={(e) => setTitle(e.target.value)} onKeyDown={(e) => e.key === "Escape" && setEditing(false)} aria-label="Chat name" className="h-9 min-w-0 flex-1 bg-transparent px-1 text-base outline-none sm:text-sm" />
          <button type="submit" className="grid size-8 place-items-center rounded hover:bg-background" aria-label="Save name">
            <Check className="size-4" />
          </button>
        </form>
      </li>
    );

  return (
    <li className={cn("group flex items-center rounded-md hover:bg-accent", active && "bg-accent")}>
      <button onClick={onOpen} aria-current={active ? "page" : undefined} className="min-w-0 flex-1 px-2.5 py-2 text-left">
        <span className="block truncate text-sm">{label}</span>
        {session.TicketNo && <span className="block text-xs text-muted-foreground">{session.TicketNo.replace("_", " ")}</span>}
      </button>
      <div className="flex opacity-100 md:opacity-0 md:group-focus-within:opacity-100 md:group-hover:opacity-100">
        <button onClick={() => setEditing(true)} className="grid size-8 place-items-center rounded text-muted-foreground hover:text-foreground" aria-label={`Rename ${label}`}>
          <Pencil className="size-3.5" />
        </button>
        <button onClick={onDelete} className="grid size-8 place-items-center rounded text-muted-foreground hover:text-destructive" aria-label={`Delete ${label}`}>
          <Trash2 className="size-3.5" />
        </button>
      </div>
    </li>
  );
}
