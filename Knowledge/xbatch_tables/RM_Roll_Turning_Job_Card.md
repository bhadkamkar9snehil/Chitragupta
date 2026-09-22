# XStudio_Xbatch.dbo.RM_Roll_Turning_Job_Card

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference roll, datetime, dia, loading, machine, time, total, after, before, cncoperator, code, conditions.

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2025-12-05T10:30:25.0000000 to 2025-12-05T11:27:18.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CNCOperatorName | varchar | YES | 36 | — |
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
| EntryDateTime | datetime | YES | — | — |
| ReportDate | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| Shift | varchar | YES | 100 | — |
| RollNo | int | YES | 10,0 | — |
| GrooveCode | varchar | YES | 100 | — |
| StdNo | varchar | YES | 100 | — |
| RollLoadingDatetime | datetime | YES | — | — |
| JobDescription | varchar | YES | 100 | — |
| RollDiaBefore | decimal | YES | 18,4 | — |
| RollDiaAfter | decimal | YES | 18,4 | — |
| RollUnLoadingDatetime | datetime | YES | — | — |
| SetUpTime | time | YES | — | — |
| TotalMachiningTime | varchar | YES | 100 | — |
| PassConditions | varchar | YES | 100 | — |
| Remarks | varchar | YES | 100 | — |
| Machine | varchar | YES | 36 | — |
| TotalMachineTimeinMin | int | YES | 10,0 | — |
| Status | varchar | YES | 36 | — |

### Top 10 Records

| ID | CNCOperatorName | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8D819CA6-87DF-456C-A78F-1FC258833AA0 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-12-05T09:42:30.3670000 | 2025-12-05T10:30:25.0000000 | False | False | NULL |
| B631BF56-2AF0-4D87-9111-BF9E9B877120 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-12-05T10:09:26.1330000 | 2025-12-05T10:36:13.0000000 | False | False | NULL |
| 9437E9E4-1240-45DF-8A51-D5242511BE9F | 3ADE6546-3C9A-49C4-A001-234025F2F901 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-12-05T10:46:16.6570000 | 2025-12-05T10:46:16.0000000 | False | False | NULL |
| 701E9B94-8FCB-4FA9-B497-7391FBE658D3 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-27T15:26:55.6500000 | 2025-12-05T11:27:18.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Roll_Turning_Job_Card.CNCOperatorName` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
