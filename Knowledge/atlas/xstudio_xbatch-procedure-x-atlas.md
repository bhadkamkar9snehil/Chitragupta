---
type: Reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch stored-procedure atlas: X

Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.

## dbo.XBatch_Add_ConditionalFormatting_Numeric_in_Lv_Usp
Safety: MUTATING
Parameters: @LVIDLst:nvarchar(max)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration.dbo.XStudio_GetDataSourceInfoFromSystemId_Fun, XStudio_Configuration_Xbatch.dbo.XStudio_LvColumns_Mst_Tbl

## dbo.XBatch_Add_Default_Heat_start_end_Usp
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration.dbo.XStudio_User_Mst_Tbl, XStudio_Xbatch.dbo.CCM_Per_Heat, XStudio_Xbatch.dbo.EAF_PER_HEAT, XStudio_Xbatch.dbo.Heat_End_Selection_Trn_Tbl, XStudio_Xbatch.dbo.LRF_Per_Heat, XStudio_Xbatch.dbo.SMS_Production_Summary_Day

## dbo.XBatch_Add_Heat_start_end_SPValidation_Usp
Safety: MUTATING
Parameters: @ReportDate:date, @FirstHeat:int, @LastHeat:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Heat_End_Selection_Trn_Tbl

## dbo.XBatch_Add_Heat_start_end_Usp
Safety: MUTATING
Parameters: @ReportDate:date, @FirstHeat:int, @LastHeat:int, @UserID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_Per_Heat, XStudio_Xbatch.dbo.EAF_PER_HEAT, XStudio_Xbatch.dbo.Heat_End_Selection_Trn_Tbl, XStudio_Xbatch.dbo.LRF_Per_Heat, XStudio_Xbatch.dbo.SMS_Production_Summary_Day, XStudio_Xbatch.dbo.SP_SMS_Producation_Summary, XStudio_Xbatch.dbo.XBatch_Recalculate_Summary_CCM_Usp, XStudio_Xbatch.dbo.XBatch_Recalculate_Summary_EAF_Usp, XStudio_Xbatch.dbo.XBatch_Recalculate_Summary_LRF_Usp, XStudio_Xbatch.dbo.XStudio_Historian_Day_SMS_Production_Usp

## dbo.XBatch_AllFurnacePosition_Billet_Deatils
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XBatch_CCM_Heat_Average_SuperHeat
Safety: MUTATING
Parameters: @ID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XBatch_Check_Material_Availibility_And_Connection_Usp
Safety: MUTATING
Parameters: @PhaseID:varchar(36), @MaterialID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XBatch_Create_Batch_Usp
Safety: MUTATING
Parameters: @BatchID:varchar(36)
Referenced objects: none detected

## dbo.XBatch_Create_Connection_Default_Transfer_Capability
Safety: MUTATING
Parameters: @ConnectionID:varchar(36), @UserID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XBatch_Electricity_Bill_Calculator_USP
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Xbatch.dbo.Electricity_Meter_Electricity_Bill_Details, XStudio_Xbatch.dbo.Electricity_Meter_Electricity_Rate_Tbl_Mst, XStudio_Xbatch.dbo.Electricity_Meter_Reading, XStudio_Xbatch.dbo.Electricity_Meter_Timing, XStudio_Xbatch.dbo.Rate_Band_Master, XStudio_Xbatch.dbo.SMS_Electricity_Meter_Bill_Amount_USP

## dbo.XBatch_Electricity_Meter_Consumption_Usp
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.Electricity_Meter_Reading, XStudio_Xbatch.dbo.Electricity_Meter_Reading, XStudio_Xbatch.dbo.Power_Consumption_LogSheet

## dbo.XBatch_Generate_Next_Batch_No_Usp
Safety: MUTATING
Parameters: none
Referenced objects: none detected

## dbo.XBatch_Generate_Recipe_Phase_Parameter_By_Equipment_Type_Usp
Safety: MUTATING
Parameters: @PhaseID:varchar(36), @EquipmentTypeID:varchar(36)
Referenced objects: none detected

## dbo.XBatch_Get_ActivePLCStaus_Usp
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XBatch_Get_All_Tags_Usp
Safety: MUTATING
Parameters: none
Referenced objects: none detected

## dbo.XBatch_Get_Batch_Equipment_Tag_Usp
Safety: MUTATING
Parameters: none
Referenced objects: none detected

## dbo.XBatch_Get_Capability_By_Type_And_Template_Usp
Safety: MUTATING
Parameters: @Type:varchar(10), @EquipmentTypeID:varchar(36), @EquipmentTemplateID:varchar(36)
Referenced objects: none detected

## dbo.XBatch_Get_Entry_for_ShiftDelay_Usp
Safety: MUTATING
Parameters: @heatNo:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.ShiftDelayEntry_Update_usp

## dbo.XBatch_Get_Equipment_Template_Tag_Usp
Safety: MUTATING
Parameters: @EquipmentTypeID:varchar(36), @TemplateID:varchar(36)
Referenced objects: XStudio_XBatch.dbo.Equipment_Type_Mst_Tbl

## dbo.XBatch_Get_Historian_Channels_By_Process_Cell_Usp
Safety: MUTATING
Parameters: @ProcessCellID:varchar(36)
Referenced objects: XStudio_Historian.dbo.XHS_Channel_Mst_Tbl, XStudio_Historian.dbo.XHS_Collector_Mst_Tbl, XStudio_XBatch.dbo.XBatch_Process_Cell_Mst_Tbl

## dbo.XBatch_Get_Historian_Collector_Usp
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Historian.dbo.XHS_Collector_Mst_Tbl

## dbo.XBatch_Get_Historian_Tags_By_Type_DataSource_Usp
Safety: MUTATING
Parameters: @TagType:varchar(100), @DataSourceID:varchar(36)
Referenced objects: XStudio_Historian.dbo.XHS_Channel_Group_Mst_Tbl, XStudio_Historian.dbo.XHS_Tag_Mst_Tbl

## dbo.XBatch_Get_Location_By_Grade_Usp
Safety: MUTATING
Parameters: @Type:varchar(10), @GradeNo:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.XBatch_Get_Location_By_Type_Usp

## dbo.XBatch_Get_Location_By_Type_Usp
Safety: MUTATING
Parameters: @Type:varchar(10), @LocationType:varchar(10)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XBatch_Get_Tag_Mapping_Entries_By_Page_Type_Usp
Safety: MUTATING
Parameters: @PageType:varchar(100), @ID:varchar(36)
Referenced objects: XStudio_Historian.dbo.XHS_Channel_Mst_Tbl, XStudio_XBatch.dbo.Equipment_Type_Mst_Tbl, XStudio_XBatch.dbo.XBatch_Connection_Capability_Mst_Tbl, XStudio_XBatch.dbo.XBatch_Connection_Interlock_Error_Mst_Tbl, XStudio_XBatch.dbo.XBatch_Connection_Parameter_Mst_Tbl

## dbo.XBatch_Get_Template_By_EquipmentType_Usp
Safety: MUTATING
Parameters: @Type:varchar(10), @EquipmentTypeID:varchar(36)
Referenced objects: none detected

## dbo.XBatch_GetRemaningHeat_Usp
Safety: MUTATING
Parameters: @type:bit, @WOID:varchar(max)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.RM_Operator_HeatSelection, Xstudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl

## dbo.Xbatch_HEAT_Tracking
Safety: MUTATING
Parameters: @p_filterCondition:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_Per_Heat, XStudio_Xbatch.dbo.EAF_PER_HEAT, XStudio_Xbatch.dbo.LRF_Per_Heat

## dbo.XBatch_Heatwise_BilletCount_SPvaildation_Usp
Safety: MUTATING
Parameters: @TotalBillet:int, @EnteredBillets:int, @Heatno:varchar(10)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XBatch_I_Customer_USP
Safety: MUTATING
Parameters: @Name:varchar(100), @Address:varchar(1000), @City:varchar(100), @State:varchar(100), @County:varchar(100), @ZipCode:int, @ContactNumber1:varchar(100), @ContactNumber2:varchar(100), @EmailAddress1:varchar(200), @EmailAddress2:varchar(200), @Description:varchar(1000), @userID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Customer_Mst_Tbl

## dbo.XBatch_I_Formula_Details_USP
Safety: MUTATING
Parameters: @FormulaName:varchar(100), @ItemNumber:varchar(100), @Unit:varchar(36), @Quantity:decimal(18,4), @QuantityType:varchar(100), @Description:varchar(max), @Isenabled:bit, @MinQuantity:decimal(18,4), @MaxQuantity:decimal(18,4), @UserID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Formula_Dtl_Tbl, XStudio_Xbatch.dbo.XBatch_Formula_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl

## dbo.XBatch_I_Formula_USP
Safety: MUTATING
Parameters: @Name:varchar(100), @ItemNumber:varchar(100), @Quantity:decimal(18,4), @Unit:varchar(36), @Description:varchar(max), @Isenabled:bit, @UserID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Formula_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl

## dbo.XBatch_I_Material_Consume_NoBOM_USP
Safety: MUTATING
Parameters: @ItemName:varchar(100), @LotNumber:varchar(100), @SublotNumber:varchar(100), @Quantity:decimal(18,4), @UOMName:varchar(100), @Grade:varchar(100), @UserID:varchar(36), @HeatNo:int, @ProduceItem:bit
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Item_Cons_Trn_Tbl

## dbo.XBatch_I_Material_Consume_USP
Safety: MUTATING
Parameters: @BOMID:varchar(36), @ItemName:varchar(100), @LotNumber:varchar(100), @SublotNumber:varchar(100), @Quantity:decimal(18,4), @UOMName:varchar(100), @Grade:varchar(100), @UserID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.XBatch_Batch_BOM_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Item_Cons_Trn_Tbl

## dbo.XBatch_I_Material_Grade_USP
Safety: MUTATING
Parameters: @Name:varchar(100), @Description:varchar(1000), @Color:varchar(50), @IsActive:bit, @userID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Material_Grade_Mst_Tbl

## dbo.XBatch_I_Material_Inventory_Transfer_USP
Safety: MUTATING
Parameters: @Name:varchar(100), @LotNumber:varchar(100), @SublotNumber:varchar(100), @Grade:varchar(100), @Quantity:decimal(18,4), @ToLocationType:varchar(100), @ToLocation:varchar(100), @FromLocationType:varchar(100), @FromLocation:varchar(100), @UserID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Generate_SublotNumber_Fun, XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl

## dbo.XBatch_I_Material_Inventory_USP
Safety: MUTATING
Parameters: @Name:varchar(100), @LotNumber:varchar(100), @SublotNumber:varchar(100), @Grade:varchar(100), @Quantity:decimal(18,4), @UOMName:varchar(200), @LocationType:varchar(100), @Location:varchar(100), @IsExpired:bit, @ExpiryDate:date, @ReceivedDate:datetime, @Vendor:varchar(100), @PONumber:varchar(100), @GRNNumber:varchar(100), @InvoiceNumber:varchar(100), @Price:decimal(18,4), @Description:varchar(1000), @OperationID:varchar(36), @Remark:varchar(1000), @UserID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl

