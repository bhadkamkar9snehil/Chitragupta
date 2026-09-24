#!/usr/bin/env python3
"""Build the live test set (e2e/live_cases.jsonl) from REAL XBatch faults, values and gaps.

Every ticket describes something that is actually in the data, phrased the way plant users write
(abbreviations, no table names). Each case records the right outcome and, where the reply must
contain a specific fact, `must_say`. Seed with: python Model_Bench/seed_real_xbatch_tickets.py --style live

    python Model_Bench/e2e/make_live_cases.py
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

import pyodbc

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from build_process_world import connect  # noqa: E402

DATA = {"data": True}
cases: list[dict] = []


def add(case_id: str, text: str, truth: str, expect: dict) -> None:
    cases.append({"id": case_id, "text": text, "truth": truth, "expect": expect})


def msg(value) -> str:
    return re.sub(r"(?s).*Response Error Message:", "", str(value or "")).strip()


def rows(cur, sql: str) -> list:
    cur.execute(sql)
    return cur.fetchall()


def sap_errors(cur) -> None:
    """One ticket per distinct kind of SAP rejection: the reply must quote the recorded cause."""
    gm = rows(cur, """SELECT Batch, MovementType, CONVERT(varchar(max), ErrorMessage) m FROM XMES_SAP_API_GoodsMovement_Error
                      WHERE ErrorMessage IS NOT NULL ORDER BY EntryDateTime DESC""")
    kinds = [("order_status", "does not allow goods receipt",
              "GR not happening for heat {h}, SAP says something about order status. pls check from xbatch side"),
             ("stock_deficit", "Deficit of BA",
              "Heat {h} production is not showing in SAP stock, stores team is asking. what happened?"),
             ("qty_exceeded", "Order quantity exceeded",
              "billets of heat {h} not posted to SAP, planning says order may be full. can you confirm"),
             ("order_locked", "already being processed",
              "production posting failed for {h}, error popup came in xbatch. please check urgently"),
             ("empty_quantity_261", "QuantityInEntryUnit",
              "consumption of heat {h} not reflecting in SAP, material still showing in stock")]
    for kind, needle, template in kinds:
        hit = next((r for r in gm if needle in msg(r.m) and (kind != "empty_quantity_261" or str(r.MovementType) == "261")), None)
        if hit:
            heat = str(hit.Batch).split("_")[0]
            add(f"sap_gm_{kind}", template.format(h=heat), msg(hit.m)[:200],
                {**DATA, "must_say": [needle], "outcome": "NEEDS_HUMAN_ACTION"})
    ud = rows(cur, "SELECT HeatNo, CONVERT(varchar(max), ErrorMessage) m FROM XMES_SAP_API_UsageDecision_Error ORDER BY EntryDateTime DESC")
    for kind, needle, template in [("access", "is not allowed", "QC cannot close UD for heat {h} from xbatch, some error. dispatch waiting"),
                                   ("locked", "already locked", "UD for {h} did not post to SAP. somebody told batch is locked?")]:
        hit = next((r for r in ud if needle in msg(r.m)), None)
        if hit:
            add(f"sap_ud_{kind}", template.format(h=hit.HeatNo), msg(hit.m)[:200],
                {**DATA, "must_say": [needle], "outcome": "NEEDS_HUMAN_ACTION"})
    rr = rows(cur, "SELECT HeatNo, CONVERT(varchar(max), ErrorMessage) m FROM XMES_SAP_API_ResultRecording_Error ORDER BY EntryDateTime DESC")
    for kind, needle, template in [("blocked", "already blocked by user", "chemistry results of heat {h} not going to SAP, lab entered them yesterday"),
                                   ("insplot_status", "not allowed in view of inspLot status", "result recording failing for {h}, QC says values are ok in xbatch")]:
        hit = next((r for r in rr if needle in msg(r.m)), None)
        if hit:
            add(f"sap_rr_{kind}", template.format(h=hit.HeatNo), msg(hit.m)[:200],
                {**DATA, "must_say": [needle], "outcome": "NEEDS_HUMAN_ACTION"})
    p2p = rows(cur, "SELECT BatchNo, CONVERT(varchar(max), ErrorMessage) m FROM XMES_SAP_API_PlantToPlantTransfer_Error ORDER BY EntryDateTime DESC")
    for kind, needle, template in [("deficit", "Deficit of BA", "billet transfer of heat {h} to rolling mill failed in SAP"),
                                   ("not_in_plant", "not maintained in plant", "plant to plant transfer error for batch of heat {h}, rm cannot receive billets"),
                                   ("no_batch", "does not exist", "transfer of {h} billets stuck, SAP says batch problem")]:
        hit = next((r for r in p2p if needle in msg(r.m)), None)
        if hit:
            add(f"sap_p2p_{kind}", template.format(h=str(hit.BatchNo).split("_")[0]), msg(hit.m)[:200],
                {**DATA, "must_say": [needle], "outcome": "NEEDS_HUMAN_ACTION"})


def counts_and_values(cur) -> None:
    gaps = rows(cur, """SELECT TOP 2 c.HeatID h, CONVERT(int, c.TotalBilletsCount) ccm,
                              (SELECT COUNT(*) FROM XMES_CCM_Billet_Genealogy_Trn_Tbl g WHERE g.HeatNo = c.HeatID) gen
                       FROM CCM_Per_Heat c WHERE c.TotalBilletsCount IS NOT NULL AND CONVERT(int, c.TotalBilletsCount) <>
                             (SELECT COUNT(*) FROM XMES_CCM_Billet_Genealogy_Trn_Tbl g WHERE g.HeatNo = c.HeatID)
                       ORDER BY c.HeatID DESC""")
    for i, g in enumerate(gaps):
        text = (f"CCM heat report shows {g.ccm} billets for heat {g.h} but in billet tracking I can count only {g.gen}. which one correct"
                if i == 0 else f"heat {g.h}: {g.gen} billets in genealogy screen but CCM report says {g.ccm}??")
        add(f"billet_gap_{g.h}", text, f"CCM_Per_Heat.TotalBilletsCount {g.ccm} vs {g.gen} genealogy rows", {**DATA})
    eaf = rows(cur, "SELECT TOP 2 HeatID, PowerOnTime, OxygenConsumption FROM EAF_PER_HEAT WHERE PowerOnTime IS NOT NULL AND OxygenConsumption > 0 ORDER BY HeatID DESC")
    lrf = rows(cur, "SELECT TOP 2 HeatID, ArcingTime, LRFTemperature FROM LRF_Per_Heat WHERE ArcingTime > 0 AND LRFTemperature > 0 ORDER BY HeatID DESC")
    if eaf:
        a = eaf[0]
        add("value_confirm_eaf_power", f"EAF report shows power on time {a.PowerOnTime} for heat {a.HeatID}. is that correct in system?",
            f"EAF_PER_HEAT.PowerOnTime = {a.PowerOnTime}", {**DATA, "must_say": [str(a.PowerOnTime)], "outcome": "RESOLUTION"})
    if len(eaf) > 1:
        b, wrong = eaf[1], int(float(eaf[1].OxygenConsumption)) + 350
        add("value_correct_eaf_oxygen", f"oxygen for heat {b.HeatID} is showing {wrong} Nm3 in our excel, xbatch value looks different. which is right",
            f"EAF_PER_HEAT.OxygenConsumption = {float(b.OxygenConsumption):g}",
            {**DATA, "must_say": [f"{float(b.OxygenConsumption):g}"], "outcome": "RESOLUTION"})
    if lrf:
        c = lrf[0]
        add("value_correct_lrf_arcing", f"LRF arcing time for heat {c.HeatID} shows {int(float(c.ArcingTime)) + 6} min on the shift report, operator says less. check pls",
            f"LRF_Per_Heat.ArcingTime = {float(c.ArcingTime):g}", {**DATA, "must_say": [f"{float(c.ArcingTime):g}"], "outcome": "RESOLUTION"})
    if len(lrf) > 1:
        d = lrf[1]
        add("value_confirm_lrf_temp", f"what is the final LRF temperature recorded for heat {d.HeatID}?",
            f"LRF_Per_Heat.LRFTemperature = {float(d.LRFTemperature):g}", {**DATA, "must_say": [f"{float(d.LRFTemperature):g}"], "outcome": "RESOLUTION"})


def no_identifier(cur) -> None:
    last = {t: str(rows(cur, f"SELECT CONVERT(date, MAX(CreatedOn)) FROM dbo.[{t}]")[0][0])
            for t in ("LRF_Per_Heat", "EAF_PER_HEAT", "ShiftDelayEntry", "XMES_SAP_API_GoodsMovement_Error")}
    add("feed_lrf_stopped", "LRF heats not showing in xbatch after 8th July evening. EAF heats are still coming. please check urgently",
        f"LRF_Per_Heat last rows {last['LRF_Per_Heat']}, EAF_PER_HEAT continues to {last['EAF_PER_HEAT']}",
        {**DATA, "must_say": [last["LRF_Per_Heat"]]})
    add("delay_report_empty", "shift delay report is not showing the delays we entered last night",
        f"ShiftDelayEntry has no rows after {last['ShiftDelayEntry']}", {**DATA, "must_say": [last["ShiftDelayEntry"]]})
    add("sap_gr_error_wave", "lot of SAP goods receipt errors this week, stores team cannot see our production in SAP",
        f"goods movement errors stop at {last['XMES_SAP_API_GoodsMovement_Error']}", {**DATA})
    add("screen_charging_bed", "billets lying on the charging bed are not showing on the charging bed screen, operator can see them physically",
        "the charging bed list view shows only Status='Entered'", {**DATA, "must_say": ["Entered"]})
    add("screen_consumed_items", "Consumed Item screen not showing consumption from last month, only few days are visible",
        "the Consumed Item list view shows only the last 7 days (CreatedOn >= today-7)", {**DATA, "must_say": ["7"]})
    add("master_grade_missing", "new grade B500SX is not coming in the grade dropdown when we create work order",
        "B500SX is not in Grade_Master / Steel_Grade_Master: master data to be created", {**DATA, "must_say": ["B500SX"]})


def not_found_and_routes() -> None:
    add("not_found_heat", "heat 1699999 not coming in any report since morning", "heat 1699999 is not in XBatch", {"none": True})
    add("not_found_wo", "WO 120000999999 is not visible on planning screen, please add", "work order 120000999999 is not in XBatch", {"none": True})
    for case_id, text, route in [
            ("howto_add_user", "how do I add a new operator user in xbatch", "how_to"),
            ("howto_reprint_card", "how to reprint the heat card? printer jammed during night shift", "how_to"),
            ("access_login", "cannot login to xbatch after my password was changed, it says invalid user", "access"),
            ("infra_slow", "xbatch is very slow on all screens since morning shift", "infrastructure"),
            ("hardware_scanner", "barcode scanner at billet yard is not reading tags since today", "hardware"),
            ("change_new_report", "we need a new report for daily ladle life summary, can you add it in xbatch", "change_request")]:
        add(case_id, text, route, {"data": False, "route": route})


def main() -> int:
    cur = connect().cursor()
    sap_errors(cur)
    counts_and_values(cur)
    no_identifier(cur)
    not_found_and_routes()
    out = HERE / "live_cases.jsonl"
    out.write_text("".join(json.dumps(c) + "\n" for c in cases), encoding="utf-8")
    kinds: dict[str, int] = {}
    for c in cases:
        kinds[c["id"].split("_")[0]] = kinds.get(c["id"].split("_")[0], 0) + 1
    print(f"{len(cases)} cases -> {out}: {kinds}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
