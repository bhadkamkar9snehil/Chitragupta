# XStudio_Xbatch.dbo.RM_WRM_Event_State_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference state, flow, off, work, condition, delay, active, attribute, different, enable, error, name.

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2026-07-06T08:22:19.0000000 to 2026-07-30T17:11:12.0000000  

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

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9EC02A2C-7320-4BC0-B6F0-AE06B1E4BD03 | NULL | F1EFFCB7-3F87-4DA7-9DF5-19D505CB76D3 | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 2026-07-06T08:10:01.0000000 | 2026-07-06T08:22:19.0000000 | False | False | NULL |
| 069F5658-50E2-4B6E-94EB-710FEA938F88 | NULL | F1EFFCB7-3F87-4DA7-9DF5-19D505CB76D3 | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-03T09:13:12.0000000 | 2026-07-30T15:36:49.0000000 | False | False | NULL |
| 7A68B508-899C-46A3-B7F2-00B53215F3A7 | NULL | F1EFFCB7-3F87-4DA7-9DF5-19D505CB76D3 | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-03T09:15:52.0000000 | 2026-07-30T17:11:12.0000000 | False | False | NULL |

---
