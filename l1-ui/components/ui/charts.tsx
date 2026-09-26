"use client";

import { useRef, useState, type FocusEvent, type MouseEvent, type ReactNode } from "react";
import { cn } from "@/lib/utils";
import { SegmentBar, TONE_BG, TONE_FILL, type VizTone } from "./viz";

// Command-centre charts in the console's panel language: thin marks, 2px surface gaps, one mint signal,
// greys for context, amber only where a person must act. Every mark has a hover/focus tooltip.

// ---------- Tooltip ----------

type TipState = { x: number; y: number; body: ReactNode } | null;

export function useTip() {
  const ref = useRef<HTMLDivElement>(null);
  const [tip, setTip] = useState<TipState>(null);
  const show = (e: MouseEvent<Element> | FocusEvent<Element>, body: ReactNode) => {
    const box = ref.current?.getBoundingClientRect();
    if (!box) return;
    const t = e.currentTarget.getBoundingClientRect();
    const x = Math.min(Math.max(t.left + t.width / 2 - box.left, 90), box.width - 90);
    setTip({ x, y: t.top - box.top, body });
  };
  const hide = () => setTip(null);
  const on = (body: ReactNode) => ({
    onMouseEnter: (e: MouseEvent<Element>) => show(e, body),
    onMouseLeave: hide,
    onFocus: (e: FocusEvent<Element>) => show(e, body),
    onBlur: hide,
  });
  return { ref, tip, on };
}

export function TipLayer({ tip }: { tip: TipState }) {
  if (!tip) return null;
  return (
    <div role="status" className="pointer-events-none absolute z-20 -translate-x-1/2 -translate-y-full whitespace-nowrap rounded-lg border border-border-strong bg-canvas px-2.5 py-1.5 font-mono text-2xs leading-relaxed text-foreground shadow-pop" style={{ left: tip.x, top: tip.y - 8 }}>
      {tip.body}
    </div>
  );
}

// ---------- Flow graph (support pipeline as weighted bands) ----------

export type FlowNode = { id: string; col: number; value: number; label: string; sub?: string; tone: VizTone; onClick?: () => void };
export type FlowLink = { from: string; to: string; value: number; tone: VizTone };

const LINK_FILL: Record<VizTone, string> = {
  signal: "fill-signal", strong: "fill-muted-foreground", mid: "fill-subtle-foreground", faint: "fill-border-strong",
  danger: "fill-destructive", warn: "fill-warning", caution: "fill-warning", info: "fill-info",
};

