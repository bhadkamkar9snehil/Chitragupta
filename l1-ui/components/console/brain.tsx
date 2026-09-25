"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { Pause, Play, RotateCcw } from "lucide-react";
import { pageTitle } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Tag } from "@/components/ui/primitives";

export type Trail = {
  route?: string;
  stopped?: string;
  seconds?: number;
  entities?: { value: string; key: string; holders?: string[] }[];
  survey?: { node: string; kind: string; value?: string; finding?: string; role?: string; confidence?: number }[];
  steps?: { chose?: string; node: string; kind: string; value?: string; finding?: string; role?: string; confidence?: number }[];
  choices?: { options: number; chosen: string }[];
  numbers?: Record<string, { source: string | null; confidence: number; candidates: string[] }>;
};

const ROLE: Record<string, { label: string; tone: string; dot: string }> = {
  cause: { label: "Cause", tone: "bg-destructive-soft text-destructive", dot: "bg-destructive" },
  stuck: { label: "Stuck record", tone: "bg-warning-soft text-warning", dot: "bg-warning" },
  sees: { label: "What requester sees", tone: "bg-info-soft text-info", dot: "bg-info" },
  unrelated: { label: "Other record", tone: "bg-surface-3 text-muted-foreground", dot: "bg-border-strong" },
};

type Evidence = NonNullable<Trail["survey"]>[number] & { at: number };
type Step = NonNullable<Trail["steps"]>[number] & { at: number; index: number };

function build(trail: Trail) {
  const steps = trail.steps ?? [];
  const stepNodes = new Set(steps.map((s) => s.node));
  const allSurvey = trail.survey ?? [];
  const meaningful = allSurvey
    .filter((s) => (s.role && s.role !== "unrelated") || stepNodes.has(s.node))
    .slice(0, 16)
    .map((s, i) => ({ ...s, at: 300 + i * 120 }));
  const hidden = Math.max(0, allSurvey.length - meaningful.length);
  const stepStart = 650 + meaningful.length * 120;
  const path = steps.map((s, i) => ({ ...s, index: i, at: stepStart + i * 850 }));
  return {
    evidence: meaningful as Evidence[],
    steps: path as Step[],
    hidden,
    duration: Math.max(1200, stepStart + path.length * 850 + 500),
  };
}

const short = (value: string, max = 48) => {
  const label = pageTitle(value);
  return label.length > max ? `${label.slice(0, max - 1)}…` : label;
};

export function Brain({
  trail,
  ticketLabel,
  autoplay = false,
  mode = "replay",
}: {
  trail: Trail | null;
  ticketLabel: string;
  autoplay?: boolean;
  compact?: boolean;
  mode?: "replay" | "live";
}) {
  const graph = useMemo(() => (trail ? build(trail) : null), [trail]);
  const live = mode === "live";
  const [time, setTime] = useState(0);
  const [playing, setPlaying] = useState(false);
  const raf = useRef(0);
  const last = useRef(0);

  useEffect(() => {
    const reset = setTimeout(() => {
      setTime(live && graph ? graph.duration : 0);
      setPlaying(!live && autoplay);
    }, 0);
    return () => clearTimeout(reset);
  }, [graph, autoplay, live]);

  useEffect(() => {
    if (live || !playing || !graph) return;
    last.current = performance.now();
    const tick = (now: number) => {
      setTime((previous) => {
        const next = previous + (now - last.current);
        last.current = now;
        if (next >= graph.duration) {
          setPlaying(false);
          return graph.duration;
        }
        return next;
      });
      raf.current = requestAnimationFrame(tick);
    };
    raf.current = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf.current);
  }, [playing, graph, live]);

  if (!trail || !graph) {
    return <div className="grid min-h-80 place-items-center p-6 text-sm text-muted-foreground">No visual investigation trail was recorded for this run.</div>;
  }

  const now = live ? graph.duration : time;
  const visibleEvidence = graph.evidence.filter((e) => now >= e.at);
  const visibleSteps = graph.steps.filter((s) => now >= s.at);
  const currentStep = visibleSteps.at(-1)?.index ?? -1;

  return (
    <div className="flex min-h-0 flex-1 flex-col bg-background">
      <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto p-4 lg:p-6">
        <div className="mx-auto max-w-6xl space-y-5">
          <div className="flex flex-wrap items-center gap-2 rounded-xl border bg-surface p-4">
            <div className="min-w-0 flex-1">
              <p className="text-2xs font-semibold uppercase tracking-wider text-subtle-foreground">Investigation trail</p>
              <p className="mt-1 font-mono text-sm font-semibold">{ticketLabel}</p>
            </div>
            {(trail.entities ?? []).slice(0, 6).map((entity) => <Tag key={`${entity.key}:${entity.value}`} mono>{entity.value}</Tag>)}
          </div>

          <div className="grid gap-5 lg:grid-cols-2">
            <section className="rounded-xl border bg-surface">
              <div className="border-b px-4 py-3">
                <h3 className="text-sm font-semibold">Evidence that mattered</h3>
                <p className="mt-0.5 text-2xs text-subtle-foreground">Only records Jev marked meaningful or used in the chosen path are promoted here.</p>
              </div>
              <div className="space-y-2 p-3">
                {!visibleEvidence.length && <p className="p-3 text-sm text-muted-foreground">{playing ? "Reviewing records…" : "Press Play to replay the evidence review."}</p>}
                {visibleEvidence.map((item) => {
                  const role = ROLE[item.role ?? "unrelated"] ?? ROLE.unrelated;
                  return (
                    <article key={item.node} className="rounded-lg border bg-background p-3">
                      <div className="flex items-start gap-2">
                        <span className={cn("mt-1.5 size-2 shrink-0 rounded-full", role.dot)} aria-hidden />
                        <div className="min-w-0 flex-1">
                          <div className="flex flex-wrap items-center gap-2">
                            <p className="min-w-0 flex-1 truncate font-mono text-xs font-medium" title={item.node}>{short(item.node)}</p>
                            <span className={cn("rounded px-1.5 py-0.5 text-2xs font-medium", role.tone)}>{role.label}</span>
                          </div>
                          {item.finding && <p className="mt-1.5 text-xs leading-relaxed text-muted-foreground">{item.finding}</p>}
                          {item.confidence != null && <p className="mt-1 text-2xs text-subtle-foreground">{Math.round(item.confidence * 100)}% confidence</p>}
                        </div>
                      </div>
                    </article>
                  );
                })}
                {graph.hidden > 0 && now >= 300 + graph.evidence.length * 120 && (
                  <p className="rounded-lg bg-surface-2 px-3 py-2 text-xs text-muted-foreground">{graph.hidden} other reviewed record{graph.hidden === 1 ? "" : "s"} stayed out of the main view because they were not material to the result.</p>
                )}
              </div>
            </section>

            <section className="rounded-xl border bg-surface">
              <div className="border-b px-4 py-3">
                <h3 className="text-sm font-semibold">Chosen investigation path</h3>
                <p className="mt-0.5 text-2xs text-subtle-foreground">The ordered steps the investigator actually followed.</p>
              </div>
              <ol className="space-y-2 p-3">
                {!visibleSteps.length && <li className="p-3 text-sm text-muted-foreground">{playing ? "Choosing the next step…" : "The chosen path appears as the replay advances."}</li>}
                {visibleSteps.map((step) => {
                  const role = ROLE[step.role ?? "unrelated"] ?? ROLE.unrelated;
                  const current = step.index === currentStep;
                  return (
                    <li key={`${step.index}:${step.node}`} className={cn("rounded-lg border bg-background p-3 transition-shadow", current && "border-primary/40 shadow-sm")}>
                      <div className="flex gap-3">
                        <span className={cn("grid size-7 shrink-0 place-items-center rounded-full text-xs font-semibold", current ? "bg-primary text-primary-foreground" : "bg-surface-3 text-muted-foreground")}>{step.index + 1}</span>
                        <div className="min-w-0 flex-1">
                          <div className="flex flex-wrap items-center gap-2">
                            <p className="min-w-0 flex-1 font-mono text-xs font-medium">{short(step.node)}</p>
                            {step.role && <span className={cn("rounded px-1.5 py-0.5 text-2xs font-medium", role.tone)}>{role.label}</span>}
                          </div>
                          <p className="mt-1 text-2xs text-subtle-foreground">{pageTitle(step.kind)}{trail.choices?.[step.index]?.options ? ` · chosen from ${trail.choices[step.index].options} options` : ""}</p>
                          {step.finding && <p className="mt-1.5 text-xs leading-relaxed text-muted-foreground">{step.finding}</p>}
                        </div>
                      </div>
                    </li>
                  );
                })}
              </ol>
            </section>
          </div>
        </div>
      </div>

      {!live && (
        <div className="flex items-center gap-3 border-t bg-surface px-4 py-2.5">
          <Button variant="ghost" size="icon-sm" aria-label={playing ? "Pause replay" : "Play replay"} onClick={() => {
            if (time >= graph.duration) setTime(0);
            setPlaying((value) => !value);
          }}>
            {playing ? <Pause /> : <Play />}
          </Button>
          <Button variant="ghost" size="icon-sm" aria-label="Restart replay" onClick={() => { setTime(0); setPlaying(false); }}>
            <RotateCcw />
          </Button>
          <input
            type="range"
            min={0}
            max={graph.duration}
            value={time}
            onChange={(e) => { setPlaying(false); setTime(Number(e.target.value)); }}
            aria-label="Replay position"
            className="h-1 min-w-24 flex-1 accent-primary"
          />
          <span className="hidden text-2xs text-subtle-foreground sm:inline">{visibleSteps.length}/{graph.steps.length} path steps</span>
        </div>
      )}
    </div>
  );
}
