# XStudio_Xbatch.dbo.SMS_Plant_Process_EventTime

**table_kind:** production_data

### What this table is for

- **Curated domain match (heat_execution):** Heat missing, wrong EAF/LRF/CCM state, per-heat value wrong, timing, alloy, power, yield, or attribution question.
  (source: `Knowledge/xstudio_semantic_atlas.json` domains, human-curated, not inferred)
- **Indexed under investigation keywords:** area, billet, ccm, chain, confirmed, core, cross, data, entities, event, flow, from, furnace, heat, insert, map, per, plant, procedure, process, production, routing, same, sms, sohar, stored, system, time, timing, tracking, xbatch, xlsx, xstudio (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference duration, heat, status, time, actual, durationin, end, equipment, mmss, seconds, sequence, start.

**Primary Key:** ID  
**Row Count:** 1,07,569  
**Date Range (ModifiedOn):** 2025-07-31T15:26:36.7500000 to 2026-08-12T11:12:55.2430000  

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
| ActualHeatID | int | YES | 10,0 | — |
| Duration | decimal | YES | 18,4 | — |
| WorkflowStatus | varchar | YES | 50 | — |
| StateSequence | int | YES | 10,0 | — |
| DurationMMSS | varchar | YES | 100 | — |
| DurationinSeconds | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0886DA18-919E-4EB9-B5DC-7AA9C3FDB8B3 | NULL | NULL | NULL | NULL | 2026-07-15T06:31:01.7600000 | NULL | False | False | NULL |
| 22E0AF26-13AB-444B-9513-0965029FE76A | NULL | NULL | NULL | NULL | 2025-09-04T17:18:39.9870000 | NULL | False | False | NULL |
| 470893CC-F476-4AB1-94C1-99718D5724E1 | NULL | NULL | NULL | NULL | 2026-07-12T05:47:42.1630000 | NULL | False | False | NULL |
| 4E480719-8A04-4220-90B3-E8260C031882 | NULL | NULL | NULL | NULL | 2026-08-10T09:48:31.1900000 | NULL | False | False | NULL |
| 60133186-430F-48DE-9B1D-801F876F9713 | NULL | NULL | NULL | NULL | 2025-08-25T11:11:53.0130000 | NULL | False | False | NULL |
| 76AEB965-946A-4BA9-B247-2C8A1F1F9126 | NULL | NULL | NULL | NULL | 2026-07-09T18:19:16.0900000 | NULL | False | False | NULL |
| BA746960-A3AC-4885-874F-1B0DEDDB475E | NULL | NULL | NULL | NULL | 2026-08-08T17:00:12.3970000 | NULL | False | False | NULL |
| C9D70159-EE1B-4067-8E19-895C01FCC935 | NULL | NULL | NULL | NULL | 2026-07-10T17:18:56.8600000 | NULL | False | False | NULL |
| D9732DE8-8D19-4D14-9122-8FABCE3D3D74 | NULL | NULL | NULL | NULL | 2025-09-04T16:49:39.6000000 | NULL | False | False | NULL |
| E9921881-09DC-4167-8524-393F709BF90E | NULL | NULL | NULL | NULL | 2025-08-28T14:53:56.9130000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B731E11E-0EED-47F0-900A-CB1A7FE1E151 | NULL | NULL | NULL |  | 2026-08-12T11:12:55.1200000 | 2026-08-12T11:12:55.2430000 | False | False | NULL |
| F8090A1D-A176-4135-9570-E3E09E210EE3 | NULL | NULL | NULL |  | 2026-08-12T08:44:37.4200000 | 2026-08-12T11:11:29.8200000 | False | False | NULL |
| A8E21B06-EFAF-49E9-A5F5-300C5C1BF1F2 | NULL | NULL | NULL |  | 2026-08-09T12:17:52.2370000 | 2026-08-12T08:43:12.4300000 | False | False | NULL |
| A07695D7-D480-4233-B765-95BC295B4E3D | NULL | NULL | NULL | NULL | 2026-08-10T09:39:17.2430000 | 2026-08-10T09:48:25.1400000 | False | False | NULL |
| 8D7C7F06-F5C7-4447-8C4E-4BE94CF40D3E | NULL | NULL | NULL |  | 2026-07-12T05:47:42.1670000 | 2026-08-09T12:19:10.3730000 | False | False | NULL |
| 9F9BEA92-DB70-46FE-8A45-BF8A8FAB3072 | NULL | NULL | NULL |  | 2026-07-15T06:31:01.7630000 | 2026-08-09T12:19:10.3730000 | False | False | NULL |
| B852D1A1-92D5-436D-A6C3-D92620258356 | NULL | NULL | NULL |  | 2026-07-08T17:57:17.7030000 | 2026-08-09T12:19:10.3730000 | False | False | NULL |
| 7EDCB509-02F4-40A1-80D4-F5422058A9BA | NULL | NULL | NULL |  | 2026-08-09T12:17:38.3570000 | 2026-08-09T12:17:42.4300000 | False | False | NULL |
| D3D9AFC1-FC1E-4AA7-8EF6-BAB5F4AAD1B3 | NULL | NULL | NULL |  | 2026-08-09T12:17:26.6470000 | 2026-08-09T12:17:27.1170000 | False | False | NULL |
| EDA1925C-4D8D-4FAC-9011-BF510D6D2ED1 | NULL | NULL | NULL |  | 2026-08-09T12:16:33.6100000 | 2026-08-09T12:16:43.2000000 | False | False | NULL |

---
