---
type: procedure
title: "SMS_Reset_Life_Tracking_Status"
built: "2026-09-24T11:36:36"
---

# SMS_Reset_Life_Tracking_Status

Parameters: @RecordID varchar.

## Writes

- Life_Tracking_Transaction_tbl: AlertPercentage, ConsumePercentage, CurrentLife, EntryDateTime, HeatID, ID, Life, LifeType, Remarks
- XMES_Element_Life_Counter_Trn_Tbl: ConsumeLifepercentage, CurrentLife, ModifiedOn

## Reads

- XMES_Element_Life_Counter_Trn_Tbl: AlertPercentage, ElementNameID, ID, IsDeleted, LastUsedBatch
- XMES_Life_Element_Mst_Tbl: ID, ParentID
- XMES_Life_Element_Type_Mst_Tbl: ID, IsDeleted, Name
