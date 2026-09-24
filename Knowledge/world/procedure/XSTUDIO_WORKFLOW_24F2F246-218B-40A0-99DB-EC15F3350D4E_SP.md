---
type: procedure
title: "XSTUDIO_WORKFLOW_24F2F246-218B-40A0-99DB-EC15F3350D4E_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_24F2F246-218B-40A0-99DB-EC15F3350D4E_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XBatch_Material_Item_Prod_Trn_Tbl: GradeID
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- XBatch_Material_Grade_Mst_Tbl: ID, Name
- XBatch_Material_Inventory_Mst_Tbl: AvailableQuantityPrice, BilletLength, BilletReceivedBy, Description, ExpiryDate, GRNNumber, ID, InvoiceNumber, InwardBy, InwardDate, IsExpired, IsPlantToPlantTransfer, LocationID, LocationType, LotNumber, MaterialGrade, MovementType, OperationID, OutwardDate, OutwardLocation, Outwardby, PONumber, ParentID, PlantName, PostingMaterialType, Price, Quantity, QuantityinCount, ReceivedDate, Remark, StorageLocation, SublotNumber, UOMID, Vendor, outwardremarks
- XBatch_Material_Item_Prod_Trn_Tbl: HeatNo, SublotNumber

## Writes (named in its SQL text)

- XBatch_Material_Inventory_Mst_Tbl
