---
type: procedure
title: "Xstudio_XBatch_Sales_Order_Mst_Tbl_USP"
built: "2026-09-24T11:36:36"
---

# Xstudio_XBatch_Sales_Order_Mst_Tbl_USP

Parameters: @ID varchar, @Mode varchar.

## Writes

- XBatch_Sales_Order_Mst_Tbl: ActualOrderCompletionSlack, ActualOrderExecutionDuration, ActualOrderStartLeadTime, OrderCompletionVariance, OrderStartVariance, PlannedOrderCompletionSlack, PlannedOrderExecutionDuration, PlannedOrderStartLeadTime, Source

## Reads

- XBatch_Sales_Order_Mst_Tbl: ActualCompletionDate, ActualStartDate, ID, PlannedCompletionDate, PlannedStartDate, ReleasedDate, RequiredCompletionDate
