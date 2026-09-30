"""Worker agent loop: one card, one LM Studio conversation, typed tools.

Run as `python agent_loop.py <card_id>` by the engine (one process per card, like a Hermes worker: crash and
timeout isolation, fresh plugin state). The existing xstudio-l2 plugins register into a tiny Hermes-compatible
context (`register_tool` / `register_hook`), so their typed tools and guards run unchanged; the loop fires the
same hooks. The card tools (`kanban_*`) are built in and write to cards.py. See
docs/plans/no-hermes-architecture.md (D2, amended: stdlib HTTP, no SDK).
"""
from __future__ import annotations

import importlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable, Optional

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
os.environ.setdefault("L2_XSTUDIO_BRIDGE", str(REPO / "Model_Bench" / "xstudio_l2_tool_bridge.py"))

import cards  # noqa: E402

CONFIG_PATH = Path(os.environ.get("CHITRAGUPTA_ENGINE_CONFIG") or REPO / "deploy" / "engine.json")
PLUGINS = ("xstudio_l2_tools_plugin", "xstudio_l2_trace_plugin")  # orchestrator/learning are not part of the worker
MAX_NUDGES = 3


def load_config() -> dict[str, Any]:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def profile_config(name: str) -> dict[str, Any]:
    cfg = load_config()
    out = {**cfg["defaults"], **cfg["profiles"].get(name, {})}
    out["base_url"] = os.environ.get("LMSTUDIO_BASE_URL") or cfg["lm_studio"]["base_url"]
    out["skills_dir"] = cfg.get("skills_dir", "deploy/skills/xstudio")
    return out


# ---------------------------------------------------------------- Hermes-compatible plugin context
class Context:
    def __init__(self) -> None:
        self.tools: dict[str, tuple[dict[str, Any], Callable[..., str]]] = {}
        self.hooks: dict[str, list[Callable[..., Any]]] = defaultdict(list)

    def register_tool(self, name: str, schema: dict[str, Any], handler: Callable[..., str], **_: Any) -> None:
        self.tools[name] = (schema, handler)

    def register_hook(self, event: str, fn: Callable[..., Any]) -> None:
        self.hooks[event].append(fn)

    def fire(self, event: str, **kwargs: Any) -> list[Any]:
        out = []
        for fn in self.hooks.get(event, []):
            try:
                out.append(fn(**kwargs))
            except Exception as exc:  # noqa: BLE001 - hooks are observers/guards; one failing must not kill the worker
                print(f"WARNING: hook {event}/{getattr(fn, '__name__', fn)} failed: {exc}", file=sys.stderr)
        return out


_KANBAN_SCHEMAS = {
    "kanban_show": {"description": "Show this card (its body is your task).", "parameters": {
        "type": "object", "properties": {}, "additionalProperties": False}},
    "kanban_complete": {"description": "Finish the card successfully (a reviewer approves with this).", "parameters": {
        "type": "object", "properties": {"summary": {"type": "string"}, "result": {"type": "string"},
                                         "metadata": {"type": "object"}}, "additionalProperties": True}},
    "kanban_block": {"description": "Block the card with a specific reason (a reviewer rejects with this).", "parameters": {
        "type": "object", "properties": {"reason": {"type": "string"}}, "additionalProperties": True}},
    "kanban_comment": {"description": "Add a note to the card.", "parameters": {
        "type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"], "additionalProperties": True}},
}
_TERMINAL = {"kanban_complete", "kanban_block"}


