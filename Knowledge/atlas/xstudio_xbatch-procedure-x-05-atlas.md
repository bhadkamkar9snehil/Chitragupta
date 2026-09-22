---
type: note
subtype: procedure-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch stored-procedure atlas: X part 5

Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.

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
