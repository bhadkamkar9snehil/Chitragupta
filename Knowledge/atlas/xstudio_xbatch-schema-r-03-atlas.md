---
type: note
subtype: schema-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch schema atlas: R part 3

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.RM_Reheating_Furnace_Event_Tag_Mapping_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, Attribute:varchar, TagName:varchar, CollectorID:varchar, ChannelID:varchar

## dbo.RM_Reheating_Furnace_Interlock_Error_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, IsProcessed:bit, SrNo:int, Description:varchar, Value:int, Type:varchar

## dbo.RM_Reheating_Furnace_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentTypeID:varchar, TemplateID:varchar, AreaID:varchar

## dbo.RM_Reheating_Furnace_Parameter_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, IsProcessed:bit, Type:varchar, Mode:varchar, Description:varchar, IsHistorize:bit

## dbo.RM_Reheating_Furnace_Properties_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, IsProcessed:bit, StorageType:varchar, IsHavingWeighingScale:bit, WeighmentType:varchar, FixWeightTag:varchar, LevelTag:varchar, LevelConversionType:varchar, Multiplier:decimal, Offset:decimal, LevelLookUpTable:varchar, LevelFieldName:varchar, WeightFieldName:varchar

## dbo.RM_Reheating_Furnace_Tag_Mapping_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, Attribute:varchar, DataSourceID:varchar, TagName:varchar, InstrumentTag:varchar, HHRange:decimal, HRange:decimal, LRange:decimal, LLRange:decimal, ColorGTHH:varchar, ColorBWHHH:varchar, ColorBWHL:varchar, ColorBWLLL:varchar, ColorLTLL:varchar, DocumentGTHH:varchar, DocumentBWHHH:varchar, DocumentBWHL:varchar, DocumentBWLLL:varchar, DocumentLTLL:varchar, Type:varchar, IsXBatchTag:bit

## dbo.RM_Ring_No_MST
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, RingNo:varchar

## dbo.RM_Roll_History_Card
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, RollNumbers:int, SupplierName:varchar, RollDiameter:int, RollDiameterMax:int, RollDrawingNo:int, StandNo:int, DiscardDiameter:int, RollMaterial:int, BarrelHardness:decimal, BarrelLength:decimal, SlNo:int, InitialDiameter:int, FinalDiameter:int, TotalTonnage:int, CummulativeTonnage:int, Remarks:varchar, TonnageRolled1:decimal, TonnageRolled2:decimal, TonnageRolled3:decimal, TonnageRolled4:decimal, TonnageRolled5:decimal, TonnageRolled6:decimal, TonnageRolled7:decimal, TonnageRolled8:decimal, TonnageRolled9:decimal, TonnageRolled10:decimal, TonnageRolled11:decimal, TonnageRolled12:decimal, TonnageRolled13:decimal

## dbo.RM_Roll_History_Card_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, RollNumbers:int, SupplierName:varchar, RollDiameter:int, RollDiameterMax:int, RollDrawingNo:int, StandNo:int, DiscardDiameter:int, RollMaterial:int, BarrelHardness:decimal, BarrelLength:decimal, SlNo:int, InitialDiameter:int, FinalDiameter:int, TotalTonnage:int, CummulativeTonnage:int, Remarks:varchar, TonnageRolled1:decimal, TonnageRolled2:decimal, TonnageRolled3:decimal, TonnageRolled4:decimal, TonnageRolled5:decimal, TonnageRolled6:decimal, TonnageRolled7:decimal, TonnageRolled8:decimal, TonnageRolled9:decimal, TonnageRolled10:decimal, TonnageRolled11:decimal, TonnageRolled12:decimal, TonnageRolled13:decimal

## dbo.RM_Roll_Stock_Card
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, PeriodFrom:datetime, PeriodTo:datetime, RollsUsedInStands:int, NewRollsOpBalanceRollsInStock:int, NewRollsReceived:int, StockNewRollsIssuedToUse:int, NewRollsClosingBalanceInStock:int, RollsInUse:int, InUseNewRollsIssuedToUse:int, RollsDiscardedDuringThisPeriod:int, TotalRollInUse:int, OpBalanceDiscardedAtStockNos:int, TotalDiscardedRollAtStockNos:int, DiscardedRollsSoldDate:datetime, NoOfRollsNos:int, DiscardedRollsBalanceStock:int, NewRollsissuedToUse:decimal

