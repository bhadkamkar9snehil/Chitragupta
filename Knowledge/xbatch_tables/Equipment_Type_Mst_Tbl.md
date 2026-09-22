# XStudio_Xbatch.dbo.Equipment_Type_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference batching, module, type, block, button, check, class, data, enabled, entity, equipment, event.

**Primary Key:** ID  
**Row Count:** 10  
**Date Range (ModifiedOn):** 2026-08-01T12:15:07.0000000 to 2026-08-14T14:36:58.0000000  

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
| GeneratePagesButton | varchar | YES | 100 | — |
| Frequency | varchar | YES | 36 | — |
| Icon | varchar | YES | 8000 | — |
| IsBatchingEntity | bit | YES | — | — |
| BatchingEquipmentClass | varchar | YES | 100 | — |
| Hierarchy | varchar | YES | 36 | — |
| IsEventCheck | bit | YES | — | — |
| BlockType | varchar | YES | 100 | — |
| DataSourceID | varchar | YES | 36 | — |
| IsHandoverEnabled | bit | YES | — | — |
| ModuleID | varchar | YES | 36 | — |
| ModuleType | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 32465e82-8dbb-4f06-8dbc-8142dc9875af | CCM | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-07-11T17:26:52.1670000 | 2026-08-01T12:15:07.0000000 | False | False | NULL |
| 40aa7b7d-0507-42bf-bf22-3e841053c72d | CCM_SMS | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-27T17:27:34.3070000 | 2026-08-01T12:15:49.0000000 | False | False | NULL |
| 8f3b6609-fc34-440b-aa38-1404b67b4119 | Communication_System | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-07-27T07:53:34.2600000 | 2026-08-01T12:18:51.0000000 | False | False | NULL |
| 554bd194-561d-4b7c-a4f3-711d5fd0756b | EAF_SMS | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-07-11T11:07:41.1000000 | 2026-08-01T12:24:59.0000000 | False | False | NULL |
| daf22a63-e305-47f0-8ff1-11521ed545e6 | LRF_SMS | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-07-22T08:35:27.0970000 | 2026-08-01T12:26:01.0000000 | False | False | NULL |
| 24dc11fb-220c-462a-9781-74439c04a85b | RM_Mill | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-16T10:04:09.4570000 | 2026-08-01T12:32:59.0000000 | False | False | NULL |
| 519bbcad-67ec-44c5-873e-44f61645ab5f | RM_Rebar | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-26T09:43:38.9200000 | 2026-08-01T12:34:05.0000000 | False | False | NULL |
| 909bd316-14f2-421e-8cda-1b2329c7f352 | RM_Reheating_Furnace | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-03T14:56:14.5130000 | 2026-08-01T12:34:50.0000000 | False | False | NULL |
| a2c96e8d-32c0-4194-99c5-898d6f2a78fd | RM_WRM | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-16T09:10:06.3130000 | 2026-08-01T12:35:59.0000000 | False | False | NULL |
| fcb43447-f8bb-42fc-a37a-f3e41ac3b9e7 | RM_Furnace_Combustion | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-08-14T12:47:04.0270000 | 2026-08-14T14:36:58.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Batch_Operation_Mst_Tbl.EquipmentTypeID` -> `XStudio_XBatch.Equipment_Type_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Recipe_Operation_Mst_Tbl.EquipmentTypeID` -> `XStudio_XBatch.Equipment_Type_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Unit_Equipment_Mst_Tbl.EquipmentTypeID` -> `XStudio_XBatch.Equipment_Type_Mst_Tbl.ID` (Many to One)
