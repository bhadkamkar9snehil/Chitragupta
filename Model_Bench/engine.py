#!/usr/bin/env python3
"""Chitragupta engine: the always-on process that replaces the Hermes gateway.

Two loops in one process (docs/plans/no-hermes-architecture.md):
  * dispatcher: claims the best ready card, runs `agent_loop.py <card>` as a worker process under the card's
    max runtime, then reconciles at once (what the orchestrator plugin's terminal-event hook did);
  * scheduler: scout every 2 minutes (reconcile + claim), completion audit every 10 minutes, and the trace drain.
The lifecycle logic itself stays in l2_pipeline_runtime.py; this file only decides when to call it.
"""
from __future__ import annotations

import atexit
import hashlib
import json
import logging
import os
import shutil
import subprocess
import sys
import threading
import time
import zipfile
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import chitragupta_config  # noqa: E402

CONFIG_MTIME = chitragupta_config.apply()  # before the runtime and cards read their environment

import cards  # noqa: E402
import l2_pipeline_runtime as rt  # noqa: E402

SCOUT_EVERY = 120
AUDIT_EVERY = 600
POLL_SECONDS = 2
DATA = chitragupta_config.data_dir()

log = logging.getLogger("engine")
_drain_lock = threading.Lock()


def tick(mode: str, fn: Callable[[Any], Any]) -> None:
    """One lifecycle call under the lifecycle lock; a busy lock means another owner is already doing it."""
    args = rt.build_parser().parse_args([mode])
    try:
        with rt.lifecycle_lock(args):
            result = fn(args)
        status = result.get("status") if isinstance(result, dict) else result
        log.info("%s: %s", mode, status)
    except RuntimeError as exc:
        if "LIFECYCLE_BUSY" not in str(exc):
            log.exception("%s failed", mode)
    except Exception:  # noqa: BLE001 - the loops must survive any single failure
        log.exception("%s failed", mode)


def audit(args: Any) -> dict[str, Any]:
    return {"review_sql_divergences": rt.audit_done_reviewers(args), "pipeline_stall_check": rt.check_pipeline_stall(args)}


def drain() -> None:
    """Persist worker traces to SQL and write the readable ticket notes (one at a time)."""
    if not _drain_lock.acquire(blocking=False):
        return
    try:
        done = subprocess.run([sys.executable, str(HERE / "drain_and_summarize.py")], capture_output=True, text=True, timeout=600)
        if done.returncode:
            log.warning("trace drain failed: %s", (done.stderr or done.stdout).strip()[-400:])
    except (OSError, subprocess.TimeoutExpired) as exc:
        log.warning("trace drain unavailable: %s", exc)
    finally:
        _drain_lock.release()


# The prebuilt index was embedded with this model; a different one needs `gbrain migrate embeddings`.
GBRAIN_CONFIG = {"engine": "pglite", "embedding_model": "lmstudio:text-embedding-nomic-embed-text-v1.5", "embedding_dimensions": 768,
                 "schema_pack": "xbatch-world", "mcp": {"publish_skills": True}, "self_upgrade": {"mode": "off"}}


def seed_index(exe: str, home: Path) -> None:
    """The index ships as brain.zip beside gbrain.exe (built once, embeddings included, so an install never runs the
    half-hour sync). Extract it on first start and again whenever a new build ships a different one."""
    seed = Path(exe).with_name("brain.zip")
    marker = home / "brain.sha256"
    if not seed.exists():
        return
    digest = hashlib.sha256(seed.read_bytes()).hexdigest()
    if marker.exists() and marker.read_text().strip() == digest and (home / ".gbrain" / "brain.pglite").exists():
        return
    log.info("installing the knowledge index from %s", seed)
    shutil.rmtree(home / ".gbrain", ignore_errors=True)
    home.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(seed) as z:
        z.extractall(home)
    marker.write_text(digest)


