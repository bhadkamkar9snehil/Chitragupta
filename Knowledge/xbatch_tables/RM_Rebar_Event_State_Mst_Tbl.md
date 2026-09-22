# XStudio_Xbatch.dbo.RM_Rebar_Event_State_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference state, flow, off, work, condition, delay, active, attribute, different, enable, error, name.

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| StateName | varchar | YES | 100 | — |
| StateSequence | int | YES | 10,0 | — |
| StateCondition | varchar | YES | -1 | — |
| IsErrorState | bit | YES | — | — |
| StateOnWorkFlow | varchar | YES | 100 | — |
| StateOffWorkFlow | varchar | YES | 100 | — |
| IsActive | bit | YES | — | — |
| WorkFlowAttribute | varchar | YES | 100 | — |
| IsWorkFlowEnable | bit | YES | — | — |
| StateOnDelay | int | YES | 10,0 | — |
| StateOffDelay | int | YES | 10,0 | — |
| IsDifferentOffCondition | bit | YES | — | — |
| StateOffCondition | varchar | YES | -1 | — |

---
