# XStudio_Xbatch.dbo.Delay_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Curated domain match (performance):** Delay, OEE, downtime, shift-delay, equipment-delay, agency-delay, or performance issue.
  (source: `Knowledge/xstudio_semantic_atlas.json` domains, human-curated, not inferred)
- **Indexed under investigation keywords:** core, delay, oee, routing (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference status, time, end, equipment, flow, heat, start, work.

**Primary Key:** ID  
**Row Count:** 1,931  
**Date Range (ModifiedOn):** 2025-09-02T14:09:26.4070000 to 2026-01-06T13:38:43.0930000  

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
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| StartTime | datetime | YES | — | — |
| EndTime | datetime | YES | — | — |
| Status | varchar | YES | 100 | — |
| HeatNo | int | YES | 10,0 | — |
| WorkFlowStatus | varchar | YES | 50 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 283673D4-D2DD-433F-960F-46C40262D063 | NULL | NULL | NULL | NULL | 2025-09-02T14:09:25.3930000 | 2025-09-02T14:09:26.4070000 | False | False | NULL |
| 848A1DFC-1724-43E0-BB34-AB178592BA23 | NULL | NULL | NULL | NULL | 2025-09-02T14:18:04.4170000 | 2025-09-02T14:18:10.5200000 | False | False | NULL |
| 8B5E3576-BC07-4FA9-AC57-73846AB67D56 | NULL | NULL | NULL | NULL | 2025-09-02T15:07:43.4770000 | 2025-09-02T15:07:50.1000000 | False | False | NULL |
| AA5CF0DF-85D8-41F3-8CC0-0A8DECD242F2 | NULL | NULL | NULL | NULL | 2025-09-02T16:05:18.1870000 | 2025-09-02T16:05:24.2670000 | False | False | NULL |
| D0CB4466-76E8-44BF-B324-E9149D09DA53 | NULL | NULL | NULL | NULL | 2025-09-02T17:12:20.4500000 | 2025-09-02T17:12:24.5230000 | False | False | NULL |
| 9B53909D-3E3B-4998-BCD8-A7604F476DC1 | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-02T11:11:50.4500000 | 2025-09-02T18:06:08.2800000 | False | False | NULL |
| 6FBBEF09-AB4E-4304-9AA2-59E0512B5638 | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-02T12:09:25.2870000 | 2025-09-02T18:27:53.7500000 | False | False | NULL |
| 2D39F627-1703-4557-B1A9-264BBE85498B | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-02T13:08:55.4070000 | 2025-09-02T18:34:29.5370000 | False | False | NULL |
| 0E7F8C99-BD69-4FCC-9785-6F931B5543CD | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-02T18:50:36.1770000 | 2025-09-02T18:50:49.4430000 | False | False | NULL |
| D3863F75-A333-42DC-96D1-89F859237655 | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-02T19:51:56.2870000 | 2025-09-02T19:51:58.3670000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 57459140-A3A3-4537-B682-2E1F5E5E6C72 | NULL | NULL | NULL |  | 2026-01-06T13:36:24.2870000 | 2026-01-06T13:38:43.0930000 | False | False | NULL |
| 60013B9C-4BB5-46DF-844D-38E9AF7DD469 | NULL | NULL | NULL |  | 2026-01-06T12:39:41.5100000 | 2026-01-06T12:43:29.1900000 | False | False | NULL |
| B68852BA-2F1A-4B09-BA8D-A7F6A13E4CD6 | NULL | NULL | NULL |  | 2026-01-06T11:41:40.2370000 | 2026-01-06T11:45:52.1400000 | False | False | NULL |
| C56E3F15-2D9E-4D4F-A8A7-4A589E86F112 | NULL | NULL | NULL |  | 2026-01-06T10:43:55.3000000 | 2026-01-06T10:48:46.6670000 | False | False | NULL |
| 0FEB1972-8312-4357-9F5F-2B1EC5AAB483 | NULL | NULL | NULL |  | 2026-01-06T09:48:34.4700000 | 2026-01-06T09:51:02.4870000 | False | False | NULL |
| 1CF5EA72-4AC7-48A0-9609-3FFEDC14E4B8 | NULL | NULL | NULL |  | 2026-01-06T08:09:35.2300000 | 2026-01-06T08:56:03.6800000 | False | False | NULL |
| CC1B75AC-891E-409F-85EE-9D83ABB372A9 | NULL | NULL | NULL |  | 2026-01-06T08:52:42.3400000 | 2026-01-06T08:56:03.5870000 | False | False | NULL |
| 98530372-41CD-48C7-B29E-95EB7174F9FA | NULL | NULL | NULL |  | 2026-01-06T07:52:26.5800000 | 2026-01-06T07:55:14.2700000 | False | False | NULL |
| 6AE4D9DB-C885-474C-93BA-15E5F8835F4D | NULL | NULL | NULL |  | 2026-01-06T06:54:44.3230000 | 2026-01-06T06:58:29.4900000 | False | False | NULL |
| 11C236DE-C335-45E6-95F9-18963CDB1DE9 | NULL | NULL | NULL |  | 2026-01-06T05:04:21.2070000 | 2026-01-06T05:07:32.7400000 | False | False | NULL |

---
