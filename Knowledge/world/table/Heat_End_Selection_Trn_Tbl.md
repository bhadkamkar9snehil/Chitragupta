---
type: table
title: "Heat_End_Selection_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# Heat_End_Selection_Trn_Tbl

Table in XStudio_Xbatch. Rows: 344.

## Identifiers it holds

- FirstHeatNo: same values as key `HeatNo`
- LastHeatNo: same values as key `HeatNo`

## Written by

- XBatch_Add_Default_Heat_start_end_Usp
- XBatch_Add_Heat_start_end_Usp
- Xstudio_Heat_End_Selection_Trn_Tbl_USP

## Read by

- SP_SMS_Producation_Summary
- XBatch_Add_Heat_start_end_SPValidation_Usp
- XMES_Recalculate_HEAT_CHEMISTRY_DEVIATION_Usp
- XMES_SP_HEAT_CHEMISTRY_REPORT_DATA
- XMES_entry_for_RAW_Material_Consumption_Usp
- XSTUDIO_WORKFLOW_98A73AE1-1D20-4959-B45E-121B93225279_SP
- Xstudio_Heat_End_Selection_Trn_Tbl_USP

## Columns

- ID varchar(36)
- Name varchar(100)
- ParentID varchar(36)
- CreatedBy varchar(36)
- ModifiedBy varchar(36)
- CreatedOn datetime
- ModifiedOn datetime
- IsDeleted bit
- IsSystem bit
- AssignedUserID varchar(36)
- HostAddress varchar(100)
- DbSyncStatus varchar(500)
- MobileSyncStatus varchar(100)
- Source varchar(20)
- ReportDate date
- IsProcessed bit
- FirstHeatNo int
- LastHeatNo int
- Dateyyyymmdd varchar(100)
- FIrstHeatStartTime datetime
- LastHeatTapTime datetime
- CalTimeinMinutes int
- CalTimeinSecond int