## dbo.XBatch_I_Material_Produce_NoBOM_USP
Safety: MUTATING
Parameters: @HeatNo:int, @ItemName:varchar(100), @LotNumber:varchar(100), @SublotNumber:varchar(100), @Quantity:decimal(18,4), @UOMName:varchar(100), @Grade:varchar(100), @UserID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.XBatch_I_Material_Produce_USP, XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl, XStudio_XBatch.dbo.XBatch_Material_Item_Prod_Trn_Tbl

## dbo.XBatch_I_Material_Produce_USP
Safety: MUTATING
Parameters: @BOMID:varchar(36), @ItemName:varchar(100), @LotNumber:varchar(100), @SublotNumber:varchar(100), @Quantity:decimal(18,4), @UOMName:varchar(100), @Grade:varchar(100), @UserID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl, XStudio_XBatch.dbo.XBatch_Material_Item_Prod_Trn_Tbl

## dbo.XBatch_I_Material_USP
Safety: MUTATING
Parameters: @Name:varchar(100), @Type:varchar(100), @Unit:varchar(100), @Number:varchar(100), @Stocktype:varchar(100), @Quantity:decimal(18,4), @Description:varchar(max), @IsEnabled:bit, @CanExpire:bit, @ExpireDays:int, @MinInventorylevel:decimal(18,4), @MaxOrderSize:decimal(18,4), @LotNumberFormat:varchar(100), @SubLotNumberFormat:varchar(100), @UserID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Type_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl

## dbo.XBatch_I_Measurement_Unit
Safety: MUTATING
Parameters: @Name:varchar(100), @Description:varchar(max), @userID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl

## dbo.XBatch_I_Measurement_Unit_USP
Safety: MUTATING
Parameters: @Name:varchar(100), @Description:varchar(max), @userID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl

## dbo.XBatch_I_Particular_Master_Trn_Usp
Safety: MUTATING
Parameters: @Reportdate:datetime
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XBatch_I_SO_USP
Safety: MUTATING
Parameters: @Name:varchar(100), @customerName:varchar(100), @ItemNumber:varchar(100), @Quantity:decimal(18,4), @Unit:varchar(100), @ReceivedDate:datetime, @ApprovedDate:datetime, @ApprovedBy:varchar(36), @CompletionDate:datetime, @Remarks:varchar(1000), @SalesOrderNumber:varchar(100), @UserID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Customer_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Sales_Order_Mst_Tbl

## dbo.XBatch_I_Storage_Area_USP
Safety: MUTATING
Parameters: @Name:varchar(100), @StorageLocation:varchar(200), @Capacity:decimal(18,4), @CapacityUnit:varchar(100), @Description:varchar(max), @IsEnabled:bit, @UserID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Storage_Area_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Store_Mst_Tbl

## dbo.XBatch_I_Storage_Subarea_USP
Safety: MUTATING
Parameters: @Name:varchar(100), @StorageArea:varchar(200), @Number:int, @IsEnabled:bit, @UserID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Storage_Area_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Storage_Rack_Mst_Tbl

## dbo.XBatch_I_Store_USP
Safety: MUTATING
Parameters: @Name:varchar(100), @Capacity:decimal(18,4), @CapacityUnit:varchar(100), @Description:varchar(max), @IsEnabled:bit, @UserID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Store_Mst_Tbl

## dbo.XBatch_I_WO_USP
Safety: MUTATING
Parameters: @Name:varchar(100), @SONumber:varchar(100), @WoNumber:varchar(100), @SerialNumber:int, @Quantity:decimal(18,4), @Unit:varchar(100), @ItemNumber:varchar(100), @Status:varchar(100), @Description:varchar(1000), @UserID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Sales_Order_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Work_Order_Mst_Tbl

## dbo.Xbatch_LastSevenDay_HEAT_Tracking
Safety: MUTATING
Parameters: @p_filterCondition:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_Per_Heat, XStudio_Xbatch.dbo.EAF_PER_HEAT, XStudio_Xbatch.dbo.LRF_Per_Heat, XStudio_Xbatch.dbo.xbatch_work_order_mst_tbl

## dbo.XBatch_Material_Consumed_Split_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @UserID:varchar(36), @HeatNo:int, @FristLotNumber:varchar(200), @Quantity:decimal(18,2), @MaterialID:varchar(36), @UOMID:varchar(36), @IsMulitLots:bit, @SecondLotNumber:varchar(200), @SecondLotQuantity:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Item_Cons_Trn_Tbl

## dbo.XBatch_Material_Consumed_Split_Validate_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @UserID:varchar(36), @HeatNo:int, @FristLotNumber:varchar(200), @Quantity:decimal(18,2), @MaterialID:varchar(36), @UOMID:varchar(36), @IsMulitLots:bit, @SecondLotNumber:varchar(200), @SecondLotQuantity:decimal(18,2)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XBatch_Material_Lot_Sublot_Validate_Usp
Safety: MUTATING
Parameters: @ID:varchar(100), @LotNumber:varchar(100), @SubLotNumber:varchar(100), @Source:varchar(20), @AvailableQuantity:decimal(18,0), @Quantity:decimal(18,0)
Referenced objects: none detected

## dbo.XBatch_Material_Split_Usp
Safety: MUTATING
Parameters: @SourceItemId:varchar(36), @SplitItemId:varchar(36), @SplitQuantity:decimal(18,4)
Referenced objects: none detected

## dbo.XBatch_Material_Transfer_Usp
Safety: MUTATING
Parameters: @SourceItemId:varchar(36), @TransfereItemId:varchar(36)
Referenced objects: none detected

## dbo.XBatch_MR_Get_Batch_Component_Detail_Usp
Safety: MUTATING
Parameters: @Type:varchar(100), @TypeParentID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Get_Batch_Details

## dbo.XBatch_MR_Get_Batch_Detail_Usp
Safety: MUTATING
Parameters: @BatchID:varchar(36)
Referenced objects: none detected

## dbo.XBatch_MR_Get_Batch_Material_List_Usp
Safety: MUTATING
Parameters: @BatchID:varchar(36)
Referenced objects: none detected

## dbo.XBatch_MR_Get_Phase_Capability_Details_Usp
Safety: MUTATING
Parameters: @PhaseID:varchar(100)
Referenced objects: none detected

## dbo.XBatch_MR_Update_Batch_Component_Status_Usp
Safety: MUTATING
Parameters: @PhaseID:varchar(36), @Status:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Batch_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Batch_Operation_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Batch_Phase_Group_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Batch_Phase_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Batch_Unit_Procedure_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_I_Material_Produce_USP, XStudio_Xbatch.dbo.XBatch_Status_Mst_Tbl

## dbo.XBatch_MR_Update_Batch_Status_Usp
Safety: MUTATING
Parameters: @BatchID:varchar(36), @Status:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Batch_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Process_Cell_Mst_Tbl

## dbo.XBatch_OEE_Dashboard_SP
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.FN_GET_ReportDate, XStudio_Xbatch.dbo.ShiftDelayEntry, XStudio_Xbatch.dbo.SMS_Production_Summary, XStudio_Xbatch.dbo.SMS_Production_Summary_Day

## dbo.XBatch_Particular_Target_Usp
Safety: MUTATING
Parameters: @enddate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Particulars_Masters

## dbo.XBatch_PERDAY_Heat_Summary_Report
Safety: MUTATING
Parameters: @PlantName:varchar(25)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_Mst_Tbl, XStudio_XBatch.dbo.CCM_PER_SHIFT, XStudio_XBatch.dbo.EAF_PER_HEAT, XStudio_Xbatch.dbo.EAF_SMS_Mst_Tbl, Xstudio_Xneo.dbo.LRF_SUMMARY2_Summary_Shift

## dbo.XBATCH_Production_Details_Usp
Safety: MUTATING
Parameters: @StartDate:date, @EndDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.SMS_Production_Summary

## dbo.XBatch_Recalculate_Summary_CCM_Usp
Safety: MUTATING
Parameters: @StartDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_Per_Heat, XStudio_Xbatch.dbo.Xstudio_Summary_CCM_Usp

## dbo.XBatch_Recalculate_Summary_EAF_Usp
Safety: MUTATING
Parameters: @StartDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.EAF_PER_HEAT, XStudio_Xbatch.dbo.Xstudio_Summary_EAF_Usp

## dbo.XBatch_Recalculate_Summary_LRF_Usp
Safety: MUTATING
Parameters: @StartDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.LRF_Per_Heat, XStudio_Xbatch.dbo.Xstudio_Summary_LRF_Usp

## dbo.XBatch_Recipe_Operation_Quantity_Save_Usp
Safety: MUTATING
Parameters: @OperationID:varchar(36), @OutputMaterialID:varchar(36)
Referenced objects: none detected

## dbo.XBatch_Recipe_Validate_BOM_Usp
Safety: MUTATING
Parameters: @MaterialID:varchar(36)
Referenced objects: none detected

## dbo.XBatch_Remove_Unused_Records_Usp
Safety: MUTATING
Parameters: none
Referenced objects: none detected

## dbo.XBatch_Reset_System_Usp
Safety: MUTATING
Parameters: none
Referenced objects: none detected

## dbo.XBatch_RM_Billet_Assign_SPValidation_Usp
Safety: MUTATING
Parameters: @RollingPlanID:varchar(36), @HeatNo:varchar(50), @TotalQty:int, @AssignQty:int, @RequiredQty:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.RM_Rolling_Plan

## dbo.XBatch_RM_Billet_Assign_Usp
Safety: MUTATING
Parameters: @RollingPlanID:varchar(36), @HeatNo:varchar(50), @TotalQty:int, @AssignQty:int, @RequiredQty:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Billet_Inventory, XStudio_Xbatch.dbo.RM_Charging_Plan, XStudio_Xbatch.dbo.RM_Rolling_Plan, XStudio_Xbatch.dbo.XBatch_Formula_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_RM_Billet_Assign_SPValidation_Usp

## dbo.XBatch_RM_BilletInventoryView_Location_U_Usp
Safety: MUTATING
Parameters: @HeatNo:varchar(50), @AssignQty:int, @TotalQty:int, @Location:varchar(500), @Material:varchar(200), @Grade:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Billet_Inventory_View, XStudio_Xbatch.dbo.XBatch_I_Material_Inventory_USP, XStudio_Xbatch.dbo.XBatch_Material_Grade_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Storage_Rack_Mst_Tbl

## dbo.XBatch_RM_BilletInventoryView_SPValidation_Usp
Safety: MUTATING
Parameters: @HeatNo:varchar(50), @AssignQty:int, @TotalQty:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.Xbatch_RM_Billets_In_Furnace_Pivot_Usp
Safety: MUTATING
Parameters: none
Referenced objects: none detected

## dbo.XBatch_RM_BilletWiseNGConsumption
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Historian.dbo.XHS_Tag_Max_Sub_Max_Value_Usp, XStudio_Historian.dbo.XHS_Tag_Mst_Tbl

## dbo.XBatch_RM_ItemsOfMaterial_In_Inventory_BOM_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @IsGroupofSubLot:bit
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Billet_Inventory, XStudio_Xbatch.dbo.RM_Rolling_Plan, XStudio_Xbatch.dbo.RM_Sales_Order, XStudio_Xbatch.dbo.XBatch_Formula_Dtl_Tbl, XStudio_Xbatch.dbo.XBatch_Formula_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Grade_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl

## dbo.XBatch_RM_Mill_Billet_DischargeTemp
Safety: MUTATING
Parameters: @StartDate:datetime, @EndDate:datetime
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Historian.dbo.XHS_Tag_MAX_Value_Usp, XStudio_Historian.dbo.XHS_Tag_Mst_Tbl, XStudio_Xbatch.dbo.Billet_NGConsumption_InFurnace, XStudio_Xbatch.dbo.BilletsPosition_InFurnace

## dbo.XBatch_RM_Rolling_Plan_Approval_Usp
Safety: MUTATING
Parameters: @ID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.RM_Rolling_Plan, XStudio_Xbatch.dbo.Steel_Grade_Master, XStudio_Xbatch.dbo.XBatch_Formula_Dtl_Tbl, XStudio_Xbatch.dbo.XBatch_Formula_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Recipe_Mst_Tbl

## dbo.XBatch_RM_Rolling_Process_SPvaildation_Usp
Safety: MUTATING
Parameters: @SalesOrderNo:varchar(50), @RollingReleaseQty:int, @SequenceNo:int, @RollingDate:datetime, @MaxSeqNo:int, @MaxRollingID:varchar(max), @IsNewRollingId:bit
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.RM_Rolling_Plan, XStudio_Xbatch.dbo.RM_Sales_Order, xstudio_xbatch.dbo.XBatch_RM_Rolling_Process_Usp

## dbo.XBatch_RM_Rolling_Process_Usp
Safety: MUTATING
Parameters: @SalesOrderNo:varchar(50), @RollingReleaseQty:int, @SequenceNo:int, @RollingDate:datetime, @MaxSeqNo:int, @MaxRollingID:varchar(200), @IsNewRollingID:bit
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.RM_Open_Campaign, XStudio_Xbatch.dbo.RM_Rolling_Plan, xstudio_xbatch.dbo.RM_Rolling_Plan, XStudio_Xbatch.dbo.RM_Sales_Order, XStudio_Xbatch.dbo.XBatch_RM_Rolling_Process_SPvaildation_Usp

## dbo.XBatch_RM_SAP_Inventory_Billet_Usp
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Billet_Inventory_View, XStudio_Xbatch.dbo.XBatch_Material_Grade_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl

## dbo.XBatch_Rolling_ID_Changer
Safety: MUTATING
Parameters: @RollingDate:varchar(50)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, xstudio_xbatch.dbo.RM_Rolling_Plan

## dbo.XBatch_SAP_Material_Prod_Cons_Usp
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XBatch_ShiftWise_Heat_Summary
Safety: MUTATING
Parameters: @PlantName:varchar(25)
Referenced objects: Xstudio_Xneo.dbo.CCM_S_Summary_Shift, Xstudio_Xneo.dbo.EAF_S_Summary_Shift, Xstudio_Xneo.dbo.LRF_SUMMARY2_Summary_Shift

## dbo.XBatch_SMS_Heat_Tracking_Daily_Production_Data
Safety: MUTATING
Parameters: @HeatID:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_Xbatch.dbo.XStudio_User_Mst_Tbl

## dbo.XBatch_SMS_MES_Delay_Dashboard_SP
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XBatch_SMS_Production_Details_ForTheDay_Usp
Safety: MUTATING
Parameters: @ReportDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Particulars_Masters

## dbo.Xbatch_SMS_WorkOrder_Wise_Consumption_Usp
Safety: MUTATING
Parameters: none
Referenced objects: none detected

## dbo.XBatch_U_Formula_Details_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @FormulaName:varchar(100), @ItemNumber:varchar(100), @Unit:varchar(36), @Quantity:decimal(18,4), @QuantityType:varchar(100), @Description:varchar(max), @Isenabled:bit, @MinQuantity:decimal(18,4), @MaxQuantity:decimal(18,4), @UserID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Formula_Dtl_Tbl, XStudio_Xbatch.dbo.XBatch_Formula_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl

## dbo.XBatch_U_Formula_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Name:varchar(100), @ItemNumber:varchar(100), @Quantity:decimal(18,4), @Unit:varchar(36), @Description:varchar(max), @Isenabled:bit, @UserID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Formula_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl

## dbo.XBatch_U_Material_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Name:varchar(100), @Type:varchar(100), @Unit:varchar(100), @Number:varchar(100), @Stocktype:varchar(100), @Quantity:decimal(18,4), @Description:varchar(max), @IsEnabled:bit, @CanExpire:bit, @ExpireDays:int, @MinInventorylevel:decimal(18,4), @MaxOrderSize:decimal(18,4), @LotNumberFormat:varchar(100), @SubLotNumberFormat:varchar(100), @UserID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Type_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl

## dbo.XBatch_U_SO_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Name:varchar(100), @customerName:varchar(100), @ItemNumber:varchar(100), @Quantity:decimal(18,4), @Unit:varchar(100), @ReceivedDate:datetime, @ApprovedDate:datetime, @ApprovedBy:varchar(36), @CompletionDate:datetime, @Remarks:varchar(1000), @SalesOrderNumber:varchar(100), @UserID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Customer_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Sales_Order_Mst_Tbl

## dbo.XBatch_U_Storage_Area_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Name:varchar(100), @StorageLocation:varchar(200), @Capacity:decimal(18,4), @CapacityUnit:varchar(100), @Description:varchar(max), @IsEnabled:bit, @UserID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Storage_Area_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Store_Mst_Tbl

## dbo.XBatch_U_Storage_Subarea_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Name:varchar(100), @StorageArea:varchar(200), @Number:int, @IsEnabled:bit, @UserID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Storage_Area_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Storage_Rack_Mst_Tbl

## dbo.XBatch_U_Store_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Name:varchar(100), @Capacity:decimal(18,4), @CapacityUnit:varchar(100), @Description:varchar(max), @IsEnabled:bit, @UserID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Store_Mst_Tbl

## dbo.XBatch_U_WO_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Name:varchar(100), @SONumber:varchar(100), @WoNumber:varchar(100), @SerialNumber:int, @Quantity:decimal(18,4), @Unit:varchar(100), @ItemNumber:varchar(100), @Status:varchar(100), @Description:varchar(1000), @UserID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Sales_Order_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Work_Order_Mst_Tbl

## dbo.XBatch_WO_Create_Batch_AI_Usp
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Recipe_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Work_Order_Mst_Tbl

## dbo.XBatch_WO_Create_Batch_Usp
Safety: MUTATING
Parameters: @BatchList:batchtogenerate, @UserID:varchar(36), @WorkOrderID:varchar(36)
Referenced objects: XStudio_Xbatch.dbo.BatchToGenerate, XStudio_Xbatch.dbo.XBatch_Create_Batch_Usp

## dbo.XBatch_WO_Get_Process_Cell_Scheduled_Batch_Usp
Safety: MUTATING
Parameters: @ProcessCellID:varchar(36)
Referenced objects: none detected

## dbo.XBatch_WO_Get_Process_Cell_Usp
Safety: MUTATING
Parameters: @WorkOrderID:varchar(36)
Referenced objects: none detected

## dbo.XMES_AUTO_WO_AND_SO_CALCULATION
Safety: MUTATING
Parameters: @Plant:varchar(300), @WorkOrder:varchar(36)
Referenced objects: none detected

## dbo.XMES_AUTO_WO_AND_SO_CALCULATION_old
Safety: MUTATING
Parameters: @Plant:varchar(300), @WorkOrder:varchar(36)
Referenced objects: none detected

## dbo.XMES_BackCalculation_GLS_Usp
Safety: MUTATING
Parameters: @HeatNo:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.SP_Xbatch_SplitsBillets_From_CCM_To_Inventory, XStudio_Xbatch.dbo.Xbatch_BackCalculation_LM_USP

## dbo.XMES_BackCalculation_Validation_GLS_Usp
Safety: MUTATING
Parameters: @HeatNo:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.SP_Xbatch_SplitsBillets_From_CCM_To_Inventory

## dbo.XMES_BilletPosting_Validation_Usp
Safety: MUTATING
Parameters: @TotalBilletCount:int, @RemainingBilletCount:int, @HotBilletCount:int, @ColdBilletCount:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XMES_CampaignId_generation_usp
Safety: MUTATING
Parameters: none
Referenced objects: none detected

## dbo.XMES_CREATE_BILLETNO_USP
Safety: MUTATING
Parameters: @EventID:varchar(36)
Referenced objects: none detected

## dbo.XMES_Dashboard_CCM_Live_USP
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Xbatch.dbo.CCM_Data, XSTUDIO_XBATCH.dbo.EAF_SMS_Data

## dbo.XMES_Dashboard_EAF_Live_USP
Safety: MUTATING
Parameters: none
Referenced objects: xstudio_xbatch.dbo.CCM_Data, xstudio_xbatch.dbo.eaf_sms_data, Xstudio_Xbatch.dbo.FN_GET_ReportDate, xstudio_xbatch.dbo.ShiftDelayEntry

## dbo.XMES_Dashboard_LRF_Live_USP
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_XBatch.dbo.EAF_SMS_Data, XStudio_XBatch.dbo.LRF_Per_Heat, XStudio_XBatch.dbo.LRF_SMS_Data, XStudio_XBatch.dbo.Per_Heat_LadleNo

## dbo.XMES_Delay_Split_Entry_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @SplitDT:varchar(20), @Userid:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XMES_Delay_Split_Validate_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @SplitDT:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XMES_DisplayCampaignPlanDetails_usp
Safety: MUTATING
Parameters: none
Referenced objects: none detected

## dbo.XMES_Duplicate_Grade_Protocol_Mst_Usp
Safety: MUTATING
Parameters: @GradeID:varchar(36), @SectionID:varchar(36), @ID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.XMES_Grade_Protocol_CCM_Parameters_Mst_Tbl, XStudio_Xbatch.dbo.XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl, XStudio_Xbatch.dbo.XMES_Grade_Protocol_LRF_Parameters_Mst_Tbl, XStudio_Xbatch.dbo.XMES_Grade_Protocol_Super_Heat_Speed_Nozzle_Mst_Tbl, XStudio_Xbatch.dbo.XMES_Grade_Protocol_Tapping_Additions_Mst_Tbl, XStudio_Xbatch.dbo.XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl, XStudio_Xbatch.dbo.XMES_SMS_Grade_Protocol_Mst_Tbl, XStudio_Xbatch.dbo.XMES_SMS_Grade_Protocol_Mst_tbl

## dbo.XMES_Electricity_Bill_Calculator_USP
Safety: MUTATING
Parameters: @EntryDAte:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Electricity_Meter_Bill_Amount, XStudio_Xbatch.dbo.Electricity_Meter_Electricity_Bill_Details, XStudio_Xbatch.dbo.Electricity_Meter_Electricity_Rate_Tbl_Mst

## dbo.XMES_entry_for_RAW_Material_Consumption_Usp
Safety: MUTATING
Parameters: @ReportDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.EAF_PER_HEAT, XStudio_Xbatch.dbo.MES_Raw_Material_Consumptions_Mapping_Mst_Tbl, XStudio_Xbatch.dbo.MES_Raw_Material_Consumptions_Trn_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Item_Cons_Trn_Tbl, XStudio_Xbatch.dbo.XBatch_Work_Order_Mst_Tbl

