# XStudio_Xbatch.dbo.RM_Tool_Stock_Report

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference date, indent, new, balance, closing, issued, nos, quantity, received, remarks, stock, tolls.

**Primary Key:** ID  
**Row Count:** 0  

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
| TypeOfTool | varchar | YES | 100 | — |
| QuantityNos | int | YES | 10,0 | — |
| Issued | varchar | YES | 100 | — |
| Balance | int | YES | 10,0 | — |
| NewIndentNo | int | YES | 10,0 | — |
| IndentDate | date | YES | — | — |
| NewTollsReceivedDate | date | YES | — | — |
| Remarks | varchar | YES | 100 | — |
| ClosingStock | varchar | YES | 100 | — |

---
