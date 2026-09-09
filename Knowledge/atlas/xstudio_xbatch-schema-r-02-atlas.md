---
type: note
subtype: schema-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch schema atlas: R part 2

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.RM_Mill_Pass_Card
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, StandNo:int, Section:varchar, RollNumberTop:int, RollNumberBottom:int, RollDiameterTop:int, RollDiameterBottom:int, Hardness:decimal, PassNo:int, NameOfGroove:varchar, ExpectedTonnage:int, SectionName:varchar, DateOfRolling:datetime, RollingSize:decimal, CassetNo:int

## dbo.RM_Mill_Pass_Card_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, StandNo:int, Section:varchar, RollNumberTop:int, RollNumberBottom:int, RollDiameterTop:int, RollDiameterBottom:int, Hardness:decimal, PassNo:int, NameOfGroove:varchar, ExpectedTonnage:int, SectionName:varchar, DateOfRolling:datetime, RollingSize:decimal, CassetNo:int

## dbo.RM_Mill_Properties_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, IsProcessed:bit, StorageType:varchar, IsHavingWeighingScale:bit, WeighmentType:varchar, FixWeightTag:varchar, LevelTag:varchar, LevelConversionType:varchar, Multiplier:decimal, Offset:decimal, LevelLookUpTable:varchar, LevelFieldName:varchar, WeightFieldName:varchar

## dbo.RM_Mill_Tag_Mapping_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, Attribute:varchar, DataSourceID:varchar, TagName:varchar, InstrumentTag:varchar, HHRange:decimal, HRange:decimal, LRange:decimal, LLRange:decimal, ColorGTHH:varchar, ColorBWHHH:varchar, ColorBWHL:varchar, ColorBWLLL:varchar, ColorLTLL:varchar, DocumentGTHH:varchar, DocumentBWHHH:varchar, DocumentBWHL:varchar, DocumentBWLLL:varchar, DocumentLTLL:varchar, Type:varchar, IsXBatchTag:bit

## dbo.RM_NGConsumption
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Date:date, FromTime:datetime, ToTime:datetime, RollingSize:varchar, Grade:varchar, Billet130Hot:int, Billet130Cold:int, Billet140Cold:int, Billet140Hot:int, Billet150Hot:int, Billet150Cold:int, Discharged:int, TotalBillet:decimal, NGCong:decimal, NGCons:int, TotalNG:decimal, CP1Operator:varchar, Crosssection:int, Shift:varchar

## dbo.RM_NGConsumption_Report
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, StartTime:datetime, EndTime:datetime, ReportDate:date, IsProcessed:bit, GRADE:varchar, DISCHARGED:decimal, TOTALBILLETMT:decimal, NGCONG:decimal, NGCONS:decimal, TOTALNG:decimal, HOTCold:decimal, CROSSSECTION:decimal, CrossSectionMax:decimal

## dbo.RM_Open_Campaign
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, CustomerName:varchar, Grade:varchar, Material:varchar, OpenQty:int, OrderDate:date, ProductCode:varchar, ReleaseQty:int, RollingQty:int, SalesOrderNo:varchar, Size:decimal, RollingDate:datetime, Status:varchar, SequenceNo:int, RollingReleaseQty:int

## dbo.RM_Operator_HeatSelection
ID:varchar, Heatno:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, BilletQty:int, Grade:varchar, BilletLength:varchar, Remainingbilletincharging:int, Srno:int, CampaignId:varchar, workorder:varchar, length:decimal

## dbo.RM_Rebar_Attribute_Tag_Template_Dtl_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Attribute:varchar, HHRange:decimal, HRange:decimal, LRange:decimal, LLRange:decimal, ColorGTHH:varchar, ColorBWHHH:varchar, ColorBWHL:varchar, ColorBWLLL:varchar, ColorLTLL:varchar, DocumentGTHH:varchar, DocumentBWHHH:varchar, DocumentBWHL:varchar, DocumentBWLLL:varchar, DocumentLTLL:varchar, ExtendRetrievalType:varchar, ExtendEquationType:varchar, ExtendEquation:varchar, TransactionRetrievalType:varchar, Procedure:varchar, PWherecolumn:varchar, POperator:varchar, PConditionType:varchar, PMSTAttribute:varchar, PWhereValue:varchar, IType:varchar, TransactionEquationType:varchar, TransactionEquation:varchar

## dbo.RM_Rebar_Attribute_Tag_Template_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.RM_Rebar_Block
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, StartTime:datetime, EndTime:datetime, ReportDate:date, IsProcessed:bit

