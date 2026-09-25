"use client";

import { useEffect, useRef, useState } from "react";
import { Radio } from "lucide-react";
import { toast } from "sonner";
import { ops, type Run, type TraceEvent, type Trail } from "@/lib/api";
import { ago, outcomeLabel, ticketLabel } from "@/lib/format";
import { IconTile, Segmented } from "@/components/ui/viz";
import { InvestigationCircuit } from "./circuit";
import { InspectorBlock } from "./inspect";

function decodeJson(value: unknown, depth = 0): unknown {
  if (depth > 2 || typeof value !== "string") return value;
  const trimmed = value.trim();
  if (!(trimmed.startsWith("{") || trimmed.startsWith("[") || (trimmed.startsWith('"') && trimmed.endsWith('"')))) return value;
  try {
    const parsed = JSON.parse(trimmed);
    return parsed === value ? value : decodeJson(parsed, depth + 1);
  } catch {
    return value;
  }
}

function JsonScalar({ value }: { value: unknown }) {
  if (value === null) return <span className="font-mono text-subtle-foreground">null</span>;
  if (typeof value === "string") return <span className="break-words font-mono text-foreground">{JSON.stringify(value)}</span>;
  if (typeof value === "number") return <span className="font-mono tabular-nums text-info">{String(value)}</span>;
  if (typeof value === "boolean") return <span className="font-mono text-warning">{String(value)}</span>;
  return <span className="break-words font-mono text-muted-foreground">{String(value)}</span>;
}

function RowTable({ rows }: { rows: Record<string, unknown>[] }) {
  const columns = [...new Set(rows.flatMap((r) => Object.keys(r)))].slice(0, 12);
  if (!columns.length) return null;
  return (
    <div className="scrollbar-thin max-h-72 overflow-auto rounded-md border">
      <table className="w-full min-w-max text-2xs">
        <thead className="sticky top-0 z-10 bg-surface-2 text-left uppercase tracking-wider text-subtle-foreground">
          <tr>{columns.map((c) => <th key={c} className="whitespace-nowrap px-2.5 py-2 font-semibold">{c}</th>)}</tr>
        </thead>
        <tbody className="divide-y">
          {rows.slice(0, 100).map((row, i) => (
            <tr key={i} className="align-top">
              {columns.map((c) => {
                const value = decodeJson(row[c]);
                return (
                  <td key={c} className="max-w-64 px-2.5 py-2">
                    {value !== null && typeof value === "object"
                      ? <span className="font-mono text-subtle-foreground">{JSON.stringify(value)}</span>
                      : <JsonScalar value={value} />}
                  </td>
                );
              })}
            </tr>
          ))}
        </tbody>
      </table>
      {rows.length > 100 && <p className="border-t px-3 py-2 text-2xs text-subtle-foreground">Showing first 100 of {rows.length} rows.</p>}
    </div>
  );
}

function tabularRows(value: unknown): Record<string, unknown>[] | null {
  if (Array.isArray(value) && value.length && value.every((x) => x && typeof x === "object" && !Array.isArray(x)))
    return value as Record<string, unknown>[];
  if (!value || typeof value !== "object" || Array.isArray(value)) return null;
  const o = value as Record<string, unknown>;
  for (const key of ["rows", "data", "items", "records", "result"]) {
    const candidate = decodeJson(o[key]);
    if (Array.isArray(candidate) && candidate.length && candidate.every((x) => x && typeof x === "object" && !Array.isArray(x)))
      return candidate as Record<string, unknown>[];
  }
  return null;
}

function JsonTree({ value, depth = 0 }: { value: unknown; depth?: number }) {
  const decoded = decodeJson(value);
  if (decoded === null || typeof decoded !== "object") return <JsonScalar value={decoded} />;

  const entries = Array.isArray(decoded)
    ? decoded.map((item, index) => [String(index), item] as const)
    : Object.entries(decoded as Record<string, unknown>);
  const kind = Array.isArray(decoded) ? "items" : "fields";

  return (
    <details open={depth === 0} className="group/json min-w-0">
      <summary className="cursor-pointer select-none py-0.5 font-mono text-2xs text-subtle-foreground marker:text-border-strong">
        {Array.isArray(decoded) ? "[" : "{"}{entries.length} {kind}{Array.isArray(decoded) ? "]" : "}"}
      </summary>
      <div className="ml-2 border-l pl-2">
        {entries.map(([key, child]) => (
          <div key={key} className="flex min-w-0 gap-2 border-b border-border/60 py-1 last:border-b-0">
            <span className="w-24 shrink-0 truncate font-mono text-2xs text-subtle-foreground" title={key}>{key}</span>
            <div className="min-w-0 flex-1 text-2xs leading-relaxed"><JsonTree value={child} depth={depth + 1} /></div>
          </div>
        ))}
        {!entries.length && <span className="font-mono text-2xs text-subtle-foreground">empty</span>}
      </div>
    </details>
  );
}

