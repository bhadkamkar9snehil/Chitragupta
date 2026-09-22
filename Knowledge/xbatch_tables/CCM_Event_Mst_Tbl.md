# XStudio_Xbatch.dbo.CCM_Event_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference active, entity, event, transaction, type.

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2025-08-21T20:53:26.0000000 to 2025-08-21T20:53:26.0000000  

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

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9012DBCE-0795-473A-A003-95515352C508 | Cast Billets Count | 32465e82-8dbb-4f06-8dbc-8142dc9875af | 49796991-BC00-4368-8182-B39E4E6BD4A6 | NULL | 2025-08-21T21:39:44.0000000 | NULL | False | False | NULL |
| 21252BBF-B0C6-41EB-90A0-558E8B60FBB8 | CCM_ProcessTime | 32465e82-8dbb-4f06-8dbc-8142dc9875af | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | NULL | 2025-09-08T17:35:07.0000000 | NULL | False | False | NULL |
| 176EC523-5534-4B28-BCA0-9756C06A3E38 | CCM_Per_Heat | 32465e82-8dbb-4f06-8dbc-8142dc9875af | 49796991-BC00-4368-8182-B39E4E6BD4A6 | NULL | 2025-08-21T20:53:15.0000000 | NULL | False | False | NULL |
| A23539D7-057D-4D5F-B98C-A4BF75DFD39C | CCM PER HEAT | 32465e82-8dbb-4f06-8dbc-8142dc9875af | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-07-11T17:29:44.0000000 | 2025-08-21T20:53:26.0000000 | False | False | NULL |

---
