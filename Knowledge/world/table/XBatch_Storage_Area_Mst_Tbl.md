---
type: table
title: "XBatch_Storage_Area_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Storage_Area_Mst_Tbl

Table in XStudio_Xbatch. Rows: 10.

## Written by

- SP_Xbatch_YMS_AssignBilletsToStack
- XBatch_I_Storage_Area_USP
- XBatch_Remove_Unused_Records_Usp
- XBatch_U_Storage_Area_USP

## Read by

- BilletsPosition_InFurnace_Usp
- SP_XBatch_YMS_BilletsTransferSummary
- SP_XBatch_YMS_TransferIntoHistory
- SP_Xbatch_YMS_AssignBilletsToStack
- SP_Xbatch_YMS_GenerateLayersForStack
- SP_Xbatch_YMS_U_OutwardLocation
- SP_YMS_StoarageCapacityDetails_With_TotalHeatNo
- XBatch_Get_Location_By_Grade_Usp
- XBatch_Get_Location_By_Type_Usp
- XBatch_I_Storage_Subarea_USP
- XBatch_Remove_Unused_Records_Usp
- XBatch_U_Storage_Area_USP
- XBatch_U_Storage_Subarea_USP

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
- Capacity decimal
- CapacityUnitID varchar(36)
- Description varchar(-1)
- IsEnabled bit
- GradeType varchar(100)
