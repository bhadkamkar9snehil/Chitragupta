"use client";

import { useEffect, useMemo, useState, type ReactNode } from "react";
import { Pause, Play, RotateCcw, ScanSearch, Waypoints } from "lucide-react";
import type { Run, TraceEvent, Trail, WalkFinding } from "@/lib/api";
import { clock, describeEvent, duration, human, outcomeLabel, ticketLabel, when } from "@/lib/format";
import { cn } from "@/lib/utils";
import { RichText } from "@/components/helpdesk/rich-text";
import { Attributes, Legend, Panel, ProbBars, Segmented, Swatch, Waterfall, ms, pct, type Span, type VizTone } from "@/components/ui/viz";
import { Json } from "./live";

// How one L2 investigation happened, drawn as the circuit it ran through:
// ticket -> Jev gates -> audited probes of the XBatch world -> evidence Jev judged -> verdict -> (reasoning) -> outcome.
// The same component follows a live run and replays a finished one, step by step, from the recorded trace.

type Answer = { type?: string; choice?: string; confidence?: number; probabilities?: Record<string, number>; noul?: number };
type StationId = "ticket" | "gates" | "probes" | "evidence" | "verdict" | "reasoning" | "outcome";
type StationState = "done" | "active" | "pending" | "skipped";
type Pick = { kind: "station"; id: StationId } | { kind: "finding"; id: string } | { kind: "event"; id: string };

const RUN_JSON: (keyof Run)[] = ["JevTriageJson", "JevInvestigationJson", "JevReviewJson", "JevTraceJson", "JevKBCurationJson"];
const OTHER_TOOLS = /^(kanban_|skill_view$|xstudio_submit_proposal$|xstudio_read_table$)/;

function stationOf(e: TraceEvent): StationId | null {
  const t = e.ToolName ?? "";
  if (e.EventType === "pre_tool_call") return null;
  if (/^TICKET_(TRIAGE|SECURITY)$|^GBRAIN_APPLICABILITY$/.test(t)) return "gates";
  if (/^WORLD_WALK_(ROUTE|SCOPE|COLUMNS)$/.test(t) || t === "xstudio_read_table") return "probes";
  if (/^WORLD_WALK_(ROLE|STEP|TRAIL)$/.test(t)) return "evidence";
  if (t === "JEV_DIRECT_ANSWER" || t === "JEV_INVESTIGATION") return "verdict";
  if (t === "TRACE_ASSESSMENT" || t === "PRIMARY_REVIEW" || t === "xstudio_submit_proposal" || t === "kanban_complete") return "outcome";
  if (e.EventType === "post_api_request" || (e.EventType === "post_tool_call" && !OTHER_TOOLS.test(t))) return "reasoning";
  return null;
}

