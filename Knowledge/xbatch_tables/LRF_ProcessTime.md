# XStudio_Xbatch.dbo.LRF_ProcessTime

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** data, flow, heat, insert, lrf, per (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference time, end, equipment, heat, lrfheat, start, status.

**Primary Key:** ID  
**Row Count:** 40,881  
**Date Range (ModifiedOn):** 2025-08-19T14:02:38.8000000 to 2026-08-13T07:20:56.2400000  

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
| HeatID | decimal | YES | 18,4 | — |
| LRFHeatID | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0F54FA2D-BD90-4CEB-BB42-EDA9B7EFBAE7 | NULL | NULL | NULL | NULL | 2026-07-09T18:19:16.1870000 | NULL | False | False | NULL |
| 25EFE002-32CA-432A-A47C-EA3920981C48 | NULL | NULL | NULL | NULL | 2026-07-12T05:47:42.4730000 | NULL | False | False | NULL |
| BA583226-343E-43A4-B530-D4957662DEB3 | NULL | NULL | NULL | NULL | 2026-07-15T06:31:02.0470000 | NULL | False | False | NULL |
| C2149360-9AFA-4B97-B60B-47FD9C2DE28D | NULL | NULL | NULL | NULL | 2025-08-19T13:31:31.7570000 | 2025-08-19T14:02:38.8000000 | False | False | NULL |
| 342D99BA-B741-4309-AA29-6237234A3597 | NULL | NULL | NULL | NULL | 2025-08-19T13:32:46.8700000 | 2025-08-19T14:02:54.5800000 | False | False | NULL |
| D0D31236-C1CF-4FAF-9ABD-A6F0F2BC20CD | NULL | NULL | NULL | NULL | 2025-08-19T13:33:41.7100000 | 2025-08-19T14:02:54.5800000 | False | False | NULL |
| F54CFA04-D155-47DB-99F7-887C6728DD3C | NULL | NULL | NULL | NULL | 2025-08-19T14:02:54.5830000 | 2025-08-19T14:03:54.9170000 | False | False | NULL |
| 3E84E381-CA7D-4E2C-BAFD-E7463F9826FE | NULL | NULL | NULL | NULL | 2025-08-19T14:28:10.7370000 | 2025-08-19T15:01:51.1300000 | False | False | NULL |
| 16C0421F-595C-4B67-B7EE-A09FD601D0DE | NULL | NULL | NULL | NULL | 2025-08-19T14:29:31.5200000 | 2025-08-19T15:02:59.5970000 | False | False | NULL |
| 8D0B2C22-6B73-47D9-802B-E7520FEF9861 | NULL | NULL | NULL | NULL | 2025-08-19T14:30:28.9500000 | 2025-08-19T15:02:59.6170000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 076D538B-1373-4333-BFFA-D2F5F73A5278 | NULL | NULL | NULL | NULL | 2026-08-08T17:00:12.4570000 | 2026-08-13T07:20:56.2400000 | False | False | NULL |
| 90FCC113-24E3-42D7-A336-2F8C78134496 | NULL | NULL | NULL | NULL | 2026-07-08T18:05:01.8170000 | 2026-08-13T07:20:56.2400000 | False | False | NULL |
| 83D72162-C1AB-4C63-85BE-90ABBFD5D823 | NULL | NULL | NULL | NULL | 2026-07-08T18:07:30.3800000 | 2026-07-09T18:19:16.2030000 | False | False | NULL |
| 173CB310-569F-440B-BE25-73FCAA39655B | NULL | NULL | NULL | NULL | 2026-07-08T18:05:36.5030000 | 2026-07-08T18:07:30.3470000 | False | False | NULL |
| AC33425C-283C-4B5A-9042-B66CFBCF7EFD | NULL | NULL | NULL | NULL | 2026-07-08T17:41:37.5630000 | 2026-07-08T18:05:36.5270000 | False | False | NULL |
| 2D086976-B692-45DA-96AC-49638F91E682 | NULL | NULL | NULL | NULL | 2026-07-08T17:41:37.5670000 | 2026-07-08T17:46:21.5000000 | False | False | NULL |
| D79C9232-4726-460E-A33D-B6AEF5513D0E | NULL | NULL | NULL | NULL | 2026-07-08T17:09:03.6670000 | 2026-07-08T17:44:31.0170000 | False | False | NULL |
| DC2453F4-D189-4517-839C-97A170C8FCA3 | NULL | NULL | NULL | NULL | 2026-07-08T17:11:23.1430000 | 2026-07-08T17:41:37.5430000 | False | False | NULL |
| 3810DF90-B7FC-4640-B18D-032FD4A9A9C0 | NULL | NULL | NULL | NULL | 2026-07-08T17:09:14.4070000 | 2026-07-08T17:41:37.5200000 | False | False | NULL |
| 1405622F-F37D-4975-BA36-75C792750E37 | NULL | NULL | NULL | NULL | 2026-07-08T17:10:40.9930000 | 2026-07-08T17:41:37.4630000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.LRF_ProcessTime.EquipmentID` -> `XStudio_XBatch.LRF_SMS_Mst_Tbl.ID` (Many to One)
