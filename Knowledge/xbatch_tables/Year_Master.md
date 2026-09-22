# XStudio_Xbatch.dbo.Year_Master

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference date, end, start.

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2026-04-09T21:57:09.0000000 to 2026-04-09T21:58:10.0000000  

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
| StartDate | datetime | YES | — | — |
| EndDate | datetime | YES | — | — |

### Top 10 Records

| ID | Name | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9B270D27-9DB5-447E-8906-5B331F01CC0B | 2027 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-04-09T21:57:09.1530000 | 2026-04-09T21:57:09.0000000 | False | False | NULL |  |
| 47A3137D-0BBB-47F6-866B-8A65EA13015D | 2026 | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-02-10T13:39:46.7900000 | 2026-04-09T21:57:54.0000000 | False | False | NULL |  |
| 8A97E235-5D7F-4991-A641-A59A621333FB | 2025 | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-02-10T13:39:02.1200000 | 2026-04-09T21:58:10.0000000 | False | False | NULL |  |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Electricity_Meter_Electricity_Rate_Tbl_Mst.Year` -> `XStudio_XBatch.Year_Master.Name` (Many to One)
- `XStudio_XBatch.Electricity_Meter_Timing.Year` -> `XStudio_XBatch.Year_Master.Name` (Many to One)
