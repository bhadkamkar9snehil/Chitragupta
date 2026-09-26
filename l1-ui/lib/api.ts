// Typed calls to the L1 API through /api/l1. Shapes mirror L1/api (Program.cs, Tickets.cs).
export type User = { ID: string; Name: string; FullName: string | null; EmailID: string | null; ContactNo?: string | null };
export type Tone = "attention" | "progress" | "pending" | "done";
export type SourceRef = { Slug: string; Title: string; Type: string };
export type Session = {
  ID: string;
  UserID?: string;
  Title: string | null;
  TicketNo: string | null;
  Status: "open" | "resolved";
  Rating: number | null;
  CreatedOn: string;
  ModifiedOn: string;
  LastMessage?: string | null;
  MessageCount?: number;
  Negative?: number;
  UserName?: string;
  UserEmail?: string;
};
export type Message = {
  ID: number | string;
  Role: "user" | "assistant";
  Content: string;
  Decision?: "answer" | "ask" | "ticket" | null;
  TicketNo?: string | null;
  SourcesJson?: string | null;
  Feedback?: number | null;
  Model?: string | null;
  LatencyMs?: number | null;
  CreatedOn: string;
};
export type TimelineItem = {
  Kind: "created" | "reply" | "answer" | "rating" | "follow_up";
  Actor: "requester" | "support";
  ResponseType?: string;
  Text: string | null;
  Rating?: number | null;
  At: string;
};
export type Ticket = {
  ID: string;
  TicketNo: string;
  BriefDetails: string | null;
  Description: string | null;
  Area: string | null;
  Type: string | null;
  Priority: string | null;
  Source: string | null;
  Channel?: "Helpdesk chat" | "Other";
  Status: string;
  AskStatus: string | null;
  CreatedOn: string;
  ModifiedOn: string | null;
  ReplyText: string | null;
  ResponseType: string | null;
  FirstLastName?: string | null;
  EmailID?: string | null;
  ExtractedEntitiesJson?: string | null;
  RunStatus?: string | null;
  FirstReplyOn?: string | null;
  Rating?: number | null;
  StateLabel: string;
  StateTone: Tone;
  Timeline?: TimelineItem[];
  SessionID?: string | null;
  Runs?: { ID: string; AttemptNo: number; ProcessStatus: string; ResponseType: string | null; Route: string | null; ClaimedOn: string | null; CompletedOn: string | null; ErrorMessage: string | null }[];
  Transcript?: Message[] | null;
};
export type WidgetConfig = { name: string; greeting: string; accent: string; suggestions: string[]; frameAncestors?: string };
export type AiSettings = {
  provider: string;
  kind: "openai" | "anthropic" | "codex";
  baseUrl: string;
  model: string;
  temperature: number;
  maxTokens: number;
  command?: string;
  hasApiKey?: boolean;
  apiKey?: string;
};
export type AllSettings = { ai: AiSettings; knowledge: { gbrain: boolean; source: string; limit: number }; widget: WidgetConfig };
export type Stats = {
  days: number;
  totals: {
    tickets: number; fromChat: number; open: number; waiting: number; resolved: number; conversations: number; answeredWithoutTicket: number;
    medianFirstReplyHours: number | null; csat: number | null; ratings: number; thumbsUp: number | null; thumbsDown: number | null; avgLatencyMs: number | null;
  };
  series: { day: string; tickets: number; resolved: number; conversations: number; answered: number }[];
  byState: { label: string; count: number }[];
  byArea: { label: string; count: number }[];
  byType: { label: string; count: number }[];
  runtime?: {
    totals: {
      Runs: number; AvgRunSeconds: number | null; MaxRunSeconds: number | null; AvgSqlReadsPerRun: number | null;
      AvgToolMs: number | null; AvgJevMs: number | null; AvgModelMs: number | null; ToolErrors: number | null; ModelErrors: number;
      TotalTokens: number | null; AvgGpuUtilPct: number | null; PeakGpuVramMb: number | null; AvgCpuUtilPct: number | null;
    };
    tools: { Label: string; Calls: number; Errors: number; AvgMs: number | null; MaxMs: number | null }[];
    models: { Model: string; Provider: string; Calls: number; AvgMs: number | null; Tokens: number | null }[];
    series: { Day: string; ToolCalls: number; ModelCalls: number; JevCalls: number; Tokens: number }[];
  };
};

export class ApiError extends Error {
  constructor(readonly status: number, message: string) {
    super(message);
  }
}

const FAILURE: Record<number, string> = {
  400: "The Helpdesk service rejected that request. Check what you entered and try again.",
  404: "That record no longer exists. Refresh the list.",
  502: "The Helpdesk service is not running. Start the L1 API, then retry.",
  503: "The Helpdesk service is starting up. Retry in a few seconds.",
};

