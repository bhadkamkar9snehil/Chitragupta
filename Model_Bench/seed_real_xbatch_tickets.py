#!/usr/bin/env python3
"""Create real, well-formed test tickets in Complaint_Mst_Tbl backed by actual plant
data from XStudio_Xbatch tables (EAF, LRF, CCM, Work Orders, SAP, Delays, Quality).

No official stored procedure exists for ticket creation (checked live via sys.procedures)
Complaint_Mst_Tbl is populated by external systems (real rows show Source='T-SQL').
This is a documented no-SP exception per xstudio-sql-write-discipline.

Usage:
    python seed_real_xbatch_tickets.py --server 10.2.6.204 [--dry-run]
"""
import os
import argparse
import json
import sys
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import pyodbc

COMPLAINT_TYPE_BUG = "814B4EAF-547F-4FBE-8444-3A8DC96AE20D"
COMPLAINT_TYPE_CLARIFICATION = "37CA8AAA-81F3-40D6-8380-F57147A75A5B"
PRIORITY_CRITICAL = "CB077E82-9055-430B-AC00-F7C7F56F51DD"
PRIORITY_HIGH = "65BE0464-2E42-4CBA-9ADF-F8E19E90B5B2"

AREA_EAF = "5FF54C4A-067F-49D8-80E9-5F4236B03947"
AREA_LRF = "27D51105-BEE2-48FD-8AB8-8ADAD48DE71C"
AREA_CCM = "B88E9146-D9DC-46D1-A46D-FC30CB5312DF"
AREA_COMMON = "5640FCDC-B42D-4F06-967A-706709A73231"
AREA_ROLLING = "6AFF2AB8-59FC-4403-B685-7CC270C5A6E3"


def build_connection(server, database, username, password):
    return pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};"
        f"UID={username};PWD={password};TrustServerCertificate=yes;"
    )


