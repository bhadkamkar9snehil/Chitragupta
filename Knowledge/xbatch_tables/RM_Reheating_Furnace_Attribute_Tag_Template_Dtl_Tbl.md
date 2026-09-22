# XStudio_Xbatch.dbo.RM_Reheating_Furnace_Attribute_Tag_Template_Dtl_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, type, equation, extend, transaction, bwhhh, bwhl, bwlll, gthh, ltll, retrieval.

**Primary Key:** ID  
**Row Count:** 134  
**Date Range (ModifiedOn):** 2025-09-03T15:13:10.0000000 to 2025-09-03T15:13:41.0000000  

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
| 18127E72-91DB-4D7B-946F-51A798A2A86C | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2025-09-17T16:58:23.2530000 | NULL | False | False | NULL |
| 14DDA340-4ABC-4C27-97E0-9649AD61D402 | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2025-09-16T12:51:23.8530000 | NULL | False | False | NULL |
| 146E676E-1A51-44D8-ABFE-798163182796 | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2025-10-06T08:30:12.6300000 | NULL | False | False | NULL |
| 133A05CD-1582-4767-8F89-257C991F09B4 | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2025-09-03T15:50:32.3830000 | NULL | False | False | NULL |
| 0F40C046-E687-48A1-969D-78BF9BCBED91 | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2025-09-17T16:55:02.8270000 | NULL | False | False | NULL |
| 0D393EED-351D-43B2-A832-FB71E9F7BE3C | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2025-10-06T08:31:20.9600000 | NULL | False | False | NULL |
| 0CE1FF91-76F4-481B-9DA2-A9FCB60E16FA | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2026-06-10T09:10:05.6430000 | NULL | False | False | NULL |
| 09EA40DB-108A-430F-B142-8FF8A511BE41 | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2025-09-17T17:00:52.2730000 | NULL | False | False | NULL |
| 08D59034-738B-4084-AC25-5E18973B7545 | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2025-11-26T13:31:44.5730000 | NULL | False | False | NULL |
| 07662B9F-FF74-4FFD-9151-1700B0D194DC | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2025-11-26T08:36:11.2100000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 54DE15A0-63C5-4DB2-BD90-F6EC36C016B4 | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-03T15:11:12.7670000 | 2025-09-03T15:13:41.0000000 | False | False | NULL |
| 44F463E2-D20E-4AD1-AE94-D00218668A69 | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-03T15:11:12.7670000 | 2025-09-03T15:13:32.0000000 | False | False | NULL |
| 32DC9F1B-9212-45A1-A159-F8B9207BB98C | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-03T15:11:12.7670000 | 2025-09-03T15:13:10.0000000 | False | False | NULL |
| 18127E72-91DB-4D7B-946F-51A798A2A86C | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2025-09-17T16:58:23.2530000 | NULL | False | False | NULL |
| 14DDA340-4ABC-4C27-97E0-9649AD61D402 | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2025-09-16T12:51:23.8530000 | NULL | False | False | NULL |
| 146E676E-1A51-44D8-ABFE-798163182796 | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2025-10-06T08:30:12.6300000 | NULL | False | False | NULL |
| 133A05CD-1582-4767-8F89-257C991F09B4 | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2025-09-03T15:50:32.3830000 | NULL | False | False | NULL |
| 0F40C046-E687-48A1-969D-78BF9BCBED91 | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2025-09-17T16:55:02.8270000 | NULL | False | False | NULL |
| 0D393EED-351D-43B2-A832-FB71E9F7BE3C | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2025-10-06T08:31:20.9600000 | NULL | False | False | NULL |
| 0CE1FF91-76F4-481B-9DA2-A9FCB60E16FA | NULL | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2026-06-10T09:10:05.6430000 | NULL | False | False | NULL |

---