export function FlowGraph({ nodes, links, label, className }: { nodes: FlowNode[]; links: FlowLink[]; label: string; className?: string }) {
  const { ref, tip, on } = useTip();
  const W = 940, NW = 8, SLOT = 34, GAP = 12, LABEL = 190;
  const cols = Math.max(...nodes.map((n) => n.col)) + 1;
  const colX = (c: number) => (c * (W - LABEL - NW)) / Math.max(1, cols - 1);
  const colTotal = Array.from({ length: cols }, (_, c) => nodes.filter((n) => n.col === c).reduce((s, n) => s + n.value, 0));
  const k = 170 / Math.max(1, ...colTotal);
  const h = (n: FlowNode) => Math.max(3, n.value * k);

  // Place columns left to right; a column starts level with the highest node that feeds it.
  const y: Record<string, number> = {};
  for (let c = 0; c < cols; c++) {
    const inCol = nodes.filter((n) => n.col === c);
    const feeders = links.filter((l) => inCol.some((n) => n.id === l.to)).map((l) => y[l.from]).filter((v) => v !== undefined);
    let cursor = feeders.length ? Math.min(...feeders) : 0;
    for (const n of inCol) {
      y[n.id] = cursor;
      cursor += Math.max(h(n), SLOT) + GAP;
    }
  }
  const H = Math.max(...nodes.map((n) => y[n.id] + Math.max(h(n), SLOT))) + 4;
  const byId = Object.fromEntries(nodes.map((n) => [n.id, n]));
  const out: Record<string, number> = {}, inn: Record<string, number> = {};
  const bands = [...links].sort((a, b) => y[a.to] - y[b.to]).map((l) => {
    const s = byId[l.from], t = byId[l.to];
    const th = Math.max(1.5, l.value * k);
    const y1 = y[s.id] + (out[s.id] ?? 0), y2 = y[t.id] + (inn[t.id] ?? 0);
    out[s.id] = (out[s.id] ?? 0) + th;
    inn[t.id] = (inn[t.id] ?? 0) + th;
    const x1 = colX(s.col) + NW, x2 = colX(t.col), mx = (x1 + x2) / 2;
    return { l, s, t, d: `M${x1},${y1} C${mx},${y1} ${mx},${y2} ${x2},${y2} L${x2},${y2 + th} C${mx},${y2 + th} ${mx},${y1 + th} ${x1},${y1 + th} Z` };
  });

  return (
    <div ref={ref} className={cn("relative overflow-x-auto", className)}>
      <svg viewBox={`0 0 ${W} ${H}`} className="w-full min-w-[640px]" role="img" aria-label={`${label}: ${nodes.map((n) => `${n.label} ${n.value}`).join(", ")}`}>
        {bands.map(({ l, s, t, d }) => (
          <path key={`${l.from}-${l.to}`} d={d} className={cn(LINK_FILL[l.tone], "opacity-20 transition-opacity hover:opacity-45")} {...on(<>{s.label} → {t.label} · <b>{l.value}</b></>)} />
        ))}
        {nodes.map((n) => {
          const nh = h(n), cy = y[n.id] + Math.min(nh, SLOT) / 2;
          const body = (
            <>
              <rect x={colX(n.col)} y={y[n.id]} width={NW} height={nh} rx={2} className={TONE_FILL[n.tone]} />
              <text x={colX(n.col) + NW + 8} y={cy} dominantBaseline="middle" className="fill-foreground text-[12px] [paint-order:stroke] [stroke-width:4px] [stroke:var(--surface)]">
                {n.label}
                <tspan dx={8} className="fill-muted-foreground font-mono">{n.value}</tspan>
              </text>
              {n.sub && <text x={colX(n.col) + NW + 8} y={cy + 15} dominantBaseline="middle" className="fill-subtle-foreground font-mono text-[10.5px] [paint-order:stroke] [stroke-width:4px] [stroke:var(--surface)]">{n.sub}</text>}
            </>
          );
          return n.onClick ? (
            <g key={n.id} role="button" tabIndex={0} aria-label={`${n.label} ${n.value}`} className="cursor-pointer outline-none focus-visible:[&>rect]:stroke-foreground hover:[&>text]:underline"
              onClick={n.onClick} onKeyDown={(e) => (e.key === "Enter" || e.key === " ") && (e.preventDefault(), n.onClick!())} {...on(<>{n.label} · <b>{n.value}</b>{n.sub ? ` · ${n.sub}` : ""}</>)}>{body}</g>
          ) : <g key={n.id} {...on(<>{n.label} · <b>{n.value}</b></>)}>{body}</g>;
        })}
      </svg>
      <TipLayer tip={tip} />
    </div>
  );
}

// ---------- Stacked columns (days, hours or histogram bins) ----------

export type Column = { key: string; label: string; tip?: ReactNode; segments: { id: string; value: number; tone: VizTone }[] };

export function StackColumns({ columns, label, height = 140, tickEvery = 1, markers = [], unit = "", className }: {
  columns: Column[]; label: string; height?: number; tickEvery?: number; unit?: string;
  /** Vertical reference lines at a fractional column position, e.g. p50 / p95. */
  markers?: { at: number; label: string }[];
  className?: string;
}) {
  const { ref, tip, on } = useTip();
  const max = Math.max(1, ...columns.map((c) => c.segments.reduce((s, x) => s + x.value, 0)));
  const n = columns.length;
  return (
    <div ref={ref} className={cn("relative", className)}>
      <div className="relative" style={{ height }}>
        <span className="absolute inset-x-0 top-0 border-t border-border" aria-hidden />
        <span className="absolute -top-2 right-0 bg-surface pl-1.5 font-mono text-2xs text-subtle-foreground tabular-nums">{max}{unit}</span>
        <span className="absolute inset-x-0 bottom-0 border-t border-border-strong" aria-hidden />
        <div className="absolute inset-0 flex items-end gap-0.5" role="img" aria-label={label}>
          {columns.map((c) => {
            const total = c.segments.reduce((s, x) => s + x.value, 0);
            const shown = c.segments.filter((x) => x.value > 0);
            return (
              <button key={c.key} type="button" tabIndex={total ? 0 : -1} className="group flex h-full min-w-0 flex-1 cursor-default items-end justify-center rounded-sm outline-none hover:bg-surface-2 focus-visible:bg-surface-2"
                {...on(c.tip ?? <>{c.label} · <b>{total}</b></>)}>
                {total ? (
                  <span className="flex w-full max-w-6 flex-col-reverse gap-0.5" style={{ height: `${(total / max) * 100}%` }}>
                    {shown.map((x, i) => (
                      <span key={x.id} className={cn("min-h-0.5 w-full", TONE_BG[x.tone], i === shown.length - 1 && "rounded-t-[4px]")} style={{ flexGrow: x.value, flexBasis: 0 }} />
                    ))}
                  </span>
                ) : <span className="h-0.5 w-full max-w-6 rounded-full bg-surface-3" />}
              </button>
            );
          })}
        </div>
        {markers.map((m) => (
          <span key={m.label} className="pointer-events-none absolute inset-y-0 border-l border-foreground/70" style={{ left: `${(m.at / n) * 100}%` }} aria-hidden>
            <span className="absolute left-1 top-3 bg-surface/80 font-mono text-2xs text-foreground">{m.label}</span>
          </span>
        ))}
      </div>
      <div className="mt-1.5 flex gap-0.5 font-mono text-2xs text-subtle-foreground" aria-hidden>
        {columns.map((c, i) => <span key={c.key} className="min-w-0 flex-1 overflow-visible whitespace-nowrap text-center">{(n - 1 - i) % tickEvery === 0 ? c.label : ""}</span>)}
      </div>
      <TipLayer tip={tip} />
    </div>
  );
}

// ---------- Hour heat grid (days down, 24 hours across) ----------

const HEAT = ["bg-surface-3", "bg-signal/25", "bg-signal/45", "bg-signal/70", "bg-signal"];

export function HourHeat({ rows, unit, label, className }: { rows: { key: string; label: string; cells: number[] }[]; unit: string; label: string; className?: string }) {
  const { ref, tip, on } = useTip();
  const max = Math.max(1, ...rows.flatMap((r) => r.cells));
  let peak = { r: -1, h: -1, v: 0 };
  rows.forEach((r, ri) => r.cells.forEach((v, h) => { if (v > peak.v) peak = { r: ri, h, v }; }));
  const hh = (h: number) => String(h).padStart(2, "0");
  return (
    <div ref={ref} className={cn("relative", className)}>
      <div className="grid grid-cols-[3.25rem_minmax(0,1fr)] gap-x-2 gap-y-1" role="img" aria-label={label}>
        {rows.map((r, ri) => (
          <div key={r.key} className="contents">
            <span className="font-mono text-2xs leading-4 text-subtle-foreground">{r.label}</span>
            <div className="grid grid-cols-24 gap-[3px]">
              {r.cells.map((v, h) => (
                <span key={h} tabIndex={v ? 0 : -1}
                  className={cn("h-4 rounded-[3px] outline-none hover:ring-2 hover:ring-foreground/40 focus-visible:ring-2 focus-visible:ring-foreground/60", ri === peak.r && h === peak.h ? "bg-foreground" : HEAT[v === 0 ? 0 : Math.min(4, Math.ceil((v / max) * 4))])}
                  {...on(<>{r.label} {hh(h)}:00 · <b>{v}</b> {unit}{v === 1 ? "" : "s"}</>)} />
              ))}
            </div>
          </div>
        ))}
        <span />
        <div className="flex justify-between font-mono text-2xs text-subtle-foreground" aria-hidden><span>00</span><span>06</span><span>12</span><span>18</span><span>23</span></div>
      </div>
      <div className="mt-3 flex items-center gap-2 font-mono text-2xs text-subtle-foreground" aria-hidden>
        <span>0</span>
        {HEAT.slice(1).map((c) => <span key={c} className={cn("h-2 w-5 rounded-[2px]", c)} />)}
        <span>{max}</span>
        <span className="ml-2 size-2 rounded-[2px] bg-foreground" /> busiest
      </div>
      <TipLayer tip={tip} />
    </div>
  );
}

