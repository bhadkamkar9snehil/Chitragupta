---
type: procedure
title: "XSTUDIO_WORKFLOW_17E91BC0-FC67-4CB1-9699-1625D71488F2_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_17E91BC0-FC67-4CB1-9699-1625D71488F2_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- Life_Tracking_Transaction_tbl: ConsumePercentage, CurrentLife, EntryDateTime, HeatID, Life, LifeType
- XMES_Element_Life_Counter_Trn_Tbl: ConsumeLifepercentage, CurrentLife, LastUsedBatch, ModifiedOn
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- XMES_ActiveLife_Element_Mst_Tbl: Activeinactiveflag, ElementNameID, ID, LastUsedBatch
- XMES_Element_Life_Counter_Trn_Tbl: ElementNameID, MaximumLife
- XMES_Life_Element_Mst_Tbl: ID, Name, ParentID
- XMES_Life_Element_Type_Mst_Tbl: ID, IsDeleted, Name

## Writes (named in its SQL text)

- XMES_ActiveLife_Element_Mst_Tbl

## What its own log shows

5,706 log rows, 2026-05-28 10:30 to 2026-06-29 14:58.

Steps:
- 1 Entered
- 2 Update CurrentLife, ConumeLifePercentage and LastUsedBatch in Element Life Count Start
- 3 Update CurrentLife, ConumeLifePercentage and LastUsedBatch in Element Life Count End
- 4 Insert Life data in Life tracking transaction Start
- 5 Insert Life data in Life tracking transaction End
- 6 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_17E91BC0-FC67-4CB1-9699-1625D71488F2_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='3ADE6546-3C9A-49C4-A001-234025F2F901', @p_RecordId='Active', @p_StatusAttributeName='FECE87C6-5990-43AA-B7E9-30E8D123AC04', @p_Status='Status'`
