#!/usr/bin/env python3
"""Fix synthetic test tickets (Model_Bench/seed_test_tickets.py batches 1-4)
that used FICTIONAL entity IDs (H99310, WO-99125, INS-99201, synthetic
1900000+ heats) instead of REAL ones that already exist in the live
database. Per explicit user direction 2026-09-03: ticket data should be
based on data that actually exists, so an investigation can find something
real and give a real answer, not "heat not found."

Pulls real HeatNo/WorkOrderNumber/BilletNo/InspectionLot/Batch/CampaignNo
values live from XStudio_Xbatch (via the views already in
Knowledge/view_catalog.json) and assigns them round-robin to every ticket
whose current entity value does NOT match the real format -- leaves alone
any ticket that already references a real-format value (e.g. Ticket_237-242,
created before this session's batches, already did this correctly).

UPDATE, not DELETE -- ticket IDs stay stable so live Kanban tasks already
referencing these tickets keep working; the ticket's own content changes,
its identity doesn't.

Usage:
    python fix_malformed_ticket_ids.py --server 10.2.6.204 [--dry-run]
"""
import os
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import pyodbc

REAL_HEAT_MIN, REAL_HEAT_MAX = 1504972, 1604015


def build_connection(server, database, username, password):
    return pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};"
        f"UID={username};PWD={password};TrustServerCertificate=yes"
    )


def fetch_real_pools(xbatch_conn):
    cur = xbatch_conn.cursor()
    pools = {}

    cur.execute("SELECT DISTINCT TOP 60 HeatNo FROM dbo.XBatch_Tracability_TotalDelay_Details_Vw WHERE HeatNo IS NOT NULL ORDER BY HeatNo DESC")
    pools["HeatNo"] = [str(r[0]) for r in cur.fetchall()]

    cur.execute("SELECT DISTINCT TOP 30 WorkOrderNumber FROM dbo.XStudio_List_XBatch_Work_Order_Mst_Tbl_Vw WHERE WorkOrderNumber IS NOT NULL")
    pools["WorkOrder"] = [str(r[0]) for r in cur.fetchall()]

    cur.execute("SELECT DISTINCT TOP 30 InspectionLot FROM dbo.XStudio_List_MES_SAP_Production_Trn_Tbl_SAPPostingFail_Vw WHERE InspectionLot IS NOT NULL")
    pools["InspectionLot"] = [str(r[0]) for r in cur.fetchall()]

    cur.execute("SELECT DISTINCT TOP 30 Batch FROM dbo.XStudio_List_MES_SAP_Consumption_Trn_Tbl_Vw WHERE Batch IS NOT NULL")
    pools["Batch"] = [str(r[0]) for r in cur.fetchall()]

    cur.execute("SELECT DISTINCT TOP 30 CampaignNo FROM dbo.XStudio_XMes_Campaign_Plan_work_order_Vw WHERE CampaignNo IS NOT NULL")
    pools["Campaign"] = [str(r[0]) for r in cur.fetchall()]

    cur.execute("SELECT TOP 30 HeatNo, BilletNo FROM dbo.XStudio_List_XMES_CCM_Billet_Genealogy_Trn_Tbl_Vw WHERE HeatNo IS NOT NULL AND BilletNo IS NOT NULL")
    pools["HeatBilletPairs"] = [(str(r[0]), str(r[1])) for r in cur.fetchall()]

    return pools


