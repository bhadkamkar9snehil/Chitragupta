# XStudio_Xbatch.dbo.Heat_End_Selection_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference heat, cal, first, last, time, timein, dateyyyymmdd, minutes, second, start, tap.

**Primary Key:** ID  
**Row Count:** 344  
**Date Range (ModifiedOn):** 2025-10-15T11:29:33.9330000 to 2026-09-02T01:30:08.5030000  

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
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| FirstHeatNo | int | YES | 10,0 | — |
| LastHeatNo | int | YES | 10,0 | — |
| Dateyyyymmdd | varchar | YES | 100 | — |
| FIrstHeatStartTime | datetime | YES | — | — |
| LastHeatTapTime | datetime | YES | — | — |
| CalTimeinMinutes | int | YES | 10,0 | — |
| CalTimeinSecond | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4D916F97-A014-40E1-84FF-DF93184CC721 | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2025-10-15T11:29:33.9330000 | 2025-10-15T11:29:33.9330000 | False | False | NULL |
| 91C07A80-DFC0-4AB1-8661-00BC1097EBAA | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2025-10-15T14:36:46.8870000 | 2025-10-15T14:36:46.8870000 | False | False | NULL |
| 99E38FDA-740A-46A8-921E-F9DD8A4BEB8B | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2025-10-15T14:48:58.4230000 | 2025-10-15T14:48:58.4230000 | False | False | NULL |
| FC803C08-174C-475F-B5EC-470E76EB75E4 | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2025-10-27T07:48:57.4200000 | 2025-10-27T07:48:57.4200000 | False | False | NULL |
| F638794B-A6D4-45E5-99CB-CBCF09DDF875 | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2025-10-27T08:09:50.7700000 | 2025-10-27T08:09:50.7700000 | False | False | NULL |
| 9F12EA06-5B5E-452E-8849-CEF74186BCB4 | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2025-10-27T08:10:09.4830000 | 2025-10-27T08:10:09.4830000 | False | False | NULL |
| C4A9772A-554C-43A3-B86C-0E2480DF533E | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2025-10-27T08:10:16.4630000 | 2025-10-27T08:10:16.4630000 | False | False | NULL |
| 897665B2-1632-478B-8556-71F79F22DEF2 | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2025-10-27T08:10:20.9970000 | 2025-10-27T08:10:20.9970000 | False | False | NULL |
| 485A605E-5298-4895-8467-2E0DA2A163A6 | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2025-10-27T08:10:25.7200000 | 2025-10-27T08:10:25.7200000 | False | False | NULL |
| 0F372793-F2A8-4FE7-9F76-C6BEDC948973 | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2025-10-27T08:10:29.1400000 | 2025-10-27T08:10:29.1400000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 435215B4-DB09-4C52-A60F-837726305867 | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-09-02T01:30:08.5030000 | 2026-09-02T01:30:08.5030000 | False | False | NULL |
| FF7F9154-F74B-4204-BD3F-8A4BE0E94A2E | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-09-01T01:30:09.9200000 | 2026-09-01T01:30:09.9200000 | False | False | NULL |
| 569C454A-2704-4DAA-8365-B396AA3F85F3 | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-08-31T01:30:03.5900000 | 2026-08-31T01:30:03.5900000 | False | False | NULL |
| 9AB48D13-BC02-460C-A111-1B2836D7F7DE | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-08-30T01:30:01.0230000 | 2026-08-30T01:30:01.0230000 | False | False | NULL |
| 7920020E-4323-4280-8BF2-08821C7E6CE8 | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-08-29T01:30:09.5670000 | 2026-08-29T01:30:09.5670000 | False | False | NULL |
| AACD9CDB-8C91-4F9B-B14A-A97AF88B0E5D | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-08-28T01:30:03.2930000 | 2026-08-28T01:30:03.2930000 | False | False | NULL |
| E7E0912E-7FA8-4CE6-A238-5ABD9A5F1BEC | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-08-27T01:30:02.8900000 | 2026-08-27T01:30:02.8900000 | False | False | NULL |
| C620C578-755E-4590-88C5-1F7837328D9F | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-08-26T01:30:03.8800000 | 2026-08-26T01:30:03.8800000 | False | False | NULL |
| 148E91EA-56D8-4BA9-B66A-0A289071921B | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-08-25T01:30:09.4570000 | 2026-08-25T01:30:09.4570000 | False | False | NULL |
| 66CEDB92-9B70-487F-AACD-FF151AAEDC95 | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-08-24T01:30:03.8300000 | 2026-08-24T01:30:03.8300000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Heat_End_Selection_Trn_Tbl.ModifiedBy` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