def build_context(card: dict[str, Any]) -> Context:
    ctx = Context()
    for mod in PLUGINS:
        importlib.import_module(mod).register(ctx)
    state = {"finished": False}

    def show(params: dict[str, Any], **_: Any) -> str:
        return json.dumps({"task": card}, default=str)

    def complete(params: dict[str, Any], **_: Any) -> str:
        summary = str(params.get("summary") or params.get("result") or "").strip()
        md = params.get("metadata") if isinstance(params.get("metadata"), dict) else None
        ok = cards.finish(card["id"], status="done", summary=summary, metadata=md,
                          result=str(params.get("result") or "") or None)
        state["finished"] = ok
        return json.dumps({"ok": ok, "status": "done"} if ok else {"error": "card is not running"})

    def block(params: dict[str, Any], **_: Any) -> str:
        reason = str(params.get("reason") or params.get("summary") or "").strip()
        ok = cards.finish(card["id"], status="blocked", summary=reason)
        state["finished"] = ok
        return json.dumps({"ok": ok, "status": "blocked"} if ok else {"error": "card is not running"})

    def comment(params: dict[str, Any], **_: Any) -> str:
        cards.comment(card["id"], str(params.get("text") or ""), author=card["assignee"])
        return json.dumps({"ok": True})

    for name, handler in (("kanban_show", show), ("kanban_complete", complete),
                          ("kanban_block", block), ("kanban_comment", comment)):
        ctx.register_tool(name, _KANBAN_SCHEMAS[name], handler)
    ctx.state = state  # type: ignore[attr-defined]
    return ctx


# ---------------------------------------------------------------- prompt
def _skill_text(name: str, skills_dir: str) -> str:
    path = REPO / skills_dir / name / "SKILL.md"
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    return re.sub(r"\A---.*?\n---\s*", "", text, count=1, flags=re.S).strip()


def system_prompt(card: dict[str, Any], cfg: dict[str, Any]) -> str:
    soul = (REPO / cfg["soul"]).read_text(encoding="utf-8") if cfg.get("soul") else ""
    skills = "\n\n".join(f"## Skill: {n}\n{_skill_text(n, cfg['skills_dir'])}" for n in card["skills"])
    return (f"{soul}\n\n{skills}\n\n"
            f"You are working card {card['id']} ({card['title']}). The card body is your task. "
            "Finish the card with kanban_complete, or with kanban_block when you must reject or cannot proceed.").strip()


# ---------------------------------------------------------------- model transport
_reasoning_cache: dict[str, Optional[str]] = {}


def reasoning_effort(cfg: dict[str, Any]) -> Optional[str]:
    """LM Studio publishes each model's reasoning options; send reasoning_effort=none when it offers to turn reasoning off."""
    key = f"{cfg['base_url']}|{cfg['model']}"
    if key not in _reasoning_cache:
        value: Optional[str] = None
        try:
            url = cfg["base_url"].rstrip("/").removesuffix("/v1") + "/api/v1/models"
            with urllib.request.urlopen(url, timeout=8) as r:
                models = json.load(r)
            models = models.get("models", models.get("data", [])) if isinstance(models, dict) else models
            for m in models:
                if cfg["model"] in (m.get("key"), m.get("id"), m.get("model_key")):
                    opts = [str(o).lower() for o in ((m.get("capabilities") or {}).get("reasoning") or {}).get("allowed_options", [])]
                    value = "none" if {"off", "none"} & set(opts) else None  # the wire value is "none" even where the UI says off
        except (OSError, ValueError):
            pass
        _reasoning_cache[key] = value
    return _reasoning_cache[key]


def chat(cfg: dict[str, Any], messages: list[dict[str, Any]], tools: list[dict[str, Any]]) -> dict[str, Any]:
    body: dict[str, Any] = {"model": cfg["model"], "messages": messages, "tools": tools, "max_tokens": cfg["max_tokens"]}
    if (effort := reasoning_effort(cfg)):
        body["reasoning_effort"] = effort
    req = urllib.request.Request(cfg["base_url"].rstrip("/") + "/chat/completions", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=cfg["request_timeout"]) as r:
            return json.load(r)
    except urllib.error.HTTPError as exc:  # the server's reason is in the body; the bare status hides it
        raise ValueError(f"HTTP {exc.code}: {exc.read()[:600].decode('utf-8', 'replace')}") from exc


