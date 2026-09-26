"use client";

import { useCallback, useEffect, useState } from "react";
import { Activity, AlertTriangle, CheckCircle2, Clock3, Cpu, Gauge, HeartPulse, ListChecks, RefreshCw, ShieldCheck, Wrench } from "lucide-react";
import { ops, type Performance, type Probe, type RuntimeStatus } from "@/lib/api";
import { ago, human, outcomeLabel, ticketLabel, whenShort } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/primitives";
import { PromptBar, VolumeBar } from "@/components/ui/charts";
import { Attributes, Headline, Legend, outcomeTone, PageTitle, Panel, SegmentBar, Segmented, SlotMeter, Stat, TickGauge } from "@/components/ui/viz";

// Pipeline health: the L2 runtime's own `status` plus the benchmark report (Model_Bench/benchmark_l2_performance.py).
// Nothing here is computed in the browser beyond arranging what those two already say.

const WINDOWS = [{ id: "2", label: "2 h" }, { id: "6", label: "6 h" }, { id: "24", label: "24 h" }, { id: "168", label: "7 d" }] as const;
type Window = (typeof WINDOWS)[number]["id"];

export function HealthView({ onOpenRun }: { onOpenRun: (id: string) => void }) {
  const [hours, setHours] = useState<Window>("24");
  const [status, setStatus] = useState<Probe<RuntimeStatus> | null>(null);
  const [perf, setPerf] = useState<Probe<Performance> | null>(null);
  const [busy, setBusy] = useState(false);

  const load = useCallback(async () => {
    setBusy(true);
    const fail = (e: Error) => ({ at: new Date().toISOString(), ok: false, error: e.message, data: null });
    // Independent: the report (SQL, ~4 s) must not wait for the runtime status (WSL, can be slower).
    await Promise.all([
      ops.status().catch(fail).then((s) => setStatus(s as Probe<RuntimeStatus>)),
      ops.performance(Number(hours)).catch(fail).then((p) => setPerf(p as Probe<Performance>)),
    ]);
    setBusy(false);
  }, [hours]);

  useEffect(() => {
    const first = setTimeout(load, 0);
    const poll = setInterval(load, 60_000);
    return () => { clearTimeout(first); clearInterval(poll); };
  }, [load]);

  const s = status?.data;
  const p = perf?.data;
  const invariants = Object.entries(p?.invariants ?? {});
  const broken = invariants.filter(([, n]) => n > 0);
  const tools = [...(p?.tool_health.per_tool ?? [])].sort((a, b) => b.Failed / Math.max(1, b.Calls) - a.Failed / Math.max(1, a.Calls) || b.Calls - a.Calls);
  const toolCalls = tools.reduce((n, t) => n + t.Calls, 0);
  const toolFailed = tools.reduce((n, t) => n + t.Failed, 0);
  const types = Object.entries(p?.outcomes.response_types ?? {}).sort((a, b) => b[1] - a[1]);
  const failing = (p?.expectations.rows ?? []).filter((r) => r.Pass === false);
  const maxToolCalls = Math.max(1, ...tools.map((t) => t.Calls));
  // One scale for every profile's prompt bar, with room past the spill limit.
  const promptScale = p ? Math.max(p.spill_threshold_chars, ...p.model_input.map((m) => m.MaxPrompt)) * 1.08 : 1;

  return (
    <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto">
      <div className="space-y-3 px-4 py-3 lg:px-6">
        <div className="flex flex-wrap items-center gap-3">
          <PageTitle icon={HeartPulse} className="flex-1" title="Pipeline health" meta={`Runtime status and performance report${p ? ` · since ${whenShort(p.window_since)}` : ""}`} />
          <Segmented label="Window" value={hours} onChange={setHours} options={WINDOWS.map((w) => ({ id: w.id, label: w.label }))} />
          <Button size="sm" variant="ghost" onClick={load} disabled={busy} aria-label="Refresh"><RefreshCw className={cn(busy && "animate-spin")} /></Button>
        </div>

        <div className="grid gap-3 xl:grid-cols-12">
          <Panel icon={Cpu} className="xl:col-span-4" title="Runtime" meta={status ? `l2_pipeline_runtime status · ${ago(status.at)}` : "asking the runtime"}>
            {!status ? <Waiting what="Asking the runtime in WSL" /> : !s ? <Failure what="The runtime status" error={status.error} /> : (
              <div className="space-y-4">
                <p className={cn("flex items-center gap-2 text-sm font-medium", s.binding_ready_for_new_claims ? "text-signal" : "text-warning")}>
                  <span className={cn("size-2 rounded-full", s.binding_ready_for_new_claims ? "bg-signal" : "bg-warning")} aria-hidden />
                  {s.binding_ready_for_new_claims ? "Ready to claim new tickets" : `Claims blocked · ${s.binding_block_reason ?? "unknown reason"}`}
                </p>
                <div className="space-y-2.5">
                  <SlotMeter label="Pipeline runs" used={s.active_runs.length} max={s.contract.max_pipeline_wip} />
                  <SlotMeter label="Local model running" used={s.local_model.running} max={s.contract.max_qwen_running} />
                  <SlotMeter label="Local model queue" used={s.local_model.queued} max={s.contract.max_qwen_waiting} tone="warn" />
                </div>
                <Legend rows={[
                  { label: "Anomalies", value: s.anomalies.length, tone: s.anomalies.length ? "danger" : "faint" },
                  { label: "Runs on the board", value: Object.keys(s.tasks_by_run).length, tone: "faint" },
                  { label: "Review cycles allowed", value: s.contract.max_review_cycles, tone: "faint" },
                ]} />
              </div>
            )}
          </Panel>

          <Panel icon={Clock3} className="xl:col-span-4" title="Claims" meta="Is the engineer picking up work">
            {!perf ? <Waiting what="Running the performance report" /> : !p ? <Failure what="The performance report" error={perf.error} /> : (
              <div className="space-y-3">
                <Headline value={p.claim_health.MinutesSinceClaim == null ? "—" : fmtMinutes(p.claim_health.MinutesSinceClaim)} unit="since last claim"
                  note={p.claim_health.Stalled ? "stalled" : "not stalled"} noteTone={p.claim_health.Stalled ? "danger" : "signal"} />
                <div className="grid grid-cols-2 gap-3">
                  <Stat label="Waiting" value={p.claim_health.Waiting} tone={p.claim_health.Waiting ? "warn" : undefined} />
                  <Stat label="Being worked" value={p.claim_health.Active} tone={p.claim_health.Active ? "signal" : undefined} />
                </div>
                <p className="border-t pt-3 text-xs text-subtle-foreground">Stalled means tickets are waiting and nothing has been claimed for too long. The scout claims within two minutes when a slot is free.</p>
              </div>
            )}
          </Panel>

          <Panel icon={ShieldCheck} className="xl:col-span-4" title="Lifecycle invariants" meta="Each must be 0">
            {!p ? <Waiting what="Waiting for the performance report" /> : (
              <div className="space-y-3">
                <Headline value={`${invariants.length - broken.length}/${invariants.length}`} unit="hold" note={broken.length ? `${broken.length} broken` : "all clear"} noteTone={broken.length ? "danger" : "signal"} />
                <ul className="space-y-1">
                  {invariants.sort((a, b) => b[1] - a[1]).map(([name, n]) => (
                    <li key={name} className="flex items-start gap-2 text-xs">
                      {n ? <AlertTriangle className="mt-0.5 size-3.5 shrink-0 text-destructive" aria-hidden /> : <CheckCircle2 className="mt-0.5 size-3.5 shrink-0 text-signal" aria-hidden />}
                      <span className={cn("min-w-0 flex-1", n ? "text-foreground" : "text-muted-foreground")}>{name}</span>
                      <span className={cn("font-mono tabular-nums", n ? "text-destructive" : "text-subtle-foreground")}>{n}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </Panel>

          <Panel icon={Activity} title="Outcomes" meta={p ? `${p.outcomes.runs} runs in the window` : "Loading"} className="xl:col-span-8">
            {!p ? <Skeleton className="h-40" /> : (
              <div className="space-y-4">
                <Headline value={`${p.outcomes.published}/${p.outcomes.runs}`} unit="published"
                  note={p.outcomes.avg_claim_to_publish_min != null ? `avg ${p.outcomes.avg_claim_to_publish_min} min claim → publish` : undefined} />
                <SegmentBar label="Replies by type" segments={types.map(([k, n]) => ({ label: outcomeLabel(k), value: n, tone: outcomeTone(k) }))} />
                <Legend inline rows={types.map(([k, n]) => ({ label: outcomeLabel(k), value: n, tone: outcomeTone(k) }))} />
                <div className="grid grid-cols-2 gap-4 border-t pt-3 sm:grid-cols-4">
                  <Stat label="Answered without the model" value={p.outcomes.answered_without_qwen} tone="signal" />
                  <Stat label="Their avg time" value={p.outcomes.avg_no_qwen_seconds != null ? `${p.outcomes.avg_no_qwen_seconds} s` : "—"} />
                  <Stat label="Failed runs" value={p.outcomes.failed} tone={p.outcomes.failed ? "danger" : undefined} />
                  <Stat label="Canned 'incomplete' replies" value={p.outcomes.canned_incomplete_replies} tone={p.outcomes.canned_incomplete_replies ? "warn" : undefined} />
                </div>
              </div>
            )}
          </Panel>

          <Panel icon={ListChecks} className="xl:col-span-4" title="Expected answers" meta={p ? `${p.expectations.scored} scored against known cases` : "Loading"}>
            {!p ? <Skeleton className="h-40" /> : p.expectations.scored ? (
              <TickGauge label="Expected answers met" value={p.expectations.passed / p.expectations.scored}
                center={`${Math.round((p.expectations.passed / p.expectations.scored) * 100)}%`}
                caption={`${p.expectations.passed} of ${p.expectations.scored} met${p.expectations.pending ? ` · ${p.expectations.pending} pending` : ""}`} />
            ) : <p className="text-sm text-muted-foreground">No runs matched a known case in this window.</p>}
          </Panel>
          <Panel icon={Wrench} title="Tool health" meta={p ? `${toolCalls} calls · ${toolFailed} failed · worst failure rate first` : "Loading"} className="xl:col-span-8">
            {!p ? <Skeleton className="h-60" /> : (
              <div className="space-y-4">
                <ul className="space-y-2">
                  {tools.slice(0, 10).map((t) => {
                    const rate = t.Failed / Math.max(1, t.Calls);
                    return (
                      <li key={t.ToolName} className="flex items-center gap-3 text-xs">
                        <span className="w-40 shrink-0 truncate font-mono" title={t.ToolName}>{t.ToolName.replace(/^xstudio_/, "")}</span>
                        <VolumeBar className="min-w-0 flex-1" share={t.Calls / maxToolCalls} label={`${t.ToolName}: ${t.Failed} failed of ${t.Calls} calls`}
                          segments={[{ label: "failed", value: t.Failed, tone: "danger" }, { label: "ok", value: t.Calls - t.Failed, tone: "faint" }]} />
                        <span className={cn("w-14 shrink-0 text-right font-mono tabular-nums", rate > 0.1 ? "text-destructive" : "text-subtle-foreground")}>{t.Failed}<span className="text-subtle-foreground">/{t.Calls}</span></span>
                      </li>
                    );
                  })}
                </ul>
                {p.tool_health.top_failure_causes.length > 0 && (
                  <div className="border-t pt-3">
                    <p className="pb-2 text-xs text-subtle-foreground">Top failure causes</p>
                    <ul className="space-y-1.5">
                      {p.tool_health.top_failure_causes.slice(0, 5).map((c, i) => (
                        <li key={i} className="flex gap-3 text-xs"><span className="w-6 shrink-0 text-right font-mono tabular-nums text-destructive">{c.count ?? c.n}</span><span className="line-clamp-2 min-w-0 break-all font-mono text-muted-foreground" title={c.cause}>{c.cause}</span></li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            )}
          </Panel>

          <Panel icon={Gauge} className="xl:col-span-4" title="Model load" meta={p ? `Prompt size against the ${Math.round(p.spill_threshold_chars / 1000)}k-character spill limit` : "Loading"}>
            {!p ? <Skeleton className="h-60" /> : (
              <div className="space-y-4">
                {p.model_input.map((m) => (
                  <div key={m.ProfileName}>
                    <p className="mb-1.5 flex justify-between text-xs"><span className="font-mono">{m.ProfileName.replace(/^l2-/, "")}</span><span className="text-subtle-foreground">{m.Sessions} sessions · {m.Requests} calls</span></p>
                    <PromptBar avg={m.AvgPrompt} max={m.MaxPrompt} limit={p.spill_threshold_chars} scale={promptScale} label={m.ProfileName} format={k} />
                    <p className="mt-1 text-2xs text-subtle-foreground">avg <span className="font-mono">{k(m.AvgPrompt)}</span> · max <span className={cn("font-mono", m.MaxPrompt > p.spill_threshold_chars && "text-destructive")}>{k(m.MaxPrompt)}</span> characters{m.MaxPrompt > p.spill_threshold_chars ? " · over the limit" : ""}</p>
                  </div>
                ))}
                <Attributes rows={[
                  ...Object.entries(p.waste).map(([name, n]) => ({ k: human(name.replace(/([a-z])([A-Z])/g, "$1_$2")), v: n, tone: n && name !== "Sessions" ? "warn" as const : undefined })),
                  { k: "Jev approvals", v: p.jev_review_gates.jev_approvals },
                  ...Object.entries(p.jev_review_gates.blocked_by_gate).map(([g, n]) => ({ k: `Blocked · ${g.replace(/_/g, " ")}`, v: n })),
                ]} />
              </div>
            )}
          </Panel>

        {failing.length > 0 && (
          <Panel icon={AlertTriangle} className="xl:col-span-12" title="Answers that missed the expected outcome" meta={`${failing.length} of ${p?.expectations.scored ?? 0} scored`} pad="none">
            <ul className="divide-y">
              {failing.map((r, i) => {
                const run = p?.runs?.find((x) => x.TicketNo === r.TicketNo);
                return (
                  <li key={`${r.TicketNo}-${i}`}>
                    <button disabled={!run} onClick={() => run && onOpenRun(run.RunID)} className="flex w-full flex-wrap items-center gap-x-4 gap-y-1 px-4 py-3 text-left enabled:hover:bg-surface-2">
                      <span className="w-12 font-mono text-xs">{ticketLabel(r.TicketNo)}</span>
                      <span className="min-w-0 flex-1 truncate font-mono text-xs text-muted-foreground">{r.Case}</span>
                      <span className="text-xs"><span className="text-subtle-foreground">Got </span>{outcomeLabel(r.ResponseType)}</span>
                      <span className="text-xs"><span className="text-subtle-foreground">wanted </span><span className="text-warning">{r.Expected}</span></span>
                    </button>
                  </li>
                );
              })}
            </ul>
          </Panel>
        )}
        </div>
      </div>
    </div>
  );
}

function Failure({ what, error }: { what: string; error: string | null }) {
  return (
    <div className="rounded-lg bg-destructive-soft p-3 text-xs text-destructive">
      <p className="font-medium">{what} could not be read.</p>
      {error && <p className="mt-1 break-words font-mono">{error}</p>}
    </div>
  );
}

const k = (n: number) => `${(n / 1000).toFixed(1)}k`;
const fmtMinutes = (m: number) => (m < 60 ? `${Math.round(m)} min` : m < 2880 ? `${(m / 60).toFixed(1)} h` : `${(m / 1440).toFixed(1)} d`);

function Waiting({ what }: { what: string }) {
  return (
    <div className="flex items-center gap-3 py-2 text-xs text-muted-foreground" role="status">
      <RefreshCw className="size-4 shrink-0 animate-spin text-subtle-foreground" aria-hidden />
      <span>{what}… this can take a few seconds.</span>
    </div>
  );
}