## dbo.XMES_Get_API_Transaction_Summary
Safety: READ_ONLY_REVIEWED
Parameters: @APIType:varchar(300)
Referenced objects: XStudio_Configuration_Xbatch.dbo.XStudio_API_Error_Log_Mst_Tbl, XStudio_Configuration_Xbatch.dbo.XStudio_Entities_Mst_Tbl, XStudio_Configuration_Xbatch.dbo.XStudio_LV_Mst_Tbl, xstudio_configuration_xbatch.dbo.xstudio_user_mst_tbl

## dbo.XMES_heat_selection_usp
Safety: MUTATING
Parameters: none
Referenced objects: none detected

## dbo.XMES_I_API_Transaction_Summary
Safety: MUTATING
Parameters: @transactionid:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_Xbatch.dbo.XStudio_API_Error_Log_Mst_Tbl, XStudio_Configuration_Xbatch.dbo.XStudio_Entities_Mst_Tbl, XStudio_Configuration_Xbatch.dbo.XStudio_LV_Mst_Tbl, XStudio_Configuration_Xbatch.dbo.XStudio_User_Mst_Tbl, xstudio_configuration_xbatch.dbo.xstudio_user_mst_tbl, XStudio_Xbatch.dbo.Heat_Chemistry_Quality_Data, XStudio_Xbatch.dbo.MES_SAP_By_Product_Trn_Tbl, XStudio_Xbatch.dbo.MES_SAP_Consumption_Trn_Tbl, XStudio_Xbatch.dbo.MES_SAP_Production_Trn_Tbl, XStudio_Xbatch.dbo.MES_SAP_UsageDecision_Trn_Tbl, Xstudio_Xbatch.dbo.MES_SAP_UsageDecision_Trn_Tbl, XStudio_Xbatch.dbo.XMES_API_Transaction_Summary_Fact_Tbl, XStudio_Xbatch.dbo.XMES_Log_trn_Tbl, XStudio_Xbatch.dbo.XMES_SAP_CreateBatch_Mst_Tbl, XStudio_Xbatch.dbo.XMES_SAP_PlantToPlantTransfer_Trn_Tbl

## dbo.XMES_I_Billets_Tracking_Usp
Safety: MUTATING
Parameters: @HeatNo:int
Referenced objects: master.dbo.spt_values, XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_Per_Heat, XStudio_XBatch.dbo.XBatch_Material_Item_Prod_Trn_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Work_Order_Mst_Tbl, XStudio_Xbatch.dbo.XMES_Billet_Tracking_Trn_tbl, XStudio_Xbatch.dbo.xmes_stage_position_mapping_mst_tbl, XStudio_Xbatch.dbo.xmes_state_position_State_mst_tbl

## dbo.XMES_I_ByProduct_Trn_Usp
Safety: MUTATING
Parameters: @heatno:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.CCM_Per_Heat, XStudio_Xbatch.dbo.MES_SAP_By_Product_Trn_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl

## dbo.XMES_I_Grade_Protocol_Chemistry_USP
Safety: MUTATING
Parameters: @ChemistryID:varchar(36)
Referenced objects: none detected

## dbo.XMES_I_Particulars_for_BestData_Usp
Safety: MUTATING
Parameters: @bestdaydate:date, @bestMonthDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Particulars_Masters, XStudio_Xbatch.dbo.SMS_Production_BestDay_BestMonth_Data, XStudio_Xbatch.dbo.SMS_Production_Summary

## dbo.XMES_I_PlantToPlantTransfer_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @ToPlant:varchar(100), @ToStorageLocation:varchar(200), @quantityinCount:int, @quantityInentryUnit:decimal(18,3)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_Per_heat, XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_tbl, XStudio_Xbatch.dbo.XBatch_Work_Order_Mst_tbl, XStudio_Xbatch.dbo.XMES_SAP_PlantToPlantTransfer_Trn_Tbl

## dbo.XMES_I_SAP_Billet_Production_Trn
Safety: MUTATING
Parameters: @UserId:varchar(36), @SystemId:varchar(36), @RecordIds:varchar(36), @Status:varchar(36), @DataCollection:nvarchar(max)
Referenced objects: master.dbo.spt_values, XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_Per_Heat, XStudio_Xbatch.dbo.ccm_per_heat, XStudio_Xbatch.dbo.Heat_Chemistry_Quality_Data, XStudio_Xbatch.dbo.LRF_Per_Heat, XStudio_Xbatch.dbo.MES_SAP_Consumption_Trn_Tbl, XStudio_Xbatch.dbo.MES_SAP_Production_Trn_Tbl, XStudio_Xbatch.dbo.XBATCH_Material_Grade_mst_tbl, XStudio_Xbatch.dbo.Xbatch_material_grade_mst_tbl, XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Inventory_mst_tbl, XStudio_XBatch.dbo.XBatch_Material_Item_Prod_Trn_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_material_mst_tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Work_Order_Mst_Tbl, XStudio_Xbatch.dbo.XMES_Billet_Tracking_Trn_tbl, XStudio_Xbatch.dbo.XMES_Billet_tracking_trn_tbl, XStudio_Xbatch.dbo.XMES_I_ByProduct_Trn_Usp, XStudio_Xbatch.dbo.XMES_SAP_Batch_Characteristic_Trn_Tbl, XStudio_Xbatch.dbo.XMES_SAP_PlantToPlantTransfer_Trn_Tbl, XStudio_Xbatch.dbo.xmes_stage_position_mapping_mst_tbl, XStudio_Xbatch.dbo.xmes_state_position_State_mst_tbl

## dbo.XMES_I_SAP_GLS_LS_Consumption_Trn_Usp
Safety: MUTATING
Parameters: @HeatNo:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.MES_SAP_Consumption_Trn_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Work_Order_Mst_Tbl

## dbo.XMES_I_SAP_GLS_LS_Production_Trn_Usp
Safety: MUTATING
Parameters: @HeatNo:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.EAF_PER_HEAT, XStudio_Xbatch.dbo.Heat_Chemistry_Quality_Data, XStudio_Xbatch.dbo.LRF_Per_Heat, XStudio_Xbatch.dbo.MES_SAP_Consumption_Trn_Tbl, XStudio_Xbatch.dbo.MES_SAP_Production_Trn_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Work_Order_Mst_Tbl

## dbo.XMES_I_SAP_GLS_Production_Trn
Safety: MUTATING
Parameters: @UserId:varchar(36), @SystemId:varchar(36), @RecordIds:varchar(36), @Status:varchar(36), @DataCollection:nvarchar(max)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.LRF_Per_Heat, XStudio_Xbatch.dbo.MES_SAP_Production_Trn_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Work_Order_Mst_Tbl

## dbo.XMES_I_SAP_LS_Production_Trn
Safety: MUTATING
Parameters: @UserId:varchar(36), @SystemId:varchar(36), @RecordIds:varchar(36), @Status:varchar(36), @DataCollection:nvarchar(max)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.EAF_Per_Heat, XStudio_Xbatch.dbo.MES_SAP_Production_Trn_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Work_Order_Mst_Tbl

## dbo.XMES_LRF_I_Raw_Material_Cons_Usp
Safety: MUTATING
Parameters: @HeatNo:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_Xbatch.dbo.XStudio_Attribute_mst_tbl, XStudio_configuration_Xbatch.dbo.XStudio_Entities_Mst_tbl, XStudio_Xbatch.dbo.MES_Raw_Material_Consumptions_Mapping_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Item_Cons_Trn_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Item_Cons_Trn_tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl

## dbo.XMES_MaterialProcess_Cursor_usp
Safety: MUTATING
Parameters: @Campaignid:varchar(max)
Referenced objects: none detected

## dbo.XMES_Missing_Heat_Entry_USP
Safety: MUTATING
Parameters: @HEATID:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, xstudio_Xbatch.dbo.xbatch_work_order_mst_tbl

## dbo.XMES_Power_Consumption_Report_Per_Ton_Data_Usp
Safety: MUTATING
Parameters: @EntryDateTime:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XMES_Power_Consumption_report_Usp
Safety: MUTATING
Parameters: @EntryDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_Summary_Day, XStudio_Xbatch.dbo.Power_Consumption_LogSheet, XStudio_Xbatch.dbo.Power_Consumption_Report, XStudio_Xbatch.dbo.RM_Consumption_Summary_Day

## dbo.XMES_Raw_Material_cons_status_count_usp
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XMES_Recalculate_BackCalculation_GLS_Usp
Safety: MUTATING
Parameters: @HeatReportdate:date, @FromHeat:int, @ToHeat:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.LRF_PER_HEAT, XStudio_Xbatch.dbo.XMES_BackCalculation_GLS_Usp

## dbo.XMES_Recalculate_HEAT_CHEMISTRY_DEVIATION_Usp
Safety: MUTATING
Parameters: @Reportdate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Chemistry_Deviation_Quality_Data, XStudio_Xbatch.dbo.Heat_Chemistry_Quality_Data, XStudio_Xbatch.dbo.XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl

## dbo.XMES_Recalculate_heat_Usp
Safety: MUTATING
Parameters: @id:varchar(36), @type:varchar(5)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration.dbo.XStudio_Schedule_TSQL_Task_Usp, XStudio_Configuration.dbo.XStudio_System_mst_tbl, XStudio_Xbatch.dbo.CCM_PER_HEAT, XStudio_Xbatch.dbo.EAF_PER_HEAT, XStudio_Xbatch.dbo.HeatChargeMixConsumption, XStudio_Xbatch.dbo.LRF_PER_HEAT, XStudio_Xbatch.dbo.XMES_LRF_I_Raw_Material_Cons_Usp, XStudio_Xbatch.dbo.XMES_Recalculate_SMS_PRODUCTION_USP

## dbo.XMES_Recalculate_Power_Consumption_USP
Safety: MUTATING
Parameters: @StartDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.XMES_Power_Consumption_report_Usp

## dbo.XMES_Recalculate_SMS_PRODUCTION_USP
Safety: MUTATING
Parameters: @StartDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.SP_SMS_Producation_Summary

## dbo.XMES_RESET_BILLET_SEQUENCE_USP
Safety: MUTATING
Parameters: none
Referenced objects: none detected

## dbo.XMES_RM_Campaign_Plan_WorkOrders_Creation
Safety: MUTATING
Parameters: @CampaignMasterid:varchar(max)
Referenced objects: none detected

## dbo.XMES_SAP_Batch_Characteristics_API_Error_Usp
Safety: MUTATING
Parameters: @RecordID:varchar(36), @TransactionID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_Xbatch.dbo.XStudio_API_Error_Log_Mst_Tbl, XStudio_Xbatch.dbo.XMES_Log_trn_Tbl

## dbo.XMES_SAP_Batch_Creation_API_Error_Usp
Safety: MUTATING
Parameters: @RecordID:varchar(36), @TransactionID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_Xbatch.dbo.XStudio_API_Error_Log_Mst_Tbl, XStudio_Xbatch.dbo.XMES_Log_trn_Tbl

## dbo.XMES_SAP_Create_Process_Order_Usp
Safety: MUTATING
Parameters: @Type:varchar(100)
Referenced objects: none detected

