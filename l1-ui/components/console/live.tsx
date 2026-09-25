"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { Cpu, Radio, Sparkles, Waypoints, Wrench, Activity as ActivityIcon, ChevronRight } from "lucide-react";
import { toast } from "sonner";
import { ops, type Run, type TraceEvent } from "@/lib/api";
import { ago, clock, describeEvent, duration, human, outcomeLabel, ticketLabel } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Switch, Tag } from "@/components/ui/primitives";
import { Brain, type Trail } from "./brain";

export const ACTOR = {
  jev: { icon: Sparkles, tone: "bg-primary text-primary-foreground", label: "Jev" },
  walk: { icon: Waypoints, tone: "bg-info text-white dark:text-background", label: "World walk" },
  tool: { icon: Wrench, tone: "bg-surface-3 text-muted-foreground", label: "Tool" },
  model: { icon: Cpu, tone: "bg-success text-white dark:text-background", label: "Writer" },
  system: { icon: ActivityIcon, tone: "bg-surface-3 text-subtle-foreground", label: "System" },
};

const STAGES: { id: string; label: string; hit: (e: TraceEvent) => boolean }[] = [
  { id: "triage", label: "Triage", hit: (e) => /TICKET_(TRIAGE|SECURITY)/.test(e.ToolName ?? "") },
  { id: "walk", label: "World walk", hit: (e) => (e.ToolName ?? "").startsWith("WORLD_WALK") || e.ToolName === "xstudio_read_table" },
  { id: "decide", label: "Jev decides", hit: (e) => /JEV_DIRECT_ANSWER|GBRAIN_APPLICABILITY|JEV_INVESTIGATION|TRACE_ASSESSMENT/.test(e.ToolName ?? "") },
  { id: "write", label: "Writer", hit: (e) => e.EventType === "post_api_request" || e.ToolName === "xstudio_submit_proposal" },
  { id: "review", label: "Review", hit: (e) => e.ToolName === "PRIMARY_REVIEW" || (e.ToolName ?? "").startsWith("kanban_") },
];

// A tool call is recorded twice (pre/post); a human follows the finished one.
const visible = (e: TraceEvent) => e.EventType !== "pre_tool_call";

export function StageRail({ run, events }: { run: Run; events: TraceEvent[] }) {
  const done = new Set(STAGES.filter((s) => events.some(s.hit)).map((s) => s.id));
  const current = run.IsActive ? STAGES.filter((s) => done.has(s.id)).at(-1)?.id : null;
  const all = [{ id: "claim", label: "Claimed", on: !!run.ClaimedOn }, ...STAGES.map((s) => ({ id: s.id, label: s.label, on: done.has(s.id) })), { id: "publish", label: outcomeLabel(run.ResponseType), on: !!run.CompletedOn }];
  return (
    <ol className="scrollbar-thin flex items-center gap-1 overflow-x-auto" aria-label="Pipeline stages">
      {all.map((s, i) => (
        <li key={s.id} className="flex items-center gap-1">
          {i > 0 && <span className={cn("h-px w-4 sm:w-8", s.on ? "bg-primary" : "bg-border")} aria-hidden />}
          <span
            className={cn(
              "flex h-7 items-center gap-1.5 whitespace-nowrap rounded-full border px-2.5 text-xs font-medium",
              s.on ? "border-primary/40 bg-primary-soft text-primary-soft-foreground" : "text-subtle-foreground",
              current === s.id && "ring-2 ring-ring motion-safe:animate-pulse",
            )}
          >
            <span className={cn("size-1.5 rounded-full", s.on ? "bg-primary" : "bg-border-strong")} aria-hidden />
            {s.label}
          </span>
        </li>
      ))}
    </ol>
  );
}