def load_real_entities(conn) -> dict:
    """Load real plant entity rows directly from XStudio_Xbatch."""
    cur = conn.cursor()
    entities = {}

    # 1. EAF Heats
    cur.execute("SELECT TOP 10 HeatID, PowerOnTime, PowerOffTime, HeatTime FROM dbo.EAF_Per_Heat WHERE HeatID IS NOT NULL AND PowerOnTime IS NOT NULL ORDER BY StartTime DESC")
    entities["eaf_heats"] = [{"HeatID": str(r[0]), "PowerOnTime": str(r[1]), "PowerOffTime": str(r[2]), "HeatTime": str(r[3])} for r in cur.fetchall()]

    # 2. LRF Heats
    cur.execute("SELECT TOP 10 HeatID, ArcingTime, PowerONTime, PowerOFFTime FROM dbo.LRF_Per_Heat WHERE HeatID IS NOT NULL AND ArcingTime IS NOT NULL ORDER BY StartTime DESC")
    entities["lrf_heats"] = [{"HeatID": str(r[0]), "ArcingTime": str(r[1]), "PowerONTime": str(r[2]), "PowerOFFTime": str(r[3])} for r in cur.fetchall()]

    # 3. CCM Billets
    cur.execute("SELECT TOP 10 HeatNo, BilletNo, StrandNo, CutStartTime FROM dbo.XMES_CCM_Billet_Genealogy_Trn_Tbl WHERE BilletNo IS NOT NULL ORDER BY CutStartTime DESC")
    entities["ccm_billets"] = [{"HeatNo": str(r[0]), "BilletNo": str(r[1]), "StrandNo": str(r[2]), "CutStartTime": str(r[3])} for r in cur.fetchall()]

    # 4. Work Orders
    cur.execute("SELECT TOP 10 WorkOrderNumber, Quantity, Status FROM dbo.XBatch_Work_Order_Mst_Tbl WHERE WorkOrderNumber IS NOT NULL ORDER BY CreatedOn DESC")
    entities["work_orders"] = [{"WorkOrderNumber": str(r[0]), "Quantity": str(r[1]), "Status": str(r[2])} for r in cur.fetchall()]

    # 5. SAP Postings
    cur.execute("SELECT TOP 10 HeatNo, ManufacturingOrder, InspectionLot, MaterialDocument FROM dbo.MES_SAP_Production_Trn_Tbl WHERE MaterialDocument IS NOT NULL ORDER BY CreatedOn DESC")
    entities["sap_postings"] = [{"HeatNo": str(r[0]), "WorkOrder": str(r[1]), "InspectionLot": str(r[2]) if r[2] else None, "MaterialDoc": str(r[3])} for r in cur.fetchall()]

    # 6. Delays
    cur.execute("SELECT TOP 10 HeatNo, Status, StartTime, EndTime FROM dbo.Delay_Trn_Tbl WHERE HeatNo IS NOT NULL AND Status IS NOT NULL ORDER BY StartTime DESC")
    entities["delays"] = [{"HeatNo": str(r[0]), "Status": str(r[1]), "StartTime": str(r[2])} for r in cur.fetchall()]

    # 7. Quality Chemistry
    cur.execute("SELECT TOP 10 HeatNo, SampleType, Grade, C, Si, ReportedTime FROM dbo.Heat_Chemistry_Quality_Data WHERE HeatNo LIKE '160%' AND SampleType IS NOT NULL ORDER BY ReportedTime DESC")
    entities["chemistry"] = [{"HeatNo": str(r[0]), "SampleType": str(r[1]), "Grade": str(r[2]), "C": str(r[3]), "Si": str(r[4]), "ReportedTime": str(r[5])} for r in cur.fetchall()]

    # 8. Genuine EAF data-quality anomalies -- real defects, not fabricated premises.
    # 8a. Malformed timing: PowerOnTime/PowerOffTime literally stored as ':' with HeatTime NULL.
    cur.execute("""
        SELECT TOP 5 HeatID FROM dbo.EAF_PER_HEAT
        WHERE IsDeleted = 0 AND HeatID IS NOT NULL
          AND (PowerOnTime = ':' OR PowerOffTime = ':' OR HeatTime IS NULL)
        ORDER BY ModifiedOn DESC
    """)
    entities["eaf_malformed_timing"] = [str(r[0]) for r in cur.fetchall()]

    # 8b. Genuine arithmetic mismatch: HeatTimeMinute far from PowerOnTimeMinute+PowerOFFTimeMinute.
    cur.execute("""
        SELECT TOP 5 HeatID, PowerOnTimeMinute, PowerOFFTimeMinute, HeatTimeMinute
        FROM dbo.EAF_PER_HEAT
        WHERE IsDeleted = 0 AND HeatID IS NOT NULL
          AND PowerOnTimeMinute IS NOT NULL AND PowerOFFTimeMinute IS NOT NULL AND HeatTimeMinute IS NOT NULL
          AND ABS(HeatTimeMinute - (PowerOnTimeMinute + PowerOFFTimeMinute)) >= 3
        ORDER BY ModifiedOn DESC
    """)
    entities["eaf_timing_mismatch"] = [
        {"HeatID": str(r[0]), "PowerOnMin": str(r[1]), "PowerOffMin": str(r[2]), "HeatTimeMin": str(r[3])}
        for r in cur.fetchall()
    ]

    return entities