## dbo.XMES_SAP_GoodsMovements_API_Error_Usp
Safety: MUTATING
Parameters: @RecordID:varchar(36), @TransactionID:varchar(36), @APIPostingType:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_Xbatch.dbo.XStudio_API_Error_Log_Mst_Tbl, XStudio_Xbatch.dbo.MES_SAP_Consumption_Trn_Tbl, XStudio_Xbatch.dbo.MES_SAP_Production_Trn_Tbl, XStudio_Xbatch.dbo.XMES_Log_trn_Tbl, XStudio_Xbatch.dbo.XMES_SAP_PlantToPlantTransfer_Trn_Tbl

## dbo.XMES_SAP_I_Inventory_Stock_Data_Usp
Safety: MUTATING
Parameters: @Type:varchar(200), @Plant:int, @Storage:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.MES_SAP_Inventory_Stock_Data_Tbl, XStudio_Xbatch.dbo.MES_SAP_Inventory_Stock_Tbl

## dbo.XMES_SAP_Inventory_API_Error_Usp
Safety: MUTATING
Parameters: @TransactionID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_Xbatch.dbo.XStudio_API_Error_Log_Mst_Tbl

## dbo.XMES_SAP_PlantToPlantTransfer_API_Error_Usp
Safety: MUTATING
Parameters: @RecordID:varchar(36), @TransactionID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_Xbatch.dbo.XStudio_API_Error_Log_Mst_Tbl, XStudio_Xbatch.dbo.XMES_Log_TRN_tbl, XStudio_Xbatch.dbo.XMES_SAP_PlantToPlantTransfer_Trn_Tbl

## dbo.XMES_SAP_Posting_Sequence_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @APIPostingType:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_Xbatch.dbo.XStudio_API_Error_Log_Mst_Tbl, XStudio_Xbatch.dbo.Heat_Chemistry_Quality_Data, XStudio_Xbatch.dbo.MES_Raw_Material_Consumptions_Trn_Tbl, XStudio_Xbatch.dbo.MES_SAP_By_Product_Trn_Tbl, XStudio_Xbatch.dbo.MES_SAP_Consumption_Trn_Tbl, XStudio_Xbatch.dbo.MES_SAP_Production_Trn_Tbl, XStudio_Xbatch.dbo.MES_SAP_UsageDecision_Trn_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Inventory_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl, XStudio_Xbatch.dbo.XMES_Billet_Tracking_Trn_Tbl, XStudio_Xbatch.dbo.XMES_Log_trn_Tbl, XStudio_Xbatch.dbo.XMES_SAP_Batch_Characteristic_Trn_Tbl, XStudio_Xbatch.dbo.XMES_SAP_CreateBatch_Mst_Tbl, XStudio_Xbatch.dbo.XMES_SAP_PlantToPlantTransfer_Trn_Tbl

## dbo.XMES_SAP_ResultRecording_API_Error_Usp
Safety: MUTATING
Parameters: @RecordID:varchar(36), @TransactionID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_Xbatch.dbo.XStudio_API_Error_Log_Mst_Tbl, XStudio_Xbatch.dbo.XMES_Log_TRN_tbl

## dbo.XMES_SAP_Usage_Decision_API_Error_Usp
Safety: MUTATING
Parameters: @RecordID:varchar(36), @TransactionID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_Xbatch.dbo.XStudio_API_Error_Log_Mst_Tbl, XStudio_Xbatch.dbo.MES_SAP_UsageDecision_Trn_Tbl, XStudio_Xbatch.dbo.XMES_Log_TRN_tbl

## dbo.XMES_SAP_WorkOrder_Creation_API_Error_Usp
Safety: MUTATING
Parameters: @RecordID:varchar(36), @TransactionID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_Xbatch.dbo.XStudio_API_Error_Log_Mst_Tbl

## dbo.XMES_Schedule_SP_to_Refresh_Data_Usp
Safety: MUTATING
Parameters: @ID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration.dbo.XStudio_Schedule_TSQL_Task_Usp, XStudio_Configuration.dbo.XStudio_System_mst_tbl

## dbo.XMES_SMS_Dashboard_Delay_USP
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Xbatch.dbo.eaf_per_heat, XStudio_Xbatch.dbo.ShiftDelayEntry, XStudio_Xbatch.dbo.SMS_Plant_Process_EventTime, XStudio_Xbatch.dbo.SMS_Production_Summary, XStudio_Xbatch.dbo.XStudio_List_CCM_Per_Heat_vw, XStudio_Xbatch.dbo.XStudio_List_ShiftDelayEntry_Vw, XStudio_Xbatch.dbo.XStudio_List_ShiftDelayEntry_vw, XStudio_Xbatch.dbo.XStudio_List_SMS_Plant_Process_EventTime_vw

## dbo.XMES_SO_Trn_VW
Safety: MUTATING
Parameters: none
Referenced objects: none detected

## dbo.XMES_SP_HEAT_CHEMISTRY_DEVIATION
Safety: MUTATING
Parameters: @SYSTEMID:varchar(36), @USERID:varchar(36), @RECORDID:varchar(36), @STATUS:varchar(50)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Chemistry_Deviation_Quality_Data, XStudio_Xbatch.dbo.Heat_Chemistry_Quality_Data, XStudio_Xbatch.dbo.XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl

## dbo.XMES_SP_HEAT_CHEMISTRY_REPORT_DATA
Safety: MUTATING
Parameters: @ReportDate:date
Referenced objects: XStudio_Xbatch.dbo.Heat_Chemistry_Quality_Data, XStudio_Xbatch.dbo.XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl, XStudio_Xbatch.dbo.XMES_SMS_Grade_Protocol_Mst_Tbl

## dbo.XMES_SPValidation_Inv_BLT_Qty_Usp
Safety: MUTATING
Parameters: @CurrentCount:int, @EnteredCount:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XMES_U_Heat_Chemistry_status_Usp
Safety: MUTATING
Parameters: @recordID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.XMES_

## dbo.XMES_U_Power_consumption_Report_Usp
Safety: MUTATING
Parameters: @recordid:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_Summary_Day, XStudio_Xbatch.dbo.Power_Consumption_LogSheet, XStudio_Xbatch.dbo.Power_Consumption_Report, XStudio_Xbatch.dbo.RM_Consumption_Summary_Day

## dbo.XMES_U_SAP_Billet_Posting_Count_Usp
Safety: MUTATING
Parameters: @ProductionID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XMES_U_SAP_Billet_Production_Trn_Usp
Safety: MUTATING
Parameters: @ProductionID:varchar(36)
Referenced objects: master.dbo.spt_values, XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_Per_Heat, XStudio_Xbatch.dbo.MES_SAP_Production_Trn_Tbl, XStudio_Xbatch.dbo.XBATCH_Material_Grade_mst_tbl, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Work_Order_Mst_Tbl, XStudio_Xbatch.dbo.XMES_Billet_Tracking_Trn_Tbl, XStudio_Xbatch.dbo.XMES_Billet_tracking_trn_tbl, XStudio_Xbatch.dbo.xmes_stage_position_mapping_mst_tbl, XStudio_Xbatch.dbo.xmes_state_position_State_mst_tbl

## dbo.XMES_U_SMS_Production_Summary_BestData_Usp
Safety: MUTATING
Parameters: @BestDayDate:date, @BestMonthDate:date, @Particular:varchar(max)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.SMS_Production_BestDay_BestMonth_Data, XStudio_Xbatch.dbo.SMS_Production_Summary, XStudio_Xbatch.dbo.SMS_Production_summary

## dbo.XMES_Water_Reading_Recalculate_Usp
Safety: MUTATING
Parameters: @Reportdate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XMES_Water_Reading_Usp
Safety: MUTATING
Parameters: @ID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.MES_Logbook_Water_Reading

## dbo.XMES_WO_Trn_VW
Safety: MUTATING
Parameters: none
Referenced objects: none detected

## dbo.XMES_WorkOrders_Creation
Safety: MUTATING
Parameters: @CampaignID:varchar(max), @StartDate:datetime, @EndDate:datetime
Referenced objects: none detected

## dbo.Xstudio_Agency_Wise_Delay_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Agency_Wise_Delay

## dbo.Xstudio_Billet_NGConsumption_InFurnace_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Billet_NGConsumption_InFurnace

## dbo.Xstudio_Billets_InFurnace_Tracking_Trn_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Billets_InFurnace_Tracking_Trn

## dbo.Xstudio_CCM_Data_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_Data

## dbo.Xstudio_CCM_Manual_Entry_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_Manual_Entry

## dbo.Xstudio_CCM_Per_Heat_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_Per_Heat

## dbo.Xstudio_CCM_Section_Strands_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_Section_Strands

## dbo.Xstudio_CCM_SMS_Data_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_SMS_Data

## dbo.Xstudio_CCM_Summary_Shift_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_Summary_Shift

## dbo.Xstudio_Day_CCM_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @DatabaseName:varchar(200), @EntityName:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.CCM_Per_Heat, XStudio_XBatch.dbo.CCM_Summary_Day, XStudio_XBatch.dbo.XStudio_Update_Day_CCM_Usp

## dbo.Xstudio_Day_Consumptions_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @DatabaseName:varchar(200), @EntityName:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.Consumptions_Summary_Day, XStudio_XBatch.dbo.Power_Consumption_LogSheet, XStudio_XBatch.dbo.XStudio_Update_Day_Consumptions_Usp

## dbo.Xstudio_Day_EAF_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @DatabaseName:varchar(200), @EntityName:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.EAF_PER_HEAT, XStudio_XBatch.dbo.EAF_Summary_Day, XStudio_XBatch.dbo.XStudio_Update_Day_EAF_Usp

## dbo.Xstudio_Day_LRF_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @DatabaseName:varchar(200), @EntityName:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.LRF_PER_HEAT, XStudio_XBatch.dbo.LRF_Per_Heat, XStudio_XBatch.dbo.LRF_Summary_Day, XStudio_XBatch.dbo.XStudio_Update_Day_LRF_Usp

## dbo.Xstudio_Day_RM_Consumption_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @DatabaseName:varchar(200), @EntityName:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.RM_Consumption_Summary_Day, XStudio_XBatch.dbo.RM_NGConsumption, XStudio_XBatch.dbo.XStudio_Update_Day_RM_Consumption_Usp

## dbo.Xstudio_EAF_LogSheet_Quantity_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.EAF_LogSheet_Quantity

## dbo.Xstudio_EAF_PER_HEAT_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.EAF_PER_HEAT

## dbo.Xstudio_EAF_ProcessTime_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.EAF_ProcessTime

## dbo.Xstudio_EAF_SMS_Data_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.EAF_SMS_Data

## dbo.Xstudio_EAF_Transformer_Reactor_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.EAF_Transformer_Reactor, Xstudio_Xbatch.dbo.FN_Get_ShiftName

## dbo.Xstudio_EAF_Transformer_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.EAF_Transformer, Xstudio_Xbatch.dbo.FN_Get_ShiftName

## dbo.Xstudio_Electricity_Meter_Bill_Amount_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Electricity_Meter_Bill_Amount

## dbo.Xstudio_Electricity_Meter_Reading_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Electricity_Meter_Reading

## dbo.XStudio_Get_SMS_Monthly_Production_Summary
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.Xstudio_Heat_Chemistry_Quality_Data_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_xbatch.dbo.ccm_per_heat, XStudio_Xbatch.dbo.Heat_Chemistry_Quality_Data

