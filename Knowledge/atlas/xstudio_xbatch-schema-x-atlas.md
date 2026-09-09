---
type: note
subtype: schema-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch schema atlas: X

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.XBatch_Batch_BOM_Mst_Tbl
ID:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ItemID:varchar, Quantity:decimal, UOMID:varchar, UnitProcedureID:varchar, OperationID:varchar, PhaseGroupID:varchar, PhaseID:varchar, ActualQuantity:decimal, QuantityDeviation:decimal, SourceType:varchar

## dbo.XBatch_Batch_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, BatchNumber:varchar, BatchMode:varchar, ProcessCellID:varchar, Quantity:decimal, QuantityUnitID:varchar, StartTime:datetime, EndTime:datetime, StatusID:varchar, Version:varchar, Position:varchar, ApprovedBy:varchar, ApprovedOn:datetime, ScheduledBy:varchar, ScheduledOn:datetime, ActualStartTime:datetime, ActualEndTime:datetime, WorkOrderID:varchar

## dbo.XBatch_Batch_Operation_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentTypeID:varchar, OutputMaterialID:varchar, SrNo:int, EquipmentID:varchar, StartTime:datetime, EndTime:datetime, StatusID:varchar, Position:varchar, OriginalID:varchar, OutputMaterialQuantity:decimal

## dbo.XBatch_Batch_Phase_Group_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SrNo:int, StartTime:datetime, EndTime:datetime, StatusID:varchar, Position:varchar, OriginalID:varchar

## dbo.XBatch_Batch_Phase_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Type:varchar, CapabilityID:varchar, MaterialID:varchar, Quantity:decimal, SrNo:int, StartTime:datetime, EndTime:datetime, StatusID:varchar, Position:varchar, TemplateID:varchar, OriginalID:varchar

## dbo.XBatch_Batch_Phase_Parameter_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Value:decimal, MinValue:decimal, MaxValue:decimal, AvgValue:decimal, Description:varchar, OriginalID:varchar

## dbo.XBatch_Batch_Phase_Trn_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Type:varchar, CapabilityID:varchar, MaterialID:varchar, SrNo:int, StartTime:datetime, EndTime:datetime, StatusID:varchar

## dbo.XBatch_Batch_Unit_Procedure_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SrNo:int, UnitID:varchar, StartTime:datetime, EndTime:datetime, StatusID:varchar, OriginalID:varchar, Position:varchar

## dbo.XBatch_Billets_Transfer_History_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, BilletNo:varchar, SubLotNo:varchar, RecievedDate:datetime, InventoryID:varchar, LocationType:varchar, RecievedBy:varchar, StackID:varchar, LayerID:varchar, MaterialGrade:varchar, LocationAssignedDate:datetime, ActionBy:varchar, CurrentStatus:varchar, InwardStatus:varchar, IsInward:bit, Isoutward:bit, OutwardBy:varchar, outwardDate:datetime, BilletLength:int

## dbo.XBatch_Billets_Transfer_History_Tbl_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, BilletNo:varchar, SubLotNo:varchar, RecievedDate:datetime, InventoryID:varchar, LocationType:varchar, RecievedBy:varchar, StackID:varchar, LayerID:varchar, MaterialGrade:varchar, LocationAssignedDate:datetime, ActionBy:varchar, CurrentStatus:varchar, InwardStatus:varchar, IsInward:bit, Isoutward:bit, OutwardBy:varchar, outwardDate:datetime, BilletLength:int

## dbo.XBatch_ConfigParameter_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Value:varchar, Description:varchar, IsVisible:bit

## dbo.XBatch_Connection_Capability_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Description:varchar, IsStart:bit, IsHold:bit, IsRestart:bit, IsAbort:bit, IsReset:bit, IsReady:bit, IsHeld:bit, IsRun:bit, IsDone:bit, IsInterlock:bit, IsAborted:bit, InterlockValueType:varchar, ErrorCodeTag:varchar, ErrorLookUpTable:varchar, ErrorCodeField:varchar, ErrorDescriptionField:varchar

## dbo.XBatch_Connection_Interlock_Error_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SrNo:int, Description:varchar, Value:int, Type:varchar, TagName:varchar, DataSourceID:varchar

