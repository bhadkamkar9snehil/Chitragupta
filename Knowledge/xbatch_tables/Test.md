# XStudio_Xbatch.dbo.Test

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference name.

**Primary Key:** ID  
**Row Count:** 6,009  
**Date Range (ModifiedOn):** 2026-09-11T13:49:48.0000000 to 2026-09-11T13:49:48.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name1 | varchar | YES | 100 | — |
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
| name2 | varchar | YES | 100 | — |
| name3 | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name1 | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 008BE124-EFD7-4C5B-BC62-C16C91BA1364 | cvdvdv | NULL | NULL | NULL | 2026-09-11T14:01:30.7930000 | NULL | False | False | NULL |
| 00605B33-D700-472B-AB6F-399550015D18 | cvdvdv | NULL | NULL | NULL | 2026-09-11T14:01:30.1500000 | NULL | False | False | NULL |
| 00597ACB-1830-41F4-BB21-0FEB7A22F4B3 | cvdvdv | NULL | NULL | NULL | 2026-09-11T14:01:29.6100000 | NULL | False | False | NULL |
| 0048297B-6A52-4AAF-9C89-21B227283FB3 | cvdvdv | NULL | NULL | NULL | 2026-09-11T13:59:37.1670000 | NULL | False | False | NULL |
| 00259D90-F159-48D7-9455-50DF69C9E5C1 | cvdvdv | NULL | NULL | NULL | 2026-09-11T14:01:27.2130000 | NULL | False | False | NULL |
| 00237250-803D-489F-B294-B427516D7624 | cvdvdv | NULL | NULL | NULL | 2026-09-11T14:01:29.5770000 | NULL | False | False | NULL |
| 0020194D-6BEB-47AA-A53B-27D7E18F3E27 | cvdvdv | NULL | NULL | NULL | 2026-09-11T14:01:29.0630000 | NULL | False | False | NULL |
| 0017644A-B889-4FC0-BAE4-13AE4EE331B3 | cvdvdv | NULL | NULL | NULL | 2026-09-11T14:01:31.2030000 | NULL | False | False | NULL |
| 001221B3-BD2C-44F1-886C-D8B9ACA7F587 | cvdvdv | NULL | NULL | NULL | 2026-09-11T14:01:28.8070000 | NULL | False | False | NULL |
| 0009D529-2E41-4BAE-AA0B-06C461AD766D | cvdvdv | NULL | NULL | NULL | 2026-09-11T14:01:29.3800000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name1 | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 52CC7D4F-5834-40A4-8664-9EEAD110D09D |  d d | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-09-11T13:49:48.5700000 | 2026-09-11T13:49:48.0000000 | False | False | NULL |
| 008BE124-EFD7-4C5B-BC62-C16C91BA1364 | cvdvdv | NULL | NULL | NULL | 2026-09-11T14:01:30.7930000 | NULL | False | False | NULL |
| 00605B33-D700-472B-AB6F-399550015D18 | cvdvdv | NULL | NULL | NULL | 2026-09-11T14:01:30.1500000 | NULL | False | False | NULL |
| 00597ACB-1830-41F4-BB21-0FEB7A22F4B3 | cvdvdv | NULL | NULL | NULL | 2026-09-11T14:01:29.6100000 | NULL | False | False | NULL |
| 0048297B-6A52-4AAF-9C89-21B227283FB3 | cvdvdv | NULL | NULL | NULL | 2026-09-11T13:59:37.1670000 | NULL | False | False | NULL |
| 00259D90-F159-48D7-9455-50DF69C9E5C1 | cvdvdv | NULL | NULL | NULL | 2026-09-11T14:01:27.2130000 | NULL | False | False | NULL |
| 00237250-803D-489F-B294-B427516D7624 | cvdvdv | NULL | NULL | NULL | 2026-09-11T14:01:29.5770000 | NULL | False | False | NULL |
| 0020194D-6BEB-47AA-A53B-27D7E18F3E27 | cvdvdv | NULL | NULL | NULL | 2026-09-11T14:01:29.0630000 | NULL | False | False | NULL |
| 0017644A-B889-4FC0-BAE4-13AE4EE331B3 | cvdvdv | NULL | NULL | NULL | 2026-09-11T14:01:31.2030000 | NULL | False | False | NULL |
| 001221B3-BD2C-44F1-886C-D8B9ACA7F587 | cvdvdv | NULL | NULL | NULL | 2026-09-11T14:01:28.8070000 | NULL | False | False | NULL |

---