def generate_tickets(entities: dict, offset: int = 0) -> list[dict]:
    tickets = []
    end = offset + 3

    # Category 1: EAF Production & Power Timing (8 tickets)
    for idx, h in enumerate(entities.get("eaf_heats", [])[offset:end]):
        heat_id = h["HeatID"]
        tickets.append({
            "AreaID": AREA_EAF,
            "ComplaintTypeID": COMPLAINT_TYPE_BUG if idx % 2 == 0 else COMPLAINT_TYPE_CLARIFICATION,
            "Priority": PRIORITY_CRITICAL,
            "BriefDetails": f"EAF Power-On time discrepancy reported for Heat {heat_id}",
            "Description": (
                f"EAF shift log shows Heat {heat_id} completed melting with recorded PowerOnTime {h['PowerOnTime']} "
                f"and PowerOffTime {h['PowerOffTime']}. The daily energy dashboard indicates higher than normal electrical "
                f"consumption. Please verify the actual PowerOnTime, PowerOffTime, and HeatTime in EAF_Per_Heat for HeatID {heat_id}."
            ),
            "ProblemCategory": "PRODUCTION_STATE",
            "SourceSystem": "Xbatch",
            "ConversationSummary": f"User is questioning electrical consumption and power timing for Heat {heat_id}.",
            "SuspectedCause": f"Check dbo.EAF_Per_Heat for HeatID = {heat_id} and compare PowerOnTime/PowerOffTime.",
            "ExtractedEntitiesJson": {"HeatNo": heat_id, "Area": "EAF"},
        })

    # Category 2: LRF Refining & Arcing (8 tickets)
    for idx, h in enumerate(entities.get("lrf_heats", [])[offset:end]):
        heat_id = h["HeatID"]
        tickets.append({
            "AreaID": AREA_LRF,
            "ComplaintTypeID": COMPLAINT_TYPE_CLARIFICATION if idx % 2 == 0 else COMPLAINT_TYPE_BUG,
            "Priority": PRIORITY_CRITICAL,
            "BriefDetails": f"LRF Arcing time inquiry for Heat {heat_id} in treatment log",
            "Description": (
                f"Operator logged ArcingTime of {h['ArcingTime']} min for Heat {heat_id} in the secondary metallurgy station. "
                f"Quality team wants to confirm whether PowerONTime ({h['PowerONTime']}) and PowerOFFTime ({h['PowerOFFTime']}) "
                f"match the recorded arcing duration in the LRF database. Please verify LRF_Per_Heat for HeatID {heat_id}."
            ),
            "ProblemCategory": "DATA_LOOKUP",
            "SourceSystem": "Xbatch",
            "ConversationSummary": f"User needs verification of LRF arcing and treatment duration for Heat {heat_id}.",
            "SuspectedCause": f"Check dbo.LRF_Per_Heat for HeatID = {heat_id} (read ArcingTime, PowerONTime, PowerOFFTime).",
            "ExtractedEntitiesJson": {"HeatNo": heat_id, "Area": "LRF"},
        })

    # Category 3: CCM Casting & Billet Genealogy (8 tickets)
    for idx, b in enumerate(entities.get("ccm_billets", [])[offset:end]):
        billet_no = b["BilletNo"]
        heat_no = b["HeatNo"]
        strand = b["StrandNo"]
        tickets.append({
            "AreaID": AREA_CCM,
            "ComplaintTypeID": COMPLAINT_TYPE_BUG,
            "Priority": PRIORITY_CRITICAL,
            "BriefDetails": f"Billet genealogy confirmation for Billet {billet_no} on Strand {strand}",
            "Description": (
                f"Casting sequence for Heat {heat_no} shows Billet {billet_no} on Strand {strand} with CutStartTime "
                f"{b['CutStartTime']}. Yard supervisor reported a mismatch between the cutting torch trigger time and "
                f"the recorded genealogy record. Please confirm whether Billet {billet_no} exists with valid CutStartTime in XMES_CCM_Billet_Genealogy_Trn_Tbl."
            ),
            "ProblemCategory": "PRODUCTION_STATE",
            "SourceSystem": "Xbatch",
            "ConversationSummary": f"User is checking whether Billet {billet_no} genealogy is properly recorded on Strand {strand}.",
            "SuspectedCause": f"Check dbo.XMES_CCM_Billet_Genealogy_Trn_Tbl for BilletNo = '{billet_no}' and HeatNo = '{heat_no}'.",
            "ExtractedEntitiesJson": {"BilletNo": billet_no, "HeatNo": heat_no, "Area": "CCM"},
        })

    # Category 4: SAP Production Posting & Goods Movement (8 tickets)
    for idx, s in enumerate(entities.get("sap_postings", [])[offset:end]):
        heat_no = s["HeatNo"]
        wo = s["WorkOrder"]
        mat_doc = s["MaterialDoc"]

        tickets.append({
            "AreaID": AREA_COMMON,
            "ComplaintTypeID": COMPLAINT_TYPE_BUG if idx % 2 == 0 else COMPLAINT_TYPE_CLARIFICATION,
            "Priority": PRIORITY_CRITICAL,
            "BriefDetails": f"Material Document {mat_doc} posting status for Heat {heat_no} / WO {wo}",
            "Description": (
                f"Production goods movement for Heat {heat_no} (Work Order {wo}) shows Material Document {mat_doc}. "
                f"Finance reports that inventory balance does not reflect this material document in ERP. "
                f"Please verify whether MaterialDocument {mat_doc} is recorded in MES_SAP_Production_Trn_Tbl for HeatNo {heat_no}."
            ),
            "ProblemCategory": "SAP_INTEGRATION",
            "SourceSystem": "Xbatch",
            "ConversationSummary": f"User needs confirmation of Material Document {mat_doc} for Heat {heat_no} and WO {wo}.",
            "SuspectedCause": f"Check dbo.MES_SAP_Production_Trn_Tbl for MaterialDocument = '{mat_doc}' and HeatNo = '{heat_no}'.",
            "ExtractedEntitiesJson": {"HeatNo": heat_no, "WorkOrder": wo, "MaterialDocument": mat_doc},
        })

    # Category 5: Work Order Lifecycle & Progress (8 tickets)
    for idx, w in enumerate(entities.get("work_orders", [])[offset:end]):
        wo_num = w["WorkOrderNumber"]
        qty = w["Quantity"]
        status = w["Status"]
        tickets.append({
            "AreaID": AREA_COMMON,
            "ComplaintTypeID": COMPLAINT_TYPE_CLARIFICATION if idx % 2 == 0 else COMPLAINT_TYPE_BUG,
            "Priority": PRIORITY_CRITICAL,
            "BriefDetails": f"Work Order {wo_num} current status and target quantity query",
            "Description": (
                f"Production scheduling dashboard displays Work Order {wo_num} with target quantity {qty} tons and status '{status}'. "
                f"Mill planner needs confirmation whether this work order is still active or completed in the MES master table. "
                f"Please verify the recorded Status and Quantity in XBatch_Work_Order_Mst_Tbl for WorkOrderNumber {wo_num}."
            ),
            "ProblemCategory": "WORK_ORDER",
            "SourceSystem": "Xbatch",
            "ConversationSummary": f"User wants to confirm the status and quantity for Work Order {wo_num}.",
            "SuspectedCause": f"Check dbo.XBatch_Work_Order_Mst_Tbl for WorkOrderNumber = '{wo_num}'.",
            "ExtractedEntitiesJson": {"WorkOrder": wo_num},
        })

    # Category 6: Plant Stoppages & Delays (8 tickets)
    for idx, d in enumerate(entities.get("delays", [])[offset:end]):
        heat_no = d["HeatNo"]
        reason = d["Status"]
        start_time = d["StartTime"]
        tickets.append({
            "AreaID": AREA_ROLLING if idx % 2 == 0 else AREA_EAF,
            "ComplaintTypeID": COMPLAINT_TYPE_CLARIFICATION,
            "Priority": PRIORITY_CRITICAL,
            "BriefDetails": f"Delay inquiry: {reason} recorded on Heat {heat_no}",
            "Description": (
                f"OEE tracking recorded a stoppage '{reason}' on Heat {heat_no} starting at {start_time}. "
                f"Shift superintendent wants to verify if the delay record has been formally completed and if "
                f"the StartTime and EndTime are properly stored in Delay_Trn_Tbl for HeatNo {heat_no}."
            ),
            "ProblemCategory": "PERFORMANCE",
            "SourceSystem": "Xbatch",
            "ConversationSummary": f"User requests verification of delay '{reason}' logged on Heat {heat_no}.",
            "SuspectedCause": f"Check dbo.Delay_Trn_Tbl for HeatNo = '{heat_no}' and Status = '{reason}'.",
            "ExtractedEntitiesJson": {"HeatNo": heat_no},
        })

    # Category 7: Quality Chemistry & Spectro Analysis (8 tickets)
    for idx, c in enumerate(entities.get("chemistry", [])[offset:end]):
        heat_no = c["HeatNo"]
        sample_type = c["SampleType"]
        grade = c["Grade"]
        c_val = c["C"]
        si_val = c["Si"]
        tickets.append({
            "AreaID": AREA_COMMON,
            "ComplaintTypeID": COMPLAINT_TYPE_BUG if idx % 2 == 0 else COMPLAINT_TYPE_CLARIFICATION,
            "Priority": PRIORITY_CRITICAL,
            "BriefDetails": f"Chemical composition verification for Heat {heat_no} ({sample_type} sample)",
            "Description": (
                f"Quality assurance lab reported chemistry for Heat {heat_no} (Grade {grade}, SampleType {sample_type}) "
                f"showing Carbon={c_val} and Silicon={si_val}. Meltshop metallurgical engineer wants to verify whether "
                f"these values match the official recorded values in Heat_Chemistry_Quality_Data for HeatNo {heat_no}."
            ),
            "ProblemCategory": "QUALITY",
            "SourceSystem": "Xbatch",
            "ConversationSummary": f"User wants to verify Carbon and Silicon spectro results for Heat {heat_no}.",
            "SuspectedCause": f"Check dbo.Heat_Chemistry_Quality_Data for HeatNo = '{heat_no}' and SampleType = '{sample_type}'.",
            "ExtractedEntitiesJson": {"HeatNo": heat_no},
        })

    # Category 8: Genuine EAF data-quality defects (real anomalies, not verification asks).
    # Unlike the categories above, these report a symptom that IS actually present in
    # live data -- there is a real root cause to find, not just a value to confirm.
    for heat_id in entities.get("eaf_malformed_timing", [])[:2]:
        tickets.append({
            "AreaID": AREA_EAF,
            "ComplaintTypeID": COMPLAINT_TYPE_BUG,
            "Priority": PRIORITY_CRITICAL,
            "BriefDetails": f"EAF power timing missing/unreadable for Heat {heat_id}",
            "Description": (
                f"Shift report for Heat {heat_id} could not calculate total heat time -- the power timing fields "
                f"appear blank or unreadable in the system. Please investigate why PowerOnTime/PowerOffTime/HeatTime "
                f"are not properly recorded in EAF_Per_Heat for HeatID {heat_id} and identify the root cause."
            ),
            "ProblemCategory": "PRODUCTION_STATE",
            "SourceSystem": "Xbatch",
            "ConversationSummary": f"User reports missing/unreadable power timing data for Heat {heat_id}.",
            "SuspectedCause": f"Check dbo.EAF_Per_Heat for HeatID = {heat_id}; PowerOnTime/PowerOffTime may be malformed placeholders.",
            "ExtractedEntitiesJson": {"HeatNo": heat_id, "Area": "EAF"},
        })
    for m in entities.get("eaf_timing_mismatch", [])[:2]:
        heat_id = m["HeatID"]
        tickets.append({
            "AreaID": AREA_EAF,
            "ComplaintTypeID": COMPLAINT_TYPE_BUG,
            "Priority": PRIORITY_CRITICAL,
            "BriefDetails": f"EAF recorded HeatTime does not add up for Heat {heat_id}",
            "Description": (
                f"Energy audit for Heat {heat_id} found PowerOnTime={m['PowerOnMin']}min and "
                f"PowerOffTime={m['PowerOffMin']}min recorded in EAF_Per_Heat, but the stored HeatTime is only "
                f"{m['HeatTimeMin']}min -- these numbers do not add up to a consistent total. Please investigate "
                f"whether this is a unit/logging error and identify the root cause."
            ),
            "ProblemCategory": "PRODUCTION_STATE",
            "SourceSystem": "Xbatch",
            "ConversationSummary": f"User reports HeatTime does not reconcile with PowerOnTime+PowerOffTime for Heat {heat_id}.",
            "SuspectedCause": f"Check dbo.EAF_Per_Heat for HeatID = {heat_id}; compare PowerOnTimeMinute+PowerOFFTimeMinute against HeatTimeMinute.",
            "ExtractedEntitiesJson": {"HeatNo": heat_id, "Area": "EAF"},
        })

    return tickets


