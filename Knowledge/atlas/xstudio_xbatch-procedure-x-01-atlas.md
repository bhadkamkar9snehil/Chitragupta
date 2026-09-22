---
type: note
subtype: procedure-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch stored-procedure atlas: X part 1

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
