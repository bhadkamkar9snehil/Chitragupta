---
type: procedure
title: "Per_Heat_LadleNo_Conformation_usp"
built: "2026-09-24T11:36:36"
---

# Per_Heat_LadleNo_Conformation_usp

Parameters: @HeatNo int, @LadleNo varchar, @LRFConformed bit, @CCMConformed bit, @TundishNo varchar.

## Writes

- Per_Heat_LadleNo: LadleNo, LadleNoAtCCM, LadleNoAtCCMDatetime, LadleNoAtLRF, LadleNoAtLRFDatetime, TundishNo
- XMES_ActiveLife_Element_Mst_Tbl: LastUsedBatch, Source, Status

## Reads

- CCM_Per_Heat: HeatID, StartTime
- LRF_Per_Heat: HeatID, StartTime
- Per_Heat_LadleNo: HeatNo
- XMES_ActiveLife_Element_Mst_Tbl: ElementNameID, IsDeleted
