---
type: table
title: "XBatch_Material_Inventory_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Material_Inventory_Mst_Tbl

Table in XStudio_Xbatch. Rows: 2,046.

## Identifiers it holds

- LotNumber: same values as key `HeatNo`

## Written by

- AllocateBilletsToStacksByBilletNo
- BilletsPosition_InFurnace_Usp
- HeatChargeMixConsumption (text)
- SP_Xbatch_SplitsBillets_From_CCM_To_Inventory
- SP_Xbatch_YMS_AssignBilletsToStack
- SP_Xbatch_YMS_U_OutwardLocation
- XBatch_I_Material_Consume_NoBOM_USP (text)
- XBatch_I_Material_Consume_USP
- XBatch_I_Material_Inventory_Transfer_USP
- XBatch_I_Material_Inventory_USP
- XBatch_I_Material_Produce_NoBOM_USP (text)
- XBatch_I_Material_Produce_USP
- XBatch_Material_Consumed_Split_Usp
- XBatch_Material_Split_Usp
- XBatch_Material_Transfer_Usp
- XMES_I_ByProduct_Trn_Usp (text)
- XMES_I_SAP_Billet_Production_Trn (text)
- XMES_I_SAP_GLS_LS_Consumption_Trn_Usp (text)
- XMES_I_SAP_GLS_LS_Production_Trn_Usp (text)
- XMES_LRF_I_Raw_Material_Cons_Usp (text)
- XMES_RM_Raw_Material_Entry_Usp
- XMES_U_Inventory_Master_byTrn_Usp
- XSTUDIO_WORKFLOW_24F2F246-218B-40A0-99DB-EC15F3350D4E_SP (text)

## Read by

- AllocateBilletsToStacksByBilletNo
- BilletsPosition_InFurnace_Usp
- HeatChargeMixConsumption
- SP_XBatch_YMS_BilletsTransferSummary
- SP_XBatch_YMS_Display_HeatNo_Wise_Total_Billet
- SP_XBatch_YMS_TransferIntoHistory
- SP_Xbatch_SplitsBillets_From_CCM_To_Inventory
- SP_Xbatch_YMS_AssignBilletsToStack
- SP_Xbatch_YMS_U_OutwardLocation
- XBatch_Get_Location_By_Grade_Usp
- XBatch_I_Material_Consume_USP
- XBatch_I_Material_Inventory_Transfer_USP
- XBatch_Material_Consumed_Split_Usp
- XBatch_Material_Consumed_Split_Validate_Usp
- XBatch_Material_Lot_Sublot_Validate_Usp
- XBatch_Material_Split_Usp
- XBatch_Material_Transfer_Usp
- XBatch_RM_BilletInventoryView_Location_U_Usp
- XBatch_RM_ItemsOfMaterial_In_Inventory_BOM_Usp
- XMES_I_PlantToPlantTransfer_Usp
- XMES_LRF_I_Raw_Material_Cons_Usp
- XMES_RM_Raw_Material_Entry_Usp
- XMES_U_Inventory_Master_byTrn_Usp
- XSTUDIO_WORKFLOW_24F2F246-218B-40A0-99DB-EC15F3350D4E_SP
- sp_YMS_U_Location_Heatwise

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
- LocationType varchar(100)
- LocationID varchar(36)
- LocationName varchar(100)
- IsExpired bit
- ExpiryDate date
- ReceivedDate datetime
- Vendor varchar(100)
- PONumber varchar(100)
- GRNNumber varchar(100)
- InvoiceNumber varchar(100)
- Price decimal
- Description varchar(1000)
- OperationID varchar(36)
- ItemSource varchar(50)
- Remark varchar(1000)
- LotwiseBillet varchar(100)
- SrNo varchar(100)
- MaterialGrade varchar(100)
- AvailableQuantityPrice decimal
- BilletReceivedBy varchar(100)
- StackLocation varchar(100)
- InwardDate datetime
- InwardBy varchar(36)
- MovementType varchar(100)
- OutwardLocation varchar(36)
- Outwardby varchar(36)
- OutwardDate datetime
- GradeID varchar(50)
- outwardremarks varchar(-1)
- Color varchar(100)
- LayerNo varchar(100)
- BilletLength int
- PlantName varchar(36)
- StorageLocation varchar(36)
- IsPlantToPlantTransfer bit
- QuantityinCount int
- PostingMaterialType varchar(100)
