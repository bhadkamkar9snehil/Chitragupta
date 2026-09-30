---
type: table
title: "MES_Current_Batch"
built: "2026-09-24T11:36:36"
---

# MES_Current_Batch

Table in XStudio_Xbatch. Rows: 0.

## Written by

- MES_I_Small_Cut
- MES_M_Strand_TMT
- MES_M_Strand_WRM
- MES_U_MES_Current_Batch
- MES_U_TMT_Bundle
- MES_U_WRM_Bundle

## Columns

- ID varchar(36)
- WRM varchar(100)
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
- TMT varchar(100)
- WRMBundle varchar(100)
- TMT_Small_Cut varchar(100)
- TMTBundle varchar(100)
- ChargeBed varchar(100)
