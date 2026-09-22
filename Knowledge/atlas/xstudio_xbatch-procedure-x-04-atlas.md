---
type: note
subtype: procedure-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch stored-procedure atlas: X part 4

Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.

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
