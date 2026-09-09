---
type: note
subtype: schema-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch schema atlas: X part 2

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

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