REQUESTERS = [
    ("Krishna Penta", "98805104", "krishna.penta@jindalshadeed.com"),
    ("Ahmed Al Balushi", "91234567", "ahmed.balushi@jindalshadeed.com"),
    ("Fatima Al Hinai", "92345678", "fatima.hinai@jindalshadeed.com"),
    ("Ravi Shankar", "93456789", "ravi.shankar@jindalshadeed.com"),
    ("Salim Al Rawahi", "94567890", "salim.rawahi@jindalshadeed.com"),
]
# Where the expected outcome of each human-style ticket is recorded. Never written to the
# ticket itself, so the pipeline cannot read the answer.
EXPECTATIONS_PATH = Path(__file__).resolve().parent / "seeded_ticket_expectations.jsonl"


def _nudge(value: str, rng) -> str:
    """A plausible misremembered number: same format, a small but real difference."""
    try:
        number = float(value)
    except (TypeError, ValueError):
        return value
    step = rng.choice([-3, -2, 2, 3])
    return str(int(number) + step) if number == int(number) else f"{number + step / 100:.4f}"


def _human_case(i: int) -> str:
    """Rotate cases so every category gets a correct report, a wrong one, and a vague one."""
    return ("MATCH", "MISMATCH", "MISSING_ID", "MATCH", "VAGUE")[i % 5]


