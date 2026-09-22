# XStudio_Xbatch.dbo.XMES_RM_Production_Data

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference end, byproduct, batch, billet, bundle, consume, consumed, cut, extra, heat, hot, length.

**Primary Key:** ID  
**Row Count:** 821  
**Date Range (ModifiedOn):** 2026-08-12T14:53:49.0000000 to 2026-08-12T14:53:49.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Workorderid | varchar | YES | -1 | — |
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
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| EndProductid | varchar | YES | -1 | — |
| BilletNo | varchar | YES | 100 | — |
| BatchNo | varchar | YES | 100 | — |
| HeatNo | varchar | YES | 100 | — |
| SectionLength | varchar | YES | 100 | — |
| BundleWeightTon | decimal | YES | 18,3 | — |
| NoofPieces | int | YES | 10,0 | — |
| EndProductNo | varchar | YES | 100 | — |
| ByproductEndCut | decimal | YES | 18,3 | — |
| ByproductMillScale | decimal | YES | 18,3 | — |
| TieRodConsume | decimal | YES | 18,3 | — |
| WorkflowStatus | varchar | YES | 50 | — |
| IsSapConsumed | bit | YES | — | — |
| IsHotOut | bit | YES | — | — |
| IsExtra | bit | YES | — | — |
| IsShort | bit | YES | — | — |

### Top 10 Records

| ID | Workorderid | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0413AE9F-25ED-4C19-9571-4152AA3DA713 | 180EACB3-BBC6-4DA8-AF75-21A68771A773 | NULL | NULL | NULL | 2026-08-24T13:43:09.4100000 | NULL | False | False | NULL |
| 0411DE8A-ECE4-4A85-84EF-F7EEF688A872 | 4FE84B02-CC1C-47D4-83E4-97B969F6D293 | NULL | NULL | NULL | 2026-08-20T16:30:29.4930000 | NULL | False | False | NULL |
| 03BD4DD5-3715-4D83-96DF-DD6FA8C40290 | 180EACB3-BBC6-4DA8-AF75-21A68771A773 | NULL | NULL | NULL | 2026-08-24T08:34:12.3270000 | NULL | False | False | NULL |
| 03556FE2-6DAC-45C9-A8D8-833FC1A1E7E9 | 180EACB3-BBC6-4DA8-AF75-21A68771A773 | NULL | NULL | NULL | 2026-08-24T16:57:59.5800000 | NULL | False | False | NULL |
| 02C57587-DB62-4D29-A64D-3A9F40F50B46 | BB3D6FE9-CEBD-447F-BE45-891548BEC566 | NULL | NULL | NULL | 2026-08-24T18:37:08.6500000 | NULL | False | False | NULL |
| 0295FD6B-F182-49A9-AB1E-077121F696EA | 180EACB3-BBC6-4DA8-AF75-21A68771A773 | NULL | NULL | NULL | 2026-08-26T15:56:24.9930000 | NULL | False | False | NULL |
| 025734C3-113C-4AC9-A23C-A71962787163 | 180EACB3-BBC6-4DA8-AF75-21A68771A773 | NULL | NULL | NULL | 2026-08-26T15:55:57.5770000 | NULL | False | False | NULL |
| 02358DFF-3A42-4533-97D5-5973855A1977 | 4FE84B02-CC1C-47D4-83E4-97B969F6D293 | NULL | NULL | NULL | 2026-08-19T18:25:21.0870000 | NULL | False | False | NULL |
| 01E5DAA1-5E3C-4DC8-964C-E9B78F4F5946 | 180EACB3-BBC6-4DA8-AF75-21A68771A773 | NULL | NULL | NULL | 2026-08-24T12:03:07.8370000 | NULL | False | False | NULL |
| 0198F558-9B49-4AA1-BD6C-8107886C8224 | 4FE84B02-CC1C-47D4-83E4-97B969F6D293 | NULL | NULL | NULL | 2026-08-26T13:20:34.9030000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Workorderid | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8850F926-6FDD-4C17-9248-952CC8CD9FDF | 2E6FA9A9-67AF-4E79-A70A-D697033E33B8 | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-08-12T14:53:49.3830000 | 2026-08-12T14:53:49.0000000 | False | False | NULL |
| 0413AE9F-25ED-4C19-9571-4152AA3DA713 | 180EACB3-BBC6-4DA8-AF75-21A68771A773 | NULL | NULL | NULL | 2026-08-24T13:43:09.4100000 | NULL | False | False | NULL |
| 0411DE8A-ECE4-4A85-84EF-F7EEF688A872 | 4FE84B02-CC1C-47D4-83E4-97B969F6D293 | NULL | NULL | NULL | 2026-08-20T16:30:29.4930000 | NULL | False | False | NULL |
| 03BD4DD5-3715-4D83-96DF-DD6FA8C40290 | 180EACB3-BBC6-4DA8-AF75-21A68771A773 | NULL | NULL | NULL | 2026-08-24T08:34:12.3270000 | NULL | False | False | NULL |
| 03556FE2-6DAC-45C9-A8D8-833FC1A1E7E9 | 180EACB3-BBC6-4DA8-AF75-21A68771A773 | NULL | NULL | NULL | 2026-08-24T16:57:59.5800000 | NULL | False | False | NULL |
| 02C57587-DB62-4D29-A64D-3A9F40F50B46 | BB3D6FE9-CEBD-447F-BE45-891548BEC566 | NULL | NULL | NULL | 2026-08-24T18:37:08.6500000 | NULL | False | False | NULL |
| 0295FD6B-F182-49A9-AB1E-077121F696EA | 180EACB3-BBC6-4DA8-AF75-21A68771A773 | NULL | NULL | NULL | 2026-08-26T15:56:24.9930000 | NULL | False | False | NULL |
| 025734C3-113C-4AC9-A23C-A71962787163 | 180EACB3-BBC6-4DA8-AF75-21A68771A773 | NULL | NULL | NULL | 2026-08-26T15:55:57.5770000 | NULL | False | False | NULL |
| 02358DFF-3A42-4533-97D5-5973855A1977 | 4FE84B02-CC1C-47D4-83E4-97B969F6D293 | NULL | NULL | NULL | 2026-08-19T18:25:21.0870000 | NULL | False | False | NULL |
| 01E5DAA1-5E3C-4DC8-964C-E9B78F4F5946 | 180EACB3-BBC6-4DA8-AF75-21A68771A773 | NULL | NULL | NULL | 2026-08-24T12:03:07.8370000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_RM_Production_Data.EndProductid` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_RM_Production_Data.Workorderid` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
