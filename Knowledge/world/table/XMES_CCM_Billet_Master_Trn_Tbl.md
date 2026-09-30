---
type: table
title: "XMES_CCM_Billet_Master_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# XMES_CCM_Billet_Master_Trn_Tbl

Table in XStudio_Xbatch. Rows: 12,862.

## Identifiers it holds

- Batch: same values as key `HeatNo`
- BilletNo: same values as key `BilletNo-2`
- HeatNo: same values as key `HeatNo`

## Written by

- XMES_CCM_BILLET_MASTER_CREATE_USP

## Read by

- XMES_CCM_BILLET_MASTER_CREATE_USP

## Columns

- ID varchar(36)
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
- CutLength decimal
- Plant varchar(100)
- ParentID varchar(36)
- StatePosition varchar(100)
- Qualitygradeid varchar(36)
- BilletQuantity int
- EntryDateTime datetime
- BilletWeight decimal
- BilletNo varchar(100)
- ProcessStage varchar(100)
- HeatNo varchar(100)
- UOMID varchar(36)
- Batch varchar(100)
- IsProcessed bit
- ManufacturingOrder varchar(100)
- ReportDate date
- Name varchar(100)
- PostingMaterialType varchar(100)
- StorageLocation varchar(100)
- Materialid varchar(36)
