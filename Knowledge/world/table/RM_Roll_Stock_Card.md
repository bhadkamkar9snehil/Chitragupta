---
type: table
title: "RM_Roll_Stock_Card"
built: "2026-09-24T11:36:36"
---

# RM_Roll_Stock_Card

Table in XStudio_Xbatch. Rows: 0.

## Written by

- Xstudio_RM_Roll_Stock_Card_USP

## Read by

- Xstudio_RM_Roll_Stock_Card_USP

## Columns

- ID varchar(36)
- Name varchar(100)
- ParentID varchar(36)
- CreatedBy varchar(36)
- ModifiedBy varchar(36)
- CreatedOn datetime
- ModifiedOn datetime
- IsDeleted bit
- IsSystem bit
- AssignedUserID varchar(36)
- HostAddress varchar(100)
- DbSyncStatus varchar(500)
- MobileSyncStatus varchar(100)
- Source varchar(20)
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- PeriodFrom datetime
- PeriodTo datetime
- RollsUsedInStands int
- NewRollsOpBalanceRollsInStock int
- NewRollsReceived int
- StockNewRollsIssuedToUse int
- NewRollsClosingBalanceInStock int
- RollsInUse int
- InUseNewRollsIssuedToUse int
- RollsDiscardedDuringThisPeriod int
- TotalRollInUse int
- OpBalanceDiscardedAtStockNos int
- TotalDiscardedRollAtStockNos int
- DiscardedRollsSoldDate datetime
- NoOfRollsNos int
- DiscardedRollsBalanceStock int
- NewRollsissuedToUse decimal