## dbo.XBatch_Connection_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, CollectorName:varchar, ChannelName:varchar, SourceEquipmentID:varchar, DestinationEquipmentID:varchar, SourceEquipmentName:varchar, DestinationEquipmentName:varchar, Status:varchar

## dbo.XBatch_Connection_Parameter_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Type:varchar, Mode:varchar, Description:varchar, IsHistorize:bit, TagName:varchar, DataSourceID:varchar

## dbo.XBatch_Connection_Segment_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.XBatch_Customer_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Address:varchar, City:varchar, State:varchar, County:varchar, ZipCode:int, ContactNumber1:varchar, ContactNumber2:varchar, EmailAddress1:varchar, EmailAddress2:varchar, Description:varchar, CustomerCode:varchar

## dbo.XBatch_Formula_Dtl_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, MaterialID:varchar, UnitID:varchar, Quantity:decimal, QuantityType:varchar, Description:varchar, IsEnabled:bit, MinQuantity:decimal, MaxQuantity:decimal

## dbo.XBatch_Formula_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Quantity:decimal, UnitID:varchar, Description:varchar, IsEnabled:bit

## dbo.XBatch_MES_Heat_Tracking
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, HeatNo:int, SteelGrade:varchar, EAFHeatStartDateTime:datetime, EAFTapStartDateTime:datetime, EAFTTTTimeMMSS:varchar, EAFPowerOnTimeMMSS:varchar, EAFPowerOffTimeMMSS:varchar, EAFTapTimeMMSS:varchar, EAFChargeWeightTon:decimal, EAFTotalChargeWeightMT:decimal, EAFLiquidMetalWeightTon:decimal, EAFLiquidMetalYield:decimal, EAFNGConsumptionSm3:decimal, EAFCarbonConsumptionKg:decimal, EAFOxygenConsumptionNm3:decimal, EAFPowerMWH:decimal, EAFBin1LimeConsumptionTon:decimal, EAFBin2DoloConsumptionTon:decimal, EAFBin3ConsumptionTon:decimal, EAFBin4ConsumptionTon:decimal, EAFCopexScrapTon:decimal, EAFHMS12Ton:decimal, EAFHMS1Ton:decimal, EAFEndCutsTon:decimal, EAFBriquetteTon:decimal, EAFBundleLMSTon:decimal, EAFHBIDRITon:decimal, EAFShreddedTon:decimal, EAFSkullTon:decimal, EAFLadleAdditionLimeKg:decimal, EAFLadleAdditionDoloKg:decimal, EAFLadleAdditionSiMnnKg:decimal, EAFLadleAdditionSiMnKg:decimal, EAFLadleAdditionFeSiKg:decimal, LRFTreatmentStartTimeHHMMSS:datetime, LRFTreatmentStopTimeHHMMSS:datetime, LRFTreatmentTimeMinutes:varchar, LRFArcingTimeMinutes:varchar, LRFLiquidMetalWeightTon:decimal, LRFArgonConsumptionNm3:decimal, LRFPowerMWH:decimal, LRFAdditionLimeKg:decimal, LRFAdditionDoloKg:decimal, LRFAdditionFeSiKg:decimal, LRFAdditionSiMnKg:decimal, LRFAdditionSiMnnKg:decimal, CCMLadleBottomOpenTime:datetime, CCMLadleBottomCloseTime:datetime, CCMArmPosition:varchar, CCMArmConsumptionTon:decimal, CCMTotalBilletCount:int, CCMCrossSectionmm:int, CCMTotalProductionTon:decimal, CCMStrand1BilletCount:int, CCMStrand1CastingSpeedAvg:decimal, CCMStrand1OscillationSpeedAvg:decimal, CCMStrand2BilletCount:int, CCMStrand3BilletCount:int, CCMStrand4BilletCount:int, CCMStrand5BilletCount:int, CCMStrand6BilletCount:int, CCMStrand2CastingSpeedAvg:decimal, CCMStrand3CastingSpeedAvg:decimal, CCMStrand4CastingSpeedAvg:decimal, CCMStrand5CastingSpeedAvg:decimal, CCMStrand6CastingSpeedAvg:decimal, CCMStrand2OscillationSpeedAvg:decimal, CCMStrand3OscillationSpeedAvg:decimal, CCMStrand4OscillationSpeedAvg:decimal, CCMStrand5OscillationSpeedAvg:decimal, CCMStrand6OscillationSpeedAvg:decimal, EAFWorkOrder:varchar, LRFWorkOrder:varchar, CCMWorkOrder:varchar, Sequence:varchar, ShiftManager:varchar, Melter:varchar, SetupTime:time, TappingDuration:varchar, ArcingOFFtime:varchar, TPH:decimal, TapEndTime:time, PowerDrawnAvg:decimal, Bundlewip:decimal, BundleTotal:decimal, RDcut:decimal, RDcutWip:decimal, RDcutTotal:decimal, RMSEndCut:decimal, RMSEndCutWIP:decimal, RMSEndCutTotal:decimal, CopexscrapWIP:decimal, CopexscrapTotal:decimal, SkullWIP:decimal, SkullTotal:decimal, PDOScrap:decimal, BriquetteWIP:decimal, BriquetteTotal:decimal, PigIron:decimal, PigIronWIP:decimal, PigIronTotal:decimal, DRI:decimal, DRIWIP:decimal, DRITotal:decimal, HBI:decimal, HBIWIP:decimal, HBITotal:decimal, LMProdnasperOprn:decimal, EnergyKWH:decimal, AvgPowerDrawn:decimal, ScrapTotal:decimal, Totalo2:decimal, NaturalGas:decimal, InjectionCarbon:decimal, TopCarbonkg:decimal, Electrodekg:decimal, Electrode1:decimal, Electrode2:decimal, Electrode3:decimal, FirstTemp:decimal, Tappingtemp:decimal, TappingCarbon:decimal, N2ppm:decimal, TappingAlingot:decimal, TappingLime:decimal, Flourspar:decimal, TappingHCFeCr:decimal, LcFeCr:decimal, HcFeCr:decimal, LcFeMn:decimal, Nutcoke:decimal, Tappingothercarbon:decimal, Gunningkg:decimal, LRFElectrodes:decimal, LFEngineer:varchar, LFHoldingTime:varchar, MnRecovery:decimal, SiRecovery:decimal, CACkg:decimal, Spar:decimal, AlIngot:decimal, LCC:decimal, HCFeMn:decimal, LFinTemp:decimal, TundishT1:decimal, TundishT2:decimal, TundishT3:decimal, AvgTemp:decimal, Superheat:decimal, NoofStrands:decimal, Noof140mmBillets:decimal, HotChargeBillets:decimal, Noof130mm12m875mbillets:decimal, CutLength:decimal, Billets103mtr:decimal, Billet117mtr:decimal, Tonnage12m875m:decimal, Noof6mbillets:decimal, Billet6mwt:decimal, TotalBillet:decimal, Noof87mbillets:decimal, Billets87mweight:decimal, LadleLoss:decimal, SecWt:decimal, EndCutShortLength:decimal, Tundishloss:decimal, LaunderLoss:decimal, Scaleloss:decimal, Others:decimal, LiquidMetalCalc:decimal, YieldChargetoBL:decimal, YieldChargetoLM:decimal, CasterYield:decimal, TeemingStart:datetime, TeemingEnd:datetime, CastingTime:datetime, PowerOFFtimechecker:varchar, LiftTemp:decimal, LRFLCFeMn:decimal, Hour:time, CCMTPH:decimal, EndCut:decimal, StartTime:datetime

