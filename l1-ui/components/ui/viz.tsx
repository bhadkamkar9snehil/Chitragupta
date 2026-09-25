"use client";

import { useState, type ReactNode } from "react";
import { Check, Copy, type LucideIcon } from "lucide-react";
import { cn } from "@/lib/utils";

// The console's one visual language: a panel shell (dashed icon tile + title + meta) around an inset body,
// mono numerals, one mint signal for what matters and greys for everything else.

export type VizTone = "signal" | "strong" | "mid" | "faint" | "danger" | "warn" | "info";

export const TONE_BG: Record<VizTone, string> = {
  signal: "bg-signal",
  strong: "bg-muted-foreground",
  mid: "bg-subtle-foreground",
  faint: "bg-border-strong",
  danger: "bg-destructive",
  warn: "bg-warning",
  info: "bg-info",
};
export const TONE_FILL: Record<VizTone, string> = {
  signal: "fill-signal",
  strong: "fill-muted-foreground",
  mid: "fill-subtle-foreground",
  faint: "fill-border-strong",
  danger: "fill-destructive",
  warn: "fill-warning",
  info: "fill-info",
};
export const TONE_TEXT: Record<VizTone, string> = {
  signal: "text-signal",
  strong: "text-foreground",
  mid: "text-muted-foreground",
  faint: "text-subtle-foreground",
  danger: "text-destructive",
  warn: "text-warning",
  info: "text-info",
};

export function IconTile({ icon: Icon, active, className }: { icon: LucideIcon; active?: boolean; className?: string }) {
  return (
    <span className={cn("grid size-9 shrink-0 place-items-center rounded-lg border border-dashed", active ? "border-signal text-signal" : "border-border-strong text-foreground", className)} aria-hidden>
      <Icon className="size-4" />
    </span>
  );
}

export function Panel({ icon, title, meta, actions, children, className, pad = "default", as: Tag = "section" }: {
  icon?: LucideIcon;
  title: ReactNode;
  meta?: ReactNode;
  actions?: ReactNode;
  children: ReactNode;
  className?: string;
  /** Inset body padding: lists and tables go "none", dense rows "tight". */
  pad?: "default" | "tight" | "none";
  as?: "section" | "div";
}) {
  return (
    <Tag className={cn("flex min-w-0 flex-col rounded-2xl border bg-canvas p-1.5", className)}>
      <header className="flex min-h-14 items-center gap-3 px-2.5 pb-2.5 pt-1.5">
        {icon && <IconTile icon={icon} />}
        <div className="min-w-0 flex-1">
          <h2 className="truncate text-sm font-semibold tracking-tight">{title}</h2>
          {meta && <p className="line-clamp-2 text-xs text-subtle-foreground">{meta}</p>}
        </div>
        {actions && <div className="flex shrink-0 items-center gap-2">{actions}</div>}
      </header>
      <div className={cn("min-h-0 flex-1 rounded-xl border bg-surface", pad === "default" && "p-4", pad === "tight" && "p-2")}>{children}</div>
    </Tag>
  );
}

export function Headline({ value, unit, note, noteTone = "signal", className }: { value: ReactNode; unit?: ReactNode; note?: ReactNode; noteTone?: VizTone; className?: string }) {
  return (
    <p className={cn("flex flex-wrap items-baseline gap-x-2.5 gap-y-1", className)}>
      <span className="font-mono text-2xl font-medium tracking-tight tabular-nums sm:text-3xl">{value}</span>
      {unit && <span className="font-mono text-lg text-muted-foreground">{unit}</span>}
      {note && <span className={cn("font-mono text-xs", TONE_TEXT[noteTone])}>{note}</span>}
    </p>
  );
}

export function Swatch({ tone, className }: { tone: VizTone | "hatch"; className?: string }) {
  return <span className={cn("inline-block size-2.5 shrink-0 rounded-[3px]", tone === "hatch" ? "hatch" : TONE_BG[tone], className)} aria-hidden />;
}

export type LegendRow = { label: ReactNode; value?: ReactNode; tone: VizTone | "hatch"; onClick?: () => void; active?: boolean };

