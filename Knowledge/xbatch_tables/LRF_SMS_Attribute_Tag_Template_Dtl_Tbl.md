# XStudio_Xbatch.dbo.LRF_SMS_Attribute_Tag_Template_Dtl_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, type, equation, extend, transaction, bwhhh, bwhl, bwlll, gthh, ltll, retrieval.

**Primary Key:** ID  
**Row Count:** 57  
**Date Range (ModifiedOn):** 2025-10-14T11:04:45.5970000 to 2025-10-14T11:04:45.5970000  

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
| 274FBCA2-4516-47E6-B5E6-5345B6DC151B | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-07-22T10:22:19.5030000 | NULL | False | False | NULL |
| 21EBCE63-EF6B-4A20-B847-5304DEEBB662 | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-07-22T12:42:13.4470000 | NULL | False | False | NULL |
| 1C232ADC-B400-4261-B8D3-C13D8B53F70D | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-07-22T10:21:04.3230000 | NULL | False | False | NULL |
| 1640630C-7501-4EED-A4B0-3F9EEC373760 | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-07-22T10:23:20.8730000 | NULL | False | False | NULL |
| 12A55E56-3F16-40A8-8B9B-2ADE9E5034F8 | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-07-22T10:21:28.4470000 | NULL | False | False | NULL |
| 0FFF5155-66C1-4CB3-80A9-8B344BD047EA | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-09-22T11:00:28.2230000 | NULL | False | False | NULL |
| 0FF066D1-65C1-4DBC-AFA1-34271F06CBC2 | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2026-06-15T08:50:26.5700000 | NULL | False | False | NULL |
| 0DE5E289-F31A-475A-A854-DD4B95A1ABDA | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-07-22T13:07:46.0700000 | NULL | False | False | NULL |
| 0CEB5320-7136-4578-965F-8D5276A4BE72 | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-10-13T11:26:12.8400000 | NULL | False | False | NULL |
| 0939FF61-ADB4-4E66-AF8E-14D5F765825D | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-08-19T11:01:22.8170000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7AECCB88-2566-4C1E-989A-E409058A4102 | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-10-13T11:27:29.5130000 | 2025-10-14T11:04:45.5970000 | False | False | NULL |
| 274FBCA2-4516-47E6-B5E6-5345B6DC151B | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-07-22T10:22:19.5030000 | NULL | False | False | NULL |
| 21EBCE63-EF6B-4A20-B847-5304DEEBB662 | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-07-22T12:42:13.4470000 | NULL | False | False | NULL |
| 1C232ADC-B400-4261-B8D3-C13D8B53F70D | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-07-22T10:21:04.3230000 | NULL | False | False | NULL |
| 1640630C-7501-4EED-A4B0-3F9EEC373760 | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-07-22T10:23:20.8730000 | NULL | False | False | NULL |
| 12A55E56-3F16-40A8-8B9B-2ADE9E5034F8 | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-07-22T10:21:28.4470000 | NULL | False | False | NULL |
| 0FFF5155-66C1-4CB3-80A9-8B344BD047EA | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-09-22T11:00:28.2230000 | NULL | False | False | NULL |
| 0FF066D1-65C1-4DBC-AFA1-34271F06CBC2 | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2026-06-15T08:50:26.5700000 | NULL | False | False | NULL |
| 0DE5E289-F31A-475A-A854-DD4B95A1ABDA | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-07-22T13:07:46.0700000 | NULL | False | False | NULL |
| 0CEB5320-7136-4578-965F-8D5276A4BE72 | NULL | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-10-13T11:26:12.8400000 | NULL | False | False | NULL |

---