## dbo.XBatch_Material_Grade_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Description:varchar, Color:varchar, IsActive:bit

## dbo.XBatch_Material_Inventory_Mst_Tbl
ID:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, LotNumber:varchar, SublotNumber:varchar, Quantity:decimal, UOMID:varchar, LocationType:varchar, LocationID:varchar, LocationName:varchar, IsExpired:bit, ExpiryDate:date, ReceivedDate:datetime, Vendor:varchar, PONumber:varchar, GRNNumber:varchar, InvoiceNumber:varchar, Price:decimal, Description:varchar, OperationID:varchar, ItemSource:varchar, Remark:varchar, LotwiseBillet:varchar, SrNo:varchar, MaterialGrade:varchar, AvailableQuantityPrice:decimal, BilletReceivedBy:varchar, StackLocation:varchar, InwardDate:datetime, InwardBy:varchar, MovementType:varchar, OutwardLocation:varchar, Outwardby:varchar, OutwardDate:datetime, GradeID:varchar, outwardremarks:varchar, Color:varchar, LayerNo:varchar, BilletLength:int, PlantName:varchar, StorageLocation:varchar, IsPlantToPlantTransfer:bit, QuantityinCount:int, PostingMaterialType:varchar

## dbo.XBatch_Material_Inventory_Mst_Tbl_Audit
ID:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, LotNumber:varchar, SublotNumber:varchar, Quantity:decimal, UOMID:varchar, LocationType:varchar, LocationID:varchar, LocationName:varchar, IsExpired:bit, ExpiryDate:date, ReceivedDate:datetime, Vendor:varchar, PONumber:varchar, GRNNumber:varchar, InvoiceNumber:varchar, Price:decimal, Description:varchar, OperationID:varchar, ItemSource:varchar, Remark:varchar, LotwiseBillet:varchar, SrNo:varchar, MaterialGrade:varchar, AvailableQuantityPrice:decimal, BilletReceivedBy:varchar, StackLocation:varchar, InwardDate:datetime, InwardBy:varchar, MovementType:varchar, OutwardLocation:varchar, Outwardby:varchar, OutwardDate:datetime, GradeID:varchar, outwardremarks:varchar, Color:varchar, LayerNo:varchar, BilletLength:int

