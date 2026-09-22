# XStudio_Xbatch.dbo.Communication_System_Attribute_Tag_Template_Dtl_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, type, equation, extend, transaction, bwhhh, bwhl, bwlll, gthh, ltll, retrieval.

**Primary Key:** ID  
**Row Count:** 85  

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
| 19F48D75-AF0C-4ED0-83DF-4C0C0906A119 | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:46:41.8330000 | NULL | False | False | NULL |
| 12FE02A0-917C-4410-975B-49675B64E44A | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:23:16.6700000 | NULL | False | False | NULL |
| 0FB7DD53-5CAE-4DAA-9A1A-2E9570E2EBEA | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:42:02.5670000 | NULL | False | False | NULL |
| 0F9AC548-C979-42EE-B4A7-38EA5F50D726 | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:47:26.2800000 | NULL | False | False | NULL |
| 0EC299C3-FCF9-4557-9624-5739DC004CE2 | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:34:17.5100000 | NULL | False | False | NULL |
| 0BE7534E-D102-41D3-B39A-F45982AF6FEE | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:22:46.9000000 | NULL | False | False | NULL |
| 07D277F8-DB11-4854-8E60-EE7F3A8EB4F0 | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:21:39.6930000 | NULL | False | False | NULL |
| 06F3DFF8-DD13-4CBA-A247-E2037CD7181D | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:43:37.4230000 | NULL | False | False | NULL |
| 06E3B22C-7CE1-4A1C-B87F-0A2329913031 | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:31:33.9000000 | NULL | False | False | NULL |
| 038306CA-1483-4861-B25F-078617176675 | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:28:30.4270000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 19F48D75-AF0C-4ED0-83DF-4C0C0906A119 | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:46:41.8330000 | NULL | False | False | NULL |
| 12FE02A0-917C-4410-975B-49675B64E44A | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:23:16.6700000 | NULL | False | False | NULL |
| 0FB7DD53-5CAE-4DAA-9A1A-2E9570E2EBEA | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:42:02.5670000 | NULL | False | False | NULL |
| 0F9AC548-C979-42EE-B4A7-38EA5F50D726 | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:47:26.2800000 | NULL | False | False | NULL |
| 0EC299C3-FCF9-4557-9624-5739DC004CE2 | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:34:17.5100000 | NULL | False | False | NULL |
| 0BE7534E-D102-41D3-B39A-F45982AF6FEE | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:22:46.9000000 | NULL | False | False | NULL |
| 07D277F8-DB11-4854-8E60-EE7F3A8EB4F0 | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:21:39.6930000 | NULL | False | False | NULL |
| 06F3DFF8-DD13-4CBA-A247-E2037CD7181D | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:43:37.4230000 | NULL | False | False | NULL |
| 06E3B22C-7CE1-4A1C-B87F-0A2329913031 | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:31:33.9000000 | NULL | False | False | NULL |
| 038306CA-1483-4861-B25F-078617176675 | NULL | 76BD0FDA-4D35-4226-93C1-F4521C41C69E | NULL | NULL | 2026-07-27T08:28:30.4270000 | NULL | False | False | NULL |

---
