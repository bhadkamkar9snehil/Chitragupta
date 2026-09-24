---
type: procedure
title: "XMES_SAP_GoodsMovements_API_Error_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_GoodsMovements_API_Error_Usp

Parameters: @RecordID varchar, @TransactionID varchar, @APIPostingType varchar.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type
- XMES_SAP_API_GoodsMovement_Error: Batch, Body, CreatedBy, EntryDateTime, ErrorMessage, ManufacturingOrder, Material, ModifiedBy, ModifiedOn, MovementType, RecordID, Source, Status, TransactionID, Type

## Reads

- MES_SAP_By_Product_Trn_Tbl: Batch, GoodsMovementType, ID, IsDeleted, ManufacturingOrder, Material, ModifiedBy, Saptransactionid
- MES_SAP_Consumption_Trn_Tbl: Batch, GoodsMovementType, ID, IsDeleted, ManufacturingOrder, Material, ModifiedBy, PostingMaterialType, Saptransactionid
- MES_SAP_Production_Trn_Tbl: Batch, GoodsMovementType, ID, IsDeleted, ManufacturingOrder, Material, ModifiedBy, PostingMaterialType, Saptransactionid
- XMES_SAP_PlantToPlantTransfer_Trn_Tbl: Batch, GoodsMovementType, ID, IsDeleted, ManufacturingOrder, Material, ModifiedBy, SAPTransactionID

## What its own log shows

992 log rows, 2026-03-20 23:28 to 2026-07-05 19:36.
Error steps: Store Errors In Goods Movement ByProduct Posting Error Table Process End; Store Errors In Goods Movement ByProduct Posting Error Table Process Start; Store Errors In Goods Movement Consumption Posting Error Table Process End; Store Errors In Goods Movement Consumption Posting Error Table Process Start; Store Errors In Goods Movement Production Posting Error Table Process End; Store Errors In Goods Movement Production Posting Error Table Process Start; Store Errors In Goods Movement Reversal Posting Error Table Process End; Store Errors In Goods Movement Reversal Posting Error Table Process Start

Steps:
- Completed
- Entered
- Store Errors In Goods Movement ByProduct Posting Error Table Process End
- Store Errors In Goods Movement ByProduct Posting Error Table Process Start
- Store Errors In Goods Movement Consumption Posting Error Table Process End
- Store Errors In Goods Movement Consumption Posting Error Table Process Start
- Store Errors In Goods Movement Production Posting Error Table Process End
- Store Errors In Goods Movement Production Posting Error Table Process Start
- Store Errors In Goods Movement Reversal Posting Error Table Process End
- Store Errors In Goods Movement Reversal Posting Error Table Process Start

Example call: `EXEC XStudio_Xbatch.dbo.XMES_SAP_GoodsMovements_API_Error_Usp @RecordID='FCB231BE-994F-4082-9AF2-9D586ECF6887', @TransactionID='6f7833bc-9c46-467d-a866-2817e80969ed', @APIPostingType='Production'`
