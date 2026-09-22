# XStudio_Xbatch.dbo.CCM_Event_Configuration_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference event, active, entity, mst, transaction, type.

**Primary Key:** ID  
**Row Count:** 4  

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
| EventType | varchar | YES | 100 | — |
| TransactionEntity | varchar | YES | 100 | — |
| IsActive | bit | YES | — | — |
| EventMstID | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E31469BE-E764-490D-BFA7-8E4BAE685886 | CCM PER HEAT | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-07-11T17:29:44.8370000 | NULL | False | False | NULL |
| C7CA0D68-DDA9-41B0-A369-1B99FFBD4FCA | CCM_Per_Heat | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-08-21T20:53:15.8430000 | NULL | False | False | NULL |
| 662EFDDE-A612-4D27-A21B-560B0896A616 | Cast Billets Count | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-08-21T21:39:44.4070000 | NULL | False | False | NULL |
| 0BE6CB2D-7475-41B8-857D-DE0C7C1CF369 | CCM_ProcessTime | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-09-08T17:35:07.4870000 | NULL | False | False | NULL |

---
