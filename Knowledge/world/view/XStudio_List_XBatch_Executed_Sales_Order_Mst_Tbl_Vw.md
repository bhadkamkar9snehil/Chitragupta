---
type: view
title: "XStudio_List_XBatch_Executed_Sales_Order_Mst_Tbl_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XBatch_Executed_Sales_Order_Mst_Tbl_Vw

View in XStudio_Xbatch. Rows: unknown.

## Reads

- XBatch_Customer_Mst_Tbl
- XBatch_Material_Mst_Tbl
- XBatch_Measurement_Unit_Mst_Tbl
- XBatch_Sales_Order_Mst_Tbl
- XBatch_Status_Mst_Tbl

## Columns

- Edit varchar(238)
- Delete varchar(100)
- SalesOrder varchar(100)
- ID varchar(36)
- CreationDate datetime
- Action varchar(50)
- SAPSalesOrder varchar(100)
- ReleasedDate datetime
- Status varchar(50)
- WorkOrder varchar(-1)
- CustomerName varchar(100)
- ItemName varchar(100)
- Quantity decimal
- Unit varchar(100)
- ProgressTonnage decimal
- ItemID varchar(36)
- ColourCode varchar(50)
- ProgressPercentage decimal
- ParentID varchar(36)
- RemainingTonnage decimal
- Details varchar(-1)
- ActualStartDate datetime
- UnitID varchar(36)
- PlannedStartDate datetime
- ActualCompletionDate datetime
- StatusColourcode varchar(50)
- PlannedCompletionDate datetime
- ItemColourCode varchar(50)
- RequiredCompletionDate datetime
- Remarks varchar(1000)
- ActualOrderExecutionDuration int
- PlannedOrderExecutionDuration int
- OrderCompletionVariance int
- OrderStartVariance int
- ActualOrderCompletionSlack int
- PlannedOrderCompletionSlack int
- ActualOrderStartLeadTime int
- PlannedOrderStartLeadTime int
