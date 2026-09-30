---
type: procedure
title: "XSTUDIO_WORKFLOW_C18D4DFF-8ADA-4080-9F2F-91DE212A1257_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_C18D4DFF-8ADA-4080-9F2F-91DE212A1257_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XBatch_Sales_Order_Mst_Tbl: ActualCompletionDate, ApprovedBy, ApprovedDate, CreatedBy, CreatedOn, ItemID, Name, ParentID, PlannedCompletionDate, Quantity, ReleasedDate, SalesOrderNumber, Status, UnitID
- XBatch_Work_Order_Mst_Tbl: CreatedBy, CreatedOn, Equipment, ItemID, ManufacturingOrderType, MaterialName, MfgOrderPlannedEndDate, MfgOrderPlannedStartDate, Name, ProductionPlant, Quantity, ReleasedDate, SalesOrder, SalesOrderName, Status, UnitID, WorkOrderNumber
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- MES_Order_Configurator: Equipment, Itemid, OrderType, Quantity, Unitid
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Sales_Order_Mst_Tbl: ID
- XBatch_Work_Order_Mst_Tbl: ActualCompletionDate, ActualCostsCostingVariant, BasicSchedulingType, BusinessArea, CampaignId, ColourCode, CompanyCode, CustomerName, Description, EndTime, Equipment, FunctionalArea, GoodsRecipientName, Grade, HeatNo, ID, InventoryUsabilityCode, IsDeleted, ItemID, LastChangeDateTime, Length, MRPArea, MRPController, ManufacturingObject, ManufacturingOrderCategory, ManufacturingOrderImportance, ManufacturingOrderType, MaterialAvailyIsNotChecked, MaterialGoodsReceiptDuration, MaxBundles, MfgOrderActualReleaseDate, MfgOrderConfirmedYieldQty, MfgOrderCreationDate, MfgOrderCreationTime, MfgOrderPlannedEndDate, MfgOrderPlannedEndTime, MfgOrderPlannedScrapQty, MfgOrderPlannedStartDate, MfgOrderPlannedStartTime, MfgOrderScheduledEndDate, MfgOrderScheduledEndTime, MfgOrderScheduledStartDate, MfgOrderScheduledStartTime, MinBundles, MinQtyToRoll, NoOfPiecesInBundles, OrderHasGeneratedOperations, OrderInternalBillOfOperations, OrderIsClosed, OrderIsConfirmed, OrderIsCreated, OrderIsDeleted, OrderIsDelivered, OrderIsLocked, OrderIsMarkedForDeletion, OrderIsPartiallyConfirmed, OrderIsPartiallyDelivered, OrderIsPartiallyReleased, OrderIsPreCosted, OrderIsPrinted, OrderIsReleased, OrderIsScheduled, OrderIsTechnicallyCompleted, OrderIsToBeHandledInBatches, OrderLongText, OrderSequenceNumber, ParentID, PlannedCostsCostingVariant, PlannedOrder, Plant, ProductConfiguration, ProductionPlant, ProductionSupervisor, ProductionUnit, ProductionUnitISOCode, ProductionUnitSAPCode, ProductionVersion, ProfitCenter, ProgressDuration, ProgressTonnage, Quantity, QuantityDistributionKey, ReleasedDate, SAPTransactionID, SalesOrder, SalesOrderItem, SerialNumber, SettlementRuleIsCreated, SettlementRuleIsCrtedManually, Size, Sn, StartTime, StockSegment, StorageLocation, UnitID, UnloadingPointName, WBSElementExternalID, WorkOrderNumber

## What its own log shows

24 log rows, 2026-06-16 22:02 to 2026-08-15 00:09.

Steps:
- 1 Entered
- 2 Get No of work order from Work order whose status either new production order or new process order or released or onhold Start
- 3 Get No of work order from Work order whose status either new production order or new process order or released or onhold End
- 4 Get Earliest work order ID from work order of released or onhold status for equipment  for sales order Start
- 4 Update status Completed Start
- 5 Get Earliest work order ID from work order of released or onhold status for equipment LRF for sales order End
- 5 Update status Completed End
- 6 Update running status in work order Start
- 7 Get Earliest work order ID from work order of released or onhold status for equipment LRF for sales order End
- 7 Update running status in work order End
- 8 Get Earliest work order ID from work order of released status for equipment LRF Start
- 8 Set Actual completion date Start
- 9 Get Earliest work order ID from work order of released status for equipment LRF End
- 9 Set Actual completion date End
- 10 Completed
- 10 Update running status in work order Start
- 11 Update running status in work order End
- 12 Set Actual completion date Start
- 13 Set Actual completion date End
- 14 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_C18D4DFF-8ADA-4080-9F2F-91DE212A1257_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='A6E924D5-B2F0-4A5F-9717-3A63F6190358', @p_RecordId='Completed', @p_StatusAttributeName='FF56F036-19A6-4808-8F29-E500C8D878AE', @p_Status='Status'`
