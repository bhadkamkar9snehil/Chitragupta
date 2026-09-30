---
type: procedure
title: "XBatch_RM_Rolling_Process_SPvaildation_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_RM_Rolling_Process_SPvaildation_Usp

Parameters: @SalesOrderNo varchar, @RollingReleaseQty int, @SequenceNo int, @RollingDate datetime, @MaxSeqNo int, @MaxRollingID varchar, @IsNewRollingId bit.

## Reads

- RM_Rolling_Plan: IsDeleted, RollingDate, RollingID, SequenceNo, Status
- RM_Sales_Order: IsDeleted, OpenQty, PONumber, Status
