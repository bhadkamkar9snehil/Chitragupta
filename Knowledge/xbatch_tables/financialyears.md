# XStudio_Xbatch.dbo.financialyears

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference date, end, fyname, startdate, target.

**Primary Key:** ID  
**Row Count:** 2  
**Date Range (ModifiedOn):** 2025-10-12T10:45:55.0000000 to 2026-04-09T22:00:38.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| fyname | varchar | YES | 100 | — |
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
| startdate | datetime | YES | — | — |
| EndDate | datetime | YES | — | — |
| TargetMT | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | fyname | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4AE9615A-40B7-4773-BC2E-C08DF15D5DF8 | FY 2025-26 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-08-28T17:23:52.6330000 | 2025-10-12T10:45:55.0000000 | False | False | NULL | 172.16.10.191 |
| 7386FE16-AD65-4636-ACBB-81B23F8B6BBD | FY 2026-27 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-04-09T21:59:36.5330000 | 2026-04-09T22:00:38.0000000 | False | False | NULL |  |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.ProductionMonthlyTargets.FiscalYear` -> `XStudio_XBatch.financialyears.ID` (Many to One)
