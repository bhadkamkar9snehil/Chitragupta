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
