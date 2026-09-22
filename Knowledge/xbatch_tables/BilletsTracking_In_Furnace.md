# XStudio_Xbatch.dbo.BilletsTracking_In_Furnace

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference status, time, end, equipment, flow, start, work.

**Primary Key:** ID  
**Row Count:** 67,958  
**Date Range (ModifiedOn):** 2026-07-30T12:53:19.7370000 to 2026-08-28T17:44:36.2030000  

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
| WorkFlowStatus | varchar | YES | 50 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D72FDF6D-2E41-48C0-B97E-9F8D32892FB9 | NULL | NULL | NULL | NULL | 2026-07-30T12:52:58.5230000 | 2026-07-30T12:53:19.7370000 | False | False | NULL |
| DBF7955A-7B92-49CD-AFE9-1199DF72647F | NULL | NULL | NULL | NULL | 2026-07-30T12:53:06.9070000 | 2026-07-30T12:53:22.5370000 | False | False | NULL |
| 45516701-58F0-4E3C-B416-55308782838A | NULL | NULL | NULL | NULL | 2026-07-30T12:53:06.9130000 | 2026-07-30T12:53:22.5570000 | False | False | NULL |
| AF6FE4F4-10B1-4BCE-870D-9C364E79D2FF | NULL | NULL | NULL | NULL | 2026-07-30T12:54:19.4570000 | 2026-07-30T12:54:40.6800000 | False | False | NULL |
| 94862BAD-747A-44F0-9471-F37245496FB4 | NULL | NULL | NULL | NULL | 2026-07-30T12:54:26.7130000 | 2026-07-30T12:54:42.9100000 | False | False | NULL |
| 4A56AC3F-877E-4A16-B5F0-5EFCEFDE61C1 | NULL | NULL | NULL | NULL | 2026-07-30T12:54:26.7570000 | 2026-07-30T12:54:42.9130000 | False | False | NULL |
| B0D1266E-53F7-4CBE-99A6-D7BC95510486 | NULL | NULL | NULL | NULL | 2026-07-30T12:55:37.7070000 | 2026-07-30T12:55:53.9000000 | False | False | NULL |
| 15FF807E-17E2-4460-AAA1-DD5634097494 | NULL | NULL | NULL | NULL | 2026-07-30T12:55:32.6700000 | 2026-07-30T12:55:53.9030000 | False | False | NULL |
| 96151F3E-531D-4577-BA46-8A711651452E | NULL | NULL | NULL | NULL | 2026-07-30T12:55:37.7270000 | 2026-07-30T12:55:53.9230000 | False | False | NULL |
| AED83D6B-78B6-479D-9B72-9795DC19A5DD | NULL | NULL | NULL | NULL | 2026-07-30T12:56:45.8970000 | 2026-07-30T12:57:05.5170000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 77101EC7-2CE3-45D4-BE19-4061E0009700 | NULL | NULL | NULL | NULL | 2026-08-27T04:34:17.1200000 | 2026-08-28T17:44:36.2030000 | False | False | NULL |
| FAF16151-BBAF-45C4-9CCB-D3B589AB941B | NULL | NULL | NULL | NULL | 2026-08-27T06:56:55.0670000 | 2026-08-27T06:57:11.8830000 | False | False | NULL |
| 3646757D-C315-48A5-AB40-695986E8DF38 | NULL | NULL | NULL | NULL | 2026-08-27T06:54:27.1930000 | 2026-08-27T06:54:42.9130000 | False | False | NULL |
| B95388FD-426F-4F84-8147-0967E8E3E2BD | NULL | NULL | NULL | NULL | 2026-08-27T06:52:40.4070000 | 2026-08-27T06:52:56.1600000 | False | False | NULL |
| CBA9AC2A-8870-4F82-8C36-86DF912F4A23 | NULL | NULL | NULL | NULL | 2026-08-27T06:50:55.4230000 | 2026-08-27T06:51:11.1230000 | False | False | NULL |
| 3DC31FE3-EF96-4910-ACE2-7E35695392E7 | NULL | NULL | NULL | NULL | 2026-08-27T06:49:08.0530000 | 2026-08-27T06:49:24.3630000 | False | False | NULL |
| C6163DA9-E5D9-4C00-9FDC-1300E18734A2 | NULL | NULL | NULL | NULL | 2026-08-27T06:45:20.0500000 | 2026-08-27T06:45:37.4130000 | False | False | NULL |
| 2B51E1ED-1158-4EB8-B486-1524FE0474D0 | NULL | NULL | NULL | NULL | 2026-08-27T06:43:36.1070000 | 2026-08-27T06:43:52.9930000 | False | False | NULL |
| 4A1A3219-3D98-4939-8D0E-320998B6E8A5 | NULL | NULL | NULL | NULL | 2026-08-27T06:41:13.9400000 | 2026-08-27T06:41:30.2400000 | False | False | NULL |
| 38B40D4A-7A82-4315-8B0D-3599A4D69F04 | NULL | NULL | NULL | NULL | 2026-08-27T06:10:34.0500000 | 2026-08-27T06:10:50.9400000 | False | False | NULL |

---
