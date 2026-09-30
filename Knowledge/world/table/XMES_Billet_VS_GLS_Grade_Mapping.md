---
type: table
title: "XMES_Billet_VS_GLS_Grade_Mapping"
built: "2026-09-24T11:36:36"
---

# XMES_Billet_VS_GLS_Grade_Mapping

Table in XStudio_Xbatch. Rows: 10.

## Read by

- XBatch_GetRemaningHeat_Usp
- XMES_Get_Billet_Count_USP
- XMES_I_SAP_Billet_Production_Trn

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
- BilletGrade varchar(36)
- GLSGrade varchar(36)
- EndproductGrade varchar(36)
