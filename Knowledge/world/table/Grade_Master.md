---
type: table
title: "Grade_Master"
built: "2026-09-24T11:36:36"
---

# Grade_Master

Table in XStudio_Xbatch. Rows: 48.

## Identifiers it holds

- GradeName: same values as key `Grade`

## Read by

- XBatch_GetRemaningHeat_Usp
- XMES_Duplicate_Grade_Protocol_Mst_Usp
- XMES_Get_Billet_Count_USP

## Columns

- ID varchar(36)
- GradeName varchar(100)
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
- Description varchar(72)
- ColorCode varchar(50)
- GradeType varchar(36)
