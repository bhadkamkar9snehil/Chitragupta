---
type: note
subtype: schema-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch schema atlas: X part 3

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.XMES_RM_Heated_Billet_trn_tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, BilletNo:varchar, HeatNO:varchar, campaignid:varchar, Workorderid:varchar, ProductType:varchar

## dbo.XMES_RM_Stand_WRM
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, ReportDate:date, IsProcessed:bit, StartTime:datetime, EndTime:datetime, Status:varchar, WorkflowStatus:varchar

## dbo.XMES_RM_Strand_Process
ID:varchar, StrandNo:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, InTime:datetime, OutTime:datetime, IsProcessed:bit, BilletNo:varchar, HeatNo:varchar, Status:varchar

## dbo.XMES_Recalculate_Data
ID:varchar, CategoryName:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Name:varchar, ReportDate:date, StoreProcedure:varchar, Description:varchar

## dbo.XMES_SAP_API_Batch_Characteristics_Error
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, IsProcessed:bit, Name:varchar, ParentID:varchar, RecordID:varchar, ErrorMessage:varchar, BatchNo:varchar, TransactionID:varchar, Body:varchar, EntryDateTime:datetime, Status:varchar, SuccessMessage:varchar

## dbo.XMES_SAP_API_Batch_Creation_Error
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ParentID:varchar, Status:varchar, RecordID:varchar, Name:varchar, TransactionID:varchar, ReportDate:date, ErrorMessage:varchar, IsProcessed:bit, Body:varchar, EntryDateTime:datetime, BatchNo:varchar, SuccessMessage:varchar

## dbo.XMES_SAP_API_GoodsMovement_Error
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, TransactionID:varchar, RecordID:varchar, Body:varchar, ErrorMessage:varchar, Status:varchar, Type:varchar, Batch:varchar, ManufacturingOrder:varchar, Material:varchar, MovementType:int, SuccessMessage:varchar

## dbo.XMES_SAP_API_Inventory_Error
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, RecordID:varchar, Body:varchar, PlantCode:varchar, IsProcessed:bit, Name:varchar, ErrorMessage:varchar, EntryDateTime:datetime, TransactionID:varchar, ParentID:varchar, Status:varchar, ReportDate:date, StorageLocation:varchar, SuccessMessage:varchar

## dbo.XMES_SAP_API_PlantToPlantTransfer_Error
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Status:varchar, EntryDateTime:datetime, IsProcessed:bit, ReportDate:date, ParentID:varchar, BatchNo:varchar, Body:varchar, Name:varchar, ErrorMessage:varchar, TransactionID:varchar, SuccessMessage:varchar, RecordID:varchar

## dbo.XMES_SAP_API_ResultRecording_Error
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Name:varchar, EntryDateTime:datetime, Body:varchar, RecordID:varchar, Status:varchar, IsProcessed:bit, HeatNo:varchar, ParentID:varchar, InspectionLot:varchar, ReportDate:date, TransactionID:varchar, ErrorMessage:varchar, SuccessMessage:varchar

## dbo.XMES_SAP_API_UsageDecision_Error
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Status:varchar, EntryDateTime:datetime, IsProcessed:bit, ReportDate:date, ParentID:varchar, InspectionLot:varchar, HeatNo:varchar, Body:varchar, Name:varchar, ErrorMessage:varchar, TransactionID:varchar, SuccessMessage:varchar, RecordID:varchar

## dbo.XMES_SAP_API_WorkOrderCreation_Error
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, TransactionID:varchar, RecordID:varchar, Body:varchar, ErrorMessage:varchar, Status:varchar, WorkOrderType:varchar, TotalQuantity:decimal, ItemName:varchar, CustomerName:varchar, SuccessMessage:varchar

## dbo.XMES_SAP_Batch_Characteristic_Trn_Tbl
ID:varchar, Plant:varchar, Saptransactionid:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, HeatNo:varchar, Product:varchar, Length:decimal, Thickness:int, Width:int, SectionalWeight:decimal, ProductionSectionalWeight:decimal, NoOfPieces:int, TonsPerPiece:decimal, ExternalGrade:varchar, ProcessRoute:varchar, InspectionAgency:varchar, TDCRefNo:int, ColourCode:varchar, Pieces:int, ActualGrade:varchar, HeatSequenceNumber:varchar, BatchNo:varchar, Material:varchar, SAPPostingStatus:varchar, ClassNumber:varchar, ClassType:varchar, ObjectTable:varchar, Message:varchar

## dbo.XMES_SAP_CreateBatch_Mst_Tbl
ID:varchar, Batch:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Material:varchar, BatchIdentifyingPlant:varchar, BatchIsMarkedForDeletion:varchar, MatlBatchIsInRstrcdUseStock:varchar, Supplier:varchar, BatchBySupplier:varchar, CountryOfOrigin:varchar, RegionOfOrigin:varchar, CreationDateTime:datetime, LastChangeDateTime:datetime, BatchExtWhseMgmtInternalId:varchar, SAPTransactionID:varchar, SAPPostingStatus:varchar, HeatNo:int