// ---------- Dot lanes (every open ticket, by owner lane and time since last progress) ----------

export type Dot = { id: string; lane: string; bin: number; tip: ReactNode; label: string; onClick?: () => void };

export function DotLanes({ lanes, bins, dots, label, className }: { lanes: { id: string; label: string; tone: VizTone }[]; bins: string[]; dots: Dot[]; label: string; className?: string }) {
  const { ref, tip, on } = useTip();
  return (
    <div ref={ref} className={cn("relative", className)}>
      <div className="grid gap-x-2" style={{ gridTemplateColumns: `8.5rem repeat(${bins.length}, minmax(0, 1fr))` }} role="group" aria-label={label}>
        {lanes.map((lane) => {
          const inLane = dots.filter((d) => d.lane === lane.id);
          return (
            <div key={lane.id} className="contents">
              <span className={cn("flex items-center gap-2 border-t border-border py-2 text-xs", inLane.length ? "text-foreground" : "text-subtle-foreground")}>
                <span className={cn("size-2 shrink-0 rounded-full", TONE_BG[lane.tone], !inLane.length && "opacity-40")} aria-hidden />
                <span className="truncate">{lane.label}</span>
                <span className="ml-auto font-mono tabular-nums text-muted-foreground">{inLane.length}</span>
              </span>
              {bins.map((b, bi) => (
                <div key={b} className="flex flex-wrap content-center gap-1 border-t border-l border-border px-1.5 py-2">
                  {inLane.filter((d) => d.bin === bi).map((d) => (
                    <button key={d.id} type="button" aria-label={d.label} onClick={d.onClick}
                      className={cn("size-3 rounded-full ring-2 ring-surface outline-none transition-transform hover:scale-150 focus-visible:scale-150 focus-visible:ring-foreground", TONE_BG[lane.tone])}
                      {...on(d.tip)} />
                  ))}
                </div>
              ))}
            </div>
          );
        })}
        <span />
        {bins.map((b) => <span key={b} className="border-t border-border-strong pt-1.5 text-center font-mono text-2xs text-subtle-foreground">{b}</span>)}
      </div>
      <TipLayer tip={tip} />
    </div>
  );
}

// ---------- Bars on a shared scale ----------

// Average and largest prompt on one shared scale, with the spill limit as a vertical line.
export function PromptBar({ avg, max, limit, scale, label, format }: { avg: number; max: number; limit: number; scale: number; label: string; format: (n: number) => string }) {
  const at = (v: number) => `${Math.min(100, (v / scale) * 100)}%`;
  const over = max > limit;
  return (
    <div className="relative h-3" role="img" aria-label={`${label}: average ${format(avg)}, largest ${format(max)}, limit ${format(limit)} characters`}>
      <span className="absolute inset-y-1 left-0 right-0 rounded-full bg-surface-3" aria-hidden />
      <span className={cn("absolute inset-y-1 left-0 rounded-full", over ? "bg-destructive/35" : "bg-subtle-foreground/40")} style={{ width: at(max) }} aria-hidden />
      <span className="absolute inset-y-0 left-0 rounded-full bg-signal" style={{ width: at(avg) }} aria-hidden />
      <span className="absolute -inset-y-1 border-l border-dashed border-foreground/70" style={{ left: at(limit) }} aria-hidden />
    </div>
  );
}