async function call<T>(path: string, init?: { method?: string; body?: unknown }): Promise<T> {
  let res: Response;
  try {
    res = await fetch(`/api/l1/${path}`, {
      method: init?.method ?? "GET",
      headers: { "Content-Type": "application/json" },
      body: init?.body === undefined ? undefined : JSON.stringify(init.body),
    });
  } catch {
    throw new ApiError(0, "Can't reach the console server. Check that it is running and your connection is up.");
  }
  if (!res.ok) throw new ApiError(res.status, FAILURE[res.status] ?? `The Helpdesk service failed (${res.status}). Retry; if it repeats, check Runtime logs.`);
  const text = await res.text();
  return (text ? JSON.parse(text) : null) as T;
}

const q = (params: Record<string, string | undefined>) =>
  new URLSearchParams(Object.entries(params).filter((e): e is [string, string] => !!e[1])).toString();

export const api = {
  config: () => call<{ widget: WidgetConfig }>("config"),
  users: (search: string) => call<User[]>(`users?${q({ q: search })}`),
  user: (id: string) => call<User>(`users/${id}`),
  sessions: (userId: string) => call<Session[]>(`sessions?userId=${userId}`),
  newSession: (userId: string) => call<Session>("sessions", { method: "POST", body: { userId } }),
  updateSession: (id: string, body: { title?: string; status?: string; rating?: number }) => call(`sessions/${id}`, { method: "PATCH", body }),
  deleteSession: (id: string) => call(`sessions/${id}`, { method: "DELETE" }),
  messages: (id: string) => call<Message[]>(`sessions/${id}/messages`),
  feedback: (messageId: number | string, value: number) => call(`messages/${messageId}/feedback`, { method: "POST", body: { value } }),
  tickets: (userId: string) => call<Ticket[]>(`tickets?userId=${userId}`),
  ticket: (id: string) => call<Ticket>(`tickets/${id}`),
  answer: (id: string, userId: string, text: string) => call(`tickets/${id}/reply`, { method: "POST", body: { userId, text } }),
  rate: (id: string, userId: string, rating: number, comment?: string) => call(`tickets/${id}/rating`, { method: "POST", body: { userId, rating, comment } }),
  followUp: (id: string, userId: string, text: string) => call<Ticket>(`tickets/${id}/follow-up`, { method: "POST", body: { userId, text } }),
  admin: {
    tickets: (f: { q?: string; tone?: string; area?: string; source?: string }) => call<Ticket[]>(`admin/tickets?${q(f)}`),
    ticket: (id: string) => call<Ticket>(`admin/tickets/${id}`),
    conversations: (f: { q?: string; filter?: string }) => call<Session[]>(`admin/conversations?${q(f)}`),
    conversation: (id: string) => call<Message[]>(`admin/conversations/${id}`),
    stats: (days: number) => call<Stats>(`admin/stats?days=${days}`),
    lookups: () => call<{ areas: string[]; sources: string[] }>("admin/lookups"),
    settings: () => call<AllSettings>("admin/settings"),
    save: (section: keyof AllSettings, body: object) => call<AllSettings>(`admin/settings/${section}`, { method: "PUT", body }),
    models: (draft: Partial<AiSettings>) => call<string[] | { error: string }>("admin/ai/models", { method: "POST", body: draft }),
    test: (draft: Partial<AiSettings>) => call<{ ok: boolean; reply?: string; error?: string; ms: number }>("admin/ai/test", { method: "POST", body: draft }),
    searchKnowledge: (text: string) => call<{ Slug: string; Title: string; Type: string; Snippet: string }[]>("admin/knowledge/search", { method: "POST", body: { q: text } }),
  },
};

export type TurnEvent =
  | { event: "user"; data: { id: number } }
  | { event: "status"; data: { text: string } }
  | { event: "sources"; data: SourceRef[] }
  | { event: "token"; data: { text: string } }
  | { event: "ticket"; data: Ticket }
  | { event: "done"; data: { id: number; decision: string; ticketNo: string | null } };

// One chat turn as server-sent events.
export async function* turn(sessionId: string, body: { userId: string; text?: string; handoff?: boolean }, signal?: AbortSignal): AsyncGenerator<TurnEvent> {
  const res = await fetch(`/api/l1/sessions/${sessionId}/turn`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
    signal,
  });
  if (!res.ok || !res.body) throw new ApiError(res.status, "The assistant is unavailable. Please try again.");
  const reader = res.body.pipeThrough(new TextDecoderStream()).getReader();
  let buffer = "";
  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    buffer += value;
    let cut;
    while ((cut = buffer.indexOf("\n\n")) >= 0) {
      const block = buffer.slice(0, cut);
      buffer = buffer.slice(cut + 2);
      const event = /^event: (.+)$/m.exec(block)?.[1];
      const data = /^data: (.+)$/m.exec(block)?.[1];
      if (event && data) yield { event, data: JSON.parse(data) } as TurnEvent;
    }
  }
}