## dbo.RM_Rebar_Capability_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, IsProcessed:bit, Description:varchar, IsStart:bit, IsHold:bit, IsRestart:bit, IsAbort:bit, IsReset:bit, IsReady:bit, IsHeld:bit, IsRun:bit, IsDone:bit, IsInterlock:bit, IsAborted:bit, InterlockValueType:varchar, ErrorCodeTag:varchar, ErrorLookUpTable:varchar, ErrorCodeField:varchar, ErrorDescriptionField:varchar

## dbo.RM_Rebar_Data
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, RebarPostprCurrentA:decimal, RebarPostprSpeedRpm:decimal, RebarPostprTorqueNm:decimal, RebarPostprSpeedMps:decimal, RebarTmtWaterflowLine1Lpm:decimal, RebarTmtWaterflow2Line2Lpm:decimal, RebarTmtWaterflow3Line3Lpm:decimal, RebarTmtWaterflow4Line4Lpm:decimal, RebarTmtMainWaterflowOutLpm:decimal, RebarTmtWaterpressBar:decimal, RebarTmtWatertempC:decimal, RebarDividingShear1CurrentA:decimal, RebarDividingShear1SpeedRpm:decimal, RebarDividingShear1TorqueNm:decimal, RebarDividingShear1SpeedMps:decimal, RebarFinishbyprtCurrentA:decimal, RebarFinishbyprtSpeedRpm:decimal, RebarFinishbyprtTorqueNm:decimal, RebarFinishbyprtSpeedMps:decimal, RebarTmtextCurrentA:decimal, RebarTmtextSpeedRpm:decimal, RebarTmtextTorqueNm:decimal, RebarTmtextSpeedMps:decimal, RebarShortBarDivCurrentA:decimal, RebarShortBarDivSpeedRpm:decimal, RebarShortBarDivTorqueNm:decimal, RebarShortBarDivSpeedMps:decimal, RebarCbapprt1CurrentA:decimal, RebarCbapprt1SpeedRpm:decimal, RebarCbapprt1TorqueNm:decimal, RebarCbapprt1SpeedMps:decimal, RebarCbapprt2CurrentA:decimal, RebarCbapprt2SpeedRpm:decimal, RebarCbapprt2TorqueNm:decimal, RebarCbapprt2SpeedMps:decimal, RebarCbapprt3CurrentA:decimal, RebarCbapprt3SpeedRpm:decimal, RebarCbapprt3TorqueNm:decimal, RebarCbapprt3SpeedMps:decimal, RebarCbapprt4CurrentA:decimal, RebarCbapprt4SpeedRpm:decimal, RebarCbapprt4TorqueNm:decimal, RebarCbapprt4SpeedMps:decimal, RebarCbapprt5CurrentA:decimal, RebarCbapprt5SpeedRpm:decimal, RebarCbapprt5TorqueNm:decimal, RebarCbapprt5SpeedMps:decimal, RebarCbapprt6CurrentA:decimal, RebarCbapprt6SpeedRpm:decimal, RebarCbapprt6TorqueNm:decimal, RebarCbapprt6SpeedMps:decimal, RebarCbrit1CurrentA:decimal, RebarCbrit1SpeedRpm:decimal, RebarCbrit1TorqueNm:decimal, RebarCbrit1SpeedMps:decimal, RebarCbrit2CurrentA:decimal, RebarCbrit2SpeedRpm:decimal, RebarCbrit2TorqueNm:decimal, RebarCbrit2SpeedMps:decimal, RebarCbrit3CurrentA:decimal, RebarCbrit3SpeedRpm:decimal, RebarCbrit3TorqueNm:decimal, RebarCbrit3SpeedMps:decimal, RebarCbrit4CurrentA:decimal, RebarCbrit4SpeedRpm:decimal, RebarCbrit4TorqueNm:decimal, RebarCbrit4SpeedMps:decimal, RebarCbrit5CurrentA:decimal, RebarCbrit5SpeedRpm:decimal, RebarCbrit5TorqueNm:decimal, RebarCbrit5SpeedMps:decimal, RebarCbrit6CurrentA:decimal, RebarCbrit6SpeedRpm:decimal, RebarCbrit6TorqueNm:decimal, RebarCbrit6SpeedMps:decimal

## dbo.RM_Rebar_Event_Action_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, StateID:varchar, Configuration:varchar, ActionType:varchar, StateMode:varchar, IsActive:bit

## dbo.RM_Rebar_Event_Attribute_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, TemplateID:varchar, AttributeName:varchar, TagType:varchar

## dbo.RM_Rebar_Event_Configuration_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EventType:varchar, TransactionEntity:varchar, IsActive:bit, EventMstID:varchar

## dbo.RM_Rebar_Event_Error_Condition_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ErrorCondition:varchar, ErrorMessage:varchar

