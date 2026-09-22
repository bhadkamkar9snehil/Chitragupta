# XStudio_Xbatch.dbo.XMES_SMS_Event_Process_Tracker_Mst

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference duration, logic, minutes, mmss, remarks, seconds, type.

**Primary Key:** ID  
**Row Count:** 19  
**Date Range (ModifiedOn):** 2026-02-18T15:54:05.0000000 to 2026-05-04T16:46:07.0000000  

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
| DurationInSeconds | int | YES | 10,0 | — |
| DurationInMMSS | varchar | YES | 100 | — |
| DurationInMinutes | decimal | YES | 18,4 | — |
| Remarks | varchar | YES | -1 | — |
| Type | varchar | YES | 100 | — |
| Logic | varchar | YES | -1 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 241E7C16-BB1C-4D10-87E0-1AE7BBDE844D | Ladle At CCM Arm 2 Rest Position | NULL | NULL | NULL | 2026-02-09T17:25:05.2370000 | NULL | False | False | NULL |
| 0C67F461-1F0B-48E3-B94F-56619A50E70C | LRF Arcing | NULL | NULL | NULL | 2026-02-09T17:25:05.2330000 | NULL | False | False | NULL |
| 0C595AEA-6CD0-4304-AAE1-B00C777310FF | EAF Roof Open For Fill Bucket Charging | NULL | NULL | NULL | 2026-02-09T17:25:05.1830000 | NULL | False | False | NULL |
| 4DAE9F5E-D998-4299-90D2-8BBEC3D1D59A | Ladle Car Move From EAF To LRF | NULL | NULL | NULL | 2026-02-09T17:25:05.2330000 | NULL | False | False | NULL |
| 3E516296-7B33-4772-96C2-C50E2460B449 | CCM Arm 2 Casting Position | NULL | NULL | NULL | 2026-02-09T17:25:05.2370000 | NULL | False | False | NULL |
| 3868A3E6-255C-4711-8574-AA733F5C60FD | Billets Production | NULL | NULL | NULL | 2026-02-09T17:25:05.2370000 | NULL | False | False | NULL |
| 2A8DA717-1AFD-4C0E-8735-00042CBDE3F9 | Turret Rotation | NULL | NULL | NULL | 2026-02-09T17:25:05.2370000 | NULL | False | False | NULL |
| 5827B1A6-7DF8-481B-974D-5322E72C1213 | LRF Roof Close | NULL | NULL | NULL | 2026-02-09T17:25:05.2330000 | NULL | False | False | NULL |
| 6B91ECA3-73EA-42FC-8111-357A4D1BAD5B | Ladle Car At EAF | NULL | NULL | NULL | 2026-02-09T17:25:05.2300000 | NULL | False | False | NULL |
| 92B2F81A-72E1-406E-96B9-C0987D0C98A0 | Ladle Car Reach At LRF | NULL | NULL | NULL | 2026-02-09T17:25:05.2330000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3898846D-46FE-44BC-9E5D-49881D0EEADC | Tapping Delay | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 1CCC2FD3-7917-41ED-B570-39440703F6CC | 2026-04-24T17:24:22.8800000 | 2026-05-04T16:46:07.0000000 | False | False | NULL |
| 04FB497F-62C0-4D25-A5CE-74D703897055 | Bucket Charging | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-04-24T17:29:20.0370000 | 2026-04-29T08:11:37.0000000 | False | False | NULL |
| 92266D52-1994-4D41-85D1-98213687D97F | Power On | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-04-24T10:29:24.4800000 | 2026-04-29T07:52:35.0000000 | False | False | NULL |
| 7644F729-1210-4775-B34B-FD22A4F098D0 | Power Off | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-04-24T17:24:32.9800000 | 2026-04-25T12:10:33.4330000 | False | False | NULL |
| 51F76788-F9D9-474A-B51E-353DC2B95DB0 | EBT Filling | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-04-24T17:24:10.7230000 | 2026-04-25T12:09:51.0000000 | False | False | NULL |
| 28E93F57-4290-46B6-AD0B-450AAA667189 | EAF Power On | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-02-09T17:25:05.2300000 | 2026-02-18T15:54:05.0000000 | False | False | NULL |
| 4DAE9F5E-D998-4299-90D2-8BBEC3D1D59A | Ladle Car Move From EAF To LRF | NULL | NULL | NULL | 2026-02-09T17:25:05.2330000 | NULL | False | False | NULL |
| 3E516296-7B33-4772-96C2-C50E2460B449 | CCM Arm 2 Casting Position | NULL | NULL | NULL | 2026-02-09T17:25:05.2370000 | NULL | False | False | NULL |
| 3868A3E6-255C-4711-8574-AA733F5C60FD | Billets Production | NULL | NULL | NULL | 2026-02-09T17:25:05.2370000 | NULL | False | False | NULL |
| 2A8DA717-1AFD-4C0E-8735-00042CBDE3F9 | Turret Rotation | NULL | NULL | NULL | 2026-02-09T17:25:05.2370000 | NULL | False | False | NULL |

---