## dbo.XMES_SAP_PlantToPlantTransfer_Trn_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, DocumentDate:datetime, PostingDate:datetime, MaterialDocumentHeaderText:varchar, ReferenceDocument:varchar, Material:varchar, Plant:varchar, StorageLocation:varchar, Batch:varchar, GoodsMovementType:varchar, EntryUnit:varchar, QuantityInEntryUnit:varchar, ManufacturingOrder:varchar, Supplier:varchar, Customer:varchar, SalesOrder:varchar, SalesOrderItem:varchar, IssgOrRcvgMaterial:varchar, IssgOrRcvgBatch:varchar, IssuingOrReceivingPlant:varchar, IssuingOrReceivingStorageLoc:varchar, MaterialDocumentYear:varchar, MaterialDocument:varchar, InventoryTransactionType:varchar, CreationDate:datetime, CreationTime:datetime, CreatedByUser:varchar, VersionForPrintingSlip:varchar, ManualPrintIsTriggered:varchar, CtrlPostgForExtWhseMgmtSyst:varchar, GoodsMovementCode:varchar, SAPPostingStatus:varchar, SAPTransactionID:varchar, QuantityInCount:int, HeatNo:int, PostingMaterialType:varchar

## dbo.XMES_SMS_Event_Process_Tracker_Mst
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, DurationInSeconds:int, DurationInMMSS:varchar, DurationInMinutes:decimal, Remarks:varchar, Type:varchar, Logic:varchar

## dbo.XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, CMin:decimal, CMax:decimal, CAim:decimal, MnMin:decimal, MnMax:decimal, MnAim:decimal, SMin:decimal, SMax:decimal, SAim:decimal, PMax:decimal, PMin:decimal, PAim:decimal, SiMin:decimal, SiMax:decimal, SiAim:decimal, CuMin:decimal, CuMax:decimal, CuAim:decimal, CrMin:decimal, CrMax:decimal, CrAim:decimal, NiMin:decimal, NiMax:decimal, NiAim:decimal, MoMin:decimal, MoMax:decimal, MoAim:decimal, VMin:decimal, VMax:decimal, VAim:decimal, NbMin:decimal, NbMax:decimal, NbAim:decimal, TiMax:decimal, TiAim:decimal, TiMin:decimal, N2ppmMin:decimal, N2ppmMax:decimal, N2ppmAim:decimal, AlMax:decimal, AlMin:decimal, AlAim:decimal, CeMin:decimal, CeMax:decimal, CeAim:decimal, MnPerSMin:decimal, MnPerSMax:decimal, MnPerSAim:decimal, MnPerSiMin:decimal, MnPerSiMax:decimal, MnPerSiAim:decimal

## dbo.XMES_SMS_Grade_Protocol_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SectionID:varchar, GradeID:varchar, ChemistryID:varchar, EAFRemarks:varchar, LRFRemarks:varchar, CCMRemarks:varchar, SignedFileUpload:varchar

## dbo.XMES_SectionWise_CutLength_Mst_Tbl
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Section:decimal, RB_B500B_8_0DIA_BundleWeight:decimal, RB_B500B_8_0DIA_NoOfPieces:int, RB_B500B_10_0DIA_BundleWeight:decimal, RB_B500B_10_0DIA_NoOfPieces:int, RB_B500B_12_0DIA_BundleWeight:decimal, RB_B500B_12_0DIA_NoOfPieces:int, RB_B500B_14_0DIA_BundleWeight:decimal, RB_B500B_14_0DIA_NoOfPieces:int, RB_B500B_16_0DIA_BundleWeight:decimal, RB_B500B_16_0DIA_NoOfPieces:int, RB_B500B_18_0DIA_BundleWeight:decimal, RB_B500B_18_0DIA_NoOfPieces:int, RB_B500B_20_0DIA_BundleWeight:decimal, RB_B500B_20_0DIA_NoOfPieces:int, RB_B500B_25_0DIA_BundleWeight:decimal, RB_B500B_25_0DIA_NoOfPieces:int, RB_B500B_32_0DIA_BundleWeight:decimal, RB_B500B_32_0DIA_NoOfPieces:int, RB_B500B_40_0DIA_BundleWeight:decimal, RB_B500B_40_0DIA_NoOfPieces:int

## dbo.XMES_Stage_Position_Mapping_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, StageCode:varchar, PositionType:varchar

## dbo.XMES_State_Position_State_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, PositionName:varchar, PositionType:varchar, ParentArea:varchar, SequenceNumber:int, IsActive:bit, Description:varchar

## dbo.XMES_Work_Order_Trn_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, WorkOrder:varchar, CampaignID:varchar

## dbo.XStudio_Alarm_Viewer_Filter_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, AreaName:varchar, TagName:varchar, TagValue:decimal, AlarmState:varchar, AlarmType:varchar, MessageType:varchar, ReceivedTime:datetime, EventTime:datetime, AcknowledgeTime:datetime, RetrunTime:datetime, Remark:varchar, Description:varchar

## dbo.XStudio_Shift_Dtl_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SrNo:int, StartTime:time, EndTime:time

## dbo.XStudio_Shift_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, NoOfShift:int, SrNo:int

## dbo.Xbatch_Material_Inventory_Trn_Tbl
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, MaterialGrade:varchar, PostingMaterialType:varchar, PlantName:varchar, ParentID:varchar, Quantity:decimal, StorageLocation:varchar, QuantityinCount:int, UOMID:varchar, LotNumber:varchar, Ismodified:bit, BilletNo:varchar

## dbo.Xstudio_Xbatch_ChargingPlan_Mst_Tbl
ID:varchar, Stackid:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar
