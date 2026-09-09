---
type: note
subtype: schema-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch schema atlas: R part 1

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.RMShiftDelayEntry_CAPA
ID:varchar, Stepstorestartmill:varchar, DelayTransactionid:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Reason1:varchar, Reason2:varchar, Reason3:varchar, Reason4:varchar, Reason5:varchar, CorrectiveAction:varchar, ProposedAction:varchar, Responsibility:varchar, TargetDate:date, File:varchar, CAPANO:varchar, Area:varchar, AgencyTransactionid:varchar, Agency:varchar, OpenDate:datetime, DateofBD:date, Equipment:varchar, SubEquipment:varchar, Status:varchar, Close:varchar, CAPACloseDate:date, FromTime:datetime, ToTime:datetime, TotalTime:decimal, AgencyBeforeCAPA:varchar, AgencyAfterCAPA:varchar, TypeofBD:varchar, SequenceofBD:varchar, ContainmentAction:varchar, ImplementDate:datetime, Photos:varchar, ListofDocument:varchar, Review:varchar, ReviewResponsibility:varchar, ReviewClosedBy:varchar, ReviewDepartment:varchar, ReviewTelephone:int, VerifiedBy:varchar, CloseDate:datetime, NotificationNumber:int, FunctionalLocation:varchar, Component:varchar, Cause:varchar, EntryDateTime:datetime, Remark:varchar, DealyReason:varchar, ReportDate:date, IsProcessed:bit

## dbo.RM_Billet_Charging_And_Discharging_Logsheet
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Shift:varchar, Size:int, Grade:varchar, SlNo:int, HeatNo:int, BilletNo:int, TypeOfBilletHotOrCold:bit, BilletSizemm:decimal, BilletLengthMeters:decimal, BilletDischargedTime:time, Remarks:varchar

## dbo.RM_Billet_Charging_And_Discharging_Logsheet_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Shift:varchar, Size:int, Grade:varchar, SlNo:int, HeatNo:int, BilletNo:int, TypeOfBilletHotOrCold:bit, BilletSizemm:decimal, BilletLengthMeters:decimal, BilletDischargedTime:time, Remarks:varchar

## dbo.RM_Billet_Weight_Block
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, StartTime:datetime, EndTime:datetime, ReportDate:date, IsProcessed:bit, BilletWeightTon:decimal

## dbo.RM_Bundle_Weighing_Record
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Shift:varchar, Size:int, QualityOrGrade:varchar, SlNo:int, HeatNumber:int, BundleNumber:int, BundleWeight:decimal, Remarks:varchar

## dbo.RM_Bundle_Weighing_Record_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Shift:varchar, Size:int, QualityOrGrade:varchar, SlNo:int, HeatNumber:int, BundleNumber:int, BundleWeight:decimal, Remarks:varchar

## dbo.RM_Campaign_Data
ID:varchar, CampaignID:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, StartTime:datetime, EndTime:datetime, Progress:decimal, Status:varchar

## dbo.RM_Campaign_RollingPlan
ID:varchar, Country:varchar, CampaignId:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, SONumber:varchar, ItemNo:int

## dbo.RM_Charging_Plan
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, HeatNo:varchar, BilletNo:varchar, PO:varchar, Size:varchar, CurrentLocation:varchar, SequenceNo:int, RollingID:varchar, RollingDate:date, MaterialId:varchar, RHFTime:datetime, MillTime:datetime, YardTime:datetime

## dbo.RM_Coil_Weighing_Record
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Shift:varchar, Size:decimal, QualityOrGrade:varchar, SlNo:int, HeatNumber:int, CoilNumber:int, CoilWeight:decimal, Remarks:varchar

## dbo.RM_Coil_Weighing_Record_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Shift:varchar, Size:decimal, QualityOrGrade:varchar, SlNo:int, HeatNumber:int, CoilNumber:int, CoilWeight:decimal, Remarks:varchar

## dbo.RM_Cold_Crop_Wastage
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Shift:varchar, Size:int, Cut1mm:decimal, Cut2mm:decimal, Cut3mm:decimal, Cut4mm:decimal, Cut5mm:decimal, Cut6mm:decimal, Cut7mm:decimal, Cut8mm:decimal, Cut9mm:decimal, Cut10mm:decimal, Lastpiecemm:decimal, Wt:decimal

## dbo.RM_Cold_Crop_Wastage_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Shift:varchar, Size:int, Cut1mm:decimal, Cut2mm:decimal, Cut3mm:decimal, Cut4mm:decimal, Cut5mm:decimal, Cut6mm:decimal, Cut7mm:decimal, Cut8mm:decimal, Cut9mm:decimal, Cut10mm:decimal, Lastpiecemm:decimal, Wt:decimal

## dbo.RM_Consumption_Summary_Day
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, NGCons:int, NGCons_MTD:int, NGCons_YTD:int

## dbo.RM_Delays
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, ReportDate:date, IsProcessed:bit, StartTime:datetime, EndTime:datetime, Status:varchar, WorkFlowStatus:varchar

## dbo.RM_Furnace_Logbook
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, StartTime:datetime, EndTime:datetime, ReportDate:date, IsProcessed:bit

## dbo.RM_Furnace_Logbook_Block
ID:varchar, Remarks:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, StartTime:datetime, EndTime:datetime, ReportDate:date, IsProcessed:bit, PreheatingTopZone1TempSet:decimal, PreheatingTopZone1TempActual:decimal, PreheatingBottomZone2TempSet:decimal, PreheatingBottomZone2TempActual:decimal, HeatingTopZone3TempSet:decimal, HeatingTopZone3TempActual:decimal, HeatingBottomZone4TempSet:decimal, HeatingBottomZone4TempActual:decimal, SoakingTopLeftZone5TempSet:decimal, SoakingTopLeftZone5TempActual:decimal, SoakingTopRightZone6TempSet:decimal, SoakingTopRightZone6TempActual:decimal, SoakingBottomLeftZone7TempSet:decimal, SoakingBottomLeftZone7TempActual:decimal, SoakingBottomRightZone8TempSet:decimal, SoakingBottomRightZone8TempActual:decimal, RecuperatorAirOutletTemp:decimal, RecuperatorFlueGasInletTemp:decimal, RecuperatorFlueGasOutletTemp:decimal, RecuperatorDamperPosition:decimal, PressureCombustionAirSet:decimal, PressureCombustionAirActual:decimal, PressureNaturalGasBeforePRV:decimal, PressureNaturalGasAfterPRV:decimal, PressureFurnaceSet:decimal, PressureFurnaceActual:decimal, OperatorName:varchar, ProductDIA:varchar, BilletLength:varchar

## dbo.RM_Furnace_Parameter
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Shift:varchar, OperatorName:varchar, ProductDia:varchar, BilletLength:int, PreheatingTopZone1TempSet:decimal, PreheatingTopZone1TempActual:decimal, PreheatingBottomZone2TempActual:decimal, PreheatingBottomZone2TempSet:decimal, HeatingTopBottomZone3TempSet:decimal, HeatingTopBottomZone3TempActual:decimal, HeatingBottomZone4TempActual:decimal, HeatingBottomZone4TempSet:decimal, SoakingTopLeftZone5TempSet:decimal, SoakingTopLeftZone5TempActual:decimal, SoakingTopRightZone6TempActual:decimal, SoakingTopRightZone6TempSet:decimal, SoakingBottomLeftZone7TempSet:decimal, SoakingBottomLeftZone7TempActual:decimal, SoakingBottomRightZone8TempActual:decimal, SoakingBottomRightZone8TempSet:decimal, RecuperatorAirOutletTemp:decimal, RecuperatorFlueGasInletTemp:decimal, RecuperatorFlueGasOutletTemp:decimal, RecuperatorDamperPosition:decimal, PressuremmWCCombustionAirSet:decimal, PressuremmWCCombustionAirActual:decimal, PressuremmWCNaturalGasBeforePRV:decimal, PressuremmWCNaturalGasAfterPRV:decimal, PressureFurnaceSet:decimal, PressureFurnaceActual:decimal, Remarks:varchar

## dbo.RM_Furnace_Parameter_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Shift:varchar, OperatorName:varchar, ProductDia:varchar, BilletLength:int, PreheatingTopZone1TempSet:decimal, PreheatingTopZone1TempActual:decimal, PreheatingBottomZone2TempActual:decimal, PreheatingBottomZone2TempSet:decimal, HeatingTopBottomZone3TempSet:decimal, HeatingTopBottomZone3TempActual:decimal, HeatingBottomZone4TempActual:decimal, HeatingBottomZone4TempSet:decimal, SoakingTopLeftZone5TempSet:decimal, SoakingTopLeftZone5TempActual:decimal, SoakingTopRightZone6TempActual:decimal, SoakingTopRightZone6TempSet:decimal, SoakingBottomLeftZone7TempSet:decimal, SoakingBottomLeftZone7TempActual:decimal, SoakingBottomRightZone8TempActual:decimal, SoakingBottomRightZone8TempSet:decimal, RecuperatorAirOutletTemp:decimal, RecuperatorFlueGasInletTemp:decimal, RecuperatorFlueGasOutletTemp:decimal, RecuperatorDamperPosition:decimal, PressuremmWCCombustionAirSet:decimal, PressuremmWCCombustionAirActual:decimal, PressuremmWCNaturalGasBeforePRV:decimal, PressuremmWCNaturalGasAfterPRV:decimal, PressureFurnaceSet:decimal, PressureFurnaceActual:decimal, Remarks:varchar

