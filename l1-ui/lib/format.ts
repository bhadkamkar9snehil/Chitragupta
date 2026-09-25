// Plant timestamps from SQL are already local (IST); show them as written.
const local = (value: string) => new Date(value.replace("Z", ""));

const dateTime = new Intl.DateTimeFormat("en-IN", { dateStyle: "medium", timeStyle: "short" });
const time = new Intl.DateTimeFormat("en-IN", { hour: "numeric", minute: "2-digit" });
const day = new Intl.DateTimeFormat("en-IN", { day: "numeric", month: "short" });

export const when = (value?: string | null) => (value ? dateTime.format(local(value)) : "");

const short = new Intl.DateTimeFormat("en-IN", { day: "numeric", month: "short", hour: "numeric", minute: "2-digit" });
export const whenShort = (value?: string | null) => (value ? short.format(local(value)) : "");

// XBatch world page titles as plant users read them ("List_RM_Available Heat" -> "RM Available Heat").
export const pageTitle = (t: string) => t.replace(/^(XStudio_)?List_/, "").replace(/_Vw$|_USP$/i, "").replace(/_/g, " ");

export function ago(value?: string | null) {
  if (!value) return "";
  const d = local(value);
  const s = (Date.now() - d.getTime()) / 1000;
  if (s < 60) return "just now";
  if (s < 3600) return `${Math.floor(s / 60)}m ago`;
  if (s < 86400) return `${Math.floor(s / 3600)}h ago`;
  if (s < 7 * 86400) return `${Math.floor(s / 86400)}d ago`;
  return day.format(d);
}

export const clock = (value?: string | null) => (value ? time.format(local(value)) : "");

export const ticketLabel = (no?: string | null) => (no ?? "").replace("_", " #").replace("Ticket #", "#");

export const displayName = (u: { FullName?: string | null; Name?: string | null } | null | undefined) => u?.FullName || u?.Name || "Unknown";

export function initials(name: string) {
  return name.split(/[\s._-]+/).filter(Boolean).slice(0, 2).map((p) => p[0]?.toUpperCase()).join("") || "?";
}

export function dayGroup(value: string) {
  const d = local(value);
  const today = new Date();
  const diff = Math.floor((new Date(today.toDateString()).getTime() - new Date(d.toDateString()).getTime()) / 86400000);
  return diff === 0 ? "Today" : diff === 1 ? "Yesterday" : diff < 7 ? "This week" : "Earlier";
}

export const RESPONSE_KIND: Record<string, string> = {
  RESOLUTION: "Resolution",
  NEEDS_HUMAN_ACTION: "Handed to the responsible team",
  L3_ESCALATION: "Escalated to a specialist",
  UPDATE: "Progress update",
  QUESTION: "Question for you",
};

// One-line preview of a Markdown reply.
export const plain = (text?: string | null) => (text ?? "").replace(/[*`#>]+|__/g, "").replace(/\s+/g, " ").trim();

// How the suite names what the L2 engineer did, in one place (live stream, run timeline, tools).
const STAGE: Record<string, string> = {
  TICKET_TRIAGE: "Triage", TICKET_SECURITY: "Security check", WORLD_WALK_ROUTE: "Route the ticket", WORLD_WALK_SCOPE: "Scope the world",
  WORLD_WALK_ROLE: "Judge findings", WORLD_WALK_STEP: "Choose next step", WORLD_WALK_COLUMNS: "Pick columns", WORLD_WALK_TRAIL: "World walk finished",
  JEV_DIRECT_ANSWER: "Direct answer", JEV_INVESTIGATION: "Investigation plan", GBRAIN_APPLICABILITY: "Knowledge applies?",
  TRACE_ASSESSMENT: "Assess the trace", PRIMARY_REVIEW: "Review the proposal",
};
export const human = (s?: string | null) => (s ?? "").replace(/_/g, " ").toLowerCase().replace(/^\w/, (c) => c.toUpperCase());

export function describeEvent(e: { EventType: string; ToolName: string | null; Model: string | null }) {
  if (e.EventType === "jev_system_one") return { actor: "jev" as const, title: STAGE[e.ToolName ?? ""] ?? human(e.ToolName) };
  if (e.EventType === "world_walk") return { actor: "walk" as const, title: STAGE[e.ToolName ?? ""] ?? "World walk" };
  if (e.EventType === "post_api_request") return { actor: "model" as const, title: `Writer model · ${e.Model ?? "model"}` };
  if (e.EventType.endsWith("tool_call")) return { actor: "tool" as const, title: human((e.ToolName ?? "").replace(/^xstudio_/, "")) };
  return { actor: "system" as const, title: human(e.ToolName || e.EventType) };
}

export const outcomeLabel = (t?: string | null) =>
  ({ RESOLUTION: "Resolved", NEEDS_HUMAN_ACTION: "Needs human action", L3_ESCALATION: "Escalated to L3", UPDATE: "Update", QUESTION: "Question" } as Record<string, string>)[t ?? ""] ?? (t ? human(t) : "In progress");

export const duration = (s?: number | null) => (s == null ? "—" : s < 60 ? `${s}s` : s < 3600 ? `${Math.floor(s / 60)}m ${s % 60}s` : `${(s / 3600).toFixed(1)}h`);