export function Json({ label, text }: { label: string; text: string }) {
  let parsed: unknown = text;
  let valid = false;
  try {
    parsed = decodeJson(JSON.parse(text));
    valid = true;
  } catch {
    parsed = text;
  }
  const rows = valid ? tabularRows(parsed) : null;

  return (
    <section className="min-w-0 space-y-2" aria-label={label}>
      <div className="flex items-center justify-between">
        <p className="font-semibold uppercase tracking-wider text-subtle-foreground">{label}</p>
        <span className="text-2xs text-subtle-foreground">{rows ? `${rows.length} row${rows.length === 1 ? "" : "s"}` : valid ? "Structured" : "Raw"}</span>
      </div>
      {rows ? <RowTable rows={rows} /> : valid ? (
        <div className="scrollbar-thin max-h-72 overflow-auto rounded-md border bg-background p-2.5">
          <JsonTree value={parsed} />
        </div>
      ) : (
        <InspectorBlock label={label} text={text} />
      )}
      {valid && (
        <details>
          <summary className="cursor-pointer text-2xs text-subtle-foreground hover:text-foreground">Raw payload</summary>
          <InspectorBlock className="mt-2" label={label} text={text} />
        </details>
      )}
    </section>
  );
}

export function LiveView({ runId, onRun, onOpenRun }: { runId: string | null; onRun: (id: string | null) => void; onOpenRun: (id: string) => void }) {
  const [follow, setFollow] = useState(!runId);
  const [runs, setRuns] = useState<Run[]>([]);
  const [run, setRun] = useState<Run | null>(null);
  const [events, setEvents] = useState<TraceEvent[]>([]);
  const [trail, setTrail] = useState<Trail | null>(null);
  const lastRef = useRef<string | undefined>(undefined);
  const idRef = useRef<string | null>(null);

  useEffect(() => {
    ops.runs().then(setRuns).catch(() => {});
  }, []);

  useEffect(() => {
    let alive = true;
    const load = async (full: boolean) => {
      try {
        const target = follow ? undefined : runId ?? undefined;
        const r = await ops.live(target, full ? undefined : lastRef.current);
        if (!alive) return;
        if (!r.run) {
          if (follow) {
            idRef.current = null;
            lastRef.current = undefined;
            setRun(null);
            setEvents([]);
            setTrail(null);
          }
          return;
        }
        const switched = idRef.current !== r.run.ID;
        if (switched || full) {
          const f = switched && !full ? await ops.live(r.run.ID) : r;
          idRef.current = r.run.ID;
          setRun(f.run);
          setEvents(f.events ?? []);
          setTrail(f.trail ?? null);
          lastRef.current = f.events?.at(-1)?.EventOn;
          if (switched && follow) toast(`Following ${ticketLabel(f.run?.TicketNo)}`, { description: f.run?.BriefDetails ?? undefined });
          return;
        }
        setRun(r.run);
        if (r.events?.length) {
          setEvents((ev) => [...ev, ...r.events!]);
          lastRef.current = r.events.at(-1)!.EventOn;
          if (r.events.some((e) => e.ToolName === "WORLD_WALK_TRAIL")) ops.live(r.run.ID).then((f) => setTrail(f.trail ?? null));
        }
      } catch (e) {
        toast.error((e as Error).message);
      }
    };
    idRef.current = null;
    load(true);
    const poll = setInterval(() => load(false), 3000);
    return () => {
      alive = false;
      clearInterval(poll);
    };
  }, [follow, runId]);

  const live = follow && !!run?.IsActive;

  return (
    <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
      <div className="mx-auto max-w-400 space-y-4 px-4 py-5 lg:px-6">
        <header className="flex flex-wrap items-center gap-3">
          <IconTile icon={Radio} active={live} />
          <div className="min-w-0 flex-1">
            <h1 className="flex items-center gap-2 text-title font-semibold tracking-tight">
              Live engineer
              {live && <span className="flex items-center gap-1.5 rounded-full bg-signal-soft px-2 py-0.5 font-mono text-2xs text-signal"><span className="size-1.5 rounded-full bg-signal motion-safe:animate-pulse" aria-hidden />working now</span>}
            </h1>
            <p className="truncate text-xs text-subtle-foreground">
              {follow ? (run ? (run.IsActive ? "Following the investigation as it happens" : "Last investigation · waiting for the next claim") : "L2 is idle · attaches when the next ticket is claimed") : "Replaying a recorded investigation"}
            </p>
          </div>
          <Segmented
            className="w-full sm:w-auto"
            label="Mode"
            value={follow ? "live" : "replay"}
            onChange={(v) => { setFollow(v === "live"); if (v === "live") onRun(null); else if (run) onRun(run.ID); }}
            options={[{ id: "live", label: "Follow live" }, { id: "replay", label: "Replay" }]}
          />
          <select
            value={follow ? "" : runId ?? run?.ID ?? ""}
            onChange={(e) => { setFollow(false); onRun(e.target.value || null); }}
            aria-label="Choose an investigation to replay"
            className="h-10 w-full min-w-0 rounded-lg border bg-surface px-2 font-mono text-xs sm:w-auto sm:max-w-80"
          >
            <option value="">{follow ? "Pick a past investigation…" : "Choose an investigation"}</option>
            {runs.map((r) => (
              <option key={r.ID} value={r.ID}>{ticketLabel(r.TicketNo)} · {outcomeLabel(r.ResponseType)} · {ago(r.CompletedOn ?? r.CreatedOn)}</option>
            ))}
          </select>
        </header>

        {run ? (
          <InvestigationCircuit key={run.ID} run={run} events={events} trail={trail} live={live} onOpenRun={onOpenRun} />
        ) : (
          <div className="dot-grid grid min-h-96 place-items-center rounded-2xl border bg-canvas p-6 text-center">
            <div className="max-w-sm">
              <IconTile icon={Radio} className="mx-auto" />
              <h2 className="mt-3 text-title font-semibold">Waiting for the next investigation</h2>
              <p className="mt-1 text-sm text-muted-foreground">When the L2 engineer claims a ticket, its circuit lights up here step by step. Pick a past investigation above to replay how it happened.</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