export function Legend({ rows, className, inline }: { rows: LegendRow[]; className?: string; inline?: boolean }) {
  return (
    <ul className={cn(inline ? "flex flex-wrap gap-x-5 gap-y-1.5" : "space-y-1", className)}>
      {rows.map((r, i) => {
        const body = (
          <>
            <Swatch tone={r.tone} />
            <span className={cn("min-w-0 truncate font-mono text-xs", r.active === false ? "text-subtle-foreground" : "text-muted-foreground")}>{r.label}</span>
            {r.value !== undefined && <span className={cn("font-mono text-xs tabular-nums text-foreground", !inline && "ml-auto pl-3")}>{r.value}</span>}
          </>
        );
        return (
          <li key={i}>
            {r.onClick ? (
              <button type="button" onClick={r.onClick} className={cn("flex w-full items-center gap-2.5 rounded-md py-1 text-left hover:bg-surface-2", !inline && "-mx-1.5 px-1.5")}>{body}</button>
            ) : (
              <div className={cn("flex items-center gap-2.5", !inline && "py-1")}>{body}</div>
            )}
          </li>
        );
      })}
    </ul>
  );
}

// Win / tie / loss style composition: rounded segments with small gaps, remainder hatched.
export function SegmentBar({ segments, className, label }: { segments: { value: number; tone: VizTone | "hatch"; label: string }[]; className?: string; label: string }) {
  const total = segments.reduce((n, s) => n + s.value, 0);
  if (!total) return <div className={cn("h-2.5 rounded-full hatch", className)} role="img" aria-label={`${label}: no data`} />;
  return (
    <div className={cn("flex h-2.5 gap-1", className)} role="img" aria-label={`${label}: ${segments.map((s) => `${s.label} ${s.value}`).join(", ")}`}>
      {segments.filter((s) => s.value > 0).map((s) => (
        <span key={s.label} title={`${s.label} · ${s.value}`} className={cn("h-full min-w-1.5 rounded-full", s.tone === "hatch" ? "hatch" : TONE_BG[s.tone])} style={{ flexGrow: s.value, flexBasis: 0 }} />
      ))}
    </div>
  );
}

// Tick gauge: a ring of short strokes, filled up to the value. `sweep` 180 = semicircle, 300 = open ring.
export function TickGauge({ value, center, caption, ticks = 56, sweep = 200, className, label }: {
  value: number;
  center: ReactNode;
  caption?: ReactNode;
  ticks?: number;
  sweep?: number;
  className?: string;
  label: string;
}) {
  const v = Math.max(0, Math.min(1, value));
  const R = 92, r = 74, cx = 110, cy = 110;
  const start = -90 - sweep / 2;
  const on = Math.round(v * ticks);
  const half = sweep <= 200;
  return (
    <div className={cn("relative mx-auto w-full max-w-72", className)} role="img" aria-label={`${label}: ${Math.round(v * 100)}%`}>
      <svg viewBox={half ? "0 0 220 132" : "0 0 220 220"} className="w-full" aria-hidden>
        {Array.from({ length: ticks }, (_, i) => {
          const a = ((start + (sweep * i) / (ticks - 1)) * Math.PI) / 180;
          const lit = i < on;
          return (
            <line
              key={i}
              x1={cx + r * Math.cos(a)} y1={cy + r * Math.sin(a)} x2={cx + R * Math.cos(a)} y2={cy + R * Math.sin(a)}
              strokeWidth={3.2} strokeLinecap="round"
              className={lit ? "stroke-signal" : "stroke-border-strong"}
              opacity={lit ? 0.55 + 0.45 * (i / Math.max(1, on)) : 1}
            />
          );
        })}
      </svg>
      <div className={cn("absolute inset-x-0 text-center", half ? "bottom-1" : "top-1/2 -translate-y-1/2")}>
        <div className="text-4xl font-medium tracking-tight tabular-nums">{center}</div>
        {caption && <div className="mt-0.5 font-mono text-xs text-subtle-foreground">{caption}</div>}
      </div>
    </div>
  );
}

export function Sparkline({ values, threshold, tone = "mid", className, label }: { values: number[]; threshold?: number; tone?: VizTone; className?: string; label: string }) {
  if (values.length < 2) return <div className={cn("h-8", className)} />;
  const max = Math.max(threshold ?? 0, ...values, 1);
  const W = 120, H = 32;
  const pts = values.map((v, i) => `${(i / (values.length - 1)) * W},${H - 2 - (v / max) * (H - 6)}`).join(" ");
  return (
    <svg viewBox={`0 0 ${W} ${H}`} preserveAspectRatio="none" className={cn("h-8 w-28", className)} role="img" aria-label={label}>
      {threshold != null && <line x1={0} x2={W} y1={H - 2 - (threshold / max) * (H - 6)} y2={H - 2 - (threshold / max) * (H - 6)} className="stroke-subtle-foreground" strokeDasharray="2 3" strokeWidth={1} vectorEffect="non-scaling-stroke" />}
      <polyline points={pts} fill="none" strokeWidth={1.6} strokeLinejoin="round" strokeLinecap="round" vectorEffect="non-scaling-stroke" className={tone === "signal" ? "stroke-signal" : tone === "danger" ? "stroke-destructive" : "stroke-muted-foreground"} />
    </svg>
  );
}

