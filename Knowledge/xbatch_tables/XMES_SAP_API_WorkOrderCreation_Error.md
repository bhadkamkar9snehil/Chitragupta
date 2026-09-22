# XStudio_Xbatch.dbo.XMES_SAP_API_WorkOrderCreation_Error

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference message, name, body, customer, error, item, order, quantity, record, status, success, total.

**Primary Key:** ID  
**Row Count:** 20  
**Date Range (ModifiedOn):** 2026-02-10T12:37:15.6270000 to 2026-07-31T09:48:38.0700000  

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
| TransactionID | varchar | YES | 100 | — |
| RecordID | varchar | YES | 100 | — |
| Body | varchar | YES | -1 | — |
| ErrorMessage | varchar | YES | -1 | — |
| Status | varchar | YES | 50 | — |
| WorkOrderType | varchar | YES | 100 | — |
| TotalQuantity | decimal | YES | 18,2 | — |
| ItemName | varchar | YES | 100 | — |
| CustomerName | varchar | YES | 100 | — |
| SuccessMessage | varchar | YES | -1 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F467766A-6D4F-4FB1-8414-F2E0289D68B5 | NULL | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-02-10T11:50:14.0330000 | 2026-02-10T12:37:15.6270000 | False | False | NULL |
| 7BF443BD-51ED-43F2-BA8B-9325DD583882 | NULL | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-02-10T11:50:14.0330000 | 2026-02-10T14:25:44.8630000 | False | False | NULL |
| 16092DC9-3FC4-4F08-9B34-0AEBD2BF4C3A | NULL | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-02-10T11:50:14.0330000 | 2026-02-10T17:38:46.8830000 | False | False | NULL |
| 86E6BD2C-FC94-470E-B7C0-6563EC5B43EC | NULL | NULL | NULL | NULL | NULL | 2026-02-12T08:15:01.5270000 | False | False | NULL |
| 322FF78E-85F8-4491-AE2A-BC009821B47A | NULL | NULL | NULL | NULL | NULL | 2026-02-14T10:33:43.8430000 | False | False | NULL |
| 5882C23A-41B7-4F14-BC44-2D53ADFFEBB2 | NULL | NULL | NULL | NULL | NULL | 2026-02-18T14:57:45.2070000 | False | False | NULL |
| BEE82D5D-1B95-41C1-BEC4-05B2102C99DB | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-03-05T14:25:41.2530000 | 2026-03-05T14:26:34.0500000 | False | False | NULL |
| D5555824-0E7E-40FC-86C9-008B1F18DFC6 | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-03-05T14:25:41.2530000 | 2026-03-05T14:29:34.7530000 | False | False | NULL |
| B4AD7380-7005-4AF7-8F2C-12929822A1DB | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-03-05T14:25:41.2530000 | 2026-03-05T14:31:07.7630000 | False | False | NULL |
| 21CBB236-C2AE-4053-85D3-59E9052D36DD | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-03-05T14:25:41.2530000 | 2026-03-05T14:31:40.0030000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C69431D3-1E14-44D5-A1BA-4CAB9F3BE875 | NULL | NULL | NULL | NULL | NULL | 2026-07-31T09:48:38.0700000 | False | False | NULL |
| 3D88EA1F-261A-4882-8070-E8389539DF92 | NULL | NULL | NULL | NULL | NULL | 2026-07-31T09:48:07.3500000 | False | False | NULL |
| 973B2AC8-114E-4AB6-9FC9-7F54FA3C888E | NULL | NULL |  |  | 2026-07-30T12:55:13.1900000 | 2026-07-30T13:25:30.3130000 | False | False | NULL |
| 600983A8-625A-4894-A16F-C2F4D50F933E | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-06-12T08:10:57.0870000 | 2026-06-12T08:11:10.5370000 | False | False | NULL |
| 9B867C9F-6F90-46F9-931A-8EDA60EC1013 | NULL | NULL | 1CCC2FD3-7917-41ED-B570-39440703F6CC | 1CCC2FD3-7917-41ED-B570-39440703F6CC | 2026-06-04T10:20:28.3870000 | 2026-06-04T10:20:52.9770000 | False | False | NULL |
| D3BEE521-97C6-4E5A-BD64-39D0AE7277BB | NULL | NULL | NULL | NULL | NULL | 2026-04-27T13:11:51.7100000 | False | False | NULL |
| B35FB019-6112-40DD-B399-532B2516FB26 | NULL | NULL | NULL | NULL | NULL | 2026-04-23T15:27:55.2130000 | False | False | NULL |
| D40C5D0A-5800-4052-B39F-4605F0FF1C1A | NULL | NULL | NULL | NULL | NULL | 2026-04-23T15:27:24.1600000 | False | False | NULL |
| 302D96A2-5973-49AC-B1F2-C538D68FEB8C | NULL | NULL | NULL | NULL | NULL | 2026-04-23T15:26:33.0700000 | False | False | NULL |
| 81CD6A6B-63CE-416A-A6EC-64819DBC157C | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-04-02T09:59:03.5900000 | 2026-04-02T09:59:22.8770000 | False | False | NULL |

---