## dbo.XBatch_Material_Item_Cons_Per_WorkOrder_Tbl
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, IsProcessed:bit, Quantity:decimal, UOMID:varchar, MaterialID:varchar, Name:varchar, WorkOrder:varchar, ParentID:varchar, ReportDate:date

## dbo.XBatch_Material_Item_Cons_Trn_Tbl
ID:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, LotNumber:varchar, SublotNumber:varchar, Quantity:decimal, UOMID:varchar, GradeID:varchar, MaterialID:varchar, HeatNo:int, Price:decimal, DeclareQuantity:decimal

## dbo.XBatch_Material_Item_Mst_Tbl
ID:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Vendor:varchar, LotNumber:varchar, Quantity:decimal, Price:decimal, PONumber:varchar, InvoiceNumber:varchar, ReceivedDate:datetime, LocationType:varchar, LocationID:varchar, LocationName:varchar, ExpiryDate:date, IsExpired:bit, UOMID:varchar, GradeID:varchar, GRNNumber:varchar, Description:varchar

## dbo.XBatch_Material_Item_Prod_Per_WorkOrder_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, WorkOrder:varchar, MaterialID:varchar, Quantity:decimal, UOMID:varchar

## dbo.XBatch_Material_Item_Prod_Trn_Tbl
ID:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, LotNumber:varchar, SublotNumber:varchar, Quantity:decimal, UOMID:varchar, GradeID:varchar, HeatNo:int, MaterialID:varchar, DeclareQuantity:decimal

## dbo.XBatch_Material_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, TypeID:varchar, UnitID:varchar, Number:varchar, StockType:varchar, Quantity:decimal, Description:varchar, IsEnabled:bit, CanExpire:bit, ExpireDays:int, MinInventoryLevel:decimal, MaxOrderSize:decimal, LotNumberFormat:varchar, SubLotNumberFormat:varchar, ColourCode:varchar, PageID:varchar, PlantID:varchar, StoragelocationID:varchar, Grade:varchar, RawMaterialName:varchar, SAPColorCode:varchar, InventorySpecialStockType:varchar

## dbo.XBatch_Material_Sample_Mst
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, MinValue:decimal, MaxValue:decimal, Description:varchar

## dbo.XBatch_Material_Sub_Item_Mst_Tbl
ID:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Quantity:decimal, UOMID:varchar, SubLotNumber:varchar

## dbo.XBatch_Material_Type_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Description:varchar, Color:varchar, Icon:varchar, CanProduced:bit, CanConsumed:bit, CanSold:bit, CanObsolete:bit

## dbo.XBatch_Measurement_Unit_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Description:varchar, ColourCode:varchar

## dbo.XBatch_OutwardLocation_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.XBatch_Process_Cell_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Capacity:decimal, UnitID:varchar, Description:varchar, IsEnabled:bit, Status:varchar, CurrentBatchID:varchar, MinCapacity:decimal, MaxCapacity:decimal, CollectorName:varchar, NextAvailableTime:datetime

