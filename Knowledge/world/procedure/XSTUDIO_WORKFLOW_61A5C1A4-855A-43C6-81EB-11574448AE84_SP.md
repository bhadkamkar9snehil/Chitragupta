---
type: procedure
title: "XSTUDIO_WORKFLOW_61A5C1A4-855A-43C6-81EB-11574448AE84_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_61A5C1A4-855A-43C6-81EB-11574448AE84_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- XBatch_Work_Order_Mst_Tbl: ActualCompletionDate, ActualCostsCostingVariant, BasicSchedulingType, BusinessArea, CampaignId, ColourCode, CompanyCode, CustomerName, Description, EndTime, Equipment, FunctionalArea, GoodsRecipientName, Grade, HeatNo, ID, InventoryUsabilityCode, ItemID, LastChangeDateTime, Length, MRPArea, MRPController, ManufacturingObject, ManufacturingOrderCategory, ManufacturingOrderImportance, ManufacturingOrderType, MaterialAvailyIsNotChecked, MaterialGoodsReceiptDuration, MaxBundles, MfgOrderActualReleaseDate, MfgOrderConfirmedYieldQty, MfgOrderCreationDate, MfgOrderCreationTime, MfgOrderPlannedEndDate, MfgOrderPlannedEndTime, MfgOrderPlannedScrapQty, MfgOrderPlannedStartDate, MfgOrderPlannedStartTime, MfgOrderScheduledEndDate, MfgOrderScheduledEndTime, MfgOrderScheduledStartDate, MfgOrderScheduledStartTime, MinBundles, MinQtyToRoll, NoOfPiecesInBundles, OrderHasGeneratedOperations, OrderInternalBillOfOperations, OrderIsClosed, OrderIsConfirmed, OrderIsCreated, OrderIsDeleted, OrderIsDelivered, OrderIsLocked, OrderIsMarkedForDeletion, OrderIsPartiallyConfirmed, OrderIsPartiallyDelivered, OrderIsPartiallyReleased, OrderIsPreCosted, OrderIsPrinted, OrderIsReleased, OrderIsScheduled, OrderIsTechnicallyCompleted, OrderIsToBeHandledInBatches, OrderLongText, OrderSequenceNumber, ParentID, PlannedCostsCostingVariant, PlannedOrder, Plant, ProductConfiguration, ProductionPlant, ProductionSupervisor, ProductionUnit, ProductionUnitISOCode, ProductionUnitSAPCode, ProductionVersion, ProfitCenter, ProgressDuration, ProgressTonnage, Quantity, QuantityDistributionKey, ReleasedDate, SAPTransactionID, SalesOrder, SalesOrderItem, SerialNumber, SettlementRuleIsCreated, SettlementRuleIsCrtedManually, Size, Sn, StartTime, StockSegment, StorageLocation, UnitID, UnloadingPointName, WBSElementExternalID, WorkOrderNumber

## Writes (named in its SQL text)

- XBatch_Work_Order_Mst_Tbl

## What its own log shows

68 log rows, 2026-06-01 16:02 to 2026-09-01 00:00.

Steps:
- 1 Entered
- 2 Set ReleasedDate Start
- 3 Set ReleasedDate End
- 4 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_61A5C1A4-855A-43C6-81EB-11574448AE84_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='A6E924D5-B2F0-4A5F-9717-3A63F6190358', @p_RecordId='Released', @p_StatusAttributeName='9212319F-69E1-4C23-ACEF-D81E75491309', @p_Status='Status'`
