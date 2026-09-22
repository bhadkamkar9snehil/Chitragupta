# XStudio_Xbatch.dbo.Tag_Configuration

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference area, heat, isenable, mapped, srno, tag.

**Primary Key:** ID  
**Row Count:** 9  
**Date Range (ModifiedOn):** 2025-11-07T16:57:04.0000000 to 2026-06-22T17:06:03.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
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
| Name | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| Area | varchar | YES | 36 | — |
| MappedTag | varchar | YES | -1 | — |
| ParentID | varchar | YES | 36 | — |
| HeatID | decimal | YES | 18,4 | — |
| Isenable | bit | YES | — | — |
| Srno | int | YES | 10,0 | — |
| ReportDate | date | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 89AF6A55-C753-4342-A13F-9892D5B4265A | 6E7ADBA5-FE49-4BC2-9433-9FFDFE425E1A | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-08-27T16:13:59.9500000 | 2025-11-07T16:57:04.0000000 | False | False | NULL |  |  |
| 31D4DEE0-8093-4170-BFFA-5424989AB583 | 6E7ADBA5-FE49-4BC2-9433-9FFDFE425E1A | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-27T16:10:26.2170000 | 2025-11-08T08:29:01.0000000 | False | False | NULL |  |  |
| E82B5D03-5F14-4550-910E-734D689D1275 | 6E7ADBA5-FE49-4BC2-9433-9FFDFE425E1A | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-27T16:27:39.5300000 | 2025-11-08T08:30:21.0000000 | False | False | NULL |  |  |
| 7361A1D9-6185-4F73-ADA9-596BE1C9A1F3 | 6E7ADBA5-FE49-4BC2-9433-9FFDFE425E1A | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-27T16:27:54.9600000 | 2025-11-08T08:34:46.0000000 | False | False | NULL |  |  |
| 5CACF28F-8FE0-42E2-B689-D30B0245159A | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-28T12:14:08.1330000 | 2025-11-08T08:36:48.0000000 | False | False | NULL |  |  |
| D53FE05A-89B2-4744-9D4E-380B2F784B66 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-28T12:13:54.6330000 | 2025-11-08T08:39:11.0000000 | False | False | NULL |  |  |
| BC6C4ACD-7838-47E6-8264-F43973842A2A | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-28T12:14:26.8030000 | 2025-11-08T08:52:13.0000000 | False | False | NULL |  |  |
| C9A6A8E8-EA90-4AB5-9BFD-AB06C6BB4F09 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-28T12:14:51.6770000 | 2025-11-08T08:52:50.0000000 | False | False | NULL |  |  |
| 59D95CF9-5C7C-4590-A9F2-9BC1AE0D9DF2 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | AE3A3D8B-EA93-450A-934E-BABBD698DA6B | 2025-08-28T12:15:06.1530000 | 2026-06-22T17:06:03.0000000 | False | False | NULL | 10.76.5.101 |  |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Tag_Configuration.Area` -> `XStudio_XBatch.Area_Mst_Tbl.Name` (Many to One)
- `XStudio_XBatch.Tag_Configuration.HeatID` -> `XStudio_XBatch.EAF_PER_HEAT.HeatID` (Many to One)
