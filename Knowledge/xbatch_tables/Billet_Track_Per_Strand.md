# XStudio_Xbatch.dbo.Billet_Track_Per_Strand

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference count, billet, status, time, end, equipment, heat, start, strandwise, workflow.

**Primary Key:** ID  
**Row Count:** 65,510  
**Date Range (ModifiedOn):** 2026-05-22T10:02:04.0670000 to 2026-08-10T15:38:28.8000000  

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
| HeatNo | int | YES | 10,0 | — |
| StrandwiseCount | int | YES | 10,0 | — |
| S1BilletCount | int | YES | 10,0 | — |
| S2BilletCount | int | YES | 10,0 | — |
| S3BilletCount | int | YES | 10,0 | — |
| S4BilletCount | int | YES | 10,0 | — |
| S5BilletCount | int | YES | 10,0 | — |
| S6BilletCount | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8F97BF7A-F008-4621-B661-0BC87904F6FA | NULL | NULL | NULL |  | 2026-05-22T10:01:31.2400000 | 2026-05-22T10:02:04.0670000 | False | False | NULL |
| AFBAC797-6A13-4D6F-8D1E-EB2C1A766496 | NULL | NULL | NULL |  | 2026-05-22T10:02:37.4500000 | 2026-05-22T10:02:54.7970000 | False | False | NULL |
| 76F3E929-AE0E-4FA3-9789-56A78B6244FC | NULL | NULL | NULL |  | 2026-05-22T10:04:32.7130000 | 2026-05-22T10:04:46.4770000 | False | False | NULL |
| A8F8D101-1045-4026-9734-E7DEA4E41C90 | NULL | NULL | NULL |  | 2026-05-22T10:04:32.8200000 | 2026-05-22T10:04:46.5270000 | False | False | NULL |
| DC314CC2-B9E9-496B-83FE-DDEFACE64F80 | NULL | NULL | NULL |  | 2026-05-22T10:05:56.8500000 | 2026-05-22T10:06:15.6770000 | False | False | NULL |
| F898A321-D59C-473C-8EAB-38E5A83854DD | NULL | NULL | NULL |  | 2026-05-22T10:09:03.7630000 | 2026-05-22T10:09:17.5100000 | False | False | NULL |
| 7FA99859-610A-49A7-9985-4EEE9659365C | NULL | NULL | NULL |  | 2026-05-22T10:09:16.4770000 | 2026-05-22T10:09:35.3070000 | False | False | NULL |
| 20058D4E-1665-42A4-A920-1CAB4AC51633 | NULL | NULL | NULL |  | 2026-05-22T10:11:04.6370000 | 2026-05-22T10:11:21.4000000 | False | False | NULL |
| D8E6C19E-367B-4F95-87CD-730D56CC99C8 | NULL | NULL | NULL |  | 2026-05-22T10:13:15.8170000 | 2026-05-22T10:13:29.5900000 | False | False | NULL |
| 5F48741D-3BC6-40BA-8D9E-DAA88E45B464 | NULL | NULL | NULL |  | 2026-05-22T10:13:15.8870000 | 2026-05-22T10:13:29.8400000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D594A5E7-373A-424F-A4B0-3D042687064A | NULL | NULL | NULL |  | 2026-08-10T14:56:20.8400000 | 2026-08-10T15:38:28.8000000 | False | False | NULL |
| 03D763E2-A9BE-4871-AC79-BE65B4889245 | NULL | NULL | NULL |  | 2026-08-10T14:56:20.7870000 | 2026-08-10T15:38:28.7270000 | False | False | NULL |
| 9652A802-3D7A-4E2D-B1EF-F13125F125B4 | NULL | NULL | NULL |  | 2026-08-10T14:56:20.7270000 | 2026-08-10T15:38:28.6470000 | False | False | NULL |
| D68B8DC3-9DD0-496F-A543-D148D1E2DA46 | NULL | NULL | NULL |  | 2026-08-10T14:56:20.6730000 | 2026-08-10T15:38:28.5800000 | False | False | NULL |
| 5B692456-EB44-41C0-B068-7200F7549FA4 | NULL | NULL | NULL |  | 2026-08-10T14:56:20.6200000 | 2026-08-10T15:38:28.4770000 | False | False | NULL |
| 902D2385-D952-43B7-9EE4-25E84795033C | NULL | NULL | NULL |  | 2026-08-10T14:56:20.5700000 | 2026-08-10T15:38:28.3900000 | False | False | NULL |
| A6E24F7F-5DC5-46B4-96EC-D4E81BC6CF12 | NULL | NULL | NULL |  | 2026-08-10T14:56:20.2930000 | 2026-08-10T15:38:28.1500000 | False | False | NULL |
| D0C54AEE-BA9C-4438-B031-7934016AB004 | NULL | NULL | NULL |  | 2026-08-10T14:56:20.0100000 | 2026-08-10T15:38:28.0930000 | False | False | NULL |
| C8AD3AAD-0C0D-4FFF-A0BC-E05A158D5364 | NULL | NULL | NULL |  | 2026-08-10T14:56:19.7300000 | 2026-08-10T15:38:28.0370000 | False | False | NULL |
| F786F719-93A6-407A-B4B5-7CF0AF1B109D | NULL | NULL | NULL |  | 2026-08-10T14:56:19.2770000 | 2026-08-10T15:38:27.9770000 | False | False | NULL |

---
