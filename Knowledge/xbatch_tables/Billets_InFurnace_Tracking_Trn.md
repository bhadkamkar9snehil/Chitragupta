# XStudio_Xbatch.dbo.Billets_InFurnace_Tracking_Trn

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference billet, grade, heat, position.

**Primary Key:** ID  
**Row Count:** 11,41,648  

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
| EntryDateTime | datetime | YES | — | — |
| ReportDate | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| BilletPosition | varchar | YES | 100 | — |
| BilletNo | varchar | YES | 100 | — |
| HeatNo | int | YES | 10,0 | — |
| Grade | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0000BC06-C1D7-44AD-8E8E-C102DBC4FAD0 | NULL | NULL | NULL | NULL | 2026-08-25T17:11:15.3100000 | NULL | False | False | NULL |
| 0000BBBC-D14D-4FEF-9C7B-8BA656F2B744 | NULL | NULL | NULL | NULL | 2026-08-03T16:32:47.4330000 | NULL | False | False | NULL |
| 0000B723-7019-48AA-85D0-3FB3DE04444B | NULL | NULL | NULL | NULL | 2026-08-01T13:43:20.9370000 | NULL | False | False | NULL |
| 0000B663-BA42-4C89-8DA5-015AFD06B8FA | NULL | NULL | NULL | NULL | 2026-08-16T06:12:56.2470000 | NULL | False | False | NULL |
| 00008E52-6EE7-4AB1-9D33-D9FD1DCE0078 | NULL | NULL | NULL | NULL | 2026-08-21T21:03:18.8730000 | NULL | False | False | NULL |
| 000086BF-6A88-43B2-8BEE-B5EBCE34A045 | NULL | NULL | NULL | NULL | 2026-08-05T03:55:38.3400000 | NULL | False | False | NULL |
| 00007A8F-3EE6-4375-8805-7014D93D108D | NULL | NULL | NULL | NULL | 2026-08-26T20:39:01.4530000 | NULL | False | False | NULL |
| 000069C6-386D-4D0E-8B62-0F3937AA0B46 | NULL | NULL | NULL | NULL | 2026-08-15T08:20:19.9870000 | NULL | False | False | NULL |
| 00005B83-2CF1-469F-AF7B-95DEA0437E7A | NULL | NULL | NULL | NULL | 2026-08-09T20:07:44.7400000 | NULL | False | False | NULL |
| 000033AC-820A-47D7-8FF9-D2035E676D9A | NULL | NULL | NULL | NULL | 2026-08-01T09:14:34.4470000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0000BC06-C1D7-44AD-8E8E-C102DBC4FAD0 | NULL | NULL | NULL | NULL | 2026-08-25T17:11:15.3100000 | NULL | False | False | NULL |
| 0000BBBC-D14D-4FEF-9C7B-8BA656F2B744 | NULL | NULL | NULL | NULL | 2026-08-03T16:32:47.4330000 | NULL | False | False | NULL |
| 0000B723-7019-48AA-85D0-3FB3DE04444B | NULL | NULL | NULL | NULL | 2026-08-01T13:43:20.9370000 | NULL | False | False | NULL |
| 0000B663-BA42-4C89-8DA5-015AFD06B8FA | NULL | NULL | NULL | NULL | 2026-08-16T06:12:56.2470000 | NULL | False | False | NULL |
| 00008E52-6EE7-4AB1-9D33-D9FD1DCE0078 | NULL | NULL | NULL | NULL | 2026-08-21T21:03:18.8730000 | NULL | False | False | NULL |
| 000086BF-6A88-43B2-8BEE-B5EBCE34A045 | NULL | NULL | NULL | NULL | 2026-08-05T03:55:38.3400000 | NULL | False | False | NULL |
| 00007A8F-3EE6-4375-8805-7014D93D108D | NULL | NULL | NULL | NULL | 2026-08-26T20:39:01.4530000 | NULL | False | False | NULL |
| 000069C6-386D-4D0E-8B62-0F3937AA0B46 | NULL | NULL | NULL | NULL | 2026-08-15T08:20:19.9870000 | NULL | False | False | NULL |
| 00005B83-2CF1-469F-AF7B-95DEA0437E7A | NULL | NULL | NULL | NULL | 2026-08-09T20:07:44.7400000 | NULL | False | False | NULL |
| 000033AC-820A-47D7-8FF9-D2035E676D9A | NULL | NULL | NULL | NULL | 2026-08-01T09:14:34.4470000 | NULL | False | False | NULL |

---
