---
type: Reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch stored-procedure atlas: S

Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.

## dbo.SAP_Posting_Data_ByHeat_Usp
Safety: MUTATING
Parameters: @HeatNo:nvarchar(50)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.SAP_Posting_Tbl

## dbo.ShiftDelayEntry_ManagerOperatorName_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @ShiftManager:varchar(36), @OperatorName:varchar(36), @DelayReason:varchar(max)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.ShiftDelayEntry_Update_usp
Safety: MUTATING
Parameters: @StartTime:datetime, @EndTime:datetime, @Status:varchar(max), @HeatNo:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.SMS_AgencyWiseDelayDuration_Validation_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @Duration:decimal(18,2), @Agency:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.SMS_Data_list_View
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.XMES_Log_trn_Tbl

## dbo.SMS_DelayRemainingDuration_U_Usp
Safety: MUTATING
Parameters: @MSTDelayID:varchar(36), @AgencyID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.SMS_Electricity_Meter_Bill_Amount_USP
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Electricity_Meter_Bill_Amount, XStudio_Xbatch.dbo.Electricity_Meter_Electricity_Bill_Details

## dbo.SMS_EquipmentWiseDelayDuration_Validation_Usp
Safety: MUTATING
Parameters: @ID:varchar(36), @Duration:decimal(18,2), @Equipment:nvarchar(100)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.SMS_AgencyWiseDelayDuration_Validation_Usp

## dbo.SMS_GET_CCM_HeatIDList
Safety: MUTATING
Parameters: none
Referenced objects: Xstudio_Xbatch.dbo.CCM_ProcessTime

## dbo.SMS_GET_EAF_HeatIDList
Safety: MUTATING
Parameters: @Type:bit
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, Xstudio_Xbatch.dbo.EAF_ProcessTime

## dbo.SMS_GET_LRF_HeatIDList
Safety: MUTATING
Parameters: none
Referenced objects: Xstudio_Xbatch.dbo.LRF_ProcessTime

## dbo.SMS_Ladle_Life_Tracking
Safety: MUTATING
Parameters: @LadleID:varchar(36), @HeatID:varchar(36), @ShellID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.sp_All_DB_Differential_Backup

## dbo.SMS_Ladle_Life_Tracking_Validation
Safety: MUTATING
Parameters: @LadleID:varchar(200), @HeatID:varchar(200)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Life_Tracking_Transaction_tbl, XStudio_Xbatch.dbo.XMES_Life_Element_Mst_Tbl

## dbo.SMS_Reset_Life_Tracking_Status
Safety: MUTATING
Parameters: @RecordID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Life_Tracking_Transaction_tbl, XStudio_Xbatch.dbo.XMES_Element_Life_Counter_Trn_Tbl, XStudio_Xbatch.dbo.XMES_Life_Element_Mst_Tbl, XStudio_Xbatch.dbo.XMES_Life_Element_Type_Mst_Tbl

## dbo.sp_All_DB_Differential_Backup
Safety: MUTATING
Parameters: none
Referenced objects: master.dbo.xp_create_subdir, XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.sp_All_DB_Backup

## dbo.sp_All_DB_Full_Backup
Safety: MUTATING
Parameters: none
Referenced objects: master.dbo.xp_create_subdir, XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.sp_All_DB_Backup

## dbo.sp_All_DB_Shrink
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.sp_All_DB_Transaction_log
Safety: MUTATING
Parameters: none
Referenced objects: master.dbo.xp_create_subdir, XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.sp_All_Historian_DB_Full_Backup
Safety: MUTATING
Parameters: @Mode:varchar(10), @RunDate:date, @BackupRootPath:nvarchar(2000), @LookbackDays:int, @ForceAll:bit
Referenced objects: master.dbo.xp_create_subdir, XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.HistorianBackupLog

## dbo.Sp_Check_GradeTestMapping_Specifications
Safety: MUTATING
Parameters: @recordid:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.Sp_DeleteBackupHistory
Safety: MUTATING
Parameters: @day:int
Referenced objects: msdb.dbo.sp_delete_backuphistory

## dbo.sp_Generate_CAPA_No
Safety: MUTATING
Parameters: @ID:varchar(36), @TransactionID:varchar(36), @AgencyID:varchar(36)
Referenced objects: none detected

## dbo.SP_GET_AREAWISE_TAG_TREND
Safety: MUTATING
Parameters: @Heatno:int, @Tagarea:nvarchar(max), @SRNO:int
Referenced objects: Xstudio_Historian.dbo.XHS_Retrieve_Tag_Full_Value_TestSSM_Usp

## dbo.SP_Get_CAPANO_SMS_RM
Safety: MUTATING
Parameters: @Type:varchar(10)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.Sp_Grade_Test_Mapping
Safety: MUTATING
Parameters: @RecordId:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.sp_Prevent_GradeTestMapping_Duplicate_Entry
Safety: MUTATING
Parameters: @Gradeid:varchar(36), @Testid:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.SP_ReCalculate_CCM_SMS_Block_USP
Safety: MUTATING
Parameters: @ReportDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_XBatch.dbo.XStudio_Block_Databases_Mst_Tbl, XStudio_Configuration_XBatch.dbo.XStudio_Block_Entities_Mst_Tbl, XStudio_Xbatch.dbo.BilletsCastCount, XStudio_Xbatch.dbo.CCM_Per_Heat, XStudio_Xbatch.dbo.Xstudio_Historian_CCM_SMS_Block_usp, XStudio_Xbatch.dbo.Xstudio_Summary_CCM_Usp

