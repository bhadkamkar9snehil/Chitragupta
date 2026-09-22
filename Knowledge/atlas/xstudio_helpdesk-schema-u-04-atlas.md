---
type: note
subtype: schema-reference
database: XStudio_Helpdesk
authority: static-advisory
---
# XStudio_Helpdesk schema atlas: U part 4

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.UAT_MANUALPOCREATION_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit, Fileupload:varchar

## dbo.UAT_MISSINGSIGNALHANDLING
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit, Fileupload:varchar

## dbo.UAT_MISSINGSIGNALHANDLING_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit, Fileupload:varchar

## dbo.UAT_POAUTOCREATION
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit, Fileupload:varchar

## dbo.UAT_POAUTOCREATION_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit, Fileupload:varchar

## dbo.UAT_POFIELDVALIDATION
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit, Fileupload:varchar

## dbo.UAT_POFIELDVALIDATION_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit, Fileupload:varchar

## dbo.UAT_POWERCONSUMPTIONCHARTMETERWISE
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, Fileupload:varchar, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit

## dbo.UAT_POWERCONSUMPTIONCHARTMETERWISE_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, Fileupload:varchar, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit

## dbo.UAT_POWERCONSUMPTIONLOGSHEET
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, Fileupload:varchar, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit

## dbo.UAT_POWERCONSUMPTIONLOGSHEET_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, Fileupload:varchar, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit

## dbo.UAT_POWERCONSUMPTIONREPORTLOGSHEET
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, Fileupload:varchar, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit

## dbo.UAT_POWERCONSUMPTIONREPORTLOGSHEET_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, Fileupload:varchar, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit

## dbo.UAT_RAWMATERIAL
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EndDateTime:datetime, TesterName:varchar, IsProcessed:bit, Q3:varchar, EntryDateTime:datetime, Q1:varchar, Q1Verdict:bit, OverallVerdict:bit, Q2Verdict:bit, Q2:varchar, Q3Verdict:bit, ReportDate:date, TestName:varchar, Comments:varchar, Fileupload:varchar

## dbo.UAT_RAWMATERIAL_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EndDateTime:datetime, TesterName:varchar, IsProcessed:bit, Q3:varchar, EntryDateTime:datetime, Q1:varchar, Q1Verdict:bit, OverallVerdict:bit, Q2Verdict:bit, Q2:varchar, Q3Verdict:bit, ReportDate:date, TestName:varchar, Comments:varchar, Fileupload:varchar

## dbo.UAT_REALTIMEDASHBOARD
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit, Fileupload:varchar

## dbo.UAT_REALTIMEDASHBOARD_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit, Fileupload:varchar

## dbo.UAT_ROLEBASEDFIELDEDIT
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit, Fileupload:varchar

## dbo.UAT_ROLEBASEDFIELDEDIT_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit, Fileupload:varchar

## dbo.UAT_SCRAPCHARGING
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit, Fileupload:varchar

## dbo.UAT_SCRAPCHARGING_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit, Fileupload:varchar

## dbo.UAT_SHIFTDELAYREPORT
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit, Fileupload:varchar

## dbo.UAT_SHIFTDELAYREPORT_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit, Fileupload:varchar

## dbo.UAT_SMS_LIVEDATADASHBOARD
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, Fileupload:varchar, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit

## dbo.UAT_SMS_LIVEDATADASHBOARD_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, Fileupload:varchar, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit

## dbo.UAT_SMS_PLANTDASHBOARD
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, Fileupload:varchar, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit

## dbo.UAT_SMS_PLANTDASHBOARD_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, Fileupload:varchar, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit

## dbo.UAT_SMS_PLANTPROCESSTIME
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, Fileupload:varchar, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit

## dbo.UAT_SMS_PLANTPROCESSTIME_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, Fileupload:varchar, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit

## dbo.UAT_TRANSFORMER125MVA
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, Fileupload:varchar, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit

## dbo.UAT_TRANSFORMER125MVA_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, Fileupload:varchar, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit

## dbo.UAT_TRANSFORMER15MVALOGSHEET
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Fileupload:varchar, EntryDateTime:datetime, Q1Verdict:bit, Q2Verdict:bit, EndDateTime:datetime, Q1:varchar, Comments:varchar, Q2:varchar, Q3:varchar, Q3Verdict:bit, OverallVerdict:bit, TesterName:varchar, ReportDate:date, IsProcessed:bit, TestName:varchar

## dbo.UAT_TRANSFORMER15MVALOGSHEET_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Fileupload:varchar, EntryDateTime:datetime, Q1Verdict:bit, Q2Verdict:bit, EndDateTime:datetime, Q1:varchar, Comments:varchar, Q2:varchar, Q3:varchar, Q3Verdict:bit, OverallVerdict:bit, TesterName:varchar, ReportDate:date, IsProcessed:bit, TestName:varchar

## dbo.UAT_TRANSFORMER24MVA
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, Fileupload:varchar, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit

## dbo.UAT_TRANSFORMER24MVA_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, Fileupload:varchar, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit

## dbo.UAT_TRANSFORMER63MVA
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, Fileupload:varchar, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit

## dbo.UAT_TRANSFORMER63MVA_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Q1Verdict:bit, Q3Verdict:bit, Q3:varchar, EndDateTime:datetime, Q1:varchar, ReportDate:date, EntryDateTime:datetime, Fileupload:varchar, TestName:varchar, Q2Verdict:bit, OverallVerdict:bit, Q2:varchar, TesterName:varchar, Comments:varchar, IsProcessed:bit

## dbo.UAT_TRANSFORMER6_6KVLOGSHEET
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Fileupload:varchar, EntryDateTime:datetime, Q1Verdict:bit, Q2Verdict:bit, EndDateTime:datetime, Q1:varchar, Comments:varchar, Q2:varchar, Q3:varchar, Q3Verdict:bit, OverallVerdict:bit, TesterName:varchar, ReportDate:date, IsProcessed:bit, TestName:varchar

## dbo.UAT_TRANSFORMER6_6KVLOGSHEET_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Fileupload:varchar, EntryDateTime:datetime, Q1Verdict:bit, Q2Verdict:bit, EndDateTime:datetime, Q1:varchar, Comments:varchar, Q2:varchar, Q3:varchar, Q3Verdict:bit, OverallVerdict:bit, TesterName:varchar, ReportDate:date, IsProcessed:bit, TestName:varchar

## dbo.UAT_Test_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Description:varchar, ExpectedOutcomeType:varchar, AreaName:varchar, Srno:int, EditPageID:varchar, LvPageID:varchar, Helpdoc:varchar, Icon:varchar, EnableUAT:bit

## dbo.UAT_Test_Report_Data
ID:varchar, TestName:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, TestingStartDatetime:datetime, IsProcessed:bit, TestingEndDatetime:datetime, TesterName:varchar, Q1Verdict:varchar, Q2Verdict:varchar, Q3Verdict:varchar, OverallVerdict:varchar, Remarks:varchar, EntityName:varchar, Q4Verdict:varchar, AreaName:varchar

## dbo.UAT_Tracking_Transaction
ID:varchar, TotalUATsTested:int, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, TotalUserConductedTest:int, TotalUATPassRate:decimal, TotalUATFailRate:decimal, LastTestConducted:datetime, UATDuration:int

## dbo.UserDetails
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar
