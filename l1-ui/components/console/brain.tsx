"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { Pause, Play, RotateCcw } from "lucide-react";
import { pageTitle } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";

// The L2 engineer's walk, replayed: ticket → identifiers Jev resolved → tables surveyed (coloured by the role Jev
// judged) → the step-by-step walk Jev chose over the world graph. Pure SVG; time drives every class.

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

type Node = { id: string; label: string; kind: string; ring: number; x: number; y: number; role?: string; confidence?: number; finding?: string; at: number; judgedAt?: number };
type Edge = { from: string; to: string; at: number; kind: "resolve" | "survey" | "step"; options?: number };

const W = 1000, H = 720, CX = W / 2, CY = H / 2;
const ROLE: Record<string, { fill: string; label: string }> = {
  cause: { fill: "fill-destructive", label: "Cause" },
  stuck: { fill: "fill-warning", label: "Stuck record" },
  sees: { fill: "fill-info", label: "What the user sees" },
  unrelated: { fill: "fill-subtle-foreground", label: "Unrelated" },
};

function layout(trail: Trail, ticketLabel: string) {
  const nodes = new Map<string, Node>();
  const edges: Edge[] = [];
  const add = (n: Node) => {
    if (!nodes.has(n.id)) nodes.set(n.id, n);
    return nodes.get(n.id)!;
  };
  const polar = (r: number, a: number) => ({ x: CX + r * Math.cos(a), y: CY + r * Math.sin(a) * 0.82 });
  add({ id: "ticket", label: ticketLabel, kind: "ticket", ring: 0, x: CX, y: CY, at: 0 });

  const values = [...new Set((trail.entities ?? []).map((e) => e.value))];
  values.forEach((v, i) => {
    const p = polar(values.length === 1 ? 0 : 95, (i / Math.max(1, values.length)) * Math.PI * 2 - Math.PI / 2);
    add({ id: `v:${v}`, label: v, kind: "identifier", ring: 1, ...(values.length === 1 ? { x: CX, y: CY - 70 } : p), at: 400 + i * 150 });
    edges.push({ from: "ticket", to: `v:${v}`, at: 400 + i * 150, kind: "resolve" });
  });

  const survey = trail.survey ?? [];
  const tSurvey = 400 + values.length * 150 + 300;
  survey.forEach((s, i) => {
    const a = (i / Math.max(1, survey.length)) * Math.PI * 2 - Math.PI / 2 + 0.08;
    const r = 240 + (i % 2) * 34;
    const at = tSurvey + i * 110;
    add({ id: `n:${s.node}`, label: s.node, kind: s.kind, ring: 2, ...polar(r, a), role: s.role, confidence: s.confidence, finding: s.finding, at, judgedAt: tSurvey + survey.length * 110 + 300 + i * 60 });
    const from = s.value && nodes.has(`v:${s.value}`) ? `v:${s.value}` : "ticket";
    edges.push({ from, to: `n:${s.node}`, at, kind: "survey" });
  });

  const steps = trail.steps ?? [];
  let t = tSurvey + survey.length * 170 + 700;
  let prev: string | null = null;
  steps.forEach((s, i) => {
    const source = s.chose?.split(" ")[0];
    const fromId = source && nodes.has(`n:${source}`) ? `n:${source}` : prev ?? (nodes.has(`n:${source}`) ? `n:${source}` : "ticket");
    if (source && !nodes.has(`n:${source}`) && !prev) {
      const p = polar(300, (i / Math.max(1, steps.length)) * Math.PI * 2);
      add({ id: `n:${source}`, label: source, kind: "table", ring: 2, ...p, at: t - 200 });
    }
    const a = (i / Math.max(1, steps.length)) * Math.PI * 1.6 - Math.PI * 0.8 + Math.PI;
    const target = add({ id: `n:${s.node}`, label: s.node, kind: s.kind, ring: 3, ...polar(345, a), role: s.role, confidence: s.confidence, finding: s.finding, at: t + 450, judgedAt: t + 650 });
    edges.push({ from: nodes.has(`n:${source}`) ? `n:${source}` : fromId, to: target.id, at: t, kind: "step", options: trail.choices?.[i]?.options });
    prev = target.id;
    t += 1100;
  });
  return { nodes: [...nodes.values()], edges, duration: t + 800 };
}

export function Brain({ trail, ticketLabel, autoplay = true, compact, mode = "replay" }: { trail: Trail | null; ticketLabel: string; autoplay?: boolean; compact?: boolean; mode?: "replay" | "live" }) {
  const graph = useMemo(() => (trail ? layout(trail, ticketLabel) : null), [trail, ticketLabel]);
  const [t, setT] = useState(0);
  const [playing, setPlaying] = useState(autoplay);
  const [hover, setHover] = useState<Node | null>(null);
  const raf = useRef(0);
  const last = useRef(0);
  const live = mode === "live";

  useEffect(() => {
    const reset = setTimeout(() => {
      setT(live && graph ? graph.duration : 0);
      setPlaying(live ? false : autoplay);
    }, 0);
    return () => clearTimeout(reset);
  }, [graph, autoplay, live]);

  useEffect(() => {
    if (live || !playing || !graph) return;
    last.current = performance.now();
    const tick = (now: number) => {
      setT((prev) => {
        const next = prev + (now - last.current);
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

  if (!graph)
    return (
      <div className="grid h-full min-h-80 place-items-center text-sm text-muted-foreground">
        No world walk recorded for this run.
      </div>
    );

  const now = live ? graph.duration : t;
  const byId = new Map(graph.nodes.map((n) => [n.id, n]));
  const litEdge = (e: Edge) => now >= e.at;
  const firing = (e: Edge) => !live && now >= e.at && now < e.at + 450;
  const step = graph.edges.filter((e) => e.kind === "step" && now >= e.at).at(-1);

  return (
    <div className={cn("relative flex h-full flex-col", compact && "min-h-96")}>
      <svg viewBox={`0 0 ${W} ${H}`} className="min-h-0 w-full flex-1" role="img" aria-label="World walk graph">
        <defs>
          <radialGradient id="glow">
            <stop offset="0%" stopColor="var(--brand)" stopOpacity="0.35" />
            <stop offset="100%" stopColor="var(--brand)" stopOpacity="0" />
          </radialGradient>
        </defs>
        {[95, 257, 345].map((r) => (
          <ellipse key={r} cx={CX} cy={CY} rx={r} ry={r * 0.82} fill="none" className="stroke-border" strokeDasharray="2 6" />
        ))}
        {graph.edges.map((e, i) => {
          const a = byId.get(e.from), b = byId.get(e.to);
          if (!a || !b) return null;
          const lit = litEdge(e);
          const p = Math.min(1, Math.max(0, (now - e.at) / 450));
          const mx = (a.x + b.x) / 2 + (e.kind === "step" ? (CY - (a.y + b.y) / 2) * 0.15 : 0);
          const my = (a.y + b.y) / 2 + (e.kind === "step" ? ((a.x + b.x) / 2 - CX) * 0.15 : 0);
          const bez = (u: number) => ({ x: (1 - u) ** 2 * a.x + 2 * (1 - u) * u * mx + u * u * b.x, y: (1 - u) ** 2 * a.y + 2 * (1 - u) * u * my + u * u * b.y });
          const spark = bez(p);
          return (
            <g key={i}>
              <path
                d={`M${a.x},${a.y} Q${mx},${my} ${b.x},${b.y}`}
                fill="none"
                className={cn(
                  "transition-all duration-500",
                  e.kind === "step" ? "stroke-primary" : "stroke-border-strong",
                  !lit && "stroke-transparent",
                )}
                strokeWidth={e.kind === "step" ? 2.2 : 1}
                strokeOpacity={e.kind === "step" ? 0.9 : 0.55}
                strokeDasharray={e.kind === "step" ? undefined : "3 4"}
              />
              {firing(e) && <circle cx={spark.x} cy={spark.y} r={e.kind === "step" ? 5 : 3} className="fill-primary" />}
              {e.kind === "step" && lit && e.options ? (
                <text x={mx} y={my - 6} textAnchor="middle" className="fill-subtle-foreground text-2xs">{`1 of ${e.options}`}</text>
              ) : null}
            </g>
          );
        })}
        {graph.nodes.map((n) => {
          const on = now >= n.at;
          const judged = n.judgedAt !== undefined && now >= n.judgedAt;
          const pulse = !live && on && now < n.at + 600;
          const r = n.ring === 0 ? 26 : n.ring === 1 ? 14 : n.ring === 3 ? 10 : 7 + (n.confidence ?? 0.5) * 5;
          const role = judged && n.role ? ROLE[n.role] : null;
          const label = n.ring === 0 ? n.label : pageTitle(n.label).slice(0, 26);
          const outside = n.ring >= 2;
          const angle = Math.atan2(n.y - CY, n.x - CX);
          const lx = outside ? n.x + Math.cos(angle) * (r + 6) : n.x;
          const ly = outside ? n.y + Math.sin(angle) * (r + 6) + 3 : n.y + r + 14;
          return (
            <g key={n.id} onMouseEnter={() => setHover(n)} onMouseLeave={() => setHover(null)} className={cn("cursor-default transition-opacity duration-300", !on && "opacity-0")}>
              {pulse && <circle cx={n.x} cy={n.y} r={r * 3.2} fill="url(#glow)" />}
              {n.ring === 0 && <circle cx={n.x} cy={n.y} r={r + 10} fill="none" className="stroke-primary/40" strokeWidth={1.5} />}
              <circle
                cx={n.x}
                cy={n.y}
                r={r}
                className={cn(
                  "stroke-surface transition-colors duration-500",
                  n.ring === 0 ? "fill-primary" : n.ring === 1 ? "fill-foreground" : role ? role.fill : n.ring === 3 ? "fill-primary" : "fill-border-strong",
                  step?.to === n.id && "stroke-primary",
                )}
                strokeWidth={step?.to === n.id ? 3 : 2}
              />
              {(n.ring <= 1 || !compact) && (
                <text
                  x={lx}
                  y={ly}
                  textAnchor={outside ? (Math.cos(angle) > 0.2 ? "start" : Math.cos(angle) < -0.2 ? "end" : "middle") : "middle"}
                  className={cn("fill-muted-foreground text-2xs", n.ring <= 1 && "fill-foreground font-semibold", n.ring === 0 && "fill-primary-foreground")}
                  dy={n.ring === 0 ? -r - 18 : 0}
                >
                  {n.ring === 0 ? "" : label}
                </text>
              )}
              {n.ring === 0 && (
                <text x={n.x} y={n.y + 4} textAnchor="middle" className="fill-primary-foreground text-2xs font-semibold">{label}</text>
              )}
            </g>
          );
        })}
      </svg>

      {hover && hover.ring > 0 && (
        <div className="pointer-events-none absolute left-3 top-3 max-w-sm rounded-lg border bg-surface p-3 text-xs shadow-pop animate-fade">
          <p className="font-semibold">{hover.ring === 1 ? `Identifier ${hover.label}` : pageTitle(hover.label)}</p>
          <p className="mt-0.5 text-subtle-foreground">
            {hover.kind}
            {hover.role && ` · ${ROLE[hover.role]?.label ?? hover.role}`}
            {hover.confidence != null && ` · ${(hover.confidence * 100).toFixed(0)}% sure`}
          </p>
          {hover.finding && <p className="mt-1.5 line-clamp-6 text-muted-foreground">{hover.finding}</p>}
        </div>
      )}

      <div className="flex flex-wrap items-center gap-3 border-t px-3 py-2">
        {!live && (
          <>
            <Button variant="ghost" size="icon-sm" aria-label={playing ? "Pause" : "Play"} onClick={() => (t >= graph.duration ? (setT(0), setPlaying(true)) : setPlaying((p) => !p))}>
              {playing ? <Pause /> : <Play />}
            </Button>
            <Button variant="ghost" size="icon-sm" aria-label="Replay" onClick={() => { setT(0); setPlaying(true); }}>
              <RotateCcw />
            </Button>
            <input
              type="range"
              min={0}
              max={graph.duration}
              value={t}
              onChange={(e) => { setPlaying(false); setT(Number(e.target.value)); }}
              aria-label="Replay position"
              className="h-1 min-w-24 flex-1 accent-primary"
            />
          </>
        )}
        <div className={cn("flex flex-wrap items-center gap-3 text-2xs text-muted-foreground", live && "ml-auto")}>
          {Object.entries(ROLE).map(([k, v]) => (
            <span key={k} className="flex items-center gap-1.5">
              <svg className="size-2.5" viewBox="0 0 10 10" aria-hidden><circle cx="5" cy="5" r="5" className={v.fill} /></svg>
              {v.label}
            </span>
          ))}
          <span className="flex items-center gap-1.5">
            <svg className="size-2.5" viewBox="0 0 10 10" aria-hidden><circle cx="5" cy="5" r="5" className="fill-primary" /></svg>
            Walk step
          </span>
        </div>
      </div>
    </div>
  );
}
