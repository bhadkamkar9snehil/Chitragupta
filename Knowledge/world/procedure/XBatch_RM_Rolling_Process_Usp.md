---
type: procedure
title: "XBatch_RM_Rolling_Process_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_RM_Rolling_Process_Usp

Parameters: @SalesOrderNo varchar, @RollingReleaseQty int, @SequenceNo int, @RollingDate datetime, @MaxSeqNo int, @MaxRollingID varchar, @IsNewRollingID bit.

## Writes

- RM_Rolling_Plan: Customer, MaterialGrade, MaterialID, PONumber, ReleaseRollingQty, RollingDate, RollingID, RollingQty, SequenceNo, Size, Status
- RM_Sales_Order: OpenQty, ReleaseQty, Status

## Reads

- RM_Rolling_Plan: IsDeleted, RollingDate, RollingID
- RM_Sales_Order: Customer, IsDeleted, MaterialGrade, MaterialID, PONumber, RollingQty, Size

## Calls

- XBatch_RM_Rolling_Process_SPvaildation_Usp
