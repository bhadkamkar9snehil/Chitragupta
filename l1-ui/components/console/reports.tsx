"use client";

import { useEffect, useState } from "react";
import { toast } from "sonner";
import { BarChart3, CalendarDays, Cpu, Layers, ListOrdered, PhoneCall, Timer } from "lucide-react";
import { api, type Stats } from "@/lib/api";
import { cn } from "@/lib/utils";
import { Skeleton } from "@/components/ui/primitives";
import { HeatCalendar, Legend, PageTitle, Panel, Segmented } from "@/components/ui/viz";
import { StackColumns, VolumeBar, type Column } from "@/components/ui/charts";

const RANGES = [7, 14, 30, 90];
const WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

const fmtHours = (h: number) => (h < 1 ? `${Math.round(h * 60)} min` : h < 48 ? `${h.toFixed(1)} h` : `${(h / 24).toFixed(1)} d`);
const fmtSeconds = (s: number | null) => (s == null ? "—" : s < 60 ? `${Math.round(s)} s` : s < 3600 ? `${(s / 60).toFixed(1)} min` : `${(s / 3600).toFixed(1)} h`);
const fmtMs = (v: number) => (v < 1000 ? `${Math.round(v)} ms` : `${(v / 1000).toFixed(1)} s`);
const compact = (v: number) => new Intl.NumberFormat("en-US", { notation: "compact", maximumFractionDigits: 1 }).format(v);
const vram = (mb: number) => (mb >= 1024 ? `${(mb / 1024).toFixed(1)} GB` : `${Math.round(mb)} MB`);
const dayLabel = (d: string) => new Date(d.slice(0, 10) + "T00:00").toLocaleDateString("en-IN", { day: "numeric", month: "short" });

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
  const series = stats?.series ?? [];
  const tick = Math.max(1, Math.ceil(series.length / 7));

  const demand: Column[] = series.map((s) => ({
    key: s.day, label: dayLabel(s.day),
    tip: <>{dayLabel(s.day)}<br />Tickets <b>{s.tickets}</b> · answered by assistant <b>{s.answered}</b>{s.resolved ? <><br />Resolved {s.resolved}</> : null}</>,
    segments: [{ id: "tickets", value: s.tickets, tone: "signal" }, { id: "answered", value: s.answered, tone: "faint" }],
  }));
  const calls: Column[] = (runtime?.series ?? []).map((s) => ({
    key: String(s.Day), label: dayLabel(String(s.Day)),
    tip: <>{dayLabel(String(s.Day))}<br />Jev <b>{s.JevCalls}</b> · tools <b>{s.ToolCalls}</b> · model <b>{s.ModelCalls}</b></>,
    segments: [{ id: "jev", value: Number(s.JevCalls) || 0, tone: "signal" }, { id: "tool", value: Number(s.ToolCalls) || 0, tone: "mid" }, { id: "model", value: Number(s.ModelCalls) || 0, tone: "info" }],
  }));
  const tokens: Column[] = (runtime?.series ?? []).map((s) => ({
    key: String(s.Day), label: dayLabel(String(s.Day)), tip: <>{dayLabel(String(s.Day))} · <b>{compact(Number(s.Tokens) || 0)}</b> tokens</>,
    segments: [{ id: "tokens", value: Number(s.Tokens) || 0, tone: "signal" }],
  }));
  const runtimeTick = Math.max(1, Math.ceil(calls.length / 7));

  return (
    <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
      <div className="space-y-3 px-4 py-3 lg:px-6">
        <div className="flex flex-wrap items-center gap-3">
          <PageTitle icon={BarChart3} className="flex-1" title="Reports" meta={`Demand, outcomes, investigation timing, tool and model performance · last ${days} days`} />
          <Segmented label="Period" value={String(days)} onChange={(v) => setDays(Number(v))} options={RANGES.map((r) => ({ id: String(r), label: `${r} d` }))} />
        </div>

        <div className="grid grid-cols-2 gap-3 md:grid-cols-4">
          <Tile label="Tickets raised" value={t?.tickets} note={t ? `${t.open} open · ${t.resolved} resolved` : undefined} />
          <Tile label="Waiting on requester" value={t?.waiting} note="Support asked a question" />
          <Tile label="Median time to first reply" value={t?.medianFirstReplyHours == null ? (t ? "—" : undefined) : fmtHours(t.medianFirstReplyHours)} note="From L2" />
          <Tile label="Satisfaction" value={t ? (t.csat == null ? "—" : `${t.csat.toFixed(1)} / 5`) : undefined} note={t ? (t.ratings ? `${t.ratings} rating${t.ratings === 1 ? "" : "s"}` : "No ratings yet") : undefined} />
          <Tile label="Conversations" value={t?.conversations} note={deflection == null ? undefined : `${deflection}% answered without a ticket`} />
          <Tile label="Answers marked helpful" value={helpful == null ? (t ? "—" : undefined) : `${helpful}%`} note={t ? ((t.thumbsUp ?? 0) + (t.thumbsDown ?? 0) ? `${t.thumbsUp ?? 0} up · ${t.thumbsDown ?? 0} down` : "No feedback yet") : undefined} />
          <Tile label="Tickets raised from chat" value={t?.fromChat} note="Handed over by the assistant" />
          <Tile label="Assistant reply time" value={t?.avgLatencyMs == null ? (t ? "—" : undefined) : fmtMs(t.avgLatencyMs)} note="Average, end to end" />
        </div>

        <div className="grid gap-3 xl:grid-cols-12">
          <Panel icon={Layers} title="Demand per day" meta="Every request: became a ticket, or answered by the assistant" className="xl:col-span-8">
            {!stats ? <Skeleton className="h-56" /> : !series.length ? <Empty what="requests" /> : (
              <div className="space-y-4">
                <StackColumns columns={demand} label="Requests per day by how they were handled" height={170} tickEvery={tick} />
                <Legend inline rows={[
                  { label: "Became a ticket", value: series.reduce((n, s) => n + s.tickets, 0), tone: "signal" },
                  { label: "Answered by assistant", value: series.reduce((n, s) => n + s.answered, 0), tone: "faint" },
                ]} />
              </div>
            )}
          </Panel>
          <Panel icon={CalendarDays} title={days >= 30 ? "Demand calendar" : "Demand by weekday"} meta={days >= 30 ? "Requests per day · busiest day highlighted" : `Requests per weekday over the last ${days} days`} className="xl:col-span-4">
            {!stats ? <Skeleton className="h-56" /> : days >= 30
              ? <HeatCalendar days={series.map((s) => ({ day: s.day, value: s.tickets + s.answered }))} unit="request" />
              : <Weekdays series={series} />}
          </Panel>

          {(["byState", "byArea", "byType"] as const).map((k) => (
            <Panel key={k} icon={ListOrdered} title={{ byState: "Tickets by state", byArea: "Tickets by area", byType: "Tickets by type" }[k]} className="xl:col-span-4">
              {stats ? <Ranked rows={stats[k]} /> : <Skeleton className="h-40" />}
            </Panel>
          ))}
        </div>

        <div className="pt-3">
          <h2 className="text-title font-semibold tracking-tight">L2 runtime &amp; compute</h2>
          <p className="mt-0.5 text-sm text-muted-foreground">Investigation time, Jev, tool and model latency, and hardware and token use captured by Hermes.</p>
        </div>
        <div className="grid grid-cols-2 gap-3 md:grid-cols-4">
          <Tile label="L2 runs" value={rt?.Runs} note={rt ? `Average ${fmtSeconds(rt.AvgRunSeconds)} · longest ${fmtSeconds(rt.MaxRunSeconds)}` : undefined} />
          <Tile label="SQL reads per run" value={rt?.AvgSqlReadsPerRun == null ? (rt ? "—" : undefined) : rt.AvgSqlReadsPerRun.toFixed(1)} note="Average audited reads" />
          <Tile label="Jev latency" value={rt?.AvgJevMs == null ? (rt ? "—" : undefined) : fmtMs(rt.AvgJevMs)} note="Average decision" />
          <Tile label="Writer latency" value={rt?.AvgModelMs == null ? (rt ? "—" : undefined) : fmtMs(rt.AvgModelMs)} note={rt?.AvgModelMs == null ? "Model calls record no duration" : "Average model call"} />
          <Tile label="Tool latency" value={rt?.AvgToolMs == null ? (rt ? "—" : undefined) : fmtMs(rt.AvgToolMs)} note={rt ? `${rt.ToolErrors ?? 0} failed tool calls` : undefined} />
          <Tile label="Model tokens" value={rt?.TotalTokens == null ? (rt ? "—" : undefined) : compact(rt.TotalTokens)} note={rt ? `${rt.ModelErrors} failed model calls` : undefined} />
          <Tile label="GPU utilisation" value={rt?.AvgGpuUtilPct == null ? (rt ? "—" : undefined) : `${rt.AvgGpuUtilPct.toFixed(0)}%`} note={rt?.PeakGpuVramMb == null ? "No GPU sample" : `Peak VRAM ${vram(rt.PeakGpuVramMb)}`} />
          <Tile label="CPU utilisation" value={rt?.AvgCpuUtilPct == null ? (rt ? "—" : undefined) : `${rt.AvgCpuUtilPct.toFixed(0)}%`} note="Average of compute samples" />
        </div>

        <div className="grid gap-3 xl:grid-cols-12">
          <Panel icon={PhoneCall} title="Observed calls per day" meta="Jev decisions, tool calls and model calls" className="xl:col-span-6">
            {!stats ? <Skeleton className="h-56" /> : !runtime ? <TelemetryUnavailable /> : !calls.length ? <Empty what="calls" /> : (
              <div className="space-y-4">
                <StackColumns columns={calls} label="Observed calls per day by kind" height={150} tickEvery={runtimeTick} />
                <Legend inline rows={[
                  { label: "Jev", value: calls.reduce((n, c) => n + c.segments[0].value, 0), tone: "signal" },
                  { label: "Tools", value: calls.reduce((n, c) => n + c.segments[1].value, 0), tone: "mid" },
                  { label: "Model", value: calls.reduce((n, c) => n + c.segments[2].value, 0), tone: "info" },
                ]} />
              </div>
            )}
          </Panel>
          <Panel icon={Cpu} title="Model tokens per day" meta={rt?.TotalTokens != null ? `${compact(rt.TotalTokens)} tokens in the period` : "Prompt and completion tokens"} className="xl:col-span-6">
            {!stats ? <Skeleton className="h-56" /> : !runtime ? <TelemetryUnavailable /> : !tokens.length ? <Empty what="tokens" /> : (
              <StackColumns columns={tokens} label="Model tokens per day" height={150} tickEvery={runtimeTick} />
            )}
          </Panel>

          <Panel icon={Timer} title="Slowest tools" meta="Average time per call, slowest first" className="xl:col-span-7">
            {!stats ? <Skeleton className="h-48" /> : !runtime ? <TelemetryUnavailable /> : (
              <LatencyTable rows={[...runtime.tools].sort((a, b) => (b.AvgMs ?? 0) - (a.AvgMs ?? 0)).map((x) => ({ label: x.Label, calls: x.Calls, errors: x.Errors, avg: x.AvgMs }))} />
            )}
          </Panel>
          <Panel icon={Cpu} title="Writer models" meta="Local model calls and tokens" className="xl:col-span-5">
            {!stats ? <Skeleton className="h-48" /> : !runtime ? <TelemetryUnavailable /> : (
              <LatencyTable rows={runtime.models.map((x) => ({ label: `${x.Model}`, sub: x.Provider, calls: x.Calls, errors: 0, avg: x.AvgMs, extra: x.Tokens == null ? undefined : `${compact(x.Tokens)} tokens` }))} />
            )}
          </Panel>
        </div>

        {stats && series.length > 0 && (
          <details className="rounded-xl border bg-surface">
            <summary className="cursor-pointer px-4 py-3 text-sm font-medium">Daily numbers as a table</summary>
            <div className="overflow-x-auto border-t">
              <table className="w-full text-meta">
                <thead className="bg-surface-2 text-left text-xs text-subtle-foreground">
                  <tr>{["Day", "Tickets", "Resolved", "Conversations", "Answered without ticket"].map((h, i) => <th key={h} className={cn("px-4 py-2 font-medium", i && "text-right")}>{h}</th>)}</tr>
                </thead>
                <tbody className="divide-y font-mono text-xs tabular-nums">
                  {[...series].reverse().map((s) => (
                    <tr key={s.day}>
                      <td className="px-4 py-2 font-sans text-meta">{dayLabel(s.day)}</td>
                      <td className="px-4 py-2 text-right">{s.tickets}</td>
                      <td className="px-4 py-2 text-right">{s.resolved}</td>
                      <td className="px-4 py-2 text-right">{s.conversations}</td>
                      <td className="px-4 py-2 text-right">{s.answered}</td>
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

function Tile({ label, value, note }: { label: string; value?: number | string; note?: string }) {
  return (
    <div className="min-w-0 rounded-2xl border bg-canvas p-1.5">
      <p className="truncate px-2.5 pb-2 pt-1 text-xs text-subtle-foreground">{label}</p>
      <div className="rounded-xl border bg-surface px-3 py-3">
        {value === undefined ? <Skeleton className="h-8 w-16" /> : <p className="font-mono text-2xl font-medium tracking-tight">{value}</p>}
        {note && <p className="mt-1 truncate text-xs text-subtle-foreground" title={note}>{note}</p>}
      </div>
    </div>
  );
}

function Weekdays({ series }: { series: Stats["series"] }) {
  const totals = WEEKDAYS.map((_, i) => series.filter((s) => (new Date(s.day.slice(0, 10) + "T00:00").getDay() + 6) % 7 === i).reduce((n, s) => n + s.tickets + s.answered, 0));
  const max = Math.max(1, ...totals);
  const busiest = totals.indexOf(Math.max(...totals));
  return (
    <ul className="space-y-2.5">
      {WEEKDAYS.map((d, i) => (
        <li key={d} className="flex items-center gap-3 text-xs">
          <span className={cn("w-8 shrink-0", i === busiest && totals[i] ? "font-medium text-foreground" : "text-muted-foreground")}>{d}</span>
          <VolumeBar className="min-w-0 flex-1" share={totals[i] / max} label={`${d}: ${totals[i]} requests`} segments={[{ label: "requests", value: totals[i], tone: i === busiest && totals[i] ? "signal" : "faint" }]} />
          <span className="w-8 shrink-0 text-right font-mono tabular-nums">{totals[i]}</span>
        </li>
      ))}
    </ul>
  );
}

function Empty({ what }: { what: string }) {
  return <p className="py-10 text-center text-sm text-muted-foreground">No {what} in this period.</p>;
}

function TelemetryUnavailable() {
  return <p className="py-10 text-center text-sm text-muted-foreground">Runtime telemetry will appear after the updated L1 API is running.</p>;
}

function LatencyTable({ rows }: { rows: { label: string; sub?: string; calls: number; errors: number; avg: number | null; extra?: string }[] }) {
  if (!rows.length) return <p className="text-sm text-muted-foreground">No runtime telemetry in this period.</p>;
  const max = Math.max(1, ...rows.map((r) => r.avg ?? 0));
  return (
    <div className="overflow-x-auto">
      <table className="w-full text-meta">
        <thead className="text-left text-xs text-subtle-foreground">
          <tr className="border-b">
            <th className="py-2 pr-3 font-medium">Operation</th>
            <th className="hidden w-2/5 px-2 py-2 font-medium sm:table-cell">Average time</th>
            <th className="px-2 py-2 text-right font-medium">Calls</th>
            <th className="px-2 py-2 text-right font-medium">Failed</th>
            <th className="py-2 pl-2 text-right font-medium">Avg</th>
          </tr>
        </thead>
        <tbody className="divide-y">
          {rows.map((r) => (
            <tr key={r.label}>
              <td className="py-2 pr-3">
                <p className="truncate font-mono text-xs">{r.label}</p>
                {(r.sub || r.extra) && <p className="text-2xs text-subtle-foreground">{[r.sub, r.extra].filter(Boolean).join(" · ")}</p>}
              </td>
              <td className="hidden px-2 py-2 sm:table-cell">
                <VolumeBar share={(r.avg ?? 0) / max} label={`${r.label}: average ${r.avg == null ? "unknown" : fmtMs(r.avg)}`} segments={[{ label: "average", value: 1, tone: r.errors / Math.max(1, r.calls) > 0.1 ? "danger" : "signal" }]} />
              </td>
              <td className="px-2 py-2 text-right font-mono text-xs tabular-nums">{r.calls}</td>
              <td className={cn("px-2 py-2 text-right font-mono text-xs tabular-nums", r.errors > 0 ? "text-destructive" : "text-subtle-foreground")}>{r.errors}</td>
              <td className="whitespace-nowrap py-2 pl-2 text-right font-mono text-xs tabular-nums">{r.avg == null ? "—" : fmtMs(r.avg)}</td>
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
        <li key={r.label} className="text-xs">
          <div className="mb-1 flex justify-between gap-2">
            <span className="truncate text-muted-foreground">{r.label}</span>
            <span className="font-mono tabular-nums">{r.count}</span>
          </div>
          <VolumeBar share={r.count / max} label={`${r.label}: ${r.count}`} segments={[{ label: r.label, value: 1, tone: "signal" }]} />
        </li>
      ))}
    </ul>
  );
}
