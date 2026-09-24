---
type: procedure
title: "XBatch_RM_Mill_Billet_DischargeTemp"
built: "2026-09-24T11:36:36"
---

# XBatch_RM_Mill_Billet_DischargeTemp

Parameters: @StartDate datetime, @EndDate datetime.

## Writes

- Billet_NGConsumption_InFurnace: DischargeTemp
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- Billet_NGConsumption_InFurnace: BilletNo
- BilletsPosition_InFurnace: IsDeleted, Position65

## What its own log shows

147,252 log rows, 2026-05-30 11:48 to 2026-06-11 12:44.

Steps:
- 1 Entered
- 2 Temp table tag condition creation Start
- 3 Temp table tag condition creation End
- 4 Insert tagid and condition in Temp table tag condition for RF_DISCHARED_BILLET_TEMP_C_PRM tag Start
- 5 Insert tagid and condition in Temp table tag condition for RF_DISCHARED_BILLET_TEMP_C_PRM tag End
- 6 Create temp table RM Mill Discharge temp Start
- 7 Create temp table RM Mill Discharge temp End
- 8 Insert data into temp table RM Mill Discharge temp by executing historian procedure XHS_Tag_Max_Value_Usp Start
- 9 Insert data into temp table RM Mill Discharge temp by executing historian procedure XHS_Tag_Max_Value_Usp End
- 10 Get Val from temp table RM Mill Discharge temp Start
- 10 Truncate temp table tag condition Start
- 11 Get Val from temp table RM Mill Discharge temp End
- 11 Truncate temp table tag condition End
- 12 Get Last Position bille no Start
- 12 Truncate temp table tag condition Start
- 13 Get Last Position bille no End
- 13 Truncate temp table tag condition End
- 14 Completed
- 14 Get Last Position bille no Start
- 15 Get Last Position bille no End
- 16 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XBatch_RM_Mill_Billet_DischargeTemp`
