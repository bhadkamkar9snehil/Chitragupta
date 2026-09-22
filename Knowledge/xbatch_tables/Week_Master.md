# XStudio_Xbatch.dbo.Week_Master

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference number, week.

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2025-09-15T18:02:03.0000000 to 2025-09-16T11:01:40.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
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
| WeekNumber | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A33251AA-7385-4232-BCA1-C3E6E3BF6308 | Week 1 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-15T18:02:03.5470000 | 2025-09-15T18:02:03.0000000 | False | False | NULL | 172.16.6.58 |
| B23C0A0D-36C3-4AAC-8B84-80A0165DDD61 | Week 2 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-15T18:02:08.9570000 | 2025-09-15T18:02:08.0000000 | False | False | NULL | 172.16.6.58 |
| ADC4971E-C088-46B9-B72B-17151408A119 | Week 3 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-15T18:02:15.3670000 | 2025-09-15T18:02:15.0000000 | False | False | NULL | 172.16.6.58 |
| 1E404928-8BB4-46F9-84BB-3D47B66C7013 | Week 4 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-15T18:02:20.4330000 | 2025-09-15T18:02:20.0000000 | False | False | NULL | 172.16.6.58 |
| 07FCB716-82FD-42FF-9F9A-9D3E9D199D93 | Week 5 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-16T11:01:40.9870000 | 2025-09-16T11:01:40.0000000 | False | False | NULL |  |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.ProductionWeeklyTargets.Week` -> `XStudio_XBatch.Week_Master.ID` (Many to One)
