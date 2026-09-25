"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { CirclePause, FileJson2, Radio, RefreshCw } from "lucide-react";
import { toast } from "sonner";
import { ops, type RuntimeLogRecord, type RuntimeLogs } from "@/lib/api";
import { cn } from "@/lib/utils";
import { PageTitle } from "@/components/ui/viz";
import { Button } from "@/components/ui/button";
import { Empty, Skeleton, Switch, Tag } from "@/components/ui/primitives";
import { Json } from "./live";
import { InspectorBlock } from "./inspect";

const stamp = (r: RuntimeLogRecord) => {
  const d = r.data ?? {};
  return String(d.event_on_ist ?? d.ts ?? d.event_on ?? "");
};

type D = Record<string, unknown>;
const str = (v: unknown) => (v == null ? "" : typeof v === "string" ? v : JSON.stringify(v));
const time = (ts: string) => (ts.match(/T(\d\d:\d\d:\d\d(\.\d{1,3})?)/)?.[1] ?? ts);
const dur = (ms: number) => (ms < 1000 ? `${Math.round(ms)} ms` : ms < 60_000 ? `${(ms / 1000).toFixed(1)} s` : `${(ms / 60_000).toFixed(1)} min`);

// What one line says, in words: call traces merge call+return; observer events get a one-line summary.
type Line = { key: string; source: string; at: string; depth: number; what: string; detail: string; ms: number | null; failed: boolean; record: RuntimeLogRecord; pending?: boolean };

function summarise(d: D): string {
  const r = (d.result ?? {}) as D;
  if (d.event_type === "lmstudio_sample") return r.error ? `model server: ${str(r.error)}` : `model server ${Math.round(Number(r.latency_s ?? 0) * 1000)} ms · ${(r.models as unknown[] | undefined)?.length ?? 0} models`;
  if (d.event_type === "compute_sample") return r.error ? `compute: ${str(r.error)}` : `gpu ${str(r.gpu_util_pct ?? "—")}% · cpu ${str(r.cpu_util_pct ?? "—")}%`;
  if (d.event_type === "world_walk") return `route ${str(r.route)} · ${str(r.stopped).replace(/_/g, " ")} · ${(r.survey as unknown[] | undefined)?.length ?? 0} records`;
  if (d.error || d.error_message) return str(d.error ?? d.error_message);
  return [d.tool_name, d.status].filter(Boolean).map(str).join(" · ");
}

function toLines(source: string, records: RuntimeLogRecord[]): Line[] {
  const out: Line[] = [];
  const open = new Map<string, number>();
  records.forEach((record, i) => {
    const d = (record.data ?? {}) as D;
    const at = String(d.event_on_ist ?? d.ts ?? d.event_on ?? "");
    if (d.event === "call" || d.event === "return") {
      const id = `${str(d.pid)}:${str(d.thread)}:${str(d.fn)}:${str(d.depth)}`;
      if (d.event === "return" && open.has(id)) {
        const line = out[open.get(id)!];
        Object.assign(line, { ms: Number(d.ms ?? 0), pending: false, record, detail: `${str(d.at)} → ${str(d.value) || "None"}`, failed: !!d.exception });
        open.delete(id);
        return;
      }
      open.set(id, out.length);
      out.push({ key: `${source}:${i}`, source, at, depth: Number(d.depth ?? 1), what: `${str(d.fn)}()`, detail: str(d.at), ms: d.event === "return" ? Number(d.ms ?? 0) : null, failed: false, record, pending: d.event === "call" });
      return;
    }
    const failed = String(d.status ?? "") === "error" || !!d.error || !!d.error_message || !!(d.result as D | undefined)?.error;
    out.push({
      key: `${source}:${i}`, source, at, depth: 1,
      what: str(d.event_type ?? d.tool_name ?? "event").replace(/_/g, " "),
      detail: [summarise(d), d.profile_name && str(d.profile_name), d.run_id && `run ${str(d.run_id).slice(0, 8)}`].filter(Boolean).join(" · "),
      ms: d.duration_ms != null ? Number(d.duration_ms) : null, failed, record,
    });
  });
  return out;
}