// Probabilities returned by a Jev decision, highest first; the chosen one is signal.
export function ProbBars({ scores, chosen, max = 5, className }: { scores: [string, number][]; chosen?: string; max?: number; className?: string }) {
  return (
    <ul className={cn("space-y-1.5", className)}>
      {scores.slice(0, max).map(([name, p]) => {
        const hit = chosen ? name === chosen : false;
        return (
          <li key={name} className="flex items-center gap-2.5 text-xs">
            <span className={cn("w-28 shrink-0 truncate font-mono", hit ? "text-foreground" : "text-subtle-foreground")} title={name}>{name.replace(/_/g, " ").toLowerCase()}</span>
            <span className="relative h-1.5 min-w-0 flex-1 overflow-hidden rounded-full bg-surface-3">
              <span className={cn("absolute inset-y-0 left-0 rounded-full", hit ? "bg-signal" : "bg-subtle-foreground")} style={{ width: `${Math.max(1.5, Math.min(100, p * 100))}%` }} />
            </span>
            <span className={cn("w-9 shrink-0 text-right font-mono tabular-nums", hit ? "text-signal" : "text-subtle-foreground")}>{Math.round(p * 100)}%</span>
          </li>
        );
      })}
    </ul>
  );
}

// Attribute rows with copy, as on a span inspector.
export function Attributes({ rows, className }: { rows: { k: string; v: ReactNode; copy?: string; tone?: VizTone }[]; className?: string }) {
  return (
    <dl className={cn("divide-y", className)}>
      {rows.map((r) => (
        <div key={r.k} className="group flex min-h-10 items-center gap-3 py-2">
          <dt className="w-32 shrink-0 font-mono text-xs text-subtle-foreground">{r.k}</dt>
          <dd className={cn("min-w-0 flex-1 break-words font-mono text-xs", r.tone ? TONE_TEXT[r.tone] : "text-foreground")}>{r.v}</dd>
          {r.copy && <CopyButton text={r.copy} label={r.k} />}
        </div>
      ))}
    </dl>
  );
}

export function CopyButton({ text, label }: { text: string; label: string }) {
  const [done, setDone] = useState(false);
  return (
    <button
      type="button"
      aria-label={`Copy ${label}`}
      onClick={() => navigator.clipboard?.writeText(text).then(() => { setDone(true); setTimeout(() => setDone(false), 1200); }).catch(() => {})}
      className="grid size-7 shrink-0 place-items-center rounded-md text-subtle-foreground opacity-70 hover:bg-surface-2 hover:text-foreground hover:opacity-100 group-hover:opacity-100"
    >
      {done ? <Check className="size-3.5" /> : <Copy className="size-3.5" />}
    </button>
  );
}

// Pill segmented control (Calls / Latency / Errors).
export function Segmented<T extends string>({ options, value, onChange, label, className }: { options: { id: T; label: ReactNode }[]; value: T; onChange: (v: T) => void; label: string; className?: string }) {
  return (
    <div role="radiogroup" aria-label={label} className={cn("flex rounded-lg border bg-surface p-0.5", className)}>
      {options.map((o) => (
        <button
          key={o.id}
          type="button"
          role="radio"
          aria-checked={value === o.id}
          onClick={() => onChange(o.id)}
          className={cn("h-8 min-w-0 flex-1 rounded-md px-3 font-mono text-xs text-subtle-foreground hover:text-foreground sm:flex-none", value === o.id && "bg-surface-3 text-foreground")}
        >
          {o.label}
        </button>
      ))}
    </div>
  );
}

// Waterfall of spans against a shared time axis (traces view).
export type Span = { id: string; label: string; sub?: string; start: number; end: number; tone: VizTone; right?: string };

export function Waterfall({ spans, total, selected, onPick, className }: { spans: Span[]; total: number; selected?: string | null; onPick?: (id: string) => void; className?: string }) {
  const T = Math.max(1, total);
  return (
    <ol className={cn("space-y-0.5", className)}>
      {spans.map((s) => {
        const left = Math.max(0, Math.min(100, (s.start / T) * 100));
        const width = Math.max(0.8, Math.min(100 - left, ((s.end - s.start) / T) * 100));
        return (
          <li key={s.id}>
            <button
              type="button"
              onClick={() => onPick?.(s.id)}
              aria-pressed={selected === s.id}
              className={cn("grid w-full grid-cols-[minmax(0,11rem)_minmax(0,1fr)_3.5rem] items-center gap-3 rounded-md px-2 py-1.5 text-left hover:bg-surface-2 sm:grid-cols-[minmax(0,14rem)_minmax(0,1fr)_4rem]", selected === s.id && "bg-surface-2")}
            >
              <span className="min-w-0">
                <span className="block truncate font-mono text-xs text-foreground">{s.label}</span>
                {s.sub && <span className="block truncate text-2xs text-subtle-foreground">{s.sub}</span>}
              </span>
              <span className="relative h-2 rounded-full">
                <span className="absolute inset-y-[3px] left-0 right-0 rounded-full bg-surface-3" />
                <span className={cn("absolute inset-y-0 rounded-full", TONE_BG[s.tone])} style={{ left: `${left}%`, width: `${width}%` }} />
              </span>
              <span className={cn("text-right font-mono text-xs tabular-nums", s.tone === "danger" ? "text-destructive" : "text-muted-foreground")}>{s.right}</span>
            </button>
          </li>
        );
      })}
    </ol>
  );
}

