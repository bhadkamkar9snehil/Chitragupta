# XStudio_Xbatch.dbo.CCM_ProcessTime

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** entities, event, from, map, procedure, sohar, stored, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference status, time, ccmheat, end, equipment, flow, start, work.

**Primary Key:** ID  
**Row Count:** 25,705  
**Date Range (ModifiedOn):** 2025-09-08T18:17:25.2870000 to 2026-08-12T11:12:55.0970000  

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
| CCMHeatNo | int | YES | 10,0 | — |
| WorkFlowStatus | varchar | YES | 50 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DCC23F9C-862D-44CB-BF3A-5E0FED0686BA | NULL | NULL | NULL | NULL | 2025-09-08T18:01:16.1070000 | 2025-09-08T18:17:25.2870000 | False | False | NULL |
| D32BA46E-AE4A-44CD-9920-825147B37919 | NULL | NULL | NULL | NULL | 2025-09-08T18:07:48.2130000 | 2025-09-08T18:18:26.0670000 | False | False | NULL |
| 2D9259C1-7551-425E-90F4-8B56BEA5BC0C | NULL | NULL | NULL | NULL | 2025-09-08T18:17:21.2330000 | 2025-09-08T18:18:44.3300000 | False | False | NULL |
| 595E3493-BA93-4D07-8962-C9D19C022AF6 | NULL | NULL | NULL | NULL | 2025-09-08T18:01:16.1330000 | 2025-09-08T18:47:46.3500000 | False | False | NULL |
| D113767E-431E-4C5D-96E2-4A60D91137F9 | NULL | NULL | NULL | NULL | 2025-09-08T18:18:26.1030000 | 2025-09-08T19:20:21.9570000 | False | False | NULL |
| D335FF84-311E-4D70-8243-104AB816505A | NULL | NULL | NULL | NULL | 2025-09-08T19:17:51.3970000 | 2025-09-08T19:21:24.3570000 | False | False | NULL |
| 881B390D-1759-424B-AB33-9852EB2B05EB | NULL | NULL | NULL | NULL | 2025-09-08T19:20:18.4200000 | 2025-09-08T19:21:39.0500000 | False | False | NULL |
| 0F1319AC-C8C4-42B8-A6A7-32D7B620FCA6 | NULL | NULL | NULL | NULL | 2025-09-08T18:48:00.5300000 | 2025-09-08T19:36:13.1770000 | False | False | NULL |
| 35ABE4C3-E935-461E-AF99-E43CF2EB01AC | NULL | NULL | NULL | NULL | 2025-09-08T19:21:24.3900000 | 2025-09-08T20:18:11.1030000 | False | False | NULL |
| 62CD2DBC-3452-40B2-8C22-371ACB87124F | NULL | NULL | NULL | NULL | 2025-09-08T20:12:36.3130000 | 2025-09-08T20:19:12.9770000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EACCAB16-9DD5-46A3-A190-044A19FF4F85 | NULL | NULL | NULL |  | 2026-08-12T11:12:54.9970000 | 2026-08-12T11:12:55.0970000 | False | False | NULL |
| 2656A303-7B6B-4EC1-93A3-9CAFDAB203DB | NULL | NULL | NULL |  | 2026-08-12T08:44:37.2500000 | 2026-08-12T11:11:29.7500000 | False | False | NULL |
| BB617E55-E978-47E9-BADA-182D91411209 | NULL | NULL | NULL |  | 2026-08-09T12:17:52.1000000 | 2026-08-12T08:43:12.2870000 | False | False | NULL |
| 29B01888-DD34-450C-BC11-7F5AEC761E67 | NULL | NULL | NULL |  | 2026-07-15T06:30:59.8930000 | 2026-08-09T12:19:10.3130000 | False | False | NULL |
| 65169D29-84F6-4697-A173-DA63C93A2FAF | NULL | NULL | NULL |  | 2026-07-12T05:47:40.8800000 | 2026-08-09T12:19:10.3130000 | False | False | NULL |
| F4987136-913E-4A76-8FCF-128922385852 | NULL | NULL | NULL |  | 2026-07-08T17:57:17.4300000 | 2026-08-09T12:19:10.3130000 | False | False | NULL |
| 1D870EE1-E28F-4E50-9206-1221BC3A8DFE | NULL | NULL | NULL |  | 2026-08-09T12:17:38.3200000 | 2026-08-09T12:17:42.3930000 | False | False | NULL |
| 3F31FF86-E16A-450C-8E29-AAAF070547C3 | NULL | NULL | NULL |  | 2026-08-09T12:17:26.5770000 | 2026-08-09T12:17:27.0800000 | False | False | NULL |
| 9BFCDF30-2903-45B4-AC74-E043042A1C68 | NULL | NULL | NULL |  | 2026-08-09T12:16:33.4200000 | 2026-08-09T12:16:43.1130000 | False | False | NULL |
| 5793B691-BF1A-4B42-ABC6-7D0C98E58C01 | NULL | NULL | NULL |  | 2026-07-15T06:31:00.2870000 | 2026-08-09T12:14:35.5000000 | False | False | NULL |

---