def generate_human_tickets(entities: dict, offset: int = 0, seed: int = 7) -> list[dict]:
    """Tickets written the way plant users write them (see Dummy_L2_Tickets.xlsx): symptom first,
    the screen or report they looked at, abbreviations, no table/column names, and none of the
    L1-extracted fields (category, suspected cause, entities) a raw ticket would not have.
    """
    import random
    rng = random.Random(seed + offset)
    out: list[dict] = []
    end = offset + 3

    def add(area, kind, brief, text, case, expect, facts):
        who = rng.choice(REQUESTERS)
        out.append({"AreaID": area, "ComplaintTypeID": kind, "Priority": PRIORITY_HIGH,
                    "BriefDetails": brief, "Description": text, "Requester": who,
                    "Expectation": {"case": case, "expected": expect, "facts": facts}})

    for i, h in enumerate(entities.get("lrf_heats", [])[offset:end]):
        case = _human_case(i)
        arc = h["ArcingTime"].split(".")[0]
        said = arc if case == "MATCH" else _nudge(arc, rng)
        if case == "MISSING_ID":
            add(AREA_LRF, COMPLAINT_TYPE_CLARIFICATION, "LRF arc time looks off",
                f"arcing time on the LRF shift report for one of last night's heats shows {said} min, "
                "operator says it ran longer. can someone check?", case, "QUESTION", {})
        else:
            add(AREA_LRF, COMPLAINT_TYPE_BUG, f"Arc time ht {h['HeatID']} not matching",
                f"LRF report says arcing {said} min for heat {h['HeatID']}. We noted power on at "
                f"{h['PowerONTime'].split('.')[0]} and off at {h['PowerOFFTime'].split('.')[0]}. "
                "Which one is correct? Quality is asking.",
                case, "CONFIRMED" if case == "MATCH" else "CORRECTED", {"ArcingTime": arc})

    for i, h in enumerate(entities.get("eaf_heats", [])[offset:end]):
        case = _human_case(i + 1)
        pon = h["PowerOnTime"]
        said = pon if case == "MATCH" else _nudge(pon.split(":")[0], rng) + ":" + pon.split(":")[-1]
        if case == "VAGUE":
            add(AREA_EAF, COMPLAINT_TYPE_BUG, "Power on times wrong in EAF report",
                "EAF heat report power on times look wrong since morning shift, some heats are too "
                "high. Kindly check.", case, "L3_ESCALATION", {})
        else:
            add(AREA_EAF, COMPLAINT_TYPE_CLARIFICATION, f"Power on time for {h['HeatID']}?",
                f"Hi, for heat {h['HeatID']} the energy dashboard shows high consumption. Shift log "
                f"has power on {said}. Is that what the system recorded?",
                case, "CONFIRMED" if case == "MATCH" else "CORRECTED", {"PowerOnTime": pon})

    for i, b in enumerate(entities.get("ccm_billets", [])[offset:end]):
        case = _human_case(i + 2)
        if case == "MISSING_ID":
            add(AREA_CCM, COMPLAINT_TYPE_BUG, "Billet missing in genealogy",
                f"one billet from strand {b['StrandNo']} is not showing in the genealogy screen, yard "
                "can see it physically. Please check urgently.", case, "QUESTION", {})
        else:
            add(AREA_CCM, COMPLAINT_TYPE_BUG, f"Billet {b['BilletNo']} genealogy",
                f"Yard says billet {b['BilletNo']} was cut around {str(b['CutStartTime'])[:16]} but "
                "the torch timing doesnt look right to them. Can you confirm the cut time the system has?",
                case, "CONFIRMED", {"CutStartTime": str(b["CutStartTime"])})

    for i, w in enumerate(entities.get("work_orders", [])[offset:end]):
        case = _human_case(i + 3)
        qty = str(w["Quantity"]).split(".")[0]
        said = qty if case == "MATCH" else _nudge(qty, rng)
        add(AREA_COMMON, COMPLAINT_TYPE_CLARIFICATION, f"WO {w['WorkOrderNumber']} status??",
            f"Planning screen shows WO {w['WorkOrderNumber']} with {said} t. Is this order still open "
            "or closed? Need to plan the next campaign.",
            case, "CONFIRMED" if case == "MATCH" else "CORRECTED", {"Quantity": qty, "Status": w["Status"]})

    for i, s in enumerate(entities.get("sap_postings", [])[offset:end]):
        add(AREA_COMMON, COMPLAINT_TYPE_BUG, f"SAP posting not reflecting - heat {s['HeatNo']} / doc {s['MaterialDoc'][-4:]}",
            f"Finance says production for heat {s['HeatNo']} is not showing in SAP stock. Mat doc on our "
            f"side is {s['MaterialDoc']}. Did it post or not?",
            "MATCH", "ANSWERED", {"MaterialDocument": s["MaterialDoc"]})
    return out