## dbo.Xstudio_Heat_End_Selection_Trn_Tbl_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Heat_End_Selection_Trn_Tbl

## dbo.Xstudio_Highest_Production_Entry_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Highest_Production_Entry

## dbo.Xstudio_Historian_CCM_SMS_Block_usp
Safety: MUTATING
Parameters: @StartTime:datetime, @EndTime:datetime, @Attribute:varchar(50), @Equipment:varchar(36), @CollectorID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration.dbo.XStudio_Summary_Entity_Historian_Schedule_Task_Usp, XStudio_Configuration_XBatch.dbo.XStudio_Block_Databases_Mst_Tbl, XStudio_Configuration_XBatch.dbo.XStudio_Block_Entities_Mst_Tbl, XStudio_Historian.dbo.XHS_Channel_Group_Mst_Tbl, XStudio_Historian.dbo.XHS_Channel_Mst_Tbl, XStudio_Historian.dbo.XHS_Collector_Mst_Tbl, XStudio_Historian.dbo.XHS_Tag_AVG_Value_Usp, XStudio_Historian.dbo.XHS_Tag_KPI_SMS_Heat_Count_Usp, XStudio_Historian.dbo.XHS_Tag_MAX_Value_Usp, XStudio_Historian.dbo.XHS_Tag_Mst_Tbl, Xstudio_Xbatch.dbo.Billet_Cross_Section, Xstudio_Xbatch.dbo.BilletsCastCount, XStudio_XBatch.dbo.CCM_SMS_MST_TBL, XStudio_XBatch.dbo.CCM_SMS_Tag_Mapping_Tbl

## dbo.XStudio_Historian_Day_SMS_Production_Usp
Safety: MUTATING
Parameters: @Entrydate:datetime, @DatabaseName:varchar(200), @EntityName:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_XBatch.dbo.XStudio_Block_Entities_Mst_Tbl, XStudio_XBatch.dbo.CCM_SMS_MST_TBL, XStudio_XBatch.dbo.SMS_Production_Summary_Day, XStudio_XBatch.dbo.XStudio_Update_Day_SMS_Production_Usp

## dbo.Xstudio_Historian_EAF_PER_HEAT_usp
Safety: MUTATING
Parameters: @CDateTime:datetime, @Type:varchar(50), @Attribute:varchar(50), @Equipment:varchar(36), @CollectorID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration.dbo.XStudio_Summary_Entity_Historian_Schedule_Task_Usp, XStudio_Configuration_XBatch.dbo.XStudio_Block_Databases_Mst_Tbl, XStudio_Configuration_XBatch.dbo.XStudio_Block_Entities_Mst_Tbl

## dbo.Xstudio_Historian_EAF_SMS_Block_usp
Safety: MUTATING
Parameters: @CDateTime:datetime, @Type:varchar(50), @Attribute:varchar(50), @Equipment:varchar(36), @CollectorID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration.dbo.XStudio_Summary_Entity_Historian_Schedule_Task_Usp, XStudio_Configuration_XBatch.dbo.XStudio_Block_Databases_Mst_Tbl, XStudio_Configuration_XBatch.dbo.XStudio_Block_Entities_Mst_Tbl, XStudio_Historian.dbo.XHS_Channel_Group_Mst_Tbl, XStudio_Historian.dbo.XHS_Channel_Mst_Tbl, XStudio_Historian.dbo.XHS_Collector_Mst_Tbl, XStudio_Historian.dbo.XHS_Tag_First_Value_Usp, XStudio_Historian.dbo.XHS_Tag_MAX_Sub_MAX_Value_Usp, XStudio_Historian.dbo.XHS_Tag_MAX_Value_Usp, XStudio_Historian.dbo.XHS_Tag_Mst_Tbl, XStudio_XBatch.dbo.EAF_SMS_MST_TBL, XStudio_XBatch.dbo.EAF_SMS_Tag_Mapping_Tbl

## dbo.Xstudio_Historian_LRF_SMS_Block_usp
Safety: MUTATING
Parameters: @StartTime:datetime, @EndTime:datetime, @Attribute:varchar(50), @Equipment:varchar(36), @CollectorID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration.dbo.XStudio_Summary_Entity_Historian_Schedule_Task_Usp, XStudio_Configuration_XBatch.dbo.XStudio_Block_Databases_Mst_Tbl, XStudio_Configuration_XBatch.dbo.XStudio_Block_Entities_Mst_Tbl, XStudio_Historian.dbo.XHS_Channel_Group_Mst_Tbl, XStudio_Historian.dbo.XHS_Channel_Mst_Tbl, XStudio_Historian.dbo.XHS_Collector_Mst_Tbl, XStudio_Historian.dbo.XHS_Tag_AVG_Value_Usp, XStudio_Historian.dbo.XHS_Tag_MAX_Value_Usp, XStudio_Historian.dbo.XHS_Tag_Mst_Tbl, XStudio_Historian.dbo.XHS_Tag_SUM_Value_Usp, XStudio_XBatch.dbo.LRF_SMS_MST_TBL, XStudio_XBatch.dbo.LRF_SMS_Tag_Mapping_Tbl

## dbo.Xstudio_Historian_Per_Billet_PVT_RM_Block_USP
Safety: MUTATING
Parameters: @ReportDate:date
Referenced objects: XStudio_Configuration_XBatch.dbo.XStudio_Block_Databases_Mst_Tbl, XStudio_Configuration_XBatch.dbo.XStudio_Block_Entities_Mst_Tbl

## dbo.Xstudio_Historian_RM_Furnace_Logbook_Block_usp
Safety: MUTATING
Parameters: @StartTime:datetime, @EndTime:datetime, @Attribute:varchar(50), @Equipment:varchar(36), @CollectorID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration.dbo.XStudio_Summary_Entity_Historian_Schedule_Task_Usp, XStudio_Configuration_XBatch.dbo.XStudio_Block_Databases_Mst_Tbl, XStudio_Configuration_XBatch.dbo.XStudio_Block_Entities_Mst_Tbl, XStudio_Historian.dbo.XHS_Channel_Group_Mst_Tbl, XStudio_Historian.dbo.XHS_Channel_Mst_Tbl, XStudio_Historian.dbo.XHS_Collector_Mst_Tbl, XStudio_Historian.dbo.XHS_Tag_Last_Value_Usp, XStudio_Historian.dbo.XHS_Tag_Mst_Tbl, XStudio_XBatch.dbo.RM_Reheating_Furnace_MST_TBL, XStudio_XBatch.dbo.RM_Reheating_Furnace_Tag_Mapping_Tbl

## dbo.Xstudio_Historian_RM_Mill_Block_usp
Safety: MUTATING
Parameters: @StartTime:datetime, @EndTime:datetime, @Attribute:varchar(50), @Equipment:varchar(36), @CollectorID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration.dbo.XStudio_Summary_Entity_Historian_Schedule_Task_Usp, XStudio_Configuration_XBatch.dbo.XStudio_Block_Databases_Mst_Tbl, XStudio_Configuration_XBatch.dbo.XStudio_Block_Entities_Mst_Tbl, XStudio_Historian.dbo.XHS_Channel_Group_Mst_Tbl, XStudio_Historian.dbo.XHS_Channel_Mst_Tbl, XStudio_Historian.dbo.XHS_Collector_Mst_Tbl, XStudio_Historian.dbo.XHS_Tag_AVG_Value_Usp, XStudio_Historian.dbo.XHS_Tag_MAX_Value_Usp, XStudio_Historian.dbo.XHS_Tag_MIN_Value_Usp, XStudio_Historian.dbo.XHS_Tag_Mst_Tbl, XStudio_XBatch.dbo.RM_Mill_MST_TBL, XStudio_XBatch.dbo.RM_Mill_Tag_Mapping_Tbl

## dbo.Xstudio_Historian_RM_NGConsumption_Report_usp
Safety: MUTATING
Parameters: @StartTime:datetime, @EndTime:datetime, @Attribute:varchar(50), @Equipment:varchar(36), @CollectorID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration.dbo.XStudio_Summary_Entity_Historian_Schedule_Task_Usp, XStudio_Configuration_XBatch.dbo.XStudio_Block_Databases_Mst_Tbl, XStudio_Configuration_XBatch.dbo.XStudio_Block_Entities_Mst_Tbl, XStudio_Historian.dbo.XHS_Channel_Group_Mst_Tbl, XStudio_Historian.dbo.XHS_Channel_Mst_Tbl, XStudio_Historian.dbo.XHS_Collector_Mst_Tbl, XStudio_Historian.dbo.XHS_Tag_Last_Value_Usp, XStudio_Historian.dbo.XHS_Tag_MAX_Value_Usp, XStudio_Historian.dbo.XHS_Tag_Mst_Tbl, XStudio_Xbatch.dbo.RM_NGConsumption, XStudio_XBatch.dbo.RM_Reheating_Furnace_MST_TBL, XStudio_XBatch.dbo.RM_Reheating_Furnace_Tag_Mapping_Tbl

## dbo.XStudio_Historian_Shift_SMS_Production_Usp
Safety: MUTATING
Parameters: @Entrydatetime:datetime, @DatabaseName:varchar(200), @EntityName:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_XBatch.dbo.XStudio_Block_Entities_Mst_Tbl, XStudio_XBatch.dbo.CCM_SMS_Block, XStudio_XBatch.dbo.CCM_SMS_MST_TBL, XStudio_XBatch.dbo.SMS_Production_Summary_Shift, XStudio_XBatch.dbo.XStudio_Shift_Dtl_Tbl, XStudio_XBatch.dbo.XStudio_Shift_Mst_Tbl

## dbo.Xstudio_Historian_Summary_SMS_Production_Usp
Safety: MUTATING
Parameters: @Entrydatetime:datetime, @DatabaseName:varchar(200), @EntityName:varchar(200)
Referenced objects: Xstudio_Configuration.dbo.Xstudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.Xstudio_Historian_Day_SMS_Production_Usp, XStudio_XBatch.dbo.Xstudio_Historian_Shift_SMS_Production_Usp

## dbo.XStudio_Inventory_Pull_Schedule_TSQL_Task_Usp
Safety: MUTATING
Parameters: @Plant:nvarchar(20)
Referenced objects: XStudio_Configuration_Xbatch.dbo.XStudio_API_Request_Configuration_Mst_Tbl, XStudio_Xbatch.dbo.MES_SAP_Inventory_Stock_Tbl, XStudio_Xbatch.dbo.XStudio_ScheduleTask_Trn_Tbl

## dbo.Xstudio_Life_Tracking_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Life_Tracking

## dbo.XStudio_List_Rebar_YS_Bucket_Data_SP
Safety: MUTATING
Parameters: @FromDate:datetime, @ToDate:datetime, @Line:varchar(50)
Referenced objects: XStudio_XBatch.dbo.Rebar_Daywise_Data

## dbo.XStudio_List_Rebar_YS_StdDev_By_Line_SP
Safety: MUTATING
Parameters: @FromDate:datetime, @ToDate:datetime
Referenced objects: XStudio_XBatch.dbo.Rebar_Daywise_Data

## dbo.Xstudio_LRF_Manual_Entry_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.LRF_Manual_Entry

