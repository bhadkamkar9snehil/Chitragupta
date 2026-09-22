# XStudio_Xbatch.dbo.CCM_Attribute_Tag_Template_Dtl_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, type, equation, extend, transaction, bwhhh, bwhl, bwlll, gthh, ltll, retrieval.

**Primary Key:** ID  
**Row Count:** 122  
**Date Range (ModifiedOn):** 2026-05-30T10:35:05.4730000 to 2026-05-30T10:35:05.4730000  

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
| Attribute | varchar | YES | 100 | — |
| HHRange | decimal | YES | 18,4 | — |
| HRange | decimal | YES | 18,4 | — |
| LRange | decimal | YES | 18,4 | — |
| LLRange | decimal | YES | 18,4 | — |
| ColorGTHH | varchar | YES | 100 | — |
| ColorBWHHH | varchar | YES | 100 | — |
| ColorBWHL | varchar | YES | 100 | — |
| ColorBWLLL | varchar | YES | 100 | — |
| ColorLTLL | varchar | YES | 100 | — |
| DocumentGTHH | varchar | YES | 8000 | — |
| DocumentBWHHH | varchar | YES | 8000 | — |
| DocumentBWHL | varchar | YES | 8000 | — |
| DocumentBWLLL | varchar | YES | 8000 | — |
| DocumentLTLL | varchar | YES | 8000 | — |
| ExtendRetrievalType | varchar | YES | 36 | — |
| ExtendEquationType | varchar | YES | 36 | — |
| ExtendEquation | varchar | YES | -1 | — |
| TransactionRetrievalType | varchar | YES | 36 | — |
| Procedure | varchar | YES | 36 | — |
| PWherecolumn | varchar | YES | 36 | — |
| POperator | varchar | YES | 36 | — |
| PConditionType | varchar | YES | 36 | — |
| PMSTAttribute | varchar | YES | 36 | — |
| PWhereValue | varchar | YES | 100 | — |
| IType | varchar | YES | 36 | — |
| TransactionEquationType | varchar | YES | 36 | — |
| TransactionEquation | varchar | YES | -1 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0C5CEEA8-390B-4A49-85F5-B77A29D64DFC | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-09-17T10:01:24.3000000 | NULL | False | False | NULL |
| 08EFD61A-4A7D-4CC6-9A83-6BBFDE94B42B | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-07-16T09:33:11.2500000 | NULL | False | False | NULL |
| 08BA7895-2FA6-4F8C-8631-17C0E6C3938B | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-07-16T09:27:42.7170000 | NULL | False | False | NULL |
| 07E14816-64B4-41AC-A326-A6656D7CF02F | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-07-11T17:58:01.7130000 | NULL | False | False | NULL |
| 077E2E58-3979-4B06-8D00-2A55F865D12D | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-09-17T09:50:25.8570000 | NULL | False | False | NULL |
| 0719A215-6705-465A-BA5A-CB83B647BABE | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-09-17T10:31:45.7000000 | NULL | False | False | NULL |
| 0559678F-31B0-4216-B5DB-12A91348D566 | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-09-17T09:51:53.2730000 | NULL | False | False | NULL |
| 045992BA-6236-41AE-A658-209C6FA1FB7F | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-10-01T10:40:15.9400000 | NULL | False | False | NULL |
| 03F941C7-89FD-4881-943D-D0C86DE7D2BD | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-07-21T16:20:04.6370000 | NULL | False | False | NULL |
| 01203BE2-C8F3-4703-80AB-4311CFE00618 | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-07-16T09:28:54.3870000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 85F44CCA-0ECA-4B84-AEAB-5101C1143294 | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2026-05-30T10:34:33.6900000 | 2026-05-30T10:35:05.4730000 | False | False | NULL |
| 0C5CEEA8-390B-4A49-85F5-B77A29D64DFC | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-09-17T10:01:24.3000000 | NULL | False | False | NULL |
| 08EFD61A-4A7D-4CC6-9A83-6BBFDE94B42B | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-07-16T09:33:11.2500000 | NULL | False | False | NULL |
| 08BA7895-2FA6-4F8C-8631-17C0E6C3938B | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-07-16T09:27:42.7170000 | NULL | False | False | NULL |
| 07E14816-64B4-41AC-A326-A6656D7CF02F | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-07-11T17:58:01.7130000 | NULL | False | False | NULL |
| 077E2E58-3979-4B06-8D00-2A55F865D12D | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-09-17T09:50:25.8570000 | NULL | False | False | NULL |
| 0719A215-6705-465A-BA5A-CB83B647BABE | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-09-17T10:31:45.7000000 | NULL | False | False | NULL |
| 0559678F-31B0-4216-B5DB-12A91348D566 | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-09-17T09:51:53.2730000 | NULL | False | False | NULL |
| 045992BA-6236-41AE-A658-209C6FA1FB7F | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-10-01T10:40:15.9400000 | NULL | False | False | NULL |
| 03F941C7-89FD-4881-943D-D0C86DE7D2BD | NULL | 9B152FDC-15D9-4D29-9B10-B29C37D28A80 | NULL | NULL | 2025-07-21T16:20:04.6370000 | NULL | False | False | NULL |

---
