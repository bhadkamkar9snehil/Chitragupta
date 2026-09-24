---
type: procedure
title: "XMES_U_SAP_Billet_Posting_Count_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_U_SAP_Billet_Posting_Count_Usp

Parameters: @ProductionID varchar.

## Writes

- CCM_Per_Heat: RemainingPostedBilletCount, RemainingPostedBilletWeightTon, TotalPostedBilletCount, TotalPostedBilletWeightTon

## Reads

- CCM_Per_Heat: ActualBilletCount, ActualBilletWeightTon, HeatID, IsDeleted
- MES_SAP_Production_Trn_Tbl: HeatNo, ID, IsDeleted, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, SAPPostingStatus