## dbo.Xstudio_LRF_Per_Heat_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.LRF_Per_Heat

## dbo.Xstudio_LRF_ProcessTime_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.LRF_ProcessTime

## dbo.Xstudio_LRF_SMS_Data_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.LRF_SMS_Data

## dbo.Xstudio_MES_Raw_Material_Consumptions_Trn_Tbl_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.MES_Raw_Material_Consumptions_Trn_Tbl

## dbo.Xstudio_Power_Consumption_LogSheet_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Power_Consumption_LogSheet

## dbo.XStudio_PowerShell_Schedule_TSQL_Task_Usp
Safety: MUTATING
Parameters: @name:varchar(500), @Path:nvarchar(max)
Referenced objects: XStudio_Xbatch.dbo.XStudio_ScheduleTask_Trn_Tbl

## dbo.Xstudio_ProductionMonthlyTargets_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.ProductionMonthlyTargets

## dbo.Xstudio_Rebar_Coil_Quality_Data_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Xbatch.dbo.High_Low_Devaition_Parameter, XStudio_Xbatch.dbo.Rebar_Coil_Quality_Data

## dbo.Xstudio_Rebar_Quality_Data_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Xbatch.dbo.High_Low_Devaition_Parameter, XStudio_Xbatch.dbo.Rebar_Quality_Data

## dbo.Xstudio_RM_Billet_Charging_And_Discharging_Logsheet_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.RM_Billet_Charging_And_Discharging_Logsheet

## dbo.Xstudio_RM_Cold_Crop_Wastage_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.RM_Cold_Crop_Wastage

## dbo.Xstudio_RM_Furnace_Parameter_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.RM_Furnace_Parameter

## dbo.Xstudio_RM_NGConsumption_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.RM_NGConsumption

## dbo.Xstudio_RM_Operator_HeatSelection_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Xbatch.dbo.FN_GET_BilletLength, Xstudio_Xbatch.dbo.FN_GET_Grade, XStudio_Xbatch.dbo.RM_Operator_HeatSelection

## dbo.Xstudio_RM_Roll_Stock_Card_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.RM_Roll_Stock_Card

## dbo.Xstudio_RM_Roll_Turning_Job_Card_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Xbatch.dbo.FN_GET_ReportDate, Xstudio_Xbatch.dbo.FN_Get_ShiftName, XStudio_Xbatch.dbo.RM_Roll_Turning_Job_Card

## dbo.Xstudio_RM_Shift_Producation_Report_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.RM_Shift_Producation_Report

## dbo.Xstudio_RM_TC_Grinding_Logbook_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Xbatch.dbo.FN_GET_ReportDate, Xstudio_Xbatch.dbo.FN_Get_ShiftName, XStudio_Xbatch.dbo.RM_TC_Grinding_Logbook

## dbo.Xstudio_Round_Bar_Quality_Data_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Round_Bar_Quality_Data

## dbo.Xstudio_Schedule_Popup_Notification_USP
Safety: MUTATING
Parameters: @Title:varchar(100), @body:nvarchar(max), @systemid:varchar(36), @userid:nvarchar(max), @TimeOut:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.XStudio_Schedule_TSQL_Task_Usp
Safety: MUTATING
Parameters: @name:varchar(500), @ID:nvarchar(max)
Referenced objects: XStudio_Xbatch.dbo.XStudio_ScheduleTask_Trn_Tbl

## dbo.Xstudio_Shift_CCM_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @DatabaseName:varchar(200), @EntityName:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.CCM_Per_Heat, XStudio_XBatch.dbo.CCM_Summary_Shift, XStudio_XBatch.dbo.XStudio_Shift_Dtl_Tbl, XStudio_XBatch.dbo.XStudio_Shift_Mst_Tbl

## dbo.Xstudio_Shift_EAF_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @DatabaseName:varchar(200), @EntityName:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.EAF_PER_HEAT, XStudio_XBatch.dbo.EAF_Summary_Shift, XStudio_XBatch.dbo.XStudio_Shift_Dtl_Tbl, XStudio_XBatch.dbo.XStudio_Shift_Mst_Tbl

## dbo.Xstudio_Shift_LRF_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @DatabaseName:varchar(200), @EntityName:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.LRF_Per_Heat, XStudio_XBatch.dbo.LRF_Summary_Shift, XStudio_XBatch.dbo.XStudio_Shift_Dtl_Tbl, XStudio_XBatch.dbo.XStudio_Shift_Mst_Tbl

## dbo.Xstudio_Shift_Operator_Incharge_Selection_Trn_Tbl_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Shift_Operator_Incharge_Selection_Trn_Tbl

## dbo.Xstudio_ShiftDelayEntry_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Xbatch.dbo.FN_GET_ReportDate, Xstudio_Xbatch.dbo.FN_Get_ShiftName, XStudio_Xbatch.dbo.ShiftDelayEntry

## dbo.Xstudio_SMS_EAF_Per_Heat_ChargeMix_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.SMS_EAF_Per_Heat_ChargeMix

## dbo.Xstudio_SMS_Plant_Process_EventTime_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.SMS_Plant_Process_EventTime

## dbo.Xstudio_SMS_Production_Summary_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.SMS_Production_Summary

## dbo.Xstudio_SMS_Shift_Operator_Incharge_Selection_Trn_Tbl_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl

## dbo.Xstudio_Summary_CCM_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @DatabaseName:varchar(200), @EntityName:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XStudio_Day_CCM_Usp, XStudio_XBatch.dbo.XStudio_Shift_CCM_Usp

## dbo.Xstudio_Summary_Consumptions_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @DatabaseName:varchar(200), @EntityName:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XStudio_Day_Consumptions_Usp

## dbo.Xstudio_Summary_EAF_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @DatabaseName:varchar(200), @EntityName:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XStudio_Day_EAF_Usp, XStudio_XBatch.dbo.XStudio_Shift_EAF_Usp

## dbo.Xstudio_Summary_LRF_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @DatabaseName:varchar(200), @EntityName:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XStudio_Day_LRF_Usp, XStudio_XBatch.dbo.XStudio_Shift_LRF_Usp

## dbo.Xstudio_Summary_RM_Consumption_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @DatabaseName:varchar(200), @EntityName:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XStudio_Day_RM_Consumption_Usp

## dbo.Xstudio_Transformer_125MVA_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Xbatch.dbo.FN_Get_ShiftName, XStudio_Xbatch.dbo.Transformer_125MVA

## dbo.Xstudio_Transformer_15MVA_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Xbatch.dbo.FN_Get_ShiftName, XStudio_Xbatch.dbo.Transformer_15MVA

## dbo.Xstudio_Transformer_24MVA_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Xbatch.dbo.FN_Get_ShiftName, XStudio_Xbatch.dbo.Transformer_24MVA

## dbo.Xstudio_Transformer_6_6kv_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Xbatch.dbo.FN_Get_ShiftName, XStudio_Xbatch.dbo.Transformer_6_6kv

## dbo.Xstudio_Transformer_63MVA_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Xbatch.dbo.FN_Get_ShiftName, XStudio_Xbatch.dbo.Transformer_63MVA

## dbo.Xstudio_Transformer_BATTERY_BANK_DG_STATUS_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Xbatch.dbo.FN_Get_ShiftName, XStudio_Xbatch.dbo.Transformer_BATTERY_BANK_DG_STATUS

## dbo.Xstudio_Transformer_Capacitor_Bank_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Xbatch.dbo.FN_Get_ShiftName, XStudio_Xbatch.dbo.Transformer_Capacitor_Bank

## dbo.Xstudio_Transformer_LRF_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Xbatch.dbo.FN_Get_ShiftName, XStudio_Xbatch.dbo.Transformer_LRF

## dbo.XStudio_Update_Day_CCM_Usp
Safety: MUTATING
Parameters: @ReportDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.CCM_Summary_Day

## dbo.XStudio_Update_Day_Consumptions_Usp
Safety: MUTATING
Parameters: @ReportDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.Consumptions_Summary_Day

## dbo.XStudio_Update_Day_EAF_Usp
Safety: MUTATING
Parameters: @ReportDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.EAF_Summary_Day

## dbo.XStudio_Update_Day_LRF_Usp
Safety: MUTATING
Parameters: @ReportDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.LRF_Summary_Day

## dbo.XStudio_Update_Day_RM_Consumption_Usp
Safety: MUTATING
Parameters: @ReportDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.RM_Consumption_Summary_Day

## dbo.XStudio_Update_Day_SMS_Production_Usp
Safety: MUTATING
Parameters: @ReportDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.SMS_Production_Summary_Day

## dbo.Xstudio_Wire_Rod_Quality_Data_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Wire_Rod_Quality_Data

## dbo.XSTUDIO_WORKFLOW_02ADFA58-6CF3-4D22-82A6-BE020FA00BC2_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XMES_SAP_API_GoodsMovement_Error

## dbo.XSTUDIO_WORKFLOW_0C110E49-9524-40BE-9C70-4A0BEDB53C79_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.Electricity_Meter_Reading

## dbo.XSTUDIO_WORKFLOW_0E59C696-ECB5-4E5C-B246-4275C0A324A4_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.MES_SAP_Production_Trn_Tbl, XStudio_Xbatch.dbo.MES_SAP_Production_Trn_Tbl

## dbo.XSTUDIO_WORKFLOW_17E91BC0-FC67-4CB1-9699-1625D71488F2_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Life_Tracking_Transaction_tbl, XStudio_XBatch.dbo.XMES_ActiveLife_Element_Mst_Tbl, XStudio_Xbatch.dbo.XMES_Element_Life_Counter_Trn_Tbl, XStudio_Xbatch.dbo.XMES_Life_Element_Mst_Tbl, XStudio_Xbatch.dbo.XMES_Life_Element_Type_Mst_Tbl

## dbo.XSTUDIO_WORKFLOW_18207AB4-8668-4F3C-B913-03CF7068BB96_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.SMS_Plant_Process_EventTime, Xstudio_xbatch.dbo.SMS_Plant_Process_EventTime

## dbo.XSTUDIO_WORKFLOW_18A1AF1E-0F09-42F7-9A37-C83AFED8D509_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.Billets_Per_Stand_Tracking

## dbo.XSTUDIO_WORKFLOW_1902B563-DDCD-4A38-9487-FE6186063998_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XMES_Campaign_Plan_Mst

## dbo.XSTUDIO_WORKFLOW_1A5F9D1B-7093-4BA2-9EAA-4ACD7371B992_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Xbatch.dbo.EAF_Per_Heat, xstudio_xbatch.dbo.eaf_per_heat, XStudio_XBatch.dbo.LRF_Per_Heat, xstudio_Xbatch.dbo.xbatch_work_order_mst_tbl, XStudio_Xbatch.dbo.XMES_ActiveLife_Element_Mst_Tbl

## dbo.XSTUDIO_WORKFLOW_21B64647-6F2C-4089-AEA4-54D9482E3A83_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XBatch_Sales_Order_Mst_Tbl

## dbo.XSTUDIO_WORKFLOW_23A94AFA-F5AE-4E7F-A558-84B7DA72D410_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.MES_SAP_Production_Trn_Tbl, XStudio_Xbatch.dbo.XMES_Log_trn_Tbl, XStudio_Xbatch.dbo.XMES_SAP_Batch_Characteristic_Trn_Tbl

