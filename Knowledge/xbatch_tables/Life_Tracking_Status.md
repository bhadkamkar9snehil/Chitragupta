# XStudio_Xbatch.dbo.Life_Tracking_Status

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** billets, cast, catalog, count, data, entities, entity, flow, from, highlights, insert, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference life, percentage, alert, consumed, current, heat, last, time, type, updated.

**Primary Key:** ID  
**Row Count:** 25  
**Date Range (ModifiedOn):** 2025-08-14T18:05:40.9630000 to 2026-07-08T19:30:49.1670000  

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
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Life | varchar | YES | 100 | — |
| LifeType | varchar | YES | 100 | — |
| CurrentLife | int | YES | 10,0 | — |
| ConsumedLifePercentage | decimal | YES | 18,4 | — |
| AlertPercentage | varchar | YES | 100 | — |
| HeatID | int | YES | 10,0 | — |
| LastUpdatedTime | datetime | YES | — | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 184D99F9-674F-4ED9-BADF-DE3740B769DD | NULL | NULL | NULL | NULL | 2025-08-21T18:26:50.4000000 | NULL | False | False | NULL |
| 0FF5A309-6B68-4B31-B4FB-3A7FF88D66EE | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | NULL | False | False | NULL |
| CDAF00DC-F927-40E4-A987-D9E5CF34FF38 | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | NULL | False | False | NULL |
| B1C6B337-1697-4A87-BDEE-A7698FF1EE61 | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | 2025-08-14T18:05:40.9630000 | False | False | NULL |
| B2FE6F8E-CD7C-473E-9FE0-0A907CBE8324 | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | 2025-08-14T18:05:55.3270000 | False | False | NULL |
| CDB4A84C-9923-4E44-8368-20F7FC3DF4AB | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | 2025-09-19T16:58:37.3800000 | False | False | NULL |
| 4D2730A7-8687-487E-94A8-B3D6837223FA | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | 2025-10-12T07:46:00.0530000 | False | False | NULL |
| E015971C-974B-47F7-8672-DD05E2D65E68 | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | 2025-10-15T14:25:56.4630000 | False | False | NULL |
| B23B425A-129F-4233-B024-D518E6235E06 | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | 2025-11-11T13:53:56.7400000 | False | False | NULL |
| 6EAC6E38-D74C-401A-917B-B68F93BCE75B | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | 2025-11-25T10:26:49.8300000 | True | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0E286FB4-A21A-4B1F-B35F-17676E57CE3B | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | 2026-07-08T19:30:49.1670000 | False | False | NULL |
| 0B2D2139-7DF6-4C9A-9F13-299EC4B6B72B | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | 2026-07-08T19:30:49.1670000 | False | False | NULL |
| 35346E53-4922-47A9-AC12-CE92A5F0B3BA | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | 2026-07-08T19:30:49.1670000 | False | False | NULL |
| 8C90C7FF-073A-4E39-8514-408D5D7DE908 | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | 2026-07-08T19:30:49.1670000 | False | False | NULL |
| B4E9BE58-F419-499F-A3AC-53973F1FDFBF | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | 2026-07-08T19:30:49.1670000 | False | False | NULL |
| CE063B88-331F-446A-B6C2-D02B505C1002 | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | 2026-07-08T19:30:49.1670000 | False | False | NULL |
| 52C0DBA5-3C8D-4EC4-A79F-E2E3A0EF1AD6 | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | 2026-02-16T17:54:55.3500000 | False | False | NULL |
| 6190F19F-060F-4D59-ABDB-E7EB99FB5607 | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | 2026-01-29T16:39:56.8300000 | False | False | NULL |
| 3A6D66B3-76FC-495F-88EB-2E979674B85E | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | 2026-01-29T16:39:56.8300000 | False | False | NULL |
| 4BF37A46-A8F9-41A0-B18F-FC259546789C | NULL | NULL | NULL | NULL | 2025-08-07T08:50:10.2830000 | 2026-01-29T16:39:56.8300000 | False | False | NULL |

---
