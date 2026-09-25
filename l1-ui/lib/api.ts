// Typed calls to the L1 API through /api/l1. Shapes mirror L1/api/Program.cs.
export type User = { ID: string; Name: string; FullName: string | null; EmailID: string | null };
export type Session = { ID: string; Title: string | null; TicketNo: string | null; ModifiedOn: string };
export type Message = { Role: "user" | "assistant"; Content: string; CreatedOn: string };
export type Tone = "attention" | "progress" | "pending" | "done";
export type Ticket = {
  ID: string;
  TicketNo: string;
  BriefDetails: string | null;
  Description: string | null;
  Area: string | null;
  Status: string;
  AskStatus: string | null;
  CreatedOn: string;
  ModifiedOn: string | null;
  ReplyRemarks: string | null;
  ResponseType: string | null;
  ReplyText: string | null;
  CompletedOn: string | null;
  StateLabel: string;
  StateTone: Tone;
  Replies?: { ID: string; ResponseType: string; ReplyText: string; CompletedOn: string }[];
};
export type Turn = { decision: "answer" | "ask" | "ticket"; reply: string; ticket: Ticket | null };

export class ApiError extends Error {
  constructor(readonly status: number, message: string) {
    super(message);
  }
}

async function call<T>(path: string, init?: { method?: string; body?: unknown }): Promise<T> {
  const res = await fetch(`/api/l1/${path}`, {
    method: init?.method ?? "GET",
    headers: { "Content-Type": "application/json" },
    body: init?.body === undefined ? undefined : JSON.stringify(init.body),
  });
  if (!res.ok) throw new ApiError(res.status, res.status === 502 ? "The Helpdesk service is unavailable." : "Something went wrong. Please try again.");
  return res.json() as Promise<T>;
}

export const api = {
  users: (q: string) => call<User[]>(`users?q=${encodeURIComponent(q)}`),
  user: (id: string) => call<User>(`users/${id}`),
  sessions: (userId: string) => call<Session[]>(`sessions?userId=${userId}`),
  newSession: (userId: string) => call<Session>("sessions", { method: "POST", body: { userId } }),
  renameSession: (id: string, title: string) => call(`sessions/${id}`, { method: "PATCH", body: { title } }),
  deleteSession: (id: string) => call(`sessions/${id}`, { method: "DELETE" }),
  messages: (id: string) => call<Message[]>(`sessions/${id}/messages`),
  send: (id: string, userId: string, text: string) => call<Turn>(`sessions/${id}/messages`, { method: "POST", body: { userId, text } }),
  tickets: (userId: string) => call<Ticket[]>(`tickets?userId=${userId}`),
  ticket: (id: string) => call<Ticket>(`tickets/${id}`),
  answer: (id: string, text: string) => call(`tickets/${id}/reply`, { method: "POST", body: { text } }),
};

const IST = new Intl.DateTimeFormat("en-IN", { dateStyle: "medium", timeStyle: "short" });
// SQL timestamps are already plant-local; render them as written.
export const when = (value: string | null | undefined) => (value ? IST.format(new Date(value.replace("Z", ""))) : "");
