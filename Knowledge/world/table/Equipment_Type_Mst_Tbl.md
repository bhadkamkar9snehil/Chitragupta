---
type: table
title: "Equipment_Type_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# Equipment_Type_Mst_Tbl

Table in XStudio_Xbatch. Rows: 10.

## Read by

- XBatch_Generate_Recipe_Phase_Parameter_By_Equipment_Type_Usp
- XBatch_Get_Batch_Equipment_Tag_Usp
- XBatch_Get_Capability_By_Type_And_Template_Usp
- XBatch_Get_Equipment_Template_Tag_Usp
- XBatch_Get_Location_By_Type_Usp
- XBatch_Get_Tag_Mapping_Entries_By_Page_Type_Usp
- XBatch_Get_Template_By_EquipmentType_Usp

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
- GeneratePagesButton varchar(100)
- Frequency varchar(36)
- Icon varchar(8000)
- IsBatchingEntity bit
- BatchingEquipmentClass varchar(100)
- Hierarchy varchar(36)
- IsEventCheck bit
- BlockType varchar(100)
- DataSourceID varchar(36)
- IsHandoverEnabled bit
- ModuleID varchar(36)
- ModuleType varchar(100)
