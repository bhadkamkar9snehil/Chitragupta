#!/usr/bin/env python3
"""Deterministic XBatch world/recipe selection and evidence packaging."""
from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any

MODULE_ROOT = Path(__file__).resolve().parents[1]


def resolve_knowledge_root(candidates: list[Path] | None = None) -> Path:
    if candidates is None:
        candidates = []
        if os.environ.get("AIHELPDESK_ROOT"):
            candidates.append(Path(os.environ["AIHELPDESK_ROOT"]))
        candidates.extend((
            MODULE_ROOT,
            Path(__file__).resolve().parent,
            Path("/mnt/c/Users/Admin/Documents/Office/AIHelpdesk"),
        ))
    required = {"xstudio_semantic_atlas.json", "manifest.json", "xbatch_investigation_recipes.json"}
    for candidate in candidates:
        roots = (candidate, candidate / "Knowledge", candidate / "knowledge")
        for root in roots:
            if root.is_dir() and required <= {path.name for path in root.iterdir() if path.is_file()}:
                return root
    raise FileNotFoundError("XBatch world knowledge bundle not found")


KNOWLEDGE_ROOT = resolve_knowledge_root()
ATLAS_PATH = KNOWLEDGE_ROOT / "xstudio_semantic_atlas.json"
MANIFEST_PATH = KNOWLEDGE_ROOT / "manifest.json"
RECIPES_PATH = KNOWLEDGE_ROOT / "xbatch_investigation_recipes.json"

ALLOWED_RECIPE_TOOLS = {
    "xstudio_select", "xstudio_suggest_tables", "xstudio_find_objects",
    "xstudio_get_definition", "xstudio_validate_identifiers",
    "xstudio_resolve_heat", "xstudio_get_ticket_context",
    "xstudio_get_run_actions", "xstudio_read_procedure",
    "xstudio_heat_context", "xstudio_sap_api_context",
    "xstudio_work_order_context",
}
REQUIRED_RECIPE_FIELDS = {
    "recipe_id", "route", "description", "ticket_signals", "identifiers",
    "probes", "required_evidence", "interpretation_rules", "stop_conditions",
    "escalation_conditions", "review_checks",
}


def validate_recipes(recipes: list[dict[str, Any]], manifest_routes: set[str]) -> None:
    seen_routes: set[str] = set()
    for index, recipe in enumerate(recipes):
        missing = sorted(REQUIRED_RECIPE_FIELDS - set(recipe))
        if missing:
            raise ValueError(f"recipe {index} missing required fields: {', '.join(missing)}")
        route = str(recipe["route"])
        if route not in manifest_routes:
            raise ValueError(f"recipe {recipe['recipe_id']} has unknown route {route}")
        if route in seen_routes:
            raise ValueError(f"route {route} has more than one recipe")
        seen_routes.add(route)
        for probe in recipe["probes"]:
            tool = probe.get("tool")
            if tool == "xstudio_query" or "sql" in (probe.get("arguments") or {}):
                raise ValueError(f"recipe {recipe['recipe_id']} contains arbitrary SQL")
            if tool not in ALLOWED_RECIPE_TOOLS:
                raise ValueError(f"recipe {recipe['recipe_id']} uses unregistered tool {tool}")
    missing_routes = manifest_routes - seen_routes
    if missing_routes:
        raise ValueError("routes without recipes: " + ", ".join(sorted(missing_routes)))