function parseAnswers(text?: string | null): Record<string, Answer> | null {
  if (!text) return null;
  try {
    return (JSON.parse(text) as { answers?: Record<string, Answer> }).answers ?? null;
  } catch {
    // A payload cut short still names its choices; recover those rather than show nothing.
    const out: Record<string, Answer> = {};
    for (const m of text.matchAll(/"(\w+)":\{"type":"(choice|noul)",(?:"choice":"([^"]+)","confidence":([\d.]+)|"noul":([\d.]+))/g))
      out[m[1]] = m[2] === "choice" ? { type: "choice", choice: m[3], confidence: Number(m[4]) } : { type: "noul", noul: Number(m[5]) };
    return Object.keys(out).length ? out : null;
  }
}

function fromRun(run: Run, stage: string): Record<string, Answer> | null {
  for (const key of RUN_JSON) {
    const text = run[key];
    if (typeof text !== "string" || !text.includes(stage)) continue;
    try {
      const answers = (JSON.parse(text) as Record<string, { answers?: Record<string, Answer> }>)[stage]?.answers;
      if (answers) return answers;
    } catch { /* fall through to the trace event */ }
  }
  return null;
}

const firstChoice = (a: Record<string, Answer> | null) => Object.values(a ?? {}).find((x) => x.choice);
const sorted = (p?: Record<string, number>) => Object.entries(p ?? {}).sort((a, b) => b[1] - a[1]);
// Jev offers options by id ("o2", "k0", "f1"); the option text itself is not stored in the trace.
const OPTION: Record<string, string> = { o: "Option", k: "Kind", f: "Finding", r: "Role" };
const optionLabel = (id: string) => { const m = id.match(/^([a-z])(\d+)$/i); return m ? `${OPTION[m[1].toLowerCase()] ?? m[1].toUpperCase()} ${m[2]}` : human(id); };
const isOpaque = (p?: Record<string, number>) => Object.keys(p ?? {}).some((k) => /^[a-z]\d+$/i.test(k));
const maxNoul = (a: Record<string, Answer> | null, match?: RegExp) =>
  Object.entries(a ?? {}).filter(([k, v]) => v.noul != null && (!match || match.test(k))).reduce((m, [, v]) => Math.max(m, v.noul ?? 0), 0);
const at = (value: string) => new Date(value.replace("Z", "")).getTime();

const ROLE: Record<string, { label: string; tone: VizTone; rank: number }> = {
  cause: { label: "cause", tone: "signal", rank: 0 },
  stuck: { label: "stuck", tone: "warn", rank: 1 },
  sees: { label: "sees", tone: "info", rank: 2 },
  unrelated: { label: "unrelated", tone: "faint", rank: 3 },
  not_observed: { label: "unreadable", tone: "mid", rank: 4 },
};
const role = (r?: string) => ROLE[r ?? ""] ?? ROLE.unrelated;
const material = (f: WalkFinding) => ["cause", "stuck", "sees"].includes(f.role ?? "");

function eventTone(e: TraceEvent): VizTone {
  if (e.Status === "error" || e.ErrorMessage) return "danger";
  const a = describeEvent(e).actor;
  return a === "jev" ? "signal" : a === "walk" ? "strong" : a === "model" ? "info" : "mid";
}

function stopLabel(stopped?: string) {
  if (!stopped) return null;
  if (stopped === "stop_explained") return "Stopped: the records explain it";
  if (stopped === "stop_not_data") return "Stopped: not a data problem";
  if (stopped === "no unvisited links left") return "Stopped: no links left to follow";
  return human(stopped.replace(/^routed: /, ""));
}

function useInvestigation(run: Run, events: TraceEvent[], trail: Trail | null, live: boolean) {
  return useMemo(() => {
    const shown = events.filter((e) => e.EventType !== "pre_tool_call");
    const last = (tool: string) => shown.findLast((e) => e.ToolName === tool);
    const decision = (stage: string) => {
      const e = last(stage);
      return e ? parseAnswers(e.ResultJson) ?? fromRun(run, stage) : null;
    };
    const hits = new Map<StationId, TraceEvent[]>();
    for (const e of shown) {
      const s = stationOf(e);
      if (s) hits.set(s, [...(hits.get(s) ?? []), e]);
    }

    const triage = decision("TICKET_TRIAGE");
    const security = decision("TICKET_SECURITY");
    const knowledge = decision("GBRAIN_APPLICABILITY");
    const walkRoute = decision("WORLD_WALK_ROUTE");
    const direct = decision("JEV_DIRECT_ANSWER");
    const investigation = decision("JEV_INVESTIGATION");
    const assessment = decision("TRACE_ASSESSMENT");
    const verdict = direct?.outcome ?? firstChoice(direct) ?? firstChoice(investigation);
    const judged = hits.get("evidence")?.some((e) => e.ToolName !== "WORLD_WALK_ROUTE") ?? false;

    const findings: (WalkFinding & { id: string; origin: string })[] = [
      ...(trail?.survey ?? []).map((f, i) => ({ ...f, id: `s${i}`, origin: "First survey" })),
      ...(trail?.steps ?? []).map((f, i) => ({ ...f, id: `p${i}`, origin: `Followed link ${i + 1}` })),
    ];
    const probesSeen = hits.has("probes") || hits.has("evidence");
    const evidence = judged ? findings.filter(material).sort((a, b) => role(a.role).rank - role(b.role).rank || (b.confidence ?? 0) - (a.confidence ?? 0)) : [];
    const models = shown.filter((e) => e.EventType === "post_api_request");
    const tools = shown.filter((e) => e.EventType === "post_tool_call" && !OTHER_TOOLS.test(e.ToolName ?? ""));
    const reads = shown.filter((e) => e.EventType === "post_tool_call" && e.ToolName === "xstudio_read_table").length;

    const order: StationId[] = ["ticket", "gates", "probes", "evidence", "verdict", "reasoning", "outcome"];
    const latest = shown.findLast((e) => stationOf(e));
    const activeId = live ? (latest ? stationOf(latest) : "gates") : null;
    const activeIndex = activeId ? order.indexOf(activeId) : -1;
    const finished = !live && !!run.CompletedOn;
    const state = (id: StationId): StationState => {
      if (id === "ticket") return "done";
      if (id === activeId) return "active";
      if (id === "outcome" && finished) return "done";
      if (hits.has(id)) return "done";
      if (live) return order.indexOf(id) > activeIndex ? "pending" : "skipped";
      return "skipped";
    };

    const entities = [...new Map((trail?.entities ?? []).map((e) => [e.value, e])).values()].slice(0, 3);
    // Model calls are recorded without a duration; estimate each as the gap since the previous recorded step.
    // A call that opens a worker session (followed by kanban_show, or first after Jev/world-walk steps) waited in the
    // queue instead; that gap is reported as queue wait, not model time.
    const took = new Map<string, { ms: number | null; estimated: boolean }>();
    let queueMs = 0;
    shown.forEach((e, i) => {
      if (e.DurationMs != null) return took.set(e.ID, { ms: e.DurationMs, estimated: false });
      if (e.EventType !== "post_api_request") return took.set(e.ID, { ms: null, estimated: false });
      const prev = shown[i - 1];
      const gap = prev ? Math.max(0, at(e.EventOn) - at(prev.EventOn)) : 0;
      const opensSession = !prev || !["post_api_request", "post_tool_call"].includes(prev.EventType) || shown[i + 1]?.ToolName === "kanban_show";
      if (opensSession) { queueMs += gap; took.set(e.ID, { ms: null, estimated: true }); }
      else took.set(e.ID, { ms: gap, estimated: true });
    });
    const dur = (e: TraceEvent) => took.get(e.ID)?.ms ?? 0;
    const t0 = shown.length ? Math.min(...shown.map((e) => at(e.EventOn) - dur(e))) : 0;
    const t1 = shown.length ? Math.max(...shown.map((e) => at(e.EventOn))) : 0;

    return {
      shown, hits, state, triage, security, knowledge, walkRoute, verdict, investigation, assessment, findings, probesSeen, judged,
      evidence, models, tools, reads, entities, t0, span: t1 - t0,
      riskMax: maxNoul(security), appliesMax: maxNoul(knowledge, /^applicable/),
      modelMs: models.reduce((n, e) => n + dur(e), 0),
      took, dur, queueMs,
    };
  }, [run, events, trail, live]);
}
type Investigation = ReturnType<typeof useInvestigation>;

export function InvestigationCircuit({ run, events, trail, live, onOpenRun, titled = true }: {
  titled?: boolean;
  run: Run;
  events: TraceEvent[];
  trail: Trail | null;
  live: boolean;
  onOpenRun?: (id: string) => void;
}) {
  const replayable = !live && events.length > 1;
  const [cursor, setCursor] = useState<number | null>(null);
  const [playing, setPlaying] = useState(false);
  const [pick, setPick] = useState<Pick>({ kind: "station", id: "verdict" });
  const [view, setView] = useState<"inspect" | "raw">("inspect");

  const visible = cursor == null ? events : events.slice(0, cursor);
  const x = useInvestigation(run, visible, trail, live || playing);

  useEffect(() => {
    if (!playing) return;
    const t = setInterval(() => {
      setCursor((c) => {
        const next = (c ?? 0) + 1;
        if (next >= events.length) {
          setPlaying(false);
          return null;
        }
        return next;
      });
    }, 420);
    return () => clearInterval(t);
  }, [playing, events.length]);

  const picked = pick.kind === "event" ? x.shown.find((e) => e.ID === pick.id) : undefined;
  const pickedFinding = pick.kind === "finding" ? x.findings.find((f) => f.id === pick.id) : undefined;
  const select = (p: Pick) => { setPick(p); setView("inspect"); };
  const { spans, worked } = traceSpans(x);

  return (
    <div className="space-y-4">
      <section className="overflow-hidden rounded-2xl border bg-canvas" aria-label="Investigation circuit">
        <div className="flex flex-wrap items-center gap-3 border-b px-4 py-3">
          <div className="min-w-0 flex-1">
            <p className="font-mono text-xs text-subtle-foreground">{ticketLabel(run.TicketNo)} · {run.FirstLastName ?? "requester"} · {live ? "live" : "recorded"} · {duration(run.Seconds)}</p>
            {titled && <h2 className="mt-0.5 line-clamp-2 text-title font-semibold tracking-tight">{run.BriefDetails || "L2 investigation"}</h2>}
          </div>
          {replayable && (
            <div className="flex w-full items-center gap-2 sm:w-auto">
              <button
                type="button"
                onClick={() => { if (!playing && cursor == null) setCursor(1); setPlaying((p) => !p); }}
                aria-label={playing ? "Pause replay" : "Replay how it happened"}
                className="flex h-9 shrink-0 items-center gap-2 rounded-full bg-foreground px-4 text-sm font-medium text-background hover:opacity-90"
              >
                {playing ? <Pause className="size-3.5" aria-hidden /> : <Play className="size-3.5" aria-hidden />}
                {playing ? "Pause" : cursor == null ? "Replay" : "Resume"}
              </button>
              <input
                type="range"
                min={1}
                max={events.length}
                value={cursor ?? events.length}
                onChange={(e) => { setPlaying(false); const v = Number(e.target.value); setCursor(v >= events.length ? null : v); }}
                aria-label="Replay position"
                className="h-9 min-w-0 flex-1 accent-signal sm:w-40 sm:flex-none"
              />
              <span className="w-14 shrink-0 font-mono text-xs tabular-nums text-subtle-foreground">{cursor ?? events.length}/{events.length}</span>
              {cursor != null && (
                <button type="button" onClick={() => { setPlaying(false); setCursor(null); }} aria-label="Show the whole run" className="grid size-9 shrink-0 place-items-center rounded-full text-muted-foreground hover:bg-surface-2 hover:text-foreground">
                  <RotateCcw className="size-4" aria-hidden />
                </button>
              )}
            </div>
          )}
          {onOpenRun && !replayable && (
            <button type="button" onClick={() => onOpenRun(run.ID)} className="h-9 rounded-full border bg-surface px-4 text-sm font-medium hover:bg-surface-2">Open record</button>
          )}
        </div>

        <div className="dot-grid scrollbar-thin overflow-x-auto p-4 sm:p-6">
          <div className="flex flex-col items-stretch xl:min-w-240 xl:flex-row xl:items-center">
            <Column className="xl:flex-4">
              <Station id="ticket" state="done" title="Ticket" sub={`${ticketLabel(run.TicketNo)} · ${run.FirstLastName ?? "requester"}`} pick={pick} onPick={select}>
                <p className="line-clamp-3 text-xs leading-relaxed">{run.BriefDetails}</p>
                {x.entities.length > 0 && (
                  <div className="mt-2 flex flex-wrap gap-1">
                    {x.entities.map((e) => <span key={e.value} className="rounded-md border bg-canvas px-1.5 py-0.5 font-mono text-2xs"><span className="text-subtle-foreground">{e.key.split(".").at(-1)} </span>{e.value}</span>)}
                  </div>
                )}
              </Station>
              <Drop label={x.entities[0]?.value ?? "claimed"} state={x.state("gates")} />
              <Group label="Jev gates" state={x.state("gates")}>
                <Gate label="Triage" value={x.triage?.route?.choice ? human(x.triage.route.choice) : undefined} score={x.triage?.route?.confidence} good pick={pick} onPick={select} />
                <Gate label="Safety" value={x.security ? (x.riskMax > 0.5 ? "flagged" : "clean") : undefined} score={x.security ? 1 - x.riskMax : undefined} good={x.riskMax <= 0.5} pick={pick} onPick={select} />
                <Gate label="Knowledge" value={x.knowledge ? (x.appliesMax > 0.5 ? "applies" : "no match") : undefined} score={x.knowledge ? x.appliesMax : undefined} good={x.appliesMax > 0.5} pick={pick} onPick={select} />
              </Group>
            </Column>

            <Wire label={x.walkRoute?.route?.choice ? human(x.walkRoute.route.choice) : "route"} state={x.state("probes")} />

            <Column className="xl:flex-5">
              <Station id="probes" state={x.state("probes")} title="Audited probes" sub={x.probesSeen ? `${run.SqlActions || x.findings.length} reads of the XBatch world${x.reads ? ` · ${x.reads} by the model` : ""}` : "Reads the world for the ticket's identifiers"} pick={pick} onPick={select}>
                <ProbeField findings={x.findings} seen={x.probesSeen} judged={x.judged} pick={pick} onPick={select} live={x.state("probes") === "active"} />
              </Station>
            </Column>

            <Wire label={x.judged ? `${x.evidence.length} flagged` : "judge"} state={x.state("evidence")} />

            <Column className="xl:flex-5">
              <Station id="evidence" state={x.state("evidence")} title="Evidence" sub={stopLabel(trail?.stopped) ?? "Jev decides which records matter"} pick={pick} onPick={select}>
                {x.evidence.length ? (
                  <ul className="space-y-1.5">
                    {x.evidence.slice(0, 4).map((f) => (
                      <li key={f.id}>
                        <button type="button" onClick={() => select({ kind: "finding", id: f.id })} className={cn("w-full rounded-lg border bg-canvas px-2 py-1.5 text-left hover:border-border-strong", pick.kind === "finding" && pick.id === f.id && "border-signal")}>
                          <span className="flex items-center gap-1.5">
                            <span className={cn("rounded px-1 font-mono text-2xs uppercase", f.role === "cause" ? "bg-signal-soft text-signal" : f.role === "stuck" ? "bg-warning-soft text-warning" : "bg-info-soft text-info")}>{role(f.role).label}</span>
                            <span className="ml-auto font-mono text-2xs text-subtle-foreground">{pct(f.confidence)}</span>
                          </span>
                          <span className="mt-1 block truncate font-mono text-2xs">{f.node}</span>
                        </button>
                      </li>
                    ))}
                    {x.evidence.length > 4 && <li className="px-1 font-mono text-2xs text-subtle-foreground">+{x.evidence.length - 4} more</li>}
                  </ul>
                ) : (
                  <p className="rounded-lg border border-dashed px-2 py-3 text-center text-xs text-subtle-foreground">
                    {x.judged ? "No record was judged material." : x.state("evidence") === "skipped" ? "No world walk was recorded." : "Waiting for Jev to judge the records."}
                  </p>
                )}
                {!!trail?.steps?.length && x.judged && (
                  <p className="mt-2 flex items-center gap-1.5 font-mono text-2xs text-subtle-foreground"><Waypoints className="size-3" aria-hidden />{trail.steps.length} link{trail.steps.length === 1 ? "" : "s"} followed</p>
                )}
              </Station>
            </Column>

            <Wire label={x.verdict?.confidence != null ? pct(x.verdict.confidence) : "decide"} state={x.state("verdict")} />

            <Column className="xl:flex-5">
              <div className="flex flex-col">
                <Station id="verdict" state={x.state("verdict")} title="Jev verdict" sub={x.verdict?.choice ? `${human(x.verdict.choice)} · ${pct(x.verdict.confidence)}` : "Picks the outcome from the facts"} pick={pick} onPick={select}>
                  {x.verdict?.probabilities ? <ProbBars scores={sorted(x.verdict.probabilities)} chosen={x.verdict.choice} max={3} /> : x.verdict?.choice ? <p className="font-mono text-xs">{human(x.verdict.choice)}</p> : <Pending state={x.state("verdict")} />}
                </Station>
                <Drop label={x.models.length ? "needs reasoning" : x.state("reasoning") === "skipped" ? "no model" : ""} state={x.state("reasoning")} />
                <Station id="reasoning" state={x.state("reasoning")} title="Local model" sub={x.models.length ? `${x.models.length} calls · ≈${ms(x.modelMs)}${x.queueMs > 60_000 ? ` · queued ${ms(x.queueMs)}` : ""}` : "Only when the verdict needs reasoning"} pick={pick} onPick={select} compact>
                  {x.tools.length > 0 ? (
                    <p className="truncate font-mono text-2xs text-muted-foreground">{[...new Set(x.tools.map((t) => (t.ToolName ?? "").replace(/^xstudio_/, "")))].slice(0, 4).join(" · ")}</p>
                  ) : x.state("reasoning") === "skipped" ? <p className="text-xs text-subtle-foreground">Not run for this ticket.</p> : null}
                </Station>
                <Drop label={x.state("outcome") === "done" ? "publish" : ""} state={x.state("outcome")} />
                <Station id="outcome" state={x.state("outcome")} title="Outcome" sub={x.state("outcome") === "done" ? outcomeLabel(run.ResponseType) : "Reply is reviewed, then published"} pick={pick} onPick={select} signal={!!run.CompletedOn}>
                  {x.state("outcome") === "done" ? (
                    run.ReplyText ? <p className="line-clamp-2 text-xs text-muted-foreground">{run.ReplyText}</p> : (
                      <p className="font-mono text-2xs text-muted-foreground">{[run.EscalateToL3 && "to L3", run.IsResolved && "resolved", run.RequiresUserInput && "asks requester"].filter(Boolean).join(" · ") || "reply published"}</p>
                    )
                  ) : <Pending state={x.state("outcome")} />}
                </Station>
              </div>
            </Column>
          </div>
        </div>
      </section>

      <div className="grid gap-4 xl:grid-cols-5">
        <Panel icon={ScanSearch} title="Work trace" meta={`${x.shown.length} steps · ${ms(x.span)} end to end · each phase on its own scale`} className="xl:col-span-3" pad="tight"
          actions={<Legend inline rows={[{ label: "Jev", tone: "signal" }, { label: "walk", tone: "strong" }, { label: "tool", tone: "mid" }, { label: "model", tone: "info" }]} className="hidden sm:flex" />}>
          {spans.length ? (
            <div className="scrollbar-thin max-h-104 overflow-y-auto">
              <Waterfall mono={false} spans={spans} total={worked} selected={pick.kind === "event" ? pick.id : null} onPick={(id) => select({ kind: "event", id })} />
            </div>
          ) : <p className="p-6 text-center text-sm text-muted-foreground">No steps recorded yet.</p>}
        </Panel>

        <Panel
          icon={Waypoints}
          title={picked ? describeEvent(picked).title : pickedFinding ? pickedFinding.node : STATION_TITLE[pick.kind === "station" ? pick.id : "evidence"]}
          meta={picked ? `${clock(picked.EventOn)} · ${x.took.get(picked.ID) && x.took.get(picked.ID)!.ms == null ? "waited in the queue" : `${x.took.get(picked.ID)?.estimated ? "≈" : ""}${ms(x.took.get(picked.ID)?.ms)}`}` : pickedFinding ? `${pickedFinding.origin} · ${role(pickedFinding.role).label}` : "Select a stage, a probe or a step"}
          className="xl:col-span-2"
          actions={picked?.ResultJson || picked?.ArgsJson ? <Segmented label="Inspector view" value={view} onChange={setView} options={[{ id: "inspect", label: "Details" }, { id: "raw", label: "Raw" }]} /> : undefined}
        >
          <div className="scrollbar-thin max-h-104 overflow-y-auto">
            {picked ? (
              view === "raw" ? (
                <div className="space-y-3 text-2xs">
                  {picked.ArgsJson && <Json label="Input" text={picked.ArgsJson} />}
                  {picked.ResultJson && <Json label="Output" text={picked.ResultJson} />}
                </div>
              ) : <EventDetail event={picked} run={run} took={x.took.get(picked.ID)} />
            ) : pickedFinding ? <FindingDetail finding={pickedFinding} /> : <StationDetail id={pick.kind === "station" ? pick.id : "evidence"} run={run} x={x} trail={trail} />}
          </div>
        </Panel>
      </div>
    </div>
  );
}

// The run's clock includes queue waits (tens of minutes) around seconds of work. Cut every idle gap
// over a minute out of the scale and mark it, so the working steps are readable.
function traceSpans(x: Investigation): { spans: Span[]; worked: number } {
  const GAP = 15_000;
  let cut = 0;
  let prevEnd: number | null = null;
  const spans = x.shown.map((e): Span => {
    const end = at(e.EventOn) - x.t0;
    const start = end - x.dur(e);
    let gap: string | undefined;
    if (prevEnd != null && start - prevEnd > GAP) {
      gap = start - prevEnd > 60_000 ? `waited ${ms(start - prevEnd)}${e.EventType === "post_api_request" ? " for a worker" : ""}` : `${ms(start - prevEnd)} idle`;
      cut += start - prevEnd - 1000;
    }
    prevEnd = Math.max(prevEnd ?? 0, end);
    return {
      id: e.ID, label: describeEvent(e).title, sub: `+${ms(start)}`, start: start - cut, end: end - cut, tone: eventTone(e), gap,
      right: e.Status === "error" || e.ErrorMessage ? "error" : x.took.get(e.ID) && x.took.get(e.ID)!.ms == null ? "queued" : `${x.took.get(e.ID)?.estimated ? "≈" : ""}${ms(x.took.get(e.ID)?.ms)}`,
    };
  });
  // Waits for a worker (over a minute) split the run into phases; each phase gets the full width,
  // so the investigator's seconds are as readable as the reviewer's minutes.
  const SCALE = 1000;
  let from = 0;
  spans.forEach((sp, i) => {
    const last = i === spans.length - 1 || spans[i + 1].gap?.startsWith("waited");
    if (!last) return;
    const phase = spans.slice(from, i + 1);
    const lo = Math.min(...phase.map((p) => p.start)), hi = Math.max(...phase.map((p) => p.end));
    const k = SCALE / Math.max(1, hi - lo);
    phase.forEach((p) => { p.start = (p.start - lo) * k; p.end = (p.end - lo) * k; });
    if (spans[i + 1]?.gap) spans[i + 1].gap += " · next phase on its own scale";
    from = i + 1;
  });
  return { spans, worked: SCALE };
}

const STATION_TITLE: Record<StationId, string> = {
  ticket: "Ticket", gates: "Jev gates", probes: "Audited probes", evidence: "Evidence", verdict: "Jev verdict", reasoning: "Local model", outcome: "Outcome",
};

function Column({ className, children }: { className?: string; children: ReactNode }) {
  return <div className={cn("min-w-0 xl:flex-1 xl:basis-0", className)}>{children}</div>;
}

function stateClass(state: StationState) {
  return cn(
    "border bg-surface",
    state === "active" && "border-signal motion-safe:animate-beacon",
    state === "pending" && "border-dashed bg-surface/40 opacity-70",
    state === "skipped" && "border-dashed bg-transparent opacity-60",
  );
}

function StateDot({ state }: { state: StationState }) {
  return <span className={cn("size-2 shrink-0 rounded-full", state === "done" ? "bg-signal" : state === "active" ? "bg-signal motion-safe:animate-pulse" : state === "pending" ? "bg-border-strong" : "border border-border-strong")} aria-label={state} />;
}

function Station({ id, state, title, sub, pick, onPick, children, compact, signal }: {
  id: StationId;
  state: StationState;
  title: string;
  sub?: string;
  pick: Pick;
  onPick: (p: Pick) => void;
  children?: ReactNode;
  compact?: boolean;
  signal?: boolean;
}) {
  const selected = pick.kind === "station" && pick.id === id;
  return (
    <div className={cn("rounded-xl transition-colors", stateClass(state), selected && state !== "active" && "border-foreground/40", signal && state === "done" && "border-signal/60")}>
      <button type="button" onClick={() => onPick({ kind: "station", id })} aria-pressed={selected} className={cn("flex w-full items-start gap-2 px-3 text-left", compact ? "py-2" : "pb-2 pt-2.5")}>
        <span className="min-w-0 flex-1">
          <span className="block text-sm font-semibold">{title}</span>
          {sub && <span className="block truncate font-mono text-2xs text-subtle-foreground">{sub}</span>}
        </span>
        <span className="mt-1.5"><StateDot state={state} /></span>
      </button>
      {children && <div className={cn("px-3", compact ? "pb-2" : "pb-3")}>{children}</div>}
    </div>
  );
}

function Group({ label, state, children }: { label: string; state: StationState; children: ReactNode }) {
  return (
    <div className={cn("rounded-2xl border border-dashed p-2", state === "active" && "border-signal", state === "skipped" && "opacity-60")}>
      <p className="px-1 pb-1.5 font-mono text-2xs uppercase tracking-wider text-subtle-foreground">{label}</p>
      <div className="space-y-1.5">{children}</div>
    </div>
  );
}

function Gate({ label, value, score, good, pick, onPick }: { label: string; value?: string; score?: number; good?: boolean; pick: Pick; onPick: (p: Pick) => void }) {
  const selected = pick.kind === "station" && pick.id === "gates";
  return (
    <button type="button" onClick={() => onPick({ kind: "station", id: "gates" })} aria-pressed={selected} className={cn("flex w-full items-center gap-2 rounded-lg border bg-surface px-2.5 py-2 text-left hover:border-border-strong", !value && "border-dashed bg-transparent", selected && "border-foreground/40")}>
      <span className="min-w-0 flex-1">
        <span className="block text-xs font-medium">{label}</span>
        <span className={cn("block truncate font-mono text-2xs", value ? (good ? "text-signal" : "text-warning") : "text-subtle-foreground")}>{value ?? "waiting"}</span>
      </span>
      {score != null && <span className="font-mono text-2xs tabular-nums text-subtle-foreground">{pct(score)}</span>}
    </button>
  );
}

// A connector between stages with the fact that crossed it. It runs while the next stage is working.
function Wire({ label, state }: { label: string; state: StationState }) {
  const on = state === "done" || state === "active";
  return (
    <div className="relative flex h-10 shrink-0 items-center justify-center xl:h-auto xl:w-20 xl:self-stretch" aria-hidden>
      <svg className="absolute inset-0 size-full" preserveAspectRatio="none">
        <line x1="50%" y1="0" x2="50%" y2="100%" className={cn("xl:hidden", on ? "stroke-signal" : "stroke-border-strong", state === "active" && "motion-safe:animate-flow")} strokeWidth={1.5} strokeDasharray={on && state !== "active" ? undefined : "4 4"} />
        <line x1="0" y1="50%" x2="100%" y2="50%" className={cn("hidden xl:block", on ? "stroke-signal" : "stroke-border-strong", state === "active" && "motion-safe:animate-flow")} strokeWidth={1.5} strokeDasharray={on && state !== "active" ? undefined : "4 4"} />
      </svg>
      <span className={cn("relative max-w-full truncate rounded-full px-2 py-0.5 font-mono text-2xs", on ? "bg-signal text-canvas" : "border bg-canvas text-subtle-foreground")}>{label}</span>
    </div>
  );
}

function Drop({ label, state }: { label: string; state: StationState }) {
  const on = state === "done" || state === "active";
  return (
    <div className="relative flex h-8 items-center justify-center" aria-hidden>
      <span className={cn("absolute inset-y-0 left-1/2 w-px", on ? "bg-signal" : "bg-border-strong")} />
      {label && <span className={cn("relative rounded-full px-2 py-0.5 font-mono text-2xs", on ? "bg-signal text-canvas" : "border bg-canvas text-subtle-foreground")}>{label}</span>}
    </div>
  );
}

function Pending({ state }: { state: StationState }) {
  return <p className="text-xs text-subtle-foreground">{state === "active" ? "Working…" : state === "pending" ? "Not reached yet" : "Not used in this run"}</p>;
}

// Every probe as one square: grey when read, coloured once Jev judged what it means.
function ProbeField({ findings, seen, judged, pick, onPick, live }: { findings: (WalkFinding & { id: string })[]; seen: boolean; judged: boolean; pick: Pick; onPick: (p: Pick) => void; live: boolean }) {
  if (!seen) return <Pending state="pending" />;
  if (!findings.length) return <p className="text-xs text-subtle-foreground">{live ? "Reading…" : "The probe list is saved when the walk ends."}</p>;
  const counts = Object.entries(findings.reduce<Record<string, number>>((m, f) => ({ ...m, [role(f.role).label]: (m[role(f.role).label] ?? 0) + 1 }), {}));
  return (
    <div>
      <div className="flex flex-wrap gap-1" role="list" aria-label="Probes">
        {findings.slice(0, 96).map((f) => {
          const tone = judged ? role(f.role).tone : "faint";
          const selected = pick.kind === "finding" && pick.id === f.id;
          return (
            <button
              key={f.id}
              type="button"
              role="listitem"
              title={`${f.node}${judged ? ` · ${role(f.role).label}` : ""}`}
              aria-label={`${f.node}${judged ? `, ${role(f.role).label}` : ""}`}
              onClick={() => onPick({ kind: "finding", id: f.id })}
              className={cn("size-3.5 rounded-sm transition-transform hover:scale-125 motion-safe:animate-fade", tone === "signal" ? "bg-signal" : tone === "warn" ? "bg-warning" : tone === "info" ? "bg-info" : tone === "mid" ? "bg-subtle-foreground" : "bg-border-strong", selected && "ring-2 ring-foreground ring-offset-2 ring-offset-surface")}
            />
          );
        })}
      </div>
      {judged && (
        <div className="mt-2.5 flex flex-wrap gap-x-3 gap-y-1">
          {counts.sort((a, b) => (ROLE[a[0]]?.rank ?? 9) - (ROLE[b[0]]?.rank ?? 9)).map(([label, n]) => (
            <span key={label} className="flex items-center gap-1.5 font-mono text-2xs text-subtle-foreground">
              <Swatch tone={Object.values(ROLE).find((r) => r.label === label)?.tone ?? "faint"} className="size-2" />{label} <span className="text-foreground">{n}</span>
            </span>
          ))}
        </div>
      )}
    </div>
  );
}

function FindingDetail({ finding }: { finding: WalkFinding & { origin: string } }) {
  return (
    <div className="space-y-3">
      <p className="text-sm leading-relaxed">{finding.finding || "No finding text was recorded for this probe."}</p>
      <Attributes rows={[
        { k: "record", v: finding.node, copy: finding.node },
        { k: "judged as", v: role(finding.role).label, tone: role(finding.role).tone === "faint" ? undefined : role(finding.role).tone },
        { k: "confidence", v: pct(finding.confidence) },
        { k: "matched on", v: finding.value ?? "—" },
        { k: "found by", v: finding.origin },
        ...(finding.action_id ? [{ k: "audit id", v: finding.action_id.slice(0, 8) + "…", copy: finding.action_id }] : []),
      ]} />
    </div>
  );
}

function EventDetail({ event, run, took }: { event: TraceEvent; run: Run; took?: { ms: number | null; estimated: boolean } }) {
  const answers = parseAnswers(event.ResultJson) ?? (event.ToolName ? fromRun(run, event.ToolName) : null);
  const choices = Object.entries(answers ?? {}).filter(([, a]) => a.choice);
  const nouls = Object.entries(answers ?? {}).filter(([, a]) => a.noul != null);
  return (
    <div className="space-y-4">
      {event.ErrorMessage && <p className="rounded-lg bg-destructive-soft p-3 text-xs text-destructive">{event.ErrorMessage}</p>}
      {choices.map(([q, a]) => (
        <div key={q}>
          <p className="mb-2 flex items-baseline justify-between gap-2 text-xs"><span className="text-subtle-foreground">{human(q)}</span><span className="text-signal">Chose <b className="font-medium">{optionLabel(a.choice!)}</b> · {pct(a.confidence)} sure</span></p>
          {a.probabilities && <ProbBars scores={sorted(a.probabilities)} chosen={a.choice} format={optionLabel} />}
          {isOpaque(a.probabilities) && <p className="mt-1.5 text-2xs text-subtle-foreground">Jev picks among numbered options; their text is not stored in the trace.</p>}
        </div>
      ))}
      {nouls.length > 0 && <div><p className="mb-2 text-xs text-subtle-foreground">Risk signals · higher is worse</p><ProbBars scores={nouls.map(([k, a]) => [k, a.noul ?? 0])} max={8} /></div>}
      <Attributes rows={[
        { k: "step", v: describeEvent(event).title },
        { k: "status", v: event.Status === "ok" ? "OK" : event.Status ? human(event.Status) : "—", tone: event.Status === "error" ? "danger" : undefined },
        { k: "duration", v: took && took.ms == null ? "waited in the worker queue" : took?.estimated ? `≈${ms(took.ms)} since the previous step` : ms(took?.ms ?? event.DurationMs) },
        { k: "at", v: when(event.EventOn) },
        ...(event.Model ? [{ k: "model", v: event.Model }] : []),
        ...(event.ToolName ? [{ k: "stage id", v: event.ToolName, copy: event.ToolName }] : []),
        { k: "trace id", v: event.ID.slice(0, 8) + "…", copy: event.ID },
      ]} />
    </div>
  );
}

function StationDetail({ id, run, x, trail }: { id: StationId; run: Run; x: Investigation; trail: Trail | null }) {
  if (id === "ticket")
    return <Attributes rows={[
      { k: "ticket", v: ticketLabel(run.TicketNo), copy: run.TicketNo ?? undefined },
      { k: "requester", v: run.FirstLastName ?? "—" },
      { k: "identifiers", v: x.entities.map((e) => `${e.key.split(".").at(-1)} ${e.value}`).join(" · ") || "none matched" },
      { k: "claimed", v: when(run.ClaimedOn) || "—" },
      { k: "completed", v: when(run.CompletedOn) || "in progress" },
      { k: "duration", v: duration(run.Seconds), tone: "signal" },
      { k: "cycle", v: `attempt ${run.AttemptNo}` },
    ]} />;
  if (id === "gates")
    return (
      <div className="space-y-4">
        {x.triage?.route ? <Decision q="Where does this ticket belong?" a={x.triage.route} /> : <Pending state={x.state("gates")} />}
        {x.security && <div><p className="mb-2 text-xs text-subtle-foreground">Safety checks (risk)</p><ProbBars scores={Object.entries(x.security).filter(([, a]) => a.noul != null).map(([k, a]) => [k, a.noul ?? 0])} max={6} /></div>}
        {x.knowledge && <p className="text-xs text-muted-foreground">Known answers {x.appliesMax > 0.5 ? "apply" : "did not apply"} (best match {pct(x.appliesMax)}).</p>}
      </div>
    );
  if (id === "probes") {
    const counts = x.findings.reduce<Record<string, number>>((m, f) => ({ ...m, [f.role ?? "unrelated"]: (m[f.role ?? "unrelated"] ?? 0) + 1 }), {});
    return (
      <div className="space-y-4">
        {x.walkRoute?.route && <Decision q="What kind of problem is it?" a={x.walkRoute.route} />}
        <Attributes rows={[
          { k: "audited reads", v: run.SqlActions, tone: "signal" },
          { k: "records probed", v: x.findings.length },
          { k: "model reads", v: x.reads },
          { k: "walk time", v: trail?.seconds != null ? `${trail.seconds} s` : "—" },
        ]} />
        {x.judged && <Legend rows={Object.entries(counts).sort((a, b) => role(a[0]).rank - role(b[0]).rank).map(([k, n]) => ({ label: role(k).label, value: n, tone: role(k).tone }))} />}
      </div>
    );
  }
  if (id === "evidence")
    return (
      <div className="space-y-4">
        <p className="text-sm">{stopLabel(trail?.stopped) ?? "Jev has not finished judging the records."}</p>
        {x.evidence.length > 0 && <Legend rows={x.evidence.map((f) => ({ label: f.node, value: pct(f.confidence), tone: role(f.role).tone }))} />}
        {!!trail?.steps?.length && (
          <ol className="flex flex-wrap items-center gap-1.5 font-mono text-2xs">
            {trail.steps.map((s, i) => <li key={`${s.node}-${i}`} className="rounded-md border bg-canvas px-1.5 py-0.5">{s.node}</li>)}
          </ol>
        )}
        {!!trail?.choices?.length && <p className="text-xs text-subtle-foreground">Last choice weighed {trail.choices.at(-1)?.options} possible next links.</p>}
      </div>
    );
  if (id === "verdict")
    return x.verdict ? <Decision q="What does the evidence say?" a={x.verdict} /> : <Pending state={x.state("verdict")} />;
  if (id === "reasoning")
    return x.models.length || x.tools.length ? (
      <div className="space-y-4">
        <Attributes rows={[{ k: "model calls", v: x.models.length, tone: "signal" }, { k: "model time", v: `≈${ms(x.modelMs)} (estimated from gaps; calls record no duration)` }, { k: "waited for a worker", v: ms(x.queueMs), tone: x.queueMs > 300_000 ? "warn" : undefined }, { k: "model", v: x.models[0]?.Model ?? "—" }, { k: "tool calls", v: x.tools.length }]} />
        <Legend rows={Object.entries(x.tools.reduce<Record<string, number>>((m, t) => ({ ...m, [(t.ToolName ?? "").replace(/^xstudio_/, "")]: (m[(t.ToolName ?? "").replace(/^xstudio_/, "")] ?? 0) + 1 }), {})).map(([k, n]) => ({ label: k, value: n, tone: "mid" as const }))} />
      </div>
    ) : <p className="text-sm text-muted-foreground">The local model was not needed. Jev picked the outcome from the fact table and a fixed reply was published.</p>;
  return (
    <div className="space-y-4">
      <Attributes rows={[
        { k: "outcome", v: run.CompletedOn ? outcomeLabel(run.ResponseType) : "in progress", tone: "signal" },
        { k: "to L3", v: run.EscalateToL3 ? "yes" : "no" },
        { k: "resolved", v: run.IsResolved ? "yes" : "no" },
        { k: "asks requester", v: run.RequiresUserInput ? "yes" : "no" },
        ...(run.JevReviewDecision ? [{ k: "review", v: `${human(run.JevReviewDecision)} · ${pct(run.JevReviewConfidence)}` }] : []),
      ]} />
      {x.assessment && <div><p className="mb-2 text-xs text-subtle-foreground">Trace assessment</p><ProbBars scores={Object.entries(x.assessment).filter(([, a]) => a.noul != null).map(([k, a]) => [k, a.noul ?? 0])} max={6} /></div>}
      {run.ReplyText && <div className="rounded-lg border bg-canvas p-3"><p className="mb-1 text-2xs text-subtle-foreground">What the requester was told</p><RichText compact>{run.ReplyText}</RichText></div>}
    </div>
  );
}

function Decision({ q, a }: { q: string; a: Answer }) {
  return (
    <div>
      <p className="mb-2 flex items-baseline justify-between gap-2 text-xs"><span className="text-subtle-foreground">{q}</span><span className="font-mono text-signal">{human(a.choice)} · {pct(a.confidence)}</span></p>
      {a.probabilities && <ProbBars scores={sorted(a.probabilities)} chosen={a.choice} />}
    </div>
  );
}