## dbo.RM_Roll_Stock_Card_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, PeriodFrom:datetime, PeriodTo:datetime, RollsUsedInStands:int, NewRollsOpBalanceRollsInStock:int, NewRollsReceived:int, StockNewRollsIssuedToUse:int, NewRollsClosingBalanceInStock:int, RollsInUse:int, InUseNewRollsIssuedToUse:int, RollsDiscardedDuringThisPeriod:int, TotalRollInUse:int, OpBalanceDiscardedAtStockNos:int, TotalDiscardedRollAtStockNos:int, DiscardedRollsSoldDate:datetime, NoOfRollsNos:int, DiscardedRollsBalanceStock:int, NewRollsissuedToUse:decimal

## dbo.RM_Roll_Turning_Job_Card
ID:varchar, CNCOperatorName:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:varchar, IsProcessed:bit, Shift:varchar, RollNo:int, GrooveCode:varchar, StdNo:varchar, RollLoadingDatetime:datetime, JobDescription:varchar, RollDiaBefore:decimal, RollDiaAfter:decimal, RollUnLoadingDatetime:datetime, SetUpTime:time, TotalMachiningTime:varchar, PassConditions:varchar, Remarks:varchar, Machine:varchar, TotalMachineTimeinMin:int, Status:varchar

## dbo.RM_Rolling_Plan
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, PONumber:varchar, Customer:varchar, Size:varchar, ReleaseRollingQty:int, SequenceNo:int, RollingDate:datetime, Status:varchar, RollingQty:int, RollingID:varchar, AssignedQty:decimal, MaterialGrade:varchar, MaterialID:varchar

## dbo.RM_Rolling_Standards
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, StandNo:int, TypeOfPass:varchar, Sizemm:decimal, RollGapFeelermm:decimal, RollGapRodmm:decimal, StaticGuideOpeningmm:decimal, EntryRollerOpening:decimal, StabilizerStaticOpeningmm:decimal, StabilizerRollerOpeningmm:decimal, DeliveryPipeOpeningmm:decimal, TwisterOpeningmm:decimal, TopToBottomSizemm:decimal

## dbo.RM_Rolling_Standards_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, StandNo:int, TypeOfPass:varchar, Sizemm:decimal, RollGapFeelermm:decimal, RollGapRodmm:decimal, StaticGuideOpeningmm:decimal, EntryRollerOpening:decimal, StabilizerStaticOpeningmm:decimal, StabilizerRollerOpeningmm:decimal, DeliveryPipeOpeningmm:decimal, TwisterOpeningmm:decimal, TopToBottomSizemm:decimal

## dbo.RM_Sales_Order
ID:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, PONumber:varchar, Customer:varchar, Size:varchar, RollingQty:int, OpenQty:int, ReleaseQty:int, OrderDate:date, Status:varchar, MaterialGrade:varchar, MaterialID:varchar, Name:varchar

## dbo.RM_Shift_Producation_Report
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Size:int, Grade:varchar, Shift:varchar, ProductionTime:time, TimeFrom:time, TimeTo:time, TimeDuration:decimal, DelayCode:varchar, Misroll:varchar, NatureOfDelay:varchar, RootCause:varchar, CorrectiveAction:varchar, Remarks:varchar

## dbo.RM_Shift_Producation_Report_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Size:int, Grade:varchar, Shift:varchar, ProductionTime:time, TimeFrom:time, TimeTo:time, TimeDuration:decimal, DelayCode:varchar, Misroll:varchar, NatureOfDelay:varchar, RootCause:varchar, CorrectiveAction:varchar, Remarks:varchar

## dbo.RM_Stock_And_Parting_Register
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Shift:varchar, Size:decimal, Shear3SampleTopOrBottom:int, Shear3SampleSide:int, FinishedRoundTopOrBottom:int, FinishedRoundSide:int, PinchRollPartingmmPR0:decimal, PinchRollPartingmmPR1:decimal, PinchRollPartingmmPR2:decimal, PinchRollPartingmmPR3:decimal, PinchRollPartingmmPR4:decimal, PinchRollPartingmmRemarks:varchar, BlockStandsPartingmm19:decimal, BlockStandsPartingmm20:decimal, BlockStandsPartingmm21:decimal, BlockStandsPartingmm22:decimal, BlockStandsPartingmm23:decimal, BlockStandsPartingmm24:decimal, BlockStandsPartingmm25:decimal, BlockStandsPartingmm26:decimal, BlockStandsPartingmm27:decimal, BlockStandsPartingmm28:decimal, BlockStandsPartingmmRemarks:varchar

