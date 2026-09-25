"use client";

import { Check, Copy } from "lucide-react";
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

const SQL_BREAK = /\b(FROM|WHERE|LEFT JOIN|RIGHT JOIN|INNER JOIN|OUTER JOIN|JOIN|GROUP BY|ORDER BY|HAVING|VALUES|SET|AND|OR)\b/gi;

export function formatSql(sql: string) {
  return sql
    .replace(/\s+/g, " ")
    .replace(SQL_BREAK, (m) => `\n${m.toUpperCase()}`)
    .replace(/,\s*/g, ",\n  ")
    .trim();
}

export function InspectorBlock({
  label,
  text,
  kind = "raw",
  className,
}: {
  label: string;
  text: string;
  kind?: "raw" | "sql";
  className?: string;
}) {
  const [copied, setCopied] = useState(false);
  const rendered = kind === "sql" ? formatSql(text) : text;

  async function copy() {
    await navigator.clipboard.writeText(text);
    setCopied(true);
    window.setTimeout(() => setCopied(false), 1200);
  }

  return (
    <section className={cn("overflow-hidden rounded-lg border bg-background", className)} aria-label={label}>
      <div className="flex items-center gap-2 border-b bg-surface-2 px-3 py-2">
        <span className="text-2xs font-semibold uppercase tracking-wider text-subtle-foreground">{label}</span>
        <span className="ml-auto text-2xs text-subtle-foreground">{kind === "sql" ? "SQL" : "Raw"}</span>
        <Button type="button" variant="ghost" size="icon-sm" aria-label={`Copy ${label}`} onClick={copy}>
          {copied ? <Check className="text-success" /> : <Copy />}
        </Button>
      </div>
      <pre className="scrollbar-thin max-h-72 overflow-auto whitespace-pre-wrap break-words p-3 font-mono text-2xs leading-relaxed text-muted-foreground">
        {rendered}
      </pre>
    </section>
  );
}
