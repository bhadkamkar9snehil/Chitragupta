---
type: note
subtype: schema-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch schema atlas: M

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.MES_Current_Batch
ID:varchar, WRM:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, TMT:varchar, WRMBundle:varchar, TMT_Small_Cut:varchar, TMTBundle:varchar, ChargeBed:varchar

## dbo.MES_Logbook_Water_Reading
ID:varchar, CommonFMReading:int, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, IsProcessed:bit, RMFMReading:int, SMSFMReading:int, MillScale:decimal, SMSScale:decimal, EntirePlantFMReading:int, RMReadingDifference:int, SMSReadingDifference:int, EntirePlantReadingDifference:int

## dbo.MES_Order_Configurator
ID:varchar, Equipment:varchar, Itemid:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Quantity:decimal, Unitid:varchar, OrderType:varchar, SrNo:int

## dbo.MES_Quality_Configurator
ID:varchar, Operation:varchar, SampleType:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Description:varchar

## dbo.MES_Raw_Material_Consumptions_Mapping_Mst_Tbl
ID:varchar, RawMaterialName:varchar, Materialid:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, MaterialType:varchar, Srno:int, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Unitid:varchar, Entityids:varchar, Attributeids:varchar

## dbo.MES_Raw_Material_Consumptions_Trn_Tbl
ID:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, CapturedQuantity:decimal, DeclaredQuantity:decimal, Unit:varchar, WorkOrder:varchar, SAPWorkflowStatus:varchar, LotNumber:varchar, Price:decimal, Difference:decimal, OrderType:varchar, WorkOrderNo:varchar

## dbo.MES_SAP_By_Product_Trn_Tbl
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Grade:varchar, GoodsMovementCode:varchar, PostingDate:datetime, DocumentDate:datetime, StorageLocation:varchar, InspectionLot:int, CtrlPostForWhseMgmtSyst:varchar, CreatedByUser:varchar, EntryUnit:varchar, ManualPrintLsTriggered:varchar, ReferenceDocument:varchar, InventoryTransactionType:varchar, Material:varchar, VersionForPrintingSlip:int, QuantityInEntryUnit:decimal, MaterialDocumentItem:varchar, QuantityInCount:int, SAPPostingStatus:varchar, CreationDate:date, CreationTime:time, GoodsMovementType:int, Plant:varchar, MaterialDocumentYear:int, MaterialDocumentHeaderText:varchar, ParentID:varchar, HeatNo:int, ReportDate:date, MaterialDocument:varchar, Saptransactionid:varchar, Batch:varchar, EntryDateTime:datetime, ManufacturingOrder:varchar, PostingMaterialType:varchar, IsProcessed:bit, Name:varchar, SuccessMessage:varchar

## dbo.MES_SAP_Consumption_Trn_Tbl
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Grade:varchar, GoodsMovementCode:varchar, PostingDate:datetime, DocumentDate:datetime, StorageLocation:varchar, InspectionLot:int, CtrlPostForWhseMgmtSyst:varchar, CreatedByUser:varchar, EntryUnit:varchar, ManualPrintLsTriggered:varchar, ReferenceDocument:varchar, InventoryTransactionType:varchar, Material:varchar, VersionForPrintingSlip:int, QuantityInEntryUnit:decimal, MaterialDocumentItem:varchar, QuantityInCount:int, SAPPostingStatus:varchar, CreationDate:date, CreationTime:time, GoodsMovementType:int, Plant:varchar, MaterialDocumentYear:int, MaterialDocumentHeaderText:varchar, ParentID:varchar, HeatNo:int, ReportDate:date, MaterialDocument:varchar, Saptransactionid:varchar, Batch:varchar, EntryDateTime:datetime, ManufacturingOrder:varchar, PostingMaterialType:varchar, IsProcessed:bit, Name:varchar, SuccessMessage:varchar, InventorySpecialStockType:varchar, RawMaterialRecordID:varchar