## dbo.RM_Stock_And_Parting_Register_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Shift:varchar, Size:decimal, Shear3SampleTopOrBottom:int, Shear3SampleSide:int, FinishedRoundTopOrBottom:int, FinishedRoundSide:int, PinchRollPartingmmPR0:decimal, PinchRollPartingmmPR1:decimal, PinchRollPartingmmPR2:decimal, PinchRollPartingmmPR3:decimal, PinchRollPartingmmPR4:decimal, PinchRollPartingmmRemarks:varchar, BlockStandsPartingmm19:decimal, BlockStandsPartingmm20:decimal, BlockStandsPartingmm21:decimal, BlockStandsPartingmm22:decimal, BlockStandsPartingmm23:decimal, BlockStandsPartingmm24:decimal, BlockStandsPartingmm25:decimal, BlockStandsPartingmm26:decimal, BlockStandsPartingmm27:decimal, BlockStandsPartingmm28:decimal, BlockStandsPartingmmRemarks:varchar

## dbo.RM_TC_Grinding_Logbook
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:varchar, IsProcessed:bit, CNCOperatorName:varchar, Shift:varchar, RingNo:varchar, GrooveCode:varchar, StdNo:varchar, Section:varchar, RollLoadingDateTime:datetime, JobDescription:varchar, RollDiameterBefore:decimal, RollDiameterAfter:decimal, RollUnloadingDatetime:datetime, PassCondition:varchar, Remarks:varchar, NoOfGrovesGrindingDone:int, TimeTakenForRoughGrinding:time, TimeTakenForFinshGrinding:time, Status:varchar

## dbo.RM_TC_Grinding_Logbook_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, CNCOperatorName:varchar, Shift:varchar, RingNo:int, GrooveCode:int, StdNo:int, Section:varchar, RollLoadingDateTime:datetime, JobDescription:varchar, RollDiameterBefore:int, RollDiameterAfter:int, RollUnloadingDatetime:datetime, PassCondition:varchar, Remarks:varchar, TypeOfWheelDetails:varchar, New:int, Used:int, OperationAtTimeOfBreakageOrDamage:datetime, ReasonForBreakageOrDamage:varchar

## dbo.RM_Tool_Stock_Report
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, TypeOfTool:varchar, QuantityNos:int, Issued:varchar, Balance:int, NewIndentNo:int, IndentDate:date, NewTollsReceivedDate:date, Remarks:varchar, ClosingStock:varchar

## dbo.RM_Tool_Stock_Report_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, TypeOfTool:varchar, QuantityNos:int, Issued:varchar, Balance:int, NewIndentNo:int, IndentDate:date, NewTollsReceivedDate:date, Remarks:varchar, ClosingStock:varchar

## dbo.RM_Trimming_Record
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Shift:varchar, Front:varchar, Back:varchar, Remarks:varchar

## dbo.RM_Trimming_Record_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Shift:varchar, Front:varchar, Back:varchar, Remarks:varchar

## dbo.RM_WRM_Attribute_Tag_Template_Dtl_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Attribute:varchar, HHRange:decimal, HRange:decimal, LRange:decimal, LLRange:decimal, ColorGTHH:varchar, ColorBWHHH:varchar, ColorBWHL:varchar, ColorBWLLL:varchar, ColorLTLL:varchar, DocumentGTHH:varchar, DocumentBWHHH:varchar, DocumentBWHL:varchar, DocumentBWLLL:varchar, DocumentLTLL:varchar, ExtendRetrievalType:varchar, ExtendEquationType:varchar, ExtendEquation:varchar, TransactionRetrievalType:varchar, Procedure:varchar, PWherecolumn:varchar, POperator:varchar, PConditionType:varchar, PMSTAttribute:varchar, PWhereValue:varchar, IType:varchar, TransactionEquationType:varchar, TransactionEquation:varchar

## dbo.RM_WRM_Attribute_Tag_Template_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.RM_WRM_Block
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentID:varchar, StartTime:datetime, EndTime:datetime, ReportDate:date, IsProcessed:bit

## dbo.RM_WRM_Capability_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ReportDate:date, IsProcessed:bit, Description:varchar, IsStart:bit, IsHold:bit, IsRestart:bit, IsAbort:bit, IsReset:bit, IsReady:bit, IsHeld:bit, IsRun:bit, IsDone:bit, IsInterlock:bit, IsAborted:bit, InterlockValueType:varchar, ErrorCodeTag:varchar, ErrorLookUpTable:varchar, ErrorCodeField:varchar, ErrorDescriptionField:varchar