// ---------------------------------------------------------------- L2 / L3 operations (L1/api/Ops.cs)
// The saved world walk: what the engineer surveyed, which links it followed and why it stopped.
export type WalkFinding = { node: string; kind: string; value?: string; finding?: string; role?: string; confidence?: number; action_id?: string; chose?: string };
export type Trail = {
  source?: string;
  route?: string;
  stopped?: string;
  seconds?: number;
  entities?: { value: string; key: string; holders?: string[] }[];
  survey?: WalkFinding[];
  steps?: WalkFinding[];
  choices?: { options: number; chosen: string }[];
  numbers?: Record<string, { source: string | null; confidence: number; candidates: string[] }>;
};
export type Run = {
  ID: string; TicketID: string; TicketNo: string | null; BriefDetails: string | null; FirstLastName: string | null;
  AttemptNo: number; ProcessStatus: string; IsActive: boolean; Route: string | null; ResponseType: string | null; ExecutionMode: string | null;
  JevReviewDecision: string | null; JevReviewConfidence: number | null; JevRiskScore: number | null; JevModel: string | null;
  LocalModelState: string | null; LocalModelPurpose: string | null; ClaimedOn: string | null; HeartbeatOn: string | null;
  CompletedOn: string | null; CreatedOn: string; ErrorMessage: string | null; EscalateToL3: boolean | null; IsResolved: boolean | null; RequiresUserInput: boolean | null;
  SqlActions: number; Events: number | TraceEvent[]; JevCalls: number; Seconds: number | null;
  ProblemSummary?: string | null; Findings?: string | null; RootCause?: string | null; Resolution?: string | null; ReplyText?: string | null;
  JevTriageJson?: string | null; JevInvestigationJson?: string | null; JevReviewJson?: string | null; JevTraceJson?: string | null;
  JevKBCurationJson?: string | null; ActionsTakenJson?: string | null;
  Trail?: Trail | null;
  SqlActionList?: SqlAction[];
};
export type TraceEvent = {
  ID: string; EventType: string; ToolName: string | null; Name: string | null; Model: string | null; Provider: string | null;
  Status: string | null; DurationMs: number | null; EventOn: string; ErrorMessage: string | null; ArgsJson: string | null; ResultJson: string | null;
};
export type SqlAction = {
  ActionNo: number; ActionType: string; OperationName: string | null; ObjectName: string | null; Purpose: string | null; Status: string;
  RowsAffected: number | null; StartedOn: string; CompletedOn?: string | null; Ms?: number | null; SqlText?: string | null; ErrorMessage: string | null;
  TicketNo?: string | null; RunID?: string;
};
export type Activity = { At: string; Lane: "l1" | "l2" | "l3"; Title: string; TicketNo: string | null; RunID: string | null; Detail: string | null };
export type AttentionTicket = {
  ID: string; TicketNo: string; BriefDetails: string | null; Priority: string | null; Status: string; AskStatus: string | null;
  CreatedOn: string; LastProgressOn: string; AgeHours: number; StalledHours: number; RunID: string | null;
  AttentionState: "L3 attention" | "L2 working" | "Waiting on requester" | "Unclaimed" | "No active work";
};
export type Overview = {
  counts: {
    NewTickets: number; ActiveRuns: number; WaitingOnRequester: number; L3Open: number; OpenTickets: number; RunsLast24h: number;
    ChatsLast24h: number; LastClaimOn: string | null; JevCallsLast24h: number; ModelCallsLast24h: number;
    ResolvedLast24h?: number; L3OpenedLast24h?: number; FailedRunsLast24h?: number;
  };
  attention?: AttentionTicket[];
  outcomes: { Label: string; Count: number }[];
  lmStudio: { EventOn: string; ResultJson: string } | null;
  activity: Activity[];
  live: Run | null;
};
export type KanbanTask = {
  id: string; title: string; status: string; assignee: string | null; priority: string | null; createdAt: number | null;
  startedAt: number | null; completedAt: number | null; error: string | null; body: string;
};
export type Board = { available: boolean; tasks: KanbanTask[]; stats: { by_status: Record<string, number>; by_assignee: Record<string, Record<string, number>> } | null };
export type Escalation = {
  ID: string; TicketID: string; TicketNo: string; RunID: string | null; EscalationCategory: string; L3Status: string | null;
  ProblemSummary: string | null; Findings: string | null; RootCause: string | null; SuggestedAction: string | null; ReplyText: string | null;
  EscalatedOn: string; AssignedToUserID: string | null; AssignedOn: string | null; L3Remarks: string | null; L3ResolutionSummary: string | null;
  ResolvedOn: string | null; BriefDetails: string | null; FirstLastName: string | null; EmailID: string | null; TicketStatus: string | null; Area: string | null;
};
export type RuntimeLogRecord = { raw: string; data: Record<string, unknown> | null };
export type RuntimeLogSource = { name: string; available: boolean; records: RuntimeLogRecord[]; error?: string | null };
export type RuntimeLogs = { at: string; sources: RuntimeLogSource[] };
export type ToolStats = {
  tools: { ToolName: string; Calls: number; Errors: number; AvgMs: number | null; MaxMs: number | null; LastUsed: string }[];
  jev: { Stage: string; Calls: number; Errors: number; AvgMs: number | null; LastUsed: string }[];
  models: { Model: string; Provider: string; Calls: number; AvgMs: number | null; LastUsed: string }[];
  catalog: { ActionCategory: string; ActionName: string; PermissionLevel: string; Description: string | null }[];
  sql: SqlAction[];
};

