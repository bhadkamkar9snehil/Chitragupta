---
type: table
title: "EAF_SMS_Tag_Mapping_Tbl"
built: "2026-09-24T11:36:36"
---

# EAF_SMS_Tag_Mapping_Tbl

Table in XStudio_Xbatch. Rows: 144.

## Identifiers it holds

- Attribute: same values as key `Attribute-2`
- TagName: same values as key `TagName-2`

## Read by

- XSTUDIO_WORKFLOW_2F446F30-57E6-4AC7-A199-42928FC388E2_SP

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