// A composition bar whose length is its share of the largest row (tool calls): volume and failure share at once.
export function VolumeBar({ share, segments, label, className }: { share: number; segments: { value: number; tone: VizTone | "hatch"; label: string }[]; label: string; className?: string }) {
  return (
    <span className={cn("block", className)}>
      <span className="block" style={{ width: `${Math.max(4, Math.min(1, share) * 100)}%` }}>
        <SegmentBar label={label} segments={segments} />
      </span>
    </span>
  );
}

// ---------- Fan-out graph (one agent -> its tools), animation carries data ----------
// Line width = share of calls. Dots travel each line at the tool's average latency (slow tool, slow dots),
// dot density follows call volume, and the red share of dots is the tool's failure rate.

export type FanRow = { id: string; label: string; sub: string; chip: ReactNode; chipTone?: "danger" | "signal" | "muted"; share: number; errRate: number; latencyMs: number | null; hot?: boolean };

const ROW = 64, GAP = 8, EDGE_W = 112;

function travelSeconds(ms: number | null) {
  if (!ms || ms <= 0) return 1.6;
  return Math.min(7, Math.max(0.7, 0.6 + Math.log10(ms / 20) * 1.4));
}

export function FanOut({ source, sub, rows, reduced, className }: { source: string; sub: string; rows: FanRow[]; reduced?: boolean; className?: string }) {
  const { ref, tip, on } = useTip();
  const H = rows.length * (ROW + GAP) - GAP;
  const cy = H / 2;
  return (
    <div ref={ref} className={cn("dot-grid relative flex flex-col items-stretch gap-3 rounded-lg p-3 md:flex-row md:items-center md:gap-0", className)}>
      <div className="shrink-0 rounded-xl border border-signal bg-surface px-3 py-2.5 md:w-40">
        <p className="font-mono text-sm">{source}</p>
        <p className="font-mono text-xs text-subtle-foreground">{sub}</p>
      </div>
      <svg width={EDGE_W} height={H} viewBox={`0 0 ${EDGE_W} ${H}`} className="hidden shrink-0 md:block" aria-hidden>
        {rows.map((r, i) => {
          const y = i * (ROW + GAP) + ROW / 2;
          const d = `M0 ${cy} C ${EDGE_W * 0.55} ${cy}, ${EDGE_W * 0.45} ${y}, ${EDGE_W} ${y}`;
          const n = Math.max(1, Math.min(7, Math.round(1 + r.share * 10)));
          const red = r.errRate > 0 ? Math.max(1, Math.round(n * r.errRate)) : 0;
          const dur = travelSeconds(r.latencyMs);
          return (
            <g key={r.id}>
              <path d={d} fill="none" strokeWidth={Math.max(1, Math.min(6, 1 + r.share * 14))} strokeLinecap="round" className={r.hot ? "stroke-signal/60" : "stroke-border-strong"} />
              {!reduced && Array.from({ length: n }, (_, k) => (
                <circle key={k} r={2.6} className={k < red ? "fill-destructive" : "fill-signal"}>
                  <animateMotion dur={`${dur}s`} begin={`${-(k / n) * dur}s`} repeatCount="indefinite" path={d} />
                </circle>
              ))}
            </g>
          );
        })}
      </svg>
      <ol className="min-w-0 flex-1 space-y-2">
        {rows.map((r) => (
          <li key={r.id} tabIndex={0} className={cn("flex h-16 items-center gap-3 rounded-xl border bg-surface px-3 outline-none focus-visible:ring-2 focus-visible:ring-ring", r.hot && "border-signal")}
            {...on(<>{r.label}<br />{Math.round(r.share * 100)}% of calls · {(r.errRate * 100).toFixed(1)}% failed · avg {r.latencyMs == null ? "—" : r.latencyMs < 1000 ? `${Math.round(r.latencyMs)} ms` : `${(r.latencyMs / 1000).toFixed(1)} s`}</>)}>
            <span className={cn("size-2 shrink-0 rounded-full", r.errRate > 0.1 ? "bg-destructive" : r.hot ? "bg-signal" : "bg-subtle-foreground")} aria-hidden />
            <span className="min-w-0 flex-1">
              <span className="block truncate font-mono text-sm">{r.label}</span>
              <span className="block truncate font-mono text-xs text-subtle-foreground">{r.sub}</span>
            </span>
            <span className={cn("shrink-0 rounded-md px-2 py-1 font-mono text-xs tabular-nums", r.chipTone === "danger" ? "bg-destructive-soft text-destructive" : r.chipTone === "signal" ? "bg-signal-soft text-signal" : "bg-surface-2 text-muted-foreground")}>{r.chip}</span>
          </li>
        ))}
      </ol>
      <TipLayer tip={tip} />
    </div>
  );
}

