"""No-Qwen answers: facts from audited probe rows, outcome from Jev, reply from a template.

Nothing here generates prose. The harness extracts the fields a ticket names from
rows the audit SP returned (each with an action ID), compares any values the
requester quoted, and renders a fixed reply around those recorded values. Jev only
chooses which outcome the facts support (see jev/direct_answer.py).
"""
from __future__ import annotations

import re
from typing import Any

# Chemistry prose names elements; columns use symbols.
_ALIASES = {
    "c": ("carbon",), "si": ("silicon",), "mn": ("manganese",), "s": ("sulphur", "sulfur"),
    "p": ("phosphorus",), "cr": ("chromium",), "ni": ("nickel",), "cu": ("copper",),
    "al": ("aluminium", "aluminum"), "v": ("vanadium",), "nb": ("niobium",), "b": ("boron",),
}
# A quoted value is one token: number, mm:ss, datetime, or an identifier-like word.
_VALUE = r"(\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}(?:\.\d+)?|-?\d+(?:\.\d+)?(?::\d{1,2})?(?![\w])|[A-Za-z0-9][\w.\-]*\d[\w.\-]*|'[^']{1,80}'|\"[^\"]{1,80}\")"
# Only connector words may sit between a field name and its value ("ArcingTime of 21",
# "PowerONTime (24.0000)", "Carbon=0.07"); never free prose like "inquiry for Heat".
_GAP = r"\s*\(?\s*(?:(?:=|:|of|is|was|as|shows|recorded as|value of)\s*)?\(?\s*"
_GENERIC = {"modifiedon", "createdon", "reportdate", "entrydatetime", "date"}


def _norm(text: Any) -> str:
    return re.sub(r"[^a-z0-9]", "", str(text).lower())


def ticket_text(ticket: dict[str, Any]) -> str:
    fields = ("BriefDetails", "Description", "ConversationSummary")
    source = ticket.get("ticket") if isinstance(ticket.get("ticket"), dict) else ticket
    return "\n".join(str(source.get(k) or "") for k in fields)


def _names(column: str) -> list[str]:
    """Ways a ticket may name a column: CamelCase words, the raw name, element aliases."""
    spaced = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", column)
    names = {column, spaced, spaced.replace(" ", "-")}
    names.update(_ALIASES.get(column.lower(), ()))
    return sorted(names, key=len, reverse=True)


def reported_value(text: str, column: str) -> str | None:
    """The value a requester quoted for a column, e.g. 'ArcingTime of 21.0000 min' -> '21.0000'."""
    for name in _names(column):
        if len(name) < 2 and name.lower() not in _ALIASES:
            continue
        match = re.search(rf"(?<![A-Za-z]){re.escape(name)}(?![A-Za-z]){_GAP}{_VALUE}", text, re.I)
        if match:
            return match.group(1).strip("'\"")
    return None


def _number(value: Any) -> float | None:
    """Plain numbers and mm:ss durations ('50:5' == '50:05' == 50 min 5 s)."""
    text = str(value).strip()
    match = re.fullmatch(r"(-?\d+(?:\.\d+)?)(?::(\d{1,2}))?", text)
    if not match:
        return None
    return float(match.group(1)) + (int(match.group(2)) / 60 if match.group(2) else 0.0)


def _same(reported: str, recorded: Any) -> bool:
    if recorded is None:
        return False
    a, b = _number(reported), _number(recorded)
    if a is not None and b is not None:
        return abs(a - b) < 1e-6
    # Datetimes: the requester may quote fewer fractional digits than stored.
    x, y = _norm(reported), _norm(recorded)
    both_datetimes = all(re.match(r"\d{4}-\d{2}-\d{2}", str(v).strip()) for v in (reported, recorded))
    return bool(x) and (x == y or (both_datetimes and (y.startswith(x) or x.startswith(y))))


