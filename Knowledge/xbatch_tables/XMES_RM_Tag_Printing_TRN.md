# XStudio_Xbatch.dbo.XMES_RM_Tag_Printing_TRN

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference heading, sequence, visible, value, campaignid, material, product, specification.

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2026-08-18T15:11:59.0000000 to 2026-08-20T13:30:58.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
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
| Entrydatetime | datetime | YES | — | — |
| isVisible12 | bit | YES | — | — |
| Material | varchar | YES | 100 | — |
| Heading2 | nvarchar | YES | -1 | — |
| Heading11 | nvarchar | YES | -1 | — |
| Heading1 | nvarchar | YES | -1 | — |
| isVisible13 | bit | YES | — | — |
| Sequence10 | varchar | YES | 100 | — |
| Sequence5 | varchar | YES | 100 | — |
| isVisible6 | bit | YES | — | — |
| Heading4 | nvarchar | YES | -1 | — |
| Sequence4 | varchar | YES | 100 | — |
| Heading5 | nvarchar | YES | -1 | — |
| Sequence11 | varchar | YES | 100 | — |
| Sequence2 | varchar | YES | 100 | — |
| Sequence6 | varchar | YES | 100 | — |
| Heading3 | nvarchar | YES | -1 | — |
| Heading12 | nvarchar | YES | -1 | — |
| Sequence8 | varchar | YES | 100 | — |
| Sequence7 | varchar | YES | 100 | — |
| isVisible10 | bit | YES | — | — |
| Heading14 | nvarchar | YES | -1 | — |
| isVisible1 | bit | YES | — | — |
| Sequence3 | varchar | YES | 100 | — |
| Specification | varchar | YES | 100 | — |
| Heading8 | nvarchar | YES | -1 | — |
| Sequence1 | varchar | YES | 100 | — |
| Sequence12 | varchar | YES | 100 | — |
| isVisible4 | bit | YES | — | — |
| Product | varchar | YES | 36 | — |
| Heading13 | nvarchar | YES | -1 | — |
| isVisible7 | bit | YES | — | — |
| isVisible5 | bit | YES | — | — |
| Heading6 | nvarchar | YES | -1 | — |
| Sequence9 | varchar | YES | 100 | — |
| isVisible8 | bit | YES | — | — |
| isVisible2 | bit | YES | — | — |
| Heading10 | nvarchar | YES | -1 | — |
| Sequence13 | varchar | YES | 100 | — |
| Sequence14 | varchar | YES | 100 | — |
| isVisible14 | bit | YES | — | — |
| Heading9 | nvarchar | YES | -1 | — |
| isVisible9 | bit | YES | — | — |
| isVisible11 | bit | YES | — | — |
| Heading7 | nvarchar | YES | -1 | — |
| isVisible3 | bit | YES | — | — |
| Campaignid | varchar | YES | 100 | — |
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

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 67311006-C088-4784-A3BD-A9304DCD3933 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-08-21T15:57:57.1800000 | 2026-08-18T15:11:59.0000000 | False | False | NULL |  | NULL |
| E267EA2E-3C6E-4AA7-9211-C3F1882851EC | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-08-24T16:05:08.6300000 | 2026-08-18T15:11:59.0000000 | False | False | NULL |  | NULL |
| E1AEE528-7058-4757-947A-6CF1112599CD | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-08-21T15:53:20.4230000 | 2026-08-18T15:11:59.0000000 | False | False | NULL |  | NULL |
| C6632B1C-0065-444A-8545-FA6776DF7CA5 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-08-18T15:58:49.9900000 | 2026-08-20T13:30:58.0000000 | False | False | NULL |  | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_RM_Tag_Printing_TRN.Campaignid` -> `XStudio_XBatch.XMES_Campaign_Plan_Mst.ID` (Many to One)
- `XStudio_XBatch.XMES_RM_Tag_Printing_TRN.Product` -> `XStudio_XBatch.Product_Master.Name` (Many to One)
