# XStudio_Xbatch.dbo.XMES_Life_Tracker_Register_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, chain, entities, entity, from, highlights, order, production, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference srno, status.

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2026-03-06T16:33:28.0000000 to 2026-07-17T17:18:19.9700000  

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
| Status | varchar | YES | 50 | — |
| Srno | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CEA1C3D8-CFB1-46FE-A586-267A09BBC4E1 | Sequence Change | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-06T16:18:57.9500000 | 2026-03-06T16:33:28.0000000 | False | False | NULL | 100.110.87.137 |
| FD0085B5-3530-45EA-8A6B-6685FFE484F4 | LRF Heat | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-03-06T16:18:57.9500000 | 2026-07-08T17:43:17.3230000 | False | False | NULL | 100.110.87.137 |
| 8D0E1442-1B43-4281-AC79-F68EB569AF51 | CCM Heat | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-03-06T16:18:57.9500000 | 2026-07-08T18:50:38.1300000 | False | False | NULL | 100.110.87.137 |
| 92D612E4-C8EC-4310-A96F-04A5DBD4C861 | EAF Heat | NULL |  | 2026-03-06T16:18:57.9130000 | 2026-07-17T17:18:19.9700000 | False | False | NULL | 100.110.87.137 |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_Element_Life_Type_Mapping_Mst_Tbl.ParentID` -> `XStudio_XBatch.XMES_Life_Tracker_Register_Mst_Tbl.ID` (Many to One)
