---
type: table
title: "Grade_Characteristics_Mapping"
built: "2026-09-24T11:36:36"
---

# Grade_Characteristics_Mapping

Table in XStudio_Xbatch. Rows: 14.

## Written by

- Sp_Grade_Test_Mapping

## Read by

- Sp_Check_GradeTestMapping_Specifications
- Sp_Grade_Test_Mapping
- Sp_Sample_Characteristics_I_Values

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
- CharacteristicName varchar(36)
- AcceptableLowerLimit decimal
- AcceptableUpperLimit decimal
- IsAccepted varchar(100)
- IsNotAccepted varchar(100)
- TestName varchar(36)
