# XStudio_Xbatch.dbo.Grade_Test_Mapping

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference name, description, grade, test.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2025-08-19T08:05:44.0000000 to 2025-08-19T08:05:44.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| GradeName | varchar | YES | 36 | — |
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
| TestName | varchar | YES | 36 | — |
| Description | varchar | YES | 72 | — |
| EntryDateTime | datetime | YES | — | — |

### Top 10 Records

| ID | GradeName | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C84991EE-6303-4665-AD65-C9151F093169 | 1C14DF3B-2EAC-4971-AB39-79AEA3E28F4B | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-19T08:05:44.0930000 | 2025-08-19T08:05:44.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Grade_Test_Mapping.GradeName` -> `XStudio_XBatch.Grade_Master.ID` (Many to One)
- `XStudio_XBatch.Grade_Test_Mapping.TestName` -> `XStudio_XBatch.Grade_Test_Master.ID` (Many to One)