def _named_in_ticket(text: str, column: str) -> bool:
    lowered = text.lower()
    if any(len(n) > 2 and re.search(rf"(?<![a-z]){re.escape(n.lower())}(?![a-z])", lowered)
           for n in _names(column)):
        return True
    if column.lower() in _ALIASES and any(a in lowered for a in _ALIASES[column.lower()]):
        return True
    # "posting status" names SAPPostingStatus: a two-word phrase that ends the column name.
    words = re.findall(r"[a-z]+", lowered)
    return any(len(x + y) >= 10 and _norm(column).endswith(x + y) for x, y in zip(words, words[1:]))


def _best_row(rows: list[dict[str, Any]], text: str) -> dict[str, Any] | None:
    """The row whose own values the ticket mentions most (billet no, sample type, ...)."""
    lowered = text.lower()
    scored = [(sum(1 for v in row.values() if v not in (None, "") and len(str(v)) >= 2
                   and str(v).lower() in lowered), -i, row) for i, row in enumerate(rows)]
    return max(scored)[2] if scored else None


def _audited_reads(probes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Every successful read: the table probes and the relationship hops followed from them."""
    reads = []
    for item in probes:
        if not isinstance(item, dict):
            continue
        for probe in [item.get("probe")] + [h.get("probe") for h in item.get("relationship_hops") or []
                                            if isinstance(h, dict)]:
            if isinstance(probe, dict) and probe.get("ok") and probe.get("probe_possible", True):
                reads.append(probe)
    return reads


def build_facts(ticket: dict[str, Any], probes: list[dict[str, Any]]) -> dict[str, Any]:
    """Fact table from audited probes: one entry per ticket-named field on the best row."""
    text = ticket_text(ticket)
    facts: list[dict[str, Any]] = []
    searched: list[dict[str, Any]] = []
    for probe in _audited_reads(probes):
        identifier = probe.get("identifier") or {}
        rows = [r for r in probe.get("rows") or [] if isinstance(r, dict)]
        searched.append({"table": probe.get("table"), "identifier": identifier, "rows": len(rows),
                         "action_id": probe.get("action_id")})
        row = _best_row(rows, text)
        if row is None or not probe.get("action_id"):
            continue
        for column, recorded in row.items():
            if _norm(column) in _GENERIC or column == identifier.get("column"):
                continue
            reported = reported_value(text, column)
            if reported is None and not _named_in_ticket(text, column):
                continue
            facts.append({
                "table": probe.get("table"), "identifier": identifier, "field": column,
                "recorded": recorded, "reported": reported,
                "matches": None if reported is None else _same(reported, recorded),
                "action_id": probe.get("action_id"),
            })
    compared = [f for f in facts if f["matches"] is not None]
    return {
        "facts": facts,
        "searched": searched,
        "compared": len(compared),
        "mismatches": sum(1 for f in compared if not f["matches"]),
        "any_rows": any(s["rows"] for s in searched),
    }


def outcome_from_facts(table: dict[str, Any]) -> str:
    """Which answer template the facts support; Jev only judges whether they answer the ticket."""
    if not table["any_rows"]:
        return "NOT_FOUND"
    if table["mismatches"]:
        return "CORRECTED"
    return "CONFIRMED" if table["compared"] else "ANSWERED"


def _fmt(value: Any) -> str:
    text = str(value)
    return text.rstrip("0").rstrip(".") if re.fullmatch(r"-?\d+\.\d+", text) else text


def _where(fact: dict[str, Any]) -> str:
    ident = fact.get("identifier") or {}
    return f"{fact['table']} ({ident.get('column')} {ident.get('value')})"


def proposal_for(outcome: str, table: dict[str, Any], *, run_id: str, ticket_id: str,
                 ticket: dict[str, Any]) -> dict[str, Any] | None:
    """Frozen proposal for a Jev-chosen outcome, or None when the facts cannot carry it."""
    facts, searched = table["facts"], table["searched"]
    if outcome == "CONFIRMED" and not (table["compared"] and not table["mismatches"]):
        return None
    if outcome == "CORRECTED" and not table["mismatches"]:
        return None
    if outcome == "ANSWERED" and not facts:
        return None
    if outcome == "NOT_FOUND" and (table["any_rows"] or not searched):
        return None
    if outcome not in {"CONFIRMED", "CORRECTED", "ANSWERED", "NOT_FOUND"}:
        return None

    lines, claims = [], []
    for i, fact in enumerate(facts, 1):
        recorded = _fmt(fact["recorded"])
        if fact["matches"] is None:
            line = f"- {fact['field']}: {recorded}"
        elif fact["matches"]:
            line = f"- {fact['field']}: {recorded} (matches the reported {_fmt(fact['reported'])})"
        else:
            line = f"- {fact['field']}: {recorded} (reported {_fmt(fact['reported'])})"
        lines.append(line)
        claims.append({"id": f"C{i}", "material": True, "status": "VERIFIED",
                       "claim": f"{_where(fact)} records {fact['field']} = {recorded}",
                       "evidence": [{"action_id": fact["action_id"]}]})

    sources = sorted({_where(f) for f in facts})
    if outcome == "NOT_FOUND":
        checked = "; ".join(f"{s['table']} ({(s['identifier'] or {}).get('column')} "
                            f"{(s['identifier'] or {}).get('value')})" for s in searched)
        return _proposal(run_id, ticket_id, ticket, "QUESTION",
                         reply=(f"We checked {checked} and found no record for the identifier in your "
                                "request. Please confirm the exact heat / work order / billet number "
                                "and the approximate time of the event."),
                         claims=[], summary=f"No live record found in: {checked}",
                         requester_question="Please confirm the exact identifier and time of the event.")
    heading = {
        "CONFIRMED": "The recorded values match what you reported; no discrepancy was found.",
        "CORRECTED": "The recorded values differ from what was reported. The official recorded values are:",
        "ANSWERED": "The current recorded values are:",
    }[outcome]
    reply = f"We checked {', '.join(sources)}. {heading}\n" + "\n".join(lines)
    resolution = f"{outcome.title()} against live records: " + "; ".join(
        f"{f['field']}={_fmt(f['recorded'])}" for f in facts)
    return _proposal(run_id, ticket_id, ticket, "RESOLUTION", reply=reply, claims=claims,
                     summary=resolution, resolution=resolution)


def _proposal(run_id: str, ticket_id: str, ticket: dict[str, Any], response_type: str, *,
              reply: str, claims: list[dict[str, Any]], summary: str, **extra: str) -> dict[str, Any]:
    source = ticket.get("ticket") if isinstance(ticket.get("ticket"), dict) else ticket
    return {
        "run_id": run_id, "ticket_id": ticket_id, "response_type": response_type,
        "reply_text": reply, "problem_summary": str(source.get("BriefDetails") or "")[:800],
        "findings": summary, "claims_contract_version": 1, "claims": claims,
        "evidence_status": "COMPLETE" if claims else "INCOMPLETE",
        "execution_mode": "QWEN_FREE", "generated_by": "jev_outcome_deterministic_reply",
        **extra,
    }


def compact_for_jev(table: dict[str, Any]) -> dict[str, Any]:
    """The fact table as Jev sees it (no action IDs or other plumbing)."""
    return {
        "facts": [{k: f[k] for k in ("table", "field", "recorded", "reported", "matches")} for f in table["facts"]],
        "searched": [{"table": s["table"], "identifier": s["identifier"], "rows": s["rows"]}
                     for s in table["searched"]],
        "compared": table["compared"], "mismatches": table["mismatches"],
    }


def writer_facts(table: dict[str, Any]) -> list[dict[str, Any]]:
    """The fact table as the writing model sees it: values plus the action ID to cite."""
    return [{k: f[k] for k in ("table", "field", "recorded", "reported", "matches", "action_id")}
            for f in table["facts"]]
