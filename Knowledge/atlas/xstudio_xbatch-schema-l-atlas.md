---
type: note
subtype: schema-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch schema atlas: L

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.LRF_Chemical_Composition
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, PerSn:decimal, PerMo:decimal, PerS:decimal, EntryDateTime:datetime, PerCr:decimal, ReportDate:date, PerN2:decimal, PerNi:decimal, PerSi:decimal, ParentID:varchar, IsProcessed:bit, PerP:decimal, PerAI:decimal, PerCu:decimal, Name:varchar, PerMn:decimal, PerC:decimal, HeatNo:varchar, Grade:varchar, Shift:varchar, Sample:varchar, Temperature:decimal, TestName:varchar

## dbo.LRF_Ladle_No_Per_Heat
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, HeatID:int, IsProcessed:bit, ReportDate:date, ActiveLadle:varchar, EntryDateTime:datetime, LadleLifeCount:int, ParentID:varchar

## dbo.LRF_Ladle_No_Per_Heat_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, HeatID:int, IsProcessed:bit, ReportDate:date, ActiveLadle:varchar, EntryDateTime:datetime, LadleLifeCount:int, ParentID:varchar

## dbo.LRF_Ladle_Number_Master
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, IsProcessed:bit, LadleNumber:int, ParentID:varchar, EntryDateTime:datetime

## dbo.LRF_Ladle_Number_Master_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, IsProcessed:bit, LadleNumber:int, ParentID:varchar, EntryDateTime:datetime

## dbo.LRF_Manual_Entry
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, IsProcessed:bit, ElectrodeConsumption1Kg:decimal, LaddleHoldTime:int, LRFTreatmentEndTime:datetime, LFInTime:datetime, LimeConsuption:decimal, AlloyAdditionPerTonOfSteel:int, TemperatureLifting:decimal, Temperature2:decimal, LFProcessTime:int, HeatNo:int, Name:varchar, EntryDateTime:datetime, CasterStartTime:datetime, ParentID:varchar, Temperature1:decimal, LFOutTime:datetime, NitrogenGasConsumption:int, ReportDate:date, DololimeConsumption:decimal, Grade:varchar, Sample:varchar, Temperature:int, PerC:decimal, PerMn:decimal, PerSi:decimal, PerS:decimal, PerP:decimal, PerCr:decimal, PerNi:decimal, PerMo:decimal, PerCu:decimal, PerSn:decimal, PerAl:decimal, PerN2:decimal, ElectrodeConsumption2Kg:decimal, ElectrodeConsumption3Kg:decimal, TotalElectrodeConsumption:decimal

## dbo.LRF_Manual_Entry_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, IsProcessed:bit, ElectrodeConsumption:int, LaddleHoldTime:int, LRFTreatmentEndTime:datetime, LFInTime:datetime, LimeConsuption:decimal, AlloyAdditionPerTonOfSteel:int, TemperatureLifting:decimal, Temperature2:decimal, LFProcessTime:int, HeatNo:int, Name:varchar, EntryDateTime:datetime, CasterStartTime:datetime, ParentID:varchar, Temperature1:decimal, LFOutTime:datetime, NitrogenGasConsumption:int, ReportDate:date, DololimeConsumption:decimal

