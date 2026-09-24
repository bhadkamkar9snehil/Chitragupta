---
type: view
title: "XStudio_Equipment_Tag_Mst_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_Equipment_Tag_Mst_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- Attribute: same values as key `Attribute`
- Attribute: same values as key `Attribute-10`
- Attribute: same values as key `Attribute-12`
- Attribute: same values as key `Attribute-2`
- Attribute: same values as key `Attribute-3`
- Attribute: same values as key `Attribute-5`
- Attribute: same values as key `Attribute-7`
- Attribute: same values as key `Attribute-8`
- Attribute: same values as key `Attribute-9`
- EquipmentID: same values as key `EquipmentID`
- TagName: same values as key `Attribute-3`
- TagName: same values as key `TagName`
- TagName: same values as key `TagName-2`
- TagName: same values as key `TagName-3`
- TagName: same values as key `TagName-4`

## Reads

- CCM_Mst_Tbl
- CCM_SMS_Mst_Tbl
- CCM_SMS_Tag_Mapping_Tbl
- CCM_Tag_Mapping_Tbl
- Communication_System_Mst_Tbl
- Communication_System_Tag_Mapping_Tbl
- EAF_SMS_Mst_Tbl
- EAF_SMS_Tag_Mapping_Tbl
- LRF_SMS_Mst_Tbl
- LRF_SMS_Tag_Mapping_Tbl
- RM_Furnace_Combustion_Mst_Tbl
- RM_Furnace_Combustion_Tag_Mapping_Tbl
- RM_Mill_Mst_Tbl
- RM_Mill_Tag_Mapping_Tbl
- RM_Rebar_Mst_Tbl
- RM_Rebar_Tag_Mapping_Tbl
- RM_Reheating_Furnace_Mst_Tbl
- RM_Reheating_Furnace_Tag_Mapping_Tbl
- RM_WRM_Mst_Tbl
- RM_WRM_Tag_Mapping_Tbl

## Read by

- XBatch_Get_All_Tags_Usp

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
- EquipmentID varchar(36)
- EquipmentName varchar(100)
- Attribute varchar(100)
- DataSourceID varchar(36)
- TagName varchar(100)
- InstrumentTag varchar(100)
- HHRange decimal
- HRange decimal
- LRange decimal
- LLRange decimal
- ColorGTHH varchar(100)
- ColorBWHHH varchar(100)
- ColorBWHL varchar(100)
- ColorBWLLL varchar(100)
- ColorLTLL varchar(100)
- DocumentGTHH varchar(8000)
- DocumentBWHHH varchar(8000)
- DocumentBWHL varchar(8000)
- DocumentBWLLL varchar(8000)
- DocumentLTLL varchar(8000)
- Type varchar(100)
- IsXBatchTag bit
- TagType varchar(9)
- FunctionType varchar(9)
