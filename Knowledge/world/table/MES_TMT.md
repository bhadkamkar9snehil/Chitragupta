---
type: table
title: "MES_TMT"
built: "2026-09-24T11:36:36"
---

# MES_TMT

Table in XStudio_Xbatch. Rows: 0.

## Written by

- MES_I_Small_Cut
- MES_M_Strand_TMT
- MES_U_TMT
- MES_U_TMT_LENGTH
- XSTUDIO_WORKFLOW_3A75D1C1-C9FA-478A-9CAD-AAB0A349751C_SP

## Read by

- MES_I_Small_Cut
- MES_M_Strand_TMT
- MES_U_TMT
- MES_U_TMT_LENGTH

## Columns

- ID varchar(36)
- BatchNo varchar(100)
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
- InTime datetime
- OutTime datetime
- IsProcessed bit
- Status varchar(50)
- CutLength decimal
- RemainLength decimal
- HeatNo varchar(100)
- BilletNo varchar(100)
- workorder varchar(36)