export function EventStream({ events, className }: { events: TraceEvent[]; className?: string }) {
  const [open, setOpen] = useState<string | null>(null);
  const end = useRef<HTMLDivElement>(null);
  const shown = events.filter(visible);
  useEffect(() => {
    end.current?.scrollIntoView({ block: "end" });
  }, [shown.length]);
  if (!shown.length) return <p className="p-4 text-sm text-muted-foreground">No events recorded yet.</p>;
  return (
    <ol className={cn("space-y-0.5 p-2", className)}>
      {shown.map((e) => {
        const d = describeEvent(e);
        const A = ACTOR[d.actor];
        const failed = e.Status === "error" || !!e.ErrorMessage;
        return (
          <li key={e.ID} className="animate-rise">
            <button onClick={() => setOpen(open === e.ID ? null : e.ID)} className="flex w-full items-center gap-2.5 rounded-md px-2 py-1.5 text-left hover:bg-surface-2" aria-expanded={open === e.ID}>
              <span className={cn("grid size-6 shrink-0 place-items-center rounded-md", A.tone)} aria-hidden>
                <A.icon className="size-3.5" />
              </span>
              <span className="min-w-0 flex-1">
                <span className={cn("block truncate text-meta", failed && "text-destructive")}>{d.title}</span>
                <span className="block text-2xs text-subtle-foreground">
                  {A.label} · {clock(e.EventOn)}
                  {e.DurationMs ? ` · ${e.DurationMs < 1000 ? `${e.DurationMs}ms` : `${(e.DurationMs / 1000).toFixed(1)}s`}` : ""}
                </span>
              </span>
              <ChevronRight className={cn("size-3.5 text-subtle-foreground transition-transform", open === e.ID && "rotate-90")} aria-hidden />
            </button>
            {open === e.ID && (
              <div className="mx-2 mb-2 space-y-2 rounded-md border bg-surface-2 p-2.5 text-2xs">
                {e.ErrorMessage && <p className="text-destructive">{e.ErrorMessage}</p>}
                {e.ArgsJson && <Json label="Input" text={e.ArgsJson} />}
                {e.ResultJson && <Json label="Output" text={e.ResultJson} />}
              </div>
            )}
          </li>
        );
      })}
      <div ref={end} />
    </ol>
  );
}

function JsonScalar({ value }: { value: unknown }) {
  if (value === null) return <span className="font-mono text-subtle-foreground">null</span>;
  if (typeof value === "string") return <span className="break-words font-mono text-foreground">{JSON.stringify(value)}</span>;
  if (typeof value === "number") return <span className="font-mono tabular-nums text-info">{String(value)}</span>;
  if (typeof value === "boolean") return <span className="font-mono text-warning">{String(value)}</span>;
  return <span className="break-words font-mono text-muted-foreground">{String(value)}</span>;
}

function JsonTree({ value, depth = 0 }: { value: unknown; depth?: number }) {
  if (value === null || typeof value !== "object") return <JsonScalar value={value} />;

  const entries = Array.isArray(value)
    ? value.map((item, index) => [String(index), item] as const)
    : Object.entries(value as Record<string, unknown>);
  const kind = Array.isArray(value) ? "items" : "fields";

  return (
    <details open={depth === 0} className="group/json min-w-0">
      <summary className="cursor-pointer select-none py-0.5 font-mono text-2xs text-subtle-foreground marker:text-border-strong">
        {Array.isArray(value) ? "[" : "{"}{entries.length} {kind}{Array.isArray(value) ? "]" : "}"}
      </summary>
      <div className="ml-2 border-l pl-2">
        {entries.map(([key, child]) => (
          <div key={key} className="grid min-w-0 grid-cols-[minmax(2.5rem,auto)_minmax(0,1fr)] gap-x-2 border-b border-border/60 py-1 last:border-b-0">
            <span className="min-w-0 truncate font-mono text-2xs text-subtle-foreground" title={key}>{key}</span>
            <div className="min-w-0 text-2xs leading-relaxed"><JsonTree value={child} depth={depth + 1} /></div>
          </div>
        ))}
        {!entries.length && <span className="font-mono text-2xs text-subtle-foreground">empty</span>}
      </div>
    </details>
  );
}

