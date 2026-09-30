---
type: table
title: "CCM_Event_State_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# CCM_Event_State_Mst_Tbl

Table in XStudio_Xbatch. Rows: 12.

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
- StateName varchar(100)
- StateSequence int
- StateCondition varchar(-1)
- IsErrorState bit
- StateOnWorkFlow varchar(100)
- StateOffWorkFlow varchar(100)
- IsActive bit
- WorkFlowAttribute varchar(100)
- IsWorkFlowEnable bit
- StateOnDelay int
- StateOffDelay int
- IsDifferentOffCondition bit
- StateOffCondition varchar(-1)