## dbo.RM_LogBook_For_Stand_Assembly
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, ShiftInchargeName:varchar, Shift:varchar, TechnicianName1:varchar, TechnicianName2:varchar, TechnicianName3:varchar, SrNo:int, JobDescription:varchar, PendingJob:varchar

## dbo.RM_LogBook_For_Stand_Assembly_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, ShiftInchargeName:varchar, Shift:varchar, TechnicianName1:varchar, TechnicianName2:varchar, TechnicianName3:varchar, SrNo:int, JobDescription:varchar, PendingJob:varchar

## dbo.RM_Mill_Attribute_Tag_Template_Dtl_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Attribute:varchar, HHRange:decimal, HRange:decimal, LRange:decimal, LLRange:decimal, ColorGTHH:varchar, ColorBWHHH:varchar, ColorBWHL:varchar, ColorBWLLL:varchar, ColorLTLL:varchar, DocumentGTHH:varchar, DocumentBWHHH:varchar, DocumentBWHL:varchar, DocumentBWLLL:varchar, DocumentLTLL:varchar, ExtendRetrievalType:varchar, ExtendEquationType:varchar, ExtendEquation:varchar, TransactionRetrievalType:varchar, Procedure:varchar, PWherecolumn:varchar, POperator:varchar, PConditionType:varchar, PMSTAttribute:varchar, PWhereValue:varchar, IType:varchar, TransactionEquationType:varchar, TransactionEquation:varchar

## dbo.RM_Mill_Attribute_Tag_Template_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.RM_Mill_Block
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, StartTime:datetime, EndTime:datetime, ReportDate:date, IsProcessed:bit, MaxTorque:decimal, MinTorque:decimal, AvgTorque:decimal, AvgCurrent:decimal, MinCurrent:decimal, MaxCurrent:decimal, AvgSpeed:decimal, MinSpeed:decimal, MaxSpeed:decimal, BilletNo:varchar

## dbo.RM_Mill_Capability_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, IsProcessed:bit, Description:varchar, IsStart:bit, IsHold:bit, IsRestart:bit, IsAbort:bit, IsReset:bit, IsReady:bit, IsHeld:bit, IsRun:bit, IsDone:bit, IsInterlock:bit, IsAborted:bit, InterlockValueType:varchar, ErrorCodeTag:varchar, ErrorLookUpTable:varchar, ErrorCodeField:varchar, ErrorDescriptionField:varchar

