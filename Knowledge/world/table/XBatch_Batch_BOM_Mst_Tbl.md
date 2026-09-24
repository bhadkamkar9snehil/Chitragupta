---
type: table
title: "XBatch_Batch_BOM_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Batch_BOM_Mst_Tbl

Table in XStudio_Xbatch. Rows: 0.

## Written by

- XBatch_Create_Batch_Usp
- XBatch_I_Material_Consume_USP
- XBatch_I_Material_Produce_USP

## Read by

- XBatch_I_Material_Consume_USP
- XBatch_I_Material_Produce_USP

## Columns

- ID varchar(36)
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
- ItemID varchar(36)
- Quantity decimal
- UOMID varchar(36)
- UnitProcedureID varchar(36)
- OperationID varchar(36)
- PhaseGroupID varchar(36)
- PhaseID varchar(36)
- ActualQuantity decimal
- QuantityDeviation decimal
- SourceType varchar(100)