def gbrain_service() -> None:
    """GBrain is a child of the engine. Its embedded database admits one process, so this one serves every client
    (the engine's world walk, the console) over HTTP. The index ships prebuilt; this writes its config (which
    holds an absolute path, so it is rewritten per install) and restarts the server if it dies."""
    exe = os.environ.get("CHITRAGUPTA_GBRAIN_BIN") or shutil.which("gbrain")
    home = Path(os.environ.get("CHITRAGUPTA_GBRAIN_HOME") or DATA / "gbrain")
    index = home / ".gbrain" / "brain.pglite"
    port = urlparse(os.environ.get("CHITRAGUPTA_GBRAIN_URL") or "http://127.0.0.1:3131").port or 3131
    if exe:
        seed_index(exe, home)
    if not exe or not index.exists():
        log.warning("GBrain not started (program %s, index %s): knowledge search is off", exe, index)
        return
    (home / ".gbrain" / "config.json").write_text(json.dumps({**GBRAIN_CONFIG, "database_path": str(index)}, indent=2), encoding="utf-8")
    env = {**os.environ, "GBRAIN_HOME": str(home)}
    while True:
        with open(DATA / "logs" / "gbrain.log", "ab") as out:
            proc = subprocess.Popen([exe, "serve", "--http", "--port", str(port)], env=env, stdout=out, stderr=subprocess.STDOUT)
            atexit.register(proc.terminate)
            log.info("GBrain serving on port %d (pid %d)", port, proc.pid)
            code = proc.wait()
        log.warning("GBrain exited with %s; restarting in 5s", code)
        time.sleep(5)


def work(card: dict[str, Any]) -> None:
    (DATA / "logs").mkdir(parents=True, exist_ok=True)
    started = time.time()
    with open(DATA / "logs" / f"worker-{card['id']}.log", "ab") as out:
        proc = subprocess.Popen([sys.executable, str(HERE / "agent_loop.py"), card["id"]],
                                stdout=out, stderr=subprocess.STDOUT)
        try:
            code = proc.wait(timeout=card["max_runtime_seconds"])
        except subprocess.TimeoutExpired:
            proc.kill()
            cards.finish(card["id"], status="timed_out", summary=f"worker exceeded {card['max_runtime_seconds']}s")
            code = None
    if (now := cards.get_card(card["id"])) and now["status"] == "running":
        cards.finish(card["id"], status="crashed", summary=f"worker exited {code} without finishing the card")
    log.info("card %s (%s) finished in %ds", card["id"], card["assignee"], time.time() - started)
    tick("reconcile", rt.reconcile)
    drain()


def dispatcher() -> None:
    while True:
        try:
            card = cards.claim()
        except Exception:  # noqa: BLE001 - SQL may be briefly unreachable; the board is durable
            log.exception("claim failed")
            time.sleep(15)
            continue
        if not card:
            time.sleep(POLL_SECONDS)
            continue
        try:
            work(card)
        except Exception:  # noqa: BLE001
            log.exception("worker supervision failed for %s", card["id"])


def main() -> None:
    (DATA / "logs").mkdir(parents=True, exist_ok=True)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s",
                        handlers=[logging.StreamHandler(), logging.FileHandler(DATA / "logs" / "engine.log", encoding="utf-8")])
    while True:  # SQL is external: the engine starts even when it is down and waits for it
        try:
            log.info("recovered %d orphaned running card(s)", cards.recover_running())
            break
        except Exception as exc:  # noqa: BLE001
            log.warning("SQL unavailable, retrying in 30s: %s", str(exc)[:200])
            time.sleep(30)
    threading.Thread(target=gbrain_service, name="gbrain", daemon=True).start()
    threading.Thread(target=dispatcher, name="dispatcher", daemon=True).start()
    last_audit = 0.0
    while True:
        if chitragupta_config.apply() != CONFIG_MTIME:  # the Connections panel saved new settings: restart to use them
            log.info("configuration changed, exiting for the service manager to restart")
            os._exit(75)
        tick("scout", rt.scout)
        drain()
        if time.time() - last_audit >= AUDIT_EVERY:
            tick("audit", audit)
            last_audit = time.time()
        time.sleep(SCOUT_EVERY)


if __name__ == "__main__":
    main()
