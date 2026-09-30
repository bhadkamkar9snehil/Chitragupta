---
type: procedure
title: "XSTUDIO_WORKFLOW_0E59C696-ECB5-4E5C-B246-4275C0A324A4_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_0E59C696-ECB5-4E5C-B246-4275C0A324A4_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- MES_SAP_Production_Trn_Tbl: Batch, CreatedByUser, CreationDate, CreationTime, CtrlPostForWhseMgmtSyst, DocumentDate, EntryDateTime, EntryUnit, GoodsMovementCode, GoodsMovementType, Grade, HeatNo, ID, InspectionLot, InventoryTransactionType, IsProcessed, IsReversal, ManualPrintLsTriggered, ManufacturingOrder, Material, MaterialDocument, MaterialDocumentHeaderText, MaterialDocumentItem, MaterialDocumentYear, Plant, PostingDate, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, ReferenceDocument, ReportDate, Sampleid, Saptransactionid, StorageLocation, VersionForPrintingSlip

## Writes (named in its SQL text)

- MES_SAP_Production_Trn_Tbl