def is_real_format(key, value):
    if not value:
        return True  # nothing to fix
    v = str(value)
    if key == "HeatNo":
        return v.isdigit() and REAL_HEAT_MIN <= int(v) <= REAL_HEAT_MAX
    if key == "WorkOrder":
        return v.isdigit() and len(v) == 12
    if key == "InspectionLot":
        return v.isdigit() and len(v) == 11
    if key == "Batch":
        return v.isdigit()
    if key == "BilletNo":
        return bool(re.match(r"^\d+(_S?\d+)+$", v)) or bool(re.match(r"^[A-Za-z0-9]+_\d+$", v))
    if key == "Campaign":
        return bool(re.match(r"^CP\d", v))
    return True  # unknown key (Area, Meter, EquipmentID, etc.) -- never touched


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--server", default="10.2.6.204")
    ap.add_argument("--username", default="sa")
    ap.add_argument("--password", default=os.environ.get("MSSQL_MCP_PASSWORD"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    xbatch_conn = build_connection(args.server, "XStudio_Xbatch", args.username, args.password)
    pools = fetch_real_pools(xbatch_conn)
    xbatch_conn.close()
    print(f"Real pools fetched: " + ", ".join(f"{k}={len(v)}" for k, v in pools.items()))

    helpdesk_conn = build_connection(args.server, "XStudio_Helpdesk", args.username, args.password)
    try:
        cur = helpdesk_conn.cursor()
        cur.execute(
            "SELECT ID, TicketNo, BriefDetails, Description, ConversationSummary, ExtractedEntitiesJson "
            "FROM Complaint_Mst_Tbl WHERE FirstLastName = 'L1 Chatbot Test' ORDER BY TicketNo"
        )
        rows = cur.fetchall()

        fixed, skipped, mapping = 0, 0, []
        pool_idx = {"HeatNo": 0, "WorkOrder": 0, "InspectionLot": 0, "Batch": 0, "Campaign": 0, "HeatBilletPairs": 0}

        for row in rows:
            ticket_id, ticket_no, brief, desc, convo, entities_json = row
            try:
                entities = json.loads(entities_json) if entities_json else {}
            except (json.JSONDecodeError, TypeError):
                entities = {}
            if not entities:
                skipped += 1
                continue

            needs_fix = {k: v for k, v in entities.items() if k in ("HeatNo", "WorkOrder", "InspectionLot", "Batch", "BilletNo", "Campaign") and not is_real_format(k, v)}
            if not needs_fix:
                skipped += 1
                continue

            new_entities = dict(entities)
            replacements = []

            # Keep HeatNo/BilletNo consistent with each other whenever HeatNo needs
            # fixing and a BilletNo is also present -- a BilletNo can pass the shape
            # regex (digits_digits) while still carrying a fake heat-number prefix
            # (confirmed real bug: "1900005_05" matches the pattern but 1900005 was
            # a synthetic heat), so gate on "HeatNo needs fixing", not "BilletNo's
            # own format looks wrong".
            if "HeatNo" in needs_fix and "BilletNo" in entities:
                heat, billet = pools["HeatBilletPairs"][pool_idx["HeatBilletPairs"] % len(pools["HeatBilletPairs"])]
                pool_idx["HeatBilletPairs"] += 1
                replacements.append((str(entities["HeatNo"]), heat))
                replacements.append((str(entities["BilletNo"]), billet))
                new_entities["HeatNo"] = heat
                new_entities["BilletNo"] = billet
                needs_fix.pop("HeatNo", None)
                needs_fix.pop("BilletNo", None)

            for key, old_val in needs_fix.items():
                pool = pools.get(key)
                if not pool:
                    continue
                new_val = pool[pool_idx[key] % len(pool)]
                pool_idx[key] += 1
                replacements.append((str(old_val), new_val))
                new_entities[key] = new_val

            new_brief, new_desc, new_convo = brief, desc, convo
            for old_val, new_val in replacements:
                if old_val in (new_brief or ""):
                    new_brief = new_brief.replace(old_val, new_val)
                if old_val in (new_desc or ""):
                    new_desc = new_desc.replace(old_val, new_val)
                if old_val in (new_convo or ""):
                    new_convo = new_convo.replace(old_val, new_val)

            mapping.append((ticket_no, dict(entities), new_entities))
            print(f"{'[DRY RUN] ' if args.dry_run else ''}{ticket_no}: {entities} -> {new_entities}")

            if not args.dry_run:
                cur.execute(
                    "UPDATE Complaint_Mst_Tbl SET BriefDetails = ?, Description = ?, "
                    "ConversationSummary = ?, ExtractedEntitiesJson = ? WHERE ID = ?",
                    new_brief, new_desc, new_convo, json.dumps(new_entities), ticket_id,
                )
            fixed += 1

        if not args.dry_run:
            helpdesk_conn.commit()
        print(f"\n{'[DRY RUN] Would fix' if args.dry_run else 'Fixed'} {fixed} ticket(s), skipped {skipped} (already real or no entities).")

        mapping_path = Path(__file__).parent / "id_fix_mapping.json"
        mapping_path.write_text(
            json.dumps([{"TicketNo": t, "old": o, "new": n} for t, o, n in mapping], indent=2),
            encoding="utf-8",
        )
        print(f"Mapping written to {mapping_path} (for updating any live Kanban task bodies).")
    finally:
        helpdesk_conn.close()


if __name__ == "__main__":
    main()
