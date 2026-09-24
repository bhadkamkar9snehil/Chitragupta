---
type: procedure
title: "XSTUDIO_WORKFLOW_CBDD76F9-AF65-4113-B5FE-987066DC8DDD_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_CBDD76F9-AF65-4113-B5FE-987066DC8DDD_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XBatch_Sales_Order_Mst_Tbl: ModifiedOn, Status
- XBatch_Work_Order_Mst_Tbl: ModifiedOn, Source, Status
- XMES_Campaign_Plan_Mst: ModifiedOn, Source, Status
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type
- XMES_Work_Order_Trn_Tbl: CampaignID, CreatedOn, EntryDateTime, ReportDate, Source, WorkOrder

## Reads

- XBatch_Sales_Order_Mst_Tbl: ID
- XBatch_Work_Order_Mst_Tbl: ActualCompletionDate, ActualCostsCostingVariant, BasicSchedulingType, BusinessArea, CampaignId, ColourCode, CompanyCode, CustomerName, Description, Equipment, FunctionalArea, GoodsRecipientName, Grade, HeatNo, ID, InventoryUsabilityCode, ItemID, LastChangeDateTime, Length, MRPArea, MRPController, ManufacturingObject, ManufacturingOrderCategory, ManufacturingOrderImportance, ManufacturingOrderType, MaterialAvailyIsNotChecked, MaterialGoodsReceiptDuration, MaxBundles, MfgOrderActualReleaseDate, MfgOrderConfirmedYieldQty, MfgOrderCreationDate, MfgOrderCreationTime, MfgOrderPlannedEndDate, MfgOrderPlannedEndTime, MfgOrderPlannedScrapQty, MfgOrderPlannedStartDate, MfgOrderPlannedStartTime, MfgOrderScheduledEndDate, MfgOrderScheduledEndTime, MfgOrderScheduledStartDate, MfgOrderScheduledStartTime, MinBundles, MinQtyToRoll, NoOfPiecesInBundles, OrderHasGeneratedOperations, OrderInternalBillOfOperations, OrderIsClosed, OrderIsConfirmed, OrderIsCreated, OrderIsDeleted, OrderIsDelivered, OrderIsLocked, OrderIsMarkedForDeletion, OrderIsPartiallyConfirmed, OrderIsPartiallyDelivered, OrderIsPartiallyReleased, OrderIsPreCosted, OrderIsPrinted, OrderIsReleased, OrderIsScheduled, OrderIsTechnicallyCompleted, OrderIsToBeHandledInBatches, OrderLongText, OrderSequenceNumber, ParentID, PlannedCostsCostingVariant, PlannedOrder, Plant, ProductConfiguration, ProductionPlant, ProductionSupervisor, ProductionUnit, ProductionUnitISOCode, ProductionUnitSAPCode, ProductionVersion, ProfitCenter, ProgressDuration, ProgressTonnage, Quantity, QuantityDistributionKey, ReleasedDate, SAPTransactionID, SalesOrder, SalesOrderItem, SerialNumber, SettlementRuleIsCreated, SettlementRuleIsCrtedManually, Size, Sn, StockSegment, StorageLocation, UnitID, UnloadingPointName, WBSElementExternalID, WorkOrderNumber
- XMES_Campaign_Plan_Mst: ID
- XMES_Work_Order_Trn_Tbl: CreatedOn, IsDeleted, WorkOrder

## What its own log shows

22,926 log rows, 2026-06-01 16:03 to 2026-09-01 00:00.

Steps:
- 1 Entered
- 2 Update On Hold status in Work order when stasus is running Start
- 3 Update On Hold status in Work order when stasus is running End
- 4 Completed
- 4 Insert running work order in work order transaction Start
- 4 Update status Running in Sales order when stasus is released or onhold Start
- 5 Insert running work order in work order transaction End
- 5 Update status Running in Sales order when stasus is released or onhold End
- 6 Completed
- 6 Insert running work order in work order transaction Start
- 7 Insert running work order in work order transaction End
- 8 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_CBDD76F9-AF65-4113-B5FE-987066DC8DDD_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='C9710FC1-E4FF-4FDC-991A-A1B54F059E59', @p_RecordId='Running', @p_StatusAttributeName='9BFC581A-2F1A-431A-AFA3-15125901834D', @p_Status='Status'`