## dbo.LRF_Per_Heat
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, StartTime:datetime, EndTime:datetime, Status:varchar, PowerONTime:decimal, PowerOFFTime:decimal, ArcingTime:decimal, ArgonConsumption:decimal, PowerMWH:decimal, HeatID:int, EntryDateTime:datetime, ReportDate:varchar, IsProcessed:bit, TapStart:datetime, TreatmentStart:datetime, KWHPerTon:decimal, TreatmentStop:datetime, ProcessTime:decimal, CokeandNutcokepertonofsteel:decimal, Argonpertonofsteel:decimal, LiquidMetalWeight:decimal, WorkFlowStatus:varchar, Lime:decimal, SiMnn:decimal, SiMn:decimal, FeSi:decimal, Dolo:decimal, Grade:varchar, Avg_LiquidMetalWeight:decimal, PurgingFlowLPM:decimal, HeatReportDate:date, WorkOrder:varchar, CalcLiquidMetalWeight:decimal, SAPWorkflowStatus:varchar, GLSDelta:decimal, Avg_CalcLiquidMetalWeight:decimal, ManualAlloyAdditionLime:decimal, ManualAlloyAdditionDolo:decimal, ManualAlloyAdditionFeSi:decimal, ManualAlloyAdditionSiMn:decimal, AutoAlloyAdditionLime:decimal, AutoAlloyAdditionDolo:decimal, AutoAlloyAdditionFeSi:decimal, AutoAlloyAdditionSiMn:decimal, Carbon:decimal, ManualAlloyAdditionCarbon:decimal, AutoAlloyAdditionCarbon:decimal, FlourSpar:decimal, ManualAlloyAdditionFlourSpar:decimal, AutoAlloyAdditionFlourSpar:decimal, Aluminium:decimal, ManualAlloyAdditionAluminium:decimal, AutoAlloyAdditionAluminium:decimal, NitrogenGasConsumption:decimal, ElectrodeConsumption1Kg:decimal, ElectrodeConsumption2Kg:decimal, ElectrodeConsumption3Kg:decimal, Temperature:decimal, TemperatureLifting:decimal, TotalElectrodeConsumptionKg:decimal

## dbo.LRF_ProcessTime
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, ReportDate:date, IsProcessed:bit, StartTime:datetime, EndTime:datetime, Status:varchar, HeatID:decimal, LRFHeatID:int

## dbo.LRF_SMS_5
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit

## dbo.LRF_SMS_Attribute_Tag_Template_Dtl_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Attribute:varchar, HHRange:decimal, HRange:decimal, LRange:decimal, LLRange:decimal, ColorGTHH:varchar, ColorBWHHH:varchar, ColorBWHL:varchar, ColorBWLLL:varchar, ColorLTLL:varchar, DocumentGTHH:varchar, DocumentBWHHH:varchar, DocumentBWHL:varchar, DocumentBWLLL:varchar, DocumentLTLL:varchar, ExtendRetrievalType:varchar, ExtendEquationType:varchar, ExtendEquation:varchar, TransactionRetrievalType:varchar, Procedure:varchar, PWherecolumn:varchar, POperator:varchar, PConditionType:varchar, PMSTAttribute:varchar, PWhereValue:varchar, IType:varchar, TransactionEquationType:varchar, TransactionEquation:varchar

## dbo.LRF_SMS_Attribute_Tag_Template_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.LRF_SMS_Block
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, StartTime:datetime, EndTime:datetime, ReportDate:date, IsProcessed:bit, Lime:decimal, SiMnn:decimal, SiMn:decimal, FeSi:decimal, Dolo:decimal, Lime1:decimal, ArcingTime:decimal, LRFActualEnergy:decimal, PowerOnTime:decimal, PowerOffTime:decimal, KWhPerTon:decimal, LiquidMetalWeight:decimal, ArgonConsumption:decimal, PurgingFlowLPM:decimal

## dbo.LRF_SMS_Capability_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Description:varchar, IsStart:bit, IsHold:bit, IsRestart:bit, IsAbort:bit, IsReset:bit, IsReady:bit, IsHeld:bit, IsRun:bit, IsDone:bit, IsInterlock:bit, IsAborted:bit, InterlockValueType:varchar, ErrorCodeTag:varchar, ErrorLookUpTable:varchar, ErrorCodeField:varchar, ErrorDescriptionField:varchar

## dbo.LRF_SMS_Data
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, LRFHeatID:decimal, ArcingTime:decimal, ArgonFlow:decimal, SiloName3:varchar, Silo3Kg:decimal, SiloName4:varchar, Silo4Kg:decimal, SiloName5:varchar, Silo5Kg:decimal, SiloName6:varchar, Silo6Kg:decimal, SiloName7:varchar, Silo7Kg:decimal, SiloName8:varchar, Silo8Kg:decimal, LRFActualEnergy:decimal, EnergyConsumption:decimal, PowerOffTime:decimal, LRFLime:decimal, LRFSiMn:decimal, LRFFeSi:decimal, LRFDolo:decimal, PowerOnTime:decimal, HeatID:int, LRFLiquidSteelweight:decimal, LRFGrade:varchar, PrimaryVoltage1:decimal, PrimaryVoltage2:decimal, PrimaryVoltage3:decimal, BoosterFanStatus:decimal, LRFActivePower:decimal, PurgingFlow:decimal, LRFPLCStatus:decimal, MHSPLCStatus:decimal, TransformerTap:decimal, MHSBoosterFanStatus:decimal, HydraclauricPump1Status:decimal, HydraclauricPump2Status:decimal, HydraclauricPump3Status:decimal, RecirculationPumpStatus:decimal, TransformerTemperature:decimal, SpecificPower:decimal, LRFLowerPanelHeader:varchar

