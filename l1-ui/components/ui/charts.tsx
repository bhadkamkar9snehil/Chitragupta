"use client";

import { useRef, useState, type FocusEvent, type MouseEvent, type ReactNode } from "react";
import { cn } from "@/lib/utils";
import { TONE_BG, TONE_FILL, type VizTone } from "./viz";

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
