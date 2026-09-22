# XStudio_Xbatch.dbo.EAF_ProcessTime

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** data, eaf, flow, heat, insert, per (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference status, time, duration, end, equipment, heat, start, workflow.

**Primary Key:** ID  
**Row Count:** 51,428  
**Date Range (ModifiedOn):** 2025-07-31T14:36:19.6200000 to 2026-09-02T02:12:27.2100000  

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
| EquipmentID | varchar | YES | 36 | — |
| StartTime | datetime | YES | — | — |
| EndTime | datetime | YES | — | — |
| Status | varchar | YES | 100 | — |
| HeatID | decimal | YES | 18,4 | — |
| Duration | int | YES | 10,0 | — |
| WorkflowStatus | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2B597523-B93D-45A9-9851-766C46413B1A | NULL | NULL | NULL | NULL | 2026-09-02T02:12:38.6100000 | NULL | False | False | NULL |
| 4DE8850B-0F0C-4316-B904-58F79F6DB04D | NULL | NULL | NULL | NULL | 2026-07-08T17:59:18.9170000 | NULL | False | False | NULL |
| 5C71C0DB-AA32-46CB-AB5C-4564BB990FF0 | NULL | NULL | NULL | NULL | 2026-08-10T09:48:31.1830000 | NULL | False | False | NULL |
| CA7D1104-FF1D-4AF6-9846-D04EB2B90FBE | NULL | NULL | NULL | NULL | 2025-07-31T14:36:01.9200000 | 2025-07-31T14:36:19.6200000 | False | False | NULL |
| 53D495D2-8CD9-4BF0-B85C-3400B9965157 | NULL | NULL | NULL | NULL | 2025-07-31T14:57:10.6700000 | 2025-07-31T15:52:12.9070000 | False | False | NULL |
| 552592E8-AB3E-48D6-9B3F-A45F278CA216 | NULL | NULL | NULL | NULL | 2025-07-31T17:08:57.5230000 | 2025-07-31T17:11:37.7600000 | False | False | NULL |
| 6B5B51A8-016E-4A31-A969-38A0593571F7 | NULL | NULL | NULL | NULL | 2025-07-31T16:12:42.6800000 | 2025-07-31T17:11:37.7930000 | False | False | NULL |
| 398DCE67-C9F8-46D6-B497-9732FA6551F1 | NULL | NULL | NULL | NULL | 2025-07-31T17:12:34.6930000 | 2025-07-31T17:14:50.7930000 | False | False | NULL |
| 558343E8-EDDF-4C53-8D45-F62D817015E3 | NULL | NULL | NULL | NULL | 2025-07-31T18:05:01.5630000 | 2025-07-31T18:07:57.6300000 | False | False | NULL |
| 0FE3726E-A36B-4FF1-83ED-844530C5F1D9 | NULL | NULL | NULL | NULL | 2025-07-31T17:11:54.6930000 | 2025-07-31T18:07:57.6670000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D31E9C50-7959-4C04-8E4C-461DF00E7104 | NULL | NULL | NULL | NULL | 2026-09-01T17:10:57.4770000 | 2026-09-02T02:12:27.2100000 | False | False | NULL |
| 85449369-E716-4089-BB4C-DD5A853169F1 | NULL | NULL | NULL | NULL | 2026-09-01T08:09:15.4670000 | 2026-09-01T17:10:46.0630000 | False | False | NULL |
| 337564AC-2679-4A0E-8E16-5434F86952EC | NULL | NULL | NULL | NULL | 2026-08-31T23:07:34.1030000 | 2026-09-01T08:09:03.9770000 | False | False | NULL |
| 63CF55BB-ECBE-4B06-A3E2-A3BA59DA8043 | NULL | NULL | NULL | NULL | 2026-08-31T05:04:09.9200000 | 2026-08-31T23:07:22.9100000 | False | False | NULL |
| B451196B-9D8B-4D43-9492-117A92F54F77 | NULL | NULL | NULL | NULL | 2026-08-30T20:02:28.4070000 | 2026-08-31T05:03:58.4130000 | False | False | NULL |
| 71186CA1-F4E6-4B04-974A-070DF396A6DE | NULL | NULL | NULL | NULL | 2026-08-30T11:00:47.7170000 | 2026-08-30T20:02:17.2100000 | False | False | NULL |
| 70ED46F1-385C-48B7-A353-A21583BD4E33 | NULL | NULL | NULL | NULL | 2026-08-30T01:59:07.0200000 | 2026-08-30T11:00:36.4330000 | False | False | NULL |
| 78F2A62B-0CF9-476D-9550-476C4C84C678 | NULL | NULL | NULL | NULL | 2026-08-29T16:57:26.4000000 | 2026-08-30T01:58:55.5770000 | False | False | NULL |
| 4110491C-0D3C-42AF-8DD5-71E6BF14CD80 | NULL | NULL | NULL | NULL | 2026-08-29T07:55:45.6570000 | 2026-08-29T16:57:15.1330000 | False | False | NULL |
| B75DA044-5116-49A1-99BA-A6C1B6ED2C4F | NULL | NULL | NULL | NULL | 2026-08-28T22:54:04.8470000 | 2026-08-29T07:55:34.4270000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.EAF_ProcessTime.EquipmentID` -> `XStudio_XBatch.EAF_SMS_Mst_Tbl.ID` (Many to One)