## dbo.SP_ReCalculate_LRF_SMS_Block_USP
Safety: MUTATING
Parameters: @ReportDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_XBatch.dbo.XStudio_Block_Databases_Mst_Tbl, XStudio_Configuration_XBatch.dbo.XStudio_Block_Entities_Mst_Tbl, XStudio_Configuration_Xbatch.dbo.XStudio_Entities_Mst_Tbl, XStudio_Xbatch.dbo.LRF_Per_Heat, XStudio_Xbatch.dbo.Xstudio_Historian_LRF_SMS_Block_usp, XStudio_Xbatch.dbo.Xstudio_Summary_LRF_Usp

## dbo.SP_ReCalculate_NG_Configuration_Block_USP
Safety: MUTATING
Parameters: @ReportDate:date
Referenced objects: master.dbo.spt_values, XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_XBatch.dbo.XStudio_Block_Databases_Mst_Tbl, XStudio_Configuration_XBatch.dbo.XStudio_Block_Entities_Mst_Tbl, XStudio_Configuration_Xbatch.dbo.XStudio_Entities_Mst_Tbl, XStudio_Xbatch.dbo.Xstudio_Historian_RM_NGConsumption_Report_usp

## dbo.SP_ReCalculate_RM_Furnace_Block_USP
Safety: MUTATING
Parameters: @ReportDate:date
Referenced objects: master.dbo.spt_values, XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Configuration_XBatch.dbo.XStudio_Block_Databases_Mst_Tbl, XStudio_Configuration_XBatch.dbo.XStudio_Block_Entities_Mst_Tbl, XStudio_Configuration_Xbatch.dbo.XStudio_Entities_Mst_Tbl, XStudio_Xbatch.dbo.Xstudio_Historian_RM_Furnace_Logbook_Block_usp

## dbo.SP_RM_Delay_Data_Modify_By_Operator
Safety: MUTATING
Parameters: @Reportdate:varchar(20), @Shift:varchar(5), @Product:varchar(40), @Section:varchar(40), @Operator:varchar(36), @ShiftManager:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.Sp_Sample_Characteristics_I_Values
Safety: MUTATING
Parameters: @Recordid:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.SP_SMS_Heat_Chemistry_Data_Section_Selection
Safety: MUTATING
Parameters: @FirstHeat:varchar(40), @LastHeat:varchar(40), @Grade:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.SP_SMS_OEE_Daily_View
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Xbatch.dbo.FN_GET_ReportDate, XStudio_Xbatch.dbo.ShiftDelayEntry, XStudio_Xbatch.dbo.SMS_Production_Summary, XStudio_Xbatch.dbo.SMS_Production_Summary_Day

## dbo.SP_SMS_Producation_Summary
Safety: MUTATING
Parameters: @ReportDate:date
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.CCM_Per_Heat, XStudio_Xbatch.dbo.Highest_Production_Entry, XStudio_Xbatch.dbo.Particulars_Masters, XStudio_Xbatch.dbo.Power_Consumption_Report, XStudio_Xbatch.dbo.SMS_Production_Summary, XStudio_XBatch.dbo.XMES_Recalculate_BackCalculation_GLS_USP

## dbo.SP_Xbatch_SplitsBillets_From_CCM_To_Inventory
Safety: MUTATING
Parameters: @HeatNo:varchar(36), @ItemName:varchar(500), @MaterialGrade:varchar(100), @Grade:varchar(500)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_XBatch.dbo.XBatch_Material_Item_Prod_Trn_Tbl

## dbo.SP_Xbatch_YMS_AssignBilletsToStack
Safety: MUTATING
Parameters: @GradeNo:varchar(36), @StackID:varchar(36), @UserID:varchar(36), @HeatNo:varchar(50)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.SP_XBatch_YMS_BilletsTransferSummary
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.xbatch_material_inventory_mst_tbl, XStudio_Xbatch.dbo.xbatch_storage_area_mst_tbl, XStudio_Xbatch.dbo.xbatch_storage_rack_mst_tbl

## dbo.SP_XBatch_YMS_Display_HeatNo_Wise_Total_Billet
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.SP_Xbatch_YMS_GenerateLayersForStack
Safety: MUTATING
Parameters: @StackID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.SP_XBatch_YMS_TransferIntoHistory
Safety: MUTATING
Parameters: @GradeNo:varchar(36), @StackID:varchar(36), @UserID:varchar(36), @HeatNo:varchar(50)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.SP_Xbatch_YMS_U_OutwardLocation
Safety: MUTATING
Parameters: @ID:varchar(36), @Userid:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.sp_Xstudio_XMES_RM_CampaignPlan_USP
Safety: MUTATING
Parameters: @recordid:varchar(36)
Referenced objects: none detected

## dbo.SP_YMS_StoarageCapacityDetails_With_TotalHeatNo
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

## dbo.sp_YMS_U_Location_Heatwise
Safety: MUTATING
Parameters: @HeatNo:varchar(50)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

