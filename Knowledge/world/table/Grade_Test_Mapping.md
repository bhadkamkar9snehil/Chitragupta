---
type: table
title: "Grade_Test_Mapping"
built: "2026-09-24T11:36:36"
---

# Grade_Test_Mapping

Table in XStudio_Xbatch. Rows: 1.

## Read by

- Sp_Grade_Test_Mapping
- sp_Prevent_GradeTestMapping_Duplicate_Entry

## Columns

- ID varchar(36)
- GradeName varchar(36)
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
- TestName varchar(36)
- Description varchar(72)
- EntryDateTime datetime
