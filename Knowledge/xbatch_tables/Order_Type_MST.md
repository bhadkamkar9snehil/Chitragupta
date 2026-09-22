# XStudio_Xbatch.dbo.Order_Type_MST

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference code, colour, description, order, type.

**Primary Key:** ID  
**Row Count:** 8  
**Date Range (ModifiedOn):** 2025-12-10T15:00:40.0000000 to 2026-07-28T16:28:52.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| OrderType | varchar | YES | 100 | — |
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
| Description | varchar | YES | 100 | — |
| ColourCode | varchar | YES | 50 | — |

### Top 10 Records

| ID | OrderType | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 98315D65-40DB-4311-821B-3583DAD82F71 | PI01 | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-05T14:33:39.4330000 | 2025-12-10T15:00:40.0000000 | False | False | NULL |
| D68D6DA3-8CEA-4B3C-B5EC-90333E6A4736 | SS01 | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-12-05T14:33:14.7130000 | 2025-12-15T13:33:51.0000000 | False | False | NULL |
| 1ACB42BA-D5DA-4507-ABC7-8FC4C874EDEC | LI01 | NULL | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | 2026-01-28T15:14:37.2100000 | 2026-01-28T15:14:50.0000000 | False | False | NULL |
| 46253FEA-8342-47EB-B0C8-BC448B41669E | SS02 | NULL | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | 2026-01-28T15:15:16.1830000 | 2026-01-28T15:15:16.0000000 | False | False | NULL |
| 528DC3DA-B226-4DAE-8466-8E0BA2A642EE | BR02 | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-04-07T09:39:28.1800000 | 2026-04-07T09:39:28.0000000 | False | False | NULL |
| 16486D9F-3A13-4A9B-9624-890C90DEA18C | WR03 | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-04-07T09:40:01.9830000 | 2026-04-07T09:40:01.0000000 | False | False | NULL |
| 9AF48F82-032B-49C3-A00E-5AC3F64E9B02 | WR04 | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-04-07T09:40:29.7200000 | 2026-04-07T09:40:43.0000000 | False | False | NULL |
| 8EB4935C-68F2-4F2E-BCE7-873A677F8DDE | BR01 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-28T16:28:52.6770000 | 2026-07-28T16:28:52.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ManufacturingOrderType` -> `XStudio_XBatch.Order_Type_MST.OrderType` (Many to One)