## dbo.XSTUDIO_WORKFLOW_24F2F246-218B-40A0-99DB-EC15F3350D4E_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XBatch_Material_Inventory_Mst_Tbl

## dbo.XSTUDIO_WORKFLOW_29CCAEB2-7671-407A-8BC3-A40164145BD2_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XBatch_Sales_Order_Mst_Tbl

## dbo.XSTUDIO_WORKFLOW_2AF85FD5-BE15-4380-9504-341EE986C74D_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XBatch_Sales_Order_Mst_Tbl

## dbo.XSTUDIO_WORKFLOW_2D29BB58-88E0-4211-B392-36920B94C0F7_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.Electricity_Meter_Reading

## dbo.XSTUDIO_WORKFLOW_2F446F30-57E6-4AC7-A199-42928FC388E2_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Historian.dbo.XHS_Retrieve_Tag_Full_Value_Usp, XStudio_XBatch.dbo.EAF_PER_HEAT, XStudio_Xbatch.dbo.EAF_SMS_Tag_Mapping_Tbl, XStudio_Xbatch.dbo.XMES_ActiveLife_Element_Mst_Tbl, XStudio_Xbatch.dbo.XMES_Log_trn_Tbl

## dbo.XSTUDIO_WORKFLOW_35A3A6C3-97F5-4029-9B30-47985E01CF21_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XMES_Campaign_Plan_Mst

## dbo.XSTUDIO_WORKFLOW_3BFFE5C9-33C9-4C50-A0F0-3665571F92D4_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.MES_SAP_Production_Trn_Tbl, XStudio_XBatch.dbo.XMES_SAP_Batch_Characteristic_Trn_Tbl

## dbo.XSTUDIO_WORKFLOW_3CD875CC-85C4-4587-848E-DF9361C98F5B_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.BilletsTracking_In_Furnace

## dbo.XSTUDIO_WORKFLOW_5ACC8A8C-2983-4EEF-ABD3-F027D83F5764_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.Billet_Track_Per_Strand

## dbo.XSTUDIO_WORKFLOW_5EE12FEC-3EFD-44D0-8EC8-CC4DCFCE98F4_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Xbatch.dbo.FN_Get_ShiftName, XStudio_XBatch.dbo.RM_Delays

## dbo.XSTUDIO_WORKFLOW_61A5C1A4-855A-43C6-81EB-11574448AE84_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XBatch_Work_Order_Mst_Tbl

## dbo.XSTUDIO_WORKFLOW_61EFD8FE-EDF5-4077-BE99-35EF68C5AFCB_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XMES_SAP_API_GoodsMovement_Error

## dbo.XSTUDIO_WORKFLOW_64B14ECC-2663-434D-B0DC-FF705136AA3A_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.CCM_Per_Heat, xstudio_Xbatch.dbo.xbatch_work_order_mst_tbl

## dbo.XSTUDIO_WORKFLOW_69C53936-AFB3-44F8-874A-FE2336FB0279_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_Xbatch.dbo.XStudio_Block_Databases_Mst_Tbl, XStudio_Configuration_XBatch.dbo.XStudio_Block_Entities_Mst_Tbl, XStudio_XBatch.dbo.LRF_Per_Heat, XStudio_Xbatch.dbo.LRF_Per_Heat, XStudio_Xbatch.dbo.LRF_SMS_Data

## dbo.XSTUDIO_WORKFLOW_6F954B26-CB87-40FC-8B73-26EE001C55DC_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_Data, XStudio_XBatch.dbo.CCM_Per_Heat, Xstudio_Xbatch.dbo.EAF_Per_Heat, xstudio_xbatch.dbo.eaf_per_heat, XStudio_Xbatch.dbo.XMES_ActiveLife_Element_Mst_Tbl

## dbo.XSTUDIO_WORKFLOW_7A119B7F-E474-4946-85D9-4D58065DACBF_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.Delay_Trn_Tbl

## dbo.XSTUDIO_WORKFLOW_7BBFE023-3C57-4473-96E0-B6CF231296F9_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XMES_Campaign_Plan_Mst

## dbo.XSTUDIO_WORKFLOW_8DA0CF0E-F9EA-4024-AB36-0C296DE94F61_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Xbatch.dbo.EAF_Per_Heat, XStudio_XBatch.dbo.LRF_Per_Heat

## dbo.XSTUDIO_WORKFLOW_92A749C7-433A-4097-B5A2-95E6350FB25B_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XMES_Campaign_Plan_Mst

## dbo.XSTUDIO_WORKFLOW_94F414DB-7BB1-4CCF-B50D-65A1E6101382_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.BilletsCastCount, Xstudio_xbatch.dbo.CCM_PER_HEAT, Xstudio_xbatch.dbo.EAF_PER_HEAT, XStudio_Xbatch.dbo.Life_Tracking, XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_94F414DB

## dbo.XSTUDIO_WORKFLOW_98A73AE1-1D20-4959-B45E-121B93225279_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.MES_Raw_Material_Consumptions_Mapping_Mst_Tbl, XStudio_XBatch.dbo.MES_Raw_Material_Consumptions_Trn_Tbl, XStudio_Xbatch.dbo.MES_Raw_Material_Consumptions_Trn_Tbl, XStudio_Xbatch.dbo.MES_SAP_Consumption_Trn_Tbl, XStudio_Xbatch.dbo.Plant_Name_MST, XStudio_Xbatch.dbo.Storage_Location_MST, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Work_Order_Mst_Tbl

## dbo.XSTUDIO_WORKFLOW_9B20AE0B-2E34-4BF8-9875-BB52B5C007E0_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XBatch_Work_Order_Mst_Tbl

## dbo.XSTUDIO_WORKFLOW_9F899B3A-621E-426A-B53F-11EDD062EC6B_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XMES_Campaign_Plan_Mst

## dbo.XSTUDIO_WORKFLOW_A1B200C6-5046-41BE-9CD1-84454600575D_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XBatch_Work_Order_Mst_Tbl

## dbo.XSTUDIO_WORKFLOW_A33E0C6A-390E-4BFA-812D-0CF28EC79BF6_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XMES_Campaign_Plan_Mst

## dbo.XSTUDIO_WORKFLOW_A6124179-0C6C-4218-A43F-FBDE140C034A_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XMES_Life_Tracker_Register_Mst_Tbl

## dbo.XSTUDIO_WORKFLOW_A6D3AC4F-60D5-4423-8936-0F59CEEA2C39_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XBatch_Work_Order_Mst_Tbl

## dbo.XSTUDIO_WORKFLOW_A8001D7B-0DFD-4034-B0DE-A73B7218AD49_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.SMS_Delay_Trn_Tbl

## dbo.XSTUDIO_WORKFLOW_B0E88401-847E-4370-9B0F-6D0BD87E68E2_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_XBatch.dbo.Electricity_Meter_Reading, XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_B0E88401

## dbo.XSTUDIO_WORKFLOW_B4724DFC-A609-44DA-A6D1-899EF9A79C90_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.BilletsCastCount, Xstudio_xbatch.dbo.CCM_PER_HEAT, Xstudio_xbatch.dbo.EAF_PER_HEAT, XStudio_Xbatch.dbo.SP_Xbatch_SplitsBillets_From_CCM_To_Inventory

## dbo.XSTUDIO_WORKFLOW_B74AE750-0673-47A3-8861-D7BBF127C2C7_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.BilletsTracking_In_Furnace

## dbo.XSTUDIO_WORKFLOW_B9D3C9DD-71EB-4175-B947-B68269F1E8E6_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.Electricity_Meter_Reading_Upload

## dbo.XSTUDIO_WORKFLOW_C18D4DFF-8ADA-4080-9F2F-91DE212A1257_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XBatch_Work_Order_Mst_Tbl

## dbo.XSTUDIO_WORKFLOW_C2B0C95A-B3B7-466F-9BFE-CDCC5017EB57_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XBatch_Sales_Order_Mst_Tbl

## dbo.XSTUDIO_WORKFLOW_C5631C30-B02A-4FEF-B2B7-E811DB1A0B59_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.Heat_Chemistry_Quality_Data, XStudio_Xbatch.dbo.XMES_Log_trn_Tbl

## dbo.XSTUDIO_WORKFLOW_C67D7329-8634-4DCC-94B2-B2B950981934_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XBatch_Sales_Order_Mst_Tbl

## dbo.XSTUDIO_WORKFLOW_C7EA6F22-24BB-490A-A748-6AE14C39B81D_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XMES_RM_Campaign_Plan_Trn

## dbo.XSTUDIO_WORKFLOW_CB83D9D0-0256-44F8-BC97-461935B736D8_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.EAF_PER_HEAT, XStudio_Xbatch.dbo.EAF_PER_HEAT

## dbo.XSTUDIO_WORKFLOW_CBDD76F9-AF65-4113-B5FE-987066DC8DDD_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XBatch_Work_Order_Mst_Tbl

## dbo.XSTUDIO_WORKFLOW_DE81675D-78C0-4060-BC94-D8FD0973FC62_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XMES_Campaign_Plan_Mst

## dbo.XSTUDIO_WORKFLOW_DEDE4001-3D55-41CB-8F02-2C2F8155E659_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.CCM_Per_Heat, Xstudio_Xbatch.dbo.EAF_Per_Heat

## dbo.XSTUDIO_WORKFLOW_DFEC0CB6-0A1F-4222-9A06-A25774049AC8_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.CCM_ProcessTime

## dbo.XSTUDIO_WORKFLOW_E2571DEB-9445-4B73-9BA2-5ED89412D715_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XMES_Campaign_Plan_Mst

## dbo.XSTUDIO_WORKFLOW_E5621281-3613-41D8-BF2E-4FFB17C30EAC_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XBatch_Sales_Order_Mst_Tbl

## dbo.XSTUDIO_WORKFLOW_F44EBC19-952C-4FC0-B3E8-64696B55EAD2_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.Electricity_Meter_Reading_Upload

## dbo.XSTUDIO_WORKFLOW_F4CB27BF-724B-4771-B93E-C17AAA1CFB9E_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XMES_Campaign_Plan_Mst

## dbo.XSTUDIO_WORKFLOW_FC44CBFD-6EDD-4543-8305-B6560572182C_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.Billets_Per_Stand_Tracking, XStudio_Xbatch.dbo.Xstudio_Historian_RM_Mill_Block_usp

## dbo.XSTUDIO_WORKFLOW_FF0AE3BF-1A32-4635-B431-3BA6931332AA_SP
Safety: MUTATING
Parameters: @p_SystemId:varchar(36), @p_UserId:varchar(36), @p_RecordId:varchar(36), @p_StatusAttributeName:varchar(200), @p_Status:varchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XMES_Campaign_Plan_Mst

## dbo.Xstudio_XBatch_Sales_Order_Mst_Tbl_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.XBatch_Sales_Order_Mst_Tbl

## dbo.Xstudio_XBatch_Work_Order_Mst_Tbl_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Sales_Order_Mst_Tbl, XStudio_Xbatch.dbo.XBatch_Work_Order_Mst_Tbl

## dbo.Xstudio_XMES_SMS_Event_Process_Tracker_Mst_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Mode:varchar(20)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.XMES_SMS_Event_Process_Tracker_Mst

