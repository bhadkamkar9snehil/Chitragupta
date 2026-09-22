# XStudio_Xbatch.dbo.XStudio_Shift_Dtl_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference time, end, start.

**Primary Key:** ID  
**Row Count:** 2  

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
| SrNo | int | YES | 10,0 | — |
| StartTime | time | YES | — | — |
| EndTime | time | YES | — | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FD8B1340-5D0B-4929-A692-B5860BC37907 | B | CA85B39F-7CD2-41C8-8674-93A4A421843E | NULL | NULL | 2025-07-11T11:01:03.2370000 | NULL | False | False | NULL |
| 72034B37-6102-46CA-B758-6AA79E57464D | A | CA85B39F-7CD2-41C8-8674-93A4A421843E | NULL | NULL | 2025-07-11T11:01:03.2230000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.Shift` -> `XStudio_XBatch.XStudio_Shift_Dtl_Tbl.ID` (Many to One)
