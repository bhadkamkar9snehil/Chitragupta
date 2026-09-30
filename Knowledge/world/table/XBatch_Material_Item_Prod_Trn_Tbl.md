---
type: table
title: "XBatch_Material_Item_Prod_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Material_Item_Prod_Trn_Tbl

Table in XStudio_Xbatch. Rows: 171,218.

## Identifiers it holds

- HeatNo: same values as key `HeatNo`
- LotNumber: same values as key `HeatNo`

## Written by

- SP_Xbatch_SplitsBillets_From_CCM_To_Inventory
- XBatch_I_Material_Produce_NoBOM_USP
- XBatch_I_Material_Produce_USP
- XMES_I_SAP_Billet_Production_Trn
- XSTUDIO_WORKFLOW_24F2F246-218B-40A0-99DB-EC15F3350D4E_SP

## Read by

- SAP_Posting_Data_ByHeat_Usp
- XSTUDIO_WORKFLOW_24F2F246-218B-40A0-99DB-EC15F3350D4E_SP

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
- HeatNo int
- MaterialID varchar(36)
- DeclareQuantity decimal
