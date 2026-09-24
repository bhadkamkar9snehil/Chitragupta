---
type: table
title: "XMES_RM_Heated_Billet_trn_tbl"
built: "2026-09-24T11:36:36"
---

# XMES_RM_Heated_Billet_trn_tbl

Table in XStudio_Xbatch. Rows: 2,100.

## Identifiers it holds

- BilletNo: same values as key `BilletNo`
- HeatNO: same values as key `HeatNo`

## Written by

- Billet_Furnace_Movement
- Billet_Furnace_Movement_Billet_Tracking
- Billet_Furnace_Movement_GradeGap
- Billet_Furnace_Movement_HeatGap
- MES_M_Sect2_to_Furnace
- MES_M_Sect2_to_Furnace_Billet_Tracking

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
- BilletNo varchar(100)
- HeatNO varchar(100)
- campaignid varchar(36)
- Workorderid varchar(36)
- ProductType varchar(36)
