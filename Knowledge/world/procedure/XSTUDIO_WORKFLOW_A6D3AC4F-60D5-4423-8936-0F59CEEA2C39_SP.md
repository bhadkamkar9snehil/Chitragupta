---
type: procedure
title: "XSTUDIO_WORKFLOW_A6D3AC4F-60D5-4423-8936-0F59CEEA2C39_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_A6D3AC4F-60D5-4423-8936-0F59CEEA2C39_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XBatch_Sales_Order_Mst_Tbl: ActualCompletionDate, ModifiedOn, Status
- XBatch_Work_Order_Mst_Tbl: ModifiedOn, Status
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- XBatch_Sales_Order_Mst_Tbl: ID
- XBatch_Work_Order_Mst_Tbl: ActualCompletionDate, ActualCostsCostingVariant, BasicSchedulingType, BusinessArea, CampaignId, ColourCode, CompanyCode, CustomerName, Description, EndTime, Equipment, FunctionalArea, GoodsRecipientName, Grade, HeatNo, ID, InventoryUsabilityCode, ItemID, LastChangeDateTime, Length, MRPArea, MRPController, ManufacturingObject, ManufacturingOrderCategory, ManufacturingOrderImportance, ManufacturingOrderType, MaterialAvailyIsNotChecked, MaterialGoodsReceiptDuration, MaxBundles, MfgOrderActualReleaseDate, MfgOrderConfirmedYieldQty, MfgOrderCreationDate, MfgOrderCreationTime, MfgOrderPlannedEndDate, MfgOrderPlannedEndTime, MfgOrderPlannedScrapQty, MfgOrderPlannedStartDate, MfgOrderPlannedStartTime, MfgOrderScheduledEndDate, MfgOrderScheduledEndTime, MfgOrderScheduledStartDate, MfgOrderScheduledStartTime, MinBundles, MinQtyToRoll, NoOfPiecesInBundles, OrderHasGeneratedOperations, OrderInternalBillOfOperations, OrderIsClosed, OrderIsConfirmed, OrderIsCreated, OrderIsDeleted, OrderIsDelivered, OrderIsLocked, OrderIsMarkedForDeletion, OrderIsPartiallyConfirmed, OrderIsPartiallyDelivered, OrderIsPartiallyReleased, OrderIsPreCosted, OrderIsPrinted, OrderIsReleased, OrderIsScheduled, OrderIsTechnicallyCompleted, OrderIsToBeHandledInBatches, OrderLongText, OrderSequenceNumber, ParentID, PlannedCostsCostingVariant, PlannedOrder, Plant, ProductConfiguration, ProductionPlant, ProductionSupervisor, ProductionUnit, ProductionUnitISOCode, ProductionUnitSAPCode, ProductionVersion, ProfitCenter, ProgressDuration, ProgressTonnage, Quantity, QuantityDistributionKey, ReleasedDate, SAPTransactionID, SalesOrder, SalesOrderItem, SerialNumber, SettlementRuleIsCreated, SettlementRuleIsCrtedManually, Size, Sn, StartTime, StockSegment, StorageLocation, UnitID, UnloadingPointName, WBSElementExternalID, WorkOrderNumber

## What its own log shows

20 log rows, 2026-06-04 10:18 to 2026-06-17 16:43.

Steps:
- 1 Entered
- 2 Get Earliest Work order ID from work order of released status for equipment CCM for sales order Start
- 2 Get Earliest Work order ID from work order of released status for equipment LRF for sales order Start
- 3 Get Earliest Work order ID from work order of released status for equipment CCM for sales order End
- 3 Get Earliest Work order ID from work order of released status for equipment LRF for sales order End
- 4 Get Earliest Work order ID from work order of released status for equipment CCM Start
- 4 Get Earliest Work order ID from work order of released status for equipment LRF Start
- 5 Get Earliest Work order ID from work order of released status for equipment CCM End
- 5 Get Earliest Work order ID from work order of released status for equipment LRF End
- 6 Update running status in work order Start
- 7 Update running status in work order End
- 8 Update status Aborted and auto completion date in sales order Start
- 9 Update status Aborted and auto completion date in sales order End
- 10 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_A6D3AC4F-60D5-4423-8936-0F59CEEA2C39_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='3ADE6546-3C9A-49C4-A001-234025F2F901', @p_RecordId='Aborted', @p_StatusAttributeName='98D11898-F46C-4DC8-83AC-A6704135E2F6', @p_Status='Status'`
