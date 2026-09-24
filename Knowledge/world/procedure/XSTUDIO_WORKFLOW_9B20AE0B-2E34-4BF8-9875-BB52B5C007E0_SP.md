---
type: procedure
title: "XSTUDIO_WORKFLOW_9B20AE0B-2E34-4BF8-9875-BB52B5C007E0_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_9B20AE0B-2E34-4BF8-9875-BB52B5C007E0_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XBatch_Sales_Order_Mst_Tbl: ApprovedBy, ApprovedDate, CreatedBy, CreatedOn, ItemID, ModifiedOn, Name, ParentID, PlannedCompletionDate, Quantity, ReleasedDate, SalesOrderNumber, Status, UnitID
- XBatch_Work_Order_Mst_Tbl: CreatedBy, CreatedOn, Equipment, ItemID, ManufacturingOrderType, MaterialName, MfgOrderPlannedEndDate, MfgOrderPlannedStartDate, Name, ProductionPlant, Quantity, SalesOrder, SalesOrderName, Status, UnitID, WorkOrderNumber
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- MES_Order_Configurator: Equipment, Itemid, OrderType, Quantity, Unitid
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Sales_Order_Mst_Tbl: ID
- XBatch_Work_Order_Mst_Tbl: ActualCompletionDate, ActualCostsCostingVariant, BasicSchedulingType, BusinessArea, CampaignId, ColourCode, CompanyCode, CustomerName, Description, EndTime, Equipment, FunctionalArea, GoodsRecipientName, Grade, HeatNo, ID, InventoryUsabilityCode, IsDeleted, ItemID, LastChangeDateTime, Length, MRPArea, MRPController, ManufacturingObject, ManufacturingOrderCategory, ManufacturingOrderImportance, ManufacturingOrderType, MaterialAvailyIsNotChecked, MaterialGoodsReceiptDuration, MaxBundles, MfgOrderActualReleaseDate, MfgOrderConfirmedYieldQty, MfgOrderCreationDate, MfgOrderCreationTime, MfgOrderPlannedEndDate, MfgOrderPlannedEndTime, MfgOrderPlannedScrapQty, MfgOrderPlannedStartDate, MfgOrderPlannedStartTime, MfgOrderScheduledEndDate, MfgOrderScheduledEndTime, MfgOrderScheduledStartDate, MfgOrderScheduledStartTime, MinBundles, MinQtyToRoll, NoOfPiecesInBundles, OrderHasGeneratedOperations, OrderInternalBillOfOperations, OrderIsClosed, OrderIsConfirmed, OrderIsCreated, OrderIsDeleted, OrderIsDelivered, OrderIsLocked, OrderIsMarkedForDeletion, OrderIsPartiallyConfirmed, OrderIsPartiallyDelivered, OrderIsPartiallyReleased, OrderIsPreCosted, OrderIsPrinted, OrderIsReleased, OrderIsScheduled, OrderIsTechnicallyCompleted, OrderIsToBeHandledInBatches, OrderLongText, OrderSequenceNumber, ParentID, PlannedCostsCostingVariant, PlannedOrder, Plant, ProductConfiguration, ProductionPlant, ProductionSupervisor, ProductionUnit, ProductionUnitISOCode, ProductionUnitSAPCode, ProductionVersion, ProfitCenter, ProgressDuration, ProgressTonnage, Quantity, QuantityDistributionKey, ReleasedDate, SAPTransactionID, SalesOrder, SalesOrderItem, SerialNumber, SettlementRuleIsCreated, SettlementRuleIsCrtedManually, Size, Sn, StartTime, StockSegment, StorageLocation, UnitID, UnloadingPointName, WBSElementExternalID, WorkOrderNumber

## What its own log shows

4 log rows, 2026-06-12 08:13 to 2026-06-12 08:13.

Steps:
- 1 Entered
- 2 Update status Cancelled in Sales Order Start
- 3 Update status Cancelled in Sales Order End
- 4 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_9B20AE0B-2E34-4BF8-9875-BB52B5C007E0_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='3ADE6546-3C9A-49C4-A001-234025F2F901', @p_RecordId='Cancelled', @p_StatusAttributeName='30E46685-29EC-46EB-88D9-8F08434D3A4B', @p_Status='Status'`
