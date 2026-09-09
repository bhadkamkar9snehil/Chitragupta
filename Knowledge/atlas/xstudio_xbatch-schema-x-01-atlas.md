---
type: note
subtype: schema-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch schema atlas: X part 1

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
