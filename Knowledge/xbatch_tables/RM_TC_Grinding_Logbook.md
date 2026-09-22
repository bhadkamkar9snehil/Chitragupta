# XStudio_Xbatch.dbo.RM_TC_Grinding_Logbook

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** billet, furnace, heat, production, tracking (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference roll, grinding, time, diameter, for, taken, after, before, cncoperator, code, condition, date.

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-12-05T13:14:07.0000000 to 2025-12-05T13:14:48.0000000  

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
| CNCOperatorName | varchar | YES | 36 | — |
| Shift | varchar | YES | 100 | — |
| RingNo | varchar | YES | 36 | — |
| GrooveCode | varchar | YES | 100 | — |
| StdNo | varchar | YES | 100 | — |
| Section | varchar | YES | 100 | — |
| RollLoadingDateTime | datetime | YES | — | — |
| JobDescription | varchar | YES | 100 | — |
| RollDiameterBefore | decimal | YES | 18,4 | — |
| RollDiameterAfter | decimal | YES | 18,4 | — |
| RollUnloadingDatetime | datetime | YES | — | — |
| PassCondition | varchar | YES | 100 | — |
| Remarks | varchar | YES | 100 | — |
| NoOfGrovesGrindingDone | int | YES | 10,0 | — |
| TimeTakenForRoughGrinding | time | YES | — | — |
| TimeTakenForFinshGrinding | time | YES | — | — |
| Status | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9839C4CA-3AE9-40C7-AF3D-D34FFB489A7F | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-27T16:12:34.5830000 | 2025-12-05T13:14:07.0000000 | False | False | NULL |
| 504FFCED-082F-4E68-A113-97EB87547DF1 | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-05T09:25:51.2200000 | 2025-12-05T13:14:29.0000000 | False | False | NULL |
| E29E286A-0C47-4CC6-9E16-1774F1DBC4F8 | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-05T09:11:17.5100000 | 2025-12-05T13:14:48.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_TC_Grinding_Logbook.CNCOperatorName` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_TC_Grinding_Logbook.RingNo` -> `XStudio_XBatch.RM_Ring_No_MST.ID` (Many to One)