## dbo.XBatch_Recipe_Connection_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SourceID:varchar, TargetID:varchar

## dbo.XBatch_Recipe_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, MaterialID:varchar, ProcessCellID:varchar, Version:varchar, Status:varchar, Position:varchar, ProcessTime:int

## dbo.XBatch_Recipe_Operation_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentTypeID:varchar, OutputMaterialID:varchar, SrNo:int, Position:varchar, OutputMaterialQuantity:decimal

## dbo.XBatch_Recipe_Phase_Group_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SrNo:int, Position:varchar

## dbo.XBatch_Recipe_Phase_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Type:varchar, TemplateID:varchar, CapabilityID:varchar, MaterialID:varchar, Quantity:decimal, SrNo:int, Position:varchar

## dbo.XBatch_Recipe_Phase_Parameter_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Value:decimal, Description:varchar

## dbo.XBatch_Recipe_Unit_Procedure_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SrNo:int, Position:varchar

## dbo.XBatch_Sales_Order_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ItemID:varchar, Quantity:decimal, UnitID:varchar, ReleasedDate:datetime, ApprovedDate:datetime, ApprovedBy:varchar, PlannedCompletionDate:datetime, Remarks:varchar, SalesOrderNumber:varchar, ColourCode:varchar, Status:varchar, ProgressTonnage:decimal, ProgressPercentage:decimal, RemainingTonnage:decimal, ActualCompletionDate:datetime, PlannedStartDate:datetime, RequiredCompletionDate:datetime, ActualStartDate:datetime, OrderCompletionVariance:int, OrderStartVariance:int, ActualOrderCompletionSlack:int, PlannedOrderCompletionSlack:int, ActualOrderStartLeadTime:int, ActualOrderExecutionDuration:int, PlannedOrderExecutionDuration:int, PlannedOrderStartLeadTime:int, Grade:varchar, SalesOrderItem:varchar, Area:varchar

## dbo.XBatch_Status_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Description:varchar, Color:varchar

## dbo.XBatch_Storage_Area_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Capacity:decimal, CapacityUnitID:varchar, Description:varchar, IsEnabled:bit, GradeType:varchar

## dbo.XBatch_Storage_Rack_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Number:int, IsEnabled:bit, TotalBilletStore:int, Capacity:int, assignGradeno:varchar

## dbo.XBatch_Store_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Capacity:decimal, CapacityUnitID:varchar, Description:varchar, IsEnabled:bit, ColourCode:varchar, SAPStorageLocation:varchar

## dbo.XBatch_Unit_Equipment_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentTypeID:varchar, TemplateID:varchar, EquipmentID:varchar, IsEnabled:bit, Status:varchar, CurrentBatchID:varchar, CurrentUnitProcedureID:varchar, CurrentOperationID:varchar

## dbo.XBatch_Unit_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Description:varchar, IsEnabled:bit, Status:varchar, CurrentBatchID:varchar, CurrentUnitProcedureID:varchar

## dbo.XBatch_UpdateStackLocation
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, StackID:varchar, GradeNo:varchar

