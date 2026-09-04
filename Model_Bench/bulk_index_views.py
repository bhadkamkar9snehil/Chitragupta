#!/usr/bin/env python3
"""Bulk-generate LITE catalog entries for every real XStudio_Xbatch view that
doesn't already have a full hand-curated entry in Knowledge/view_catalog.json.

Why this exists: full entries (export_view_samples.py + a human reading the
live sample rows + hand-written relationships/verified queries) take real
time per view -- a live DB round-trip plus judgment, not just a lookup.
There are 666 real views in XStudio_Xbatch alone; hand-curating all of them
one at a time is not a viable way to reach "every view indexed."

This script instead builds a LITE entry for every view directly from
Knowledge/schema_allowlist.json (already populated, no DB trip needed):
category guessed from name-keyword rules, key_column guessed from common ID
column names actually present, no sample rows / no verified queries / no
relates_to. Lite entries are explicitly marked "tier": "lite" so nothing
downstream mistakes a guess for a verified fact.

This does NOT replace or downgrade existing full entries -- a view already
present in the catalog (any tier) is left untouched.

Usage:
    python bulk_index_views.py --view-list <path to newline-separated real view names>
"""
import argparse
import json
import re
from pathlib import Path

ALLOWLIST_PATH = Path(__file__).parent.parent / "Knowledge" / "schema_allowlist.json"
CATALOG_PATH = Path(__file__).parent.parent / "Knowledge" / "view_catalog.json"
DATABASE = "XStudio_Xbatch"

# Ordered: first matching rule wins. Keep in sync with view_catalog.json's
# existing categories -- do not invent a new category name here without
# also adding its "description" to categories in the catalog.
CATEGORY_RULES = [
    ("heat_execution", re.compile(r"heat|eaf|lrf|ccm|sms_.*process|tracability", re.I)),
    ("performance_delay", re.compile(r"delay|oee|downtime", re.I)),
    ("sap_posting", re.compile(r"sap|api_", re.I)),
    ("billet_inventory", re.compile(r"billet", re.I)),
    ("quality", re.compile(r"quality|spectro|chemistry|rebar|wire_rod|round_bar", re.I)),
    ("work_order", re.compile(r"work_?order|campaign_plan", re.I)),
    ("platform_monitoring", re.compile(r"monitoring|backup|dlb|fcm|hardware|folder_monitoring|events_monitoring", re.I)),
    ("audit_trail", re.compile(r"_audit_?vw$|_audit$", re.I)),
]

KEY_COLUMN_CANDIDATES = ["HeatNo", "HeatID", "BilletNo", "WorkOrderNumber", "TransactionID", "TicketNo", "ID"]


def guess_category(view_name: str) -> str:
    for category, pattern in CATEGORY_RULES:
        if pattern.search(view_name):
            return category
    return "uncategorized"


def guess_key_column(columns: list) -> str | None:
    for candidate in KEY_COLUMN_CANDIDATES:
        if candidate in columns:
            return candidate
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--view-list", required=True, help="Newline-separated file of real view names (from sys.views)")
    args = ap.parse_args()

    view_names = [
        line.strip() for line in Path(args.view_list).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    allowlist = json.loads(ALLOWLIST_PATH.read_text(encoding="utf-8"))
    db_objects = allowlist.get(DATABASE, {})

    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    existing_views = catalog.setdefault("views", {})

    added, skipped_existing, skipped_no_columns = 0, 0, 0

    for view_name in view_names:
        if view_name in existing_views:
            skipped_existing += 1
            continue

        columns = db_objects.get(f"dbo.{view_name}")
        if not columns:
            skipped_no_columns += 1
            continue

        category = guess_category(view_name)
        key_column = guess_key_column(columns)

        existing_views[view_name] = {
            "database": DATABASE,
            "category": category,
            "tier": "lite",
            "tags": ["auto-indexed"],
            "key_column": key_column,
            "column_count": len(columns),
            "columns": columns,
            "what_it_has": (
                f"Auto-indexed, not yet hand-reviewed. Category and key column are name-based "
                f"guesses -- verify against real sample data (export_view_samples.py) before "
                f"trusting them for investigation. {len(columns)} columns: "
                + ", ".join(columns[:15]) + (", ..." if len(columns) > 15 else "")
            ),
            "doc": None,
        }
        added += 1

    for category, _ in CATEGORY_RULES + [("uncategorized", None)]:
        catalog.setdefault("categories", {}).setdefault(category, {
            "description": f"Auto-populated bucket for lite-indexed views matching '{category}' name patterns -- not yet hand-reviewed.",
            "views": [],
        })

    for view_name, entry in existing_views.items():
        cat = entry.get("category")
        if cat and view_name not in catalog["categories"].setdefault(cat, {"description": "", "views": []})["views"]:
            catalog["categories"][cat]["views"].append(view_name)

    catalog["_meta"]["coverage"] = (
        f"{len(existing_views)} of 960 real views in the catalog as of this run "
        f"({added} lite auto-indexed this pass). Lite entries (tier=lite) are name/column-based "
        f"guesses, not verified -- see verified_query_discipline for the bar full entries meet."
    )

    CATALOG_PATH.write_text(json.dumps(catalog, indent=2), encoding="utf-8")
    print(f"Added {added} lite entries. Skipped {skipped_existing} already-catalogued, "
          f"{skipped_no_columns} not found in schema_allowlist.")
    print(f"Total views in catalog now: {len(existing_views)}")


if __name__ == "__main__":
    main()
