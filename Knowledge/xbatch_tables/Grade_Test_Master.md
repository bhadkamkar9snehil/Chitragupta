# XStudio_Xbatch.dbo.Grade_Test_Master

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference description, name, test.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2025-08-19T08:05:13.0000000 to 2025-08-19T08:05:13.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| TestName | varchar | YES | 100 | — |
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
| Description | varchar | YES | 72 | — |

### Top 10 Records

| ID | TestName | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F529F46D-729D-4591-A528-80683FE5B7F2 | CheComp Test 1 | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-19T08:05:13.0130000 | 2025-08-19T08:05:13.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.EAF_LogSheet_Quantity.TestName` -> `XStudio_XBatch.Grade_Test_Master.ID` (Many to One)
- `XStudio_XBatch.Grade_Characteristics_Mapping.TestName` -> `XStudio_XBatch.Grade_Test_Master.ID` (Many to One)
- `XStudio_XBatch.Grade_Test_Mapping.TestName` -> `XStudio_XBatch.Grade_Test_Master.ID` (Many to One)
- `XStudio_XBatch.LRF_Chemical_Composition.TestName` -> `XStudio_XBatch.Grade_Test_Master.ID` (Many to One)
