---
type: procedure
title: "XSTUDIO_WORKFLOW_9A172601-2557-4597-B6A4-CDE39CA602BB_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_9A172601-2557-4597-B6A4-CDE39CA602BB_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_RM_Production_Data: Source, WorkflowStatus

## Reads

- MES_SAP_Consumption_Trn_Tbl: Batch, CreatedByUser, CreationDate, CreationTime, CtrlPostForWhseMgmtSyst, Cutlength, DocumentDate, EntryDateTime, EntryUnit, FurnaceBilletStatus, GoodsMovementCode, GoodsMovementType, Grade, HeatNo, ID, InspectionLot, InventorySpecialStockType, InventoryTransactionType, IsProcessed, ManualPrintLsTriggered, ManufacturingOrder, Material, MaterialDocument, MaterialDocumentHeaderText, MaterialDocumentItem, MaterialDocumentYear, Plant, PostingDate, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, RawMaterialRecordID, ReferenceDocument, ReportDate, SAPQuantity, Saptransactionid, StorageLocation, SuccessMessage, VersionForPrintingSlip
- XMES_RM_Production_Data: BilletNo

## Writes (named in its SQL text)

- MES_SAP_Consumption_Trn_Tbl