def _insert_human_ticket(cur, new_id: str, ticket_no: str, t: dict, offset_minutes: int) -> None:
    """A raw user ticket: only what the requester typed; L1-extracted fields stay NULL."""
    name, phone, email = t["Requester"]
    cur.execute(
        """
        INSERT INTO Complaint_Mst_Tbl (
            ID, AreaID, CreatedBy, CreatedOn, ModifiedOn, IsDeleted, IsSystem, Source, ComplaintTypeID,
            Description, BriefDetails, Status, TicketNo, Priority, FirstLastName, ContactNo, EmailID,
            messages, AskStatus, SourceSystem
        ) VALUES (?, ?, NULL, DATEADD(MINUTE, ?, GETDATE()), DATEADD(MINUTE, ?, GETDATE()), 0, 0, 'T-SQL', ?,
                  ?, ?, 'Enter', ?, ?, ?, ?, ?, 'Enter', 'Enter', 'Xbatch')
        """,
        new_id, t["AreaID"], offset_minutes, offset_minutes, t["ComplaintTypeID"],
        t["Description"], t["BriefDetails"], ticket_no, t["Priority"], name, phone, email,
    )
    with EXPECTATIONS_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps({"ticket_no": ticket_no, "ticket_id": new_id, **t["Expectation"]}) + "\n")