// ---------- Swimlanes (who did what, when) ----------

export type LaneMark = { key: string; lane: string; track: number; start: number; end?: number; tone: VizTone; tip: ReactNode; onClick?: () => void };

export function Swimlanes({ lanes, tracks, marks, domain, label, className }: {
  lanes: { id: string; label: string; sub?: string }[];
  tracks: string[];
  marks: LaneMark[];
  domain: [number, number];
  label: string;
  className?: string;
}) {
  const { ref, tip, on } = useTip();
  const [t0, t1] = domain;
  const span = Math.max(1, t1 - t0);
  const x = (t: number) => Math.max(0, Math.min(100, ((t - t0) / span) * 100));
  const hhmm = (t: number) => new Date(t).toLocaleTimeString("en-IN", { hour: "2-digit", minute: "2-digit", second: span < 180_000 ? "2-digit" : undefined, hour12: false, timeZone: "Asia/Kolkata" });
  const ticks = Array.from({ length: 5 }, (_, i) => t0 + (span * i) / 4);
  return (
    <div ref={ref} className={cn("relative", className)}>
      <div className="grid grid-cols-[6.5rem_minmax(0,1fr)] gap-x-3 sm:grid-cols-[9rem_minmax(0,1fr)]" role="img" aria-label={label}>
        {lanes.map((lane) => (
          <div key={lane.id} className="contents">
            <div className="flex flex-col justify-center border-t border-border py-2">
              <span className="truncate text-xs font-medium">{lane.label}</span>
              {lane.sub && <span className="truncate font-mono text-2xs text-subtle-foreground">{lane.sub}</span>}
            </div>
            <div className="relative border-t border-border py-2">
              {tracks.map((t, ti) => (
                <div key={t} className="relative my-1 h-4" title={t}>
                  <span className="absolute inset-x-0 top-1/2 border-t border-dashed border-border" aria-hidden />
                  {marks.filter((m) => m.lane === lane.id && m.track === ti).map((m) => {
                    const left = x(m.start), w = m.end != null ? Math.max(0.35, x(m.end) - left) : 0;
                    return (
                      <button key={m.key} type="button" onClick={m.onClick} aria-label={typeof m.tip === "string" ? m.tip : undefined}
                        className={cn("absolute top-1/2 -translate-y-1/2 rounded-[3px] outline-none ring-surface hover:ring-2 hover:ring-foreground/50 focus-visible:ring-2 focus-visible:ring-foreground", TONE_BG[m.tone], m.end != null ? "h-3 min-w-[3px]" : "size-2.5 -translate-x-1/2 rounded-full ring-2")}
                        style={{ left: `${left}%`, width: m.end != null ? `${w}%` : undefined }} {...on(m.tip)} />
                    );
                  })}
                </div>
              ))}
            </div>
          </div>
        ))}
        <span />
        <div className="relative h-5 border-t border-border-strong font-mono text-2xs text-subtle-foreground" aria-hidden>
          {ticks.map((t, i) => <span key={i} className={cn("absolute top-1", i === 0 ? "left-0" : i === 4 ? "right-0" : "-translate-x-1/2")} style={i > 0 && i < 4 ? { left: `${(i / 4) * 100}%` } : undefined}>{hhmm(t)}</span>)}
        </div>
      </div>
      <TipLayer tip={tip} />
    </div>
  );
}
