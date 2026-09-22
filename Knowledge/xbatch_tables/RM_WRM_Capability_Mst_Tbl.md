# XStudio_Xbatch.dbo.RM_WRM_Capability_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference error, code, description, field, interlock, abort, aborted, done, held, hold, look, ready.

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
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Description | varchar | YES | -1 | — |
| IsStart | bit | YES | — | — |
| IsHold | bit | YES | — | — |
| IsRestart | bit | YES | — | — |
| IsAbort | bit | YES | — | — |
| IsReset | bit | YES | — | — |
| IsReady | bit | YES | — | — |
| IsHeld | bit | YES | — | — |
| IsRun | bit | YES | — | — |
| IsDone | bit | YES | — | — |
| IsInterlock | bit | YES | — | — |
| IsAborted | bit | YES | — | — |
| InterlockValueType | varchar | YES | 100 | — |
| ErrorCodeTag | varchar | YES | 100 | — |
| ErrorLookUpTable | varchar | YES | 100 | — |
| ErrorCodeField | varchar | YES | 100 | — |
| ErrorDescriptionField | varchar | YES | 100 | — |

---