## dbo.XBatch_Work_Order_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, WorkOrderNumber:varchar, SerialNumber:int, Quantity:decimal, UnitID:varchar, ItemID:varchar, Status:varchar, Description:varchar, HeatNo:varchar, SalesOrder:varchar, Equipment:varchar, StartTime:datetime, EndTime:datetime, ProgressTonnage:decimal, ProgressDuration:decimal, RemainingTonnage:decimal, ProgressPercentage:decimal, ManufacturingOrderCategory:varchar, ManufacturingOrderType:varchar, ManufacturingOrderImportance:varchar, OrderIsCreated:varchar, OrderIsReleased:varchar, OrderIsPrinted:varchar, OrderIsConfirmed:varchar, OrderIsPartiallyConfirmed:varchar, OrderIsDelivered:varchar, OrderIsDeleted:varchar, OrderIsPreCosted:varchar, SettlementRuleIsCreated:varchar, OrderIsPartiallyReleased:varchar, OrderIsLocked:varchar, OrderIsTechnicallyCompleted:varchar, OrderIsClosed:varchar, OrderIsPartiallyDelivered:varchar, OrderIsMarkedForDeletion:varchar, SettlementRuleIsCrtedManually:varchar, OrderIsScheduled:varchar, OrderHasGeneratedOperations:varchar, OrderIsToBeHandledInBatches:varchar, MaterialAvailyIsNotChecked:varchar, MfgOrderCreationDate:datetime, MfgOrderCreationTime:time, LastChangeDateTime:datetime, StorageLocation:varchar, GoodsRecipientName:varchar, UnloadingPointName:varchar, InventoryUsabilityCode:varchar, MaterialGoodsReceiptDuration:int, QuantityDistributionKey:varchar, StockSegment:varchar, OrderInternalBillOfOperations:varchar, ProductionPlant:int, Plant:varchar, MRPArea:varchar, MRPController:varchar, ProductionSupervisor:varchar, ProductionVersion:varchar, PlannedOrder:varchar, SalesOrderItem:varchar, BasicSchedulingType:varchar, ManufacturingObject:varchar, ProductConfiguration:varchar, OrderSequenceNumber:varchar, BusinessArea:varchar, CompanyCode:int, ProfitCenter:varchar, ActualCostsCostingVariant:varchar, PlannedCostsCostingVariant:varchar, FunctionalArea:varchar, MfgOrderPlannedStartDate:datetime, MfgOrderPlannedStartTime:time, MfgOrderPlannedEndDate:datetime, MfgOrderPlannedEndTime:time, MfgOrderScheduledStartDate:datetime, MfgOrderScheduledStartTime:time, MfgOrderScheduledEndDate:datetime, MfgOrderScheduledEndTime:time, MfgOrderActualReleaseDate:varchar, ProductionUnit:varchar, ProductionUnitISOCode:varchar, ProductionUnitSAPCode:varchar, MfgOrderPlannedScrapQty:decimal, MfgOrderConfirmedYieldQty:decimal, CustomerName:varchar, WBSElementExternalID:varchar, OrderLongText:varchar, ColourCode:varchar, Sn:int, MaterialName:varchar, SalesOrderName:varchar, ReleasedDate:datetime, ActualCompletionDate:datetime, SAPTransactionID:varchar, Grade:varchar, CampaignId:varchar, Length:decimal, Size:varchar, MinBundles:decimal, MaxBundles:decimal, MinQtyToRoll:decimal, NoOfPiecesInBundles:int

## dbo.XMES_API_Transaction_Summary_Fact_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, TransactionID:varchar, APIName:varchar, APIStatus:varchar, APISource:varchar, RequestedDatetime:datetime, ResponseDatetime:datetime, RequestURL:varchar, RequestBody:varchar, ResponseData:varchar, ResponseDataInsertion:varchar, ResponseError:varchar, RecordID:varchar, EntityID:varchar, LVid:varchar, LVName:varchar, ActionUserName:varchar, ResolvedEntityTable:varchar

## dbo.XMES_ActiveLife_Element_Mst_Tbl
ID:varchar, ElementNameID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Status:varchar, Activeinactiveflag:bit, LastUsedBatch:varchar

## dbo.XMES_Active_Heat
ID:varchar, HeatNo:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, HeatStartTime:datetime, HeatEndTime:datetime, IsActive:bit

## dbo.XMES_Billet_Movement_Dtl_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ChargingBedBilletNo:varchar, Section1BilletNo:varchar, Section2BilletNo:varchar

## dbo.XMES_Billet_Strand_tracking
ID:varchar, S1IT:datetime, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, S1OT:datetime, S2OT:datetime, S3OT:datetime, S4OT:datetime, S5OT:date, S6OT:datetime, S7OT:datetime, S8OT:datetime, S9OT:datetime, S10OT:datetime, S11OT:datetime, S12OT:datetime, S13OT:datetime, S14OT:datetime, S15OT:datetime, S16OT:datetime, S2IT:datetime, S3IT:datetime, S4IT:datetime, S5IT:datetime, S6IT:datetime, S7IT:datetime, S8IT:datetime, S9IT:datetime, S10IT:datetime, S11IT:datetime, S12IT:datetime, S13IT:datetime, S14IT:datetime, S15IT:datetime, S16IT:datetime, BIlletNo:varchar, Status:varchar, S17IT:datetime, S18IT:datetime, S17OT:datetime, S18OT:datetime, S0OT:datetime, Cobble:varchar, Stand8HTSample:decimal, Stand8TTSample:decimal, Stand14HTSample:decimal, Stand14TTSample:decimal, Stand8SamplingDatetime:datetime, Stand14SamplingDatetime:datetime, Sample8Status:varchar, Sample14Status:varchar, Stand:int, EndProduct:varchar

