---
type: procedure
title: "XMES_SAP_I_Inventory_Stock_Data_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_I_Inventory_Stock_Data_Usp

Parameters: @Type varchar, @Plant int, @Storage varchar.

## Writes

- MES_SAP_Inventory_Stock_Data_Tbl: Batch, BlockedStock, Customer, InventorySpecialStockType, InventoryStockType, Material, MaterialBaseUnit, MatlWrhsStkQtyInMatlBaseUnit, MetaData, Plant, RestrictedUseStock, Returns, SDDocument, SDDocumentItem, StockTransferPlant, StockTransferStorageLocation, StockinQualityInspection, StockinTransit, StorageLocation, Supplier, TiedEmpties, UnrestrictedUseStock, ValuatedGoodsReceiptBlockedStock, WebElementInternalID
- MES_SAP_Inventory_Stock_Tbl
- XMES_Billet_Tracking_Trn_Tbl: Batch, BilletNo, BilletQuantity, BilletWeight, CreatedOn, CutLength, EntryDateTime, HeatNo, ManufacturingOrder, Materialid, Plant, PostingMaterialType, ProcessStage, Qualitygradeid, ReportDate, Source, StatePosition, StorageLocation, UOMID
- Xbatch_Material_Inventory_Trn_Tbl: CreatedOn, LotNumber, MaterialGrade, ParentID, PlantName, PostingMaterialType, Quantity, QuantityinCount, Source, StorageLocation, UOMID, isExternal

## Reads

- Billet_Cross_Section: CreatedOn, IsDeleted, MaterialSpecificWeight
- MES_SAP_Inventory_Stock_Data_Tbl: CreatedOn
- MES_SAP_Inventory_Stock_Tbl: Batch, CreatedOn, Customer, InventorySpecialStockType, InventoryStockType, IsDeleted, Material, MaterialBaseUnit, MatlWrhsStkQtyInMatlBaseUnit, MetaData, Plant, SDDocument, SDDocumentItem, StorageLocation, Supplier, WebElementInternalID
- MES_SAP_Production_Trn_Tbl: Batch
- XBatch_Material_Grade_Mst_Tbl: ID, Name
- XBatch_Material_Mst_Tbl: Grade, ID, IsDeleted, Name, Number, UnitID
- XMES_State_Position_State_Mst_Tbl: ID, SequenceNumber
- Xbatch_Material_Inventory_Trn_Tbl: BilletNo, CreatedOn, IsDeleted, Ismodified, LotNumber, PlantName, Quantity, QuantityinCount, StorageLocation, TotalQuantity
