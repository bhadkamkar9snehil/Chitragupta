"""Raise realistic tickets through the L1 chat, the way a requester does: a casual first message, then the details
the assistant asks for. Uses the same real plant entities and requesters as seed_real_xbatch_tickets.py.

    python Model_Bench/seed_l1_chats.py [--api http://localhost:3417] [--offset 0] [--dry-run]

Each conversation stops as soon as the assistant raises a ticket (decision == "ticket").
"""
from __future__ import annotations

import argparse
import json
import os
import urllib.parse
import urllib.request

import seed_real_xbatch_tickets as seed


def conversations(ent: dict, o: int) -> list[tuple[str, list[str]]]:
    """(requester full name, messages). Each is a question L2 can answer from live records."""
    eaf, lrf, ccm = ent["eaf_heats"][o], ent["lrf_heats"][o], ent["ccm_billets"][o]
    wo, sap = ent["work_orders"][o], ent["sap_postings"][o]
    qty = str(wo["Quantity"]).split(".")[0]
    return [
        ("Akbar Ali", [
            "hi, quick one on the energy numbers",
            f"for heat {eaf['HeatID']} shift log has power on {eaf['PowerOnTime']}. does xbatch have the same?",
            "yes that heat, EAF. just need to confirm before I sign the shift report"]),
        ("Anand Sonnis", [
            "LRF arcing time question",
            f"heat {lrf['HeatID']}, operator wrote {int(float(lrf['ArcingTime'])) + 2} min arcing on paper. what does the report show?",
            "its for the quality file, no problem with the heat as such"]),
        ("Arshad Parvez", [
            f"is WO {wo['WorkOrderNumber']} still open? planning needs to line up the next campaign",
            f"we have {qty} t on our sheet. is that the same quantity in the system?"]),
        ("Ashok Prasad", [
            "finance is asking if our production got posted to SAP",
            f"heat {sap['HeatNo']}, material doc {sap['MaterialDoc']}. did it post or not?"]),
        ("Basit Ansari", [
            f"yard says billet {ccm['BilletNo']} was cut around {str(ccm['CutStartTime'])[11:16]}",
            "can you check what time the system has for the cut? they think the torch timing is off",
            "its from the 8th July night shift"]),
    ]


def call(api: str, path: str, body: dict | None = None):
    req = urllib.request.Request(api + path, data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Content-Type": "application/json"})
    return urllib.request.urlopen(req, timeout=180)


def turn(api: str, session: str, user_id: str, text: str) -> dict:
    """One streamed turn; returns the final `done` event data."""
    done, event = {}, ""
    with call(api, f"/api/sessions/{session}/turn", {"userId": user_id, "text": text}) as resp:
        for raw in resp:
            line = raw.decode().strip()
            if line.startswith("event: "):
                event = line[7:]
            elif line.startswith("data: ") and event == "done":
                done = json.loads(line[6:])
    return done


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--api", default="http://localhost:3417")
    ap.add_argument("--offset", type=int, default=0, help="which real entity (0-9) each conversation uses")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    env = os.environ
    conn = seed.build_connection(env.get("MSSQL_MCP_SERVER") or "10.2.6.204", "XStudio_Xbatch",
                                 env.get("MSSQL_MCP_USER") or "sa", env.get("MSSQL_MCP_PASSWORD"))
    for who, messages in conversations(seed.load_real_entities(conn), args.offset):
        print(f"\n== {who}")
        for m in messages:
            print(f"   > {m}")
        if args.dry_run:
            continue
        users = json.load(call(args.api, "/api/users?q=" + urllib.parse.quote(who)))
        user = next(u for u in users if u.get("FullName") == who)
        session = json.load(call(args.api, "/api/sessions", {"userId": user["ID"]}))["ID"]
        for m in messages:
            done = turn(args.api, session, user["ID"], m)
            print(f"   decision={done.get('decision')} ticket={done.get('ticketNo')}")
            if done.get("ticketNo"):
                break


if __name__ == "__main__":
    main()
