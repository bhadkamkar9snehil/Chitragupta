---
type: table
title: "Billet_NGConsumption_InFurnace"
built: "2026-09-24T11:36:36"
---

# Billet_NGConsumption_InFurnace

Table in XStudio_Xbatch. Rows: 934.

## Identifiers it holds

- BilletNo: same values as key `BilletNo`

## Written by

- Billet_Furnace_Movement
- BilletsPosition_InFurnace_Usp
- MES_M_Sect2_to_Furnace
- XBatch_RM_BilletWiseNGConsumption
- XBatch_RM_Mill_Billet_DischargeTemp
- Xstudio_Billet_NGConsumption_InFurnace_USP

## Read by

- Billet_Furnace_Movement
- XBatch_RM_BilletWiseNGConsumption
- XBatch_RM_Mill_Billet_DischargeTemp
- Xstudio_Billet_NGConsumption_InFurnace_USP

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
- InTime datetime
- ReportDate date
- IsProcessed bit
- BilletNo varchar(100)
- NGConsumption decimal
- Price decimal
- OutTime datetime
- DurationHHMM varchar(100)
- DischargeTemp decimal