## dbo.LRF_SMS_Event_Action_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, StateID:varchar, Configuration:varchar, ActionType:varchar, StateMode:varchar, IsActive:bit

## dbo.LRF_SMS_Event_Attribute_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, TemplateID:varchar, AttributeName:varchar, TagType:varchar

## dbo.LRF_SMS_Event_Configuration_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EventType:varchar, TransactionEntity:varchar, IsActive:bit, EventMstID:varchar

## dbo.LRF_SMS_Event_Error_Condition_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ErrorCondition:varchar, ErrorMessage:varchar

## dbo.LRF_SMS_Event_Error_Configuration_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ErrorLookupType:varchar, ErrorAttribute:varchar, ErrorLookupEntity:varchar, ErrorCodeAttribute:varchar, ErrorMessageAttribute:varchar

## dbo.LRF_SMS_Event_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EventType:varchar, TransactionEntity:varchar, IsActive:bit

## dbo.LRF_SMS_Event_State_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, StateName:varchar, StateSequence:int, StateCondition:varchar, IsErrorState:bit, StateOnWorkFlow:varchar, StateOffWorkFlow:varchar, IsActive:bit, WorkFlowAttribute:varchar, IsWorkFlowEnable:bit, StateOnDelay:int, StateOffDelay:int

## dbo.LRF_SMS_Event_Tag_Mapping_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, Attribute:varchar, TagName:varchar, CollectorID:varchar, ChannelID:varchar

## dbo.LRF_SMS_Interlock_Error_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, SrNo:int, Description:varchar, Value:int, Type:varchar

## dbo.LRF_SMS_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentTypeID:varchar, TemplateID:varchar, AreaID:varchar, ModuleID:varchar, ModuleType:varchar

## dbo.LRF_SMS_Parameter_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Type:varchar, Mode:varchar, Description:varchar, IsHistorize:bit

## dbo.LRF_SMS_Properties_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, StorageType:varchar, IsHavingWeighingScale:bit, WeighmentType:varchar, FixWeightTag:varchar, LevelTag:varchar, LevelConversionType:varchar, Multiplier:decimal, Offset:decimal, LevelLookUpTable:varchar, LevelFieldName:varchar, WeightFieldName:varchar

## dbo.LRF_SMS_Tag_Mapping_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, Attribute:varchar, DataSourceID:varchar, TagName:varchar, InstrumentTag:varchar, HHRange:decimal, HRange:decimal, LRange:decimal, LLRange:decimal, ColorGTHH:varchar, ColorBWHHH:varchar, ColorBWHL:varchar, ColorBWLLL:varchar, ColorLTLL:varchar, DocumentGTHH:varchar, DocumentBWHHH:varchar, DocumentBWHL:varchar, DocumentBWLLL:varchar, DocumentLTLL:varchar, Type:varchar, IsXBatchTag:bit

## dbo.LRF_Summary_Day
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, ArgonConsumption:decimal, HeatID:decimal, PowerMWH:decimal, PowerMWH_MTD:decimal, HeatID_MTD:decimal, ArgonConsumption_MTD:decimal, PowerMWH_YTD:decimal, HeatID_YTD:decimal, ArgonConsumption_YTD:decimal, SiMnn:decimal, FeSi:decimal, Dolo:decimal, SiMn:decimal, SiMnn_YTD:decimal, SiMn_MTD:decimal, Dolo_MTD:decimal, FeSi_YTD:decimal, FeSi_MTD:decimal, SiMn_YTD:decimal, Dolo_YTD:decimal, SiMnn_MTD:decimal, LiquidMetalWeight:decimal, LiquidMetalWeight_YTD:decimal, LiquidMetalWeight_MTD:decimal, Avg_LiquidMetalWeight:decimal, Avg_LiquidMetalWeight_YTD:decimal, Avg_LiquidMetalWeight_MTD:decimal, Lime:decimal, Lime_YTD:decimal, Lime_MTD:decimal, Avg_CalcLiquidMetalWeight:decimal, CalcLiquidMetalWeight:decimal, Avg_CalcLiquidMetalWeight_YTD:decimal, CalcLiquidMetalWeight_MTD:decimal, CalcLiquidMetalWeight_YTD:decimal, Avg_CalcLiquidMetalWeight_MTD:decimal, TotalElectrodeConsumptionKg:decimal, TotalElectrodeConsumptionKg_MTD:decimal, TotalElectrodeConsumptionKg_YTD:decimal, Aluminium:decimal, Carbon:decimal, Aluminium_YTD:decimal, Carbon_MTD:decimal, Aluminium_MTD:decimal, Carbon_YTD:decimal, FlourSpar:decimal, FlourSpar_YTD:decimal, FlourSpar_MTD:decimal