def next_ticket_no(cur) -> int:
    cur.execute("SELECT MAX(CAST(REPLACE(TicketNo,'Ticket_','') AS INT)) FROM Complaint_Mst_Tbl WHERE TicketNo LIKE 'Ticket_%'")
    return (cur.fetchone()[0] or 0) + 1


def existing_brief_details(cur) -> set:
    cur.execute("SELECT BriefDetails FROM Complaint_Mst_Tbl WHERE ISNULL(IsDeleted, 0) = 0")
    return {row[0] for row in cur.fetchall() if row[0]}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--server", default="10.2.6.204")
    ap.add_argument("--database", default="XStudio_Helpdesk")
    ap.add_argument("--xbatch-db", default="XStudio_Xbatch")
    ap.add_argument("--username", default="sa")
    ap.add_argument("--password", default=os.environ.get("MSSQL_MCP_PASSWORD"))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--style", choices=["template", "human"], default="template",
                    help="human: tickets written the way plant users write them, with expected outcomes recorded aside.")
    ap.add_argument("--offset", type=int, default=0,
                     help="Skip the first N real entities per category (each entity list "
                          "fetches TOP 10) so a re-run produces different real tickets instead "
                          "of the same deterministic top-3 every time. Existing-title dedup still "
                          "applies as a safety net regardless of offset.")
    args = ap.parse_args()

    print(f"Connecting to {args.server} (DB: {args.xbatch_db} for entities, {args.database} for tickets)...")
    conn_xbatch = build_connection(args.server, args.xbatch_db, args.username, args.password)
    try:
        entities = load_real_entities(conn_xbatch)
    finally:
        conn_xbatch.close()

    human = args.style == "human"
    tickets = generate_human_tickets(entities, offset=args.offset) if human else generate_tickets(entities, offset=args.offset)
    print(f"Generated {len(tickets)} {args.style}-style tickets using real plant entities.")

    conn_hd = build_connection(args.server, args.database, args.username, args.password)
    try:
        cur = conn_hd.cursor()
        ticket_no = next_ticket_no(cur)
        already_seeded = existing_brief_details(cur)

        created = 0
        for t in tickets:
            if t["BriefDetails"] in already_seeded:
                print(f"Skipping (already exists): {t['BriefDetails']}")
                continue

            new_id = str(uuid.uuid4()).upper()
            new_ticket_no = f"Ticket_{ticket_no}"
            entities_json = json.dumps(t.get("ExtractedEntitiesJson"))
            # Stagger creation time so this batch doesn't look like a single-instant
            # synthetic dump the way the prior seed run did (all 56 within 7 seconds).
            offset_minutes = created * 7

            print(f"{'[DRY RUN] ' if args.dry_run else ''}Creating {new_ticket_no} (Priority={t['Priority']}): {t['BriefDetails']}")
            if human:
                if args.dry_run:
                    print(f"    {t['Description']}\n    expect {t['Expectation']['expected']}")
                else:
                    _insert_human_ticket(cur, new_id, new_ticket_no, t, offset_minutes)
                ticket_no += 1
                created += 1
                continue
            if not args.dry_run:
                cur.execute(
                    """
                    INSERT INTO Complaint_Mst_Tbl (
                        ID, AreaID, CreatedBy, CreatedOn, ModifiedOn, IsDeleted, IsSystem,
                        Source, ComplaintTypeID, Description, BriefDetails, Status, TicketNo,
                        Priority, FirstLastName, ContactNo, EmailID, messages, AskStatus,
                        ProblemCategory, SourceSystem, ConversationSummary, SuspectedCause,
                        ExtractedEntitiesJson
                    ) VALUES (
                        ?, ?, NULL, DATEADD(MINUTE, ?, GETDATE()), DATEADD(MINUTE, ?, GETDATE()), 0, 0,
                        'T-SQL', ?, ?, ?, 'Enter', ?,
                        ?, 'Real Plant Ticket Test', '90000010', 'planttest@example.com', 'Enter', 'Enter',
                        ?, ?, ?, ?,
                        ?
                    )
                    """,
                    new_id, t["AreaID"], offset_minutes, offset_minutes, t["ComplaintTypeID"], t["Description"], t["BriefDetails"], new_ticket_no,
                    t["Priority"], t["ProblemCategory"], t["SourceSystem"], t["ConversationSummary"],
                    t["SuspectedCause"], entities_json,
                )
            ticket_no += 1
            created += 1

        if not args.dry_run:
            conn_hd.commit()
            print(f"\nSuccessfully created {created} real plant ticket(s) (skipped {len(tickets) - created} existing).")
        else:
            print(f"\n[DRY RUN] Would create {created} ticket(s) (would skip {len(tickets) - created} existing).")
    finally:
        conn_hd.close()


if __name__ == "__main__":
    main()