## dbo.RM_Rebar_Event_Error_Configuration_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ErrorLookupType:varchar, ErrorAttribute:varchar, ErrorLookupEntity:varchar, ErrorCodeAttribute:varchar, ErrorMessageAttribute:varchar

## dbo.RM_Rebar_Event_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EventType:varchar, TransactionEntity:varchar, IsActive:bit

## dbo.RM_Rebar_Event_State_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, StateName:varchar, StateSequence:int, StateCondition:varchar, IsErrorState:bit, StateOnWorkFlow:varchar, StateOffWorkFlow:varchar, IsActive:bit, WorkFlowAttribute:varchar, IsWorkFlowEnable:bit, StateOnDelay:int, StateOffDelay:int, IsDifferentOffCondition:bit, StateOffCondition:varchar

## dbo.RM_Rebar_Event_Tag_Mapping_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, Attribute:varchar, TagName:varchar, CollectorID:varchar, ChannelID:varchar

## dbo.RM_Rebar_Interlock_Error_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, IsProcessed:bit, SrNo:int, Description:varchar, Value:int, Type:varchar

## dbo.RM_Rebar_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentTypeID:varchar, TemplateID:varchar, AreaID:varchar, AssetIdentificationProperties:varchar

## dbo.RM_Rebar_Parameter_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, IsProcessed:bit, Type:varchar, Mode:varchar, Description:varchar, IsHistorize:bit, DefaultValue:varchar

## dbo.RM_Rebar_Properties_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, IsProcessed:bit, StorageType:varchar, IsHavingWeighingScale:bit, WeighmentType:varchar, FixWeightTag:varchar, LevelTag:varchar, LevelConversionType:varchar, Multiplier:decimal, Offset:decimal, LevelLookUpTable:varchar, LevelFieldName:varchar, WeightFieldName:varchar

## dbo.RM_Rebar_Tag_Mapping_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, Attribute:varchar, DataSourceID:varchar, TagName:varchar, InstrumentTag:varchar, HHRange:decimal, HRange:decimal, LRange:decimal, LLRange:decimal, ColorGTHH:varchar, ColorBWHHH:varchar, ColorBWHL:varchar, ColorBWLLL:varchar, ColorLTLL:varchar, DocumentGTHH:varchar, DocumentBWHHH:varchar, DocumentBWHL:varchar, DocumentBWLLL:varchar, DocumentLTLL:varchar, Type:varchar, IsXBatchTag:bit

## dbo.RM_Reheating_Furnace_Attribute_Tag_Template_Dtl_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Attribute:varchar, HHRange:decimal, HRange:decimal, LRange:decimal, LLRange:decimal, ColorGTHH:varchar, ColorBWHHH:varchar, ColorBWHL:varchar, ColorBWLLL:varchar, ColorLTLL:varchar, DocumentGTHH:varchar, DocumentBWHHH:varchar, DocumentBWHL:varchar, DocumentBWLLL:varchar, DocumentLTLL:varchar, ExtendRetrievalType:varchar, ExtendEquationType:varchar, ExtendEquation:varchar, TransactionRetrievalType:varchar, Procedure:varchar, PWherecolumn:varchar, POperator:varchar, PConditionType:varchar, PMSTAttribute:varchar, PWhereValue:varchar, IType:varchar, TransactionEquationType:varchar, TransactionEquation:varchar

## dbo.RM_Reheating_Furnace_Attribute_Tag_Template_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.RM_Reheating_Furnace_Block
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, StartTime:datetime, EndTime:datetime, ReportDate:date, IsProcessed:bit, PreheatingTopZone1TempSet:decimal

## dbo.RM_Reheating_Furnace_Capability_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, IsProcessed:bit, Description:varchar, IsStart:bit, IsHold:bit, IsRestart:bit, IsAbort:bit, IsReset:bit, IsReady:bit, IsHeld:bit, IsRun:bit, IsDone:bit, IsInterlock:bit, IsAborted:bit, InterlockValueType:varchar, ErrorCodeTag:varchar, ErrorLookUpTable:varchar, ErrorCodeField:varchar, ErrorDescriptionField:varchar

