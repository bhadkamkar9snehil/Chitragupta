#!/usr/bin/env python3
"""Reusable model-evaluation harness that drives Hermes itself.

Per explicit project decision (2026-09-03): local-model evaluation must go
through the `hermes` CLI against the real `l2-investigator` profile, not a
raw HTTP call to LM Studio/Ollama. The profile's SOUL.md, AGENTS.md routing,
and xstudio-* skills are the whole point of the comparison -- a naked
completion tells you the model's raw fluency, not whether it can actually
do this job.

Run from WSL (this is where the working l2-investigator profile and gateway
live -- see AGENTS.md/CLAUDE.md "primary working install"):

    python3 hermes_cli_bench.py --model "qwen/qwen3.5-9b" --tag qwen35-9b

Each battery prompt becomes one *separate*, fresh `hermes -p l2-investigator
-m <model> --provider lmstudio -z "<prompt>"` invocation (no --resume, so no
cross-prompt session contamination). Full stdout (whatever Hermes actually
produced -- reasoning, tool calls, skill routing, final answer) is captured
verbatim per prompt.

This script does NOT load or unload any LM Studio model -- load the
candidate model first (lms load ...), then run this against it. The L2
polling cron job (52e0844c3c1e) should stay paused for the whole evaluation
phase -- this script does not touch cron state either.
"""
import argparse
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

BATTERY = [
    {
        "id": "sql_basic_filter",
        "category": "sql_generation",
        "prompt": (
            "Write a T-SQL query against SQL Server to find all rows in "
            "dbo.Complaint_Mst_Tbl where Status = 'Enter' and the ticket "
            "was created more than 24 hours ago. Assume a datetime column "
            "named CreatedDate exists. Return only the query, no explanation."
        ),
    },
    {
        "id": "sql_json_extract",
        "category": "sql_generation",
        "prompt": (
            "In dbo.Complaint_Mst_Tbl there are columns ProblemCategory, "
            "SourceSystem, and ExtractedEntitiesJson (nvarchar(max) holding "
            "a JSON object like {\"HeatNo\": \"H12345\"}). Write a T-SQL "
            "query that extracts the HeatNo value from ExtractedEntitiesJson "
            "for rows where SourceSystem = 'Xbatch', using SQL Server's "
            "native JSON functions. Return only the query, no explanation."
        ),
    },
    {
        "id": "ticket_triage",
        "category": "reasoning_with_routing",
        "prompt": (
            "A helpdesk ticket says: 'Batch report for heat H88213 shows "
            "wrong yield percentage, values dropped to zero after the 9am "
            "shift change, other heats look fine.' Using this profile's own "
            "task-router knowledge, name the likely problem category, which "
            "Knowledge file / skill this should route to, and what the "
            "first investigation step should be. 3-4 sentences."
        ),
    },
    {
        "id": "workflow_awareness",
        "category": "domain_knowledge",
        "prompt": (
            "Briefly explain, using this profile's own knowledge (not "
            "general SQL knowledge), what Hermes_L2_Publish_Response_Usp is "
            "for and why a response should go through it instead of a raw "
            "UPDATE on Complaint_Mst_Tbl."
        ),
    },
]


def run_one(model, provider, prompt, timeout):
    cmd = ["hermes", "-p", "l2-investigator", "-m", model, "--provider", provider, "-z", prompt]
    t0 = time.time()
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        elapsed = time.time() - t0
        return {
            "ok": proc.returncode == 0,
            "elapsed_s": round(elapsed, 1),
            "returncode": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr[-4000:] if proc.stderr else "",
        }
    except subprocess.TimeoutExpired as e:
        elapsed = time.time() - t0
        return {
            "ok": False,
            "elapsed_s": round(elapsed, 1),
            "error": f"timed out after {timeout}s",
            "stdout": (e.stdout or ""),
            "stderr": (e.stderr or ""),
        }


def write_report(model, provider, results, out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    safe_model = model.replace("/", "_").replace(":", "_")
    json_path = out_dir / f"{safe_model}_{ts}.json"
    md_path = out_dir / f"{safe_model}_{ts}.md"

    json_path.write_text(json.dumps(
        {"model": model, "provider": provider, "timestamp": ts, "results": results}, indent=2,
    ), encoding="utf-8")

    lines = [f"# Hermes CLI bench: {model} ({provider})", "", f"Timestamp: {ts}", ""]
    for r in results:
        lines.append(f"## {r['id']} ({r['category']})")
        lines.append(f"- ok: {r.get('ok')} | elapsed: {r.get('elapsed_s')}s | returncode: {r.get('returncode')}")
        lines.append("")
        lines.append("```")
        lines.append((r.get("stdout") or "").strip() or "(empty stdout)")
        lines.append("```")
        if r.get("stderr"):
            lines.append("<details><summary>stderr</summary>")
            lines.append("")
            lines.append("```")
            lines.append(r["stderr"].strip())
            lines.append("```")
            lines.append("</details>")
        lines.append("")
    md_path.write_text("\n".join(lines), encoding="utf-8")
    return json_path, md_path


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True, help="model identifier as passed to hermes -m")
    ap.add_argument("--provider", default="lmstudio", choices=["lmstudio", "ollama"])
    ap.add_argument("--timeout", type=int, default=900,
                     help="per-prompt timeout in seconds -- a single hermes -z call through the "
                          "l2-investigator profile's skill/routing stack measured 12m8s in an "
                          "initial live test, far slower than raw model inference alone")
    ap.add_argument("--out-dir", default=str(Path(__file__).parent / "results"))
    ap.add_argument("--only", help="comma-separated battery ids to run, default all")
    args = ap.parse_args()

    battery = BATTERY
    if args.only:
        wanted = set(args.only.split(","))
        battery = [b for b in BATTERY if b["id"] in wanted]

    print(f"Evaluating {args.model} via hermes CLI (provider={args.provider}), {len(battery)} prompts")
    results = []
    for case in battery:
        print(f"  [{case['id']}] running (timeout {args.timeout}s) ...", flush=True)
        r = run_one(args.model, args.provider, case["prompt"], args.timeout)
        r["id"] = case["id"]
        r["category"] = case["category"]
        results.append(r)
        status = "ok" if r.get("ok") else "FAILED"
        print(f"  [{case['id']}] {status} in {r.get('elapsed_s')}s", flush=True)

    json_path, md_path = write_report(args.model, args.provider, results, args.out_dir)
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    ok = sum(1 for r in results if r.get("ok"))
    print(f"{ok}/{len(results)} calls succeeded")


if __name__ == "__main__":
    main()