export function LogsView() {
  const [data, setData] = useState<RuntimeLogs | null>(null);
  const [source, setSource] = useState("All");
  const [follow, setFollow] = useState(true);
  const [open, setOpen] = useState<string | null>(null);
  const end = useRef<HTMLDivElement>(null);

  const load = useCallback(async () => {
    try { setData(await ops.logs()); }
    catch (e) { toast.error((e as Error).message); }
  }, []);

  useEffect(() => {
    const initial = setTimeout(load, 0);
    if (!follow) return () => clearTimeout(initial);
    const id = setInterval(load, 2500);
    return () => {
      clearTimeout(initial);
      clearInterval(id);
    };
  }, [follow, load]);

  const rows = useMemo(() => (data?.sources ?? [])
    .filter((src) => source === "All" || src.name === source)
    .flatMap((src) => toLines(src.name, src.records))
    .sort((x, y) => x.at.localeCompare(y.at)), [data, source]);

  useEffect(() => {
    if (follow) end.current?.scrollIntoView({ block: "end" });
  }, [rows.length, follow]);

  return (
    <div className="flex min-h-0 flex-1 flex-col">
      <header className="shrink-0 border-b bg-canvas px-4 py-3 lg:px-6">
        <div className="flex flex-wrap items-center gap-3">
          <PageTitle icon={FileJson2} className="flex-1" title="Runtime logs" meta="read-only tail of the JSONL observability written inside WSL" />
          <label className="flex items-center gap-2 text-meta text-muted-foreground">
            <Switch checked={follow} onCheckedChange={setFollow} aria-label="Follow runtime logs" />
            {follow ? <><Radio className="size-3 text-signal" /> Follow live</> : <><CirclePause className="size-3" /> Paused</>}
          </label>
          <Button variant="outline" size="sm" onClick={load}><RefreshCw /> Refresh</Button>
        </div>
        <div className="mt-3 flex flex-wrap gap-2">
          {["All", ...(data?.sources.map((s) => s.name) ?? [])].map((name) => (
            <button key={name} onClick={() => setSource(name)} className={cn("rounded-md border px-2.5 py-1 text-xs text-muted-foreground", source === name && "border-signal/40 bg-signal-soft text-signal")}>
              {name}
            </button>
          ))}
          {data?.sources.map((s) => <Tag key={s.name} variant={s.available ? "default" : "error"}>{s.name} · {s.available ? `${s.records.length} tailed` : "unavailable"}</Tag>)}
        </div>
      </header>

      <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto bg-background p-3 lg:p-4">
        {!data && <div className="space-y-2"><Skeleton className="h-16" /><Skeleton className="h-16" /><Skeleton className="h-16" /></div>}
        {data && !rows.length && <Empty icon={<FileJson2 className="size-5" />} title="No log records">The selected JSONL source is empty or unavailable.</Empty>}
        <ol className="mx-auto max-w-6xl overflow-hidden rounded-xl border bg-canvas font-mono text-xs">
          {rows.map((l) => {
            const isOpen = open === l.key;
            const slow = (l.ms ?? 0) >= 5000;
            return (
              <li key={l.key} className="border-b last:border-b-0">
                <button onClick={() => setOpen(isOpen ? null : l.key)} aria-expanded={isOpen}
                  className={cn("flex w-full items-baseline gap-3 px-3 py-1.5 text-left hover:bg-surface-2", l.failed && "bg-destructive-soft/40")}>
                  <span className="w-24 shrink-0 tabular-nums text-subtle-foreground">{time(l.at) || "—"}</span>
                  <span className={cn("size-1.5 shrink-0 self-center rounded-full", l.failed ? "bg-destructive" : l.source === "Observer events" ? "bg-signal" : "bg-border-strong")} aria-hidden />
                  <span className="min-w-0 flex-1 truncate">
                    <span className="text-subtle-foreground">{"  ".repeat(Math.max(0, l.depth - 1))}</span>
                    <span className={cn("text-foreground", l.failed && "text-destructive")}>{l.what}</span>
                    {l.detail && <span className="text-muted-foreground">  {l.detail}</span>}
                  </span>
                  <span className={cn("w-20 shrink-0 text-right tabular-nums", l.pending ? "text-signal" : slow ? "text-warning" : "text-subtle-foreground")}>
                    {l.pending ? "running" : l.ms != null ? dur(l.ms) : ""}
                  </span>
                </button>
                {isOpen && (
                  <div className="space-y-3 border-t bg-surface p-3 font-sans">
                    {l.record.data ? <Json label="Record" text={JSON.stringify(l.record.data)} /> : <InspectorBlock label="Raw line" text={l.record.raw} />}
                  </div>
                )}
              </li>
            );
          })}
          <div ref={end} />
        </ol>
      </div>
      <div className="sr-only" aria-live="polite">{follow ? "Following runtime logs" : "Runtime log following paused"}</div>
    </div>
  );
}
