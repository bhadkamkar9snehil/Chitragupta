---
type: table
title: "XBatch_Material_Item_Cons_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Material_Item_Cons_Trn_Tbl

Table in XStudio_Xbatch. Rows: 96,143.

## Identifiers it holds

- HeatNo: same values as key `HeatNo`
- LotNumber: same values as key `HeatNo`

## Written by

- HeatChargeMixConsumption
- XBatch_I_Material_Consume_NoBOM_USP
- XBatch_I_Material_Consume_USP
- XBatch_Material_Consumed_Split_Usp
- XMES_LRF_I_Raw_Material_Cons_Usp
- XSTUDIO_WORKFLOW_98A73AE1-1D20-4959-B45E-121B93225279_SP

## Read by

- HeatChargeMixConsumption
- SAP_Posting_Data_ByHeat_Usp
- XMES_LRF_I_Raw_Material_Cons_Usp
- XMES_entry_for_RAW_Material_Consumption_Usp
- XSTUDIO_WORKFLOW_98A73AE1-1D20-4959-B45E-121B93225279_SP

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
- LotNumber varchar(100)
- SublotNumber varchar(100)
- Quantity decimal
- UOMID varchar(36)
- GradeID varchar(36)
- MaterialID varchar(36)
- HeatNo int
- Price decimal
- DeclareQuantity decimal
