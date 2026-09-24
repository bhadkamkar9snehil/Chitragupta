---
type: table
title: "ShiftDelayEntry"
built: "2026-09-24T11:36:36"
---

# ShiftDelayEntry

Table in XStudio_Xbatch. Rows: 19,231.

## Written by

- DelayEntry_EBTFilling_USP
- MES_U_Delay_Merge
- SMS_DelayRemainingDuration_U_Usp
- SP_RM_Delay_Data_Modify_By_Operator
- ShiftDelayEntry_ManagerOperatorName_Usp
- ShiftDelayEntry_Update_usp
- XMES_Cummulative_RMDelay_Entry_USP
- XMES_Delay_Split_Entry_Usp
- XSTUDIO_WORKFLOW_5EE12FEC-3EFD-44D0-8EC8-CC4DCFCE98F4_SP
- Xstudio_ShiftDelayEntry_USP

## Read by

- DelayEntry_EBTFilling_USP
- MES_U_Delay_Merge
- SMS_AgencyWiseDelayDuration_Validation_Usp
- SMS_DelayRemainingDuration_U_Usp
- SP_RM_Delay_Data_Modify_By_Operator
- SP_SMS_OEE_Daily_View
- SP_SMS_Producation_Summary
- ShiftDelayEntry_ManagerOperatorName_Usp
- ShiftDelayEntry_Update_usp
- XBatch_OEE_Dashboard_SP
- XMES_Dashboard_EAF_Live_USP
- XMES_Delay_Split_Entry_Usp
- XMES_Delay_Split_Validate_Usp
- XMES_SMS_Dashboard_Delay_USP
- Xstudio_ShiftDelayEntry_USP
- sp_Generate_CAPA_No

## Columns

- ID varchar(36)
- CreatedBy varchar(36)
- ModifiedBy varchar(36)
- CreatedOn datetime
- ModifiedOn datetime
- IsDeleted bit
- IsSystem bit
- AssignedUserID varchar(36)
- HostAddress varchar(100)
- DbSyncStatus varchar(500)
- MobileSyncStatus varchar(100)
- Source varchar(20)
- DelayStartTime datetime
- DelayInMinutes decimal
- ParentID varchar(36)
- DelayEndTime datetime
- DelayReason varchar(-1)
- DelayType varchar(36)
- DelayAgency varchar(36)
- AgencyOther varchar(100)
- HeatNo int
- EquipmentName varchar(-1)
- SubEquipmentName varchar(36)
- ReportDate varchar(100)
- AreaName varchar(-1)
- ShiftManager varchar(36)
- OperatorName varchar(36)
- RMProduct varchar(100)
- DelaySubtypeid varchar(36)
- DelayInSecond int
- Grade varchar(100)
- RMSection varchar(100)
- Shift varchar(100)
- Cobble int
- Hotout int
- Refractory int
- Mechanical int
- Electrical int
- Operation int
- OtherDelay int
- RemainingDuration decimal
- DelayDuration varchar(100)
- SMSReportDate varchar(100)
- CAPARecordid varchar(36)
- ShortDescription varchar(100)
- Issplit bit
- Status varchar(50)