## dbo.RM_Mill_Data
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, MILLSTAND01CURRENTAPRM:decimal, MILLSTAND01SPEEDMSPRM:decimal, MILLSTAND01TORQUENMPRM:decimal, MILLSTAND02CURRENTAPRM:decimal, MILLSTAND02SPEEDMSPRM:decimal, MILLSTAND02TORQUENMPRM:decimal, MILLSTAND13CURRENTAPRM:decimal, MILLSTAND03SPEEDMSPRM:decimal, MILLSTAND03TORQUENMPRM:decimal, MILLSTAND04CURRENTAPRM:decimal, MILLSTAND04SPEEDMSPRM:decimal, MILLSTAND04TORQUENMPRM:decimal, MILLSTAND05CURRENTAPRM:decimal, MILLSTAND05SPEEDMSPRM:decimal, MILLSTAND05TORQUENMPRM:decimal, MILLSTAND06CURRENTAPRM:decimal, MILLSTAND06SPEEDMSPRM:decimal, MILLSTAND06TORQUENMPRM:decimal, MILLSTAND07CURRENTAPRM:decimal, MILLSTAND07SPEEDMSPRM:decimal, MILLSTAND07TORQUENMPRM:decimal, MILLSTAND08CURRENTAPRM:decimal, MILLSTAND08SPEEDMSPRM:decimal, MILLSTAND08TORQUENMPRM:decimal, RoughingMill:decimal, Shear1HL:decimal, Shear1TL:decimal, MILLSTAND09CURRENTAPRM:decimal, MILLSTAND09SPEEDMSPRM:decimal, MILLSTAND09TORQUENMPRM:decimal, MILLSTAND10CURRENTAPRM:decimal, MILLSTAND10SPEEDMSPRM:decimal, MILLSTAND10TORQUENMPRM:decimal, MILLSTAND11CURRENTAPRM:decimal, MILLSTAND11TORQUENMPRM:decimal, MILLSTAND12CURRENTAPRM:decimal, MILLSTAND12SPEEDMSPRM:decimal, MILLSTAND12TORQUENMPRM:decimal, MILLSTAND03CURRENTAPRM:decimal, MILLSTAND13SPEEDMSPRM:decimal, MILLSTAND13TORQUENMPRM:decimal, MILLSTAND14CURRENTAPRM:decimal, MILLSTAND14SPEEDMSPRM:decimal, MILLSTAND14TORQUENMPRM:decimal, IntermidiateMill:decimal, Shear2HL:decimal, Shear2TL:decimal, MILLSTAND15CURRENTAPRM:decimal, MILLSTAND15SPEEDMSPRM:decimal, MILLSTAND15TORQUENMPRM:decimal, MILLSTAND16CURRENTAPRM:decimal, MILLSTAND16SPEEDMSPRM:decimal, MILLSTAND16TORQUENMPRM:decimal, MILLSTAND17CURRENTAPRM:decimal, MILLSTAND17SPEEDMSPRM:decimal, MILLSTAND17TORQUENMPRM:decimal, MILLSTAND18CURRENTAPRM:decimal, MILLSTAND18SPEEDMSPRM:decimal, MILLSTAND18TORQUENMPRM:decimal, FinishingMill:decimal, DescalerPressure:decimal, DescalerTemperature:decimal, MILLPRODUCTSIZEMMPRM:decimal, MILLSPEEDMPSPRM:decimal, MILLSTAND11SPEEDMSPRM:decimal, MillStand01BilletTriggerStatus:decimal, MillStand02BilletTriggerStatus:decimal, MillStand03BilletTriggerStatus:decimal, MillStand04BilletTriggerStatus:decimal, MillStand05BilletTriggerStatus:decimal, MillStand06BilletTriggerStatus:decimal, MillStand07BilletTriggerStatus:decimal, MillStand08BilletTriggerStatus:decimal, MillStand09BilletTriggerStatus:decimal, MillStand10BilletTriggerStatus:decimal, MillStand11BilletTriggerStatus:decimal, MillStand12BilletTriggerStatus:decimal, MillStand13BilletTriggerStatus:decimal, MillStand14BilletTriggerStatus:decimal, MillStand15BilletTriggerStatus:decimal, MillStand16BilletTriggerStatus:decimal, MillStand17BilletTriggerStatus:decimal, MillStand18BilletTriggerStatus:decimal

## dbo.RM_Mill_Event_Action_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, StateID:varchar, Configuration:varchar, ActionType:varchar, StateMode:varchar, IsActive:bit

## dbo.RM_Mill_Event_Attribute_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, TemplateID:varchar, AttributeName:varchar, TagType:varchar

## dbo.RM_Mill_Event_Configuration_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EventType:varchar, TransactionEntity:varchar, IsActive:bit, EventMstID:varchar

## dbo.RM_Mill_Event_Error_Condition_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ErrorCondition:varchar, ErrorMessage:varchar

## dbo.RM_Mill_Event_Error_Configuration_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ErrorLookupType:varchar, ErrorAttribute:varchar, ErrorLookupEntity:varchar, ErrorCodeAttribute:varchar, ErrorMessageAttribute:varchar

## dbo.RM_Mill_Event_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EventType:varchar, TransactionEntity:varchar, IsActive:bit

## dbo.RM_Mill_Event_State_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, StateName:varchar, StateSequence:int, StateCondition:varchar, IsErrorState:bit, StateOnWorkFlow:varchar, StateOffWorkFlow:varchar, IsActive:bit, WorkFlowAttribute:varchar, IsWorkFlowEnable:bit, StateOnDelay:int, StateOffDelay:int, IsDifferentOffCondition:bit, StateOffCondition:varchar

## dbo.RM_Mill_Event_Tag_Mapping_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, Attribute:varchar, TagName:varchar, CollectorID:varchar, ChannelID:varchar

## dbo.RM_Mill_Interlock_Error_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, IsProcessed:bit, SrNo:int, Description:varchar, Value:int, Type:varchar

## dbo.RM_Mill_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentTypeID:varchar, TemplateID:varchar, AreaID:varchar, AssetIdentificationProperties:varchar

## dbo.RM_Mill_Parameter_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, IsProcessed:bit, Type:varchar, Mode:varchar, Description:varchar, IsHistorize:bit, DefaultValue:varchar
