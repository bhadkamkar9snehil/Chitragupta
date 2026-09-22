---
type: note
subtype: procedure-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch stored-procedure atlas: X part 2

Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.

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
