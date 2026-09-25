"use client";

import { useEffect, useState } from "react";
import { toast } from "sonner";
import { api, type Stats } from "@/lib/api";
import { cn } from "@/lib/utils";
import { Skeleton } from "@/components/ui/primitives";
import { BarChart3, CalendarDays } from "lucide-react";
import { HeatCalendar, IconTile, Panel as VizPanel, Segmented } from "@/components/ui/viz";

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
  const runtime = stats?.runtime;
  const rt = runtime?.totals;

  return (
    <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
      <div className="mx-auto max-w-6xl px-4 py-6 lg:px-8">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div className="flex items-center gap-3">
            <IconTile icon={BarChart3} />
            <div>
              <h1 className="text-title font-semibold tracking-tight">Reports</h1>
              <p className="text-xs text-subtle-foreground">Demand, outcomes, investigation timing, tool and model performance</p>
            </div>
          </div>
          <Segmented label="Period" value={String(days)} onChange={(v) => setDays(Number(v))} options={RANGES.map((r) => ({ id: String(r), label: `${r}d` }))} />
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

        <div className="mt-4">
          <VizPanel icon={CalendarDays} title="Demand calendar" meta="tickets and conversations per day · busiest day in white">
            {stats ? <HeatCalendar days={stats.series.map((s) => ({ day: s.day, value: s.tickets + s.conversations }))} unit="request" /> : <Skeleton className="h-36" />}
          </VizPanel>
        </div>

        <div className="mt-4 grid gap-3 lg:grid-cols-2">
          <Panel title="Tickets raised per day">{stats ? <DailyBars data={stats.series.map((s) => ({ day: s.day, value: s.tickets }))} unit="ticket" /> : <Skeleton className="h-48" />}</Panel>
          <Panel title="Conversations per day">{stats ? <DailyBars data={stats.series.map((s) => ({ day: s.day, value: s.conversations }))} unit="conversation" /> : <Skeleton className="h-48" />}</Panel>
        </div>

        <div className="mt-6">
          <h2 className="text-title font-semibold tracking-tight">L2 runtime &amp; compute</h2>
          <p className="mt-0.5 text-sm text-muted-foreground">Observed investigation time, Jev/tool/model latency and hardware/token telemetry captured by Hermes.</p>
        </div>
        <div className="mt-3 grid grid-cols-2 gap-3 lg:grid-cols-4">
          <Tile label="L2 runs" value={rt?.Runs} note={rt ? `Avg ${fmtSeconds(rt.AvgRunSeconds)} · max ${fmtSeconds(rt.MaxRunSeconds)}` : undefined} />
          <Tile label="SQL reads / run" value={rt?.AvgSqlReadsPerRun == null ? (rt ? "—" : undefined) : rt.AvgSqlReadsPerRun.toFixed(1)} note="Average audited reads" />
          <Tile label="Jev latency" value={rt?.AvgJevMs == null ? (rt ? "—" : undefined) : fmtMs(rt.AvgJevMs)} note="Average decision call" />
          <Tile label="Writer latency" value={rt?.AvgModelMs == null ? (rt ? "—" : undefined) : fmtMs(rt.AvgModelMs)} note="Average model call" />
          <Tile label="Tool latency" value={rt?.AvgToolMs == null ? (rt ? "—" : undefined) : fmtMs(rt.AvgToolMs)} note={rt ? `${rt.ToolErrors ?? 0} failed tool calls` : undefined} />
          <Tile label="Model tokens" value={rt?.TotalTokens == null ? (rt ? "—" : undefined) : compactNumber(rt.TotalTokens)} note={rt ? `${rt.ModelErrors} failed model calls` : undefined} />
          <Tile label="GPU utilisation" value={rt?.AvgGpuUtilPct == null ? (rt ? "—" : undefined) : `${rt.AvgGpuUtilPct.toFixed(0)}%`} note={rt?.PeakGpuVramMb == null ? "No GPU sample" : `Peak VRAM ${compactNumber(rt.PeakGpuVramMb)} MB`} />
          <Tile label="CPU utilisation" value={rt?.AvgCpuUtilPct == null ? (rt ? "—" : undefined) : `${rt.AvgCpuUtilPct.toFixed(0)}%`} note="Average captured compute samples" />
        </div>

        <div className="mt-3 grid gap-3 lg:grid-cols-2">
          <Panel title="Model tokens per day">{!stats ? <Skeleton className="h-48" /> : runtime ? <DailyBars data={runtime.series.map((s) => ({ day: String(s.Day), value: Number(s.Tokens) || 0 }))} unit="token" /> : <TelemetryUnavailable />}</Panel>
          <Panel title="Observed calls per day">{!stats ? <Skeleton className="h-48" /> : runtime ? <DailyBars data={runtime.series.map((s) => ({ day: String(s.Day), value: Number(s.ToolCalls) + Number(s.ModelCalls) + Number(s.JevCalls) }))} unit="call" /> : <TelemetryUnavailable />}</Panel>
        </div>

        <div className="mt-3 grid gap-3 lg:grid-cols-2">
          <Panel title="Slowest tools">{!stats ? <Skeleton className="h-48" /> : runtime ? <RuntimeTable rows={runtime.tools.map((x) => ({ label: x.Label, calls: x.Calls, errors: x.Errors, avg: x.AvgMs }))} /> : <TelemetryUnavailable />}</Panel>
          <Panel title="Writer models">{!stats ? <Skeleton className="h-48" /> : runtime ? <RuntimeTable rows={runtime.models.map((x) => ({ label: `${x.Provider} · ${x.Model}`, calls: x.Calls, errors: 0, avg: x.AvgMs, extra: x.Tokens == null ? "—" : `${compactNumber(x.Tokens)} tokens` }))} /> : <TelemetryUnavailable />}</Panel>
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
const fmtSeconds = (s: number | null) => s == null ? "—" : s < 60 ? `${Math.round(s)}s` : s < 3600 ? `${(s / 60).toFixed(1)}m` : `${(s / 3600).toFixed(1)}h`;
const fmtMs = (v: number) => v < 1000 ? `${Math.round(v)}ms` : `${(v / 1000).toFixed(1)}s`;
const compactNumber = (v: number) => new Intl.NumberFormat("en-IN", { notation: "compact", maximumFractionDigits: 1 }).format(v);

function Tile({ label, value, note }: { label: string; value?: number | string; note?: string }) {
  return (
    <div className="rounded-2xl border bg-canvas p-1.5">
      <p className="px-2.5 pb-2 pt-1 text-xs text-subtle-foreground">{label}</p>
      <div className="rounded-xl border bg-surface px-3 py-3">
        {value === undefined ? <Skeleton className="h-8 w-16" /> : <p className="font-mono text-2xl font-medium tabular-nums tracking-tight">{value}</p>}
        {note && <p className="mt-1 truncate font-mono text-2xs text-subtle-foreground">{note}</p>}
      </div>
    </div>
  );
}

function Panel({ title, children }: { title: string; children: React.ReactNode }) {
  return <VizPanel title={title}>{children}</VizPanel>;
}

// Single series: one hue (brand), 4px rounded tops on a baseline, 2px gaps, hover tooltip per bar.
function DailyBars({ data, unit }: { data: { day: string; value: number }[]; unit: string }) {
  const [hover, setHover] = useState<number | null>(null);
  if (!data.length) return <p className="py-10 text-center text-sm text-muted-foreground">No {unit} data in this period.</p>;
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
                  className={cn("fill-signal transition-opacity", hover !== null && hover !== i && "opacity-45")}
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

function TelemetryUnavailable() {
  return <p className="py-10 text-center text-sm text-muted-foreground">Runtime telemetry will appear after the updated L1 API is running.</p>;
}

function RuntimeTable({ rows }: { rows: { label: string; calls: number; errors: number; avg: number | null; extra?: string }[] }) {
  if (!rows.length) return <p className="text-sm text-muted-foreground">No runtime telemetry in this period.</p>;
  return (
    <div className="overflow-x-auto">
      <table className="w-full text-meta">
        <thead className="text-left text-2xs uppercase tracking-wider text-subtle-foreground">
          <tr><th className="py-2 pr-3 font-semibold">Operation</th><th className="px-2 py-2 font-semibold">Calls</th><th className="px-2 py-2 font-semibold">Errors</th><th className="py-2 pl-2 text-right font-semibold">Avg</th></tr>
        </thead>
        <tbody className="divide-y">
          {rows.map((r) => (
            <tr key={r.label}>
              <td className="py-2 pr-3"><p className="font-medium">{r.label}</p>{r.extra && <p className="text-2xs text-subtle-foreground">{r.extra}</p>}</td>
              <td className="px-2 py-2 tabular-nums">{r.calls}</td>
              <td className={cn("px-2 py-2 tabular-nums", r.errors > 0 && "text-destructive")}>{r.errors}</td>
              <td className="py-2 pl-2 text-right tabular-nums">{r.avg == null ? "—" : fmtMs(r.avg)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export function Ranked({ rows }: { rows: { label: string; count: number }[] }) {
  const max = Math.max(1, ...rows.map((r) => r.count));
  if (!rows.length) return <p className="text-sm text-muted-foreground">No tickets in this period.</p>;
  return (
    <ul className="space-y-2.5">
      {rows.slice(0, 8).map((r) => (
        <li key={r.label} className="text-meta">
          <div className="flex justify-between gap-2">
            <span className="truncate font-mono text-xs text-muted-foreground">{r.label}</span>
            <span className="font-mono text-xs tabular-nums">{r.count}</span>
          </div>
          <div className="mt-1 h-1.5 rounded-full bg-surface-3">
            <div
              className="h-full rounded-full bg-signal"
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
