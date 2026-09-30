---
type: procedure
title: "XMES_RM_SAP_Posting_Sequence_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_RM_SAP_Posting_Sequence_Usp

Parameters: @ID varchar, @APIPostingType varchar.

## Writes

- MES_SAP_Production_Trn_Tbl: SAPPostingStatus

## Reads

- MES_SAP_Consumption_Trn_Tbl: Batch, FurnaceBilletStatus, ID
- MES_SAP_Production_Trn_Tbl: Batch
- XMES_RM_Production_Data: BilletNo, EndProductNo, IsSapConsumed