// Compact stat used in panel footers: grey label over a mono value.
export function Stat({ label, value, tone }: { label: string; value: ReactNode; tone?: VizTone }) {
  return (
    <div className="min-w-0">
      <p className="truncate text-xs text-subtle-foreground">{label}</p>
      <p className={cn("mt-0.5 truncate font-mono text-sm tabular-nums", tone ? TONE_TEXT[tone] : "text-foreground")}>{value}</p>
    </div>
  );
}

export const ms = (v?: number | null) => (v == null ? "—" : v < 1000 ? `${Math.round(v)} ms` : v < 60_000 ? `${(v / 1000).toFixed(v < 10_000 ? 2 : 1)} s` : v < 3_600_000 ? `${(v / 60_000).toFixed(1)} min` : `${(v / 3_600_000).toFixed(1)} h`);
export const pct = (v?: number | null) => (v == null ? "—" : `${Math.round(v * 100)}%`);

// Calendar heat grid: weeks across, weekdays down; five intensity steps of the signal, the peak day in white.
const HEAT = ["bg-surface-3", "bg-signal/25", "bg-signal/45", "bg-signal/70", "bg-signal"];
export function HeatCalendar({ days, unit, className }: { days: { day: string; value: number }[]; unit: string; className?: string }) {
  if (!days.length) return <p className="py-8 text-center text-sm text-muted-foreground">No {unit} data in this period.</p>;
  const max = Math.max(1, ...days.map((d) => d.value));
  const peak = days.reduce((a, b) => (b.value > a.value ? b : a));
  const first = new Date(days[0].day);
  const offset = (first.getDay() + 6) % 7; // Monday first
  const cells: ({ day: string; value: number } | null)[] = [...Array(offset).fill(null), ...days];
  const weeks = Math.ceil(cells.length / 7);
  const fmt = (d: string) => new Date(d).toLocaleDateString("en-IN", { weekday: "short", day: "numeric", month: "short" });
  return (
    <div className={cn("flex gap-3", className)}>
      <div className="grid grid-rows-7 gap-1 pt-0.5 font-mono text-2xs leading-4 text-subtle-foreground" aria-hidden>
        {["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"].map((d) => <span key={d} className="h-4">{d}</span>)}
      </div>
      <div className="grid min-w-0 flex-1 grid-flow-col grid-rows-7 gap-1" style={{ gridTemplateColumns: `repeat(${weeks}, minmax(0, 2.25rem))` }} role="img" aria-label={`${unit}s per day; busiest ${fmt(peak.day)} with ${peak.value}`}>
        {cells.map((c, i) => c ? (
          <span
            key={c.day}
            title={`${fmt(c.day)} · ${c.value} ${unit}${c.value === 1 ? "" : "s"}`}
            className={cn("h-4 rounded-[3px] transition-transform hover:scale-110", c === peak && c.value > 0 ? "bg-foreground" : HEAT[c.value === 0 ? 0 : Math.min(4, Math.ceil((c.value / max) * 4))])}
          />
        ) : <span key={`pad-${i}`} className="h-4" />)}
      </div>
    </div>
  );
}

// Every screen opens the same way: dashed icon tile, title, one mono line of context, actions on the right.
export function PageTitle({ icon, title, meta, children, className }: { icon: LucideIcon; title: ReactNode; meta?: ReactNode; children?: ReactNode; className?: string }) {
  return (
    <div className={cn("flex min-w-0 items-center gap-3", className)}>
      <IconTile icon={icon} />
      <div className="min-w-0 flex-1">
        <h1 className="truncate text-title font-semibold tracking-tight">{title}</h1>
        {meta && <p className="truncate font-mono text-2xs text-subtle-foreground">{meta}</p>}
      </div>
      {children && <div className="flex shrink-0 items-center gap-1.5">{children}</div>}
    </div>
  );
}
