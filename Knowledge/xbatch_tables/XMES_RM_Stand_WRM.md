# XStudio_Xbatch.dbo.XMES_RM_Stand_WRM

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference status, time, end, equipment, start, workflow.

**Primary Key:** ID  
**Row Count:** 43,678  
**Date Range (ModifiedOn):** 2026-07-03T12:31:46.4400000 to 2026-08-30T19:07:16.3030000  

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
| WorkflowStatus | varchar | YES | 50 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6986F591-2CE5-45B0-B1A4-A94BA6B93CF1 | NULL | NULL | NULL | NULL | 2026-08-30T19:07:56.1670000 | NULL | False | False | NULL |
| 7265BC83-E02E-4814-B73A-E856B341E71C | NULL | NULL | NULL |  | 2026-07-03T12:31:43.7300000 | 2026-07-03T12:31:46.4400000 | False | False | NULL |
| 560A0FC7-AE4F-4B7F-827E-683196F595B3 | NULL | NULL | NULL |  | 2026-07-03T12:31:43.6830000 | 2026-07-03T12:32:22.4730000 | False | False | NULL |
| 60CE89EF-F9F5-4A82-AABD-349DF63CAE24 | NULL | NULL | NULL |  | 2026-07-03T12:32:00.4330000 | 2026-07-03T12:32:22.5100000 | False | False | NULL |
| 70DC8AE0-9F8C-431A-9D4E-DE1BF5CB4BDE | NULL | NULL | NULL |  | 2026-07-03T12:32:32.6070000 | 2026-07-03T12:33:14.2430000 | False | False | NULL |
| 4CD3713C-206E-474E-9F85-159F573A685C | NULL | NULL | NULL |  | 2026-07-03T12:32:32.5630000 | 2026-07-03T12:33:50.2530000 | False | False | NULL |
| DB8F7FF4-10EF-4080-AE34-A0CBE9439180 | NULL | NULL | NULL |  | 2026-07-03T12:33:29.3900000 | 2026-07-03T12:33:50.2830000 | False | False | NULL |
| AAC45C07-382C-4C1E-9CC4-84ECAA5857D7 | NULL | NULL | NULL |  | 2026-07-03T12:34:01.5430000 | 2026-07-03T12:34:43.1500000 | False | False | NULL |
| DF5EE424-0541-46F3-9E42-863E8161F806 | NULL | NULL | NULL |  | 2026-07-03T12:34:01.5130000 | 2026-07-03T12:35:19.2130000 | False | False | NULL |
| 741133A9-7DF1-455B-AE01-062978648C77 | NULL | NULL | NULL |  | 2026-07-03T12:34:57.2130000 | 2026-07-03T12:35:19.2600000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1E5CE08F-C153-407D-ADB6-8EF70089BB81 | NULL | NULL | NULL | NULL | 2026-08-30T19:06:31.3870000 | 2026-08-30T19:07:16.3030000 | False | False | NULL |
| D1037125-0FC7-4A84-997E-CC4493FD8A9A | NULL | NULL | NULL | NULL | 2026-08-30T17:12:57.3100000 | 2026-08-30T18:57:13.3830000 | False | False | NULL |
| 2D02896B-13F8-4DBF-A0C8-4B36DB119962 | NULL | NULL | NULL |  | 2026-08-30T18:05:28.5200000 | 2026-08-30T18:05:28.5600000 | False | False | NULL |
| 89962D3C-8704-4EE4-B2BE-5C0EC4B5D4FB | NULL | NULL | NULL |  | 2026-08-30T18:05:28.4170000 | 2026-08-30T18:05:28.4770000 | False | False | NULL |
| 48CB5D44-A574-4B77-B2C5-DE1028889BAE | NULL | NULL | NULL | NULL | 2026-08-30T12:51:25.7670000 | 2026-08-30T15:39:42.2900000 | False | False | NULL |
| A242BA1D-1B0C-49C1-BD63-2602179D8682 | NULL | NULL | NULL | NULL | 2026-08-30T10:16:27.9200000 | 2026-08-30T12:49:49.2070000 | False | False | NULL |
| 9E025F59-6862-4544-A534-62F22F6C9D8C | NULL | NULL | NULL | NULL | 2026-08-29T19:36:05.0970000 | 2026-08-30T09:54:51.8000000 | False | False | NULL |
| 4F210BDA-1267-4D33-A867-0011EB7B5385 | NULL | NULL | NULL | NULL | 2026-08-29T19:31:54.7500000 | 2026-08-29T19:33:03.8570000 | False | False | NULL |
| 8933CAF7-A418-41B3-885A-B607E4239925 | NULL | NULL | NULL | NULL | 2026-08-29T19:30:40.1030000 | 2026-08-29T19:31:51.9470000 | False | False | NULL |
| 5FE27C50-383A-4DED-849E-6AFF435BEB21 | NULL | NULL | NULL | NULL | 2026-08-29T18:38:43.9870000 | 2026-08-29T19:30:37.3200000 | False | False | NULL |

---
