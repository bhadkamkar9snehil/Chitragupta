---
type: table
title: "Xbatch_Material_Inventory_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# Xbatch_Material_Inventory_Trn_Tbl

Table in XStudio_Xbatch. Rows: 1,300.

## Identifiers it holds

- BilletNo: same values as key `BilletNo`
- LotNumber: same values as key `HeatNo`

## Written by

- HeatChargeMixConsumption
- MES_M_Strand
- XBatch_I_Material_Consume_NoBOM_USP
- XBatch_I_Material_Produce_NoBOM_USP
- XMES_I_ByProduct_Trn_Usp
- XMES_I_SAP_Billet_Production_Trn
- XMES_I_SAP_GLS_LS_Consumption_Trn_Usp
- XMES_I_SAP_GLS_LS_Production_Trn_Usp
- XMES_LRF_I_Raw_Material_Cons_Usp
- XMES_SAP_I_Inventory_Stock_Data_Usp
- XMES_SAP_Posting_Sequence_Usp
- XMES_U_Inventory_Master_byTrn_Usp
- XMES_U_SAP_Billet_Production_Trn_Usp
- Xmes_Billet_Tracking_Move_to_Stand_1
- Xmes_Billet_Tracking_Move_to_Stand_18 (text)

## Read by

- XMES_RemaingBillets_In_Inventory_Usp
- XMES_SAP_I_Inventory_Stock_Data_Usp
- XMES_U_Inventory_Master_byTrn_Usp

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
- MaterialGrade varchar(100)
- PostingMaterialType varchar(100)
- PlantName varchar(36)
- ParentID varchar(36)
- Quantity decimal
- StorageLocation varchar(36)
- QuantityinCount int
- UOMID varchar(36)
- LotNumber varchar(100)
- Ismodified bit
- BilletNo varchar(100)
- isExternal bit
- TotalQuantity decimal
