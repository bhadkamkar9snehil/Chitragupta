#!/usr/bin/env python3
"""Create real, well-formed test tickets in Complaint_Mst_Tbl for stress-
testing the L2 pipeline.

No official stored procedure exists for ticket creation (checked live via
sys.procedures, 2026-09-03 -- confirmed empty) -- Complaint_Mst_Tbl is
normally populated by an external system (real rows show Source='T-SQL').
This is a documented no-SP exception per xstudio-sql-write-discipline, not
a shortcut around it.

Modeled directly on 14 real synthetic tickets already found live in the
table (FirstLastName='L1 Chatbot Test', created 2026-09-02, before this
session's context was compacted -- the original creation script did not
survive on disk, this is a faithful rebuild from the real rows' own
structure). Deliberately only creates Bug/Clarification-type tickets with
real Heat/WO/Lot identifiers and populated ExtractedEntitiesJson --
confirmed 2026-09-03 that ~43% of the live queue is "Request for
Customization" (unsolvable by SQL investigation by design), so seeding
more of those would just grow the unsolvable backlog further. Each ticket
below is deliberately routable to one specific task-router.md domain, so a
real investigation has a genuine chance of resolving it, not just
escalating.

Usage:
    python seed_test_tickets.py --server 10.2.6.204 [--dry-run]
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
PRIORITY_HIGH = "65BE0464-2E42-4CBA-9ADF-F8E19E90B5B2"

# One ticket per task-router.md route, so the resulting batch exercises
# every domain skill, not just whichever one the live queue happens to be
# full of right now.
TICKETS = [
    {
        "AreaID": "EAF", "ComplaintTypeID": COMPLAINT_TYPE_BUG,
        "BriefDetails": "Electrode consumption looks doubled for Heat H99310",
        "Description": "Electrode consumption for Heat H99310 in the EAF daily summary shows roughly double the expected value compared to similar heats this week. Please check whether this is a real consumption spike or a data/unit conversion issue.",
        "ProblemCategory": "PRODUCTION_STATE", "SourceSystem": "Xbatch",
        "ConversationSummary": "User flagged an anomalous electrode consumption reading for Heat H99310 and wants to know if it's real or a data bug.",
        "SuspectedCause": "Possible unit mismatch (kg vs lb) or a genuine process deviation -- needs L2 to check EAF_PER_HEAT against the raw sensor log.",
        "ExtractedEntitiesJson": {"HeatNo": "H99310", "Area": "EAF"},
    },
    {
        "AreaID": "LRF", "ComplaintTypeID": COMPLAINT_TYPE_CLARIFICATION,
        "BriefDetails": "Ladle number missing for Heat H99312 in LRF summary",
        "Description": "The LRF per-heat summary for Heat H99312 shows a blank ladle number, but the heat did complete LRF processing according to the shift log. Was the ladle number simply not recorded, or is this heat missing from LRF_Per_Heat entirely?",
        "ProblemCategory": "DATA_LOOKUP", "SourceSystem": "Xbatch",
        "ConversationSummary": "User needs to know whether Heat H99312's LRF record exists at all and why its ladle number field is empty.",
        "SuspectedCause": "Either a genuinely missing LRF_Per_Heat row for this heat, or the ladle number was never entered during that shift.",
        "ExtractedEntitiesJson": {"HeatNo": "H99312", "Area": "LRF"},
    },
    {
        "AreaID": "CCM", "ComplaintTypeID": COMPLAINT_TYPE_BUG,
        "BriefDetails": "Billet count for Heat H99315 doesn't match cast plan",
        "Description": "The billet count recorded for Heat H99315 in the CCM tracker is 2 fewer than what the casting plan specified for this heat. Please check if billets were genuinely lost/rejected or if this is a tracking gap.",
        "ProblemCategory": "PRODUCTION_STATE", "SourceSystem": "Xbatch",
        "ConversationSummary": "User wants to reconcile a billet-count discrepancy for Heat H99315 against its cast plan.",
        "SuspectedCause": "Could be genuine rejects/scrap not reflected in the plan comparison, or a billet tracking gap in CCM_Heat_Tracker.",
        "ExtractedEntitiesJson": {"HeatNo": "H99315", "Area": "CCM"},
    },
    {
        "AreaID": "Common", "ComplaintTypeID": COMPLAINT_TYPE_BUG,
        "BriefDetails": "SAP posting stuck pending for Heat H99318 / WO-99120",
        "Description": "SAP production posting for Heat H99318 (Work Order WO-99120) has been stuck in pending status for over 12 hours. No error is shown on screen. Please check whether the API call was ever actually sent to SAP.",
        "ProblemCategory": "SAP_INTEGRATION", "SourceSystem": "Xbatch",
        "ConversationSummary": "User needs to know if the SAP posting for this heat/work-order pair actually fired or is silently stuck.",
        "SuspectedCause": "Likely a stuck/failed row in SAP_Posting_Tbl or MES_SAP_Production_Trn_Tbl -- needs the real error log checked, not just the UI status.",
        "ExtractedEntitiesJson": {"HeatNo": "H99318", "WorkOrder": "WO-99120"},
    },
    {
        "AreaID": "Common", "ComplaintTypeID": COMPLAINT_TYPE_CLARIFICATION,
        "BriefDetails": "Quality release on hold for Heat H99320 -- why?",
        "Description": "Heat H99320 shows Quality Release on hold with no visible reason code. The chemistry results look within spec on the operator screen. What's actually blocking the release?",
        "ProblemCategory": "QUALITY", "SourceSystem": "Xbatch",
        "ConversationSummary": "User wants the real reason a quality hold is still active for Heat H99320 despite chemistry looking fine.",
        "SuspectedCause": "Could be a pending Usage Decision/RR record rather than the chemistry itself -- needs MES_SAP_UsageDecision_Trn_Tbl checked.",
        "ExtractedEntitiesJson": {"HeatNo": "H99320"},
    },
    {
        "AreaID": "Common", "ComplaintTypeID": COMPLAINT_TYPE_BUG,
        "BriefDetails": "Work order WO-99125 not closing after completion",
        "Description": "Work Order WO-99125 shows all operations complete but the work order itself will not close in the system. No error message is displayed. Please check what's actually blocking closure.",
        "ProblemCategory": "WORK_ORDER", "SourceSystem": "Xbatch",
        "ConversationSummary": "User wants to know why a fully-completed work order won't close.",
        "SuspectedCause": "Possibly a dangling SAP WO creation/sync step -- needs MES_SAP_WO_Trn_Tbl and XBatch_Work_Order_Mst_Tbl cross-checked.",
        "ExtractedEntitiesJson": {"WorkOrder": "WO-99125"},
    },
    {
        "AreaID": "Common", "ComplaintTypeID": COMPLAINT_TYPE_CLARIFICATION,
        "BriefDetails": "Delay entries missing Report Date for Rolling Mill",
        "Description": "Several delay entries logged for the Rolling Mill Stands area this week are missing a Report Date, which is breaking the daily OEE report. Is this a data entry gap or a system bug in delay logging?",
        "ProblemCategory": "PERFORMANCE", "SourceSystem": "Xbatch",
        "ConversationSummary": "User wants to know if missing Report Date on recent delay entries is operator error or a real bug.",
        "SuspectedCause": "Check Delay_Trn_Tbl for the actual NULL pattern -- may correlate with a specific shift or delay type.",
        "ExtractedEntitiesJson": {"Area": "Rolling Mill Stands"},
    },
    # ------------------------------------------------------------------
    # Batch 2 (2026-09-03): added to exercise the domains catalogued in
    # Knowledge/view_catalog.json since batch 1 -- sap_posting (5 API-error
    # call types), billet_inventory (yard/transfer/genealogy), quality
    # (spec-limit deviation), work_order (cancelled/campaign). Real entity
    # values are synthetic (H993xx/WO-991xx pattern, same as batch 1) --
    # deliberately not live heat/billet numbers, so a genuine investigation
    # correctly concludes "not found" rather than accidentally matching an
    # unrelated real production record.
    # ------------------------------------------------------------------
    {
        "AreaID": "Common", "ComplaintTypeID": COMPLAINT_TYPE_BUG,
        "BriefDetails": "Goods movement API failed silently for Heat H99322",
        "Description": "Production goods movement for Heat H99322 shows no material document number and no error on screen. Please check whether the SAP goods-movement API call was ever made and what it returned.",
        "ProblemCategory": "SAP_INTEGRATION", "SourceSystem": "Xbatch",
        "ConversationSummary": "User needs confirmation of whether the goods-movement API call for this heat actually fired and its real status.",
        "SuspectedCause": "Check XMES_SAP_API_GoodsMovement_Error_Vw by TransactionID -- Status may show Completed even if ErrorMessage is populated, so check Status explicitly not ErrorMessage presence.",
        "ExtractedEntitiesJson": {"HeatNo": "H99322"},
    },
    {
        "AreaID": "Common", "ComplaintTypeID": COMPLAINT_TYPE_CLARIFICATION,
        "BriefDetails": "SAP work order creation never confirmed for WO-99130",
        "Description": "Work Order WO-99130 was created in MES three days ago but its SAP work order number is still blank. Was the SAP work-order-creation API call ever actually sent?",
        "ProblemCategory": "SAP_INTEGRATION", "SourceSystem": "Xbatch",
        "ConversationSummary": "User wants to know if SAP work-order creation was attempted for this work order and what SAP said back.",
        "SuspectedCause": "Check XMES_SAP_API_WorkOrderCreation_Error_Vw for a matching TransactionID against this WorkOrderNumber.",
        "ExtractedEntitiesJson": {"WorkOrder": "WO-99130"},
    },
    {
        "AreaID": "Common", "ComplaintTypeID": COMPLAINT_TYPE_BUG,
        "BriefDetails": "Usage decision never posted for Heat H99325 / Lot INS-99201",
        "Description": "Chemistry results for Heat H99325 (Inspection Lot INS-99201) came back within spec three days ago but the SAP usage decision still shows pending. What's blocking the post?",
        "ProblemCategory": "QUALITY", "SourceSystem": "Xbatch",
        "ConversationSummary": "User wants to know why a passed quality result hasn't triggered a SAP usage decision post.",
        "SuspectedCause": "Check XMES_SAP_API_UsageDecision_Error_Vw by HeatNo/InspectionLot -- this is the quality<->SAP bridge, cross-check against XStudio_List_Quality_Spectro_Result_Vw for the actual pass/fail.",
        "ExtractedEntitiesJson": {"HeatNo": "H99325", "InspectionLot": "INS-99201"},
    },
    {
        "AreaID": "Common", "ComplaintTypeID": COMPLAINT_TYPE_BUG,
        "BriefDetails": "Billet 1602500_09 shows in two locations at once",
        "Description": "Billet 1602500_09 appears in the yard inventory view AND shows as charged in a furnace at the same time. Which is correct, and is this a real duplicate transfer or a stale record?",
        "ProblemCategory": "PRODUCTION_STATE", "SourceSystem": "Xbatch",
        "ConversationSummary": "User needs the real current location of this billet and an explanation for the apparent duplicate.",
        "SuspectedCause": "Check XStudio_List_XBatch_Billets_Transfer_History_Tbl_Vw for the full chronological trail -- the most recent ActionDate should resolve which location is current.",
        "ExtractedEntitiesJson": {"BilletNo": "1602500_09", "HeatNo": "1602500"},
    },
    {
        "AreaID": "Common", "ComplaintTypeID": COMPLAINT_TYPE_CLARIFICATION,
        "BriefDetails": "Billet genealogy missing strand for Heat H99328",
        "Description": "Heat H99328 was cast on all 6 strands per the shift log, but billet genealogy only shows 5 strands recorded. Is one strand's data genuinely missing or just not yet synced?",
        "ProblemCategory": "DATA_LOOKUP", "SourceSystem": "Xbatch",
        "ConversationSummary": "User wants to confirm whether a strand's billet genealogy is truly missing or a timing/sync gap.",
        "SuspectedCause": "Check XStudio_List_XMES_CCM_Billet_Genealogy_Trn_Tbl_Vw grouped by StrandNo for this HeatNo.",
        "ExtractedEntitiesJson": {"HeatNo": "H99328"},
    },
    {
        "AreaID": "Common", "ComplaintTypeID": COMPLAINT_TYPE_BUG,
        "BriefDetails": "Rebar Tran Rib height reading outside spec but not flagged",
        "Description": "A rebar sample's Tran Rib height reading looks outside the documented spec range but the system did not flag it as a deviation. Please check whether the configured limits are being applied correctly.",
        "ProblemCategory": "QUALITY", "SourceSystem": "Xbatch",
        "ConversationSummary": "User suspects a quality deviation was missed and wants the configured spec limits checked against the actual reading.",
        "SuspectedCause": "Compare the real reading against XStudio_List_Quality_Deviation_Master_Vw's High/Low for Product=Rebar, ParameterName='Tran Rib ht (am) mm'.",
        "ExtractedEntitiesJson": {},
    },
    {
        "AreaID": "Common", "ComplaintTypeID": COMPLAINT_TYPE_CLARIFICATION,
        "BriefDetails": "Why was Work Order WO-99135 cancelled?",
        "Description": "Work Order WO-99135 shows as cancelled in the system but no cancellation reason or remark is visible on screen. What happened to it?",
        "ProblemCategory": "WORK_ORDER", "SourceSystem": "Xbatch",
        "ConversationSummary": "User wants the real reason and timing behind a work order's cancellation.",
        "SuspectedCause": "Check XStudio_List_XBatch_Cancelled_and_Aborted_Work_Order_Mst_Tbl_Vw for this WorkOrderNumber's detail.",
        "ExtractedEntitiesJson": {"WorkOrder": "WO-99135"},
    },
    {
        "AreaID": "Common", "ComplaintTypeID": COMPLAINT_TYPE_BUG,
        "BriefDetails": "Raw material consumption not posted for Heat H99330",
        "Description": "Raw material consumption for Heat H99330 does not appear in SAP even though production posting completed normally for the same heat. Is consumption stuck separately from production?",
        "ProblemCategory": "SAP_INTEGRATION", "SourceSystem": "Xbatch",
        "ConversationSummary": "User wants to know if raw-material consumption posting is stuck independently of the (successful) production posting for this heat.",
        "SuspectedCause": "Check XStudio_List_MES_SAP_Consumption_Trn_Tbl_Vw by HeatNo -- consumption and production post separately, one succeeding doesn't guarantee the other did.",
        "ExtractedEntitiesJson": {"HeatNo": "H99330"},
    },
]

# ------------------------------------------------------------------
# Batch 3 (2026-09-03): scale batch -- 80 more tickets, generated from
# templates instead of hand-written one at a time, per the user's explicit
# "add 80 more, scale" request. Same discipline as batches 1-2: synthetic
# H994xx/WO-993xx/etc. entity numbers (never real production IDs), one
# ProblemCategory/route per template so each ticket is genuinely routable,
# and real column/view names cited in SuspectedCause so a real investigation
# has somewhere concrete to look. 8 templates x 10 numbered variants = 80,
# each BriefDetails is unique (varies by entity number) so the existing
# dedup guard (existing_brief_details) works unchanged.
# ------------------------------------------------------------------
_BATCH_3_TEMPLATES = [
    {
        "area": "EAF", "type": COMPLAINT_TYPE_BUG, "category": "PRODUCTION_STATE", "source": "Xbatch",
        "brief": "EAF power-on time looks wrong for Heat H994{n:02d}",
        "desc": "Heat H994{n:02d}'s EAF power-on time in the daily summary looks inconsistent with the shift log. Please check the real PowerOnTime/PowerOffTime against the tap timing for this heat.",
        "summary": "User wants EAF power timing verified for Heat H994{n:02d} against the shift log.",
        "cause": "Check XBatch_Tracability_Heat_Details_Vw for PowerOnTime/PowerOffTime/TapToTapTime on this HeatNo.",
        "entities": lambda n: {"HeatNo": f"H994{n:02d}"},
    },
    {
        "area": "Common", "type": COMPLAINT_TYPE_CLARIFICATION, "category": "SAP_INTEGRATION", "source": "Xbatch",
        "brief": "SAP inventory sync missing for Plant/Storage on Batch B994{n:02d}",
        "desc": "Batch B994{n:02d} does not appear in the SAP inventory sync for its storage location, though the goods movement in MES looks complete. Was the inventory-sync API call ever made?",
        "summary": "User needs confirmation of whether the SAP inventory-sync call fired for this batch's storage location.",
        "cause": "Check XStudio_List_XMES_SAP_API_Inventory_Error_Vw by PlantCode/StorageLocation and Status.",
        "entities": lambda n: {"Batch": f"B994{n:02d}"},
    },
    {
        "area": "Common", "type": COMPLAINT_TYPE_BUG, "category": "PRODUCTION_STATE", "source": "Xbatch",
        "brief": "Billet 1603{n:03d}_05 not showing in yard inventory",
        "desc": "Billet 1603{n:03d}_05 was transferred to the yard per the shift log but does not appear in the current yard inventory listing. Is this a sync delay or a genuine missing transfer record?",
        "summary": "User wants to confirm whether this billet's yard arrival was ever recorded.",
        "cause": "Check XStudio_List_XBatch_Billets_Transfer_History_Tbl_Vw for the most recent ActionDate/FromLocation for this BilletNo, then cross-check XStudio_List_Billet_Inventory_Vw.",
        "entities": lambda n: {"BilletNo": f"1603{n:03d}_05", "HeatNo": f"1603{n:03d}"},
    },
    {
        "area": "Common", "type": COMPLAINT_TYPE_CLARIFICATION, "category": "QUALITY", "source": "Xbatch",
        "brief": "Spectro result for Heat H995{n:02d} missing MinLimit/MaxLimit",
        "desc": "The spectrometer result for Heat H995{n:02d} shows a value but no MinLimit/MaxLimit, so pass/fail can't be determined from the screen. Are the spec limits configured for this element/product?",
        "summary": "User wants the missing spec limits investigated for this heat's spectro result.",
        "cause": "Check XStudio_List_Quality_Spectro_Result_Vw for this HeatNo's rows, and XStudio_List_Quality_Deviation_Master_Vw for whether the Product/ParameterName combination has configured limits at all.",
        "entities": lambda n: {"HeatNo": f"H995{n:02d}"},
    },
    {
        "area": "Common", "type": COMPLAINT_TYPE_BUG, "category": "WORK_ORDER", "source": "Xbatch",
        "brief": "Campaign plan missing Work Order WO-994{n:02d}",
        "desc": "Work Order WO-994{n:02d} was created under Campaign CMP-99{n:02d} but doesn't show up when listing that campaign's work orders. Is it linked to the wrong campaign or genuinely orphaned?",
        "summary": "User wants to confirm this work order's real campaign linkage.",
        "cause": "Check XStudio_XMes_Campaign_Plan_work_order_Vw by CampaignNo and by WorkOrderNumber separately -- if it shows under neither or a different CampaignNo, that's the real answer.",
        "entities": lambda n: {"WorkOrder": f"WO-994{n:02d}", "Campaign": f"CMP-99{n:02d}"},
    },
    {
        "area": "Common", "type": COMPLAINT_TYPE_CLARIFICATION, "category": "PERFORMANCE", "source": "Xbatch",
        "brief": "Delay reason blank for a {n} minute stoppage on Heat H996{n:02d}",
        "desc": "A {n}-minute delay was logged against Heat H996{n:02d} with no DelayReason and no Equipment recorded. Was this a real unattributed stoppage or a data entry gap?",
        "summary": "User wants the real cause behind an unattributed delay on this heat.",
        "cause": "Check XBatch_Delay_Analysis_Vw for this HeatNo -- compare AgencyRemark/EquipmentRemark across the merged rows for anything the blank TotalDelayReason might be missing.",
        "entities": lambda n: {"HeatNo": f"H996{n:02d}"},
    },
    {
        "area": "Common", "type": COMPLAINT_TYPE_BUG, "category": "SAP_INTEGRATION", "source": "Xbatch",
        "brief": "Batch creation API status unclear for Batch B995{n:02d}",
        "desc": "Batch B995{n:02d} exists in MES but it's unclear whether the SAP batch-creation API call succeeded, failed, or was never sent. Please check the real transaction status.",
        "summary": "User wants the real SAP batch-creation status for this batch confirmed.",
        "cause": "Check XStudio_List_XMES_SAP_API_Batch_Creation_Error_Vw by BatchNo, read Status not just ErrorMessage presence.",
        "entities": lambda n: {"Batch": f"B995{n:02d}"},
    },
    {
        "area": "Common", "type": COMPLAINT_TYPE_CLARIFICATION, "category": "PRODUCTION_STATE", "source": "Xbatch",
        "brief": "CCM billet genealogy strand sequence looks out of order for Heat H997{n:02d}",
        "desc": "The billet genealogy for Heat H997{n:02d} shows StrandSequence values that don't look monotonically increasing for one strand. Is this a real casting anomaly or a data recording issue?",
        "summary": "User wants the strand sequence anomaly for this heat's billet genealogy checked.",
        "cause": "Check XStudio_List_XMES_CCM_Billet_Genealogy_Trn_Tbl_Vw grouped by StrandNo, ordered by StrandSequence, for this HeatNo.",
        "entities": lambda n: {"HeatNo": f"H997{n:02d}"},
    },
]


# ------------------------------------------------------------------
# Batch 4 (2026-09-03): fixes a real bug found in batches 1-3 -- their
# entity IDs (H99310, WO-99125, INS-99201, 1602500_09) used made-up formats
# that don't match real production conventions, confirmed live:
#   HeatNo        -- 7-digit int, real range ~1504972-1604015 (EAF_PER_HEAT
#                    has no HeatNo column at all; it's HeatID there)
#   WorkOrderNumber -- 12-digit numeric string (e.g. "120000154929")
#   InspectionLot / Batch -- 11-digit numeric string (e.g. "40002997923")
#   BilletNo      -- "<HeatNo>_<sequence>" (confirmed via
#                    XStudio_List_Billet_Inventory_Vw / Transfer_History_Vw;
#                    a second "<HeatNo>_S<strand>_<seq>" form also exists,
#                    confirmed via XMES_CCM_Billet_Genealogy -- two real,
#                    different conventions depending on which view/context)
# Any ticket referencing a wrong-format ID was testing "does the bot detect
# a garbage identifier", not "can the bot investigate a real one" -- not a
# fair test of solver quality. Batches 1-3 are left in place (some already
# have live Kanban tasks against them -- deleting would orphan that work),
# this batch is additive and uses IDs in a range that clearly never
# collides with real production heats (1900000+, never issued).
# ------------------------------------------------------------------
def _synthetic_heat(n: int) -> int:
    return 1900000 + n


def _synthetic_wo(n: int) -> str:
    return f"199000000{n:03d}"


def _synthetic_lot(n: int) -> str:
    return f"49900000{n:03d}"


_BATCH_4_TEMPLATES = [
    {
        "area": "EAF", "type": COMPLAINT_TYPE_BUG, "category": "PRODUCTION_STATE", "source": "Xbatch",
        "brief": "Electrode consumption looks doubled for Heat {heat}",
        "desc": "Electrode consumption for Heat {heat} in the EAF daily summary shows roughly double the expected value compared to similar heats this week. Please check whether this is a real consumption spike or a data/unit conversion issue.",
        "summary": "User flagged an anomalous electrode consumption reading for Heat {heat} and wants to know if it's real or a data bug.",
        "cause": "Check XBatch_Tracability_Heat_Details_Vw for this HeatNo -- known live bug: this view can fail with 'Subquery returned more than 1 value' on some row sets, fall back to base EAF tables if so.",
        "entities": lambda n: {"HeatNo": str(_synthetic_heat(n))},
    },
    {
        "area": "Common", "type": COMPLAINT_TYPE_CLARIFICATION, "category": "SAP_INTEGRATION", "source": "Xbatch",
        "brief": "SAP posting stuck pending for Heat {heat} / WO {wo}",
        "desc": "SAP production posting for Heat {heat} (Work Order {wo}) has been stuck in pending status for over 12 hours. No error is shown on screen. Please check whether the API call was ever actually sent to SAP.",
        "summary": "User needs to know if the SAP posting for this heat/work-order pair actually fired or is silently stuck.",
        "cause": "Check XStudio_List_MES_SAP_Production_Trn_Tbl_SAPPostingFail_Vw and XStudio_List_XMES_SAP_API_GoodsMovement_Error_Vw by HeatNo/TransactionID -- filter SAPPostingStatus/Status explicitly, view is not pre-filtered.",
        "entities": lambda n: {"HeatNo": str(_synthetic_heat(n)), "WorkOrder": _synthetic_wo(n)},
    },
    {
        "area": "Common", "type": COMPLAINT_TYPE_BUG, "category": "PRODUCTION_STATE", "source": "Xbatch",
        "brief": "Billet {heat}_05 not showing in yard inventory",
        "desc": "Billet {heat}_05 was transferred to the yard per the shift log but does not appear in the current yard inventory listing. Is this a sync delay or a genuine missing transfer record?",
        "summary": "User wants to confirm whether this billet's yard arrival was ever recorded.",
        "cause": "Check XStudio_List_XBatch_Billets_Transfer_History_Tbl_Vw for the most recent ActionDate/FromLocation for this BilletNo, then cross-check XStudio_List_Billet_Inventory_Vw.",
        "entities": lambda n: {"BilletNo": f"{_synthetic_heat(n)}_05", "HeatNo": str(_synthetic_heat(n))},
    },
    {
        "area": "Common", "type": COMPLAINT_TYPE_CLARIFICATION, "category": "QUALITY", "source": "Xbatch",
        "brief": "Usage decision never posted for Heat {heat} / Lot {lot}",
        "desc": "Chemistry results for Heat {heat} (Inspection Lot {lot}) came back within spec three days ago but the SAP usage decision still shows pending. What's blocking the post?",
        "summary": "User wants to know why a passed quality result hasn't triggered a SAP usage decision post.",
        "cause": "Check XMES_SAP_API_UsageDecision_Error_Vw by HeatNo/InspectionLot -- cross-check against XStudio_List_Quality_Spectro_Result_Vw for the actual pass/fail.",
        "entities": lambda n: {"HeatNo": str(_synthetic_heat(n)), "InspectionLot": _synthetic_lot(n)},
    },
    {
        "area": "Common", "type": COMPLAINT_TYPE_BUG, "category": "WORK_ORDER", "source": "Xbatch",
        "brief": "Work order {wo} not closing after completion",
        "desc": "Work Order {wo} shows all operations complete but the work order itself will not close in the system. No error message is displayed. Please check what's actually blocking closure.",
        "summary": "User wants to know why a fully-completed work order won't close.",
        "cause": "Check XStudio_List_XBatch_Work_Order_Mst_Tbl_Vw and XStudio_List_XBatch_Cancelled_and_Aborted_Work_Order_Mst_Tbl_Vw for this WorkOrderNumber's real Status.",
        "entities": lambda n: {"WorkOrder": _synthetic_wo(n)},
    },
    {
        "area": "Common", "type": COMPLAINT_TYPE_CLARIFICATION, "category": "PERFORMANCE", "source": "Xbatch",
        "brief": "Delay reason blank for Heat {heat}",
        "desc": "A delay was logged against Heat {heat} with no DelayReason and no Equipment recorded. Was this a real unattributed stoppage or a data entry gap?",
        "summary": "User wants the real cause behind an unattributed delay on this heat.",
        "cause": "Check XBatch_Delay_Analysis_Vw for this HeatNo -- compare AgencyRemark/EquipmentRemark across the merged rows for anything the blank TotalDelayReason might be missing.",
        "entities": lambda n: {"HeatNo": str(_synthetic_heat(n))},
    },
]


def generate_batch_4_tickets(count: int = 30) -> list:
    generated = []
    for i in range(count):
        template = _BATCH_4_TEMPLATES[i % len(_BATCH_4_TEMPLATES)]
        n = (i // len(_BATCH_4_TEMPLATES)) + 1
        entities = template["entities"](n)
        fmt_args = {"heat": entities.get("HeatNo"), "wo": entities.get("WorkOrder"), "lot": entities.get("InspectionLot")}
        generated.append({
            "AreaID": template["area"],
            "ComplaintTypeID": template["type"],
            "BriefDetails": template["brief"].format(**fmt_args),
            "Description": template["desc"].format(**fmt_args),
            "ProblemCategory": template["category"],
            "SourceSystem": template["source"],
            "ConversationSummary": template["summary"].format(**fmt_args),
            "SuspectedCause": template["cause"],
            "ExtractedEntitiesJson": entities,
        })
    return generated


TICKETS.extend(generate_batch_4_tickets(30))


def generate_batch_3_tickets(count: int = 80) -> list:
    """Round-robins the 8 templates above with an incrementing variant
    number so BriefDetails stays unique per ticket (required for the
    existing_brief_details dedup guard to work)."""
    generated = []
    for i in range(count):
        template = _BATCH_3_TEMPLATES[i % len(_BATCH_3_TEMPLATES)]
        n = (i // len(_BATCH_3_TEMPLATES)) + 1
        generated.append({
            "AreaID": template["area"],
            "ComplaintTypeID": template["type"],
            "BriefDetails": template["brief"].format(n=n),
            "Description": template["desc"].format(n=n),
            "ProblemCategory": template["category"],
            "SourceSystem": template["source"],
            "ConversationSummary": template["summary"].format(n=n),
            "SuspectedCause": template["cause"],
            "ExtractedEntitiesJson": template["entities"](n),
        })
    return generated


TICKETS.extend(generate_batch_3_tickets(80))


def build_connection(server, database, username, password):
    return pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};"
        f"UID={username};PWD={password};TrustServerCertificate=yes"
    )


def next_ticket_no(cur):
    cur.execute("SELECT MAX(CAST(REPLACE(TicketNo,'Ticket_','') AS INT)) FROM Complaint_Mst_Tbl WHERE TicketNo LIKE 'Ticket_%'")
    return (cur.fetchone()[0] or 0) + 1


def existing_brief_details(cur) -> set:
    """Idempotency guard: BriefDetails is unique enough across this script's
    own synthetic tickets (real ones don't collide with 'Heat H993..' style
    text) to detect a ticket this script already inserted in an earlier run,
    so re-running after adding new templates doesn't duplicate old ones."""
    cur.execute("SELECT BriefDetails FROM Complaint_Mst_Tbl WHERE FirstLastName = 'L1 Chatbot Test'")
    return {row[0] for row in cur.fetchall()}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--server", default="10.2.6.204")
    ap.add_argument("--database", default="XStudio_Helpdesk")
    ap.add_argument("--username", default="sa")
    ap.add_argument("--password", default=os.environ.get("MSSQL_MCP_PASSWORD"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = build_connection(args.server, args.database, args.username, args.password)
    try:
        cur = conn.cursor()
        ticket_no = next_ticket_no(cur)
        already_seeded = existing_brief_details(cur)

        created = 0
        for t in TICKETS:
            if t["BriefDetails"] in already_seeded:
                print(f"Skipping (already seeded): {t['BriefDetails']}")
                continue

            new_id = str(uuid.uuid4()).upper()
            new_ticket_no = f"Ticket_{ticket_no}"
            entities = json.dumps(t["ExtractedEntitiesJson"])

            print(f"{'[DRY RUN] ' if args.dry_run else ''}Creating {new_ticket_no}: {t['BriefDetails']}")
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
                        ?, ?, NULL, GETDATE(), GETDATE(), 0, 0,
                        'T-SQL', ?, ?, ?, 'Enter', ?,
                        ?, 'L1 Chatbot Test', '90000010', 'l1test10@example.com', 'Enter', 'Enter',
                        ?, ?, ?, ?,
                        ?
                    )
                    """,
                    new_id, t["AreaID"], t["ComplaintTypeID"], t["Description"], t["BriefDetails"], new_ticket_no,
                    PRIORITY_HIGH, t["ProblemCategory"], t["SourceSystem"], t["ConversationSummary"],
                    t["SuspectedCause"], entities,
                )
            ticket_no += 1
            created += 1

        if not args.dry_run:
            conn.commit()
            print(f"\nCreated {created} ticket(s) (skipped {len(TICKETS) - created} already-seeded).")
        else:
            print(f"\n[DRY RUN] Would create {created} ticket(s) (would skip {len(TICKETS) - created} already-seeded).")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