// Pipeline health: the runtime's own `status` and the benchmark report, passed through by the API.
export type Probe<T> = { at: string; ok: boolean; error: string | null; data: T | null };
export type RuntimeStatus = {
  active_runs: { run_id?: string; ticket_no?: string; stage?: string }[];
  tasks_by_run: Record<string, { id: string; title: string; status: string; assignee: string; pipeline_stage: string; review_cycle: number }[]>;
  anomalies: unknown[];
  local_model: { running: number; queued: number };
  binding_ready_for_new_claims: boolean;
  binding_block_reason: string | null;
  contract: { max_pipeline_wip: number; max_qwen_running: number; max_qwen_waiting: number; max_review_cycles: number; priorities: Record<string, number>; execution_modes: string[] };
};
export type Performance = {
  window_since: string;
  runs: { RunID: string; TicketNo: string; ResponseType: string | null; DurationSeconds: number | null }[];
  outcomes: { runs: number; published: number; failed: number; active: number; response_types: Record<string, number>; canned_incomplete_replies: number; avg_claim_to_publish_min: number | null; answered_without_qwen: number; avg_no_qwen_seconds: number | null };
  tool_health: { per_tool: { ToolName: string; Calls: number; Failed: number }[]; top_failure_causes: { cause: string; count?: number; n?: number }[] };
  waste: Record<string, number>;
  failure_reasons: { reason?: string; count?: number }[];
  jev_review_gates: { jev_approvals: number; direct_publish: number; blocked_by_gate: Record<string, number> };
  model_input: { ProfileName: string; Sessions: number; Requests: number; AvgFirstPrompt: number; AvgPrompt: number; MaxPrompt: number }[];
  spill_threshold_chars: number;
  claim_health: { Waiting: number; Active: number; MinutesSinceClaim: number | null; Stalled: boolean };
  expectations: { scored: number; passed: number; pending: number; rows: { TicketNo: string; ResponseType: string; Case: string; Expected: string; Pass: boolean | null; Reply?: string }[] };
  invariants: Record<string, number>;
};

export const ops = {
  overview: () => call<Overview>("ops/overview"),
  runs: (search?: string) => call<Run[]>(`ops/runs?${q({ q: search })}`),
  run: (id: string) => call<Run & { Events: TraceEvent[] }>(`ops/runs/${id}`),
  live: (runId?: string, since?: string) =>
    call<{ run: Run | null; events?: TraceEvent[]; trail?: Run["Trail"] }>(`ops/live?${q({ runId, since })}`),
  board: () => call<Board>("ops/board"),
  l3: (status?: string) => call<Escalation[]>(`ops/l3?${q({ status })}`),
  l3Act: (id: string, body: { userId: string; action: "assign" | "note" | "resolve" | "reopen"; text?: string; public?: boolean; closeTicket?: boolean }) =>
    call<{ escalation: Escalation; ticket: Ticket }>(`ops/l3/${id}`, { method: "POST", body }),
  tools: () => call<ToolStats>("ops/tools"),
  logs: (take = 160) => call<RuntimeLogs>(`ops/logs?take=${take}`),
  status: () => call<Probe<RuntimeStatus>>("ops/status"),
  performance: (hours: number) => call<Probe<Performance>>(`ops/performance?hours=${hours}`),
};
