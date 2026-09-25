"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { CirclePause, FileJson2, Radio, RefreshCw } from "lucide-react";
import { toast } from "sonner";
import { ops, type RuntimeLogRecord, type RuntimeLogs } from "@/lib/api";
import { ago } from "@/lib/format";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Empty, Skeleton, Switch, Tag } from "@/components/ui/primitives";
import { Json } from "./live";
import { InspectorBlock } from "./inspect";

const stamp = (r: RuntimeLogRecord) => {
  const d = r.data ?? {};
  return String(d.event_on_ist ?? d.ts ?? d.event_on ?? "");
};

const title = (r: RuntimeLogRecord) => {
  const d = r.data ?? {};
  return String(d.event_type ?? d.event ?? d.fn ?? d.tool_name ?? "record");
};

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
    load();
    if (!follow) return;
    const id = setInterval(load, 2500);
    return () => clearInterval(id);
  }, [follow, load]);

  const rows = useMemo(() => {
    const items = (data?.sources ?? []).flatMap((s) => s.records.map((record, index) => ({ source: s.name, record, key: `${s.name}:${stamp(record)}:${index}` })));
    return items
      .filter((x) => source === "All" || x.source === source)
      .sort((a, b) => stamp(a.record).localeCompare(stamp(b.record)));
  }, [data, source]);

  useEffect(() => {
    if (follow) end.current?.scrollIntoView({ block: "end" });
  }, [rows.length, follow]);

  return (
    <div className="flex min-h-0 flex-1 flex-col">
      <header className="shrink-0 border-b bg-surface px-4 py-3 lg:px-6">
        <div className="flex flex-wrap items-center gap-3">
          <div className="min-w-0 flex-1">
            <h1 className="text-title font-semibold tracking-tight">Runtime logs</h1>
            <p className="text-2xs text-subtle-foreground">Read-only tail of Chitragupta JSONL observability written inside WSL.</p>
          </div>
          <label className="flex items-center gap-2 text-meta text-muted-foreground">
            <Switch checked={follow} onCheckedChange={setFollow} aria-label="Follow runtime logs" />
            {follow ? <><Radio className="size-3 text-destructive" /> Follow live</> : <><CirclePause className="size-3" /> Paused</>}
          </label>
          <Button variant="outline" size="sm" onClick={load}><RefreshCw /> Refresh</Button>
        </div>
        <div className="mt-3 flex flex-wrap gap-2">
          {["All", ...(data?.sources.map((s) => s.name) ?? [])].map((name) => (
            <button key={name} onClick={() => setSource(name)} className={cn("rounded-md border px-2.5 py-1 text-xs text-muted-foreground", source === name && "border-primary/40 bg-primary-soft text-primary-soft-foreground")}>
              {name}
            </button>
          ))}
          {data?.sources.map((s) => <Tag key={s.name} className={!s.available ? "text-destructive" : undefined}>{s.name} · {s.available ? `${s.records.length} tailed` : "unavailable"}</Tag>)}
        </div>
      </header>

      <div className="scrollbar-thin min-h-0 flex-1 overflow-y-auto bg-background p-3 lg:p-4">
        {!data && <div className="space-y-2"><Skeleton className="h-16" /><Skeleton className="h-16" /><Skeleton className="h-16" /></div>}
        {data && !rows.length && <Empty icon={<FileJson2 className="size-5" />} title="No log records">The selected JSONL source is empty or unavailable.</Empty>}
        <ol className="mx-auto max-w-6xl space-y-1.5">
          {rows.map(({ source: sourceName, record, key }) => {
            const isOpen = open === key;
            const d = record.data ?? {};
            const failed = String(d.status ?? "") === "error" || !!d.error || !!d.error_message;
            return (
              <li key={key} className="overflow-hidden rounded-lg border bg-surface">
                <button onClick={() => setOpen(isOpen ? null : key)} className="flex w-full items-center gap-3 px-3 py-2.5 text-left hover:bg-surface-2" aria-expanded={isOpen}>
                  <span className={cn("size-2 shrink-0 rounded-full", failed ? "bg-destructive" : sourceName === "Observer events" ? "bg-primary" : "bg-border-strong")} aria-hidden />
                  <span className="w-28 shrink-0 text-2xs text-subtle-foreground">{sourceName}</span>
                  <span className="min-w-0 flex-1 truncate text-meta font-medium">{title(record)}</span>
                  {d.tool_name != null && <span className="hidden max-w-48 truncate font-mono text-2xs text-muted-foreground md:block">{String(d.tool_name)}</span>}
                  <span className="shrink-0 text-2xs text-subtle-foreground">{stamp(record) ? ago(stamp(record)) : "—"}</span>
                </button>
                {isOpen && (
                  <div className="space-y-3 border-t bg-surface-2 p-3">
                    {record.data ? <Json label="Structured record" text={JSON.stringify(record.data)} /> : <InspectorBlock label="Raw line" text={record.raw} />}
                    {record.data && <details><summary className="cursor-pointer text-2xs text-subtle-foreground">Original JSONL line</summary><InspectorBlock className="mt-2" label="Raw line" text={record.raw} /></details>}
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
