"use client";

import { useEffect, useState } from "react";
import { toast } from "sonner";
import { api, type Stats } from "@/lib/api";
import { cn } from "@/lib/utils";
import { Skeleton } from "@/components/ui/primitives";

const RANGES = [7, 14, 30, 90];

export function ReportsView() {
  const [days, setDays] = useState(14);
  const [stats, setStats] = useState<Stats | null>(null);

  useEffect(() => {
    api.admin.stats(days).then(setStats).catch((e: Error) => toast.error(e.message));
  }, [days]);

  const t = stats?.totals;
  const deflection = t && t.conversations ? Math.round((t.answeredWithoutTicket / t.conversations) * 100) : null;
  const helpful = t && (t.thumbsUp ?? 0) + (t.thumbsDown ?? 0) > 0 ? Math.round(((t.thumbsUp ?? 0) / ((t.thumbsUp ?? 0) + (t.thumbsDown ?? 0))) * 100) : null;

  return (
    <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
      <div className="mx-auto max-w-6xl px-4 py-6 lg:px-8">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div>
            <h1 className="text-heading font-semibold tracking-tight">Reports</h1>
            <p className="mt-0.5 text-sm text-muted-foreground">Tickets raised in the period and how the helpdesk handled conversations.</p>
          </div>
          <div className="flex rounded-lg border bg-surface p-0.5" role="radiogroup" aria-label="Period">
            {RANGES.map((r) => (
              <button key={r} role="radio" aria-checked={days === r} onClick={() => setDays(r)} className={cn("h-8 rounded-md px-3 text-meta font-medium text-muted-foreground", days === r && "bg-surface-3 text-foreground")}>
                {r}d
              </button>
            ))}
          </div>
        </div>

        <div className="mt-6 grid grid-cols-2 gap-3 lg:grid-cols-4">
          <Tile label="Tickets raised" value={t?.tickets} note={t ? `${t.open} open · ${t.resolved} resolved` : undefined} />
          <Tile label="Waiting on requester" value={t?.waiting} note="Support asked a question" />
          <Tile label="Median time to first reply" value={t?.medianFirstReplyHours == null ? (t ? "—" : undefined) : fmtHours(t.medianFirstReplyHours)} note="From L2" />
          <Tile label="Satisfaction" value={t ? (t.csat == null ? "—" : `${t.csat.toFixed(1)} / 5`) : undefined} note={t ? `${t.ratings} rating${t.ratings === 1 ? "" : "s"}` : undefined} />
          <Tile label="Conversations" value={t?.conversations} note={deflection == null ? undefined : `${deflection}% answered without a ticket`} />
          <Tile label="Answers marked helpful" value={helpful == null ? (t ? "—" : undefined) : `${helpful}%`} note={t ? `${t.thumbsUp ?? 0} up · ${t.thumbsDown ?? 0} down` : undefined} />
          <Tile label="Tickets raised from chat" value={t?.fromChat} note="Handed over by the assistant" />
          <Tile label="Assistant reply time" value={t?.avgLatencyMs == null ? (t ? "—" : undefined) : `${(t.avgLatencyMs / 1000).toFixed(1)}s`} note="Average, end to end" />
        </div>

        <div className="mt-6 grid gap-3 lg:grid-cols-2">
          <Panel title="Tickets raised per day">{stats ? <DailyBars data={stats.series.map((s) => ({ day: s.day, value: s.tickets }))} unit="ticket" /> : <Skeleton className="h-48" />}</Panel>
          <Panel title="Conversations per day">{stats ? <DailyBars data={stats.series.map((s) => ({ day: s.day, value: s.conversations }))} unit="conversation" /> : <Skeleton className="h-48" />}</Panel>
        </div>

        <div className="mt-3 grid gap-3 lg:grid-cols-3">
          <Panel title="By state">{stats ? <Ranked rows={stats.byState} /> : <Skeleton className="h-40" />}</Panel>
          <Panel title="By area">{stats ? <Ranked rows={stats.byArea} /> : <Skeleton className="h-40" />}</Panel>
          <Panel title="By type">{stats ? <Ranked rows={stats.byType} /> : <Skeleton className="h-40" />}</Panel>
        </div>

        {stats && (
          <details className="mt-3 rounded-xl border bg-surface">
            <summary className="cursor-pointer px-4 py-3 text-sm font-medium">Daily numbers as a table</summary>
            <div className="overflow-x-auto border-t">
              <table className="w-full text-meta tabular-nums">
                <thead className="bg-surface-2 text-left text-2xs uppercase tracking-wider text-subtle-foreground">
                  <tr>{["Day", "Tickets", "Resolved", "Conversations", "Answered without ticket"].map((h) => <th key={h} className="px-4 py-2 font-semibold">{h}</th>)}</tr>
                </thead>
                <tbody className="divide-y">
                  {[...stats.series].reverse().map((s) => (
                    <tr key={s.day}>
                      <td className="px-4 py-2">{s.day}</td>
                      <td className="px-4 py-2">{s.tickets}</td>
                      <td className="px-4 py-2">{s.resolved}</td>
                      <td className="px-4 py-2">{s.conversations}</td>
                      <td className="px-4 py-2">{s.answered}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </details>
        )}
      </div>
    </div>
  );
}

const fmtHours = (h: number) => (h < 1 ? `${Math.round(h * 60)}m` : h < 48 ? `${h.toFixed(1)}h` : `${(h / 24).toFixed(1)}d`);

function Tile({ label, value, note }: { label: string; value?: number | string; note?: string }) {
  return (
    <div className="rounded-xl border bg-surface p-4">
      <p className="text-meta text-muted-foreground">{label}</p>
      {value === undefined ? <Skeleton className="mt-2 h-8 w-16" /> : <p className="mt-1 text-display font-semibold tabular-nums tracking-tight">{value}</p>}
      {note && <p className="mt-1 text-xs text-subtle-foreground">{note}</p>}
    </div>
  );
}

function Panel({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <section className="rounded-xl border bg-surface p-4" aria-label={title}>
      <h2 className="text-sm font-semibold">{title}</h2>
      <div className="mt-4">{children}</div>
    </section>
  );
}

// Single series: one hue (brand), 4px rounded tops on a baseline, 2px gaps, hover tooltip per bar.
function DailyBars({ data, unit }: { data: { day: string; value: number }[]; unit: string }) {
  const [hover, setHover] = useState<number | null>(null);
  const max = Math.max(1, ...data.map((d) => d.value));
  const W = 600, H = 180, pad = 22, gutter = 28, bw = (W - gutter - 2) / data.length;
  const ticks = [0, Math.ceil(max / 2), max];
  const label = (d: string) => new Date(d).toLocaleDateString("en-IN", { day: "numeric", month: "short" });
  return (
    <div className="relative">
      <svg viewBox={`0 0 ${W} ${H + pad}`} className="w-full" role="img" aria-label={`${unit}s per day`} onMouseLeave={() => setHover(null)}>
        {ticks.map((v) => {
          const y = H - (v / max) * (H - 12);
          return (
            <g key={v}>
              <line x1={gutter} x2={W} y1={y} y2={y} className="stroke-border" strokeWidth={1} />
              <text x={gutter - 6} y={y + 4} textAnchor="end" className="fill-subtle-foreground text-2xs tabular-nums">{v}</text>
            </g>
          );
        })}
        {data.map((d, i) => {
          const h = (d.value / max) * (H - 12);
          const x = gutter + i * bw + 1;
          return (
            <g key={d.day} onMouseEnter={() => setHover(i)}>
              <rect x={x} y={0} width={bw} height={H} fill="transparent" />
              {d.value > 0 && (
                <path
                  d={`M${x + 1},${H} v${-(h - Math.min(4, h))} q0,${-Math.min(4, h)} ${Math.min(4, h)},${-Math.min(4, h)} h${Math.max(0, bw - 2 - 2 * Math.min(4, h))} q${Math.min(4, h)},0 ${Math.min(4, h)},${Math.min(4, h)} v${h - Math.min(4, h)} z`}
                  className={cn("fill-primary transition-opacity", hover !== null && hover !== i && "opacity-45")}
                />
              )}
            </g>
          );
        })}
        {data.map((d, i) =>
          i % Math.ceil(data.length / 7) === 0 ? (
            <text key={d.day} x={gutter + i * bw + bw / 2} y={H + 16} textAnchor="middle" className="fill-subtle-foreground text-2xs">{label(d.day)}</text>
          ) : null,
        )}
      </svg>
      {hover !== null && (
        <div
          className="pointer-events-none absolute top-0 z-10 -translate-x-1/2 rounded-md border bg-surface px-2.5 py-1.5 text-xs shadow-pop"
          ref={(el) => {
            el?.style.setProperty("left", `${((gutter + (hover + 0.5) * bw) / W) * 100}%`);
          }}
        >
          <p className="font-medium">{label(data[hover].day)}</p>
          <p className="tabular-nums text-muted-foreground">{data[hover].value} {unit}{data[hover].value === 1 ? "" : "s"}</p>
        </div>
      )}
    </div>
  );
}

function Ranked({ rows }: { rows: { label: string; count: number }[] }) {
  const max = Math.max(1, ...rows.map((r) => r.count));
  if (!rows.length) return <p className="text-sm text-muted-foreground">No tickets in this period.</p>;
  return (
    <ul className="space-y-2.5">
      {rows.slice(0, 8).map((r) => (
        <li key={r.label} className="text-meta">
          <div className="flex justify-between gap-2">
            <span className="truncate">{r.label}</span>
            <span className="tabular-nums text-muted-foreground">{r.count}</span>
          </div>
          <div className="mt-1 h-1.5 rounded-full bg-surface-3">
            <div
              className="h-full rounded-full bg-primary"
              ref={(el) => {
                el?.style.setProperty("width", `${(r.count / max) * 100}%`);
              }}
            />
          </div>
        </li>
      ))}
    </ul>
  );
}