## dbo.XMES_Billet_Tracking_Per_Strand
ID:varchar, HeatNo:varchar, EventID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, IsProcessed:bit, BilletNo:varchar, StrandNo:varchar, BilletSequence:int, ChargeType:varchar, Status:varchar, StrandSequence:int

## dbo.XMES_Billet_Tracking_Trn_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, HeatNo:varchar, Batch:varchar, BilletNo:varchar, Plant:varchar, StorageLocation:varchar, StatePosition:varchar, ProcessStage:varchar, Materialid:varchar, Qualitygradeid:varchar, BilletWeight:decimal, UOMID:varchar, ManufacturingOrder:varchar, BilletQuantity:int, PostingMaterialType:varchar, CutLength:decimal

## dbo.XMES_Billet_VS_GLS_Grade_Mapping
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, BilletGrade:varchar, GLSGrade:varchar

## dbo.XMES_CCM_Billet_Genealogy_Trn_Tbl
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, CutEventID:varchar, Status:varchar, ChargeType:varchar, StrandSequence:int, IsProcessed:bit, StrandNo:varchar, BilletSequence:int, HeatNo:varchar, BilletNo:varchar, CutStartTime:datetime, CutEndTime:datetime, ProducedStartTime:datetime, ProducedEndTime:datetime, ProducedEventID:varchar

## dbo.XMES_CCM_Billet_Master_Trn_Tbl
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, CutLength:decimal, Plant:varchar, ParentID:varchar, StatePosition:varchar, Qualitygradeid:varchar, BilletQuantity:int, EntryDateTime:datetime, BilletWeight:decimal, BilletNo:varchar, ProcessStage:varchar, HeatNo:varchar, UOMID:varchar, Batch:varchar, IsProcessed:bit, ManufacturingOrder:varchar, ReportDate:date, Name:varchar, PostingMaterialType:varchar, StorageLocation:varchar, Materialid:varchar

## dbo.XMES_CCM_Billet_Sequence
ID:varchar, HeatNo:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, StrandNo:varchar, CurrentSequence:int, StrandSequence:int

## dbo.XMES_CCM_Billet_Sequence_New
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, CurrentSequence:int, StrandNo:varchar, StrandSequence:int, HeatNo:varchar

## dbo.XMES_Campaign_Plan_Mst
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Working:varchar, Material:varchar, Size:decimal, Grade:varchar, TotalQtyWt:decimal, TotalPieces:int, Status:varchar, CampaignId:varchar, Length:varchar, StartDate:date, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, MinQtytoRollMT:decimal, MaxQtytoRollMT:decimal, MinNoOfBundles:decimal, MaxNoOfBundles:decimal, Action:varchar, AllFilesUpload:varchar, EndDate:date, UploadStatus:varchar, Productname:varchar, ProgressTonnage:decimal, ProgressPercentage:decimal, RemaningTonnage:decimal, CampaignstartDate:date, CampaignEndDate:date, WRMExcelUpload:varchar, WRMStatus:varchar, WRMUploadStatus:varchar

## dbo.XMES_Element_Life_Counter_Trn_Tbl
ID:varchar, CurrentLife:int, ElementNameID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ConsumeLifepercentage:decimal, AlertPercentage:int, LastUsedBatch:varchar, MaximumLife:int

## dbo.XMES_Element_Life_Month_Wise_Summary
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Month:varchar, MonthNumber:int, Year:int, ShellFullDown:int, EAFAvgLife:int, LadleAvgLife:int, TotalTundishUsed:int, AvgSeq:int

## dbo.XMES_Element_Life_Type_Mapping_Mst_Tbl
ID:varchar, ElementType:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, DataCaptureType:varchar

## dbo.XMES_Grade_Protocol_CCM_Parameters_Mst_Tbl
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ParentID:varchar, Values:varchar, Unit:varchar

## dbo.XMES_Grade_Protocol_CCM_Remarks_Mst_Tbl
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Remarks:varchar, ParentID:varchar