## dbo.LRF_Summary_Shift
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, Entrydatetime:datetime, ShiftName:varchar, HeatID:decimal, PowerMWH:decimal, ArgonConsumption:decimal, FeSi:decimal, Dolo:decimal, SiMn:decimal, SiMnn:decimal, LiquidMetalWeight:decimal, Avg_LiquidMetalWeight:decimal, Lime:decimal, CalcLiquidMetalWeight:decimal, Avg_CalcLiquidMetalWeight:decimal, TotalElectrodeConsumptionKg:decimal, Carbon:decimal, Aluminium:decimal, FlourSpar:decimal

## dbo.Laddle_Life_for_Each_Heat
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, LaddleLife:int, ReportDate:date, ParentID:varchar, LaddleNumber:varchar, IsProcessed:bit

## dbo.Laddle_Life_for_Each_Heat_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, LaddleLife:int, ReportDate:date, ParentID:varchar, LaddleNumber:varchar, IsProcessed:bit

## dbo.LadleAddition
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, ReportDate:date, IsProcessed:bit, StartTime:datetime, EndTime:datetime, Status:varchar, Silo3KG:decimal, Silo4KG:decimal, Silo5KG:decimal, Silo6KG:decimal, Silo7KG:decimal, Silo8KG:decimal, HeatNo:int

## dbo.LayerConfiguration
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ParentID:varchar, Name:varchar, decrementValue:int, StartCapacity:int, MinCapacity:int

## dbo.Length
ID:varchar, Lenght_In_Meter:decimal, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.LifeName_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.LifeName_Mst_Tbl_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.Life_Tracking
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, AlertPercentage:int, Area:varchar, CurrentLife:int, Description:varchar, LifeName:varchar, MaximumLife:int, ConsumeLife:decimal, EnableStatus:bit

## dbo.Life_Tracking_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, AlertPercentage:int, Area:varchar, CurrentLife:int, Description:varchar, LifeName:varchar, MaximumLife:int, ConsumeLife:decimal, EnableStatus:bit

## dbo.Life_Tracking_Status
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Life:varchar, LifeType:varchar, CurrentLife:int, ConsumedLifePercentage:decimal, AlertPercentage:varchar, HeatID:int, LastUpdatedTime:datetime

## dbo.Life_Tracking_Status_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Life:varchar, LifeType:varchar, CurrentLife:int, ConsumedLifePercentage:decimal, AlertPercentage:varchar, HeatID:int, LastUpdatedTime:datetime

## dbo.Life_Tracking_Transaction_tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, HeatID:varchar, Life:varchar, LifeType:varchar, CurrentLife:int, ConsumePercentage:decimal, AlertPercentage:varchar, Remarks:varchar

## dbo.Life_Tracking_Transaction_tbl_Pivot
Life1:decimal, Life2:decimal, Life3:decimal, Life4:decimal, Life5:decimal

## dbo.Lightning_Arrestor_Counter_Reading
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, F2CableEndY:int, F1CableEndB:int, F1CableEndR:int, F2CableEndB:int, F1XmerEndB:int, F2XmerEndY:int, F1XmerEndR:int, Shift:varchar, EntryDateTime:datetime, ParentID:varchar, F1XmerEndY:int, EngineerName:varchar, F2CableEndR:int, IsProcessed:bit, F1CableEndY:int, TechnicianName:varchar, Name:varchar, F2XmerEndR:int, F2XmerEndB:int, ReportDate:date