export function Json({ label, text }: { label: string; text: string }) {
  let parsed: unknown;
  let valid = true;
  try {
    parsed = JSON.parse(text);
  } catch {
    valid = false;
  }

  return (
    <section className="min-w-0 overflow-hidden rounded-md border bg-background" aria-label={label}>
      <div className="flex items-center justify-between border-b bg-surface-2 px-2.5 py-1.5">
        <p className="font-semibold uppercase tracking-wider text-subtle-foreground">{label}</p>
        <span className="text-2xs text-subtle-foreground">{valid ? "Structured JSON" : "Plain text"}</span>
      </div>
      <div className="scrollbar-thin max-h-72 overflow-auto p-2.5">
        {valid ? (
          <JsonTree value={parsed} />
        ) : (
          <pre className="whitespace-pre-wrap break-words font-mono text-2xs leading-relaxed text-muted-foreground">{text}</pre>
        )}
      </div>
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
          setTrail((f.trail as Trail) ?? null);
          lastRef.current = f.events?.at(-1)?.EventOn;
          if (switched && follow) toast(`Following ${ticketLabel(f.run?.TicketNo)}`, { description: f.run?.BriefDetails ?? undefined });
          return;
        }
        setRun(r.run);
        if (r.events?.length) {
          setEvents((ev) => [...ev, ...r.events!]);
          lastRef.current = r.events.at(-1)!.EventOn;
          if (r.events.some((e) => e.ToolName === "WORLD_WALK_TRAIL")) ops.live(r.run.ID).then((f) => setTrail((f.trail as Trail) ?? null));
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

  const counts = useMemo(() => ({
    jev: events.filter((e) => e.EventType === "jev_system_one").length,
    tools: events.filter((e) => e.EventType === "post_tool_call").length,
    model: events.filter((e) => e.EventType === "post_api_request").length,
  }), [events]);

  return (
    <div className="flex min-h-0 flex-1 flex-col">
      <header className="shrink-0 space-y-3 border-b bg-surface px-4 py-3 lg:px-6">
        <div className="flex flex-wrap items-center gap-3">
          <div className="min-w-0 w-full sm:w-auto sm:flex-1">
            <div className="flex flex-wrap items-center gap-2">
              <h1 className="text-title font-semibold tracking-tight">L2 engineer · live</h1>
              {run?.IsActive ? (
                <span className="flex items-center gap-1.5 rounded-full bg-destructive-soft px-2 py-0.5 text-2xs font-semibold text-destructive">
                  <Radio className="size-3 motion-safe:animate-pulse" aria-hidden /> Working now
                </span>
              ) : run ? (
                <span className="text-2xs text-subtle-foreground">Historical replay</span>
              ) : follow ? (
                <span className="text-2xs text-subtle-foreground">L2 idle · waiting for the next run</span>
              ) : null}
            </div>
            {run && (
              <p className="mt-0.5 truncate text-meta text-muted-foreground">
                <button className="font-mono text-foreground hover:underline" onClick={() => onOpenRun(run.ID)}>{ticketLabel(run.TicketNo)}</button> · {run.BriefDetails}
              </p>
            )}
          </div>
          <label className="flex items-center gap-2 text-meta">
            <Switch checked={follow} onCheckedChange={(v) => { setFollow(v); if (v) onRun(null); }} aria-label="Follow the live run" />
            Follow live
          </label>
          <select
            value={follow ? "" : runId ?? run?.ID ?? ""}
            onChange={(e) => { setFollow(false); onRun(e.target.value || null); }}
            aria-label="Replay a run"
            className="h-11 w-full min-w-0 rounded-md border bg-surface px-2 text-meta sm:h-9 sm:w-auto sm:max-w-72"
          >
            <option value="">{follow ? "Following live" : "Pick a run to replay"}</option>
            {runs.map((r) => (
              <option key={r.ID} value={r.ID}>{ticketLabel(r.TicketNo)} · {outcomeLabel(r.ResponseType)} · {ago(r.CompletedOn ?? r.CreatedOn)}</option>
            ))}
          </select>
        </div>
        {run && <StageRail run={run} events={events} />}
      </header>

      <div className="scrollbar-thin flex min-h-0 flex-1 flex-col overflow-y-auto xl:flex-row xl:overflow-hidden">
        <section className="relative flex h-130 min-w-0 shrink-0 flex-col bg-background xl:h-auto xl:min-h-0 xl:flex-1" aria-label="World walk">
          {run && (
            <div className="flex flex-wrap gap-2 px-4 pt-3 text-2xs">
              {trail?.route && <Tag>Route · {human(trail.route)}</Tag>}
              <Tag>Jev decisions · {counts.jev}</Tag>
              <Tag>Tool calls · {counts.tools}</Tag>
              <Tag>Writer calls · {counts.model}</Tag>
              <Tag>Took · {duration(run.Seconds)}</Tag>
              {trail?.stopped && <Tag>Stopped · {trail.stopped.replace(/_/g, " ")}</Tag>}
            </div>
          )}
          <div className="min-h-0 flex-1">
            {follow && !run ? (
              <div className="grid h-full min-h-80 place-items-center px-6 text-center">
                <div>
                  <Radio className="mx-auto size-5 text-subtle-foreground" aria-hidden />
                  <p className="mt-2 text-sm font-medium">No L2 run is active</p>
                  <p className="mt-1 text-xs text-muted-foreground">Follow Live is connected and will attach when the engineer claims the next ticket.</p>
                </div>
              </div>
            ) : (
              <Brain trail={trail} ticketLabel={ticketLabel(run?.TicketNo) || "Ticket"} mode={follow ? "live" : "replay"} autoplay={!follow} />
            )}
          </div>
        </section>
        <aside className="flex min-h-64 flex-col border-t bg-surface xl:min-h-0 xl:w-96 xl:border-l xl:border-t-0" aria-label="Event stream">
          <p className="border-b px-4 py-2.5 text-2xs font-semibold uppercase tracking-wider text-subtle-foreground">What the engineer did</p>
          <div className="scrollbar-thin max-h-96 min-h-0 flex-1 overflow-y-auto xl:max-h-none">
            <EventStream events={events} />
          </div>
        </aside>
      </div>
    </div>
  );
}
