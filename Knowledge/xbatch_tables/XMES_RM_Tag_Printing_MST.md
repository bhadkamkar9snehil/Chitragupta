# XStudio_Xbatch.dbo.XMES_RM_Tag_Printing_MST

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference header, heading, main, sequence, visible, value, material, product, specification.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2026-08-18T15:11:59.0000000 to 2026-08-18T15:11:59.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Material | varchar | YES | 100 | — |
| Specification | varchar | YES | 100 | — |
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
| Product | varchar | YES | 20 | — |
| Entrydatetime | datetime | YES | — | — |
| Sequence1 | varchar | YES | 100 | — |
| Heading1 | nvarchar | YES | -1 | — |
| MainHeader1 | varchar | YES | 100 | — |
| Sequence2 | varchar | YES | 100 | — |
| Heading2 | nvarchar | YES | -1 | — |
| MainHeader2 | varchar | YES | 100 | — |
| Sequence3 | varchar | YES | 100 | — |
| Sequence4 | varchar | YES | 100 | — |
| Sequence5 | varchar | YES | 100 | — |
| Sequence6 | varchar | YES | 100 | — |
| Sequence7 | varchar | YES | 100 | — |
| Sequence8 | varchar | YES | 100 | — |
| Sequence9 | varchar | YES | 100 | — |
| Sequence10 | varchar | YES | 100 | — |
| Sequence11 | varchar | YES | 100 | — |
| Sequence12 | varchar | YES | 100 | — |
| Sequence13 | varchar | YES | 100 | — |
| Sequence14 | varchar | YES | 100 | — |
| Heading3 | nvarchar | YES | -1 | — |
| Heading4 | nvarchar | YES | -1 | — |
| Heading5 | nvarchar | YES | -1 | — |
| Heading6 | nvarchar | YES | -1 | — |
| Heading7 | nvarchar | YES | -1 | — |
| Heading8 | nvarchar | YES | -1 | — |
| Heading9 | nvarchar | YES | -1 | — |
| Heading10 | nvarchar | YES | -1 | — |
| Heading11 | nvarchar | YES | -1 | — |
| Heading12 | nvarchar | YES | -1 | — |
| Heading13 | nvarchar | YES | -1 | — |
| Heading14 | nvarchar | YES | -1 | — |
| MainHeader3 | varchar | YES | 100 | — |
| MainHeader4 | varchar | YES | 100 | — |
| MainHeader5 | varchar | YES | 100 | — |
| MainHeader6 | varchar | YES | 100 | — |
| MainHeader7 | varchar | YES | 100 | — |
| MainHeader8 | varchar | YES | 100 | — |
| MainHeader9 | varchar | YES | 100 | — |
| MainHeader10 | varchar | YES | 100 | — |
| MainHeader11 | varchar | YES | 100 | — |
| MainHeader12 | varchar | YES | 100 | — |
| MainHeader13 | nvarchar | YES | -1 | — |
| MainHeader14 | varchar | YES | 100 | — |
| isVisible1 | bit | YES | — | — |
| isVisible2 | bit | YES | — | — |
| isVisible3 | bit | YES | — | — |
| isVisible4 | bit | YES | — | — |
| isVisible5 | bit | YES | — | — |
| isVisible6 | bit | YES | — | — |
| isVisible7 | bit | YES | — | — |
| isVisible8 | bit | YES | — | — |
| isVisible9 | bit | YES | — | — |
| isVisible10 | bit | YES | — | — |
| isVisible11 | bit | YES | — | — |
| isVisible12 | bit | YES | — | — |
| isVisible13 | bit | YES | — | — |
| isVisible14 | bit | YES | — | — |
| Value3 | varchar | YES | 100 | — |
| Value4 | varchar | YES | 100 | — |
| Value5 | varchar | YES | 100 | — |
| Value6 | varchar | YES | 100 | — |
| Value7 | varchar | YES | 100 | — |
| Value8 | varchar | YES | 100 | — |
| Value9 | varchar | YES | 100 | — |
| Value10 | varchar | YES | 100 | — |
| Value11 | varchar | YES | 100 | — |
| Value12 | varchar | YES | 100 | — |
| Value13 | varchar | YES | 100 | — |
| Value14 | varchar | YES | 100 | — |

### Top 10 Records

| ID | Material | Specification | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 535D2DC4-CF0D-4407-A341-3BEA838C049E | REINFORCEMENT STEEL BAR | BS4449:2005 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-08-12T16:33:58.6170000 | 2026-08-18T15:11:59.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_RM_Tag_Printing_MST.Product` -> `XStudio_XBatch.Product_Master.Name` (Many to One)