## dbo.XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl
ID:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Values:varchar, Unit:varchar, Section:varchar, Grade:varchar

## dbo.XMES_Grade_Protocol_EAF_Remarks_Mst_Tbl
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Remarks:varchar, ParentID:varchar

## dbo.XMES_Grade_Protocol_LRF_Parameters_Mst_Tbl
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ParentID:varchar, Values:varchar, Unit:varchar

## dbo.XMES_Grade_Protocol_LRF_Remarks_Mst_Tbl
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Remarks:varchar, ParentID:varchar

## dbo.XMES_Grade_Protocol_Super_Heat_Speed_Nozzle_Mst_Tbl
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Superheat:varchar, ParentID:varchar, SpeedAsPerNozzle:varchar

## dbo.XMES_Grade_Protocol_Tapping_Additions_Mst_Tbl
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ParentID:varchar, Values:varchar, Unit:varchar

## dbo.XMES_Life_Element_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.XMES_Life_Element_Type_Mst_Tbl
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Name:varchar, Srno:int

## dbo.XMES_Life_Tracker_Register_Mst_Tbl
ID:varchar, Name:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Status:varchar, Srno:int

## dbo.XMES_Live_Billet_Charging_Bed
ID:varchar, BilletNo:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, InTIme:datetime, OutTime:datetime, IsProcessed:bit, BedNo:varchar, Status:varchar, BatchNo:varchar, SequenceNo:int, BilletTrackingStatus:varchar, BilletAreaWiseTracking:varchar, BilletLength:varchar

## dbo.XMES_Live_Charging_SECT1
ID:varchar, BilletNo:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, IsProcessed:bit, InTIme:datetime, OutTime:datetime, Status:varchar, Type:varchar, ReverseWorkFlow:varchar

## dbo.XMES_Live_Charging_SECT2
ID:varchar, BilletNo:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, IsProcessed:bit, InTIme:datetime, OutTime:datetime, Status:varchar, Weighment:decimal, FurnaceOutTime:datetime, TotalResidenceTime:int

## dbo.XMES_Log_Trn_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, ExecutionQuery:nvarchar, Type:varchar, Status:varchar, SrNo:int, SubSeqNo:int

## dbo.XMES_Process_Stage_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, StageCode:varchar, StageName:varchar, StageGroup:varchar, StageType:varchar, Sequence:int

## dbo.XMES_Production_Campaign_Tracking
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Work_Order:varchar, Sales_Order:varchar, Billet_Charged:varchar, Billet_Rolled:varchar, Quantity_Produce_MT:varchar, Bundles:varchar, Total_Pcs:varchar, Remaining_Pcs:varchar, PercentageComplete:varchar, Status:varchar, CampaignId:varchar, ProductionStartDate:datetime, ProductionEndDate:datetime, ReleasedDate:datetime, OnholdDate:datetime, CancelledDate:datetime, CompletedDate:datetime, AbortDate:datetime, RunningDate:datetime

## dbo.XMES_RM_Campaign_Plan_Trn
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Country:varchar, SONumber:varchar, ItemNo:int, MaterialNo:varchar, Specification:varchar, MinQtytoRollMT:decimal, MaxQtytoRollMT:int, Length:decimal, PositiveTolerance:decimal, NegativeTolerance:int, TagDetails:varchar, Remarks:varchar, MinNoOfBundles:int, MaxNoOfBundles:int, BundlesweightTon:decimal, NumberOfPiecesInBundles:int, Section:int, CampaignId:varchar, WorkorderNo:varchar, status:varchar, AllFIleUpload:varchar, Size:varchar, Validation:bit, ContractNo:int, Grade:varchar, NoofCoilstoBeRoll:int, BilletType:varchar, Customer:varchar

## dbo.XMES_RM_Furnace_Billet_Trn_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Starttime:datetime, EndTime:datetime, HeatNo:varchar, BilletNo:varchar, TotalResidenceTime:decimal, zone2ResidenceTime:datetime, zone3ResidenceTime:datetime, zone4ResidenceTime:datetime, zone5ResidenceTime:datetime, zone6ResidenceTime:datetime, zone7ResidenceTime:datetime, zone8ResidenceTime:datetime, zone1ResidenceTime:datetime

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

