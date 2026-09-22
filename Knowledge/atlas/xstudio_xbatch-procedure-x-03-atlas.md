---
type: note
subtype: procedure-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch stored-procedure atlas: X part 3

Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.

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