## dbo.MES_SAP_Inventory_Stock_Data_Tbl
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Supplier:varchar, EntryDateTime:datetime, Name:varchar, Material:varchar, SDDocument:varchar, ReportDate:date, InventoryStockType:varchar, MatlWrhsStkQtyInMatlBaseUnit:decimal, SDDocumentItem:int, Customer:varchar, MaterialBaseUnit:varchar, Plant:int, Batch:varchar, ParentID:varchar, InventorySpecialStockType:varchar, WebElementInternalID:varchar, StorageLocation:varchar, IsProcessed:bit, MetaData:varchar, UnrestrictedUseStock:varchar, StockinQualityInspection:varchar, Returns:varchar, StockTransferStorageLocation:varchar, StockTransferPlant:varchar, StockinTransit:varchar, BlockedStock:varchar, RestrictedUseStock:varchar, TiedEmpties:varchar, ValuatedGoodsReceiptBlockedStock:varchar

## dbo.MES_SAP_Inventory_Stock_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Material:varchar, Plant:int, StorageLocation:varchar, Batch:varchar, Supplier:varchar, Customer:varchar, WebElementInternalID:varchar, SDDocument:varchar, SDDocumentItem:int, InventorySpecialStockType:varchar, InventoryStockType:varchar, MaterialBaseUnit:varchar, MatlWrhsStkQtyInMatlBaseUnit:decimal, MetaData:varchar, PlantName:varchar

## dbo.MES_SAP_Inventory_Stock_Tbl_copy
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Material:varchar, Plant:int, StorageLocation:int, Batch:varchar, Supplier:varchar, Customer:varchar, WebElementInternalID:varchar, SDDocument:varchar, SDDocumentItem:int, InventorySpecialStockType:varchar, InventoryStockType:varchar, MaterialBaseUnit:varchar, MatlWrhsStkQtyInMatlBaseUnit:decimal, MetaData:varchar

## dbo.MES_SAP_Production_Trn_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, HeatNo:int, Grade:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Material:varchar, Plant:varchar, StorageLocation:varchar, Batch:varchar, ManufacturingOrder:varchar, QuantityInEntryUnit:decimal, InspectionLot:varchar, MaterialDocument:bigint, InventoryTransactionType:varchar, MaterialDocumentYear:int, DocumentDate:datetime, PostingDate:datetime, CreationDate:date, CreationTime:time, CreatedByUser:varchar, MaterialDocumentHeaderText:varchar, ReferenceDocument:varchar, VersionForPrintingSlip:int, ManualPrintLsTriggered:varchar, CtrlPostForWhseMgmtSyst:varchar, GoodsMovementCode:varchar, MaterialDocumentItem:varchar, Saptransactionid:varchar, GoodsMovementType:int, EntryUnit:varchar, QuantityInCount:int, PostingMaterialType:varchar, SAPPostingStatus:varchar, Sampleid:varchar, IsReversal:bit, SuccessMessage:varchar, IsAutoPost:bit, Cutlength:decimal, BilletNo:int

## dbo.MES_SAP_RR_Trn_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit

## dbo.MES_SAP_UD_Trn_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit

## dbo.MES_SAP_UsageDecision_Trn_Tbl
ID:varchar, InspectionLot:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, UsgDecCode:varchar, Message:varchar, SAPPostingStatus:varchar, SAPTransactionID:varchar, HeatNo:int, MaterialType:varchar

## dbo.MES_SAP_WO_Trn_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit

## dbo.MES_SAP_WorkOrder_Movements_Trn_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, PostingDate:date, IsProcessed:bit, MaterialDocument:varchar, MovementType:int, Batch:varchar, StorageLocation:int, DebitCreditindication:varchar, Quantity:decimal, NoOfItem:int, QuantityinCount:int

## dbo.MES_TMT
ID:varchar, BatchNo:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, InTime:datetime, OutTime:datetime, IsProcessed:bit, Status:varchar, CutLength:decimal, RemainLength:decimal, HeatNo:varchar, BilletNo:varchar, workorder:varchar

## dbo.MES_TMT_Small_Cut
ID:varchar, BatchNo:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, BundleNo:varchar, Length:decimal, Status:varchar

## dbo.MES_WO_Trn_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit

## dbo.MES_WRM
ID:varchar, BatchNo:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, InTIme:datetime, ReportDate:date, IsProcessed:bit, OutTIme:datetime, Status:varchar, BundleNo:varchar, Heatno:varchar, Billetno:varchar, Workorder:varchar

## dbo.Month_Master
ID:varchar, Name:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, MonthNumber:int

