---
type: procedure
title: "XBatch_Campaign_Plan_Modified_Status_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Campaign_Plan_Modified_Status_Usp

Parameters: @billetno varchar.

## Writes

- XBatch_Work_Order_Mst_Tbl: Status

## Reads

- RM_Operator_HeatSelection: ID, workorder
- XBatch_Work_Order_Mst_Tbl: ID
- XMES_Live_Billet_Charging_Bed: BilletNo, IsDeleted, ParentID