def load_world(
    atlas_path: Path = ATLAS_PATH,
    manifest_path: Path = MANIFEST_PATH,
    recipes_path: Path = RECIPES_PATH,
) -> dict[str, Any]:
    atlas = json.loads(atlas_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    recipes = json.loads(recipes_path.read_text(encoding="utf-8"))["recipes"]
    routes = {str(item["route"]) for item in manifest.get("routes", [])}
    validate_recipes(recipes, routes)
    return {"atlas": atlas, "manifest": manifest, "recipes": recipes}


def _entities(ticket: dict[str, Any]) -> dict[str, Any]:
    value = ticket.get("ExtractedEntitiesJson")
    if isinstance(value, dict):
        return value
    try:
        parsed = json.loads(str(value or "{}"))
        return parsed if isinstance(parsed, dict) else {}
    except json.JSONDecodeError:
        return {}


def _identifiers(ticket: dict[str, Any]) -> dict[str, str]:
    entities = _entities(ticket)
    aliases = {
        "heat": ("HeatNo", "HeatID", "Heat"),
        "work_order": ("WorkOrderNumber", "WorkOrder", "ManufacturingOrder", "MESWorkOrderNumber"),
        "transaction_id": ("TransactionID", "SAPTransactionID", "Saptransactionid"),
        "inspection_lot": ("InspectionLot",), "billet": ("BilletNo",),
        "sub_lot": ("SubLotNo",), "equipment": ("EquipmentID",),
        "campaign": ("CampaignNo", "Campaign"),
    }
    result: dict[str, str] = {}
    for canonical, keys in aliases.items():
        value = next((entities.get(key) for key in keys if entities.get(key) not in (None, "")), None)
        if value is not None:
            normalized = str(value).strip()
            if canonical == "heat" and re.fullmatch(r"[Hh]?\d+", normalized):
                normalized = normalized.lstrip("Hh")
            result[canonical] = normalized
    return result


def select_recipes(ticket: dict[str, Any], world: dict[str, Any] | None = None) -> dict[str, Any]:
    world = world or load_world()
    text = " ".join(str(ticket.get(key) or "") for key in (
        "BriefDetails", "Description", "ProblemCategory", "HermesAreaName", "ConversationSummary"
    )).casefold()
    priority = (
        ("hermes_runtime", ("hermes", "kanban", "reviewer", "l2 run")),
        ("api_transaction", ("transaction id", "api error", "api call", "usage decision api")),
        ("sap_posting", ("sap", "posting", "material document", "goods movement")),
        ("work_order", ("work order", "manufacturing order", "campaign")),
        ("billet_inventory", ("billet", "genealogy", "strand", "yard")),
        ("quality", ("quality", "chemistry", "spectro", "usage decision", "inspection lot", "deviation")),
        ("performance", ("delay", "oee", "downtime", "stoppage")),
        ("heat_execution", ("heat", "eaf", "lrf", "ccm", "tapping", "casting")),
        ("helpdesk_ticket", ("ticket status", "assignment", "helpdesk workflow")),
    )
    route = next((name for name, signals in priority if any(signal in text for signal in signals)), "discover")
    by_route = {recipe["route"]: recipe for recipe in world["recipes"]}
    return {"primary": by_route[route], "secondary": [], "identifiers": _identifiers(ticket)}


def world_context(selection: dict[str, Any], world: dict[str, Any] | None = None,
                  max_chars: int = 6000) -> dict[str, Any]:
    world = world or load_world()
    recipe = selection["primary"]
    preferred = set(recipe.get("preferred_objects") or [])
    relationships = [
        edge for edge in world["atlas"].get("relationships", [])
        if edge["source"]["object"] in preferred or edge["target"]["object"] in preferred
    ]
    compact_recipe = {key: recipe[key] for key in (
        "recipe_id", "route", "description", "identifiers", "probes",
        "required_evidence", "interpretation_rules", "stop_conditions",
        "escalation_conditions", "review_checks",
    )}
    context = {
        "recipe": compact_recipe,
        "ticket_identifiers": selection.get("identifiers", {}),
        "preferred_objects": sorted(preferred),
        "relationships": relationships[:24],
        "authority": "routing knowledge only; current ticket claims require audited live evidence",
    }
    while relationships and len(json.dumps(context, separators=(",", ":"))) > max_chars:
        context["relationships"] = context["relationships"][:-1]
        relationships = context["relationships"]
    if len(json.dumps(context, separators=(",", ":"))) > max_chars:
        context["relationships"] = []
    return context


def build_evidence_matrix(proposal: dict[str, Any], recipe: dict[str, Any],
                          actions: list[dict[str, Any]]) -> dict[str, Any]:
    action_map = {str(row.get("ID") or row.get("action_id")): row for row in actions}
    categories = recipe.get("required_evidence") or []
    rows = []
    for claim in proposal.get("claims") or []:
        refs = [str(value) for value in (claim.get("evidence_refs") or [])]
        refs.extend(
            str(item["action_id"])
            for item in (claim.get("evidence") or [])
            if isinstance(item, dict) and item.get("action_id")
        )
        refs = list(dict.fromkeys(refs))
        matched_actions = [action_map[ref] for ref in refs if ref in action_map]
        matched_categories = []
        for category in categories:
            objects = {str(value).casefold() for value in category.get("objects", [])}
            operations = {str(value).casefold() for value in category.get("operations", [])}
            if any(
                str(action.get("ObjectName") or action.get("object_name") or "").casefold() in objects
                or str(action.get("OperationName") or action.get("operation") or "").casefold() in operations
                for action in matched_actions
            ):
                matched_categories.append(category["category"])
        status = "REFERENCED" if matched_actions else ("MISSING_REFERENCE" if not refs else "UNKNOWN_REFERENCE")
        rows.append({
            "claim": claim.get("claim") or claim.get("text"), "status": status,
            "evidence_refs": refs, "evidence_categories": matched_categories,
        })
    return {"recipe_id": recipe["recipe_id"], "claims": rows, "review_checks": recipe.get("review_checks", [])}
