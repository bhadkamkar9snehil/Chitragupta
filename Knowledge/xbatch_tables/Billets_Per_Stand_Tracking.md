# XStudio_Xbatch.dbo.Billets_Per_Stand_Tracking

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference time, billet, end, equipment, flow, start, status, work.

**Primary Key:** ID  
**Row Count:** 2,38,343  
**Date Range (ModifiedOn):** 2025-10-30T13:32:31.0130000 to 2026-01-16T14:31:01.1530000  

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
| BilletNo | varchar | YES | 100 | — |
| WorkFlow | varchar | YES | 50 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A0871D06-6287-441E-8AA4-DB331D3B0B70 | NULL | NULL | NULL | NULL | 2025-10-30T13:32:28.0570000 | 2025-10-30T13:32:31.0130000 | False | False | NULL |
| F45EF0B2-B65F-4A49-98F2-326ADAD07899 | NULL | NULL | NULL | NULL | 2025-10-30T13:32:28.0200000 | 2025-10-30T13:32:35.0500000 | False | False | NULL |
| 2F11FBE4-D69D-49EF-8ED8-E864EF86A4EC | NULL | NULL | NULL | NULL | 2025-10-30T13:32:28.0370000 | 2025-10-30T13:32:38.0770000 | False | False | NULL |
| 54D00680-7BCB-4512-9DC6-551D0E020D8C | NULL | NULL | NULL | NULL | 2025-10-30T13:32:28.0330000 | 2025-10-30T13:32:41.1070000 | False | False | NULL |
| BC8AC5C1-A3A4-4266-BF7A-DC2BF3F02693 | NULL | NULL | NULL | NULL | 2025-10-30T13:32:28.0430000 | 2025-10-30T13:32:48.1630000 | False | False | NULL |
| 581CF22D-C089-4961-90CA-9DD4F12C6030 | NULL | NULL | NULL | NULL | 2025-10-30T13:32:28.0300000 | 2025-10-30T13:32:50.1800000 | False | False | NULL |
| E0314CFA-50F8-4173-B81F-7FD95F2357AA | NULL | NULL | NULL | NULL | 2025-10-30T13:32:28.0230000 | 2025-10-30T13:32:52.1900000 | False | False | NULL |
| 08C35BC3-02AD-48CE-9DB9-0514228F5630 | NULL | NULL | NULL | NULL | 2025-10-30T13:32:28.0300000 | 2025-10-30T13:32:54.2170000 | False | False | NULL |
| 3FD6A6C0-F65D-4FDE-98EF-E25E7B63873B | NULL | NULL | NULL | NULL | 2025-10-30T13:32:28.0270000 | 2025-10-30T13:32:56.2270000 | False | False | NULL |
| A906F116-31FE-4C04-B1D7-B03DFB35A2C7 | NULL | NULL | NULL | NULL | 2025-10-30T13:32:28.0400000 | 2025-10-30T13:32:57.3300000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 58C399D7-6453-4837-A68A-B6B7D889FE80 | NULL | NULL | NULL |  | 2026-01-16T14:29:35.8830000 | 2026-01-16T14:31:01.1530000 | False | False | NULL |
| F72DBE07-F4F5-431C-BD82-8ED97EA35AC9 | NULL | NULL | NULL |  | 2026-01-16T14:30:58.7800000 | 2026-01-16T14:30:58.8100000 | False | False | NULL |
| 483E9C2F-DE25-4062-A822-D98AD8A9EFF1 | NULL | NULL | NULL |  | 2026-01-16T14:30:54.1330000 | 2026-01-16T14:30:54.1570000 | False | False | NULL |
| D709F990-1AD5-4952-96CC-A048057ADAF1 | NULL | NULL | NULL |  | 2026-01-16T14:29:27.1270000 | 2026-01-16T14:30:54.1100000 | False | False | NULL |
| 55EECFB2-272D-4C7B-A644-0A5ACFC19CBA | NULL | NULL | NULL |  | 2026-01-16T14:29:24.1100000 | 2026-01-16T14:30:52.0970000 | False | False | NULL |
| 81190E74-952E-4B2B-848C-BB387C6186FE | NULL | NULL | NULL |  | 2026-01-16T14:30:49.0700000 | 2026-01-16T14:30:49.0930000 | False | False | NULL |
| F65E0D46-D749-423E-92D5-EEBD5CA3DA16 | NULL | NULL | NULL |  | 2026-01-16T14:29:21.0930000 | 2026-01-16T14:30:49.0470000 | False | False | NULL |
| 6878D02D-28AC-496E-9836-04C98EC95DEA | NULL | NULL | NULL |  | 2026-01-16T14:29:17.0600000 | 2026-01-16T14:30:46.0970000 | False | False | NULL |
| BC420222-202A-47A5-8AD0-179B4AD72498 | NULL | NULL | NULL |  | 2026-01-16T14:30:41.6770000 | 2026-01-16T14:30:41.7000000 | False | False | NULL |
| C10A6D79-2BAB-4F25-8409-0E3BEEE693B5 | NULL | NULL | NULL |  | 2026-01-16T14:29:12.0270000 | 2026-01-16T14:30:38.9670000 | False | False | NULL |

---