## dbo.RM_Reheating_Furnace_Data
ID:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, RMCallBillet:decimal, RMReady:decimal, FurnaceReady:decimal, SNGLineOn:decimal, NGLineOn:decimal, NGActualHour:decimal, NGActualShift:decimal, NGActualDay:decimal, SNGActualHour:decimal, SNGActualShift:decimal, SNGActualDay:decimal, NGPreviousHour:decimal, NGPreviousShift:decimal, NGPreviousDay:decimal, SNGPreviousHour:decimal, SNGPreviousShift:decimal, SNGPreviousDay:decimal, TotalEnergy:decimal, NGEnergy:decimal, SNGEnergy:decimal, PreHeatingZoneTopSet:decimal, PreHeatingZoneBottomSet:decimal, HeatingZoneTopSet:decimal, HeatingZoneBottomSet:decimal, SoakingZoneRightTopSet:decimal, SoakingZoneRightBottomSet:decimal, SoakingZoneLeftTopSet:decimal, SoakingZoneLeftBottomSet:decimal, SoakingZoneLeftBottomActual:decimal, SoakingZoneLeftTopActual:decimal, SoakingZoneRightBottomActual:decimal, SoakingZoneRightTopActual:decimal, CombustionAirPressureActual:decimal, CombustionAirPressureSet:decimal, FurnacePressureSet:decimal, FurnacePressureActual:decimal, PreHeatingZoneTopActual:decimal, PreHeatingZoneBottomActual:decimal, HeatingZoneTopActual:decimal, HeatingZoneBottomActual:decimal, PreheatingZoneTopAirflowActual:decimal, PreheatingZoneTopAirflowSet:decimal, PreheatingZoneTopGasflowSet:decimal, PreheatingZoneTopGasflowActual:decimal, PreheatingZoneBottomAirflowSet:decimal, PreheatingzoneBottomAirflowActual:decimal, PreheatingzoneBottomGasflowActual:decimal, PreheatingZoneBottomGasflowSet:decimal, HeatingZoneTopAirflowActual:decimal, HeatingZoneTopAirflowSet:decimal, HeatingZoneTopGasflowSet:decimal, HeatingZoneTopGasflowActual:decimal, HeatingZoneBottomAirflowActual:decimal, HeatingZoneBottomAirflowSet:decimal, HeatingZoneBottomGasflowSet:decimal, HeatingZoneBottomGasflowActual:decimal, SoakingTopLeftAirflowSet:decimal, SoakingTopLeftAirflowActual:decimal, SoakingTopLeftGasflowActual:decimal, SoakingTopLeftGasflowSet:decimal, SoakingBottomLeftAirflowSet:decimal, SoakingBottomLeftAirflowActual:decimal, SoakingBottomLeftGasflowActual:decimal, SoakingBottomLeftGasflowSet:decimal, SoakingTopRightAirflowSet:decimal, SoakingTopRightAirflowActual:decimal, SoakingTopRightGasflowActual:decimal, SoakingTopRightGasflowSet:decimal, SoakingBottomRightAirflowSet:decimal, SoakingBottomRightAirflowActual:decimal, SoakingBottomRightGasflowActual:decimal, SoakingBottomRightGasflowSet:decimal, DescalerPump1RunningStatus:decimal, DescalerPump2RunningStatus:decimal, DescalerPump3RunningStatus:decimal, DeacalerPressure:decimal, DescalerDRT1Speed:decimal, DescalerDRT2Speed:decimal, DescalerDRT3Speed:decimal, DescalerDRT4Speed:decimal, ChargingDoorOpenStatus:decimal, ChargingDoorCloseStatus:decimal, DischargingDoorCloseStatus:decimal, DischargingDoorOpenStatus:decimal

## dbo.RM_Reheating_Furnace_Event_Action_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, StateID:varchar, Configuration:varchar, ActionType:varchar, StateMode:varchar, IsActive:bit

## dbo.RM_Reheating_Furnace_Event_Attribute_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, TemplateID:varchar, AttributeName:varchar, TagType:varchar

## dbo.RM_Reheating_Furnace_Event_Configuration_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EventType:varchar, TransactionEntity:varchar, IsActive:bit, EventMstID:varchar

## dbo.RM_Reheating_Furnace_Event_Error_Condition_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ErrorCondition:varchar, ErrorMessage:varchar

## dbo.RM_Reheating_Furnace_Event_Error_Configuration_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ErrorLookupType:varchar, ErrorAttribute:varchar, ErrorLookupEntity:varchar, ErrorCodeAttribute:varchar, ErrorMessageAttribute:varchar

## dbo.RM_Reheating_Furnace_Event_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EventType:varchar, TransactionEntity:varchar, IsActive:bit

## dbo.RM_Reheating_Furnace_Event_State_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, StateName:varchar, StateSequence:int, StateCondition:varchar, IsErrorState:bit, StateOnWorkFlow:varchar, StateOffWorkFlow:varchar, IsActive:bit, WorkFlowAttribute:varchar, IsWorkFlowEnable:bit, StateOnDelay:int, StateOffDelay:int, IsDifferentOffCondition:bit, StateOffCondition:varchar
