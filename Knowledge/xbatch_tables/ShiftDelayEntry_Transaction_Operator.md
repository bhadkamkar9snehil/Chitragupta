# XStudio_Xbatch.dbo.ShiftDelayEntry_Transaction_Operator

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference shift, manager, operator, product, section.

**Primary Key:** ID  
**Row Count:** 7  
**Date Range (ModifiedOn):** 2025-09-21T12:48:48.0000000 to 2026-07-14T16:49:52.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Operator | varchar | YES | 36 | — |
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
| Shift | varchar | YES | 100 | — |
| Product | varchar | YES | 100 | — |
| Section | varchar | YES | 100 | — |
| ShiftManager | varchar | YES | 36 | — |

### Top 10 Records

| ID | Operator | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 644BC39C-012F-44D6-8BDF-9893AF5C0D4C | 24ACB9DE-730F-478B-9ECA-ED28ACA847B0 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-21T12:05:59.4270000 | 2025-09-21T12:48:48.0000000 | False | False | NULL | 172.16.2.63 |
| 01AAF020-F0B2-420A-B231-EE2DFC796B25 | F563AE5E-714D-4243-B603-A26E97562917 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-21T14:21:37.3900000 | 2025-09-21T14:21:37.0000000 | False | False | NULL | 172.16.3.178 |
| F2958272-E9E3-4874-A836-7CFA014AF3C3 | CCB3F7E1-25CE-43EA-9838-A799E8DD195E | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-24T14:46:35.5830000 | 2025-09-24T14:46:35.0000000 | False | False | NULL | 172.16.6.98 |
| 508346DC-C976-4295-A26A-E724A3E6CBC1 | 456EF9F5-605A-427F-942B-1EBE70FD2B41 | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2025-10-28T15:09:34.7300000 | 2025-10-28T15:09:34.0000000 | False | False | NULL | 172.16.2.147 |
| 61CBA2B9-B89B-4D85-A725-948121ACECD6 | 0A501912-B26B-4D8B-92B6-FE3749E1B5B4 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-05-26T14:18:24.0830000 | 2026-05-26T14:18:24.0000000 | False | False | NULL | 172.16.7.110 |
| 54582D40-90F7-4E9A-8559-53A3BB85D72C | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-03T16:20:16.7200000 | 2026-07-03T16:20:16.0000000 | False | False | NULL | 172.16.7.110 |
| 814A063B-463F-4895-A48A-B26D4AEC984D | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-14T16:49:52.6730000 | 2026-07-14T16:49:52.0000000 | False | False | NULL |  |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.ShiftDelayEntry_Transaction_Operator.Operator` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.ShiftDelayEntry_Transaction_Operator.ShiftManager` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
