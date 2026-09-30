---
type: procedure
title: "Xstudio_RM_Roll_Stock_Card_USP"
built: "2026-09-24T11:36:36"
---

# Xstudio_RM_Roll_Stock_Card_USP

Parameters: @ID varchar, @Mode varchar.

## Writes

- RM_Roll_Stock_Card: DiscardedRollsBalanceStock, NewRollsClosingBalanceInStock, Source, TotalDiscardedRollAtStockNos, TotalRollInUse

## Reads

- RM_Roll_Stock_Card: ID, InUseNewRollsIssuedToUse, NewRollsOpBalanceRollsInStock, NewRollsReceived, NewRollsissuedToUse, NoOfRollsNos, OpBalanceDiscardedAtStockNos, RollsDiscardedDuringThisPeriod, RollsInUse