# ---------------------------------------------------------------- the loop
def run(card_id: str) -> int:
    card = cards.get_card(card_id)
    if not card:
        print(f"unknown card {card_id}", file=sys.stderr)
        return 2
    cfg = profile_config(card["assignee"])
    os.environ["HERMES_KANBAN_TASK"] = card_id  # the tools plugin scopes a worker to its own card by this name
    os.environ["HERMES_PROFILE"] = card["assignee"]  # the trace plugin labels events by profile
    ctx = build_context(card)
    tools = [{"type": "function", "function": {"name": n, "description": s.get("description", ""), "parameters": s["parameters"]}}
             for n, (s, _h) in ctx.tools.items()]
    ids = {"session_id": card_id, "task_id": card_id}
    messages: list[dict[str, Any]] = [{"role": "system", "content": system_prompt(card, cfg)},
                                      {"role": "user", "content": card["body"]}]
    ctx.fire("on_session_start", **ids, model=cfg["model"], platform="cli")
    nudges = 0
    try:
        for _turn in range(cfg["max_turns"]):
            injected = [r["context"] for r in ctx.fire("pre_llm_call", **ids, user_message=card["body"], model=cfg["model"])
                        if isinstance(r, dict) and r.get("context")]
            sent = messages if not injected else [{**messages[0], "content": messages[0]["content"] + "\n\n" + "\n".join(injected)}] + messages[1:]
            started = time.time()
            try:
                resp = chat(cfg, sent, tools)
            except (urllib.error.URLError, OSError, ValueError) as exc:
                ctx.fire("api_request_error", **ids, model=cfg["model"], provider="lmstudio", error=str(exc)[:300], retryable=False)
                cards.finish(card_id, status="crashed", summary=f"model request failed: {str(exc)[:300]}")
                return 1
            msg = resp["choices"][0]["message"]
            calls = msg.get("tool_calls") or []
            ctx.fire("post_api_request", **ids, model=cfg["model"], provider="lmstudio", started_at=started,
                     api_duration=time.time() - started, usage=resp.get("usage"),
                     finish_reason=resp["choices"][0].get("finish_reason"),
                     assistant_content_chars=len(msg.get("content") or ""), assistant_tool_call_count=len(calls))
            messages.append({"role": "assistant", "content": msg.get("content") or "", **({"tool_calls": calls} if calls else {})})
            if not calls:
                nudges += 1
                if nudges > MAX_NUDGES:
                    break
                messages.append({"role": "user", "content": "The card is still running. Call the tool that finishes it "
                                 "(kanban_complete, or kanban_block to reject) now."})
                continue
            for call in calls:
                messages.append({"role": "tool", "tool_call_id": call.get("id"), "content": _execute(ctx, call, ids)})
            if ctx.state["finished"]:  # type: ignore[attr-defined]
                return 0
        cards.finish(card_id, status="gave_up", summary="worker ended without finishing the card")
        return 1
    finally:
        ctx.fire("on_session_end", **ids)
        ctx.fire("on_session_finalize", **ids)


def _execute(ctx: Context, call: dict[str, Any], ids: dict[str, str]) -> str:
    fn = call.get("function") or {}
    name = str(fn.get("name") or "")
    try:
        args = json.loads(fn.get("arguments") or "{}")
        args = args if isinstance(args, dict) else {}
    except json.JSONDecodeError:
        args = {}
    extra = {**ids, "tool_call_id": call.get("id")}
    for verdict in ctx.fire("pre_tool_call", tool_name=name, args=args, **extra):
        if isinstance(verdict, dict) and verdict.get("action") == "block":
            result = json.dumps({"ok": False, "error": verdict.get("message", "blocked"), "retry_same_call": False})
            ctx.fire("post_tool_call", tool_name=name, args=args, result=result, status="blocked", duration_ms=0, **extra)
            return result
        if isinstance(verdict, dict) and verdict.get("action") == "modify":
            args = {**args, **(verdict.get("args") or {})}
    entry = ctx.tools.get(name)
    started = time.time()
    if not entry:
        result, status = json.dumps({"ok": False, "error": f"unknown tool {name}"}), "error"
    else:
        try:
            result, status = str(entry[1](args, **ids)), "ok"
        except Exception as exc:  # noqa: BLE001 - a tool failure is a tool result, not a worker crash
            result, status = json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}), "error"
    ctx.fire("post_tool_call", tool_name=name, args=args, result=result, status=status,
             duration_ms=round((time.time() - started) * 1000), **extra)
    return result


if __name__ == "__main__":
    raise SystemExit(run(sys.argv[1]))
