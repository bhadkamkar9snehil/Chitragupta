---
type: table
title: "XBatch_Storage_Rack_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Storage_Rack_Mst_Tbl

Table in XStudio_Xbatch. Rows: 117.

## Written by

- SP_Xbatch_YMS_GenerateLayersForStack
- XBatch_I_Storage_Subarea_USP
- XBatch_Remove_Unused_Records_Usp
- XBatch_U_Storage_Subarea_USP

## Read by

- AllocateBilletsToStacksByBilletNo
- BilletsPosition_InFurnace_Usp
- SP_XBatch_YMS_BilletsTransferSummary
- SP_XBatch_YMS_TransferIntoHistory
- SP_Xbatch_YMS_AssignBilletsToStack
- SP_Xbatch_YMS_U_OutwardLocation
- SP_YMS_StoarageCapacityDetails_With_TotalHeatNo
- XBatch_Get_Location_By_Grade_Usp
- XBatch_Get_Location_By_Type_Usp
- XBatch_I_Material_Inventory_Transfer_USP
- XBatch_I_Material_Inventory_USP
- XBatch_RM_BilletInventoryView_Location_U_Usp
- XBatch_Remove_Unused_Records_Usp
- XBatch_U_Storage_Subarea_USP
- sp_YMS_U_Location_Heatwise

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
- Number int
- IsEnabled bit
- TotalBilletStore int
- Capacity int
- assignGradeno varchar(100)
