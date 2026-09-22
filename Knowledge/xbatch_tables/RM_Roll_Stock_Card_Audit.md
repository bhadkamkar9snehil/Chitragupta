# XStudio_Xbatch.dbo.RM_Roll_Stock_Card_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference rolls, new, stock, use, discarded, balance, nos, period, issued, roll, total, closing.

> NOTE: this is a generated audit-history shadow of another table. Prefer the base table unless the investigation specifically needs change history.

**Primary Key:** —  
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
| PeriodFrom | datetime | YES | — | — |
| PeriodTo | datetime | YES | — | — |
| RollsUsedInStands | int | YES | 10,0 | — |
| NewRollsOpBalanceRollsInStock | int | YES | 10,0 | — |
| NewRollsReceived | int | YES | 10,0 | — |
| StockNewRollsIssuedToUse | int | YES | 10,0 | — |
| NewRollsClosingBalanceInStock | int | YES | 10,0 | — |
| RollsInUse | int | YES | 10,0 | — |
| InUseNewRollsIssuedToUse | int | YES | 10,0 | — |
| RollsDiscardedDuringThisPeriod | int | YES | 10,0 | — |
| TotalRollInUse | int | YES | 10,0 | — |
| OpBalanceDiscardedAtStockNos | int | YES | 10,0 | — |
| TotalDiscardedRollAtStockNos | int | YES | 10,0 | — |
| DiscardedRollsSoldDate | datetime | YES | — | — |
| NoOfRollsNos | int | YES | 10,0 | — |
| DiscardedRollsBalanceStock | int | YES | 10,0 | — |
| NewRollsissuedToUse | decimal | YES | 18,4 | — |

---
