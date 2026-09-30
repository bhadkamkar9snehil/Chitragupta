---
type: table
title: "XMES_SAP_API_GoodsMovement_Error"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_API_GoodsMovement_Error

Table in XStudio_Xbatch. Rows: 1,371.

## Identifiers it holds

- Batch: same values as key `HeatNo`
- ManufacturingOrder: same values as key `ManufacturingOrder`
- Material: same values as key `Material`
- TransactionID: same values as key `TransactionID`

## Written by

- XMES_SAP_GoodsMovements_API_Error_Usp
- XSTUDIO_WORKFLOW_02ADFA58-6CF3-4D22-82A6-BE020FA00BC2_SP (text)
- XSTUDIO_WORKFLOW_61EFD8FE-EDF5-4077-BE99-35EF68C5AFCB_SP (text)

## Read by

- XSTUDIO_WORKFLOW_02ADFA58-6CF3-4D22-82A6-BE020FA00BC2_SP
- XSTUDIO_WORKFLOW_61EFD8FE-EDF5-4077-BE99-35EF68C5AFCB_SP

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
- TransactionID varchar(100)
- RecordID varchar(100)
- Body varchar(-1)
- ErrorMessage varchar(-1)
- Status varchar(50)
- Type varchar(100)
- Batch varchar(100)
- ManufacturingOrder varchar(100)
- Material varchar(100)
- MovementType int
- SuccessMessage varchar(-1)
