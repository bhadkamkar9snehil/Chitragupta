---
type: table
title: "XMES_RM_Furnace_Billet_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# XMES_RM_Furnace_Billet_Trn_Tbl

Table in XStudio_Xbatch. Rows: 2,680.

## Identifiers it holds

- BilletNo: same values as key `BilletNo`
- HeatNo: same values as key `HeatNo`

## Written by

- Billet_Furnace_Movement
- Billet_Furnace_Movement_Billet_Tracking
- Billet_Furnace_Movement_GradeGap
- Billet_Furnace_Movement_HeatGap
- MES_M_Sect2_to_Furnace
- MES_M_Sect2_to_Furnace_Billet_Tracking
- Xstudio_XMES_RM_Furnace_Billet_Trn_Tbl_USP

## Read by

- Billet_Furnace_Movement
- Billet_Furnace_Movement_Billet_Tracking
- Billet_Furnace_Movement_GradeGap
- Billet_Furnace_Movement_HeatGap
- MES_M_Sect2_to_Furnace_Billet_Tracking
- Xstudio_XMES_RM_Furnace_Billet_Trn_Tbl_USP

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
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- Starttime datetime
- EndTime datetime
- HeatNo varchar(36)
- BilletNo varchar(100)
- TotalResidenceTime decimal
- zone2ResidenceTime datetime
- zone3ResidenceTime datetime
- zone4ResidenceTime datetime
- zone5ResidenceTime datetime
- zone6ResidenceTime datetime
- zone7ResidenceTime datetime
- zone8ResidenceTime datetime
- zone1ResidenceTime datetime
- Zone4ResidenceTimeMinute decimal
- Zone1ResidenceTimeMinute decimal
- Zone2ResidenceTimeMinute decimal
- Zone3ResidenceTimeMinute decimal
- Zone5ResidenceTimeMinute decimal
- Zone6ResidenceTimeMinute decimal
- Zone7ResidenceTimeMinute decimal
- Zone8ResidenceTimeMinute decimal
- Zone1ResidenceTimeMMSS varchar(100)
- Zone2ResidenceTimeMMSS varchar(100)
- Zone3ResidenceTimeMMSS varchar(100)
- Zone4ResidenceTimeMMSS varchar(100)
- Zone5ResidenceTimeMMSS varchar(100)
- Zone6ResidenceTimeMMSS varchar(100)
- Zone7ResidenceTimeMMSS varchar(100)
- Zone8ResidenceTimeMMSS varchar(100)
