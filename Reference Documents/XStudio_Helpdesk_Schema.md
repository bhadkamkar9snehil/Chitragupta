# LMEL MES Comprehensive Database Schema Reference

_Generated automatically on 2026-09-03 10:41:10 IST_

**Database:** `XStudio_Helpdesk`
**Server:** `10.2.6.204`
**Script Run DateTime:** `2026-09-03 10:41:10 IST`
**Script Run DateTime For File Name:** `2026-09-03_10-41-10`

This document provides detailed information about all included tables in the LMEL MES database:
- Schema (columns, data types, nullability, defaults)
- Primary keys
- Row counts and date ranges
- Top 10 and bottom 10 records per table

---

## Table of Contents

- [dbo.Area_Mst_Tbl](#dboareamsttbl)
- [dbo.Area_Mst_Tbl_Audit](#dboareamsttblaudit)
- [dbo.Asset_Hierarchy_Mst_Tbl](#dboassethierarchymsttbl)
- [dbo.Backup_Monitoring](#dbobackupmonitoring)
- [dbo.Backup_Monitoring_Audit](#dbobackupmonitoringaudit)
- [dbo.CentralDispatch_Mst_Tbl](#dbocentraldispatchmsttbl)
- [dbo.CentralDispatch_Mst_Tbl_Audit](#dbocentraldispatchmsttblaudit)
- [dbo.CommonErrors](#dbocommonerrors)
- [dbo.CommonErrors_Audit](#dbocommonerrorsaudit)
- [dbo.ComplaintType_Mst_Tbl](#dbocomplainttypemsttbl)
- [dbo.ComplaintType_Mst_Tbl_Audit](#dbocomplainttypemsttblaudit)
- [dbo.Complaint_Mst_Tbl](#dbocomplaintmsttbl)
- [dbo.Complaint_Mst_Tbl_Audit](#dbocomplaintmsttblaudit)
- [dbo.ControlRoom_Mst_Tbl](#dbocontrolroommsttbl)
- [dbo.ControlRoom_Mst_Tbl_Audit](#dbocontrolroommsttblaudit)
- [dbo.DLBMonitoring](#dbodlbmonitoring)
- [dbo.DLBMonitoring_Audit](#dbodlbmonitoringaudit)
- [dbo.Equipment_Type_Mst_Tbl](#dboequipmenttypemsttbl)
- [dbo.Events_Monitoring](#dboeventsmonitoring)
- [dbo.Events_Monitoring_Audit](#dboeventsmonitoringaudit)
- [dbo.FCM_Monitoring](#dbofcmmonitoring)
- [dbo.FCM_Monitoring_Audit](#dbofcmmonitoringaudit)
- [dbo.FCM_Node_Monitoring](#dbofcmnodemonitoring)
- [dbo.Folder_Monitoring](#dbofoldermonitoring)
- [dbo.Folder_Monitoring_Audit](#dbofoldermonitoringaudit)
- [dbo.HOD_Mst_Tbl](#dbohodmsttbl)
- [dbo.HOD_Mst_Tbl_Audit](#dbohodmsttblaudit)
- [dbo.Hardware_Monitoring](#dbohardwaremonitoring)
- [dbo.Hardware_Monitoring_Audit](#dbohardwaremonitoringaudit)
- [dbo.Hermes_L2_Response_Trn_Tbl](#dbohermesl2responsetrntbl)
- [dbo.Hermes_L2_SQL_Action_Trn_Tbl](#dbohermesl2sqlactiontrntbl)
- [dbo.HyperV_Monitoring](#dbohypervmonitoring)
- [dbo.HyperV_Monitoring_Audit](#dbohypervmonitoringaudit)
- [dbo.Import_Export](#dboimportexport)
- [dbo.MonitoringReport](#dbomonitoringreport)
- [dbo.Organization_Mst_Tbl](#dboorganizationmsttbl)
- [dbo.Pipeline_Mst_Tbl](#dbopipelinemsttbl)
- [dbo.Pipeline_Mst_Tbl_Audit](#dbopipelinemsttblaudit)
- [dbo.PowerGenerationOutput](#dbopowergenerationoutput)
- [dbo.PowerGenerationOutput_Audit](#dbopowergenerationoutputaudit)
- [dbo.Procedure_Mst_Tbl](#dboproceduremsttbl)
- [dbo.Procedure_Steps_Mst_Tbl](#dboprocedurestepsmsttbl)
- [dbo.Procedure_Task_Mst_Tbl](#dboproceduretaskmsttbl)
- [dbo.Region_Mst_Tbl](#dboregionmsttbl)
- [dbo.Region_Mst_Tbl_Audit](#dboregionmsttblaudit)
- [dbo.Replica_Monitoring](#dboreplicamonitoring)
- [dbo.Round_Mst_Tbl](#dboroundmsttbl)
- [dbo.Round_Steps_Mst_Tbl](#dboroundstepsmsttbl)
- [dbo.SQL_Monitoring](#dbosqlmonitoring)
- [dbo.SQL_Monitoring_Audit](#dbosqlmonitoringaudit)
- [dbo.Services_Monitoring](#dboservicesmonitoring)
- [dbo.Services_Monitoring_Audit](#dboservicesmonitoringaudit)
- [dbo.Station_Mst_Tbl](#dbostationmsttbl)
- [dbo.Station_Mst_Tbl_Audit](#dbostationmsttblaudit)
- [dbo.Storage_Monitoring](#dbostoragemonitoring)
- [dbo.Storage_Monitoring_Audit](#dbostoragemonitoringaudit)
- [dbo.Support_Executive_Mst_Tbl](#dbosupportexecutivemsttbl)
- [dbo.Support_Executive_Mst_Tbl_Audit](#dbosupportexecutivemsttblaudit)
- [dbo.SystemDetails](#dbosystemdetails)
- [dbo.SystemDetails_Audit](#dbosystemdetailsaudit)
- [dbo.System_Mst_Tbl](#dbosystemmsttbl)
- [dbo.System_Mst_Tbl_Audit](#dbosystemmsttblaudit)
- [dbo.TicketScheme_Mst_Tbl](#dboticketschememsttbl)
- [dbo.TicketScheme_Mst_Tbl_Audit](#dboticketschememsttblaudit)
- [dbo.UAT_ACCESSDENIAL](#dbouataccessdenial)
- [dbo.UAT_ACCESSDENIAL_Audit](#dbouataccessdenialaudit)
- [dbo.UAT_ALLOYADDITIONRECORD](#dbouatalloyadditionrecord)
- [dbo.UAT_ALLOYADDITIONRECORD_Audit](#dbouatalloyadditionrecordaudit)
- [dbo.UAT_AUDITTRAILLOGGING](#dbouataudittraillogging)
- [dbo.UAT_AUDITTRAILLOGGING_Audit](#dbouataudittrailloggingaudit)
- [dbo.UAT_AUTOCLOSE](#dbouatautoclose)
- [dbo.UAT_AUTOCLOSE_Audit](#dbouatautocloseaudit)
- [dbo.UAT_AUTOPRODUCTIONORDER](#dbouatautoproductionorder)
- [dbo.UAT_AUTOPRODUCTIONORDER_Audit](#dbouatautoproductionorderaudit)
- [dbo.UAT_AVAILABILITYPERSHIFT](#dbouatavailabilitypershift)
- [dbo.UAT_AVAILABILITYPERSHIFT_Audit](#dbouatavailabilitypershiftaudit)
- [dbo.UAT_BATTERYBANKANDDGSTATUSLOGSHEET](#dbouatbatterybankanddgstatuslogsheet)
- [dbo.UAT_BATTERYBANKANDDGSTATUSLOGSHEET_Audit](#dbouatbatterybankanddgstatuslogsheetaudit)
- [dbo.UAT_CAPACITORBANKLOGSHEET](#dbouatcapacitorbanklogsheet)
- [dbo.UAT_CAPACITORBANKLOGSHEET_Audit](#dbouatcapacitorbanklogsheetaudit)
- [dbo.UAT_CCM_CASTINGSPEEDPERSTRAND](#dbouatccmcastingspeedperstrand)
- [dbo.UAT_CCM_CASTINGSPEEDPERSTRAND_Audit](#dbouatccmcastingspeedperstrandaudit)
- [dbo.UAT_CCM_LADLEDETAILSLOGSHEET](#dbouatccmladledetailslogsheet)
- [dbo.UAT_CCM_LADLEDETAILSLOGSHEET_Audit](#dbouatccmladledetailslogsheetaudit)
- [dbo.UAT_CCM_LIVEDATADASHABORD](#dbouatccmlivedatadashabord)
- [dbo.UAT_CCM_LIVEDATADASHABORD_Audit](#dbouatccmlivedatadashabordaudit)
- [dbo.UAT_CCM_LOGBOOKDATADASHBOARD](#dbouatccmlogbookdatadashboard)
- [dbo.UAT_CCM_LOGBOOKDATADASHBOARD_Audit](#dbouatccmlogbookdatadashboardaudit)
- [dbo.UAT_CCM_MANUALENTRYLOGBOOK](#dbouatccmmanualentrylogbook)
- [dbo.UAT_CCM_MANUALENTRYLOGBOOK_Audit](#dbouatccmmanualentrylogbookaudit)
- [dbo.UAT_CCM_MANULENTRYLOGBOOK](#dbouatccmmanulentrylogbook)
- [dbo.UAT_CCM_MANULENTRYLOGBOOK_Audit](#dbouatccmmanulentrylogbookaudit)
- [dbo.UAT_CCM_NOOFBILETSPERHEAT](#dbouatccmnoofbiletsperheat)
- [dbo.UAT_CCM_NOOFBILETSPERHEAT_Audit](#dbouatccmnoofbiletsperheataudit)
- [dbo.UAT_CCM_OSCILLATIONPERSTRAND](#dbouatccmoscillationperstrand)
- [dbo.UAT_CCM_OSCILLATIONPERSTRAND_Audit](#dbouatccmoscillationperstrandaudit)
- [dbo.UAT_CCM_QUALITYDATADASHBOARD](#dbouatccmqualitydatadashboard)
- [dbo.UAT_CCM_QUALITYDATADASHBOARD_Audit](#dbouatccmqualitydatadashboardaudit)
- [dbo.UAT_CCM_SECTIONSTRANDSDATALOGSHEET](#dbouatccmsectionstrandsdatalogsheet)
- [dbo.UAT_CCM_SECTIONSTRANDSDATALOGSHEET_Audit](#dbouatccmsectionstrandsdatalogsheetaudit)
- [dbo.UAT_CCM_SHIFTPRODUCTIVITYREPORT](#dbouatccmshiftproductivityreport)
- [dbo.UAT_CCM_SHIFTPRODUCTIVITYREPORT_Audit](#dbouatccmshiftproductivityreportaudit)
- [dbo.UAT_CCM_SHIFTWISEDATADASHBOARD](#dbouatccmshiftwisedatadashboard)
- [dbo.UAT_CCM_SHIFTWISEDATADASHBOARD_Audit](#dbouatccmshiftwisedatadashboardaudit)
- [dbo.UAT_CCM_SHORTBILETSGENERATED](#dbouatccmshortbiletsgenerated)
- [dbo.UAT_CCM_SHORTBILETSGENERATED_Audit](#dbouatccmshortbiletsgeneratedaudit)
- [dbo.UAT_CCM_WATERFLOWZONEWISE](#dbouatccmwaterflowzonewise)
- [dbo.UAT_CCM_WATERFLOWZONEWISE_Audit](#dbouatccmwaterflowzonewiseaudit)
- [dbo.UAT_DELAYSPERSHIFT](#dbouatdelayspershift)
- [dbo.UAT_DELAYSPERSHIFT_Audit](#dbouatdelayspershiftaudit)
- [dbo.UAT_DUPLICATESIGNALHANDLING](#dbouatduplicatesignalhandling)
- [dbo.UAT_DUPLICATESIGNALHANDLING_Audit](#dbouatduplicatesignalhandlingaudit)
- [dbo.UAT_EAFTOLRFHEATTRANSFER](#dbouateaftolrfheattransfer)
- [dbo.UAT_EAFTOLRFHEATTRANSFER_Audit](#dbouateaftolrfheattransferaudit)
- [dbo.UAT_EAF_CONSUMPTIONDATALOGSHEET](#dbouateafconsumptiondatalogsheet)
- [dbo.UAT_EAF_CONSUMPTIONDATALOGSHEET_Audit](#dbouateafconsumptiondatalogsheetaudit)
- [dbo.UAT_EAF_DELAYTYPEMASTERLOGBOOK](#dbouateafdelaytypemasterlogbook)
- [dbo.UAT_EAF_DELAYTYPEMASTERLOGBOOK_Audit](#dbouateafdelaytypemasterlogbookaudit)
- [dbo.UAT_EAF_ELECTRODECONSUMPTIONPERHEAT](#dbouateafelectrodeconsumptionperheat)
- [dbo.UAT_EAF_ELECTRODECONSUMPTIONPERHEAT_Audit](#dbouateafelectrodeconsumptionperheataudit)
- [dbo.UAT_EAF_LADLEADDITIONLOGSHEET](#dbouateafladleadditionlogsheet)
- [dbo.UAT_EAF_LADLEADDITIONLOGSHEET_Audit](#dbouateafladleadditionlogsheetaudit)
- [dbo.UAT_EAF_LADLEDETAILSLOGSHEET](#dbouateafladledetailslogsheet)
- [dbo.UAT_EAF_LADLEDETAILSLOGSHEET_Audit](#dbouateafladledetailslogsheetaudit)
- [dbo.UAT_EAF_LIVEDATADASHBOARD](#dbouateaflivedatadashboard)
- [dbo.UAT_EAF_LIVEDATADASHBOARD_Audit](#dbouateaflivedatadashboardaudit)
- [dbo.UAT_EAF_LOGBOOKDATADASHBOARD](#dbouateaflogbookdatadashboard)
- [dbo.UAT_EAF_LOGBOOKDATADASHBOARD_Audit](#dbouateaflogbookdatadashboardaudit)
- [dbo.UAT_EAF_MANUALENTRYLOGBOOK](#dbouateafmanualentrylogbook)
- [dbo.UAT_EAF_MANUALENTRYLOGBOOK_Audit](#dbouateafmanualentrylogbookaudit)
- [dbo.UAT_EAF_NGCONSUMPTIONPERTON](#dbouateafngconsumptionperton)
- [dbo.UAT_EAF_NGCONSUMPTIONPERTON_Audit](#dbouateafngconsumptionpertonaudit)
- [dbo.UAT_EAF_NOOFHEAT](#dbouateafnoofheat)
- [dbo.UAT_EAF_NOOFHEAT_Audit](#dbouateafnoofheataudit)
- [dbo.UAT_EAF_POWERPERTON_1](#dbouateafpowerperton1)
- [dbo.UAT_EAF_POWERPERTON_1_Audit](#dbouateafpowerperton1audit)
- [dbo.UAT_EAF_QUALITYDATADASHBOARD](#dbouateafqualitydatadashboard)
- [dbo.UAT_EAF_QUALITYDATADASHBOARD_Audit](#dbouateafqualitydatadashboardaudit)
- [dbo.UAT_EAF_QUALITYDATALOGSHEET](#dbouateafqualitydatalogsheet)
- [dbo.UAT_EAF_QUALITYDATALOGSHEET_Audit](#dbouateafqualitydatalogsheetaudit)
- [dbo.UAT_EAF_REACTORLOGSHEET](#dbouateafreactorlogsheet)
- [dbo.UAT_EAF_REACTORLOGSHEET_Audit](#dbouateafreactorlogsheetaudit)
- [dbo.UAT_EAF_SHIFTDELAYENTRYLOGBOOK](#dbouateafshiftdelayentrylogbook)
- [dbo.UAT_EAF_SHIFTDELAYENTRYLOGBOOK_Audit](#dbouateafshiftdelayentrylogbookaudit)
- [dbo.UAT_EAF_SHIFTWISEDATADASHBOARD](#dbouateafshiftwisedatadashboard)
- [dbo.UAT_EAF_SHIFTWISEDATADASHBOARD_Audit](#dbouateafshiftwisedatadashboardaudit)
- [dbo.UAT_EAF_TRANSFORMERLOGSHEET](#dbouateaftransformerlogsheet)
- [dbo.UAT_EAF_TRANSFORMERLOGSHEET_Audit](#dbouateaftransformerlogsheetaudit)
- [dbo.UAT_EAF_YIELDPERHEAT](#dbouateafyieldperheat)
- [dbo.UAT_EAF_YIELDPERHEAT_Audit](#dbouateafyieldperheataudit)
- [dbo.UAT_ELECTRICALCHECKLISTREPORTS](#dbouatelectricalchecklistreports)
- [dbo.UAT_ELECTRICALCHECKLISTREPORTS_Audit](#dbouatelectricalchecklistreportsaudit)
- [dbo.UAT_ELECTRICAL_A_SHIFTCHECKLIST](#dbouatelectricalashiftchecklist)
- [dbo.UAT_ELECTRICAL_A_SHIFTCHECKLIST_Audit](#dbouatelectricalashiftchecklistaudit)
- [dbo.UAT_ELECTRICAL_B_SHIFTCHECKLIST](#dbouatelectricalbshiftchecklist)
- [dbo.UAT_ELECTRICAL_B_SHIFTCHECKLIST_Audit](#dbouatelectricalbshiftchecklistaudit)
- [dbo.UAT_EVENTCHRONOLOGYCHECK](#dbouateventchronologycheck)
- [dbo.UAT_EVENTCHRONOLOGYCHECK_Audit](#dbouateventchronologycheckaudit)
- [dbo.UAT_HEATSUMMARYREPORT](#dbouatheatsummaryreport)
- [dbo.UAT_HEATSUMMARYREPORT_Audit](#dbouatheatsummaryreportaudit)
- [dbo.UAT_HISTORICALDATAACCURACY](#dbouathistoricaldataaccuracy)
- [dbo.UAT_HISTORICALDATAACCURACY_Audit](#dbouathistoricaldataaccuracyaudit)
- [dbo.UAT_INTERSTAGEDELAY](#dbouatinterstagedelay)
- [dbo.UAT_INTERSTAGEDELAY_Audit](#dbouatinterstagedelayaudit)
- [dbo.UAT_KPIDASHBOARDREFRESH](#dbouatkpidashboardrefresh)
- [dbo.UAT_KPIDASHBOARDREFRESH_Audit](#dbouatkpidashboardrefreshaudit)
- [dbo.UAT_LADLECHANGE](#dbouatladlechange)
- [dbo.UAT_LADLECHANGE_Audit](#dbouatladlechangeaudit)
- [dbo.UAT_LOGSEETSREPORT](#dbouatlogseetsreport)
- [dbo.UAT_LOGSEETSREPORT_Audit](#dbouatlogseetsreportaudit)
- [dbo.UAT_LOGSHEETSREPORT](#dbouatlogsheetsreport)
- [dbo.UAT_LOGSHEETSREPORT_Audit](#dbouatlogsheetsreportaudit)
- [dbo.UAT_LRF_ALLOYADDITION](#dbouatlrfalloyaddition)
- [dbo.UAT_LRF_ALLOYADDITION_Audit](#dbouatlrfalloyadditionaudit)
- [dbo.UAT_LRF_ARCINGTIMEPERHEAT](#dbouatlrfarcingtimeperheat)
- [dbo.UAT_LRF_ARCINGTIMEPERHEAT_Audit](#dbouatlrfarcingtimeperheataudit)
- [dbo.UAT_LRF_ELECTRODECONSUMPTION](#dbouatlrfelectrodeconsumption)
- [dbo.UAT_LRF_ELECTRODECONSUMPTION_Audit](#dbouatlrfelectrodeconsumptionaudit)
- [dbo.UAT_LRF_LADLELIFETRACKING](#dbouatlrfladlelifetracking)
- [dbo.UAT_LRF_LADLELIFETRACKING_Audit](#dbouatlrfladlelifetrackingaudit)
- [dbo.UAT_LRF_LIVEDATADAHSBOARD](#dbouatlrflivedatadahsboard)
- [dbo.UAT_LRF_LIVEDATADAHSBOARD_Audit](#dbouatlrflivedatadahsboardaudit)
- [dbo.UAT_LRF_LOGBOOKDATADASHBOARD](#dbouatlrflogbookdatadashboard)
- [dbo.UAT_LRF_LOGBOOKDATADASHBOARD_Audit](#dbouatlrflogbookdatadashboardaudit)
- [dbo.UAT_LRF_MANUALENTRYLOGBOOK](#dbouatlrfmanualentrylogbook)
- [dbo.UAT_LRF_MANUALENTRYLOGBOOK_Audit](#dbouatlrfmanualentrylogbookaudit)
- [dbo.UAT_LRF_QUALITYDATALOGSHEET](#dbouatlrfqualitydatalogsheet)
- [dbo.UAT_LRF_QUALITYDATALOGSHEET_Audit](#dbouatlrfqualitydatalogsheetaudit)
- [dbo.UAT_LRF_SHIFTWISEDATADASHBOARD](#dbouatlrfshiftwisedatadashboard)
- [dbo.UAT_LRF_SHIFTWISEDATADASHBOARD_Audit](#dbouatlrfshiftwisedatadashboardaudit)
- [dbo.UAT_LRF_TEMPERATUREKPIS](#dbouatlrftemperaturekpis)
- [dbo.UAT_LRF_TEMPERATUREKPIS_Audit](#dbouatlrftemperaturekpisaudit)
- [dbo.UAT_LRF_TRANSFORMERLOGSHEET](#dbouatlrftransformerlogsheet)
- [dbo.UAT_LRF_TRANSFORMERLOGSHEET_Audit](#dbouatlrftransformerlogsheetaudit)
- [dbo.UAT_LRF_qUALITYDATADASHBOARD](#dbouatlrfqualitydatadashboard)
- [dbo.UAT_LRF_qUALITYDATADASHBOARD_Audit](#dbouatlrfqualitydatadashboardaudit)
- [dbo.UAT_MANUALOVERRIDEOFEVENT](#dbouatmanualoverrideofevent)
- [dbo.UAT_MANUALOVERRIDEOFEVENT_Audit](#dbouatmanualoverrideofeventaudit)
- [dbo.UAT_MANUALPOCREATION](#dbouatmanualpocreation)
- [dbo.UAT_MANUALPOCREATION_Audit](#dbouatmanualpocreationaudit)
- [dbo.UAT_MISSINGSIGNALHANDLING](#dbouatmissingsignalhandling)
- [dbo.UAT_MISSINGSIGNALHANDLING_Audit](#dbouatmissingsignalhandlingaudit)
- [dbo.UAT_POAUTOCREATION](#dbouatpoautocreation)
- [dbo.UAT_POAUTOCREATION_Audit](#dbouatpoautocreationaudit)
- [dbo.UAT_POFIELDVALIDATION](#dbouatpofieldvalidation)
- [dbo.UAT_POFIELDVALIDATION_Audit](#dbouatpofieldvalidationaudit)
- [dbo.UAT_POWERCONSUMPTIONCHARTMETERWISE](#dbouatpowerconsumptionchartmeterwise)
- [dbo.UAT_POWERCONSUMPTIONCHARTMETERWISE_Audit](#dbouatpowerconsumptionchartmeterwiseaudit)
- [dbo.UAT_POWERCONSUMPTIONLOGSHEET](#dbouatpowerconsumptionlogsheet)
- [dbo.UAT_POWERCONSUMPTIONLOGSHEET_Audit](#dbouatpowerconsumptionlogsheetaudit)
- [dbo.UAT_POWERCONSUMPTIONREPORTLOGSHEET](#dbouatpowerconsumptionreportlogsheet)
- [dbo.UAT_POWERCONSUMPTIONREPORTLOGSHEET_Audit](#dbouatpowerconsumptionreportlogsheetaudit)
- [dbo.UAT_RAWMATERIAL](#dbouatrawmaterial)
- [dbo.UAT_RAWMATERIAL_Audit](#dbouatrawmaterialaudit)
- [dbo.UAT_REALTIMEDASHBOARD](#dbouatrealtimedashboard)
- [dbo.UAT_REALTIMEDASHBOARD_Audit](#dbouatrealtimedashboardaudit)
- [dbo.UAT_ROLEBASEDFIELDEDIT](#dbouatrolebasedfieldedit)
- [dbo.UAT_ROLEBASEDFIELDEDIT_Audit](#dbouatrolebasedfieldeditaudit)
- [dbo.UAT_SCRAPCHARGING](#dbouatscrapcharging)
- [dbo.UAT_SCRAPCHARGING_Audit](#dbouatscrapchargingaudit)
- [dbo.UAT_SHIFTDELAYREPORT](#dbouatshiftdelayreport)
- [dbo.UAT_SHIFTDELAYREPORT_Audit](#dbouatshiftdelayreportaudit)
- [dbo.UAT_SMS_LIVEDATADASHBOARD](#dbouatsmslivedatadashboard)
- [dbo.UAT_SMS_LIVEDATADASHBOARD_Audit](#dbouatsmslivedatadashboardaudit)
- [dbo.UAT_SMS_PLANTDASHBOARD](#dbouatsmsplantdashboard)
- [dbo.UAT_SMS_PLANTDASHBOARD_Audit](#dbouatsmsplantdashboardaudit)
- [dbo.UAT_SMS_PLANTPROCESSTIME](#dbouatsmsplantprocesstime)
- [dbo.UAT_SMS_PLANTPROCESSTIME_Audit](#dbouatsmsplantprocesstimeaudit)
- [dbo.UAT_TRANSFORMER125MVA](#dbouattransformer125mva)
- [dbo.UAT_TRANSFORMER125MVA_Audit](#dbouattransformer125mvaaudit)
- [dbo.UAT_TRANSFORMER15MVALOGSHEET](#dbouattransformer15mvalogsheet)
- [dbo.UAT_TRANSFORMER15MVALOGSHEET_Audit](#dbouattransformer15mvalogsheetaudit)
- [dbo.UAT_TRANSFORMER24MVA](#dbouattransformer24mva)
- [dbo.UAT_TRANSFORMER24MVA_Audit](#dbouattransformer24mvaaudit)
- [dbo.UAT_TRANSFORMER63MVA](#dbouattransformer63mva)
- [dbo.UAT_TRANSFORMER63MVA_Audit](#dbouattransformer63mvaaudit)
- [dbo.UAT_TRANSFORMER6_6KVLOGSHEET](#dbouattransformer66kvlogsheet)
- [dbo.UAT_TRANSFORMER6_6KVLOGSHEET_Audit](#dbouattransformer66kvlogsheetaudit)
- [dbo.UAT_Test_Mst_Tbl](#dbouattestmsttbl)
- [dbo.UAT_Test_Report_Data](#dbouattestreportdata)
- [dbo.UAT_Tracking_Transaction](#dbouattrackingtransaction)
- [dbo.UserDetails](#dbouserdetails)
- [dbo.VM_Monitoring](#dbovmmonitoring)
- [dbo.VM_Monitoring_Audit](#dbovmmonitoringaudit)
- [dbo.XStudio_Alarm_Viewer_Filter_Mst_Tbl](#dboxstudioalarmviewerfiltermsttbl)
- [dbo.XStudio_Shift_Dtl_Tbl](#dboxstudioshiftdtltbl)
- [dbo.XStudio_Shift_Mst_Tbl](#dboxstudioshiftmsttbl)
- [dbo.priority_mst](#dboprioritymst)
- [dbo.subarea](#dbosubarea)
- [dbo.subarea_Audit](#dbosubareaaudit)
- [dbo.subareadetails](#dbosubareadetails)
- [dbo.subareadetails_Audit](#dbosubareadetailsaudit)
- [dbo.systemreferencedocuments](#dbosystemreferencedocuments)
- [dbo.systemreferencedocuments_Audit](#dbosystemreferencedocumentsaudit)


## Summary

| Table | Columns | Rows | Primary Key |
| --- | ---: | ---: | --- |
| dbo.Area_Mst_Tbl | 20 | 9 | ID |
| dbo.Area_Mst_Tbl_Audit | 16 | 0 | — |
| dbo.Asset_Hierarchy_Mst_Tbl | 15 | 0 | ID |
| dbo.Backup_Monitoring | 17 | 0 | ID |
| dbo.Backup_Monitoring_Audit | 17 | 0 | — |
| dbo.CentralDispatch_Mst_Tbl | 14 | 67 | ID |
| dbo.CentralDispatch_Mst_Tbl_Audit | 14 | 0 | — |
| dbo.CommonErrors | 15 | 8 | ID |
| dbo.CommonErrors_Audit | 15 | 0 | — |
| dbo.ComplaintType_Mst_Tbl | 14 | 8 | ID |
| dbo.ComplaintType_Mst_Tbl_Audit | 14 | 0 | — |
| dbo.Complaint_Mst_Tbl | 42 | 242 | ID |
| dbo.Complaint_Mst_Tbl_Audit | 36 | 0 | — |
| dbo.ControlRoom_Mst_Tbl | 14 | 1 | ID |
| dbo.ControlRoom_Mst_Tbl_Audit | 14 | 0 | — |
| dbo.DLBMonitoring | 15 | 76 | ID |
| dbo.DLBMonitoring_Audit | 15 | 30 | — |
| dbo.Equipment_Type_Mst_Tbl | 24 | 0 | ID |
| dbo.Events_Monitoring | 26 | 62 | ID |
| dbo.Events_Monitoring_Audit | 26 | 13 | — |
| dbo.FCM_Monitoring | 22 | 449 | ID |
| dbo.FCM_Monitoring_Audit | 22 | 11 | — |
| dbo.FCM_Node_Monitoring | 16 | 906 | ID |
| dbo.Folder_Monitoring | 15 | 938 | ID |
| dbo.Folder_Monitoring_Audit | 15 | 43 | — |
| dbo.HOD_Mst_Tbl | 15 | 0 | ID |
| dbo.HOD_Mst_Tbl_Audit | 15 | 0 | — |
| dbo.Hardware_Monitoring | 46 | 73 | ID |
| dbo.Hardware_Monitoring_Audit | 46 | 25 | — |
| dbo.Hermes_L2_Response_Trn_Tbl | 32 | 79 | — |
| dbo.Hermes_L2_SQL_Action_Trn_Tbl | 26 | 16 | — |
| dbo.HyperV_Monitoring | 20 | 234 | ID |
| dbo.HyperV_Monitoring_Audit | 20 | 7 | — |
| dbo.Import_Export | 20 | 10 | ID |
| dbo.MonitoringReport | 18 | 14 | ID |
| dbo.Organization_Mst_Tbl | 14 | 1 | ID |
| dbo.Pipeline_Mst_Tbl | 14 | 43 | ID |
| dbo.Pipeline_Mst_Tbl_Audit | 14 | 0 | — |
| dbo.PowerGenerationOutput | 24 | 0 | ID |
| dbo.PowerGenerationOutput_Audit | 24 | 0 | — |
| dbo.Procedure_Mst_Tbl | 18 | 0 | ID |
| dbo.Procedure_Steps_Mst_Tbl | 18 | 0 | ID |
| dbo.Procedure_Task_Mst_Tbl | 19 | 0 | ID |
| dbo.Region_Mst_Tbl | 13 | 5 | ID |
| dbo.Region_Mst_Tbl_Audit | 13 | 0 | — |
| dbo.Replica_Monitoring | 19 | 456 | ID |
| dbo.Round_Mst_Tbl | 18 | 0 | ID |
| dbo.Round_Steps_Mst_Tbl | 24 | 0 | ID |
| dbo.SQL_Monitoring | 16 | 67 | ID |
| dbo.SQL_Monitoring_Audit | 16 | 11 | — |
| dbo.Services_Monitoring | 26 | 66 | ID |
| dbo.Services_Monitoring_Audit | 26 | 79 | — |
| dbo.Station_Mst_Tbl | 15 | 169 | ID |
| dbo.Station_Mst_Tbl_Audit | 15 | 0 | — |
| dbo.Storage_Monitoring | 18 | 6,264 | ID |
| dbo.Storage_Monitoring_Audit | 18 | 78 | — |
| dbo.Support_Executive_Mst_Tbl | 15 | 0 | ID |
| dbo.Support_Executive_Mst_Tbl_Audit | 15 | 0 | — |
| dbo.SystemDetails | 16 | 157 | ID |
| dbo.SystemDetails_Audit | 16 | 0 | — |
| dbo.System_Mst_Tbl | 16 | 160 | ID |
| dbo.System_Mst_Tbl_Audit | 16 | 0 | — |
| dbo.TicketScheme_Mst_Tbl | 14 | 2 | ID |
| dbo.TicketScheme_Mst_Tbl_Audit | 14 | 0 | — |
| dbo.UAT_ACCESSDENIAL | 27 | 0 | ID |
| dbo.UAT_ACCESSDENIAL_Audit | 27 | 0 | — |
| dbo.UAT_ALLOYADDITIONRECORD | 27 | 0 | ID |
| dbo.UAT_ALLOYADDITIONRECORD_Audit | 27 | 0 | — |
| dbo.UAT_AUDITTRAILLOGGING | 27 | 0 | ID |
| dbo.UAT_AUDITTRAILLOGGING_Audit | 27 | 0 | — |
| dbo.UAT_AUTOCLOSE | 27 | 0 | ID |
| dbo.UAT_AUTOCLOSE_Audit | 27 | 0 | — |
| dbo.UAT_AUTOPRODUCTIONORDER | 27 | 0 | ID |
| dbo.UAT_AUTOPRODUCTIONORDER_Audit | 27 | 0 | — |
| dbo.UAT_AVAILABILITYPERSHIFT | 27 | 3 | ID |
| dbo.UAT_AVAILABILITYPERSHIFT_Audit | 27 | 0 | — |
| dbo.UAT_BATTERYBANKANDDGSTATUSLOGSHEET | 27 | 3 | ID |
| dbo.UAT_BATTERYBANKANDDGSTATUSLOGSHEET_Audit | 27 | 0 | — |
| dbo.UAT_CAPACITORBANKLOGSHEET | 27 | 3 | ID |
| dbo.UAT_CAPACITORBANKLOGSHEET_Audit | 27 | 0 | — |
| dbo.UAT_CCM_CASTINGSPEEDPERSTRAND | 27 | 5 | ID |
| dbo.UAT_CCM_CASTINGSPEEDPERSTRAND_Audit | 27 | 0 | — |
| dbo.UAT_CCM_LADLEDETAILSLOGSHEET | 27 | 4 | ID |
| dbo.UAT_CCM_LADLEDETAILSLOGSHEET_Audit | 27 | 0 | — |
| dbo.UAT_CCM_LIVEDATADASHABORD | 27 | 5 | ID |
| dbo.UAT_CCM_LIVEDATADASHABORD_Audit | 27 | 0 | — |
| dbo.UAT_CCM_LOGBOOKDATADASHBOARD | 27 | 4 | ID |
| dbo.UAT_CCM_LOGBOOKDATADASHBOARD_Audit | 27 | 0 | — |
| dbo.UAT_CCM_MANUALENTRYLOGBOOK | 27 | 3 | ID |
| dbo.UAT_CCM_MANUALENTRYLOGBOOK_Audit | 27 | 0 | — |
| dbo.UAT_CCM_MANULENTRYLOGBOOK | 27 | 0 | ID |
| dbo.UAT_CCM_MANULENTRYLOGBOOK_Audit | 27 | 0 | — |
| dbo.UAT_CCM_NOOFBILETSPERHEAT | 27 | 5 | ID |
| dbo.UAT_CCM_NOOFBILETSPERHEAT_Audit | 27 | 0 | — |
| dbo.UAT_CCM_OSCILLATIONPERSTRAND | 27 | 5 | ID |
| dbo.UAT_CCM_OSCILLATIONPERSTRAND_Audit | 27 | 0 | — |
| dbo.UAT_CCM_QUALITYDATADASHBOARD | 27 | 3 | ID |
| dbo.UAT_CCM_QUALITYDATADASHBOARD_Audit | 27 | 0 | — |
| dbo.UAT_CCM_SECTIONSTRANDSDATALOGSHEET | 27 | 3 | ID |
| dbo.UAT_CCM_SECTIONSTRANDSDATALOGSHEET_Audit | 27 | 0 | — |
| dbo.UAT_CCM_SHIFTPRODUCTIVITYREPORT | 27 | 3 | ID |
| dbo.UAT_CCM_SHIFTPRODUCTIVITYREPORT_Audit | 27 | 0 | — |
| dbo.UAT_CCM_SHIFTWISEDATADASHBOARD | 27 | 4 | ID |
| dbo.UAT_CCM_SHIFTWISEDATADASHBOARD_Audit | 27 | 0 | — |
| dbo.UAT_CCM_SHORTBILETSGENERATED | 27 | 3 | ID |
| dbo.UAT_CCM_SHORTBILETSGENERATED_Audit | 27 | 0 | — |
| dbo.UAT_CCM_WATERFLOWZONEWISE | 27 | 4 | ID |
| dbo.UAT_CCM_WATERFLOWZONEWISE_Audit | 27 | 0 | — |
| dbo.UAT_DELAYSPERSHIFT | 27 | 6 | ID |
| dbo.UAT_DELAYSPERSHIFT_Audit | 27 | 0 | — |
| dbo.UAT_DUPLICATESIGNALHANDLING | 27 | 0 | ID |
| dbo.UAT_DUPLICATESIGNALHANDLING_Audit | 27 | 0 | — |
| dbo.UAT_EAFTOLRFHEATTRANSFER | 27 | 5 | ID |
| dbo.UAT_EAFTOLRFHEATTRANSFER_Audit | 27 | 0 | — |
| dbo.UAT_EAF_CONSUMPTIONDATALOGSHEET | 27 | 3 | ID |
| dbo.UAT_EAF_CONSUMPTIONDATALOGSHEET_Audit | 27 | 0 | — |
| dbo.UAT_EAF_DELAYTYPEMASTERLOGBOOK | 27 | 3 | ID |
| dbo.UAT_EAF_DELAYTYPEMASTERLOGBOOK_Audit | 27 | 0 | — |
| dbo.UAT_EAF_ELECTRODECONSUMPTIONPERHEAT | 27 | 4 | ID |
| dbo.UAT_EAF_ELECTRODECONSUMPTIONPERHEAT_Audit | 27 | 0 | — |
| dbo.UAT_EAF_LADLEADDITIONLOGSHEET | 27 | 4 | ID |
| dbo.UAT_EAF_LADLEADDITIONLOGSHEET_Audit | 27 | 0 | — |
| dbo.UAT_EAF_LADLEDETAILSLOGSHEET | 27 | 3 | ID |
| dbo.UAT_EAF_LADLEDETAILSLOGSHEET_Audit | 27 | 0 | — |
| dbo.UAT_EAF_LIVEDATADASHBOARD | 27 | 10 | ID |
| dbo.UAT_EAF_LIVEDATADASHBOARD_Audit | 27 | 0 | — |
| dbo.UAT_EAF_LOGBOOKDATADASHBOARD | 27 | 3 | ID |
| dbo.UAT_EAF_LOGBOOKDATADASHBOARD_Audit | 27 | 0 | — |
| dbo.UAT_EAF_MANUALENTRYLOGBOOK | 27 | 3 | ID |
| dbo.UAT_EAF_MANUALENTRYLOGBOOK_Audit | 27 | 0 | — |
| dbo.UAT_EAF_NGCONSUMPTIONPERTON | 27 | 3 | ID |
| dbo.UAT_EAF_NGCONSUMPTIONPERTON_Audit | 27 | 0 | — |
| dbo.UAT_EAF_NOOFHEAT | 27 | 7 | ID |
| dbo.UAT_EAF_NOOFHEAT_Audit | 27 | 0 | — |
| dbo.UAT_EAF_POWERPERTON_1 | 27 | 5 | ID |
| dbo.UAT_EAF_POWERPERTON_1_Audit | 27 | 0 | — |
| dbo.UAT_EAF_QUALITYDATADASHBOARD | 27 | 3 | ID |
| dbo.UAT_EAF_QUALITYDATADASHBOARD_Audit | 27 | 0 | — |
| dbo.UAT_EAF_QUALITYDATALOGSHEET | 27 | 3 | ID |
| dbo.UAT_EAF_QUALITYDATALOGSHEET_Audit | 27 | 0 | — |
| dbo.UAT_EAF_REACTORLOGSHEET | 27 | 3 | ID |
| dbo.UAT_EAF_REACTORLOGSHEET_Audit | 27 | 0 | — |
| dbo.UAT_EAF_SHIFTDELAYENTRYLOGBOOK | 27 | 3 | ID |
| dbo.UAT_EAF_SHIFTDELAYENTRYLOGBOOK_Audit | 27 | 0 | — |
| dbo.UAT_EAF_SHIFTWISEDATADASHBOARD | 27 | 5 | ID |
| dbo.UAT_EAF_SHIFTWISEDATADASHBOARD_Audit | 27 | 0 | — |
| dbo.UAT_EAF_TRANSFORMERLOGSHEET | 27 | 5 | ID |
| dbo.UAT_EAF_TRANSFORMERLOGSHEET_Audit | 27 | 0 | — |
| dbo.UAT_EAF_YIELDPERHEAT | 27 | 5 | ID |
| dbo.UAT_EAF_YIELDPERHEAT_Audit | 27 | 0 | — |
| dbo.UAT_ELECTRICALCHECKLISTREPORTS | 29 | 4 | ID |
| dbo.UAT_ELECTRICALCHECKLISTREPORTS_Audit | 29 | 0 | — |
| dbo.UAT_ELECTRICAL_A_SHIFTCHECKLIST | 27 | 7 | ID |
| dbo.UAT_ELECTRICAL_A_SHIFTCHECKLIST_Audit | 27 | 0 | — |
| dbo.UAT_ELECTRICAL_B_SHIFTCHECKLIST | 27 | 4 | ID |
| dbo.UAT_ELECTRICAL_B_SHIFTCHECKLIST_Audit | 27 | 0 | — |
| dbo.UAT_EVENTCHRONOLOGYCHECK | 27 | 0 | ID |
| dbo.UAT_EVENTCHRONOLOGYCHECK_Audit | 27 | 0 | — |
| dbo.UAT_HEATSUMMARYREPORT | 27 | 0 | ID |
| dbo.UAT_HEATSUMMARYREPORT_Audit | 27 | 0 | — |
| dbo.UAT_HISTORICALDATAACCURACY | 29 | 4 | ID |
| dbo.UAT_HISTORICALDATAACCURACY_Audit | 29 | 0 | — |
| dbo.UAT_INTERSTAGEDELAY | 27 | 0 | ID |
| dbo.UAT_INTERSTAGEDELAY_Audit | 27 | 0 | — |
| dbo.UAT_KPIDASHBOARDREFRESH | 27 | 0 | ID |
| dbo.UAT_KPIDASHBOARDREFRESH_Audit | 27 | 0 | — |
| dbo.UAT_LADLECHANGE | 27 | 0 | ID |
| dbo.UAT_LADLECHANGE_Audit | 27 | 0 | — |
| dbo.UAT_LOGSEETSREPORT | 27 | 0 | ID |
| dbo.UAT_LOGSEETSREPORT_Audit | 27 | 0 | — |
| dbo.UAT_LOGSHEETSREPORT | 29 | 4 | ID |
| dbo.UAT_LOGSHEETSREPORT_Audit | 29 | 0 | — |
| dbo.UAT_LRF_ALLOYADDITION | 29 | 5 | ID |
| dbo.UAT_LRF_ALLOYADDITION_Audit | 29 | 0 | — |
| dbo.UAT_LRF_ARCINGTIMEPERHEAT | 27 | 5 | ID |
| dbo.UAT_LRF_ARCINGTIMEPERHEAT_Audit | 27 | 0 | — |
| dbo.UAT_LRF_ELECTRODECONSUMPTION | 27 | 2 | ID |
| dbo.UAT_LRF_ELECTRODECONSUMPTION_Audit | 27 | 0 | — |
| dbo.UAT_LRF_LADLELIFETRACKING | 27 | 3 | ID |
| dbo.UAT_LRF_LADLELIFETRACKING_Audit | 27 | 0 | — |
| dbo.UAT_LRF_LIVEDATADAHSBOARD | 27 | 6 | ID |
| dbo.UAT_LRF_LIVEDATADAHSBOARD_Audit | 27 | 0 | — |
| dbo.UAT_LRF_LOGBOOKDATADASHBOARD | 27 | 3 | ID |
| dbo.UAT_LRF_LOGBOOKDATADASHBOARD_Audit | 27 | 0 | — |
| dbo.UAT_LRF_MANUALENTRYLOGBOOK | 27 | 3 | ID |
| dbo.UAT_LRF_MANUALENTRYLOGBOOK_Audit | 27 | 0 | — |
| dbo.UAT_LRF_QUALITYDATALOGSHEET | 27 | 3 | ID |
| dbo.UAT_LRF_QUALITYDATALOGSHEET_Audit | 27 | 0 | — |
| dbo.UAT_LRF_SHIFTWISEDATADASHBOARD | 27 | 3 | ID |
| dbo.UAT_LRF_SHIFTWISEDATADASHBOARD_Audit | 27 | 0 | — |
| dbo.UAT_LRF_TEMPERATUREKPIS | 27 | 3 | ID |
| dbo.UAT_LRF_TEMPERATUREKPIS_Audit | 27 | 0 | — |
| dbo.UAT_LRF_TRANSFORMERLOGSHEET | 27 | 3 | ID |
| dbo.UAT_LRF_TRANSFORMERLOGSHEET_Audit | 27 | 0 | — |
| dbo.UAT_LRF_qUALITYDATADASHBOARD | 27 | 3 | ID |
| dbo.UAT_LRF_qUALITYDATADASHBOARD_Audit | 27 | 0 | — |
| dbo.UAT_MANUALOVERRIDEOFEVENT | 27 | 0 | ID |
| dbo.UAT_MANUALOVERRIDEOFEVENT_Audit | 27 | 0 | — |
| dbo.UAT_MANUALPOCREATION | 27 | 0 | ID |
| dbo.UAT_MANUALPOCREATION_Audit | 27 | 0 | — |
| dbo.UAT_MISSINGSIGNALHANDLING | 27 | 0 | ID |
| dbo.UAT_MISSINGSIGNALHANDLING_Audit | 27 | 0 | — |
| dbo.UAT_POAUTOCREATION | 27 | 0 | ID |
| dbo.UAT_POAUTOCREATION_Audit | 27 | 0 | — |
| dbo.UAT_POFIELDVALIDATION | 27 | 0 | ID |
| dbo.UAT_POFIELDVALIDATION_Audit | 27 | 0 | — |
| dbo.UAT_POWERCONSUMPTIONCHARTMETERWISE | 27 | 3 | ID |
| dbo.UAT_POWERCONSUMPTIONCHARTMETERWISE_Audit | 27 | 0 | — |
| dbo.UAT_POWERCONSUMPTIONLOGSHEET | 27 | 3 | ID |
| dbo.UAT_POWERCONSUMPTIONLOGSHEET_Audit | 27 | 0 | — |
| dbo.UAT_POWERCONSUMPTIONREPORTLOGSHEET | 27 | 3 | ID |
| dbo.UAT_POWERCONSUMPTIONREPORTLOGSHEET_Audit | 27 | 0 | — |
| dbo.UAT_RAWMATERIAL | 27 | 0 | ID |
| dbo.UAT_RAWMATERIAL_Audit | 27 | 0 | — |
| dbo.UAT_REALTIMEDASHBOARD | 27 | 5 | ID |
| dbo.UAT_REALTIMEDASHBOARD_Audit | 27 | 0 | — |
| dbo.UAT_ROLEBASEDFIELDEDIT | 27 | 0 | ID |
| dbo.UAT_ROLEBASEDFIELDEDIT_Audit | 27 | 0 | — |
| dbo.UAT_SCRAPCHARGING | 27 | 0 | ID |
| dbo.UAT_SCRAPCHARGING_Audit | 27 | 0 | — |
| dbo.UAT_SHIFTDELAYREPORT | 27 | 0 | ID |
| dbo.UAT_SHIFTDELAYREPORT_Audit | 27 | 0 | — |
| dbo.UAT_SMS_LIVEDATADASHBOARD | 27 | 5 | ID |
| dbo.UAT_SMS_LIVEDATADASHBOARD_Audit | 27 | 0 | — |
| dbo.UAT_SMS_PLANTDASHBOARD | 27 | 5 | ID |
| dbo.UAT_SMS_PLANTDASHBOARD_Audit | 27 | 0 | — |
| dbo.UAT_SMS_PLANTPROCESSTIME | 27 | 3 | ID |
| dbo.UAT_SMS_PLANTPROCESSTIME_Audit | 27 | 0 | — |
| dbo.UAT_TRANSFORMER125MVA | 27 | 4 | ID |
| dbo.UAT_TRANSFORMER125MVA_Audit | 27 | 0 | — |
| dbo.UAT_TRANSFORMER15MVALOGSHEET | 27 | 3 | ID |
| dbo.UAT_TRANSFORMER15MVALOGSHEET_Audit | 27 | 0 | — |
| dbo.UAT_TRANSFORMER24MVA | 27 | 3 | ID |
| dbo.UAT_TRANSFORMER24MVA_Audit | 27 | 0 | — |
| dbo.UAT_TRANSFORMER63MVA | 27 | 6 | ID |
| dbo.UAT_TRANSFORMER63MVA_Audit | 27 | 0 | — |
| dbo.UAT_TRANSFORMER6_6KVLOGSHEET | 27 | 3 | ID |
| dbo.UAT_TRANSFORMER6_6KVLOGSHEET_Audit | 27 | 0 | — |
| dbo.UAT_Test_Mst_Tbl | 23 | 87 | ID |
| dbo.UAT_Test_Report_Data | 25 | 683 | ID |
| dbo.UAT_Tracking_Transaction | 21 | 257 | ID |
| dbo.UserDetails | 14 | 0 | ID |
| dbo.VM_Monitoring | 20 | 67 | ID |
| dbo.VM_Monitoring_Audit | 20 | 4 | — |
| dbo.XStudio_Alarm_Viewer_Filter_Mst_Tbl | 26 | 0 | ID |
| dbo.XStudio_Shift_Dtl_Tbl | 17 | 0 | ID |
| dbo.XStudio_Shift_Mst_Tbl | 16 | 0 | ID |
| dbo.priority_mst | 14 | 3 | ID |
| dbo.subarea | 15 | 19 | ID |
| dbo.subarea_Audit | 15 | 0 | — |
| dbo.subareadetails | 15 | 0 | ID |
| dbo.subareadetails_Audit | 15 | 0 | — |
| dbo.systemreferencedocuments | 21 | 12 | ID |
| dbo.systemreferencedocuments_Audit | 21 | 0 | — |

---



## Detailed Table Information



## dbo.Area_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 9  
**Date Range (ModifiedOn):** 2025-08-11 12:27:07 to 2025-10-13 13:15:02  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| icon | varchar | YES | 200 | — |
| Organizationid | varchar | YES | 36 | — |
| SrNo | int | YES | 10,0 | — |
| AssetIdentificationProperties | varchar | YES | -1 | — |
| ShiftID | varchar | YES | 36 | — |
| RoleIDList | varchar | YES | -1 | — |
| IsHandoverEnabled | bit | YES | — | — |

### Top 10 Records

| ID | Name | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5FF54C4A-067F-49D8-80E9-5F4236B03947 | EAF | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-11 11:47:12 | 2025-08-11 12:27:07 | False | False | NULL | 10.2.18.42 |
| 27D51105-BEE2-48FD-8AB8-8ADAD48DE71C | LRF | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-11 16:22:53 | 2025-08-11 12:27:11 | False | False | NULL | 10.2.18.42 |
| B88E9146-D9DC-46D1-A46D-FC30CB5312DF | CCM | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-11 17:22:53 | 2025-08-11 12:27:16 | False | False | NULL | 10.2.18.42 |
| 5640FCDC-B42D-4F06-967A-706709A73231 | Common | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-06 12:31:24 | 2025-08-11 12:27:21 | False | False | NULL | 10.2.18.42 |
| BD31E350-6456-4B52-ABE5-F5412246AEA5 | Billet Yard | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-10-13 13:13:28 | 2025-10-13 13:13:28 | False | False | NULL | 172.16.3.201 |
| B6CA0FEE-8E52-4897-B076-C9D5128D9889 | Reheating Furnace | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-10-13 13:13:47 | 2025-10-13 13:13:47 | False | False | NULL | 172.16.3.201 |
| 6AFF2AB8-59FC-4403-B685-7CC270C5A6E3 | Rolling Mill Stands | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-10-13 13:14:20 | 2025-10-13 13:14:20 | False | False | NULL | 172.16.3.201 |
| 4588225B-FF06-49C4-B3E4-19411225287F | WRM | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-10-13 13:14:35 | 2025-10-13 13:14:35 | False | False | NULL | 172.16.3.201 |
| 06611EED-455C-470E-9F41-5952DE77E780 | Rebar | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-10-13 13:15:02 | 2025-10-13 13:15:02 | False | False | NULL | 172.16.3.201 |

---


## dbo.Area_Mst_Tbl_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| icon | varchar | YES | 200 | — |
| Organizationid | varchar | YES | 36 | — |
| SrNo | int | YES | 10,0 | — |

---


## dbo.Asset_Hierarchy_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| SerialNumber | int | YES | 10,0 | — |

---


## dbo.Backup_Monitoring

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| CurrentDate | date | YES | — | — |
| SubfolderName | varchar | YES | 100 | — |
| FullBackupCount | int | YES | 10,0 | — |
| DifferentialCount | int | YES | 10,0 | — |
| TransactionCount | int | YES | 10,0 | — |

---


## dbo.Backup_Monitoring_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| CurrentDate | date | YES | — | — |
| SubfolderName | varchar | YES | 100 | — |
| FullBackupCount | int | YES | 10,0 | — |
| DifferentialCount | int | YES | 10,0 | — |
| TransactionCount | int | YES | 10,0 | — |

---


## dbo.CentralDispatch_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 67  
**Date Range (ModifiedOn):** 2022-08-10 14:45:20 to 2023-09-01 18:40:37  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| PipelineID | varchar | YES | 360 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |

### Top 10 Records

| ID | Name | PipelineID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DA5DD6C1-0C4C-4CBD-809E-E95AF73F3119 | fack | 02E3BE17-32C6-4A49-B775-9493865F166C | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 14:45:12 | 2022-08-10 14:45:20 | True | False | NULL |
| 4BD6ACCD-2F4C-4079-840F-B7465D659436 | fack | 02E3BE17-32C6-4A49-B775-9493865F166C,03C3B671-21EC-426F-9934-FA171CED7DD4,04A4457F-3B12-4144-936A... | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 14:55:07 | 2022-08-10 15:15:00 | True | False | NULL |
| 97D129CD-D391-441B-ADD9-385ACD8ABBA0 | fack | 02E3BE17-32C6-4A49-B775-9493865F166C,03C3B671-21EC-426F-9934-FA171CED7DD4,04A4457F-3B12-4144-936A... | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 15:17:25 | 2022-08-10 15:24:45 | True | False | NULL |
| 356D79B0-F6AE-4239-A30B-6027D5D057EE | test | 02E3BE17-32C6-4A49-B775-9493865F166C | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 15:18:47 | 2022-08-10 15:24:47 | True | False | NULL |
| 4103A41A-7978-48BF-887A-C78C94C74912 | Barauni CD | 3702BEA5-58DA-4345-9F9D-090FBC6549E7 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 12:30:00 | 2022-08-10 15:29:26 | True | False | NULL |
| 5F39FC52-0182-414A-AECD-DEC00E05E92D | Manali CD | E95BF60D-0A37-4A18-B480-C3DC23FBA4C3 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 12:23:40 | 2022-08-10 15:29:28 | True | False | NULL |
| 2943F8D9-1D3D-4168-819E-FF9A7DDA9900 | Manali CD | BBD23078-B5D3-4066-A31A-1F6BF61FCE58 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 12:26:30 | 2022-08-10 15:29:30 | True | False | NULL |
| 7E351AEE-06EF-4784-98A7-528532A66541 | Guwahati CD | 03C3B671-21EC-426F-9934-FA171CED7DD4 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 12:30:21 | 2022-08-10 15:30:34 | True | False | NULL |
| 4E67F184-6664-49E3-B16B-0CA75953B33F | Haldia | 24940C73-3EA9-431E-838F-52893C987AD9 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 12:25:45 | 2022-08-10 15:30:36 | True | False | NULL |
| 694CB04F-B921-47F0-8E06-92680871B1F6 | Haldia | 875F51DC-453F-4651-B2F4-60E31F9E76F5 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 12:26:59 | 2022-08-10 15:30:38 | True | False | NULL |

### Bottom 10 Records

| ID | Name | PipelineID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 35A7D34B-B058-4DE8-B699-BE69B7A5321D | Paradip | FFC1A040-FFA5-4004-B8BA-9ED0955CF30A | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-09-01 17:36:39 | 2023-09-01 18:40:37 | True | False | NULL |
| 1E5EF7C0-FF23-49CF-B565-3A05460DF254 | Paradip CD PHBMPL | 9B9C1EA5-0ADB-4D16-91FE-C2957F88290D | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 5FE97C53-D3CA-4ABA-B52C-C1A8AE3934EF | 2022-08-10 16:01:48 | 2023-04-11 15:35:49 | False | False | NULL |
| B03A4A3B-7902-4403-B45A-151FDA29D140 | Paradip CD PSHPL | FFC1A040-FFA5-4004-B8BA-9ED0955CF30A | 5FE97C53-D3CA-4ABA-B52C-C1A8AE3934EF | 5FE97C53-D3CA-4ABA-B52C-C1A8AE3934EF | 2023-03-20 16:18:25 | 2023-03-20 16:18:25 | False | False | NULL |
| 56B69ACA-7E2F-4D9B-BB14-87362306A29A | Koyali CD | 48190ADE-3F5D-4D08-B475-D2442A149A8A | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-03-18 11:51:31 | 2023-03-18 11:51:31 | False | False | NULL |
| AB6D8E75-7DAF-41FD-A8AA-384F75AB4549 | Paradip | 5D257561-9F88-4CCA-82A7-3C327531F770 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 5FE97C53-D3CA-4ABA-B52C-C1A8AE3934EF | 2022-09-27 14:59:18 | 2022-12-27 16:29:27 | False | False | NULL |
| C87D7D30-BD44-4DC9-8FC9-89680E705E72 | Panipat_Product_CD | 2F5FEC4C-2EC0-4AC4-92AF-B4CBCBD98A06 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2022-12-24 12:31:28 | 2022-12-24 12:31:28 | False | False | NULL |
| CE84F35C-4ACE-4D0C-AB27-4CFC45630A8B | Panipat_Product_CD | BB4D41FC-F354-4687-BF8A-7FB2E8B118A3 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2022-12-24 12:31:12 | 2022-12-24 12:31:12 | False | False | NULL |
| 23AF6EBE-9BB6-4AEA-871E-695CA3C74B4F | Panipat_Product_CD | 83B9FC3B-2931-4753-8E94-2A48F9227A75 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2022-12-24 12:30:50 | 2022-12-24 12:30:50 | False | False | NULL |
| 6AA891F8-3801-4D93-8754-D3808E0F3FA8 | Panipat_Product_CD | 811FA18C-ABD5-4D5C-BA60-8498DEF6CB7D | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2022-12-24 12:30:29 | 2022-12-24 12:30:29 | False | False | NULL |
| C2154523-08EF-463D-9F5F-16872CE8765E | Panipat_Product_CD | 8E448FCF-5517-4404-975D-E8EF2C784ABE | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2022-12-20 11:22:34 | 2022-12-24 12:29:02 | False | False | NULL |

---


## dbo.CentralDispatch_Mst_Tbl_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| PipelineID | varchar | YES | 360 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |

---


## dbo.CommonErrors

**Primary Key:** ID  
**Row Count:** 8  
**Date Range (ModifiedOn):** 2022-08-12 13:46:17 to 2022-08-12 13:48:20  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| subarea | varchar | YES | -1 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DAAD071F-539E-4C7A-9DCB-7E83E3DC2E59 | Add Button Not Visible | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-12 13:46:17 | 2022-08-12 13:46:17 | False | False | NULL |
| 92947097-C7ED-4640-B66A-1E2C8564C1CE | Data Not Reflected After Saving | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-12 13:46:46 | 2022-08-12 13:46:46 | False | False | NULL |
| E2B78E59-9B10-4567-9B39-C290AA64FFCB | Unable to access using iDRAC | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-12 13:47:08 | 2022-08-12 13:47:08 | False | False | NULL |
| 679F3233-F2C5-41B6-8FEB-129733EAE4C8 | Record Not Found Error | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-12 13:47:24 | 2022-08-12 13:47:24 | False | False | NULL |
| 9382E58C-F3C8-4F68-B97B-6ACDED88AC6E | Unable to access using iDRAC | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-12 13:47:35 | 2022-08-12 13:47:35 | False | False | NULL |
| 6AEB33EA-383A-467D-A39B-415FCA038101 | WiFi Not Working | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-12 13:47:51 | 2022-08-12 13:47:51 | False | False | NULL |
| 1CA396F0-5065-4D71-9B03-9536B1FA2166 | Application Not Opening After Version Update | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-12 13:48:05 | 2022-08-12 13:48:05 | False | False | NULL |
| 47C79F35-9CE6-44A8-8D1E-013A64E754DD | Device Not Charging | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-12 13:48:20 | 2022-08-12 13:48:20 | False | False | NULL |

---


## dbo.CommonErrors_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| subarea | varchar | YES | -1 | — |

---


## dbo.ComplaintType_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 8  
**Date Range (ModifiedOn):** 2022-08-12 13:22:51 to 2025-08-06 11:36:37  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| subarea | varchar | YES | -1 | — |

### Top 10 Records

| ID | Name | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7DB6EE18-8D76-4A1C-B53C-417C5FA1A321 | Suggestion | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-12 12:32:28 | 2022-08-12 13:22:51 | False | False | NULL | 192.168.11.143 |
| D560B7EE-94EA-4D18-93DC-CCB24859D30D | Repeat Complaint | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-07-30 22:27:06 | 2022-08-12 13:23:07 | True | False | NULL | 192.168.11.143 |
| FFA57FDA-AF44-4335-8992-583DD7E88133 | New | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-07-30 22:27:38 | 2022-08-12 13:23:12 | True | False | NULL | 192.168.11.143 |
| 70CB56EB-7D94-4529-B06D-1C28ECE2ECDA | Request for Customization | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-12 12:32:49 | 2022-09-22 12:03:55 | False | False | NULL | 10.20.65.184 |
| 37CA8AAA-81F3-40D6-8380-F57147A75A5B | Clarification or Doubt | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 5FE97C53-D3CA-4ABA-B52C-C1A8AE3934EF | 2022-08-12 12:32:38 | 2022-12-06 16:39:32 | False | False | NULL | 10.20.65.184 |
| 78357479-E66C-4818-959F-B0990A312266 | Request For Customization Rights | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | 2023-04-18 11:14:37 | 2025-08-06 10:50:02 | True | False | NULL | 10.2.20.160 |
| 910C8925-5F72-41D5-AB8C-9FAF6C864DC3 | UAT Failures | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | 2022-08-12 12:32:22 | 2025-08-06 11:36:32 | False | False | NULL | 10.2.20.160 |
| 814B4EAF-547F-4FBE-8444-3A8DC96AE20D | Bug | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | 2025-08-06 11:36:37 | 2025-08-06 11:36:37 | False | False | NULL | 10.2.20.160 |

---


## dbo.ComplaintType_Mst_Tbl_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| subarea | varchar | YES | -1 | — |

---


## dbo.Complaint_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 242  
**Date Range (ModifiedOn):** 2025-08-11 16:49:36 to 2026-09-02 15:41:22  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| AreaID | varchar | YES | 200 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| ComplaintTypeID | varchar | YES | -1 | — |
| Description | varchar | YES | -1 | — |
| BriefDetails | varchar | YES | 500 | — |
| Solution | varchar | YES | -1 | — |
| Status | varchar | YES | 50 | — |
| TicketNo | varchar | YES | 100 | — |
| Attachment | varchar | YES | 8000 | — |
| Priority | varchar | YES | -1 | — |
| RepeatTicketNo | varchar | YES | 7999 | — |
| commonerror | varchar | YES | -1 | — |
| subareadetails | varchar | YES | 36 | — |
| repeat | bit | YES | — | — |
| FirstLastName | varchar | YES | 100 | — |
| ContactNo | varchar | YES | 100 | — |
| EmailID | varchar | YES | 100 | — |
| ssmmessage | varchar | YES | -1 | — |
| Soharmessage | varchar | YES | -1 | — |
| messages | varchar | YES | 50 | — |
| SupportExecutiveRemarks | varchar | YES | -1 | — |
| ServerName | varchar | YES | -1 | — |
| AskRemarks | varchar | YES | -1 | — |
| ReplyRemarks | varchar | YES | -1 | — |
| AskStatus | varchar | YES | 50 | — |
| ProblemCategory | varchar | YES | 100 | — |
| SourceSystem | varchar | YES | 100 | — |
| ConversationSummary | nvarchar | YES | -1 | — |
| SuspectedCause | nvarchar | YES | -1 | — |
| ExtractedEntitiesJson | nvarchar | YES | -1 | — |
| ConversationLogJson | nvarchar | YES | -1 | — |

### Top 10 Records

| ID | AreaID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0F4239EF-7507-425A-AEDD-812C1018EB72 | LRF | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | NULL | 2026-09-02 15:25:19 | NULL | False | False | NULL | NULL |
| 209C9084-5A3B-4BFA-ADF6-51D6D288A79D | EAF | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | NULL | 2026-09-02 13:51:30 | NULL | False | False | NULL | NULL |
| 2CA8D413-8507-4F4D-89C4-645B1EA1260D | CCM | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | NULL | 2026-09-02 18:54:32 | NULL | False | False | NULL | NULL |
| 5F279691-2E90-4899-B72A-470099E87912 | CCM | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | NULL | 2026-09-02 15:25:19 | NULL | False | False | NULL | NULL |
| 67615469-526C-4806-A26E-6CBEAD930AAD | CCM | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | NULL | 2026-09-02 18:54:32 | NULL | False | False | NULL | NULL |
| 679DCA6B-DCAD-41AE-B295-626258B25CB6 | Rolling Mill Stands | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | NULL | 2026-09-02 15:25:19 | NULL | False | False | NULL | NULL |
| 79F1DE89-B15E-4F1E-8F96-25E42A2C7D5E | Common | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | NULL | 2026-09-02 15:25:19 | NULL | False | False | NULL | NULL |
| 7BA71367-0348-44B8-8719-90A1D6CBFCF3 | CCM | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | NULL | 2026-09-02 18:54:32 | NULL | False | False | NULL | NULL |
| 7C316CED-8967-424A-B7F8-AD0BBC55021E | CCM | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | NULL | 2026-09-02 18:54:32 | NULL | False | False | NULL | NULL |
| 7C73354A-F5A8-4D82-ACF6-F20B5193334B | Common | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | NULL | 2026-09-02 15:40:13 | NULL | False | False | NULL | NULL |

### Bottom 10 Records

| ID | AreaID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 56782340-C44E-4F46-8447-4A9D14669583 | Common | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | NULL | 2026-09-02 15:40:13 | 2026-09-02 15:41:22 | False | False | NULL | NULL |
| 7038E619-D3AD-4DFD-8D56-78DC0C4B8092 | Common | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | NULL | 2026-09-02 15:40:13 | 2026-09-02 15:41:21 | False | False | NULL | NULL |
| E8DF09F6-4EF4-4BC1-AD9F-BCFB30E09C5C | Common | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | NULL | 2026-09-02 15:40:13 | 2026-09-02 15:41:21 | False | False | NULL | NULL |
| 6F8C03D6-D135-480A-BE66-CC810F17EC6F | EAF | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-02-08 16:13:16 | 2026-09-02 15:22:45 | False | False | NULL |  |
| 274BFA51-AF52-429E-9AFD-51A66DC7C5A6 | CCM | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-02-03 17:02:27 | 2026-09-02 15:12:52 | False | False | NULL |  |
| 1B1E794A-A779-4471-A5E7-FE4AF7D5ACFD | Common | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-02-03 12:51:53 | 2026-09-02 15:02:59 | False | False | NULL |  |
| D1D6620C-1222-4DD3-984A-F028753EEBBF | Common | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-01-28 15:29:58 | 2026-09-02 14:53:23 | False | False | NULL | 10.76.5.122 |
| 9E16FB49-3D75-4719-996D-D973F91E63E9 | Common | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-01-28 15:09:18 | 2026-09-02 14:44:34 | False | False | NULL | 10.76.5.122 |
| 91813D74-6CF6-4077-A51A-699CC6BE2062 | Common | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-02-08 17:43:04 | 2026-09-02 14:17:03 | False | False | NULL |  |
| 43C246E7-ADDD-4D0F-900B-41F4674D5DD7 | Common | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-02-08 17:08:37 | 2026-09-02 14:07:58 | False | False | NULL |  |

---


## dbo.Complaint_Mst_Tbl_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | YES | 36 | (newid()) |
| AreaID | varchar | YES | 200 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| ComplaintTypeID | varchar | YES | -1 | — |
| Description | varchar | YES | -1 | — |
| BriefDetails | varchar | YES | 500 | — |
| Solution | varchar | YES | -1 | — |
| Status | varchar | YES | 50 | — |
| TicketNo | varchar | YES | 100 | — |
| Attachment | varchar | YES | 8000 | — |
| Priority | varchar | YES | -1 | — |
| RepeatTicketNo | varchar | YES | 7999 | — |
| commonerror | varchar | YES | -1 | — |
| subareadetails | varchar | YES | 36 | — |
| repeat | bit | YES | — | — |
| FirstLastName | varchar | YES | 100 | — |
| ContactNo | varchar | YES | 100 | — |
| EmailID | varchar | YES | 100 | — |
| ssmmessage | varchar | YES | -1 | — |
| Soharmessage | varchar | YES | -1 | — |
| messages | varchar | YES | 50 | — |
| SupportExecutiveRemarks | varchar | YES | -1 | — |
| ServerName | varchar | YES | -1 | — |
| AskRemarks | varchar | YES | -1 | — |
| ReplyRemarks | varchar | YES | -1 | — |
| AskStatus | varchar | YES | 50 | — |

---


## dbo.ControlRoom_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2022-12-06 16:39:56 to 2022-12-06 16:39:56  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| SystemID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |

### Top 10 Records

| ID | Name | SystemID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 39C8E856-A754-41E2-B52E-1B2018243F9B | Paradip | 9FC3F185-6C3B-4C11-8CA3-41E14C50F82A | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 5FE97C53-D3CA-4ABA-B52C-C1A8AE3934EF | 2022-09-19 13:48:48 | 2022-12-06 16:39:56 | False | False | NULL |

---


## dbo.ControlRoom_Mst_Tbl_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| SystemID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |

---


## dbo.DLBMonitoring

**Primary Key:** ID  
**Row Count:** 76  
**Date Range (ModifiedOn):** 2023-04-07 13:43:03 to 2025-05-11 01:05:07  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| TicketNo | int | YES | 10,0 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Entrydatetime | datetime | YES | — | — |
| Remarks | varchar | YES | -1 | — |

### Top 10 Records

| ID | TicketNo | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 50F41A4B-D2E0-4871-9059-A62663EF8E06 | 4 | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-07 13:43:03 | 2023-04-07 13:43:03 | False | False | NULL | 10.54.25.77 |
| 70C23700-983F-451F-85CD-1857710A7D53 | 1 | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-07 09:25:22 | 2023-04-07 16:20:16 | True | False | NULL | 10.20.88.4 |
| FD1FEA9B-37AF-464B-9111-8FA6F2EF966E | 2 | 80534764-F53E-4106-81A8-D86849F6E75C | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-07 11:35:38 | 2023-04-07 16:20:19 | True | False | NULL | 10.20.88.4 |
| 0C5ABCA4-CA8C-436D-84DD-945E8E5C5FBF | 3 | 80534764-F53E-4106-81A8-D86849F6E75C | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-07 12:50:57 | 2023-04-07 16:20:23 | True | False | NULL | 10.20.88.4 |
| 0C2EC874-7748-40A5-84EF-380CE3964D2C | 5 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-04-08 10:07:11 | 2023-04-08 10:07:11 | False | False | NULL | 10.20.88.4 |
| E8455E67-11BF-4B76-B52A-1D7FF8C7956E | 6 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-10 09:44:40 | 2023-04-10 09:44:40 | False | False | NULL | 10.54.25.77 |
| 3FA889F2-9476-49F8-A8CC-9CFD16FDE396 | 7 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-11 10:41:32 | 2023-04-11 10:41:32 | False | False | NULL | 10.20.88.4 |
| 590F69D8-9EF9-4E24-8C6D-DBB9F5A3582F | 8 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-12 10:13:13 | 2023-04-12 10:13:13 | False | False | NULL | 10.20.65.186 |
| 96FCFD29-D268-48FC-A21B-59EFF906C653 | 9 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-13 10:23:05 | 2023-04-13 10:23:05 | False | False | NULL | 10.54.25.77 |
| C34AFF69-2B0B-4D06-AE9C-C2F4E7BF6D0C | 10 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-14 09:33:58 | 2023-04-14 09:33:58 | False | False | NULL | 10.54.25.77 |

### Bottom 10 Records

| ID | TicketNo | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7C86DFA8-242F-4758-B263-20D89560DCDE | 64 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-11 01:05:07 | 2025-05-11 01:05:07 | False | False | NULL | 10.20.65.239 |
| DCA1ACD5-94C4-4BD0-9E9F-DE0FB8203439 | 63 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-07-13 12:23:52 | 2023-07-13 12:23:52 | False | False | NULL | 10.20.79.108 |
| E630D763-579B-4476-8207-FB858ADFAC85 | 62 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-07-04 10:10:40 | 2023-07-04 10:10:40 | False | False | NULL | 10.20.79.9 |
| B5021435-5B6A-44D8-AF2E-499F12DF5B4D | 61 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-07-03 10:13:01 | 2023-07-03 10:13:01 | False | False | NULL | 10.20.79.9 |
| CE5EF93E-761D-4E48-8A3C-28D2F1C06A19 | 60 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-30 11:42:08 | 2023-06-30 11:42:08 | False | False | NULL | 10.20.79.9 |
| 30451152-A13B-4FCF-908F-6D8590EC9145 | 59 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-28 09:32:40 | 2023-06-28 09:32:40 | False | False | NULL | 10.20.79.9 |
| 46DEF245-B8E8-464D-892F-D41B007B4EC0 | 58 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-06-26 09:12:27 | 2023-06-26 09:12:27 | False | False | NULL | 10.20.65.186 |
| 52347E61-7A6D-4D84-B379-904665BE01AE | 57 | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-06-23 09:27:47 | 2023-06-23 09:27:47 | False | False | NULL | 10.20.88.4 |
| 847F91E6-B5DB-4582-B6A7-356BD176842E | 56 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-22 13:45:12 | 2023-06-22 13:45:12 | False | False | NULL | 10.20.79.108 |
| 1DB085FA-6C3A-4A50-A82E-64B0497CFC43 | 55 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-21 15:01:06 | 2023-06-21 15:01:06 | False | False | NULL | 10.20.79.9 |

---


## dbo.DLBMonitoring_Audit

**Primary Key:** —  
**Row Count:** 30  
**Date Range (ModifiedOn):** 2023-04-06 15:02:36 to 2023-06-10 09:10:18  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| TicketNo | int | YES | 10,0 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Entrydatetime | datetime | YES | — | — |
| Remarks | varchar | YES | -1 | — |

### Top 10 Records

| ID | TicketNo | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B8050131-69B8-43D3-8A9F-8A8C0A9DBFE9 | NULL | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-06 15:02:36 | 2023-04-06 15:02:36 | False | False | NULL | 10.20.88.4 |
| B8050131-69B8-43D3-8A9F-8A8C0A9DBFE9 | NULL | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-06 15:02:36 | 2023-04-06 15:16:19 | False | False | NULL | 10.20.88.4 |
| 24BD4E22-76EB-49FC-B204-2D30F23E6468 | NULL | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-06 15:16:30 | 2023-04-06 15:16:30 | False | False | NULL | 10.20.88.4 |
| 24BD4E22-76EB-49FC-B204-2D30F23E6468 | NULL | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-06 15:16:30 | 2023-04-06 15:37:02 | False | False | NULL | 10.20.88.4 |
| 31A4CF5A-716E-4000-97A6-A0ECF20CF7B9 | NULL | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-06 15:37:09 | 2023-04-06 15:37:09 | False | False | NULL | 10.20.88.4 |
| 24BD4E22-76EB-49FC-B204-2D30F23E6468 | NULL | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-06 15:16:30 | 2023-04-06 15:40:35 | False | False | NULL | 10.20.88.4 |
| 24BD4E22-76EB-49FC-B204-2D30F23E6468 | NULL | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-06 15:16:30 | 2023-04-06 15:41:19 | False | False | NULL | 10.20.88.4 |
| 24BD4E22-76EB-49FC-B204-2D30F23E6468 | NULL | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-06 15:16:30 | 2023-04-06 15:44:34 | False | False | NULL | 10.20.88.4 |
| 24BD4E22-76EB-49FC-B204-2D30F23E6468 | NULL | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-06 15:16:30 | 2023-04-06 16:00:45 | False | False | NULL | 10.20.88.4 |
| 24BD4E22-76EB-49FC-B204-2D30F23E6468 | 2 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-06 15:16:30 | 2023-04-06 16:00:45 | False | False | NULL | 10.20.88.4 |

### Bottom 10 Records

| ID | TicketNo | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B2B86546-D3B0-4845-B920-4A261F2C9BD2 | 46 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-06-10 09:10:18 | 2023-06-10 09:10:18 | False | False | NULL | 10.20.65.186 |
| 0C5ABCA4-CA8C-436D-84DD-945E8E5C5FBF | 3 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-07 12:50:57 | 2023-04-07 13:05:58 | False | False | NULL | 10.20.88.4 |
| 0C5ABCA4-CA8C-436D-84DD-945E8E5C5FBF | 3 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-07 12:50:57 | 2023-04-07 12:50:57 | False | False | NULL | 10.20.88.4 |
| FD1FEA9B-37AF-464B-9111-8FA6F2EF966E | 2 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-07 11:35:38 | 2023-04-07 11:35:38 | False | False | NULL | 10.20.88.4 |
| 70C23700-983F-451F-85CD-1857710A7D53 | 1 | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-07 09:25:22 | 2023-04-07 09:25:22 | False | False | NULL | 10.54.25.77 |
| 7E7F6B29-D82B-4A04-B7A4-FBE2CA1E03ED | 3 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-06 16:26:57 | 2023-04-06 16:26:57 | False | False | NULL | 10.20.88.4 |
| B4BA3FE3-16E8-4DD0-A65D-BB27005AF736 | 3 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-06 16:23:35 | 2023-04-06 16:23:35 | False | False | NULL | 10.20.88.4 |
| 21B48DC0-40B7-43E7-9705-BA79C2E73578 | 3 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-06 16:23:05 | 2023-04-06 16:23:05 | False | False | NULL | 10.20.88.4 |
| 3AF7EB4D-7F68-4BD1-B560-2BD8711ADD15 | NULL | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-06 16:19:39 | 2023-04-06 16:19:39 | False | False | NULL | 10.20.88.4 |
| 3AF7EB4D-7F68-4BD1-B560-2BD8711ADD15 | 1 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-06 16:19:39 | 2023-04-06 16:19:39 | False | False | NULL | 10.20.88.4 |

---


## dbo.Equipment_Type_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| GeneratePagesButton | varchar | YES | 100 | — |
| Frequency | varchar | YES | 36 | — |
| Icon | varchar | YES | 8000 | — |
| IsBatchingEntity | bit | YES | — | — |
| BatchingEquipmentClass | varchar | YES | 100 | — |
| Hierarchy | varchar | YES | 36 | — |
| IsEventCheck | bit | YES | — | — |
| BlockType | varchar | YES | 100 | — |
| DataSourceID | varchar | YES | 36 | — |
| IsHandoverEnabled | bit | YES | — | — |

---


## dbo.Events_Monitoring

**Primary Key:** ID  
**Row Count:** 62  
**Date Range (ModifiedOn):** 2023-04-07 16:17:53 to 2023-07-03 17:13:29  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| EntryDateTime | datetime | YES | — | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| ErrorLastHoursMessageCount | int | YES | 10,0 | — |
| ErrorLastHoursMessageImage | varchar | YES | -1 | — |
| ErrorLast24HoursMessageCount | int | YES | 10,0 | — |
| WarningLastHoursMessageCount | int | YES | 10,0 | — |
| WarningLastHoursMessageImage | varchar | YES | -1 | — |
| WarningLast24HoursMessageCount | int | YES | 10,0 | — |
| CriticalLastHoursMessageCount | int | YES | 10,0 | — |
| CriticalLastHoursMessageImage | varchar | YES | -1 | — |
| CriticalLast24HoursMessageCount | int | YES | 10,0 | — |
| ErrorLastHoursMessageRemarks | varchar | YES | 100 | — |
| WarningLastHoursMessageRemarks | varchar | YES | 100 | — |
| CriticalLastHoursMessageRemarks | varchar | YES | 100 | — |

### Top 10 Records

| ID | EntryDateTime | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 48030009-5535-4020-BA1E-45BCF47DAA97 | 2023-04-06 18:24:00 | NULL | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-06 18:25:14 | 2023-04-07 16:17:53 | True | False | NULL |
| EF8931A6-4A94-4D3F-80DD-51A59E162484 | 2023-04-08 17:51:00 | 0C2EC874-7748-40A5-84EF-380CE3964D2C | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-08 18:11:34 | 2023-04-08 18:11:34 | False | False | NULL |
| AFA0319F-6995-4955-AB04-497ABF4C1E13 | 2023-04-10 15:01:00 | E8455E67-11BF-4B76-B52A-1D7FF8C7956E | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-10 15:16:40 | 2023-04-10 15:16:39 | False | False | NULL |
| 20F64560-534C-4C95-B8FD-1EEE0CE5EC3D | 2023-04-11 10:58:00 | 3FA889F2-9476-49F8-A8CC-9CFD16FDE396 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-11 11:02:59 | 2023-04-11 11:02:59 | False | False | NULL |
| A949C5F0-7D3F-4654-92E1-DDA35174822C | 2023-04-13 15:23:00 | 96FCFD29-D268-48FC-A21B-59EFF906C653 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-13 15:46:41 | 2023-04-13 15:46:41 | False | False | NULL |
| A5C712BB-3AF9-47AB-8BB7-2CB5F5FC15A4 | 2023-04-14 09:34:00 | C34AFF69-2B0B-4D06-AE9C-C2F4E7BF6D0C | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-14 09:38:31 | 2023-04-14 09:38:31 | False | False | NULL |
| 583ABBB7-4F77-4A1B-8FD6-60E62F35EDB6 | 2023-04-15 09:41:00 | 15AA35F0-3A90-4C73-82CA-D12D5C7FD9BD | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-15 09:44:38 | 2023-04-15 09:44:38 | False | False | NULL |
| 3E16B124-A5E9-4BB1-871E-582C8C526BEC | 2023-04-17 10:30:00 | 0523710F-31BB-417C-A081-F73C0B158CB4 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-17 10:34:00 | 2023-04-17 10:33:59 | False | False | NULL |
| 7105460A-03E5-4503-9243-6B1C53218B37 | 2023-04-18 09:33:00 | 4CEE639C-248D-47B0-A9FE-63DA6CAE8462 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-18 09:35:48 | 2023-04-18 09:35:48 | False | False | NULL |
| 66164492-6F8C-449D-A985-7A21ED8A2AD1 | 2023-04-19 17:04:00 | 2369A5D1-0F94-42E6-91E7-214AD8BBEC7F | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-19 17:07:21 | 2023-04-19 17:07:21 | False | False | NULL |

### Bottom 10 Records

| ID | EntryDateTime | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F5BFCC9C-69D1-4763-8976-422C382200C2 | 2023-07-03 17:10:00 | B5021435-5B6A-44D8-AF2E-499F12DF5B4D | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-07-03 17:13:29 | 2023-07-03 17:13:29 | False | False | NULL |
| 10034771-F2CC-4900-88B8-4714CE8D52EE | 2023-06-30 17:02:00 | CE5EF93E-761D-4E48-8A3C-28D2F1C06A19 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-30 17:06:28 | 2023-06-30 17:06:28 | False | False | NULL |
| 8966ECFB-CEC2-467A-9472-A7D47AFBD551 | 2023-06-26 10:41:00 | 46DEF245-B8E8-464D-892F-D41B007B4EC0 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-26 10:45:53 | 2023-06-26 10:45:52 | False | False | NULL |
| 57B18842-E709-46CF-A18C-BD07BB9B137A | 2023-06-23 17:16:00 | 52347E61-7A6D-4D84-B379-904665BE01AE | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-23 17:22:00 | 2023-06-23 17:21:59 | False | False | NULL |
| DC81740D-398A-4DE1-9D7D-28E4D3608C51 | 2023-06-22 15:19:00 | 847F91E6-B5DB-4582-B6A7-356BD176842E | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-22 15:27:35 | 2023-06-22 15:27:35 | False | False | NULL |
| 6FF0EBB3-EDC1-4F4D-9F0D-6CA6F24884E5 | 2023-06-21 15:16:00 | 1DB085FA-6C3A-4A50-A82E-64B0497CFC43 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-21 15:23:24 | 2023-06-21 15:23:23 | False | False | NULL |
| F7FCE98C-722B-4DC9-81DD-6364F34DABB6 | 2023-06-20 17:01:00 | 80C40A12-92A1-47F5-9F1B-EBF1B4CED735 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-20 17:08:12 | 2023-06-20 17:08:12 | False | False | NULL |
| 4580E007-B424-4C8A-A178-72D8841C3BBF | 2023-06-19 16:43:00 | CEDBCADC-D841-49BE-8C12-CB35FC0E7A38 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-19 16:46:19 | 2023-06-19 16:46:19 | False | False | NULL |
| B9362736-7BA5-4E00-8D31-68F8635A0473 | 2023-06-17 11:08:00 | 994FDFCB-7EA2-449B-AF52-513AFA20C3E8 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-17 11:10:55 | 2023-06-17 11:10:55 | False | False | NULL |
| EFFDAA25-F430-446F-B9DA-5377B89AF45C | 2023-06-16 08:57:00 | 460CA49A-63DA-45FB-A556-53D09642AB8B | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-16 08:59:39 | 2023-06-16 09:00:37 | False | False | NULL |

---


## dbo.Events_Monitoring_Audit

**Primary Key:** —  
**Row Count:** 13  
**Date Range (ModifiedOn):** 2023-04-06 18:25:14 to 2023-06-16 08:59:39  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| EntryDateTime | datetime | YES | — | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| ErrorLastHoursMessageCount | int | YES | 10,0 | — |
| ErrorLastHoursMessageImage | varchar | YES | -1 | — |
| ErrorLast24HoursMessageCount | int | YES | 10,0 | — |
| WarningLastHoursMessageCount | int | YES | 10,0 | — |
| WarningLastHoursMessageImage | varchar | YES | -1 | — |
| WarningLast24HoursMessageCount | int | YES | 10,0 | — |
| CriticalLastHoursMessageCount | int | YES | 10,0 | — |
| CriticalLastHoursMessageImage | varchar | YES | -1 | — |
| CriticalLast24HoursMessageCount | int | YES | 10,0 | — |
| ErrorLastHoursMessageRemarks | varchar | YES | 100 | — |
| WarningLastHoursMessageRemarks | varchar | YES | 100 | — |
| CriticalLastHoursMessageRemarks | varchar | YES | 100 | — |

### Top 10 Records

| ID | EntryDateTime | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 48030009-5535-4020-BA1E-45BCF47DAA97 | 2023-04-06 18:24:00 | NULL | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-06 18:25:14 | 2023-04-06 18:25:14 | False | False | NULL |
| 8431EBEC-76D6-4AB7-B438-340A3B36A4AC | 2023-05-01 14:40:00 | B1A2671F-0449-404A-B9DC-F1C3716047E3 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-01 14:43:47 | 2023-05-01 14:43:47 | False | False | NULL |
| DB77830B-59D4-48E5-A6D8-6871EFDB6880 | 2023-05-02 09:17:00 | C38C2F4B-8FA7-494D-86A5-54CB637E78A5 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-02 09:22:33 | 2023-05-02 09:22:32 | False | False | NULL |
| D63E652D-154C-4123-8C24-E9DF452B6EC3 | 2023-05-05 16:33:00 | 46C87B54-01DC-40B4-B91D-DBC4BF60DCEF | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-05-05 16:39:12 | 2023-05-05 16:39:12 | False | False | NULL |
| EB605129-7D91-4A8F-A29B-9F1973CB2649 | 2023-05-20 09:57:00 | 1F679365-F508-4BAF-A98E-E09D131B8CD2 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-20 09:59:49 | 2023-05-20 09:59:49 | False | False | NULL |
| 46ED4CC1-20C9-4170-8DF1-A15743DC1482 | 2023-05-31 12:11:00 | 493ACBEE-8EFE-4276-A331-237A59B63AA5 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-31 12:13:07 | 2023-05-31 12:13:07 | False | False | NULL |
| 61BD09B7-2348-40E9-BD54-9FBE442B3AA8 | 2023-06-05 10:25:00 | 0B37ABEA-7F1B-410D-9E4B-B29F28652962 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-05 10:44:31 | 2023-06-05 10:44:31 | False | False | NULL |
| 342FA015-D3E9-4CF7-95FD-2610A30FB717 | 2023-06-07 09:05:00 | 6DDC8421-B2BE-400F-90F0-51AA3D435DD1 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-07 09:06:27 | 2023-06-07 09:06:27 | False | False | NULL |
| 342FA015-D3E9-4CF7-95FD-2610A30FB717 | 2023-06-07 09:05:00 | 6DDC8421-B2BE-400F-90F0-51AA3D435DD1 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-07 09:06:27 | 2023-06-07 09:07:40 | False | False | NULL |
| 2E7DD44B-254D-4B6A-B99E-013C67574D69 | 2023-06-07 09:08:00 | 6DDC8421-B2BE-400F-90F0-51AA3D435DD1 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-07 09:08:55 | 2023-06-07 09:08:55 | False | False | NULL |

### Bottom 10 Records

| ID | EntryDateTime | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EFFDAA25-F430-446F-B9DA-5377B89AF45C | 2023-06-16 08:57:00 | 460CA49A-63DA-45FB-A556-53D09642AB8B | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-16 08:59:39 | 2023-06-16 08:59:39 | False | False | NULL |
| 8AC14FCA-D162-416E-B9C1-45004A0AD4B0 | 2023-06-09 12:36:00 | 86D836D9-48EF-4626-BCBE-956841779329 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-09 12:38:55 | 2023-06-09 12:38:55 | False | False | NULL |
| 7E719FD6-8768-4548-ABA6-50FA8D2FB63E | 2023-06-08 08:59:00 | AD9A0692-2E18-499C-A685-C1D842A01C02 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-08 09:01:32 | 2023-06-08 09:01:31 | False | False | NULL |
| 2E7DD44B-254D-4B6A-B99E-013C67574D69 | 2023-06-07 09:08:00 | 6DDC8421-B2BE-400F-90F0-51AA3D435DD1 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-07 09:08:55 | 2023-06-07 09:08:55 | False | False | NULL |
| 342FA015-D3E9-4CF7-95FD-2610A30FB717 | 2023-06-07 09:05:00 | 6DDC8421-B2BE-400F-90F0-51AA3D435DD1 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-07 09:06:27 | 2023-06-07 09:07:40 | False | False | NULL |
| 342FA015-D3E9-4CF7-95FD-2610A30FB717 | 2023-06-07 09:05:00 | 6DDC8421-B2BE-400F-90F0-51AA3D435DD1 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-07 09:06:27 | 2023-06-07 09:06:27 | False | False | NULL |
| 61BD09B7-2348-40E9-BD54-9FBE442B3AA8 | 2023-06-05 10:25:00 | 0B37ABEA-7F1B-410D-9E4B-B29F28652962 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-05 10:44:31 | 2023-06-05 10:44:31 | False | False | NULL |
| 46ED4CC1-20C9-4170-8DF1-A15743DC1482 | 2023-05-31 12:11:00 | 493ACBEE-8EFE-4276-A331-237A59B63AA5 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-31 12:13:07 | 2023-05-31 12:13:07 | False | False | NULL |
| EB605129-7D91-4A8F-A29B-9F1973CB2649 | 2023-05-20 09:57:00 | 1F679365-F508-4BAF-A98E-E09D131B8CD2 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-20 09:59:49 | 2023-05-20 09:59:49 | False | False | NULL |
| D63E652D-154C-4123-8C24-E9DF452B6EC3 | 2023-05-05 16:33:00 | 46C87B54-01DC-40B4-B91D-DBC4BF60DCEF | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-05-05 16:39:12 | 2023-05-05 16:39:12 | False | False | NULL |

---


## dbo.FCM_Monitoring

**Primary Key:** ID  
**Row Count:** 449  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| DateTime | datetime | YES | — | — |
| ClusterName | varchar | YES | 100 | — |
| DiskName | varchar | YES | 100 | — |
| Path | varchar | YES | 100 | — |
| Size | varchar | YES | 100 | — |
| FreeSpace | varchar | YES | 100 | — |
| UsedSpace | varchar | YES | 100 | — |
| PercentFree | varchar | YES | 100 | — |
| State | varchar | YES | 100 | — |
| OwnerNode | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 056F3C35-2CB0-41BF-B30E-F338DDC6C397 | NULL | NULL | 2023-08-22 09:00:28 | NULL | False | False | NULL | NULL | NULL |
| 055AAF14-6B50-4A36-A669-050AD6044049 | NULL | NULL | 2024-05-20 09:00:04 | NULL | False | False | NULL | NULL | NULL |
| 05165332-6B79-4AF3-B775-4059F3817218 | NULL | NULL | 2024-07-15 09:00:03 | NULL | False | False | NULL | NULL | NULL |
| 046B5832-353B-4074-A1D3-D3258B315019 | NULL | NULL | 2023-10-25 09:01:11 | NULL | False | False | NULL | NULL | NULL |
| 044D1F4D-1671-4CF8-A11F-FE7F6988A488 | NULL | NULL | 2023-07-22 09:00:26 | NULL | False | False | NULL | NULL | NULL |
| 03AC1CE1-F1B2-4B35-9004-9553D7B47050 | NULL | NULL | 2024-04-29 09:00:02 | NULL | False | False | NULL | NULL | NULL |
| 02F7021F-D5F1-4B60-B2E3-7F9EF67AAF68 | NULL | NULL | 2024-06-20 09:00:02 | NULL | False | False | NULL | NULL | NULL |
| 023D6A3B-F5F8-4329-A23D-E31A2AC6B0BA | NULL | NULL | 2024-06-26 09:00:02 | NULL | False | False | NULL | NULL | NULL |
| 01317556-B87D-4476-AF04-51322005ED4F | NULL | NULL | 2024-04-16 09:00:05 | NULL | False | False | NULL | NULL | NULL |
| 01113452-0D42-459E-9FDC-0C1677809A14 | NULL | NULL | 2024-04-08 09:00:06 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 056F3C35-2CB0-41BF-B30E-F338DDC6C397 | NULL | NULL | 2023-08-22 09:00:28 | NULL | False | False | NULL | NULL | NULL |
| 055AAF14-6B50-4A36-A669-050AD6044049 | NULL | NULL | 2024-05-20 09:00:04 | NULL | False | False | NULL | NULL | NULL |
| 05165332-6B79-4AF3-B775-4059F3817218 | NULL | NULL | 2024-07-15 09:00:03 | NULL | False | False | NULL | NULL | NULL |
| 046B5832-353B-4074-A1D3-D3258B315019 | NULL | NULL | 2023-10-25 09:01:11 | NULL | False | False | NULL | NULL | NULL |
| 044D1F4D-1671-4CF8-A11F-FE7F6988A488 | NULL | NULL | 2023-07-22 09:00:26 | NULL | False | False | NULL | NULL | NULL |
| 03AC1CE1-F1B2-4B35-9004-9553D7B47050 | NULL | NULL | 2024-04-29 09:00:02 | NULL | False | False | NULL | NULL | NULL |
| 02F7021F-D5F1-4B60-B2E3-7F9EF67AAF68 | NULL | NULL | 2024-06-20 09:00:02 | NULL | False | False | NULL | NULL | NULL |
| 023D6A3B-F5F8-4329-A23D-E31A2AC6B0BA | NULL | NULL | 2024-06-26 09:00:02 | NULL | False | False | NULL | NULL | NULL |
| 01317556-B87D-4476-AF04-51322005ED4F | NULL | NULL | 2024-04-16 09:00:05 | NULL | False | False | NULL | NULL | NULL |
| 01113452-0D42-459E-9FDC-0C1677809A14 | NULL | NULL | 2024-04-08 09:00:06 | NULL | False | False | NULL | NULL | NULL |

---


## dbo.FCM_Monitoring_Audit

**Primary Key:** —  
**Row Count:** 11  
**Date Range (ModifiedOn):** 2023-04-21 11:53:58 to 2023-06-15 14:37:14  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| DateTime | datetime | YES | — | — |
| ClusterName | varchar | YES | 100 | — |
| DiskName | varchar | YES | 100 | — |
| Path | varchar | YES | 100 | — |
| Size | varchar | YES | 100 | — |
| FreeSpace | varchar | YES | 100 | — |
| UsedSpace | varchar | YES | 100 | — |
| PercentFree | varchar | YES | 100 | — |
| State | varchar | YES | 100 | — |
| OwnerNode | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4084F527-D78F-4EE5-BF1B-A905014AFA5D | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-21 11:53:59 | 2023-04-21 11:53:58 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 281D9EF8-2E14-41C5-A3DE-684575C31786 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-24 10:24:13 | 2023-04-24 10:24:13 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 281D9EF8-2E14-41C5-A3DE-684575C31786 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-24 10:24:13 | 2023-04-24 12:24:39 | False | False | NULL | 10.54.25.77 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| D7D223E4-76CA-41BD-96C1-DBC58CC82B4D | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-02 09:59:28 | 2023-05-02 09:59:28 | False | False | NULL | 10.54.25.77 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| D7D223E4-76CA-41BD-96C1-DBC58CC82B4D | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-02 09:59:28 | 2023-05-02 11:08:17 | False | False | NULL | 10.20.88.4 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| D7D223E4-76CA-41BD-96C1-DBC58CC82B4D | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-02 09:59:28 | 2023-05-02 11:26:55 | False | False | NULL | 10.20.88.4 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| D7D223E4-76CA-41BD-96C1-DBC58CC82B4D | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-02 09:59:28 | 2023-05-02 11:34:47 | False | False | NULL | 10.20.88.4 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 2A14FCCA-0ACF-424C-BF4F-6418590D74D7 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-23 17:32:30 | 2023-05-23 17:32:30 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 2A14FCCA-0ACF-424C-BF4F-6418590D74D7 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-23 17:32:30 | 2023-05-23 17:34:49 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 82F8D510-6B46-4C59-B89C-F5F08660CC9A | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-06-07 17:17:28 | 2023-06-07 17:17:28 | False | False | NULL | 10.20.88.4 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 99ED1E3F-968C-472B-A4AC-7E566DBFA788 | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-06-15 14:37:14 | 2023-06-15 14:37:14 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 82F8D510-6B46-4C59-B89C-F5F08660CC9A | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-06-07 17:17:28 | 2023-06-07 17:17:28 | False | False | NULL | 10.20.88.4 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 2A14FCCA-0ACF-424C-BF4F-6418590D74D7 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-23 17:32:30 | 2023-05-23 17:34:49 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 2A14FCCA-0ACF-424C-BF4F-6418590D74D7 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-23 17:32:30 | 2023-05-23 17:32:30 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| D7D223E4-76CA-41BD-96C1-DBC58CC82B4D | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-02 09:59:28 | 2023-05-02 11:34:47 | False | False | NULL | 10.20.88.4 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| D7D223E4-76CA-41BD-96C1-DBC58CC82B4D | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-02 09:59:28 | 2023-05-02 11:26:55 | False | False | NULL | 10.20.88.4 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| D7D223E4-76CA-41BD-96C1-DBC58CC82B4D | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-02 09:59:28 | 2023-05-02 11:08:17 | False | False | NULL | 10.20.88.4 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| D7D223E4-76CA-41BD-96C1-DBC58CC82B4D | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-02 09:59:28 | 2023-05-02 09:59:28 | False | False | NULL | 10.54.25.77 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 281D9EF8-2E14-41C5-A3DE-684575C31786 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-24 10:24:13 | 2023-04-24 12:24:39 | False | False | NULL | 10.54.25.77 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 281D9EF8-2E14-41C5-A3DE-684575C31786 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-24 10:24:13 | 2023-04-24 10:24:13 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |

---


## dbo.FCM_Node_Monitoring

**Primary Key:** ID  
**Row Count:** 906  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| DateTime | datetime | YES | — | — |
| Cluster | varchar | YES | 100 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Name | varchar | YES | 100 | — |
| State | varchar | YES | 100 | — |

### Top 10 Records

| ID | DateTime | Cluster | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 03AE7963-7DAC-4C57-A796-26F997FAF6DE | 2024-06-26 08:15:04 | RBCSDLBCLS | NULL | NULL | 2024-07-30 09:00:03 | NULL | False | False | NULL |
| 03A09A67-DDFE-49BB-99C2-4A47584B59E0 | 2024-06-21 08:15:04 | PLHODLBCLS | NULL | NULL | 2024-06-21 09:00:03 | NULL | False | False | NULL |
| 035EFFA9-51FC-4A88-983E-8535030165C5 | 2023-08-06 08:15:05 | PLHODLBCLS | NULL | NULL | 2023-08-06 09:00:35 | NULL | False | False | NULL |
| 02F49FBA-CE1A-4BC4-BFA1-CF801AC4E065 | 2024-04-18 08:15:06 | PLHODLBCLS | NULL | NULL | 2024-04-18 09:00:06 | NULL | False | False | NULL |
| 02BF1734-B067-4B29-8ABD-7340A79FDE1B | 2023-09-09 08:15:06 | RBCSDLBCLS | NULL | NULL | 2023-09-09 09:00:27 | NULL | False | False | NULL |
| 029E2A8B-2773-4D04-8A46-A6DAED4DDBDD | 2023-09-27 08:15:06 | RBCSDLBCLS | NULL | NULL | 2023-09-27 09:00:29 | NULL | False | False | NULL |
| 01EE6462-19A7-4B96-A112-A98E22C7A09D | 2023-07-16 08:15:06 | PLHODLBCLS | NULL | NULL | 2023-07-16 09:01:04 | NULL | False | False | NULL |
| 01641811-5AA5-4AB9-8718-E6574EA401A6 | 2024-06-20 08:15:04 | RBCSDLBCLS | NULL | NULL | 2024-06-20 09:00:02 | NULL | False | False | NULL |
| 00D82C83-2AE1-4F58-86B9-9851621BFEB2 | 2023-07-08 08:15:06 | PLHODLBCLS | NULL | NULL | 2023-07-08 09:13:45 | NULL | False | False | NULL |
| 007BF52A-480F-4950-9B04-E29E341EC011 | 2023-09-04 08:15:05 | RBCSDLBCLS | NULL | NULL | 2023-09-04 09:00:35 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | DateTime | Cluster | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 03AE7963-7DAC-4C57-A796-26F997FAF6DE | 2024-06-26 08:15:04 | RBCSDLBCLS | NULL | NULL | 2024-07-30 09:00:03 | NULL | False | False | NULL |
| 03A09A67-DDFE-49BB-99C2-4A47584B59E0 | 2024-06-21 08:15:04 | PLHODLBCLS | NULL | NULL | 2024-06-21 09:00:03 | NULL | False | False | NULL |
| 035EFFA9-51FC-4A88-983E-8535030165C5 | 2023-08-06 08:15:05 | PLHODLBCLS | NULL | NULL | 2023-08-06 09:00:35 | NULL | False | False | NULL |
| 02F49FBA-CE1A-4BC4-BFA1-CF801AC4E065 | 2024-04-18 08:15:06 | PLHODLBCLS | NULL | NULL | 2024-04-18 09:00:06 | NULL | False | False | NULL |
| 02BF1734-B067-4B29-8ABD-7340A79FDE1B | 2023-09-09 08:15:06 | RBCSDLBCLS | NULL | NULL | 2023-09-09 09:00:27 | NULL | False | False | NULL |
| 029E2A8B-2773-4D04-8A46-A6DAED4DDBDD | 2023-09-27 08:15:06 | RBCSDLBCLS | NULL | NULL | 2023-09-27 09:00:29 | NULL | False | False | NULL |
| 01EE6462-19A7-4B96-A112-A98E22C7A09D | 2023-07-16 08:15:06 | PLHODLBCLS | NULL | NULL | 2023-07-16 09:01:04 | NULL | False | False | NULL |
| 01641811-5AA5-4AB9-8718-E6574EA401A6 | 2024-06-20 08:15:04 | RBCSDLBCLS | NULL | NULL | 2024-06-20 09:00:02 | NULL | False | False | NULL |
| 00D82C83-2AE1-4F58-86B9-9851621BFEB2 | 2023-07-08 08:15:06 | PLHODLBCLS | NULL | NULL | 2023-07-08 09:13:45 | NULL | False | False | NULL |
| 007BF52A-480F-4950-9B04-E29E341EC011 | 2023-09-04 08:15:05 | RBCSDLBCLS | NULL | NULL | 2023-09-04 09:00:35 | NULL | False | False | NULL |

---


## dbo.Folder_Monitoring

**Primary Key:** ID  
**Row Count:** 938  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| EntryDateTime | datetime | YES | — | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| SizeInGB | decimal | YES | 18,4 | — |
| FolderName | varchar | YES | 100 | — |

### Top 10 Records

| ID | EntryDateTime | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 028FD26F-1196-4BC3-B31A-57AA7AF3508B | 2023-07-29 08:25:03 | NULL | NULL | 2023-07-29 09:00:17 | NULL | False | False | NULL | NULL |
| 0284C59D-88E8-4678-9525-6A692645537C | 2024-06-26 08:25:02 | NULL | NULL | 2024-07-03 09:00:03 | NULL | False | False | NULL | NULL |
| 026DF7B2-E0BD-4AA0-84E7-2C170E03B743 | 2024-05-20 08:25:03 | NULL | NULL | 2024-05-20 09:00:04 | NULL | False | False | NULL | NULL |
| 01F9ABE3-CA66-4F99-8FBB-194A5AF2ECF3 | 2024-06-17 08:25:02 | NULL | NULL | 2024-06-17 09:00:05 | NULL | False | False | NULL | NULL |
| 01DCDCCC-5348-4FBE-B7BF-842EB32AE206 | 2024-05-08 08:25:03 | NULL | NULL | 2024-05-08 09:00:07 | NULL | False | False | NULL | NULL |
| 01887801-FEDF-405A-A5DE-D6D1FB7672DD | 2023-09-26 08:25:03 | NULL | NULL | 2023-09-26 09:00:11 | NULL | False | False | NULL | NULL |
| 0103E75A-B858-49B0-9353-E6E1C712378B | 2023-09-07 08:25:03 | NULL | NULL | 2023-09-07 09:00:06 | NULL | False | False | NULL | NULL |
| 0103718F-DFF1-4667-B854-65083CD90B12 | 2023-07-14 08:25:03 | NULL | NULL | 2023-07-14 09:00:38 | NULL | False | False | NULL | NULL |
| 00AAE741-F5B0-44B0-9AD8-54620ABB37D9 | 2024-04-29 08:25:03 | NULL | NULL | 2024-04-29 09:00:02 | NULL | False | False | NULL | NULL |
| 0072A8A4-0D51-49C3-9B97-348DE66D14A5 | 2024-04-11 08:25:03 | NULL | NULL | 2024-04-11 09:00:09 | NULL | False | False | NULL | NULL |

### Bottom 10 Records

| ID | EntryDateTime | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 028FD26F-1196-4BC3-B31A-57AA7AF3508B | 2023-07-29 08:25:03 | NULL | NULL | 2023-07-29 09:00:17 | NULL | False | False | NULL | NULL |
| 0284C59D-88E8-4678-9525-6A692645537C | 2024-06-26 08:25:02 | NULL | NULL | 2024-07-03 09:00:03 | NULL | False | False | NULL | NULL |
| 026DF7B2-E0BD-4AA0-84E7-2C170E03B743 | 2024-05-20 08:25:03 | NULL | NULL | 2024-05-20 09:00:04 | NULL | False | False | NULL | NULL |
| 01F9ABE3-CA66-4F99-8FBB-194A5AF2ECF3 | 2024-06-17 08:25:02 | NULL | NULL | 2024-06-17 09:00:05 | NULL | False | False | NULL | NULL |
| 01DCDCCC-5348-4FBE-B7BF-842EB32AE206 | 2024-05-08 08:25:03 | NULL | NULL | 2024-05-08 09:00:07 | NULL | False | False | NULL | NULL |
| 01887801-FEDF-405A-A5DE-D6D1FB7672DD | 2023-09-26 08:25:03 | NULL | NULL | 2023-09-26 09:00:11 | NULL | False | False | NULL | NULL |
| 0103E75A-B858-49B0-9353-E6E1C712378B | 2023-09-07 08:25:03 | NULL | NULL | 2023-09-07 09:00:06 | NULL | False | False | NULL | NULL |
| 0103718F-DFF1-4667-B854-65083CD90B12 | 2023-07-14 08:25:03 | NULL | NULL | 2023-07-14 09:00:38 | NULL | False | False | NULL | NULL |
| 00AAE741-F5B0-44B0-9AD8-54620ABB37D9 | 2024-04-29 08:25:03 | NULL | NULL | 2024-04-29 09:00:02 | NULL | False | False | NULL | NULL |
| 0072A8A4-0D51-49C3-9B97-348DE66D14A5 | 2024-04-11 08:25:03 | NULL | NULL | 2024-04-11 09:00:09 | NULL | False | False | NULL | NULL |

---


## dbo.Folder_Monitoring_Audit

**Primary Key:** —  
**Row Count:** 43  
**Date Range (ModifiedOn):** 2023-04-06 18:21:41 to 2023-06-28 17:06:45  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| EntryDateTime | datetime | YES | — | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| SizeInGB | decimal | YES | 18,4 | — |
| FolderName | varchar | YES | 100 | — |

### Top 10 Records

| ID | EntryDateTime | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7A8D585D-904C-458D-B9FF-52A002F4A4F8 | 2023-04-06 18:20:00 | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-06 18:21:42 | 2023-04-06 18:21:41 | False | False | NULL | 10.20.88.4 |
| 2F953D69-7744-47A0-9544-FD94B2CEC8D9 | 2023-04-08 12:11:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-08 12:19:17 | 2023-04-08 12:19:17 | False | False | NULL | 10.54.25.77 |
| 12EEE26B-762C-4183-8488-EA3A770C4EA5 | 2023-04-12 17:06:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-12 17:11:33 | 2023-04-12 17:11:33 | False | False | NULL | 10.54.25.77 |
| E6735AAE-17F2-449B-8FFC-B92DDB52E669 | 2023-04-13 12:29:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-13 12:33:42 | 2023-04-13 12:33:42 | False | False | NULL | 10.54.25.77 |
| FE80DD66-DF76-4219-B7C7-BC95124C2F86 | 2023-04-14 10:29:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-14 10:36:34 | 2023-04-14 10:36:34 | False | False | NULL | 10.54.25.77 |
| 8A679A26-A3DA-42A7-B53E-6D03D3BD269D | 2023-04-15 10:11:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-15 10:12:53 | 2023-04-15 10:12:53 | False | False | NULL | 10.20.65.186 |
| 51B4F76A-53E1-4793-8B23-041642A68881 | 2023-04-18 09:36:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-18 09:37:30 | 2023-04-18 09:37:30 | False | False | NULL | 10.54.25.77 |
| 51B4F76A-53E1-4793-8B23-041642A68881 | 2023-04-18 09:36:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-18 09:37:30 | 2023-04-18 09:39:36 | False | False | NULL | 10.54.25.77 |
| A704CD5F-5D73-40EA-BD8B-A03250493BBA | 2023-04-19 17:02:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-19 17:03:35 | 2023-04-19 17:03:35 | False | False | NULL | 10.54.25.77 |
| 80CA58AF-F7EB-4FBE-8F0B-577AE6BC2E58 | 2023-05-01 14:27:00 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-01 14:28:15 | 2023-05-01 14:28:14 | False | False | NULL | 10.20.88.4 |

### Bottom 10 Records

| ID | EntryDateTime | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DBDE69C7-C30D-454A-80C9-9D30BC464514 | 2023-06-28 16:58:00 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-06-28 17:06:45 | 2023-06-28 17:06:45 | False | False | NULL | 10.54.25.77 |
| 0E19EEE0-01B8-4E82-9045-B901673E6D93 | 2023-06-21 15:36:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-21 15:37:57 | 2023-06-21 15:43:12 | False | False | NULL | 10.54.25.77 |
| 0E19EEE0-01B8-4E82-9045-B901673E6D93 | 2023-06-21 15:36:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-21 15:37:57 | 2023-06-21 15:42:36 | False | False | NULL | 10.54.25.77 |
| 0E19EEE0-01B8-4E82-9045-B901673E6D93 | 2023-06-21 15:36:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-21 15:37:57 | 2023-06-21 15:37:57 | False | False | NULL | 10.54.25.77 |
| 85F07D63-8466-48A0-80CC-06BDE9CAABA0 | 2023-06-20 16:34:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-20 16:42:37 | 2023-06-20 16:42:37 | False | False | NULL | 10.54.25.77 |
| F8B94D98-3936-4DAA-80D9-B9B901819D72 | 2023-06-19 15:37:00 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-19 15:42:13 | 2023-06-19 15:42:13 | False | False | NULL | 10.54.25.77 |
| A9E5212C-20FA-4BFF-B698-2FBD43600A60 | 2023-06-17 11:11:00 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-17 11:12:13 | 2023-06-17 11:12:13 | False | False | NULL | 10.54.25.77 |
| 40CB5239-A28B-45A6-95DD-75D8EBA02DB5 | 2023-06-16 09:01:00 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-16 09:04:56 | 2023-06-16 09:25:59 | False | False | NULL | 10.54.25.77 |
| 40CB5239-A28B-45A6-95DD-75D8EBA02DB5 | 2023-06-16 09:01:00 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-16 09:04:56 | 2023-06-16 09:04:56 | False | False | NULL | 10.54.25.77 |
| A9ED0C9A-44D7-41C7-B899-2A4949F17CF1 | 2023-06-13 11:24:00 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-13 11:26:26 | 2023-06-13 11:26:26 | False | False | NULL | 10.54.25.77 |

---


## dbo.HOD_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| AreaID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| UserID | varchar | YES | -1 | — |

---


## dbo.HOD_Mst_Tbl_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| AreaID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| UserID | varchar | YES | -1 | — |

---


## dbo.Hardware_Monitoring

**Primary Key:** ID  
**Row Count:** 73  
**Date Range (ModifiedOn):** 2023-04-07 16:04:18 to 2023-07-04 10:26:48  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| RBCSCDLBP1Summary | varchar | YES | -1 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| RBCSCDLBP1ErrorFound | bit | YES | — | — |
| RBCSCDLBP1ErrorImages | varchar | YES | -1 | — |
| RBCSCDLBP2Summary | varchar | YES | -1 | — |
| RBCSCDLBP2ErrorFound | bit | YES | — | — |
| RBCSCDLBP2ErrorImages | varchar | YES | -1 | — |
| PLHODLBP1Summary | varchar | YES | -1 | — |
| PLHODLBP1ErrorFound | bit | YES | — | — |
| PLHODLBP1ErrorImages | varchar | YES | -1 | — |
| PLHODLBP2Summary | varchar | YES | -1 | — |
| PLHODLBP2ErrorFound | bit | YES | — | — |
| PLHODLBP2ErrorImages | varchar | YES | -1 | — |
| NoidaSANSummary | varchar | YES | -1 | — |
| NoidaSANErrorFound | bit | YES | — | — |
| NoidaSANErrorImages | varchar | YES | -1 | — |
| BangaloreSANSummary | varchar | YES | -1 | — |
| BangaloreSANErrorFound | bit | YES | — | — |
| BangaloreSANErrorImages | varchar | YES | -1 | — |
| RBCSCDLBP1FailurePrediction | varchar | YES | -1 | — |
| RBCSCDLBP2FailurePrediction | varchar | YES | -1 | — |
| PLHODLBP1FailurePrediction | varchar | YES | -1 | — |
| PLHODLBP2FailurePrediction | varchar | YES | -1 | — |
| Entrydatetime | datetime | YES | — | — |
| Parentid | varchar | YES | 36 | — |
| RBCSCDLBP1SummaryRemarks | varchar | YES | 100 | — |
| RBCSCDLBP2SummaryRemarks | varchar | YES | 100 | — |
| PLHODLBP1SummaryRemarks | varchar | YES | 100 | — |
| PLHODLBP2SummaryRemarks | varchar | YES | 100 | — |
| NoidaSANSummaryRemarks | varchar | YES | 100 | — |
| BangaloreSANSummaryRemarks | varchar | YES | 100 | — |
| RBCSCDLBP1FailurePredictionRemarks | varchar | YES | 100 | — |
| RBCSCDLBP2FailurePredictionRemarks | varchar | YES | 100 | — |
| PLHODLBP1FailurePredictionRemarks | varchar | YES | 100 | — |
| PLHODLBP2FailurePredictionRemarks | varchar | YES | 100 | — |

### Top 10 Records

| ID | RBCSCDLBP1Summary | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8BB3CF21-658B-4D98-9642-6F537E60B8A1 | <p><br><img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAeAB4AAD/4RDyRXhpZgAATU0AKgAAAAgABAE7A... | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-07 16:04:18 | 2023-04-07 16:04:18 | False | False | NULL | 10.54.25.77 |
| E6551553-C54F-4EB1-A406-BE7443910326 | NULL | 80534764-F53E-4106-81A8-D86849F6E75C | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-06 16:27:21 | 2023-04-07 16:16:42 | True | False | NULL | 10.20.88.4 |
| 68C445A1-5B48-47BC-A38E-5BA3A5CE7ACB | <p>1</p> | 88C277EC-D407-477C-AD45-83A63BDF24EE | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-07 14:38:19 | 2023-04-07 16:16:47 | True | False | NULL | 10.20.88.4 |
| EEBE977F-878A-4894-93CC-F2E9253E205E | NULL | 59AAEDF6-FFC8-4064-BADB-5C85341AF7B3 | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-07 11:13:49 | 2023-04-07 16:16:51 | True | False | NULL | 10.20.88.4 |
| 5777122E-EC20-41C7-A512-ADCFBA70356C | NULL | 9EFA3064-E41F-4661-9244-8631B72F601D | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-07 10:52:06 | 2023-04-07 16:16:56 | True | False | NULL | 10.20.88.4 |
| 337237B6-C82C-4AB0-86B3-4FB2088956B1 | NULL | 80534764-F53E-4106-81A8-D86849F6E75C | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-07 10:48:56 | 2023-04-07 16:17:03 | True | False | NULL | 10.20.88.4 |
| 9807410A-2FEB-42E2-B421-9E75A110F0A6 | <p><img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAeAB4AAD/4RDyRXhpZgAATU0AKgAAAAgABAE7AAIAA... | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-08 10:27:50 | 2023-04-08 10:27:50 | False | False | NULL | 10.54.25.77 |
| 8BDEA611-3B6D-46EB-9EC9-023630B5E57A | <p><br><img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAeAB4AAD/4RDyRXhpZgAATU0AKgAAAAgABAE7A... | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-10 14:22:19 | 2023-04-10 14:24:55 | False | False | NULL | 10.54.25.77 |
| E3C5E333-409F-4908-B7A3-AA174FAFB4ED | NULL | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-11 12:13:30 | 2023-04-11 12:13:29 | False | False | NULL | 10.54.25.77 |
| 4A5D733E-FD4E-4272-9F70-1C9A59867F17 | <p><img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/4RDyRXhpZgAATU0AKgAAAAgABAE7AAIAA... | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-12 16:52:53 | 2023-04-12 17:03:14 | False | False | NULL | 10.54.25.77 |

### Bottom 10 Records

| ID | RBCSCDLBP1Summary | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F150470E-482F-4DA8-8587-DB1FDF1514E9 | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB4AAAAQ4CAYAAADo08FDAAAAAXNSR0IArs4c6Q... | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-07-04 10:26:48 | 2023-07-04 10:26:48 | False | False | NULL | 10.20.79.9 |
| DD291F6E-C0FD-49A2-8BDA-1F323EF278B6 | <p><br><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB4AAAAQ4CAYAAADo08FDAAAAAXNSR0IArs... | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-07-03 10:28:30 | 2023-07-03 10:28:29 | False | False | NULL | 10.20.79.9 |
| F92EF6A8-648E-4ACF-A59D-0C886C812BC1 | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB4AAAAQ4CAYAAADo08FDAAAAAXNSR0IArs4c6Q... | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-30 11:54:44 | 2023-06-30 11:54:42 | False | False | NULL | 10.20.79.9 |
| 2C8D6366-F722-4C8E-B413-E5B8BC313485 | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB4AAAAQ4CAYAAADo08FDAAAAAXNSR0IArs4c6Q... | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-28 10:00:21 | 2023-06-28 10:00:21 | False | False | NULL | 10.20.79.9 |
| 7DBB4226-08CF-4E71-B5B6-A779D70012EE | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB4AAAAQ4CAYAAADo08FDAAAAAXNSR0IArs4c6Q... | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-26 10:25:52 | 2023-06-26 10:26:37 | False | False | NULL | 10.20.79.9 |
| 9A82F065-1E23-48BF-A28F-BD179FEFE65E | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB4AAAAQ4CAYAAADo08FDAAAAAXNSR0IArs4c6Q... | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-23 12:51:43 | 2023-06-23 12:51:43 | False | False | NULL | 10.20.79.9 |
| 9BAFE8BB-27F3-4F29-AC5D-26A533BE4F4A | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB4AAAAQ4CAYAAADo08FDAAAAAXNSR0IArs4c6Q... | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-22 14:23:33 | 2023-06-22 14:23:32 | False | False | NULL | 10.20.79.9 |
| 9006A3B2-729B-40B5-BE1D-C92CF148595C | <p><br><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB4AAAAQ4CAYAAADo08FDAAAAAXNSR0IArs... | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-21 15:11:15 | 2023-06-21 15:11:15 | False | False | NULL | 10.20.79.9 |
| D15D2EDF-8C6D-43DE-8178-C2AFD9F9AA91 | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB4AAAAQ4CAYAAADo08FDAAAAAXNSR0IArs4c6Q... | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-20 16:17:53 | 2023-06-20 16:17:52 | False | False | NULL | 10.20.79.9 |
| B913B025-4C9B-4921-8875-79EB0FB55E66 | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB4AAAAQ4CAYAAADo08FDAAAAAXNSR0IArs4c6Q... | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-19 14:16:04 | 2023-06-19 14:16:04 | False | False | NULL | 10.20.79.9 |

---


## dbo.Hardware_Monitoring_Audit

**Primary Key:** —  
**Row Count:** 25  
**Date Range (ModifiedOn):** 2023-04-06 16:27:21 to 2023-06-26 10:25:51  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| RBCSCDLBP1Summary | varchar | YES | -1 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| RBCSCDLBP1ErrorFound | bit | YES | — | — |
| RBCSCDLBP1ErrorImages | varchar | YES | -1 | — |
| RBCSCDLBP2Summary | varchar | YES | -1 | — |
| RBCSCDLBP2ErrorFound | bit | YES | — | — |
| RBCSCDLBP2ErrorImages | varchar | YES | -1 | — |
| PLHODLBP1Summary | varchar | YES | -1 | — |
| PLHODLBP1ErrorFound | bit | YES | — | — |
| PLHODLBP1ErrorImages | varchar | YES | -1 | — |
| PLHODLBP2Summary | varchar | YES | -1 | — |
| PLHODLBP2ErrorFound | bit | YES | — | — |
| PLHODLBP2ErrorImages | varchar | YES | -1 | — |
| NoidaSANSummary | varchar | YES | -1 | — |
| NoidaSANErrorFound | bit | YES | — | — |
| NoidaSANErrorImages | varchar | YES | -1 | — |
| BangaloreSANSummary | varchar | YES | -1 | — |
| BangaloreSANErrorFound | bit | YES | — | — |
| BangaloreSANErrorImages | varchar | YES | -1 | — |
| RBCSCDLBP1FailurePrediction | varchar | YES | -1 | — |
| RBCSCDLBP2FailurePrediction | varchar | YES | -1 | — |
| PLHODLBP1FailurePrediction | varchar | YES | -1 | — |
| PLHODLBP2FailurePrediction | varchar | YES | -1 | — |
| Entrydatetime | datetime | YES | — | — |
| Parentid | varchar | YES | 36 | — |
| RBCSCDLBP1SummaryRemarks | varchar | YES | 100 | — |
| RBCSCDLBP2SummaryRemarks | varchar | YES | 100 | — |
| PLHODLBP1SummaryRemarks | varchar | YES | 100 | — |
| PLHODLBP2SummaryRemarks | varchar | YES | 100 | — |
| NoidaSANSummaryRemarks | varchar | YES | 100 | — |
| BangaloreSANSummaryRemarks | varchar | YES | 100 | — |
| RBCSCDLBP1FailurePredictionRemarks | varchar | YES | 100 | — |
| RBCSCDLBP2FailurePredictionRemarks | varchar | YES | 100 | — |
| PLHODLBP1FailurePredictionRemarks | varchar | YES | 100 | — |
| PLHODLBP2FailurePredictionRemarks | varchar | YES | 100 | — |

### Top 10 Records

| ID | RBCSCDLBP1Summary | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E6551553-C54F-4EB1-A406-BE7443910326 | NULL | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-06 16:27:21 | 2023-04-06 16:27:21 | False | False | NULL | 10.20.88.4 |
| 337237B6-C82C-4AB0-86B3-4FB2088956B1 | NULL | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-07 10:48:56 | 2023-04-07 10:48:56 | False | False | NULL | 10.20.88.4 |
| 5777122E-EC20-41C7-A512-ADCFBA70356C | NULL | 9EFA3064-E41F-4661-9244-8631B72F601D | 9EFA3064-E41F-4661-9244-8631B72F601D | 2023-04-07 10:52:06 | 2023-04-07 10:52:06 | False | False | NULL | 10.54.25.77 |
| EEBE977F-878A-4894-93CC-F2E9253E205E | NULL | 59AAEDF6-FFC8-4064-BADB-5C85341AF7B3 | 59AAEDF6-FFC8-4064-BADB-5C85341AF7B3 | 2023-04-07 11:13:49 | 2023-04-07 11:13:49 | False | False | NULL | 10.20.88.4 |
| 68C445A1-5B48-47BC-A38E-5BA3A5CE7ACB | <p>1</p> | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-07 14:38:19 | 2023-04-07 14:38:19 | False | False | NULL | 10.54.25.77 |
| 8BDEA611-3B6D-46EB-9EC9-023630B5E57A | NULL | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-10 14:22:19 | 2023-04-10 14:22:18 | False | False | NULL | 10.54.25.77 |
| 4A5D733E-FD4E-4272-9F70-1C9A59867F17 | <p><img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/4RDyRXhpZgAATU0AKgAAAAgABAE7AAIAA... | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-12 16:52:53 | 2023-04-12 16:52:53 | False | False | NULL | 10.54.25.77 |
| 2594E700-EEDD-48D5-A3D0-3E57BA7E96C1 | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAByAAAAPYCAYAAACSaO6eAAAgAElEQVR4nOzde1... | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-05-01 11:18:50 | 2023-05-01 11:18:49 | False | False | NULL | 10.54.25.77 |
| 3ECA0A22-DCBD-48B5-818A-3C10AA7790EE | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABVYAAAMACAYAAADPPjzCAAAgAElEQVR4nOydeX... | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-05-02 09:09:11 | 2023-05-02 09:09:11 | False | False | NULL | 10.20.88.4 |
| 88CC37E5-FCB7-4206-A9D8-50130A4F4A14 | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB4AAAAQ4CAYAAADo08FDAAAgAElEQVR4nOzdf1... | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-05-05 14:15:49 | 2023-05-05 14:15:49 | False | False | NULL | 10.20.65.186 |

### Bottom 10 Records

| ID | RBCSCDLBP1Summary | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7DBB4226-08CF-4E71-B5B6-A779D70012EE | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB4AAAAQ4CAYAAADo08FDAAAAAXNSR0IArs4c6Q... | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-26 10:25:52 | 2023-06-26 10:25:51 | False | False | NULL | 10.20.79.9 |
| CFD05BD2-FC4C-48D4-8147-DB0E0FCF3FC8 | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABkAAAAOECAYAAAD5Tf2iAAAgAElEQVR4nOy9eX... | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-16 09:24:41 | 2023-06-16 09:24:40 | False | False | NULL | 10.54.25.77 |
| 41CBE191-E67F-4D9D-8798-029D0CE96847 | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABkAAAAOECAYAAAD5Tf2iAAAgAElEQVR4nOy9eX... | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-14 09:54:45 | 2023-06-14 11:42:31 | False | False | NULL | 10.20.79.9 |
| 41CBE191-E67F-4D9D-8798-029D0CE96847 | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABkAAAAOECAYAAAD5Tf2iAAAgAElEQVR4nOy9eX... | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-14 09:54:45 | 2023-06-14 09:54:39 | False | False | NULL | 10.20.88.4 |
| 2FC43F4E-3425-4B38-B9DE-936876ED1A93 | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABkAAAAOECAYAAAD5Tf2iAAAgAElEQVR4nOzde3... | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-10 09:25:06 | 2023-06-10 09:25:06 | False | False | NULL | 10.54.25.77 |
| 49DD910C-7282-42A5-8261-27E50423E958 | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB4AAAAQ4CAYAAADo08FDAAAAAXNSR0IArs4c6Q... | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-09 12:23:08 | 2023-06-09 12:23:08 | False | False | NULL | 10.20.79.9 |
| A43ABD45-5CD3-4C37-84F5-B895D5C55C4D | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABkAAAAOECAYAAAD5Tf2iAAAgAElEQVR4nOzde1... | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-08 08:57:47 | 2023-06-08 08:57:43 | False | False | NULL | 10.54.25.77 |
| E7276A4C-4064-4350-A519-E19ECBB8626A | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABkAAAAOECAYAAAD5Tf2iAAAgAElEQVR4nOzdeX... | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-06 09:03:57 | 2023-06-06 09:03:57 | False | False | NULL | 10.54.25.77 |
| 2D73981A-E14A-4485-9E8A-77F703B9FC1C | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB4AAAAQ4CAYAAADo08FDAAAgAElEQVR4nOzde3... | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-03 11:46:15 | 2023-06-03 11:46:14 | False | False | NULL | 10.54.25.77 |
| E82D0F38-F7B3-4111-9461-D44D5E4824DF | NULL | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-29 09:59:04 | 2023-05-29 09:59:04 | False | False | NULL | 10.54.25.77 |

---


## dbo.Hermes_L2_Response_Trn_Tbl

**Primary Key:** —  
**Row Count:** 79  
**Date Range (ModifiedOn):** 2026-09-02 11:59:31 to 2026-09-03 10:12:43  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| TicketID | varchar | NO | 36 | — |
| AttemptNo | int | NO | 10,0 | — |
| WorkerID | varchar | YES | 200 | — |
| ProcessStatus | varchar | NO | 30 | ('CLAIMED') |
| IsActive | bit | NO | — | ((1)) |
| Route | varchar | YES | 100 | — |
| ResponseType | varchar | YES | 30 | — |
| ProblemSummary | nvarchar | YES | -1 | — |
| Findings | nvarchar | YES | -1 | — |
| RootCause | nvarchar | YES | -1 | — |
| Resolution | nvarchar | YES | -1 | — |
| ReplyText | nvarchar | YES | -1 | — |
| InvestigationJson | nvarchar | YES | -1 | — |
| ActionsTakenJson | nvarchar | YES | -1 | — |
| RequiresUserInput | bit | NO | — | ((0)) |
| EscalateToL3 | bit | NO | — | ((0)) |
| IsResolved | bit | NO | — | ((0)) |
| TicketModifiedOnSeen | datetime | YES | — | — |
| ClaimedOn | datetime | NO | — | (getdate()) |
| HeartbeatOn | datetime | YES | — | — |
| NextEligibleOn | datetime | YES | — | — |
| CompletedOn | datetime | YES | — | — |
| ErrorMessage | nvarchar | YES | -1 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | NO | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | NO | — | ((0)) |
| IsSystem | bit | NO | — | ((0)) |
| HostAddress | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |

### Top 10 Records

| ID | TicketID | AttemptNo | WorkerID | ProcessStatus | IsActive | Route | ResponseType | ProblemSummary | Findings |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BB84D968-61CF-49FA-9C27-A924FA97BFE3 | B7E115A3-32B9-46C8-9DEC-A94D6B539A05 | 1 | HERMES_WORKER_001 | FAILED | False | GENERIC_L2_TICKET | NULL | NULL | NULL |
| 42891566-9ED5-4A62-999A-75752A2A27CB | A83BFDF3-0687-4E8E-96A9-5919F291475B | 1 | HERMES_WORKER_001 | COMPLETED | False | GENERIC_L2_TICKET | UPDATE | UAT Failures ticket in EAF: Total Carbon consumption is wrong | {"ticket_summary": {"ticket_no": "Ticket_147", "area": "EAF", "complaint_type": "UAT Failures", "... |
| 6618683E-D2B4-442C-BDBE-3FD157DF6DA5 | 82D9FE3B-EB38-4B96-B1F3-6F8F4C6874BE | 1 | HERMES_WORKER_001 | COMPLETED | False | GENERIC_L2_TICKET | UPDATE | UAT Failures ticket in Common: Wrong Calculation of delays  | {"ticket_summary": {"ticket_no": "Ticket_148", "area": "Common", "complaint_type": "UAT Failures"... |
| 3E6C4208-289F-4F90-81D3-1E0037A66F06 | D230F25E-7FFE-4C10-9297-BED912C46DE5 | 1 | HERMES_WORKER_001 | COMPLETED | False | GENERIC_L2_TICKET | UPDATE | UAT Failures ticket in EAF: Delays time is not capturing correct. EAF Power off to next EAF Power... | {"ticket_summary": {"ticket_no": "Ticket_150", "area": "EAF", "complaint_type": "UAT Failures", "... |
| A6A8ECE8-7B71-4109-9804-43176E426A5F | A99CB6BD-911B-447B-9AAF-7A46FBCEDC65 | 1 | HERMES_WORKER_001 | COMPLETED | False | GENERIC_L2_TICKET | UPDATE | UAT Failures ticket in CCM: Total Prime production wrong value in daily summary report | {"ticket_summary": {"ticket_no": "Ticket_151", "area": "CCM", "complaint_type": "UAT Failures", "... |
| 8A06BF91-95CB-407E-BB41-7B7F0B369756 | DF71A065-B62F-45D6-B391-A08A9BF69DEB | 1 | HERMES_WORKER_001 | COMPLETED | False | GENERIC_L2_TICKET | UPDATE | Request for Customization ticket in Common: Need of Between option for filtering to get range of ... | {"ticket_summary": {"ticket_no": "Ticket_156", "area": "Common", "complaint_type": "Request for C... |
| 9F79E3FA-8175-475F-B9FE-049F9224761E | 09AA1465-A5E5-4CA1-9348-7B417CB9D544 | 1 | HERMES_WORKER_001 | COMPLETED | False | GENERIC_L2_TICKET | UPDATE | Clarification or Doubt ticket in Common: Explain what are you trying to do with the logbook data ... | {"ticket_summary": {"ticket_no": "Ticket_157", "area": "Common", "complaint_type": "Clarification... |
| 559E732B-A50A-4922-A893-C0E64547B75C | 7D8855CF-23B0-46AE-9B5F-11A6DB8FE1FE | 1 | HERMES_WORKER_001 | COMPLETED | False | GENERIC_L2_TICKET | UPDATE | Request for Customization ticket in Common: SMS Delay Booking | {"ticket_summary": {"ticket_no": "Ticket_164", "area": "Common", "complaint_type": "Request for C... |
| B29BFD33-369A-4379-AC5B-B418A5B74065 | D1074D10-1CB8-412F-84C5-0BD4A47ADEEA | 1 | HERMES_WORKER_001 | COMPLETED | False | GENERIC_L2_TICKET | UPDATE | Bug ticket in EAF: Test Sagar | {"ticket_summary": {"ticket_no": "Ticket_189", "area": "EAF", "complaint_type": "Bug", "priority"... |
| A7355992-528D-40DB-8A46-4CD4AAA80C2C | 8363FE41-5726-4423-B8E1-95EDD0B073EC | 1 | HERMES_WORKER_001 | COMPLETED | False | GENERIC_L2_TICKET | UPDATE | Request for Customization ticket in Common: Remove 'Add reason' column in delay booking platform | {"ticket_summary": {"ticket_no": "Ticket_190", "area": "Common", "complaint_type": "Request for C... |

### Bottom 10 Records

| ID | TicketID | AttemptNo | WorkerID | ProcessStatus | IsActive | Route | ResponseType | ProblemSummary | Findings |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 45E45908-200F-4A7F-9A4A-5771DD087D6B | 73EC838A-440E-497B-8EDB-9CBECE8A65CF | 10 | HERMES_WORKER_001 | INVESTIGATING | True | AGENT_INVESTIGATION | NULL | NULL | NULL |
| 922B9640-605A-4EDE-A642-A162E7BF6DBA | CA88E22F-5D32-468A-BA18-5D7F3EBD2C24 | 11 | HERMES_WORKER_001 | INVESTIGATING | True | AGENT_INVESTIGATION | NULL | NULL | NULL |
| BE2C733E-7518-4FB0-A29D-196AAA0E2A79 | CA88E22F-5D32-468A-BA18-5D7F3EBD2C24 | 10 | HERMES_WORKER_001 | FAILED | False | AGENT_INVESTIGATION | NULL | NULL | NULL |
| 0E3A838E-92EF-41F2-BEA7-B7CB38774D94 | 73EC838A-440E-497B-8EDB-9CBECE8A65CF | 9 | HERMES_WORKER_001 | FAILED | False | AGENT_INVESTIGATION | NULL | NULL | NULL |
| 2D1381D0-F77A-4C1E-8F82-B18FE12D3172 | 2D7F59A4-7469-44D0-9B3B-2F51D08D9D20 | 7 | HERMES_WORKER_001 | FAILED | False | AGENT_INVESTIGATION | NULL | NULL | NULL |
| DFED635B-C136-4E87-90FE-DC410F6047E8 | CA88E22F-5D32-468A-BA18-5D7F3EBD2C24 | 9 | HERMES_WORKER_001 | FAILED | False | AGENT_INVESTIGATION | NULL | NULL | NULL |
| 0E025296-80F1-4572-9218-EEBA4708C1A7 | 73EC838A-440E-497B-8EDB-9CBECE8A65CF | 8 | HERMES_WORKER_001 | FAILED | False | AGENT_INVESTIGATION | NULL | NULL | NULL |
| CF7E1711-67EB-4BE6-ABB7-659C26345164 | 209C9084-5A3B-4BFA-ADF6-51D6D288A79D | 7 | HERMES_WORKER_001 | FAILED | False | AGENT_INVESTIGATION | NULL | NULL | NULL |
| 16BC53FF-9938-4A51-9D3E-EC7EC117888F | 209C9084-5A3B-4BFA-ADF6-51D6D288A79D | 6 | HERMES_WORKER_001 | FAILED | False | AGENT_INVESTIGATION | NULL | NULL | NULL |
| 7A8E4CF5-3706-4471-B300-AC3F383E9B45 | CA88E22F-5D32-468A-BA18-5D7F3EBD2C24 | 8 | HERMES_WORKER_001 | FAILED | False | AGENT_INVESTIGATION | NULL | NULL | NULL |

---


## dbo.Hermes_L2_SQL_Action_Trn_Tbl

**Primary Key:** —  
**Row Count:** 16  
**Date Range (ModifiedOn):** 2026-09-02 14:05:46 to 2026-09-02 15:41:20  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| RunID | varchar | NO | 36 | — |
| TicketID | varchar | NO | 36 | — |
| ActionNo | int | NO | 10,0 | — |
| ActionType | varchar | YES | 30 | — |
| DatabaseName | varchar | YES | 200 | — |
| SchemaName | varchar | YES | 200 | — |
| ObjectName | varchar | YES | 500 | — |
| OperationName | varchar | YES | 500 | — |
| Purpose | nvarchar | YES | 1000 | — |
| SqlText | nvarchar | YES | -1 | — |
| ParametersJson | nvarchar | YES | -1 | — |
| BeforeJson | nvarchar | YES | -1 | — |
| AfterJson | nvarchar | YES | -1 | — |
| Status | varchar | NO | 30 | — |
| RowsAffected | int | YES | 10,0 | — |
| StartedOn | datetime | NO | — | (getdate()) |
| CompletedOn | datetime | YES | — | — |
| ErrorNumber | int | YES | 10,0 | — |
| ErrorMessage | nvarchar | YES | -1 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | NO | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | NO | — | ((0)) |
| Source | varchar | YES | 20 | — |

### Top 10 Records

| ID | RunID | TicketID | ActionNo | ActionType | DatabaseName | SchemaName | ObjectName | OperationName | Purpose |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 64C7C464-120C-46E3-9510-EBAFF13A7954 | B469F17E-428F-4504-B716-87E2A5358CD5 | 43C246E7-ADDD-4D0F-900B-41F4674D5DD7 | 1 | READ | XStudio_Xbatch | dbo | NULL | objects_and_columns | Live investigation read for Ticket_212 |
| BED99BF4-DA63-44C7-B162-A6A1B99AAAE1 | B469F17E-428F-4504-B716-87E2A5358CD5 | 43C246E7-ADDD-4D0F-900B-41F4674D5DD7 | 2 | READ | XStudio_Xbatch | dbo | NULL | objects_and_columns | Live investigation read for Ticket_212 |
| 7AFD89FF-217A-4028-A9FD-C43DF4AB791B | B469F17E-428F-4504-B716-87E2A5358CD5 | 43C246E7-ADDD-4D0F-900B-41F4674D5DD7 | 3 | READ | XStudio_Xbatch | dbo | NULL | recalc_definition_context | Live investigation read for Ticket_212 |
| 931F9CB4-33BA-4160-BE38-439BA4F00BD3 | B469F17E-428F-4504-B716-87E2A5358CD5 | 43C246E7-ADDD-4D0F-900B-41F4674D5DD7 | 4 | READ | XStudio_Xbatch | dbo | NULL | calculation_data_and_dependencies | Live investigation read for Ticket_212 |
| F20FA769-81C0-4F73-B4D2-9BE9187B34A9 | B469F17E-428F-4504-B716-87E2A5358CD5 | 43C246E7-ADDD-4D0F-900B-41F4674D5DD7 | 5 | READ | XStudio_Helpdesk | dbo | NULL | ticket_workflow_live | Live investigation read for Ticket_212 |
| DE829BDB-4C2F-48F0-BDC6-7BE30A9C1ED8 | F67D3936-E63E-416A-A458-261C55AF027C | 9E16FB49-3D75-4719-996D-D973F91E63E9 | 1 | SELECT | XStudio_Xbatch | sys | objects | Find delay-booking objects | Locate production objects related to delay booking |
| C1A72642-4867-49C7-AE72-130A0F96E594 | F67D3936-E63E-416A-A458-261C55AF027C | 9E16FB49-3D75-4719-996D-D973F91E63E9 | 2 | SELECT | XStudio_Xbatch | dbo | Delay_Trn_Tbl | Assess short-description data model impact | Inspect delay table fields and dependent server objects before escalation |
| DA312D7F-685C-449B-9D09-C183BC0636C7 | 3CB3FBD1-9F78-4567-AEEB-8EA0412FA868 | 1B1E794A-A779-4471-A5E7-FE4AF7D5ACFD | 1 | READ | XStudio_Xbatch | NULL | NULL | Locate arcing-delay threshold logic | Investigate Ticket_201 request for an arcing-delay threshold above 47 minutes and determine wheth... |
| 51CA6A25-0439-4020-8435-1481A1935F2F | 8A5310EC-394E-4223-BC85-994B5DB5C587 | 274BFA51-AF52-429E-9AFD-51A66DC7C5A6 | 1 | READ | XStudio_Xbatch | dbo | NULL | Ticket_205_CCM_investigation | Verify live CCM table schemas and identify official CCM/heat procedures before data investigation. |
| 3B88EB96-7897-4CCE-840D-51AE0E4A81A8 | 8A5310EC-394E-4223-BC85-994B5DB5C587 | 274BFA51-AF52-429E-9AFD-51A66DC7C5A6 | 2 | READ | XStudio_Xbatch | dbo | NULL | Ticket_205_CCM_investigation | Verify live CCM table schemas and identify official CCM/heat procedures before data investigation. |

### Bottom 10 Records

| ID | RunID | TicketID | ActionNo | ActionType | DatabaseName | SchemaName | ObjectName | OperationName | Purpose |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FFD663B3-9CAC-4E83-BFC0-9CFE96E11CFB | F63D5873-EF31-463C-B4DF-E8BB2CF178F2 | E8DF09F6-4EF4-4BC1-AD9F-BCFB30E09C5C | 1 | READ | XStudio_Helpdesk | NULL | NULL | NULL | verification read |
| 5520FF5A-BD85-4DBF-91FC-F9F65A75D42A | B39A2F7C-1D1E-460D-93F9-7B1E487F5B5A | CA88E22F-5D32-468A-BA18-5D7F3EBD2C24 | 1 | READ | XStudio_Xbatch | dbo | EAF_PER_HEAT;EAF_ProcessTime;SMS_Delay_Trn_Tbl;ShiftDelayEntry | Validate completed heat timing and delay attribution | Validate Ticket_215 delay records against underlying EAF heat and process-time records. |
| 29A61E67-80E8-45F0-9A55-2A8406E5B06E | 8A5310EC-394E-4223-BC85-994B5DB5C587 | 274BFA51-AF52-429E-9AFD-51A66DC7C5A6 | 6 | READ | XStudio_Xbatch | dbo | NULL | Ticket_205_CCM_investigation | Verify whether heat 1600778 is present in the live CCM display and process-time sources after con... |
| FB387AD6-7B43-4B87-B5FC-5CB2D88120D2 | 8A5310EC-394E-4223-BC85-994B5DB5C587 | 274BFA51-AF52-429E-9AFD-51A66DC7C5A6 | 5 | READ | XStudio_Xbatch | dbo | NULL | Ticket_205_CCM_investigation | Read live records for heat 1600778, identify its CCM data path, and inspect official procedure si... |
| F29BE4F3-E751-4AF6-8780-DAA65E7DCAF6 | 8A5310EC-394E-4223-BC85-994B5DB5C587 | 274BFA51-AF52-429E-9AFD-51A66DC7C5A6 | 4 | READ | XStudio_Xbatch | dbo | NULL | Ticket_205_CCM_investigation | Verify live CCM table schemas and identify official CCM/heat procedures before data investigation. |
| 483341C0-4CFA-4560-A8D1-9FC91B38F305 | 8A5310EC-394E-4223-BC85-994B5DB5C587 | 274BFA51-AF52-429E-9AFD-51A66DC7C5A6 | 3 | READ | XStudio_Xbatch | dbo | NULL | Ticket_205_CCM_investigation | Read live records for heat 1600778, identify its CCM data path, and inspect official procedure si... |
| 3B88EB96-7897-4CCE-840D-51AE0E4A81A8 | 8A5310EC-394E-4223-BC85-994B5DB5C587 | 274BFA51-AF52-429E-9AFD-51A66DC7C5A6 | 2 | READ | XStudio_Xbatch | dbo | NULL | Ticket_205_CCM_investigation | Verify live CCM table schemas and identify official CCM/heat procedures before data investigation. |
| 51CA6A25-0439-4020-8435-1481A1935F2F | 8A5310EC-394E-4223-BC85-994B5DB5C587 | 274BFA51-AF52-429E-9AFD-51A66DC7C5A6 | 1 | READ | XStudio_Xbatch | dbo | NULL | Ticket_205_CCM_investigation | Verify live CCM table schemas and identify official CCM/heat procedures before data investigation. |
| DA312D7F-685C-449B-9D09-C183BC0636C7 | 3CB3FBD1-9F78-4567-AEEB-8EA0412FA868 | 1B1E794A-A779-4471-A5E7-FE4AF7D5ACFD | 1 | READ | XStudio_Xbatch | NULL | NULL | Locate arcing-delay threshold logic | Investigate Ticket_201 request for an arcing-delay threshold above 47 minutes and determine wheth... |
| C1A72642-4867-49C7-AE72-130A0F96E594 | F67D3936-E63E-416A-A458-261C55AF027C | 9E16FB49-3D75-4719-996D-D973F91E63E9 | 2 | SELECT | XStudio_Xbatch | dbo | Delay_Trn_Tbl | Assess short-description data model impact | Inspect delay table fields and dependent server objects before escalation |

---


## dbo.HyperV_Monitoring

**Primary Key:** ID  
**Row Count:** 234  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Entrydatetime | datetime | YES | — | — |
| Name | varchar | YES | 100 | — |
| State | varchar | YES | 100 | — |
| MemoryAssigned | int | YES | 10,0 | — |
| CPUUsage | int | YES | 10,0 | — |
| PSComputerName | varchar | YES | 100 | — |
| RunspaceId | varchar | YES | 100 | — |
| PSShowComputerName | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0C6FCFDB-4065-4B35-A2C6-74AEEA81D182 | NULL | NULL | 2023-07-22 09:00:36 | NULL | False | False | NULL | NULL | NULL |
| 09DC1144-CE2E-4E29-8025-4FCE652BB15B | NULL | NULL | 2023-09-21 09:00:29 | NULL | False | False | NULL | NULL | NULL |
| 095F411B-174E-448D-A4C4-17BEDF167600 | NULL | NULL | 2023-09-22 09:00:30 | NULL | False | False | NULL | NULL | NULL |
| 08BA9C04-34B7-4C5C-A141-2A977BA660EE | NULL | NULL | 2023-08-30 09:00:40 | NULL | False | False | NULL | NULL | NULL |
| 07AA4BCB-39D4-4D16-9421-7DA27E98F0CD | NULL | NULL | 2023-07-09 09:01:16 | NULL | False | False | NULL | NULL | NULL |
| 076C820A-0FC6-461E-9C07-CDCFD364995B | NULL | NULL | 2023-07-17 09:01:08 | NULL | False | False | NULL | NULL | NULL |
| 0476883D-6DAC-4577-849D-CC20CF1801B7 | NULL | NULL | 2023-08-08 09:00:38 | NULL | False | False | NULL | NULL | NULL |
| 03D980F3-6C71-4D35-BF54-D12F64F9B4A4 | NULL | NULL | 2023-09-13 09:00:22 | NULL | False | False | NULL | NULL | NULL |
| 03005AA6-D686-407D-B7E6-A66FAE25C604 | NULL | NULL | 2023-07-08 09:01:09 | NULL | False | False | NULL | NULL | NULL |
| 01C68DE3-504C-4351-925C-807CC4F448A4 | NULL | NULL | 2024-01-31 15:46:30 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0C6FCFDB-4065-4B35-A2C6-74AEEA81D182 | NULL | NULL | 2023-07-22 09:00:36 | NULL | False | False | NULL | NULL | NULL |
| 09DC1144-CE2E-4E29-8025-4FCE652BB15B | NULL | NULL | 2023-09-21 09:00:29 | NULL | False | False | NULL | NULL | NULL |
| 095F411B-174E-448D-A4C4-17BEDF167600 | NULL | NULL | 2023-09-22 09:00:30 | NULL | False | False | NULL | NULL | NULL |
| 08BA9C04-34B7-4C5C-A141-2A977BA660EE | NULL | NULL | 2023-08-30 09:00:40 | NULL | False | False | NULL | NULL | NULL |
| 07AA4BCB-39D4-4D16-9421-7DA27E98F0CD | NULL | NULL | 2023-07-09 09:01:16 | NULL | False | False | NULL | NULL | NULL |
| 076C820A-0FC6-461E-9C07-CDCFD364995B | NULL | NULL | 2023-07-17 09:01:08 | NULL | False | False | NULL | NULL | NULL |
| 0476883D-6DAC-4577-849D-CC20CF1801B7 | NULL | NULL | 2023-08-08 09:00:38 | NULL | False | False | NULL | NULL | NULL |
| 03D980F3-6C71-4D35-BF54-D12F64F9B4A4 | NULL | NULL | 2023-09-13 09:00:22 | NULL | False | False | NULL | NULL | NULL |
| 03005AA6-D686-407D-B7E6-A66FAE25C604 | NULL | NULL | 2023-07-08 09:01:09 | NULL | False | False | NULL | NULL | NULL |
| 01C68DE3-504C-4351-925C-807CC4F448A4 | NULL | NULL | 2024-01-31 15:46:30 | NULL | False | False | NULL | NULL | NULL |

---


## dbo.HyperV_Monitoring_Audit

**Primary Key:** —  
**Row Count:** 7  
**Date Range (ModifiedOn):** 2023-04-07 11:04:14 to 2023-05-02 09:51:03  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Entrydatetime | datetime | YES | — | — |
| Name | varchar | YES | 100 | — |
| State | varchar | YES | 100 | — |
| MemoryAssigned | int | YES | 10,0 | — |
| CPUUsage | int | YES | 10,0 | — |
| PSComputerName | varchar | YES | 100 | — |
| RunspaceId | varchar | YES | 100 | — |
| PSShowComputerName | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B75AA401-1FE8-48E5-B3F6-E9869368F653 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-07 11:04:14 | 2023-04-07 11:04:14 | False | False | NULL | 10.20.88.4 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 571107F5-7510-4E19-AD8F-D97D36373BBF | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-14 18:00:23 | 2023-04-14 18:00:23 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 6F3B0BE1-94B7-4C8B-993B-DFEC0096C776 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-20 16:11:10 | 2023-04-20 16:11:10 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 1F84E736-EEBE-4C01-B61B-13626BCDF20C | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-24 10:09:08 | 2023-04-24 10:09:08 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 1F84E736-EEBE-4C01-B61B-13626BCDF20C | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-24 10:09:08 | 2023-04-24 12:26:24 | False | False | NULL | 10.54.25.77 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 1F84E736-EEBE-4C01-B61B-13626BCDF20C | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-24 10:09:08 | 2023-04-24 12:37:38 | False | False | NULL | 10.54.25.77 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 7FE7BBAD-6F83-4E16-98CA-28FE59E4183F | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-02 09:51:03 | 2023-05-02 09:51:03 | False | False | NULL | 10.54.25.77 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |

---


## dbo.Import_Export

**Primary Key:** ID  
**Row Count:** 10  
**Date Range (ModifiedOn):** 2023-06-28 12:02:16 to 2023-11-20 11:42:05  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| CurrentRegister | varchar | YES | -1 | — |
| CurrentSystem | varchar | YES | -1 | — |
| FilePath | varchar | YES | 8000 | — |
| username | varchar | YES | 100 | — |
| StartDateTime | datetime | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| TemplateFileName | varchar | YES | 100 | — |
| ipaddress | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7410F26C-B900-4F78-80AF-C4EA7158D515 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-28 12:02:08 | 2023-06-28 12:02:16 | True | False | NULL | 10.20.88.4 | NULL |
| 61C4386E-68C0-443D-BE70-6FE910F2D697 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-29 10:35:21 | 2023-06-29 10:40:24 | True | False | NULL | 10.54.25.77 | NULL |
| FE5ED525-ABEF-4EFE-9656-05B82CB80746 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-29 10:40:57 | 2023-06-29 10:43:27 | True | False | NULL | 10.54.25.77 | NULL |
| 6CF63B16-5608-4703-9E36-92CF5BD735A3 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-08-31 15:11:19 | 2023-08-31 17:31:36 | True | False | NULL | 10.54.25.77 | NULL |
| 6F6C44EB-8F48-4E95-A6A3-8B6308A1A67A | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-06-29 10:43:57 | 2023-08-31 17:31:40 | True | False | NULL | 10.54.25.77 | NULL |
| BA97F575-1152-4CF7-8B22-9A762E9534CF | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-08-31 17:36:12 | 2023-08-31 17:36:32 | False | False | NULL | 10.54.25.77 | NULL |
| 72EEE664-3731-466C-88A7-B49A595E58F3 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-09-02 10:41:39 | 2023-09-02 10:50:56 | False | False | NULL | 10.54.25.77 | NULL |
| 08BA062F-5BC0-41F0-8B0D-D0389AE084EF | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-08-16 15:56:08 | 2023-09-22 14:52:42 | False | False | NULL | 10.20.79.68 | NULL |
| 4685DB39-7C58-4D7F-83CD-273F11961901 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-10-18 15:11:55 | 2023-10-18 15:11:55 | False | False | NULL | 10.20.65.186 | NULL |
| FF432295-4D2C-49DE-8A4D-476FA2E3D389 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-11-20 11:41:02 | 2023-11-20 11:42:05 | False | False | NULL | 10.20.65.186 | NULL |

---


## dbo.MonitoringReport

**Primary Key:** ID  
**Row Count:** 14  
**Date Range (ModifiedOn):** 2025-05-11 01:18:20 to 2025-06-03 17:26:12  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Report | varchar | YES | 8000 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A126150C-2653-46AC-977D-1A4934137309 | NULL | NULL | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-11 01:14:31 | 2025-05-11 01:18:20 | True | False | NULL |
| C12E7117-EE2E-4C9F-941E-7E50CD3A72DF | NULL | NULL | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-11 01:21:26 | 2025-05-11 01:21:26 | False | False | NULL |
| E3A6D30E-94B5-47C3-8317-5AD0FF07AF1E | OK | NULL | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-13 19:25:20 | 2025-05-13 19:25:20 | False | False | NULL |
| 8A740617-7681-4D52-B71C-20A7E9264193 | Okay | NULL | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-13 19:25:53 | 2025-05-13 19:25:53 | False | False | NULL |
| 91800277-447D-4CC8-89F7-DFD1693F14A6 | As yesterday | NULL | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-14 20:02:22 | 2025-05-14 20:02:38 | False | False | NULL |
| 4E774153-BE66-45E9-ACD3-3D3702E85B06 | NULL | NULL | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-16 19:18:52 | 2025-05-16 19:18:52 | False | False | NULL |
| 6F4622EC-9F41-49B0-BA3B-B97E3EE0352F | NULL | NULL | E053DDC8-3640-4090-8C68-1DFF8CDB6D5C | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-16 12:24:16 | 2025-05-16 19:19:14 | True | False | NULL |
| 491CB59C-44D3-4C30-9C5D-C3B2B70B9B6B | NULL | NULL | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-20 17:55:41 | 2025-05-20 17:55:41 | False | False | NULL |
| A2F1388F-CF28-4D29-A2EA-816FF362B0DC | NULL | NULL | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-20 17:56:04 | 2025-05-20 17:56:04 | False | False | NULL |
| 04305C6F-06BC-4172-9BCE-4D85D251334E | NULL | NULL | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-21 20:29:35 | 2025-05-21 20:29:35 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 089F1D07-F68D-413C-BB5F-3A4A90B83F5E | NULL | NULL | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-06-03 17:26:12 | 2025-06-03 17:26:12 | False | False | NULL |
| 09816B51-7D93-4ACC-A2B6-FDE3B23970D5 | NULL | NULL | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-27 18:58:00 | 2025-05-27 18:58:00 | False | False | NULL |
| F0EE835B-535F-4C10-9DF9-4A742A37696B | NULL | NULL | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-23 20:12:13 | 2025-05-23 20:12:13 | False | False | NULL |
| B9261B41-A58B-42F0-84DD-C8D280A91A27 | NULL | NULL | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-22 13:57:06 | 2025-05-22 13:57:06 | False | False | NULL |
| 04305C6F-06BC-4172-9BCE-4D85D251334E | NULL | NULL | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-21 20:29:35 | 2025-05-21 20:29:35 | False | False | NULL |
| A2F1388F-CF28-4D29-A2EA-816FF362B0DC | NULL | NULL | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-20 17:56:04 | 2025-05-20 17:56:04 | False | False | NULL |
| 491CB59C-44D3-4C30-9C5D-C3B2B70B9B6B | NULL | NULL | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-20 17:55:41 | 2025-05-20 17:55:41 | False | False | NULL |
| 6F4622EC-9F41-49B0-BA3B-B97E3EE0352F | NULL | NULL | E053DDC8-3640-4090-8C68-1DFF8CDB6D5C | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-16 12:24:16 | 2025-05-16 19:19:14 | True | False | NULL |
| 4E774153-BE66-45E9-ACD3-3D3702E85B06 | NULL | NULL | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-16 19:18:52 | 2025-05-16 19:18:52 | False | False | NULL |
| 91800277-447D-4CC8-89F7-DFD1693F14A6 | As yesterday | NULL | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 8B5B8594-F0CE-4389-B366-C4551533DC09 | 2025-05-14 20:02:22 | 2025-05-14 20:02:38 | False | False | NULL |

---


## dbo.Organization_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2025-08-06 14:30:54 to 2025-08-06 14:30:54  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| ParentID | varchar | YES | 36 | — |
| Name | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 77052F06-7227-47DB-82D2-7C4825C6F26E | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-06 14:30:54 | 2025-08-06 14:30:54 | False | False | NULL |  |  |

---


## dbo.Pipeline_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 43  
**Date Range (ModifiedOn):** 2022-08-10 11:59:01 to 2023-07-13 10:55:40  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| RegionID | varchar | YES | 3600 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |

### Top 10 Records

| ID | Name | RegionID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3702BEA5-58DA-4345-9F9D-090FBC6549E7 | BKPL | EC079833-B449-45E2-B4CC-2666D8D5F646 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 11:59:01 | 2022-08-10 11:59:01 | False | False | NULL |
| 24940C73-3EA9-431E-838F-52893C987AD9 | HBPL | EC079833-B449-45E2-B4CC-2666D8D5F646 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 11:59:43 | 2022-08-10 11:59:43 | False | False | NULL |
| 875F51DC-453F-4651-B2F4-60E31F9E76F5 | HMRPL | EC079833-B449-45E2-B4CC-2666D8D5F646 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 12:00:12 | 2022-08-10 12:00:12 | False | False | NULL |
| BFFC3FC4-C5A8-43FE-A57C-689D71A21026 | Lucknow ATF | EC079833-B449-45E2-B4CC-2666D8D5F646 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 12:01:52 | 2022-08-10 12:01:52 | False | False | NULL |
| 66FA0878-B0AB-4E28-91E1-B0A32FEBC3C3 | PHBPL | 89A84945-9A9A-42F6-9C3D-7F286911FE47 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 12:04:32 | 2022-08-10 12:04:32 | False | False | NULL |
| E95BF60D-0A37-4A18-B480-C3DC23FBA4C3 | CBPL | 50A8737F-4D5B-4975-B34E-B5A047AC7890 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 12:07:50 | 2022-08-10 12:07:50 | False | False | NULL |
| 02E3BE17-32C6-4A49-B775-9493865F166C | Chennai ATF | 50A8737F-4D5B-4975-B34E-B5A047AC7890 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 12:08:23 | 2022-08-10 12:08:23 | False | False | NULL |
| BBD23078-B5D3-4066-A31A-1F6BF61FCE58 | CTMPL | 50A8737F-4D5B-4975-B34E-B5A047AC7890 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 12:08:58 | 2022-08-10 12:08:58 | False | False | NULL |
| 0E5DE8B9-1B9B-4194-9DDA-9C10440FCD4A | DDPL | 50A8737F-4D5B-4975-B34E-B5A047AC7890 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 12:09:16 | 2022-08-10 12:09:16 | False | False | NULL |
| 71D3101D-11A0-4319-8C53-587FD82F5537 | ETBPNMTPL | 50A8737F-4D5B-4975-B34E-B5A047AC7890 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 12:09:45 | 2022-08-10 12:09:45 | False | False | NULL |

### Bottom 10 Records

| ID | Name | RegionID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9D866357-6A20-4F39-A2B7-EA341F1F5F82 | ATFPL | 50A8737F-4D5B-4975-B34E-B5A047AC7890 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-07-13 10:55:40 | 2023-07-13 10:55:40 | False | False | NULL |
| 9B9C1EA5-0ADB-4D16-91FE-C2957F88290D | PHBMPL | 89A84945-9A9A-42F6-9C3D-7F286911FE47 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 5FE97C53-D3CA-4ABA-B52C-C1A8AE3934EF | 2022-08-10 12:04:51 | 2023-04-11 15:34:05 | False | False | NULL |
| FFC1A040-FFA5-4004-B8BA-9ED0955CF30A | PSHPL | 89A84945-9A9A-42F6-9C3D-7F286911FE47 | 5FE97C53-D3CA-4ABA-B52C-C1A8AE3934EF | 5FE97C53-D3CA-4ABA-B52C-C1A8AE3934EF | 2023-03-20 16:16:39 | 2023-03-20 16:16:39 | False | False | NULL |
| 48190ADE-3F5D-4D08-B475-D2442A149A8A | KASPL | 334A1B18-FF30-4FD6-A858-BF35DF2C6C0C | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-03-18 11:40:40 | 2023-03-18 11:40:40 | False | False | NULL |
| 5D257561-9F88-4CCA-82A7-3C327531F770 | PHPL | 89A84945-9A9A-42F6-9C3D-7F286911FE47 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 5FE97C53-D3CA-4ABA-B52C-C1A8AE3934EF | 2022-09-27 14:58:38 | 2022-12-27 16:29:21 | False | False | NULL |
| 5801FA4C-FC90-4D85-9DCF-0C4EEC85E933 | MDPL | 92C17DA5-6422-47FA-B8D4-03090C83FABD | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 5FE97C53-D3CA-4ABA-B52C-C1A8AE3934EF | 2022-08-10 12:13:39 | 2022-12-23 16:20:07 | False | False | NULL |
| 9F316171-0D67-4BAE-8939-26387BB2C85A | Bijwasan ATF | 92C17DA5-6422-47FA-B8D4-03090C83FABD | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 5FE97C53-D3CA-4ABA-B52C-C1A8AE3934EF | 2022-08-10 12:12:20 | 2022-12-23 16:13:45 | False | False | NULL |
| A3DC81EF-6D92-4B6D-BC42-34A15A5D951A | PRRPL | 89A84945-9A9A-42F6-9C3D-7F286911FE47 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 5FE97C53-D3CA-4ABA-B52C-C1A8AE3934EF | 2022-08-10 12:05:08 | 2022-12-06 12:12:03 | False | False | NULL |
| F0F77AC8-ECC0-4258-BEE6-31E8533B7FAC | DPPL | 92C17DA5-6422-47FA-B8D4-03090C83FABD | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 12:12:36 | 2022-09-28 10:53:47 | True | False | NULL |
| E3894893-CDB7-40A1-AC9E-6C19BDE29F7B | DPPL | 92C17DA5-6422-47FA-B8D4-03090C83FABD | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-09-28 10:53:10 | 2022-09-28 10:53:10 | False | False | NULL |

---


## dbo.Pipeline_Mst_Tbl_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| RegionID | varchar | YES | 3600 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |

---


## dbo.PowerGenerationOutput

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| TotalForTheYear | decimal | YES | 18,4 | — |
| TotalForTheDay | decimal | YES | 18,4 | — |
| SolarForTheYear | decimal | YES | 18,4 | — |
| SolarForTheMonth | decimal | YES | 18,4 | — |
| WindForTheMonth | decimal | YES | 18,4 | — |
| WindForTheDay | decimal | YES | 18,4 | — |
| Region | varchar | YES | 100 | — |
| TotalForTheMonth | decimal | YES | 18,4 | — |
| WindForTheYear | decimal | YES | 18,4 | — |
| SolarForTheDay | decimal | YES | 18,4 | — |
| ReportDate | date | YES | — | — |
| Station | varchar | YES | 100 | — |

---


## dbo.PowerGenerationOutput_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| TotalForTheYear | decimal | YES | 18,4 | — |
| TotalForTheDay | decimal | YES | 18,4 | — |
| SolarForTheYear | decimal | YES | 18,4 | — |
| SolarForTheMonth | decimal | YES | 18,4 | — |
| WindForTheMonth | decimal | YES | 18,4 | — |
| WindForTheDay | decimal | YES | 18,4 | — |
| Region | varchar | YES | 100 | — |
| TotalForTheMonth | decimal | YES | 18,4 | — |
| WindForTheYear | decimal | YES | 18,4 | — |
| SolarForTheDay | decimal | YES | 18,4 | — |
| ReportDate | date | YES | — | — |
| Station | varchar | YES | 100 | — |

---


## dbo.Procedure_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| AreaID | varchar | YES | 36 | — |
| DurationUnit | varchar | YES | 36 | — |
| FrequencyID | varchar | YES | 36 | — |
| GenerationTimeLimit | int | YES | 10,0 | — |

---


## dbo.Procedure_Steps_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| ProcedureID | varchar | YES | 36 | — |
| StepDtlID | varchar | YES | 36 | — |
| Srno | int | YES | 10,0 | — |
| Type | varchar | YES | 100 | — |

---


## dbo.Procedure_Task_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| EntityID | varchar | YES | 36 | — |
| EquipmentID | varchar | YES | 36 | — |
| PageID | varchar | YES | 36 | — |
| ViewPageID | varchar | YES | 36 | — |
| Isscanable | bit | YES | — | — |

---


## dbo.Region_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2022-08-10 11:46:16 to 2022-12-06 12:11:53  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |

### Top 10 Records

| ID | Name | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 92C17DA5-6422-47FA-B8D4-03090C83FABD | NRPL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 11:46:16 | 2022-08-10 11:46:16 | False | False | NULL | 192.168.11.167 |
| 50A8737F-4D5B-4975-B34E-B5A047AC7890 | SRPL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 11:46:25 | 2022-08-10 11:46:25 | False | False | NULL | 192.168.11.167 |
| 89A84945-9A9A-42F6-9C3D-7F286911FE47 | SERPL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 11:46:34 | 2022-08-10 11:46:34 | False | False | NULL | 192.168.11.167 |
| EC079833-B449-45E2-B4CC-2666D8D5F646 | ERPL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-10 11:47:21 | 2022-08-10 11:47:21 | False | False | NULL | 192.168.11.167 |
| 334A1B18-FF30-4FD6-A858-BF35DF2C6C0C | WRPL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 5FE97C53-D3CA-4ABA-B52C-C1A8AE3934EF | 2022-08-10 11:46:44 | 2022-12-06 12:11:53 | False | False | NULL | 10.20.65.184 |

---


## dbo.Region_Mst_Tbl_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |

---


## dbo.Replica_Monitoring

**Primary Key:** ID  
**Row Count:** 456  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| ComputerName | varchar | YES | 100 | — |
| DateTime | datetime | YES | — | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| CurrentReplicaServerName | varchar | YES | 100 | — |
| State | varchar | YES | 100 | — |
| Health | varchar | YES | 100 | — |
| ReplicationState | varchar | YES | 100 | — |
| LastReplicationTime | varchar | YES | 100 | — |

### Top 10 Records

| ID | ComputerName | DateTime | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 04FF0028-027F-47D0-A599-AB9B94DA5D6C | RBCSCDLBP2 | 2024-05-20 08:05:02 | NULL | NULL | 2024-05-20 09:00:04 | NULL | False | False | NULL |
| 0466A9FF-0024-4F99-BAA9-B3E03455EBDB | PLHODLBP1 | 2023-09-22 08:05:04 | NULL | NULL | 2023-09-22 09:00:17 | NULL | False | False | NULL |
| 03A1B5B5-CC93-4F38-88B6-B7AF460EED7C | RBCSCDLBP2 | 2024-06-26 08:05:02 | NULL | NULL | 2024-07-12 09:00:03 | NULL | False | False | NULL |
| 03A1A1FB-F806-44A3-AA8A-7998B2677DAF | PLHODLBP2 | 2023-10-04 08:05:03 | NULL | NULL | 2023-10-18 09:00:25 | NULL | False | False | NULL |
| 0327A87F-75A0-40A3-AAC6-AAC10E3D47DA | RBCSCDLBP2 | 2023-07-10 08:05:03 | NULL | NULL | 2023-07-11 09:02:06 | NULL | False | False | NULL |
| 01DE479F-62B9-4BE9-BA34-CFF8FB5FCEA9 | PLHODLBP1 | 2024-04-30 08:05:03 | NULL | NULL | 2024-04-30 09:00:07 | NULL | False | False | NULL |
| 01C0537E-ACC5-4C25-99A9-97BE2F2C0E77 | PLHODLBP1 | 2023-09-04 08:05:03 | NULL | NULL | 2023-09-04 09:00:20 | NULL | False | False | NULL |
| 00A80287-5B50-47DA-8971-EC7C726B11FE | RBCSCDLBP2 | 2024-06-26 08:05:02 | NULL | NULL | 2024-06-30 09:00:03 | NULL | False | False | NULL |
| 006B34B3-DEDC-44AE-8364-DD79AB0E5290 | PLHODLBP1 | 2024-06-26 08:05:02 | NULL | NULL | 2024-07-02 09:00:03 | NULL | False | False | NULL |
| 000DDC4B-E767-4969-95F2-9EC827268194 | RBCSCDLBP1 | 2023-10-04 08:05:03 | NULL | NULL | 2023-10-07 09:00:15 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | ComputerName | DateTime | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 04FF0028-027F-47D0-A599-AB9B94DA5D6C | RBCSCDLBP2 | 2024-05-20 08:05:02 | NULL | NULL | 2024-05-20 09:00:04 | NULL | False | False | NULL |
| 0466A9FF-0024-4F99-BAA9-B3E03455EBDB | PLHODLBP1 | 2023-09-22 08:05:04 | NULL | NULL | 2023-09-22 09:00:17 | NULL | False | False | NULL |
| 03A1B5B5-CC93-4F38-88B6-B7AF460EED7C | RBCSCDLBP2 | 2024-06-26 08:05:02 | NULL | NULL | 2024-07-12 09:00:03 | NULL | False | False | NULL |
| 03A1A1FB-F806-44A3-AA8A-7998B2677DAF | PLHODLBP2 | 2023-10-04 08:05:03 | NULL | NULL | 2023-10-18 09:00:25 | NULL | False | False | NULL |
| 0327A87F-75A0-40A3-AAC6-AAC10E3D47DA | RBCSCDLBP2 | 2023-07-10 08:05:03 | NULL | NULL | 2023-07-11 09:02:06 | NULL | False | False | NULL |
| 01DE479F-62B9-4BE9-BA34-CFF8FB5FCEA9 | PLHODLBP1 | 2024-04-30 08:05:03 | NULL | NULL | 2024-04-30 09:00:07 | NULL | False | False | NULL |
| 01C0537E-ACC5-4C25-99A9-97BE2F2C0E77 | PLHODLBP1 | 2023-09-04 08:05:03 | NULL | NULL | 2023-09-04 09:00:20 | NULL | False | False | NULL |
| 00A80287-5B50-47DA-8971-EC7C726B11FE | RBCSCDLBP2 | 2024-06-26 08:05:02 | NULL | NULL | 2024-06-30 09:00:03 | NULL | False | False | NULL |
| 006B34B3-DEDC-44AE-8364-DD79AB0E5290 | PLHODLBP1 | 2024-06-26 08:05:02 | NULL | NULL | 2024-07-02 09:00:03 | NULL | False | False | NULL |
| 000DDC4B-E767-4969-95F2-9EC827268194 | RBCSCDLBP1 | 2023-10-04 08:05:03 | NULL | NULL | 2023-10-07 09:00:15 | NULL | False | False | NULL |

---


## dbo.Round_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| AreaID | varchar | YES | 36 | — |
| ProcedureID | varchar | YES | 36 | — |
| EntryDateTime | datetime | YES | — | — |
| Status | varchar | YES | 50 | — |

---


## dbo.Round_Steps_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| RoundID | varchar | YES | 36 | — |
| EntityID | varchar | YES | 36 | — |
| EquipmentID | varchar | YES | 36 | — |
| PageID | varchar | YES | 36 | — |
| ViewPageID | varchar | YES | 36 | — |
| RecordID | varchar | YES | 36 | — |
| EntryDateTime | datetime | YES | — | — |
| Status | varchar | YES | 50 | — |
| Isscanable | bit | YES | — | — |
| PhysicalTag | varchar | YES | 100 | — |

---


## dbo.SQL_Monitoring

**Primary Key:** ID  
**Row Count:** 67  
**Date Range (ModifiedOn):** 2023-04-07 16:18:27 to 2023-07-03 17:08:10  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| EntryDateTime | datetime | YES | — | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| SQLServerMonitoringImage | varchar | YES | -1 | — |
| Parentid | varchar | YES | 36 | — |
| SQLServerMonitoringRemarks | varchar | YES | 8000 | — |

### Top 10 Records

| ID | EntryDateTime | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E8CE6FAC-F488-433E-A994-5B474757514C | 2023-04-07 01:47:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-07 11:47:56 | 2023-04-07 16:18:27 | True | False | NULL | 10.20.88.4 |
| 7E68279D-C18A-4B79-9CA6-B66BD3BD311B | 2023-04-07 10:53:00 | 9EFA3064-E41F-4661-9244-8631B72F601D | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-07 10:54:04 | 2023-04-07 16:18:29 | True | False | NULL | 10.20.88.4 |
| 45A14F92-0DFD-4716-A93E-C0E484044398 | 2023-04-07 10:54:00 | 80534764-F53E-4106-81A8-D86849F6E75C | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-07 10:54:58 | 2023-04-07 16:18:30 | True | False | NULL | 10.20.88.4 |
| 9FB71399-DC7B-47DE-8C4E-DB276119D657 | 2023-04-07 10:59:00 | 80534764-F53E-4106-81A8-D86849F6E75C | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-07 11:00:01 | 2023-04-07 16:18:32 | True | False | NULL | 10.20.88.4 |
| D4EE1A05-D595-468B-922C-CFF579EE37CE | 2023-04-07 11:40:00 | 80534764-F53E-4106-81A8-D86849F6E75C | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-07 11:40:48 | 2023-04-07 16:18:34 | True | False | NULL | 10.20.88.4 |
| 2318AADD-97E6-48CA-8D62-4F49784E5687 | 2023-04-07 11:48:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-07 11:49:28 | 2023-04-07 16:18:36 | True | False | NULL | 10.20.88.4 |
| 378330F4-E99E-4185-9C8E-5439505A4554 | 2023-04-08 18:56:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-08 18:57:00 | 2023-04-08 18:57:00 | False | False | NULL | 10.54.25.77 |
| 3B78C66F-CD94-4411-80E3-566061E34A8F | 2023-04-10 19:26:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-10 19:27:03 | 2023-04-10 19:27:03 | False | False | NULL | 10.20.65.186 |
| DD77D723-96E1-44E4-9633-9F8F78E14AC9 | 2023-04-11 12:26:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-11 12:26:46 | 2023-04-11 12:26:46 | False | False | NULL | 10.54.25.77 |
| C5001C25-D6C2-4061-9A8B-2F2510CA1DDF | 2023-04-12 12:07:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-12 12:07:56 | 2023-04-12 12:07:56 | False | False | NULL | 10.54.25.77 |

### Bottom 10 Records

| ID | EntryDateTime | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 08F9E4D7-9E08-4501-81F2-5A4C6528C1F7 | 2023-07-03 17:08:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-07-03 17:08:10 | 2023-07-03 17:08:10 | False | False | NULL | 10.54.25.77 |
| 5EF73E3F-DE29-4E57-BD21-7C38130CD323 | 2023-06-26 10:55:00 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-26 10:55:51 | 2023-06-26 10:55:51 | False | False | NULL | 10.54.25.77 |
| 0F623183-535E-4ECA-8DAC-49F8E902245D | 2023-06-23 17:28:00 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-23 17:29:08 | 2023-06-23 17:29:08 | False | False | NULL | 10.54.25.77 |
| BAA192AC-0C1F-4BB3-829B-BB8FC8F5ED53 | 2023-06-22 18:21:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-22 18:22:42 | 2023-06-22 18:22:42 | False | False | NULL | 10.54.25.77 |
| C2C6296A-A8C3-4473-B82A-D3A13B29C209 | 2023-06-20 17:08:00 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-20 17:13:53 | 2023-06-20 17:13:53 | False | False | NULL | 10.54.25.77 |
| 90F0C7CA-A1C6-4224-9906-3F5ED6D9FE20 | 2023-06-19 15:43:00 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-19 15:44:47 | 2023-06-19 15:44:47 | False | False | NULL | 10.54.25.77 |
| 43E06CF0-A414-4A40-BECA-92B88BD707EB | 2023-06-17 11:04:00 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-17 11:04:27 | 2023-06-17 11:04:27 | False | False | NULL | 10.54.25.77 |
| 3C585DCA-F1F7-4EA6-AAA4-39E849B4F566 | 2023-06-16 08:53:00 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-16 08:54:18 | 2023-06-16 08:54:18 | False | False | NULL | 10.54.25.77 |
| AD3B2704-14F0-4868-8D95-8EB7D9DBFC50 | 2023-06-15 09:06:00 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-15 09:06:39 | 2023-06-15 09:06:39 | False | False | NULL | 10.54.25.77 |
| 284519C3-C98E-40FC-A1C1-1D8D6BAD1D9A | 2023-06-14 09:24:00 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-14 09:25:41 | 2023-06-14 09:25:41 | False | False | NULL | 10.20.88.4 |

---


## dbo.SQL_Monitoring_Audit

**Primary Key:** —  
**Row Count:** 11  
**Date Range (ModifiedOn):** 2023-04-07 10:54:04 to 2023-05-20 10:00:23  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| EntryDateTime | datetime | YES | — | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| SQLServerMonitoringImage | varchar | YES | -1 | — |
| Parentid | varchar | YES | 36 | — |
| SQLServerMonitoringRemarks | varchar | YES | 8000 | — |

### Top 10 Records

| ID | EntryDateTime | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7E68279D-C18A-4B79-9CA6-B66BD3BD311B | 2023-04-07 10:53:00 | 9EFA3064-E41F-4661-9244-8631B72F601D | 9EFA3064-E41F-4661-9244-8631B72F601D | 2023-04-07 10:54:04 | 2023-04-07 10:54:04 | False | False | NULL | 10.54.25.77 |
| 45A14F92-0DFD-4716-A93E-C0E484044398 | 2023-04-07 10:54:00 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-07 10:54:58 | 2023-04-07 10:54:58 | False | False | NULL | 10.20.88.4 |
| 9FB71399-DC7B-47DE-8C4E-DB276119D657 | 2023-04-07 10:59:00 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-07 11:00:01 | 2023-04-07 11:00:01 | False | False | NULL | 10.20.88.4 |
| D4EE1A05-D595-468B-922C-CFF579EE37CE | 2023-04-07 11:40:00 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-07 11:40:48 | 2023-04-07 11:40:48 | False | False | NULL | 10.20.88.4 |
| E8CE6FAC-F488-433E-A994-5B474757514C | 2023-04-07 01:47:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-07 11:47:56 | 2023-04-07 11:47:56 | False | False | NULL | 10.20.88.4 |
| 2318AADD-97E6-48CA-8D62-4F49784E5687 | 2023-04-07 11:48:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-07 11:49:28 | 2023-04-07 11:49:28 | False | False | NULL | 10.20.88.4 |
| 9C4FE9F5-2230-42A7-A51F-331237ED34E5 | 2023-04-13 10:29:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-13 10:29:56 | 2023-04-13 10:29:56 | False | False | NULL | 10.54.25.77 |
| 1BD9FE72-3FA4-4A32-BD21-CB63591D8414 | 2023-04-13 10:30:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-13 10:30:03 | 2023-04-13 10:30:03 | False | False | NULL | 10.54.25.77 |
| 5DAA89FC-68F8-446D-894A-8B930BF299FC | 2023-05-02 09:25:00 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-02 09:26:56 | 2023-05-02 09:26:56 | False | False | NULL | 10.54.25.77 |
| 3FDBC9DC-99C1-4DB7-BD6C-17BFAA4A1AFC | 2023-05-17 09:32:00 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-17 09:33:00 | 2023-05-17 09:33:00 | False | False | NULL | 10.54.25.77 |

### Bottom 10 Records

| ID | EntryDateTime | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E7B26775-BA69-4548-9F20-216B9C2335FE | 2023-05-20 10:00:00 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-20 10:00:23 | 2023-05-20 10:00:23 | False | False | NULL | 10.54.25.77 |
| 3FDBC9DC-99C1-4DB7-BD6C-17BFAA4A1AFC | 2023-05-17 09:32:00 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-17 09:33:00 | 2023-05-17 09:33:00 | False | False | NULL | 10.54.25.77 |
| 5DAA89FC-68F8-446D-894A-8B930BF299FC | 2023-05-02 09:25:00 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-02 09:26:56 | 2023-05-02 09:26:56 | False | False | NULL | 10.54.25.77 |
| 1BD9FE72-3FA4-4A32-BD21-CB63591D8414 | 2023-04-13 10:30:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-13 10:30:03 | 2023-04-13 10:30:03 | False | False | NULL | 10.54.25.77 |
| 9C4FE9F5-2230-42A7-A51F-331237ED34E5 | 2023-04-13 10:29:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-13 10:29:56 | 2023-04-13 10:29:56 | False | False | NULL | 10.54.25.77 |
| 2318AADD-97E6-48CA-8D62-4F49784E5687 | 2023-04-07 11:48:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-07 11:49:28 | 2023-04-07 11:49:28 | False | False | NULL | 10.20.88.4 |
| E8CE6FAC-F488-433E-A994-5B474757514C | 2023-04-07 01:47:00 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-07 11:47:56 | 2023-04-07 11:47:56 | False | False | NULL | 10.20.88.4 |
| D4EE1A05-D595-468B-922C-CFF579EE37CE | 2023-04-07 11:40:00 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-07 11:40:48 | 2023-04-07 11:40:48 | False | False | NULL | 10.20.88.4 |
| 9FB71399-DC7B-47DE-8C4E-DB276119D657 | 2023-04-07 10:59:00 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-07 11:00:01 | 2023-04-07 11:00:01 | False | False | NULL | 10.20.88.4 |
| 45A14F92-0DFD-4716-A93E-C0E484044398 | 2023-04-07 10:54:00 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-07 10:54:58 | 2023-04-07 10:54:58 | False | False | NULL | 10.20.88.4 |

---


## dbo.Services_Monitoring

**Primary Key:** ID  
**Row Count:** 66  
**Date Range (ModifiedOn):** 2023-04-07 16:18:04 to 2023-07-03 17:19:21  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| EntryDateTime | datetime | YES | — | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| FailoverClusterManager | varchar | YES | 8000 | — |
| HyperV | varchar | YES | 8000 | — |
| KernelPower | varchar | YES | 8000 | — |
| KernelBoot | varchar | YES | 8000 | — |
| XStudioSyncService | varchar | YES | 8000 | — |
| XStudioSchedulersService | varchar | YES | 8000 | — |
| FailoverClusterManagerRemarks | varchar | YES | 100 | — |
| HyperVRemarks | varchar | YES | 100 | — |
| KernelPowerRemarks | varchar | YES | 100 | — |
| KernelBootRemarks | varchar | YES | 100 | — |
| XStudioSyncServiceRemarks | varchar | YES | 100 | — |
| XStudioSchedulersServiceRemarks | varchar | YES | 100 | — |

### Top 10 Records

| ID | EntryDateTime | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 14C8E8BD-DBD0-4B98-BFC5-BBFCA04D1930 | 2023-04-07 11:08:00 | NULL | 80534764-F53E-4106-81A8-D86849F6E75C | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-07 11:08:39 | 2023-04-07 16:18:04 | True | False | NULL |
| EB264099-CD76-47E7-937D-5C3B54E44C13 | 2023-04-07 11:52:00 | NULL | 88C277EC-D407-477C-AD45-83A63BDF24EE | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-07 11:53:31 | 2023-04-07 16:18:16 | True | False | NULL |
| 93CDC525-0B7C-4137-AF12-DB34517B0E44 | 2023-04-08 18:24:00 | 0C2EC874-7748-40A5-84EF-380CE3964D2C | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-08 18:36:34 | 2023-04-08 19:16:06 | False | False | NULL |
| 49AE766F-FDBB-4FE2-9316-831C78ABF753 | 2023-04-10 18:59:00 | E8455E67-11BF-4B76-B52A-1D7FF8C7956E | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-10 19:12:52 | 2023-04-10 19:23:38 | False | False | NULL |
| AEEB42B8-92F0-4B2B-8695-DB21C382E47F | 2023-04-11 10:43:00 | 3FA889F2-9476-49F8-A8CC-9CFD16FDE396 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-11 10:48:11 | 2023-04-11 10:57:57 | False | False | NULL |
| 6CAB58F7-7803-4566-95FA-5D1DF333012C | 2023-04-12 12:08:00 | 590F69D8-9EF9-4E24-8C6D-DBB9F5A3582F | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-12 12:14:17 | 2023-04-12 12:14:31 | True | False | NULL |
| 609BEFBD-97F0-4AF3-84BB-03FF444F278B | 2023-04-12 11:44:00 | 590F69D8-9EF9-4E24-8C6D-DBB9F5A3582F | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-12 11:45:30 | 2023-04-12 12:20:39 | False | False | NULL |
| 0C091E67-BB36-46A2-8AF6-6FB2100F0931 | 2023-04-13 14:25:00 | 96FCFD29-D268-48FC-A21B-59EFF906C653 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-13 14:25:44 | 2023-04-13 14:25:57 | True | False | NULL |
| 44E85A61-4AA1-4A2B-BBDC-7CB87113F3EF | 2023-04-13 14:25:00 | 96FCFD29-D268-48FC-A21B-59EFF906C653 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-13 14:25:28 | 2023-04-13 18:30:06 | False | False | NULL |
| 834EEB60-57D9-420D-AC1A-EDB9423DDDCD | 2023-04-14 09:43:00 | C34AFF69-2B0B-4D06-AE9C-C2F4E7BF6D0C | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-14 09:43:38 | 2023-04-14 18:06:33 | False | False | NULL |

### Bottom 10 Records

| ID | EntryDateTime | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 28D042BD-D605-4BB4-905F-26E9DA7C2F95 | 2023-07-03 17:02:00 | B5021435-5B6A-44D8-AF2E-499F12DF5B4D | 80534764-F53E-4106-81A8-D86849F6E75C | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-07-03 17:03:18 | 2023-07-03 17:19:21 | False | False | NULL |
| B2279A60-03CB-4C65-B75A-171202D78B2B | 2023-06-30 12:08:00 | CE5EF93E-761D-4E48-8A3C-28D2F1C06A19 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-30 12:12:13 | 2023-06-30 17:08:07 | False | False | NULL |
| 7FA1FEA4-E8B3-4286-A517-93420E6A4EED | 2023-06-28 17:22:00 | 30451152-A13B-4FCF-908F-6D8590EC9145 | 59AAEDF6-FFC8-4064-BADB-5C85341AF7B3 | 59AAEDF6-FFC8-4064-BADB-5C85341AF7B3 | 2023-06-28 17:24:42 | 2023-06-28 17:24:42 | False | False | NULL |
| 4373DB92-935A-4178-9388-37A00B1490D8 | 2023-06-26 10:52:00 | 46DEF245-B8E8-464D-892F-D41B007B4EC0 | 80534764-F53E-4106-81A8-D86849F6E75C | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-06-26 10:54:56 | 2023-06-26 18:22:34 | False | False | NULL |
| BA6C29A8-E639-422A-9763-6B47AC97C0B6 | 2023-06-23 17:22:00 | 52347E61-7A6D-4D84-B379-904665BE01AE | 80534764-F53E-4106-81A8-D86849F6E75C | 59AAEDF6-FFC8-4064-BADB-5C85341AF7B3 | 2023-06-23 17:23:27 | 2023-06-23 18:01:37 | False | False | NULL |
| 0A65307E-512B-4735-BF5A-8CAEF3C6E6A8 | 2023-06-22 15:29:00 | 847F91E6-B5DB-4582-B6A7-356BD176842E | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-22 15:31:56 | 2023-06-22 15:31:56 | False | False | NULL |
| DE07BDE7-1281-46C5-BD79-FBB7B4D99515 | 2023-06-21 15:45:00 | 1DB085FA-6C3A-4A50-A82E-64B0497CFC43 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-21 15:50:19 | 2023-06-21 16:21:59 | False | False | NULL |
| 7AF1126F-9FC0-4009-BFFC-113FB58B1E24 | 2023-06-20 17:14:00 | 80C40A12-92A1-47F5-9F1B-EBF1B4CED735 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-20 17:21:07 | 2023-06-20 17:21:27 | False | False | NULL |
| 3445DAB3-D66A-4544-9BC8-D97F95B16A50 | 2023-06-17 11:04:00 | 994FDFCB-7EA2-449B-AF52-513AFA20C3E8 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-17 11:06:33 | 2023-06-17 11:08:30 | False | False | NULL |
| B1F22AEE-C387-4CF9-B98E-4CAD2E816644 | 2023-06-16 08:54:00 | 460CA49A-63DA-45FB-A556-53D09642AB8B | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-16 08:56:35 | 2023-06-16 09:10:47 | False | False | NULL |

---


## dbo.Services_Monitoring_Audit

**Primary Key:** —  
**Row Count:** 79  
**Date Range (ModifiedOn):** 2023-04-07 11:08:39 to 2023-07-03 17:03:18  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| EntryDateTime | datetime | YES | — | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| FailoverClusterManager | varchar | YES | 8000 | — |
| HyperV | varchar | YES | 8000 | — |
| KernelPower | varchar | YES | 8000 | — |
| KernelBoot | varchar | YES | 8000 | — |
| XStudioSyncService | varchar | YES | 8000 | — |
| XStudioSchedulersService | varchar | YES | 8000 | — |
| FailoverClusterManagerRemarks | varchar | YES | 100 | — |
| HyperVRemarks | varchar | YES | 100 | — |
| KernelPowerRemarks | varchar | YES | 100 | — |
| KernelBootRemarks | varchar | YES | 100 | — |
| XStudioSyncServiceRemarks | varchar | YES | 100 | — |
| XStudioSchedulersServiceRemarks | varchar | YES | 100 | — |

### Top 10 Records

| ID | EntryDateTime | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 14C8E8BD-DBD0-4B98-BFC5-BBFCA04D1930 | 2023-04-07 11:08:00 | NULL | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-07 11:08:39 | 2023-04-07 11:08:39 | False | False | NULL |
| EB264099-CD76-47E7-937D-5C3B54E44C13 | 2023-04-07 11:52:00 | NULL | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-07 11:53:31 | 2023-04-07 11:53:31 | False | False | NULL |
| 93CDC525-0B7C-4137-AF12-DB34517B0E44 | 2023-04-08 18:24:00 | 0C2EC874-7748-40A5-84EF-380CE3964D2C | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-08 18:36:34 | 2023-04-08 18:36:34 | False | False | NULL |
| 49AE766F-FDBB-4FE2-9316-831C78ABF753 | 2023-04-10 18:59:00 | E8455E67-11BF-4B76-B52A-1D7FF8C7956E | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-10 19:12:52 | 2023-04-10 19:12:52 | False | False | NULL |
| AEEB42B8-92F0-4B2B-8695-DB21C382E47F | 2023-04-11 10:43:00 | 3FA889F2-9476-49F8-A8CC-9CFD16FDE396 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-11 10:48:11 | 2023-04-11 10:48:11 | False | False | NULL |
| AEEB42B8-92F0-4B2B-8695-DB21C382E47F | 2023-04-11 10:43:00 | 3FA889F2-9476-49F8-A8CC-9CFD16FDE396 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-11 10:48:11 | 2023-04-11 10:51:37 | False | False | NULL |
| 609BEFBD-97F0-4AF3-84BB-03FF444F278B | 2023-04-12 11:44:00 | 590F69D8-9EF9-4E24-8C6D-DBB9F5A3582F | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-12 11:45:30 | 2023-04-12 11:45:30 | False | False | NULL |
| 6CAB58F7-7803-4566-95FA-5D1DF333012C | 2023-04-12 12:08:00 | 590F69D8-9EF9-4E24-8C6D-DBB9F5A3582F | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-12 12:14:17 | 2023-04-12 12:14:17 | False | False | NULL |
| 44E85A61-4AA1-4A2B-BBDC-7CB87113F3EF | 2023-04-13 14:25:00 | 96FCFD29-D268-48FC-A21B-59EFF906C653 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-13 14:25:28 | 2023-04-13 14:25:28 | False | False | NULL |
| 0C091E67-BB36-46A2-8AF6-6FB2100F0931 | 2023-04-13 14:25:00 | 96FCFD29-D268-48FC-A21B-59EFF906C653 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-13 14:25:44 | 2023-04-13 14:25:44 | False | False | NULL |

### Bottom 10 Records

| ID | EntryDateTime | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 28D042BD-D605-4BB4-905F-26E9DA7C2F95 | 2023-07-03 17:02:00 | B5021435-5B6A-44D8-AF2E-499F12DF5B4D | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-07-03 17:03:18 | 2023-07-03 17:03:18 | False | False | NULL |
| B2279A60-03CB-4C65-B75A-171202D78B2B | 2023-06-30 12:08:00 | CE5EF93E-761D-4E48-8A3C-28D2F1C06A19 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-30 12:12:13 | 2023-06-30 12:12:13 | False | False | NULL |
| 4373DB92-935A-4178-9388-37A00B1490D8 | 2023-06-26 10:52:00 | 46DEF245-B8E8-464D-892F-D41B007B4EC0 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-26 10:54:56 | 2023-06-26 10:54:56 | False | False | NULL |
| BA6C29A8-E639-422A-9763-6B47AC97C0B6 | 2023-06-23 17:22:00 | 52347E61-7A6D-4D84-B379-904665BE01AE | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-23 17:23:27 | 2023-06-23 17:23:26 | False | False | NULL |
| DE07BDE7-1281-46C5-BD79-FBB7B4D99515 | 2023-06-21 15:45:00 | 1DB085FA-6C3A-4A50-A82E-64B0497CFC43 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-21 15:50:19 | 2023-06-21 15:50:19 | False | False | NULL |
| 7AF1126F-9FC0-4009-BFFC-113FB58B1E24 | 2023-06-20 17:14:00 | 80C40A12-92A1-47F5-9F1B-EBF1B4CED735 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-20 17:21:07 | 2023-06-20 17:21:07 | False | False | NULL |
| 3445DAB3-D66A-4544-9BC8-D97F95B16A50 | 2023-06-17 11:04:00 | 994FDFCB-7EA2-449B-AF52-513AFA20C3E8 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-17 11:06:33 | 2023-06-17 11:06:33 | False | False | NULL |
| B1F22AEE-C387-4CF9-B98E-4CAD2E816644 | 2023-06-16 08:54:00 | 460CA49A-63DA-45FB-A556-53D09642AB8B | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-16 08:56:35 | 2023-06-16 08:56:35 | False | False | NULL |
| B92BD196-A394-4E48-A040-7F678E39394C | 2023-06-15 09:07:00 | DD223DAA-4AB8-432C-8F2B-6AC1AB49E126 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-15 09:09:52 | 2023-06-15 09:09:52 | False | False | NULL |
| 98A410EF-CB8A-4AF4-94EA-2CD23617C0E7 | 2023-06-13 10:42:00 | 6DCBDA26-21D9-406A-893F-8867180C368D | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-06-13 10:43:45 | 2023-06-13 10:43:45 | False | False | NULL |

---


## dbo.Station_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 169  
**Date Range (ModifiedOn):** 2022-08-12 15:10:29 to 2023-09-01 18:51:54  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| CentralDispatchID | varchar | YES | -1 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| SrNo | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | CentralDispatchID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 19324690-DBE7-4B4B-9DDA-EDFC6661E970 | Durgapur | 1E5EF7C0-FF23-49CF-B565-3A05460DF254 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-09-20 17:15:25 | NULL | False | False | NULL |
| 32868D97-E950-4CAD-AB49-6F0EF282192B | Korba | 35229A09-995B-4BEF-B00D-09DE0EB39FE9 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-09-20 16:45:26 | NULL | False | False | NULL |
| 36B7E303-1473-4741-A408-DFEFB7F054E4 | Banka | 1E5EF7C0-FF23-49CF-B565-3A05460DF254 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-09-20 17:15:25 | NULL | False | False | NULL |
| 3EE72B21-1D4A-4B31-B3A9-701DBA9FA58F | Raipur | 35229A09-995B-4BEF-B00D-09DE0EB39FE9 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-09-20 16:45:26 | NULL | False | False | NULL |
| 406DCB28-6502-411B-835D-7B6C950A89A4 | Haldia | 1E5EF7C0-FF23-49CF-B565-3A05460DF254 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-09-20 17:15:25 | NULL | False | False | NULL |
| 8529C86D-7449-497C-A9A3-A2B09A0F3DDA | Bolpur | D1C61B31-F479-46FC-8095-DFDAE6DC61C2 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-09-20 17:15:25 | NULL | False | False | NULL |
| 8ECC8D96-4178-4F12-A66B-CF6C37CCFF04 | Haldia | D1C61B31-F479-46FC-8095-DFDAE6DC61C2 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-09-20 17:15:25 | NULL | False | False | NULL |
| B0CB708F-5925-4A3F-B545-248AF54262CA | Balasore | 1E5EF7C0-FF23-49CF-B565-3A05460DF254 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-09-20 17:15:25 | NULL | False | False | NULL |
| BE7420A0-CABA-4F3F-BDC0-F95167484B57 | Balasore | D1C61B31-F479-46FC-8095-DFDAE6DC61C2 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-09-20 17:15:25 | NULL | False | False | NULL |
| CF7EC0FB-56E9-42AA-B1E7-391950CA4BD0 | Paradip | D1C61B31-F479-46FC-8095-DFDAE6DC61C2 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-09-20 17:15:25 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | CentralDispatchID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EFC0155E-C38E-4863-9BE7-33FDD92E0056 | Ahmednagar | 56B69ACA-7E2F-4D9B-BB14-87362306A29A | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-09-01 18:51:54 | 2023-09-01 18:51:54 | False | False | NULL |
| BF6B79B6-1095-4256-AB15-2FA79E468EF0 | Solapur | 56B69ACA-7E2F-4D9B-BB14-87362306A29A | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-09-01 18:50:58 | 2023-09-01 18:50:58 | False | False | NULL |
| 8EC26FB2-8076-441B-96BC-FB3D4BB2FA3C | Hyderabad | AB6D8E75-7DAF-41FD-A8AA-384F75AB4549 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-09-01 18:49:53 | 2023-09-01 18:49:53 | False | False | NULL |
| B836C497-3A21-468D-9C75-8165D5309C5D | Motihari | 1E5EF7C0-FF23-49CF-B565-3A05460DF254 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-09-01 18:48:25 | 2023-09-01 18:48:25 | False | False | NULL |
| F7948581-A987-4E6C-A8F9-747E5F218319 | Muzaffarpur | 1E5EF7C0-FF23-49CF-B565-3A05460DF254 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-09-01 18:47:47 | 2023-09-01 18:47:47 | False | False | NULL |
| E51CE38B-0AD6-4DD2-B25C-527C6415C500 | Barauni | 1E5EF7C0-FF23-49CF-B565-3A05460DF254 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-09-01 18:47:02 | 2023-09-01 18:47:02 | False | False | NULL |
| 5393B4AF-04D5-40DF-A20B-04E70F161950 | Patna | 1E5EF7C0-FF23-49CF-B565-3A05460DF254 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-09-01 18:46:32 | 2023-09-01 18:46:32 | False | False | NULL |
| B96849FA-50A5-4C1B-A7E8-4EE354A3532C | Haldia | B03A4A3B-7902-4403-B45A-151FDA29D140 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-09-01 17:37:20 | 2023-09-01 17:39:24 | False | False | NULL |
| 46CE9739-1590-45A4-ADB8-51C95DC18133 | Balasore | B03A4A3B-7902-4403-B45A-151FDA29D140 | 5FE97C53-D3CA-4ABA-B52C-C1A8AE3934EF | 5FE97C53-D3CA-4ABA-B52C-C1A8AE3934EF | 2023-03-20 16:18:48 | 2023-03-20 16:18:48 | False | False | NULL |
| C048E771-C60E-4D0C-8299-B3A348A0BFFD | Songadh | 56B69ACA-7E2F-4D9B-BB14-87362306A29A | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-03-18 11:53:23 | 2023-03-18 11:53:23 | False | False | NULL |

---


## dbo.Station_Mst_Tbl_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| CentralDispatchID | varchar | YES | -1 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| SrNo | decimal | YES | 18,4 | — |

---


## dbo.Storage_Monitoring

**Primary Key:** ID  
**Row Count:** 6,264  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| DateTime | datetime | YES | — | — |
| PSComputerName | varchar | YES | 100 | — |
| HealthStatus | varchar | YES | 100 | — |
| DriveLetter | varchar | YES | 100 | — |
| Size | decimal | YES | 18,4 | — |
| SizeRemaining | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00519074-1876-4E1B-AB7E-CD94B02FBC64 | NULL | NULL | 2024-04-28 09:00:03 | NULL | False | False | NULL | NULL | NULL |
| 00468C01-BFCB-4CE8-96CD-8BC8F5997D17 | NULL | NULL | 2024-06-21 09:00:03 | NULL | False | False | NULL | NULL | NULL |
| 00448DB1-1038-4F69-A92A-1653E8D0856C | NULL | NULL | 2023-10-04 09:00:20 | NULL | False | False | NULL | NULL | NULL |
| 003F9438-99C7-4310-9E6F-63537F57DFCF | NULL | NULL | 2023-08-17 09:00:14 | NULL | False | False | NULL | NULL | NULL |
| 0036166E-1F82-4763-8DA8-A5BFADAD67B5 | NULL | NULL | 2024-06-30 09:00:03 | NULL | False | False | NULL | NULL | NULL |
| 0018D092-51BF-41AE-89A3-C47594238C19 | NULL | NULL | 2024-05-25 09:00:09 | NULL | False | False | NULL | NULL | NULL |
| 000E4227-C01A-436B-9A98-49E31A123C40 | NULL | NULL | 2023-08-12 09:00:23 | NULL | False | False | NULL | NULL | NULL |
| 000CC0E2-0768-440E-B465-C2C9565C4857 | NULL | NULL | 2024-07-19 09:00:03 | NULL | False | False | NULL | NULL | NULL |
| 000912A6-5ABC-41B8-B4FD-2A9215012801 | NULL | NULL | 2023-10-17 09:00:16 | NULL | False | False | NULL | NULL | NULL |
| 0002FCCE-852F-42FD-BDDD-405AE82D27CE | NULL | NULL | 2023-09-21 09:00:13 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00519074-1876-4E1B-AB7E-CD94B02FBC64 | NULL | NULL | 2024-04-28 09:00:03 | NULL | False | False | NULL | NULL | NULL |
| 00468C01-BFCB-4CE8-96CD-8BC8F5997D17 | NULL | NULL | 2024-06-21 09:00:03 | NULL | False | False | NULL | NULL | NULL |
| 00448DB1-1038-4F69-A92A-1653E8D0856C | NULL | NULL | 2023-10-04 09:00:20 | NULL | False | False | NULL | NULL | NULL |
| 003F9438-99C7-4310-9E6F-63537F57DFCF | NULL | NULL | 2023-08-17 09:00:14 | NULL | False | False | NULL | NULL | NULL |
| 0036166E-1F82-4763-8DA8-A5BFADAD67B5 | NULL | NULL | 2024-06-30 09:00:03 | NULL | False | False | NULL | NULL | NULL |
| 0018D092-51BF-41AE-89A3-C47594238C19 | NULL | NULL | 2024-05-25 09:00:09 | NULL | False | False | NULL | NULL | NULL |
| 000E4227-C01A-436B-9A98-49E31A123C40 | NULL | NULL | 2023-08-12 09:00:23 | NULL | False | False | NULL | NULL | NULL |
| 000CC0E2-0768-440E-B465-C2C9565C4857 | NULL | NULL | 2024-07-19 09:00:03 | NULL | False | False | NULL | NULL | NULL |
| 000912A6-5ABC-41B8-B4FD-2A9215012801 | NULL | NULL | 2023-10-17 09:00:16 | NULL | False | False | NULL | NULL | NULL |
| 0002FCCE-852F-42FD-BDDD-405AE82D27CE | NULL | NULL | 2023-09-21 09:00:13 | NULL | False | False | NULL | NULL | NULL |

---


## dbo.Storage_Monitoring_Audit

**Primary Key:** —  
**Row Count:** 78  
**Date Range (ModifiedOn):** 2023-04-07 11:04:31 to 2023-07-03 16:58:16  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| DateTime | datetime | YES | — | — |
| PSComputerName | varchar | YES | 100 | — |
| HealthStatus | varchar | YES | 100 | — |
| DriveLetter | varchar | YES | 100 | — |
| Size | decimal | YES | 18,4 | — |
| SizeRemaining | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B4F37746-8FEA-4CC0-9B87-82E97DAEE940 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-04-07 11:04:31 | 2023-04-07 11:04:31 | False | False | NULL | 10.20.88.4 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 391CCF29-9335-41C0-BF43-61A42EF38523 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-08 11:33:38 | 2023-04-08 11:33:38 | False | False | NULL | 10.54.25.77 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 7AB30C4D-21AA-433C-9DFF-4E23BCF4A5D6 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-12 17:06:18 | 2023-04-12 17:06:18 | False | False | NULL | 10.54.25.77 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| D8616C5A-69E5-4BA8-A84B-AC65482708F6 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-12 17:55:12 | 2023-04-12 17:55:12 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 0ACFD215-EC71-42F7-93B9-0C9BDD62939A | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-13 14:24:27 | 2023-04-13 14:24:27 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 479FC114-4727-416C-A0DE-48EB21A2600C | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-15 09:36:54 | 2023-04-15 09:36:54 | False | False | NULL | 10.54.25.77 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| E8F018C0-6147-4B68-8EB5-B19C4C52C0B5 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-17 09:32:43 | 2023-04-17 09:32:43 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| E8F018C0-6147-4B68-8EB5-B19C4C52C0B5 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-17 09:32:43 | 2023-04-17 09:34:52 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 78CFEDA1-68A7-4D7C-83F6-B597BE08E009 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-17 10:22:34 | 2023-04-17 10:22:34 | False | False | NULL | 10.54.25.77 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| CC07C21E-5C49-4216-8AB7-7138E384349E | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-18 09:18:49 | 2023-04-18 09:18:49 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 64B00A86-5077-44EC-A7F5-3A6554826F51 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-07-03 16:58:16 | 2023-07-03 16:58:16 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 1A323164-A0CB-4796-B3B2-382A1072EED8 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-30 12:11:07 | 2023-06-30 16:57:56 | False | False | NULL | 10.54.25.77 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 1A323164-A0CB-4796-B3B2-382A1072EED8 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-30 12:11:07 | 2023-06-30 12:11:07 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| ADCDF7C8-DEC9-4FF9-92EF-03F2C8F9D91B | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-06-28 16:56:08 | 2023-06-28 16:56:08 | False | False | NULL | 10.54.25.77 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 3D51ED70-F730-415E-A96C-4C15657C27EE | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-26 10:48:39 | 2023-06-26 10:48:39 | False | False | NULL | 10.54.25.77 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 69628A45-DBC8-496D-9B73-F1A9F5339BA9 | 80534764-F53E-4106-81A8-D86849F6E75C | 59AAEDF6-FFC8-4064-BADB-5C85341AF7B3 | 2023-06-23 16:59:25 | 2023-06-23 17:59:01 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 69628A45-DBC8-496D-9B73-F1A9F5339BA9 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-23 16:59:25 | 2023-06-23 16:59:25 | False | False | NULL | 10.54.25.77 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 93F75FC0-B133-4B9C-AD5C-9E170F30D5F4 | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-06-22 18:42:10 | 2023-06-22 18:42:10 | False | False | NULL | 10.20.65.186 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| 30300291-8EEB-4308-96CF-1A27C7753CA6 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-22 18:34:09 | 2023-06-22 18:34:09 | False | False | NULL | 10.54.25.77 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |
| C33BBD42-D51D-482E-AAA1-5E4F17AA03B7 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-21 15:36:41 | 2023-06-21 15:36:41 | False | False | NULL | 10.54.25.77 | IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII... |

---


## dbo.Support_Executive_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| Area | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| UserID | varchar | YES | -1 | — |

---


## dbo.Support_Executive_Mst_Tbl_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| Area | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| UserID | varchar | YES | -1 | — |

---


## dbo.SystemDetails

**Primary Key:** ID  
**Row Count:** 157  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| HostName | varchar | YES | 100 | — |
| IPAddress | varchar | YES | 100 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Station | varchar | YES | 100 | — |
| MACAddress | varchar | YES | 100 | — |

### Top 10 Records

| ID | HostName | IPAddress | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 107B9D7E-3F6D-4560-B453-4605B3EBAFBA | ERPLDGPCRPC01 | 10.74.74.3 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |
| 0DF4114F-26E9-4258-B7CA-F16F133C399C | NRPLBIJCONTROOM | 10.14.151.173 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |
| 0D5AECBB-78D6-4421-B8BB-293FA8B0C1FA | NRPLPNPOPRSCC | 10.10.100.91 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |
| 0CD54B44-C7B3-4F96-99D5-59BBA2372285 | WRPLVGMCTRLDLB | 10.139.128.170 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |
| 0B8A9968-3A27-4A6F-AA9F-63BED1C9A184 | NRPLAMBOPRPC | 10.11.66.12 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |
| 0B79E24C-C346-4369-8369-D425282263C5 | ERPLJAS00510397 | 10.252.82.33 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |
| 0B5012B0-1D09-49F6-BFDB-91D00CC99693 | WRPLKDLCTRLROOM | 10.139.168.210 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |
| 08166AB0-AC4F-4DC1-8DF3-846E320AA487 | erplmgscontroom | 10.40.66.120 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |
| 07AD6E4E-B960-457F-AA58-24A2BDF8DFA4 | PHBPLCRSHIFT | 10.66.160.167 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |
| 0510D3E2-E035-4ED6-954F-78DC815A69C4 | SERPLPDPCNTRL | 10.102.66.148 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | HostName | IPAddress | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 107B9D7E-3F6D-4560-B453-4605B3EBAFBA | ERPLDGPCRPC01 | 10.74.74.3 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |
| 0DF4114F-26E9-4258-B7CA-F16F133C399C | NRPLBIJCONTROOM | 10.14.151.173 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |
| 0D5AECBB-78D6-4421-B8BB-293FA8B0C1FA | NRPLPNPOPRSCC | 10.10.100.91 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |
| 0CD54B44-C7B3-4F96-99D5-59BBA2372285 | WRPLVGMCTRLDLB | 10.139.128.170 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |
| 0B8A9968-3A27-4A6F-AA9F-63BED1C9A184 | NRPLAMBOPRPC | 10.11.66.12 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |
| 0B79E24C-C346-4369-8369-D425282263C5 | ERPLJAS00510397 | 10.252.82.33 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |
| 0B5012B0-1D09-49F6-BFDB-91D00CC99693 | WRPLKDLCTRLROOM | 10.139.168.210 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |
| 08166AB0-AC4F-4DC1-8DF3-846E320AA487 | erplmgscontroom | 10.40.66.120 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |
| 07AD6E4E-B960-457F-AA58-24A2BDF8DFA4 | PHBPLCRSHIFT | 10.66.160.167 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |
| 0510D3E2-E035-4ED6-954F-78DC815A69C4 | SERPLPDPCNTRL | 10.102.66.148 | 2872F583-6495-4CCC-93B3-98A4E63858A4 | NULL | 2022-10-13 17:22:26 | NULL | False | False | NULL |

---


## dbo.SystemDetails_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| HostName | varchar | YES | 100 | — |
| IPAddress | varchar | YES | 100 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Station | varchar | YES | 100 | — |
| MACAddress | varchar | YES | 100 | — |

---


## dbo.System_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 160  
**Date Range (ModifiedOn):** 2022-09-21 16:20:23 to 2023-09-26 16:18:56  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| StationID | varchar | YES | 360 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| SrNo | decimal | YES | 18,4 | — |
| State | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | StationID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F7982551-0F2C-4F30-82DD-B386E1FFA3CC | Kot  | 93F6D374-582F-4AB9-9A56-22521AF796B2 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-09-21 16:20:23 | 2022-09-21 16:20:23 | False | False | NULL |
| CBB47004-0120-469F-82E4-869953441EF2 | Allahabad_BKPL | B87B6A96-B0EF-4E2D-A7F1-DB4A2E70CE26 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-09-21 17:09:05 | 2022-09-21 17:09:05 | False | False | NULL |
| 8FE6B9A6-A991-4139-B1C5-4617E508F39E | Amlekhgunj_BKPL | 2A52F82E-B353-4509-B552-9567ED07F5BE | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-09-21 17:09:24 | 2022-09-21 17:09:24 | False | False | NULL |
| 467E1C46-E0C9-44EF-B6D5-DA105C8CFCBC | Baitalpur_BKPL | C7A40140-967D-4450-A2C8-3138532B3D84 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-09-21 17:09:41 | 2022-09-21 17:09:41 | False | False | NULL |
| EE115D32-8282-4222-8349-9B76DB9568E6 | Kanpur_BKPL | 42315322-5BEC-4DC4-B685-8B55CD4B5BC3 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-09-21 17:12:15 | 2022-09-21 17:12:14 | False | False | NULL |
| 945CE129-B889-4352-A905-B5189C4F2B35 | Lucknow_BKPL | DAD98851-E354-4977-8149-FB21A6B257F0 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-09-21 17:12:34 | 2022-09-21 17:12:34 | False | False | NULL |
| 3FDEDED2-BEB1-4621-BBED-83091A0A0B5C | Motihari_BKPL | 6E0317A8-52DD-49AD-8A0F-A7009D7BFF16 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-09-21 17:12:49 | 2022-09-21 17:12:49 | False | False | NULL |
| C8649C5B-7B60-45F4-A601-F1A6A915B710 | Mughalsarai_BKPL | C18AD720-F56E-4343-B1C1-6278E2F091DD | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-09-21 17:13:05 | 2022-09-21 17:13:05 | False | False | NULL |
| 5AF93EF5-BC70-44E8-851B-578E55D688C1 | Betkuchi_GSPL | 4AC37639-FCAC-4F07-AF24-EB9A3B7B9D77 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-09-21 17:14:26 | 2022-09-21 17:14:26 | False | False | NULL |
| 6F681383-3234-4A92-815E-35C60357B2F4 | Bongaigaon_GSPL | F3C9EADA-69FC-446F-8B44-278443138906 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-09-21 17:14:46 | 2022-09-21 17:14:46 | False | False | NULL |

### Bottom 10 Records

| ID | Name | StationID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 326CE484-72DA-4606-92FB-49CB6E0914B7 | Koyali_CD | 64A10424-982A-47A1-B810-FC5C3987A2AE | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 80534764-F53E-4106-81A8-D86849F6E75C | 2022-09-26 11:57:39 | 2023-09-26 16:18:56 | False | False | NULL |
| 0C555ACB-F59D-45E2-B769-E86DB7AA9840 | Manmad_KASPL | 0686F81F-DC2D-417D-BCE7-4330682A7AC5 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-03-18 11:32:38 | 2023-09-26 16:18:41 | False | False | NULL |
| F0BC31B8-5100-45AF-89E5-9DF49C88D4D6 | Patna_PHBMPL | 5393B4AF-04D5-40DF-A20B-04E70F161950 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-09-01 18:57:18 | 2023-09-01 18:57:18 | False | False | NULL |
| 81BE9DA1-0183-48C1-9D83-F36B207463B8 | Barauni_PHBMPL | E51CE38B-0AD6-4DD2-B25C-527C6415C500 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-09-01 18:56:56 | 2023-09-01 18:56:56 | False | False | NULL |
| D24D04DE-20C6-483A-98D9-5E3CF4B97595 | Solapur_KASPL | BF6B79B6-1095-4256-AB15-2FA79E468EF0 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-09-01 18:56:12 | 2023-09-01 18:56:12 | False | False | NULL |
| 8FF0BDC3-E935-458E-8D90-1899E9273677 | Hyderabad_PHPL | 8EC26FB2-8076-441B-96BC-FB3D4BB2FA3C | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-09-01 18:55:53 | 2023-09-01 18:55:53 | False | False | NULL |
| 924B98DD-6FF9-4FD5-A46C-987450FE970E | Muzaffarpur_PHBMPL | F7948581-A987-4E6C-A8F9-747E5F218319 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-09-01 18:55:28 | 2023-09-01 18:55:28 | False | False | NULL |
| 99B3ED6E-A767-4DBF-A483-BFCD9696ED23 | Motihari_PHBMPL | B836C497-3A21-468D-9C75-8165D5309C5D | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-09-01 18:55:07 | 2023-09-01 18:55:07 | False | False | NULL |
| D74452A6-570D-44AB-B3EF-7E5BD4846F9A | Ahmednagar_KASPL | EFC0155E-C38E-4863-9BE7-33FDD92E0056 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-09-01 18:54:28 | 2023-09-01 18:54:28 | False | False | NULL |
| 9D5688AB-327D-4250-8884-54CEEE2188C2 | Haldia_PSHPL | B96849FA-50A5-4C1B-A7E8-4EE354A3532C | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-09-01 17:43:55 | 2023-09-01 17:43:55 | False | False | NULL |

---


## dbo.System_Mst_Tbl_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| StationID | varchar | YES | 360 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| SrNo | decimal | YES | 18,4 | — |
| State | varchar | YES | 100 | — |

---


## dbo.TicketScheme_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 2  
**Date Range (ModifiedOn):** 2022-09-22 16:16:03 to 2025-08-11 13:42:12  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| SrNo | int | YES | 10,0 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Name | varchar | YES | 100 | — |

### Top 10 Records

| ID | SrNo | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 45A72989-C5D0-4C66-B741-7A6738C39D03 | 326 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-09-19 14:12:03 | 2022-09-22 16:16:03 | True | False | NULL | 10.54.25.77 |
| 5F31539B-2536-4041-AB6B-A09142A1E08F | 242 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2022-08-12 13:12:37 | 2025-08-11 13:42:12 | False | False | NULL | 172.16.100.58 |

---


## dbo.TicketScheme_Mst_Tbl_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| SrNo | int | YES | 10,0 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Name | varchar | YES | 100 | — |

---


## dbo.UAT_ACCESSDENIAL

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_ACCESSDENIAL_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_ALLOYADDITIONRECORD

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_ALLOYADDITIONRECORD_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_AUDITTRAILLOGGING

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_AUDITTRAILLOGGING_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_AUTOCLOSE

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_AUTOCLOSE_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_AUTOPRODUCTIONORDER

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_AUTOPRODUCTIONORDER_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_AVAILABILITYPERSHIFT

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:35:10 to 2025-11-15 08:56:26  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7FB090FC-880B-4CD7-B8EC-09D8B96C717F | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:35:10 | 2025-11-15 08:35:10 | False | False | NULL | 172.16.7.110 |  |
| 2036029A-464D-4C9B-8C98-D0972FFB69E3 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:36:25 | 2025-11-15 08:36:25 | False | False | NULL |  |  |
| 79D4EAC4-957A-403C-A941-2E7286C3144B | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:56:26 | 2025-11-15 08:56:26 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_AVAILABILITYPERSHIFT_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_BATTERYBANKANDDGSTATUSLOGSHEET

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:44:11 to 2025-11-15 09:03:04  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Fileupload | varchar | YES | 8000 | — |
| EntryDateTime | datetime | YES | — | — |
| Q1Verdict | bit | YES | — | — |
| Q2Verdict | bit | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| Q2 | varchar | YES | -1 | — |
| Q3 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| TestName | varchar | YES | -1 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C155A40F-F648-42B5-B02B-2CC9ED78E201 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:44:11 | 2025-11-15 08:44:11 | False | False | NULL | 172.16.7.110 |  |
| 860D7D58-BFAB-4DBB-9303-08652BFC0CBF | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:45:58 | 2025-11-15 08:45:58 | False | False | NULL |  |  |
| 075EA4BC-B4C1-43BF-891F-BA5C7A835193 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:03:04 | 2025-11-15 09:03:04 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_BATTERYBANKANDDGSTATUSLOGSHEET_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Fileupload | varchar | YES | 8000 | — |
| EntryDateTime | datetime | YES | — | — |
| Q1Verdict | bit | YES | — | — |
| Q2Verdict | bit | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| Q2 | varchar | YES | -1 | — |
| Q3 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| TestName | varchar | YES | -1 | — |

---


## dbo.UAT_CAPACITORBANKLOGSHEET

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:44:33 to 2025-11-15 09:03:18  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Fileupload | varchar | YES | 8000 | — |
| EntryDateTime | datetime | YES | — | — |
| Q1Verdict | bit | YES | — | — |
| Q2Verdict | bit | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| Q2 | varchar | YES | -1 | — |
| Q3 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| TestName | varchar | YES | -1 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2B757AC6-530C-44C8-BD5D-2C2B26FD49EE | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:44:33 | 2025-11-15 08:44:33 | False | False | NULL | 172.16.7.110 |  |
| 9CDED679-ED2A-4473-B9A1-F160BABC2963 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:46:11 | 2025-11-15 08:46:11 | False | False | NULL |  |  |
| 0A758793-717D-4553-B0A1-42420F5314AC | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:03:18 | 2025-11-15 09:03:18 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_CAPACITORBANKLOGSHEET_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Fileupload | varchar | YES | 8000 | — |
| EntryDateTime | datetime | YES | — | — |
| Q1Verdict | bit | YES | — | — |
| Q2Verdict | bit | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| Q2 | varchar | YES | -1 | — |
| Q3 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| TestName | varchar | YES | -1 | — |

---


## dbo.UAT_CCM_CASTINGSPEEDPERSTRAND

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2025-09-04 12:44:09 to 2025-11-15 08:55:32  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFAE35E6-8EA8-44E2-8AAB-1130762678F6 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-09-04 12:44:09 | 2025-09-04 12:44:09 | False | False | NULL | 172.16.7.23 |  |
| 9FAF22D6-D416-418C-83E6-39CC55DD58C2 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-15 08:11:03 | 2025-11-15 08:11:03 | False | False | NULL |  |  |
| 3442892F-7E92-42C8-B966-F3849AED1BF1 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:33:04 | 2025-11-15 08:33:04 | False | False | NULL | 172.16.7.110 |  |
| 51415605-D18F-458A-A019-87256CDE2E58 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:34:38 | 2025-11-15 08:34:38 | False | False | NULL |  |  |
| DE9EA691-ABD1-4D36-B3E1-273B3AE6BD89 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:55:32 | 2025-11-15 08:55:32 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_CCM_CASTINGSPEEDPERSTRAND_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_CCM_LADLEDETAILSLOGSHEET

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2025-08-13 17:22:53 to 2025-11-15 09:04:31  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B8CF9DCE-6380-43C9-BE64-F86E06219619 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2025-08-13 17:22:53 | 2025-08-13 17:22:53 | False | False | NULL | 172.16.4.38 |  |
| DC6CE9F7-2DD3-4B4B-9DF0-E311A2A9CFD1 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:45:50 | 2025-11-15 08:45:50 | False | False | NULL | 172.16.7.110 |  |
| 5C0E1520-3856-40AD-95DA-835A5A36C714 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:47:46 | 2025-11-15 08:47:46 | False | False | NULL |  |  |
| 05706000-4A61-418C-9950-2557EA6685FF | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:04:31 | 2025-11-15 09:04:31 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_CCM_LADLEDETAILSLOGSHEET_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_CCM_LIVEDATADASHABORD

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2025-08-28 11:01:06 to 2025-11-15 08:58:01  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5A17C064-F0C1-4AC9-8D92-E66CBD6E6068 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-08-28 11:01:06 | 2025-08-28 11:01:06 | False | False | NULL | 172.16.4.40 |  |
| 35E463AE-B4E8-4F79-9208-75C9D958ACB3 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-15 08:14:46 | 2025-11-15 08:14:46 | False | False | NULL |  |  |
| F3D06E4B-C1E7-4FD8-A52A-B431611AE261 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:37:43 | 2025-11-15 08:37:43 | False | False | NULL | 172.16.7.110 |  |
| E8C05F18-5CA0-482D-A940-72D9CD6D9554 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:39:52 | 2025-11-15 08:39:52 | False | False | NULL |  |  |
| 6934DD2A-0896-4235-9FE2-8A4A2EF4DD86 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:58:01 | 2025-11-15 08:58:01 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_CCM_LIVEDATADASHABORD_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_CCM_LOGBOOKDATADASHBOARD

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2025-09-04 12:53:54 to 2025-11-15 09:00:34  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C8DC5830-AE10-44E6-9A19-D90DC31D24CB | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-09-04 12:53:54 | 2025-09-04 12:53:54 | False | False | NULL | 172.16.7.23 |  |
| 20A16556-6A5B-40A2-874F-F52BB8B19B13 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:40:51 | 2025-11-15 08:40:51 | False | False | NULL | 172.16.7.110 |  |
| 0D39DB07-E2E9-4E0B-938B-1CFA4CC67D01 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:42:23 | 2025-11-15 08:42:23 | False | False | NULL |  |  |
| 9AD22EE1-55C3-4335-A177-15BB4A769777 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:00:34 | 2025-11-15 09:00:34 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_CCM_LOGBOOKDATADASHBOARD_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_CCM_MANUALENTRYLOGBOOK

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:47:29 to 2025-11-15 09:06:26  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 52818415-797E-4426-A575-2A3A843EE817 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:47:29 | 2025-11-15 08:47:29 | False | False | NULL | 172.16.7.110 |  |
| 70319BE6-AE99-47EC-B8E3-5AE92BE4A8AA | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:50:35 | 2025-11-15 08:50:35 | False | False | NULL |  |  |
| 0B2D21F9-4D1B-47A9-B0D0-01D1E63A3AA8 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:06:26 | 2025-11-15 09:06:26 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_CCM_MANUALENTRYLOGBOOK_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_CCM_MANULENTRYLOGBOOK

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_CCM_MANULENTRYLOGBOOK_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_CCM_NOOFBILETSPERHEAT

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2025-09-04 13:06:34 to 2025-11-15 08:55:40  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q3Verdict | bit | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Comments | varchar | YES | -1 | — |
| EntryDateTime | datetime | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| TestName | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1Verdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| Q2Verdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| OverallVerdict | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C73E8519-0B1B-4152-B847-B641763C5659 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-09-04 13:06:34 | 2025-09-04 13:06:34 | False | False | NULL | 172.16.7.23 |  |
| 54106D9E-B6AB-4603-819E-FE22340A4953 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-15 08:11:14 | 2025-11-15 08:11:14 | False | False | NULL |  |  |
| 9879FD19-A628-4328-972B-1C8D857143C7 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:33:13 | 2025-11-15 08:33:13 | False | False | NULL | 172.16.7.110 |  |
| 1977BDAA-187F-4710-AD01-F581D3F088CA | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:34:56 | 2025-11-15 08:34:56 | False | False | NULL |  |  |
| 641C2CEC-B5E6-4E4C-A768-A571F8D9AD0C | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:55:40 | 2025-11-15 08:55:40 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_CCM_NOOFBILETSPERHEAT_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q3Verdict | bit | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Comments | varchar | YES | -1 | — |
| EntryDateTime | datetime | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| TestName | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1Verdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| Q2Verdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| OverallVerdict | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_CCM_OSCILLATIONPERSTRAND

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2025-09-04 12:41:34 to 2025-11-15 08:56:09  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 812EF678-D0B8-447F-888E-5D61033EA759 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-09-04 12:41:34 | 2025-09-04 12:41:34 | False | False | NULL | 172.16.7.23 |  |
| 808EE479-D0FD-4BD9-9639-20758B5D43AB | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-15 08:11:35 | 2025-11-15 08:11:35 | False | False | NULL |  |  |
| 30194E95-7AD0-4711-AF66-7C5DF60002DF | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:34:39 | 2025-11-15 08:34:39 | False | False | NULL | 172.16.7.110 |  |
| BBC40777-3FC1-446B-82EF-827EA0A81124 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:35:45 | 2025-11-15 08:35:45 | False | False | NULL |  |  |
| 1E78B0D0-24E2-442B-9289-79AA30616663 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:56:09 | 2025-11-15 08:56:09 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_CCM_OSCILLATIONPERSTRAND_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_CCM_QUALITYDATADASHBOARD

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:40:14 to 2025-11-15 08:59:14  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 94B3F854-914D-43ED-B6F0-62757B7A9E52 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:40:14 | 2025-11-15 08:40:14 | False | False | NULL | 172.16.7.110 |  |
| C5A6E344-E8EE-4EA3-8F9B-04BDE8E837D7 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:41:37 | 2025-11-15 08:41:37 | False | False | NULL |  |  |
| 7D7E95DC-C533-4B64-9D13-2B638E27D784 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:59:14 | 2025-11-15 08:59:14 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_CCM_QUALITYDATADASHBOARD_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_CCM_SECTIONSTRANDSDATALOGSHEET

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:46:00 to 2025-11-15 09:04:47  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 864B7CC9-3725-4894-BD1C-B600709B6FE4 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:46:00 | 2025-11-15 08:46:00 | False | False | NULL | 172.16.7.110 |  |
| 8440FC20-41B2-4625-A953-58CEC9D629DC | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:48:00 | 2025-11-15 08:48:00 | False | False | NULL |  |  |
| 9DAFBDAA-8040-4251-9682-6D71362A200D | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:04:47 | 2025-11-15 09:04:47 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_CCM_SECTIONSTRANDSDATALOGSHEET_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_CCM_SHIFTPRODUCTIVITYREPORT

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:34:58 to 2025-11-15 08:56:17  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F45C2C36-DFC6-453F-93C2-475A3F47DEAE | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:34:58 | 2025-11-15 08:34:58 | False | False | NULL | 172.16.7.110 |  |
| 2F3EF1B3-805F-4052-BD28-C3218F1E38C1 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:36:12 | 2025-11-15 08:36:12 | False | False | NULL |  |  |
| 0E2E06F7-9DD8-4E68-9BFD-590350BFBEB0 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:56:17 | 2025-11-15 08:56:17 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_CCM_SHIFTPRODUCTIVITYREPORT_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_CCM_SHIFTWISEDATADASHBOARD

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2025-09-04 13:03:29 to 2025-11-15 08:58:33  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4BB8B6F6-3398-4BBE-AD95-BD5501792BAB | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-09-04 13:03:29 | 2025-09-04 13:03:29 | False | False | NULL | 172.16.7.23 |  |
| 35F87033-ECAB-4AFE-92D5-C7AFC5B6B60E | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:38:44 | 2025-11-15 08:38:44 | False | False | NULL | 172.16.7.110 |  |
| FE3D0580-3DB3-4299-956A-A53B16A57F2C | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:40:40 | 2025-11-15 08:40:40 | False | False | NULL |  |  |
| 6ACFBAFC-647D-4807-98A4-BBF6434FD27A | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:58:33 | 2025-11-15 08:58:33 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_CCM_SHIFTWISEDATADASHBOARD_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_CCM_SHORTBILETSGENERATED

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:33:42 to 2025-11-15 08:55:51  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F929E90B-4DB2-44DE-81C4-17B35F0BEDAC | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:33:42 | 2025-11-15 08:33:42 | False | False | NULL | 172.16.7.110 |  |
| EC81EF8B-DBC5-48E7-9306-BA2E96988C46 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:35:09 | 2025-11-15 08:35:09 | False | False | NULL |  |  |
| 1342E17A-63B1-47B3-A4F0-44686F6FBAD7 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:55:51 | 2025-11-15 08:55:51 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_CCM_SHORTBILETSGENERATED_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_CCM_WATERFLOWZONEWISE

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2025-11-15 08:11:26 to 2025-11-15 08:56:01  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BC9948A9-5562-4130-B593-70B6A7CBBFD2 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-15 08:11:26 | 2025-11-15 08:11:26 | False | False | NULL |  |  |
| 7BE95967-A6C4-4C4F-B3D8-573509B53B09 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:34:08 | 2025-11-15 08:34:08 | False | False | NULL | 172.16.7.110 |  |
| 8CFEDEC3-A8C9-47CD-A9DA-3EA7A592444A | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:35:23 | 2025-11-15 08:35:23 | False | False | NULL |  |  |
| B74C0BD5-B5EC-46F4-8CF9-37F220F6FA31 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:56:01 | 2025-11-15 08:56:01 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_CCM_WATERFLOWZONEWISE_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_DELAYSPERSHIFT

**Primary Key:** ID  
**Row Count:** 6  
**Date Range (ModifiedOn):** 2025-08-12 17:27:59 to 2025-11-15 08:56:33  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 57C49BE9-65CE-4F40-98BF-B321FF31B78A | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 2025-08-12 17:27:59 | 2025-08-12 17:27:59 | False | False | NULL | 172.16.6.149 |  |
| 5A2C3B98-3DDF-4B6E-827D-344F01F94A3B | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-10-29 10:21:26 | 2025-10-29 10:21:26 | False | False | NULL | 172.16.10.102 |  |
| 55C0903A-5F76-4951-A418-62E03F23C550 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-15 08:11:50 | 2025-11-15 08:11:50 | False | False | NULL |  |  |
| 1C898413-4F56-4FF0-9D49-1C8DE1C3A86D | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:35:21 | 2025-11-15 08:35:21 | False | False | NULL | 172.16.7.110 |  |
| 9FB325AC-B046-4AE2-86DC-E89D1240DCBB | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:36:51 | 2025-11-15 08:36:51 | False | False | NULL |  |  |
| 41CA11D5-D061-492D-9FEE-D20A6F98FCC7 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:56:33 | 2025-11-15 08:56:33 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_DELAYSPERSHIFT_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_DUPLICATESIGNALHANDLING

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_DUPLICATESIGNALHANDLING_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_EAFTOLRFHEATTRANSFER

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2025-08-13 17:43:27 to 2025-11-15 08:57:14  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B6B708B5-55F5-425B-84E8-C293F1B6A82B | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2025-08-13 17:43:27 | 2025-08-13 17:43:27 | False | False | NULL | 172.16.4.38 |  |
| 761625AC-7790-44BE-8EE7-8D05ABE0E29C | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-15 08:13:21 | 2025-11-15 08:13:21 | False | False | NULL |  |  |
| D55E7C69-FD3D-4FDB-827F-C95818646B07 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:36:08 | 2025-11-15 08:36:08 | False | False | NULL | 172.16.7.110 |  |
| CDD58173-F52B-47AF-A355-669325EED583 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:38:33 | 2025-11-15 08:38:33 | False | False | NULL |  |  |
| AC4BF408-E621-4B6A-8979-27102F849709 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:57:14 | 2025-11-15 08:57:14 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_EAFTOLRFHEATTRANSFER_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_EAF_CONSUMPTIONDATALOGSHEET

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:44:58 to 2025-11-15 09:03:45  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Fileupload | varchar | YES | 8000 | — |
| EntryDateTime | datetime | YES | — | — |
| Q1Verdict | bit | YES | — | — |
| Q2Verdict | bit | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| Q2 | varchar | YES | -1 | — |
| Q3 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| TestName | varchar | YES | -1 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 444FA145-4BB1-4990-BAE5-12C32B0AD1ED | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:44:58 | 2025-11-15 08:44:58 | False | False | NULL | 172.16.7.110 |  |
| 0EC78B7E-3567-4D9E-91A2-2D3886A2A337 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:46:36 | 2025-11-15 08:46:36 | False | False | NULL |  |  |
| 88949DBB-6EDD-476F-91C1-5B2A5D1E6940 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:03:45 | 2025-11-15 09:03:45 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_EAF_CONSUMPTIONDATALOGSHEET_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Fileupload | varchar | YES | 8000 | — |
| EntryDateTime | datetime | YES | — | — |
| Q1Verdict | bit | YES | — | — |
| Q2Verdict | bit | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| Q2 | varchar | YES | -1 | — |
| Q3 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| TestName | varchar | YES | -1 | — |

---


## dbo.UAT_EAF_DELAYTYPEMASTERLOGBOOK

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:47:07 to 2025-11-15 09:06:03  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0D76BE3F-507D-4104-BB06-AA95A0C9F88D | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:47:07 | 2025-11-15 08:47:07 | False | False | NULL | 172.16.7.110 |  |
| DF4B9075-CF06-4956-87FF-FE8CBD3C8BBE | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:50:01 | 2025-11-15 08:50:01 | False | False | NULL |  |  |
| 99D07B01-79B9-409D-9586-5DC01F628636 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:06:03 | 2025-11-15 09:06:03 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_EAF_DELAYTYPEMASTERLOGBOOK_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_EAF_ELECTRODECONSUMPTIONPERHEAT

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2025-08-12 17:20:54 to 2025-11-15 08:54:30  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6DFD74CD-99FF-46AA-B5EA-C48EA6D1B108 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2025-08-12 17:20:54 | 2025-08-12 17:20:54 | False | False | NULL | 172.16.4.38 |  |
| EF5CA8F3-0718-472F-9F64-DF84E1BA80B7 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:32:10 | 2025-11-15 08:32:10 | False | False | NULL | 172.16.7.110 |  |
| 20D9F87E-32C6-4D95-AF8E-525231F20379 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:32:39 | 2025-11-15 08:32:39 | False | False | NULL |  |  |
| FAECC84D-BBFE-4E7D-BD7E-5643DEE5EFF7 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:54:30 | 2025-11-15 08:54:30 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_EAF_ELECTRODECONSUMPTIONPERHEAT_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_EAF_LADLEADDITIONLOGSHEET

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2025-08-13 17:24:36 to 2025-11-15 09:04:09  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E3943EFF-FE5E-4020-B3B1-5A98B584CF47 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2025-08-13 17:24:36 | 2025-08-13 17:24:36 | False | False | NULL | 172.16.4.38 |  |
| AADBAF13-C5F0-4D39-BAE7-CE2D4B87ABD6 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:45:24 | 2025-11-15 08:45:24 | False | False | NULL | 172.16.7.110 |  |
| F028D2D8-55C5-4F5F-8D72-49C7FB0C7214 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:47:08 | 2025-11-15 08:47:08 | False | False | NULL |  |  |
| D62CA1F1-E286-4C9B-AE37-EB60DEE870FD | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:04:09 | 2025-11-15 09:04:09 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_EAF_LADLEADDITIONLOGSHEET_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_EAF_LADLEDETAILSLOGSHEET

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:45:13 to 2025-11-15 09:03:58  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EE32D7B3-216A-4828-8EA8-FBB39E0A3F20 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:45:13 | 2025-11-15 08:45:13 | False | False | NULL | 172.16.7.110 |  |
| D16850FE-44B3-4BD7-99DB-959A5ECE44F0 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:46:50 | 2025-11-15 08:46:50 | False | False | NULL |  |  |
| 0B0C3851-D18C-4B5C-A9C2-B95EB0492E79 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:03:58 | 2025-11-15 09:03:58 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_EAF_LADLEDETAILSLOGSHEET_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_EAF_LIVEDATADASHBOARD

**Primary Key:** ID  
**Row Count:** 10  
**Date Range (ModifiedOn):** 2025-08-13 17:12:49 to 2025-11-15 09:07:03  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 02B4DED7-F821-4874-BAE0-478FA79E24F4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2025-08-13 17:12:49 | 2025-08-13 17:12:49 | False | False | NULL | 172.16.4.38 |  |
| 155CC48A-CAB6-4CA9-A8FF-8BA4F43397DB | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2025-08-13 17:50:20 | 2025-08-13 17:50:20 | False | False | NULL | 172.16.4.38 |  |
| 9A9A7278-F7E2-4869-A5DB-7998413D63E8 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-08-28 10:50:06 | 2025-08-28 10:50:06 | False | False | NULL | 172.16.4.40 |  |
| 6884E91C-8835-42A4-B750-40B90B5CEE87 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-15 08:14:16 | 2025-11-15 08:14:16 | False | False | NULL |  |  |
| 0C4F7EF5-B7B1-4F7A-9DF6-FC4286008624 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:37:19 | 2025-11-15 08:37:19 | False | False | NULL | 172.16.7.110 |  |
| AC313D4D-858D-4B97-91B2-B8922DD8DEA9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:39:25 | 2025-11-15 08:39:25 | False | False | NULL |  |  |
| A2A68882-BEB1-4EAD-B6A1-368DF6E056D1 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:48:45 | 2025-11-15 08:48:45 | False | False | NULL | 172.16.7.110 |  |
| D37970DC-C3C8-4D22-9B62-21253132F3D8 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:52:26 | 2025-11-15 08:52:26 | False | False | NULL |  |  |
| 7162DA4D-5910-46C1-BAF6-EB8DA0DA70FF | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:57:42 | 2025-11-15 08:57:42 | False | False | NULL | 172.16.6.41 |  |
| B018CDF4-1E44-43C5-B1D6-30455879CD98 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:07:03 | 2025-11-15 09:07:03 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_EAF_LIVEDATADASHBOARD_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_EAF_LOGBOOKDATADASHBOARD

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:40:29 to 2025-11-15 09:00:11  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F9DD15CB-A022-41F9-9D4A-B88807C9AC05 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:40:29 | 2025-11-15 08:40:29 | False | False | NULL | 172.16.7.110 |  |
| 6273681A-7948-48E3-BFFA-5BCC0EB6A87A | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:41:51 | 2025-11-15 08:41:51 | False | False | NULL |  |  |
| 3BDDBE00-AC15-4FF8-8012-962117DF5D7A | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:00:11 | 2025-11-15 09:00:11 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_EAF_LOGBOOKDATADASHBOARD_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_EAF_MANUALENTRYLOGBOOK

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:46:44 to 2025-11-15 09:05:39  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F6B37A03-FB42-4F3B-AE49-2CCEE6E71706 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:46:44 | 2025-11-15 08:46:44 | False | False | NULL | 172.16.7.110 |  |
| D7823B0F-C60A-4AA7-AEB7-A466DA8F8313 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:49:13 | 2025-11-15 08:49:13 | False | False | NULL |  |  |
| D9CD91AF-1D7E-4318-A447-65F0E08B5101 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:05:39 | 2025-11-15 09:05:39 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_EAF_MANUALENTRYLOGBOOK_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_EAF_NGCONSUMPTIONPERTON

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:35:41 to 2025-11-15 08:56:51  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4E1C1350-19A2-4DCB-AC71-34ED8318F872 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:35:41 | 2025-11-15 08:35:41 | False | False | NULL | 172.16.7.110 |  |
| 9633BD1D-D987-48C1-B2D4-DB71A0D6F9A7 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:37:54 | 2025-11-15 08:37:54 | False | False | NULL |  |  |
| 03FF304E-597E-4213-8039-ED9C34637348 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:56:51 | 2025-11-15 08:56:51 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_EAF_NGCONSUMPTIONPERTON_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_EAF_NOOFHEAT

**Primary Key:** ID  
**Row Count:** 7  
**Date Range (ModifiedOn):** 2025-08-11 15:20:17 to 2025-11-15 08:54:08  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| TestName | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| TesterName | varchar | YES | -1 | — |
| Q1Verdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Comments | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | TestName | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0A6183EA-0AF8-461C-A29A-62C4103AD8BC | D9387246-73A3-433A-8BBB-008F6C43CB38 | AE3A3D8B-EA93-450A-934E-BABBD698DA6B | AE3A3D8B-EA93-450A-934E-BABBD698DA6B | 2025-08-11 15:20:17 | 2025-08-11 15:20:17 | False | False | NULL | 172.16.100.58 |
| 4A5BF1B8-473B-4E4B-9B82-B0AA774BFBF1 | D9387246-73A3-433A-8BBB-008F6C43CB38 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-08-28 10:27:54 | 2025-08-28 10:27:54 | False | False | NULL | 172.16.6.195 |
| A4CCDAF7-A7DC-4007-99B3-51E80351190B | D9387246-73A3-433A-8BBB-008F6C43CB38 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-15 08:09:46 | 2025-11-15 08:09:46 | False | False | NULL |  |
| AAA72638-D576-4F0A-88E9-997AE8D7F8E9 | D9387246-73A3-433A-8BBB-008F6C43CB38 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-15 08:30:45 | 2025-11-15 08:30:45 | False | False | NULL |  |
| E987FA54-7441-4FE3-95B1-0F069D8E7948 | D9387246-73A3-433A-8BBB-008F6C43CB38 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:31:40 | 2025-11-15 08:31:40 | False | False | NULL | 172.16.7.110 |
| A43ADB5C-947C-466D-A9BB-3BEEE3146002 | D9387246-73A3-433A-8BBB-008F6C43CB38 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:32:21 | 2025-11-15 08:32:21 | False | False | NULL |  |
| 3C164082-904D-4D78-B002-8FF796E6827E | D9387246-73A3-433A-8BBB-008F6C43CB38 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:54:08 | 2025-11-15 08:54:08 | False | False | NULL | 172.16.6.41 |

---


## dbo.UAT_EAF_NOOFHEAT_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| TestName | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| TesterName | varchar | YES | -1 | — |
| Q1Verdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Comments | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_EAF_POWERPERTON_1

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2025-08-28 10:37:15 to 2025-11-15 08:54:22  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F0BEFE1D-1FE6-4AB0-BE88-740A57677EA6 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-08-28 10:37:15 | 2025-08-28 10:37:15 | False | False | NULL | 172.16.4.40 |  |
| BD86D074-E578-4F58-8570-4BC4649A452B | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-15 08:10:10 | 2025-11-15 08:10:10 | False | False | NULL |  |  |
| 9F4EB63F-86B0-4885-BA4D-28E3DF7D2539 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:31:56 | 2025-11-15 08:31:56 | False | False | NULL | 172.16.7.110 |  |
| F7D8DD11-0A10-4CED-92DF-2EF68853C822 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:32:01 | 2025-11-15 08:32:01 | False | False | NULL |  |  |
| C9C0A991-60E0-4FBB-92C2-A69F45EEE30C | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:54:22 | 2025-11-15 08:54:22 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_EAF_POWERPERTON_1_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_EAF_QUALITYDATADASHBOARD

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:38:58 to 2025-11-15 08:58:51  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 321235CF-7A33-4FCB-828D-CC83C72C5398 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:38:58 | 2025-11-15 08:38:58 | False | False | NULL | 172.16.7.110 |  |
| 0C9694DA-A21F-4B73-89DB-CA7BF31C2B11 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:40:57 | 2025-11-15 08:40:57 | False | False | NULL |  |  |
| 5351701A-4778-40D8-A217-30CDB41AE6E0 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:58:51 | 2025-11-15 08:58:51 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_EAF_QUALITYDATADASHBOARD_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_EAF_QUALITYDATALOGSHEET

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:44:46 to 2025-11-15 09:03:30  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Fileupload | varchar | YES | 8000 | — |
| EntryDateTime | datetime | YES | — | — |
| Q1Verdict | bit | YES | — | — |
| Q2Verdict | bit | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| Q2 | varchar | YES | -1 | — |
| Q3 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| TestName | varchar | YES | -1 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C59B7E80-5703-453D-93A4-159993270135 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:44:46 | 2025-11-15 08:44:46 | False | False | NULL | 172.16.7.110 |  |
| 2C5881EE-41DA-40AE-8AAB-DB900A4E049B | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:46:23 | 2025-11-15 08:46:23 | False | False | NULL |  |  |
| 8091FD1C-BA8C-429C-B328-1ECEBEC7E125 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:03:30 | 2025-11-15 09:03:30 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_EAF_QUALITYDATALOGSHEET_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Fileupload | varchar | YES | 8000 | — |
| EntryDateTime | datetime | YES | — | — |
| Q1Verdict | bit | YES | — | — |
| Q2Verdict | bit | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| Q2 | varchar | YES | -1 | — |
| Q3 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| TestName | varchar | YES | -1 | — |

---


## dbo.UAT_EAF_REACTORLOGSHEET

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:41:55 to 2025-11-15 09:01:37  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 455116D0-F2FA-4EC9-8356-758119FDE414 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:41:55 | 2025-11-15 08:41:55 | False | False | NULL | 172.16.7.110 |  |
| B28F3795-8B44-4CDB-9DE9-155A7FFB2755 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:43:53 | 2025-11-15 08:43:53 | False | False | NULL |  |  |
| 3F2EC5B9-A28A-4892-90B8-17437067BC1B | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:01:37 | 2025-11-15 09:01:37 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_EAF_REACTORLOGSHEET_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_EAF_SHIFTDELAYENTRYLOGBOOK

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:46:54 to 2025-11-15 09:05:49  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5C66F6AF-FE3A-4C5F-B2CF-505AB51C2481 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:46:54 | 2025-11-15 08:46:54 | False | False | NULL | 172.16.7.110 |  |
| 8468509B-B7A3-44B6-8885-FD53ADC35BCC | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:49:42 | 2025-11-15 08:49:42 | False | False | NULL |  |  |
| 66966314-6CD7-405B-BA0A-F75BBA09F174 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:05:49 | 2025-11-15 09:05:49 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_EAF_SHIFTDELAYENTRYLOGBOOK_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_EAF_SHIFTWISEDATADASHBOARD

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2025-08-28 11:14:05 to 2025-11-15 08:58:09  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1D91334-1973-4D29-9D2B-B4ACB88B122B | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-08-28 11:14:05 | 2025-08-28 11:14:05 | False | False | NULL | 172.16.4.40 |  |
| 8B3C5B67-EE57-49E4-A319-96D720A4A8C7 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-08-28 11:16:08 | 2025-08-28 11:16:08 | False | False | NULL | 172.16.4.40 |  |
| 1902FF17-C481-40AE-8427-B44813B89B0D | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:37:53 | 2025-11-15 08:37:53 | False | False | NULL | 172.16.7.110 |  |
| B42BB413-5FCF-4752-812D-1279D4947988 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:40:05 | 2025-11-15 08:40:05 | False | False | NULL |  |  |
| 7DDD867D-6522-4765-90E9-B81C022AE0BB | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:58:09 | 2025-11-15 08:58:09 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_EAF_SHIFTWISEDATADASHBOARD_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_EAF_TRANSFORMERLOGSHEET

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2025-10-11 10:51:25 to 2025-11-15 09:01:23  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2A9892B9-1332-4A86-951B-7919ADA60EB4 | 83E3F386-31EE-476F-9651-39B924B01514 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-10-11 10:51:25 | 2025-10-11 10:51:25 | False | False | NULL | 172.16.6.215 |  |
| DFF9F347-6B91-4F77-991E-02A12B70F4F3 | 83E3F386-31EE-476F-9651-39B924B01514 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-10-11 10:54:16 | 2025-10-11 10:54:16 | False | False | NULL | 172.16.6.215 |  |
| A65CA3B5-5488-4C21-9290-A8F7C4B93939 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:41:40 | 2025-11-15 08:41:40 | False | False | NULL | 172.16.7.110 |  |
| EC00737D-EB94-478D-B551-BF68CD57BA7F | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:43:35 | 2025-11-15 08:43:35 | False | False | NULL |  |  |
| 90C34BB7-2BF3-4C1D-B174-B81968502922 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:01:23 | 2025-11-15 09:01:23 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_EAF_TRANSFORMERLOGSHEET_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_EAF_YIELDPERHEAT

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2025-08-12 17:28:24 to 2025-11-15 08:54:43  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q2Verdict | bit | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| OverallVerdict | bit | YES | — | — |
| Q1Verdict | bit | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| TestName | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DC663763-1EAF-4A5B-962E-03E8443158F6 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2025-08-12 17:28:24 | 2025-08-12 17:28:24 | False | False | NULL | 172.16.4.38 |  |
| C74DA436-39CE-49D3-A277-322051A7C991 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-15 08:10:24 | 2025-11-15 08:10:24 | False | False | NULL |  |  |
| 4EFD7342-3340-4A40-AF4F-88D627D8D0F5 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:32:18 | 2025-11-15 08:32:18 | False | False | NULL | 172.16.7.110 |  |
| 11DAC37F-0E2B-4288-BFE7-B6534675A85F | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:32:53 | 2025-11-15 08:32:53 | False | False | NULL |  |  |
| 85D1758C-6BC0-49A6-BC9E-329DBA8EB34A | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:54:43 | 2025-11-15 08:54:43 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_EAF_YIELDPERHEAT_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q2Verdict | bit | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| OverallVerdict | bit | YES | — | — |
| Q1Verdict | bit | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| TestName | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_ELECTRICALCHECKLISTREPORTS

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2025-08-12 20:48:22 to 2025-11-15 09:06:39  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| IsProcessed | bit | YES | — | — |
| Q4 | varchar | YES | -1 | — |
| Q3 | varchar | YES | -1 | — |
| Q2 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Fileupload | varchar | YES | 8000 | — |
| EntryDateTime | datetime | YES | — | — |
| Q4Response | bit | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| Q1Verdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| Q2Verdict | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 22D43AE5-F73F-4790-8F05-FFF49642710D | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 2025-08-12 20:48:22 | 2025-08-12 20:48:22 | False | False | NULL | 172.16.6.195 |  |
| A7179B35-F887-4D0D-BB12-74C8E625C3FD | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:47:42 | 2025-11-15 08:47:42 | False | False | NULL | 172.16.7.110 |  |
| 8DF9F7D4-B2AE-4D1C-9E8F-B5A35AF14FB5 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:50:51 | 2025-11-15 08:50:51 | False | False | NULL |  |  |
| 581045BD-07EE-4C67-9D08-0713256FF654 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:06:39 | 2025-11-15 09:06:39 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_ELECTRICALCHECKLISTREPORTS_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| IsProcessed | bit | YES | — | — |
| Q4 | varchar | YES | -1 | — |
| Q3 | varchar | YES | -1 | — |
| Q2 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Fileupload | varchar | YES | 8000 | — |
| EntryDateTime | datetime | YES | — | — |
| Q4Response | bit | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| Q1Verdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| Q2Verdict | bit | YES | — | — |

---


## dbo.UAT_ELECTRICAL_A_SHIFTCHECKLIST

**Primary Key:** ID  
**Row Count:** 7  
**Date Range (ModifiedOn):** 2025-08-12 21:43:43 to 2025-11-15 09:01:02  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 64646C26-7B45-460F-B695-3CDE67FE87E1 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 2025-08-12 21:43:43 | 2025-08-12 21:43:43 | False | False | NULL | 172.16.6.195 |  |
| 09055DAB-5C4A-4948-B919-E6DA945A48AC | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 2025-08-12 21:50:18 | 2025-08-12 21:50:18 | False | False | NULL | 172.16.6.195 |  |
| 1B0EB358-D864-4037-9F80-5E26146691F4 | F3334E28-CABA-4154-903B-3B1355F07CF8 | F3334E28-CABA-4154-903B-3B1355F07CF8 | 2025-11-11 21:16:51 | 2025-11-11 21:27:58 | True | False | NULL | 172.16.6.215 |  |
| 5AEDC9AB-8600-4822-AC18-152D81170B5F | F3334E28-CABA-4154-903B-3B1355F07CF8 | F3334E28-CABA-4154-903B-3B1355F07CF8 | 2025-11-11 21:28:58 | 2025-11-11 21:28:58 | False | False | NULL | 172.16.6.215 |  |
| 9077B48A-9396-4017-A5A9-B37EB8A04C0A | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:41:18 | 2025-11-15 08:41:18 | False | False | NULL | 172.16.7.110 |  |
| A03BC692-5972-47BA-9B44-1F749F9AF343 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:42:58 | 2025-11-15 08:42:58 | False | False | NULL |  |  |
| D78EBD23-9D8B-4778-B8CA-835C970512F6 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:01:02 | 2025-11-15 09:01:02 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_ELECTRICAL_A_SHIFTCHECKLIST_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_ELECTRICAL_B_SHIFTCHECKLIST

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2025-08-12 21:40:28 to 2025-11-15 09:01:13  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2FE863BE-A204-428D-9EC7-7C941E5418F9 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 2025-08-12 21:40:28 | 2025-08-12 21:40:28 | False | False | NULL | 172.16.6.195 |  |
| 74176FF2-1FB7-4636-9DE8-77E98ECC66C1 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:41:30 | 2025-11-15 08:41:30 | False | False | NULL | 172.16.7.110 |  |
| 92C606E2-6A3E-4548-9031-FBD35C51B47A | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:43:16 | 2025-11-15 08:43:16 | False | False | NULL |  |  |
| 89F6F5FC-CC55-493F-92DC-22D21FFCD644 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:01:13 | 2025-11-15 09:01:13 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_ELECTRICAL_B_SHIFTCHECKLIST_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_EVENTCHRONOLOGYCHECK

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_EVENTCHRONOLOGYCHECK_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_HEATSUMMARYREPORT

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_HEATSUMMARYREPORT_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_HISTORICALDATAACCURACY

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2025-11-15 08:13:07 to 2025-11-15 08:57:04  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| Q4 | varchar | YES | -1 | — |
| Q4Response | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E8F229C0-D7B9-4617-AB5E-EF3ABC6FDF99 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-15 08:13:07 | 2025-11-15 08:13:07 | False | False | NULL |  |  |
| 10843FB9-B26C-40E6-9C85-C581541ACCD9 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:36:00 | 2025-11-15 08:36:00 | False | False | NULL | 172.16.7.110 |  |
| 83058640-5968-4347-A2B6-4BC98DC4DFD0 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:38:23 | 2025-11-15 08:38:23 | False | False | NULL |  |  |
| 3A62245E-5928-43F9-AF67-CFE807703D6B | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:57:04 | 2025-11-15 08:57:04 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_HISTORICALDATAACCURACY_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| Q4 | varchar | YES | -1 | — |
| Q4Response | bit | YES | — | — |

---


## dbo.UAT_INTERSTAGEDELAY

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_INTERSTAGEDELAY_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_KPIDASHBOARDREFRESH

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_KPIDASHBOARDREFRESH_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_LADLECHANGE

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_LADLECHANGE_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_LOGSEETSREPORT

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_LOGSEETSREPORT_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_LOGSHEETSREPORT

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2025-08-13 17:16:52 to 2025-11-15 09:06:51  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| Q2 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q2Verdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| Q1 | varchar | YES | -1 | — |
| Q4 | varchar | YES | -1 | — |
| Q4Response | bit | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| Q3 | varchar | YES | -1 | — |
| OverallVerdict | bit | YES | — | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Q1Verdict | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFC09E24-B70D-417D-A3FF-3691C08A1BD5 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2025-08-13 17:16:52 | 2025-08-13 17:16:52 | False | False | NULL | 172.16.4.38 |  |
| D898488E-414F-469D-A9B1-F91D366D88C8 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:48:31 | 2025-11-15 08:48:31 | False | False | NULL | 172.16.7.110 |  |
| DF73E472-8FE6-4013-8DF4-9C23EB2569CE | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:51:07 | 2025-11-15 08:51:07 | False | False | NULL |  |  |
| C7105314-5AF9-435C-BF0A-BB70260D3B45 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:06:51 | 2025-11-15 09:06:51 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_LOGSHEETSREPORT_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| Q2 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q2Verdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| Q1 | varchar | YES | -1 | — |
| Q4 | varchar | YES | -1 | — |
| Q4Response | bit | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| Q3 | varchar | YES | -1 | — |
| OverallVerdict | bit | YES | — | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Q1Verdict | bit | YES | — | — |

---


## dbo.UAT_LRF_ALLOYADDITION

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2025-08-12 17:20:24 to 2025-11-15 08:54:56  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| Q4Response | bit | YES | — | — |
| Q4 | varchar | YES | -1 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B5094491-9B06-48D3-8CC7-AB2952F0EF5E | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2025-08-12 17:20:24 | 2025-08-12 17:20:24 | False | False | NULL | 172.16.4.38 |  |
| 032147C1-4B3B-4FA9-80D3-1CBBB80E6987 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2025-08-13 17:56:15 | 2025-08-13 17:56:15 | False | False | NULL | 172.16.4.38 |  |
| 06179854-CF7A-4D6B-A14D-D9FA192237C2 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:32:27 | 2025-11-15 08:32:27 | False | False | NULL | 172.16.7.110 |  |
| 6D35B7CF-4E42-4A17-BA67-091CEEC2456C | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:33:27 | 2025-11-15 08:33:27 | False | False | NULL |  |  |
| 614ED2BB-0A5F-4AC4-AD7A-CCB1AE5AB775 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:54:56 | 2025-11-15 08:54:56 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_LRF_ALLOYADDITION_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| Q4Response | bit | YES | — | — |
| Q4 | varchar | YES | -1 | — |

---


## dbo.UAT_LRF_ARCINGTIMEPERHEAT

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2025-08-12 17:26:28 to 2025-11-15 08:56:43  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 466498F6-D67A-4E37-AA2E-4F1886767D22 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2025-08-12 17:26:28 | 2025-08-12 17:26:28 | False | False | NULL | 172.16.4.38 |  |
| FC67CA77-27DA-4B29-80B7-37B4884A19CC | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-15 08:12:30 | 2025-11-15 08:12:30 | False | False | NULL |  |  |
| A570864A-7783-4F27-866E-30542549C71A | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:35:33 | 2025-11-15 08:35:33 | False | False | NULL | 172.16.7.110 |  |
| FD28ED9D-0FAF-490C-A168-269EA050C5A9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:37:09 | 2025-11-15 08:37:09 | False | False | NULL |  |  |
| AC156DBB-8336-4F11-B583-CB85153CDCDB | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:56:43 | 2025-11-15 08:56:43 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_LRF_ARCINGTIMEPERHEAT_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_LRF_ELECTRODECONSUMPTION

**Primary Key:** ID  
**Row Count:** 2  
**Date Range (ModifiedOn):** 2025-11-15 08:33:57 to 2025-11-15 08:55:04  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q2Verdict | bit | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| OverallVerdict | bit | YES | — | — |
| Q1Verdict | bit | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| TestName | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC4CE22A-E646-4AF8-B96D-81484356AB22 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:33:57 | 2025-11-15 08:33:57 | False | False | NULL |  |  |
| 41054D53-F9B1-4E55-BA5D-FD48300FA15B | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:55:04 | 2025-11-15 08:55:04 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_LRF_ELECTRODECONSUMPTION_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q2Verdict | bit | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| OverallVerdict | bit | YES | — | — |
| Q1Verdict | bit | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| TestName | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_LRF_LADLELIFETRACKING

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:32:54 to 2025-11-15 08:55:24  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 78F82938-9BED-4287-8AD8-B06C4CF166F0 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:32:54 | 2025-11-15 08:32:54 | False | False | NULL | 172.16.7.110 |  |
| 51A67F9F-F517-4750-9A5C-2421C1195BAA | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:34:17 | 2025-11-15 08:34:17 | False | False | NULL |  |  |
| 2C74A46A-95C7-44F9-BE15-A712F181CF3F | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:55:24 | 2025-11-15 08:55:24 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_LRF_LADLELIFETRACKING_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_LRF_LIVEDATADAHSBOARD

**Primary Key:** ID  
**Row Count:** 6  
**Date Range (ModifiedOn):** 2025-08-28 10:58:54 to 2025-11-15 09:07:18  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F324BD4E-EACD-45C6-B277-6C1330BD062B | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-08-28 10:58:54 | 2025-08-28 10:58:54 | False | False | NULL | 172.16.4.40 |  |
| 9946211A-1142-4135-BDF1-64C4FCD92322 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-15 08:14:33 | 2025-11-15 08:14:33 | False | False | NULL |  |  |
| EF8AE2D9-7455-41B1-B2DF-3F631A662052 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:37:31 | 2025-11-15 08:37:31 | False | False | NULL | 172.16.7.110 |  |
| A7943C15-26D5-43F4-B084-1137ACD90D36 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:39:43 | 2025-11-15 08:39:43 | False | False | NULL |  |  |
| FA33308F-ED6F-4358-B4F0-797D3864F319 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:57:53 | 2025-11-15 08:57:53 | False | False | NULL | 172.16.6.41 |  |
| 648537AF-E199-4CF6-B826-8DE19165BAAC | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:07:18 | 2025-11-15 09:07:18 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_LRF_LIVEDATADAHSBOARD_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_LRF_LOGBOOKDATADASHBOARD

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:40:40 to 2025-11-15 09:00:23  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1A2C11C8-28BA-490A-806E-B8BA11A2CABD | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:40:40 | 2025-11-15 08:40:40 | False | False | NULL | 172.16.7.110 |  |
| 6B8DB1A7-974E-4C4F-9230-3416EEC2C432 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:42:07 | 2025-11-15 08:42:07 | False | False | NULL |  |  |
| A859172E-517B-49B5-902D-F225AA91B33E | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:00:23 | 2025-11-15 09:00:23 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_LRF_LOGBOOKDATADASHBOARD_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_LRF_MANUALENTRYLOGBOOK

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:47:20 to 2025-11-15 09:06:14  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8B8D50DF-B58B-4C8F-82F7-AA148EDEDB94 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:47:20 | 2025-11-15 08:47:20 | False | False | NULL | 172.16.7.110 |  |
| B6BEBB63-11A8-4AFF-A223-1AF96E7C3CFA | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:50:18 | 2025-11-15 08:50:18 | False | False | NULL |  |  |
| A3CE95AD-E8F4-4EB1-9DC5-9B7B4438E68A | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:06:14 | 2025-11-15 09:06:14 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_LRF_MANUALENTRYLOGBOOK_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_LRF_QUALITYDATALOGSHEET

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:45:37 to 2025-11-15 09:04:20  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3F59A124-F567-4214-A9C9-8485942B9ACE | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:45:37 | 2025-11-15 08:45:37 | False | False | NULL | 172.16.7.110 |  |
| CC58409A-3967-46A2-868F-575CC38E666F | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:47:30 | 2025-11-15 08:47:30 | False | False | NULL |  |  |
| 77B8269C-619A-43D4-AB2C-3CA555F973C1 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:04:20 | 2025-11-15 09:04:20 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_LRF_QUALITYDATALOGSHEET_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_LRF_SHIFTWISEDATADASHBOARD

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:38:10 to 2025-11-15 08:58:19  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6A1E081A-5ECC-4E7B-868E-20B99FF7906F | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:38:10 | 2025-11-15 08:38:10 | False | False | NULL | 172.16.7.110 |  |
| 3B169B68-714E-43EE-81D1-1FF19F8B6273 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:40:18 | 2025-11-15 08:40:18 | False | False | NULL |  |  |
| 85BE1AB5-89F6-405E-929C-461AAF0B8BF5 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:58:19 | 2025-11-15 08:58:19 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_LRF_SHIFTWISEDATADASHBOARD_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_LRF_TEMPERATUREKPIS

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:32:36 to 2025-11-15 08:55:15  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 56965597-070F-40D0-85F4-F59F63F5AE04 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:32:36 | 2025-11-15 08:32:36 | False | False | NULL | 172.16.7.110 |  |
| 87C42B16-990C-45F3-997F-A6B127F3DDC5 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:34:07 | 2025-11-15 08:34:07 | False | False | NULL |  |  |
| EC0BCEB0-EE32-47BB-B658-72A03238139E | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:55:15 | 2025-11-15 08:55:15 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_LRF_TEMPERATUREKPIS_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_LRF_TRANSFORMERLOGSHEET

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:42:10 to 2025-11-15 09:01:50  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 76EB97E5-395D-442C-9EF3-368957B78C0B | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:42:10 | 2025-11-15 08:42:10 | False | False | NULL | 172.16.7.110 |  |
| 09860586-C7EA-48C0-B008-F482EE5581AB | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:44:12 | 2025-11-15 08:44:12 | False | False | NULL |  |  |
| 91525EA2-E8D3-49C0-99A6-6FFCF69358FD | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:01:50 | 2025-11-15 09:01:50 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_LRF_TRANSFORMERLOGSHEET_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_LRF_qUALITYDATADASHBOARD

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:39:17 to 2025-11-15 08:59:02  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1F291595-E031-4376-8ECB-D0AB40CCB01A | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:39:17 | 2025-11-15 08:39:17 | False | False | NULL | 172.16.7.110 |  |
| 42D1BD65-50CC-4EBF-9752-7A2BE0276835 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:41:10 | 2025-11-15 08:41:10 | False | False | NULL |  |  |
| 4D4303C1-8CD5-4585-9D99-5185C14AD880 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:59:02 | 2025-11-15 08:59:02 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_LRF_qUALITYDATADASHBOARD_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_MANUALOVERRIDEOFEVENT

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_MANUALOVERRIDEOFEVENT_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_MANUALPOCREATION

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_MANUALPOCREATION_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_MISSINGSIGNALHANDLING

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_MISSINGSIGNALHANDLING_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_POAUTOCREATION

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_POAUTOCREATION_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_POFIELDVALIDATION

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_POFIELDVALIDATION_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_POWERCONSUMPTIONCHARTMETERWISE

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:46:25 to 2025-11-15 09:05:14  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1D9FBEEF-DB26-4ECA-A25F-7DE0856C327B | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:46:25 | 2025-11-15 08:46:25 | False | False | NULL | 172.16.7.110 |  |
| 55DBF6A9-91E9-4276-B2F4-B830530B4A82 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:48:29 | 2025-11-15 08:48:29 | False | False | NULL |  |  |
| 4A345946-EA9A-4F66-AC06-48AE4F506B6C | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:05:14 | 2025-11-15 09:05:14 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_POWERCONSUMPTIONCHARTMETERWISE_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_POWERCONSUMPTIONLOGSHEET

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:46:13 to 2025-11-15 09:04:59  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 171A877C-16EE-4FEF-A0CA-355D1F1D9AD9 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:46:13 | 2025-11-15 08:46:13 | False | False | NULL | 172.16.7.110 |  |
| 7607B24E-EFB1-48B4-A2DF-0C5D802E655C | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:48:14 | 2025-11-15 08:48:14 | False | False | NULL |  |  |
| B3F5C128-DF29-4E29-B30B-4C99EFBFF825 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:04:59 | 2025-11-15 09:04:59 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_POWERCONSUMPTIONLOGSHEET_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_POWERCONSUMPTIONREPORTLOGSHEET

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:46:35 to 2025-11-15 09:05:27  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 25298414-2D14-4F23-80B4-FA48FB851D05 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:46:35 | 2025-11-15 08:46:35 | False | False | NULL | 172.16.7.110 |  |
| D301F4E0-D169-4BBE-908D-B89571955C8F | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:48:54 | 2025-11-15 08:48:54 | False | False | NULL |  |  |
| 1DC1A3D3-5E64-43B4-8705-0801F7D1C2B5 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:05:27 | 2025-11-15 09:05:27 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_POWERCONSUMPTIONREPORTLOGSHEET_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_RAWMATERIAL

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| EndDateTime | datetime | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| IsProcessed | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EntryDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| Q1Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2Verdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| ReportDate | date | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_RAWMATERIAL_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| EndDateTime | datetime | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| IsProcessed | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EntryDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| Q1Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2Verdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| ReportDate | date | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_REALTIMEDASHBOARD

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2025-08-28 17:08:47 to 2025-11-15 08:56:58  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 56DF47A3-FA01-4B8C-A496-073E96210930 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-08-28 17:08:47 | 2025-08-28 17:08:47 | False | False | NULL | 172.16.6.195 |  |
| 151AE7DA-95A2-4819-B15D-BCB651448CA7 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-15 08:12:55 | 2025-11-15 08:12:55 | False | False | NULL |  |  |
| BAC9BDB1-63BD-41A2-A9A4-A7B6E16DF1FB | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:35:50 | 2025-11-15 08:35:50 | False | False | NULL | 172.16.7.110 |  |
| 71A8263A-42C0-4008-941B-B0FB97788015 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:38:12 | 2025-11-15 08:38:12 | False | False | NULL |  |  |
| F8D0373B-3D0C-4550-945C-4078BC614198 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:56:58 | 2025-11-15 08:56:58 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_REALTIMEDASHBOARD_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_ROLEBASEDFIELDEDIT

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_ROLEBASEDFIELDEDIT_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_SCRAPCHARGING

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_SCRAPCHARGING_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_SHIFTDELAYREPORT

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_SHIFTDELAYREPORT_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |

---


## dbo.UAT_SMS_LIVEDATADASHBOARD

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2025-08-28 11:06:49 to 2025-11-15 08:57:32  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0E2458D2-5E04-42BD-8CA9-DE2056BCCA41 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-08-28 11:06:49 | 2025-08-28 11:06:49 | False | False | NULL | 172.16.4.40 |  |
| 01A1CBC3-A4C1-44D2-AB06-CC6D193233D0 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2025-09-29 12:38:31 | 2025-09-29 12:38:31 | False | False | NULL |  |  |
| 8C1159AA-BDA0-413A-A75C-4E7F998E3CBA | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:37:06 | 2025-11-15 08:37:06 | False | False | NULL | 172.16.7.110 |  |
| 28BE89E0-3DDE-427D-8C24-5D23578591DA | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:39:07 | 2025-11-15 08:39:07 | False | False | NULL |  |  |
| CFE43BC7-3713-4507-AE38-26436889CD66 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:57:32 | 2025-11-15 08:57:32 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_SMS_LIVEDATADASHBOARD_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_SMS_PLANTDASHBOARD

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2025-08-12 17:31:02 to 2025-11-15 08:57:24  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9F4A0E4F-9937-4BE2-BA3D-2186BBF828E4 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 2025-08-12 17:31:02 | 2025-08-12 17:31:02 | False | False | NULL | 172.16.6.149 |  |
| 6AF1F7E4-D887-4761-B55E-DDB65DA4839B | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-15 08:13:55 | 2025-11-15 08:13:55 | False | False | NULL |  |  |
| 35574DB9-9B7C-4EB9-93FE-FD0A2792D216 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:36:51 | 2025-11-15 08:36:51 | False | False | NULL | 172.16.7.110 |  |
| B1DEA6B2-2554-4699-AFF8-B332C82EF366 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:38:51 | 2025-11-15 08:38:51 | False | False | NULL |  |  |
| 1D528183-40EE-423F-8948-089158D999CF | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 08:57:24 | 2025-11-15 08:57:24 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_SMS_PLANTDASHBOARD_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_SMS_PLANTPROCESSTIME

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:41:04 to 2025-11-15 09:00:49  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6FABE501-FCA1-4588-934F-2947C15C4B78 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:41:04 | 2025-11-15 08:41:04 | False | False | NULL | 172.16.7.110 |  |
| 4F3BEF4B-72DB-498F-8B1E-ED14B41EF756 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:42:42 | 2025-11-15 08:42:42 | False | False | NULL |  |  |
| 411A5B81-77B7-402B-A7A5-1AEE78120474 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:00:49 | 2025-11-15 09:00:49 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_SMS_PLANTPROCESSTIME_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_TRANSFORMER125MVA

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2025-11-11 21:20:38 to 2025-11-15 09:02:16  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A066A458-5604-4539-AFB7-25F8B7F6430B | F3334E28-CABA-4154-903B-3B1355F07CF8 | F3334E28-CABA-4154-903B-3B1355F07CF8 | 2025-11-11 20:57:56 | 2025-11-11 21:20:38 | True | False | NULL | 172.16.6.215 |  |
| 34BB9800-355C-4E32-AB8F-D4B5DD57FE7F | F3334E28-CABA-4154-903B-3B1355F07CF8 | F3334E28-CABA-4154-903B-3B1355F07CF8 | 2025-11-11 21:23:25 | 2025-11-11 21:23:25 | False | False | NULL | 172.16.6.215 |  |
| 198F20C6-728C-4D60-A62C-A89AB30C0AD7 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:44:50 | 2025-11-15 08:44:50 | False | False | NULL |  |  |
| B6917337-63A1-4A5B-9BF5-9C1FEB01BDE4 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:02:16 | 2025-11-15 09:02:16 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_TRANSFORMER125MVA_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_TRANSFORMER15MVALOGSHEET

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:43:46 to 2025-11-15 09:02:42  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Fileupload | varchar | YES | 8000 | — |
| EntryDateTime | datetime | YES | — | — |
| Q1Verdict | bit | YES | — | — |
| Q2Verdict | bit | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| Q2 | varchar | YES | -1 | — |
| Q3 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| TestName | varchar | YES | -1 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C8D14625-96B1-4C41-A4EE-CBA9BFCBBB08 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:43:46 | 2025-11-15 08:43:46 | False | False | NULL | 172.16.7.110 |  |
| 15D2AC55-0E64-473B-A268-D368DE9F8902 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:45:24 | 2025-11-15 08:45:24 | False | False | NULL |  |  |
| 1659E7E6-5844-4272-BBF6-8C2B188D2C7C | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:02:42 | 2025-11-15 09:02:42 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_TRANSFORMER15MVALOGSHEET_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Fileupload | varchar | YES | 8000 | — |
| EntryDateTime | datetime | YES | — | — |
| Q1Verdict | bit | YES | — | — |
| Q2Verdict | bit | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| Q2 | varchar | YES | -1 | — |
| Q3 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| TestName | varchar | YES | -1 | — |

---


## dbo.UAT_TRANSFORMER24MVA

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:43:34 to 2025-11-15 09:02:28  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 991D2B4D-EBED-4625-B5A1-9402E427308E | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:43:34 | 2025-11-15 08:43:34 | False | False | NULL | 172.16.7.110 |  |
| D407F17A-7AAE-4FC4-B23E-5C521F7E9B58 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:45:08 | 2025-11-15 08:45:08 | False | False | NULL |  |  |
| 3E9D225B-E93E-40E0-96D2-593D8F8D8A01 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:02:28 | 2025-11-15 09:02:28 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_TRANSFORMER24MVA_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_TRANSFORMER63MVA

**Primary Key:** ID  
**Row Count:** 6  
**Date Range (ModifiedOn):** 2025-11-11 21:25:57 to 2025-11-15 09:02:03  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ECEA495E-8F49-4EB9-A778-9C5BAF7D5871 | 83E3F386-31EE-476F-9651-39B924B01514 | F3334E28-CABA-4154-903B-3B1355F07CF8 | 2025-11-11 20:50:26 | 2025-11-11 21:25:57 | True | False | NULL | 172.16.6.215 |  |
| F76AFE36-D246-4CF4-B58E-5B174C6CEA8A | F3334E28-CABA-4154-903B-3B1355F07CF8 | F3334E28-CABA-4154-903B-3B1355F07CF8 | 2025-11-11 21:27:26 | 2025-11-11 21:27:26 | False | False | NULL | 172.16.6.215 |  |
| 677D092A-102C-49CB-80A4-587C1609EE18 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:42:22 | 2025-11-15 08:42:22 | False | False | NULL | 172.16.7.110 |  |
| 35B584CE-5BFB-47C3-91C7-C0642CFB3E8E | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:42:36 | 2025-11-15 08:42:36 | False | False | NULL | 172.16.7.110 |  |
| 97B2F6B3-2BB3-458A-B7A5-115BAC4D8303 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:44:33 | 2025-11-15 08:44:33 | False | False | NULL |  |  |
| AE3873ED-7D0B-46A2-BE8D-1961385E489B | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:02:03 | 2025-11-15 09:02:03 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_TRANSFORMER63MVA_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Q1Verdict | bit | YES | — | — |
| Q3Verdict | bit | YES | — | — |
| Q3 | varchar | YES | -1 | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| Fileupload | varchar | YES | 8000 | — |
| TestName | varchar | YES | -1 | — |
| Q2Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| Q2 | varchar | YES | -1 | — |
| TesterName | varchar | YES | 36 | — |
| Comments | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |

---


## dbo.UAT_TRANSFORMER6_6KVLOGSHEET

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-15 08:43:57 to 2025-11-15 09:02:53  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Fileupload | varchar | YES | 8000 | — |
| EntryDateTime | datetime | YES | — | — |
| Q1Verdict | bit | YES | — | — |
| Q2Verdict | bit | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| Q2 | varchar | YES | -1 | — |
| Q3 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| TestName | varchar | YES | -1 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EA760EC8-CD04-476C-B1AD-C7A56A902F48 | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-15 08:43:57 | 2025-11-15 08:43:57 | False | False | NULL | 172.16.7.110 |  |
| 282F8B61-0149-4BCF-8C25-9FE92B9BEB5C | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-15 08:45:41 | 2025-11-15 08:45:41 | False | False | NULL |  |  |
| E3B3F5A8-7048-43D9-85F4-B2881CE1BACC | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-15 09:02:53 | 2025-11-15 09:02:53 | False | False | NULL | 172.16.6.41 |  |

---


## dbo.UAT_TRANSFORMER6_6KVLOGSHEET_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Fileupload | varchar | YES | 8000 | — |
| EntryDateTime | datetime | YES | — | — |
| Q1Verdict | bit | YES | — | — |
| Q2Verdict | bit | YES | — | — |
| EndDateTime | datetime | YES | — | — |
| Q1 | varchar | YES | -1 | — |
| Comments | varchar | YES | -1 | — |
| Q2 | varchar | YES | -1 | — |
| Q3 | varchar | YES | -1 | — |
| Q3Verdict | bit | YES | — | — |
| OverallVerdict | bit | YES | — | — |
| TesterName | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| TestName | varchar | YES | -1 | — |

---


## dbo.UAT_Test_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 87  
**Date Range (ModifiedOn):** 2025-08-08 13:29:24 to 2025-09-29 11:59:50  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Description | varchar | YES | -1 | — |
| ExpectedOutcomeType | varchar | YES | 100 | — |
| AreaName | varchar | YES | -1 | — |
| Srno | int | YES | 10,0 | — |
| EditPageID | varchar | YES | 36 | — |
| LvPageID | varchar | YES | 36 | — |
| Helpdoc | varchar | YES | 8000 | — |
| Icon | varchar | YES | 200 | — |
| EnableUAT | bit | YES | — | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D9387246-73A3-433A-8BBB-008F6C43CB38 | No. of Heats per Shift | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-04 17:17:12 | 2025-08-08 13:29:24 | False | False | NULL |
| AD98ECC9-6DD9-403F-A70F-E41560CA394C | Power per Ton of Steel | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-04 17:17:55 | 2025-08-08 13:29:28 | False | False | NULL |
| 7176C52A-4E48-4D82-947D-0916166EC37E | Electrode Consumption per Heat | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-05 12:11:05 | 2025-08-08 13:29:33 | False | False | NULL |
| 2F4B2C4E-6D38-4A02-B7EA-9508AE8DC5B7 | Yield per Heat | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-05 12:11:05 | 2025-08-08 13:29:37 | False | False | NULL |
| 4C188371-6126-45CF-80E0-7F926C8A2ADB | Alloy Addition per Ton | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-05 12:11:05 | 2025-08-08 13:29:42 | False | False | NULL |
| DDDD8A5B-4D01-47CE-9D7A-63628D8BCBE1 | Electrode Consumption per Ton | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-05 12:11:05 | 2025-08-08 13:29:47 | False | False | NULL |
| 58BCD082-7CD5-457F-BF3C-3718395D6AEF | Temperature KPIs | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-05 12:11:05 | 2025-08-08 13:29:51 | False | False | NULL |
| 9FAD3C9D-7E1A-47A6-A857-523C4E55E354 | Ladle Life Tracking | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-05 12:11:05 | 2025-08-08 13:29:55 | False | False | NULL |
| 148D0F70-C3C4-496D-9F0E-BA3FF2B00F4F | Casting Speed per Strand | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-05 12:11:05 | 2025-08-08 13:30:01 | False | False | NULL |
| 785FD875-6EAC-4D04-B3D7-DA5FF4748E63 | No. of Billets per Heat | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-05 12:11:05 | 2025-08-08 13:30:05 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CD6F2F6E-515D-4E05-8287-CB777D44A82F | NULL | NULL | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2025-09-29 11:59:50 | 2025-09-29 11:59:50 | False | False | NULL |
| 5A536098-4C56-41BB-9AF7-B0275DEB9CED | NULL | NULL | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2025-09-28 14:13:32 | 2025-09-28 14:13:32 | False | False | NULL |
| 3F081305-638A-437A-B39A-160CAB031FD3 | CCM Manual Entry Logbook | NULL | 6E7ADBA5-FE49-4BC2-9433-9FFDFE425E1A | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-08-08 16:04:17 | 2025-08-11 13:50:56 | False | False | NULL |
| 30B9D71A-D5B8-44BF-9D92-FD4AB2AEA72B | LRF Manual Entry Logbook | NULL | 6E7ADBA5-FE49-4BC2-9433-9FFDFE425E1A | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-08-08 16:04:01 | 2025-08-11 13:50:46 | False | False | NULL |
| DADF469C-9095-4F12-85D1-0AC03862C180 | EAF Manual Entry Logbook | NULL | 6E7ADBA5-FE49-4BC2-9433-9FFDFE425E1A | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-08-08 16:02:49 | 2025-08-11 13:50:34 | False | False | NULL |
| 64726AB8-AE66-40FF-B320-86EFE553076E | Manual PO Creation | NULL | NULL | 6E7ADBA5-FE49-4BC2-9433-9FFDFE425E1A | 2025-08-06 11:26:54 | 2025-08-11 13:01:22 | False | False | NULL |
| 69436140-F8E3-41B9-A64D-72621D099E1B | Heat Summary Report | NULL | NULL | 6E7ADBA5-FE49-4BC2-9433-9FFDFE425E1A | 2025-08-06 11:26:54 | 2025-08-11 13:01:17 | False | False | NULL |
| 8177B149-FF4B-463B-B644-0A64C110BCE1 | Inter-Stage Delay | NULL | NULL | 6E7ADBA5-FE49-4BC2-9433-9FFDFE425E1A | 2025-08-06 11:26:54 | 2025-08-11 13:01:11 | False | False | NULL |
| 826BB20E-D0D9-46A1-BA46-5F0FA60FA6E3 | Scrap Charging Record | NULL | NULL | 6E7ADBA5-FE49-4BC2-9433-9FFDFE425E1A | 2025-08-06 11:26:54 | 2025-08-11 13:01:06 | False | False | NULL |
| 919D8560-D6F3-492D-868D-941D4FD5F076 | Role-Based Field Edit | NULL | NULL | 6E7ADBA5-FE49-4BC2-9433-9FFDFE425E1A | 2025-08-06 11:26:54 | 2025-08-11 13:01:00 | False | False | NULL |

---


## dbo.UAT_Test_Report_Data

**Primary Key:** ID  
**Row Count:** 683  
**Date Range (ModifiedOn):** 2025-08-11 15:20:17 to 2025-11-15 09:07:18  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| TestName | varchar | YES | 100 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| TestingStartDatetime | datetime | YES | — | — |
| IsProcessed | bit | YES | — | — |
| TestingEndDatetime | datetime | YES | — | — |
| TesterName | varchar | YES | 100 | — |
| Q1Verdict | varchar | YES | 100 | — |
| Q2Verdict | varchar | YES | 100 | — |
| Q3Verdict | varchar | YES | 100 | — |
| OverallVerdict | varchar | YES | 100 | — |
| Remarks | varchar | YES | -1 | — |
| EntityName | varchar | YES | 100 | — |
| Q4Verdict | varchar | YES | 100 | — |
| AreaName | varchar | YES | 100 | — |

### Top 10 Records

| ID | TestName | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3652B7DC-E26C-4BE6-8258-52711B250A85 | No. of Heats per Shift | NULL | NULL | 2025-08-11 15:20:17 | 2025-08-11 15:20:17 | False | False | NULL | NULL |
| 4DA0431A-2D71-478A-8D73-F86363A8DA53 | No. of Heats per Shift | NULL | NULL | 2025-08-11 15:20:17 | 2025-08-11 15:20:17 | False | False | NULL | NULL |
| 6D6EB01B-0FFE-415F-A677-87521347F1EC | No. of Heats per Shift | NULL | NULL | 2025-08-11 15:20:17 | 2025-08-11 15:20:17 | False | False | NULL | NULL |
| 855BEEB0-F635-4B85-90CE-0532CFFD9A40 | No. of Heats per Shift | NULL | NULL | 2025-08-11 15:20:17 | 2025-08-11 15:20:17 | False | False | NULL | NULL |
| AC9B77C6-AB18-45FC-9253-82B277205D94 | No. of Heats per Shift | NULL | NULL | 2025-08-11 15:20:17 | 2025-08-11 15:20:17 | False | False | NULL | NULL |
| DB645345-A713-4A07-A1B0-9D116194226B | No. of Heats per Shift | NULL | NULL | 2025-08-11 15:20:17 | 2025-08-11 15:20:17 | False | False | NULL | NULL |
| E0CDCCAC-D5AE-442C-AEA6-A9B43D9603EB | No. of Heats per Shift | NULL | NULL | 2025-08-11 15:20:17 | 2025-08-11 15:20:17 | False | False | NULL | NULL |
| 23EFC462-4C30-44E5-BDA7-3FD5C564200C | Alloy Addition per Ton | NULL | NULL | 2025-08-12 17:20:24 | 2025-08-12 17:20:24 | False | False | NULL | NULL |
| 4E1B2FBF-9149-48EF-AB1D-1951614C6670 | Alloy Addition per Ton | NULL | NULL | 2025-08-12 17:20:24 | 2025-08-12 17:20:24 | False | False | NULL | NULL |
| 770C7C9F-D4AE-42F5-B630-0DB36C346919 | Alloy Addition per Ton | NULL | NULL | 2025-08-12 17:20:24 | 2025-08-12 17:20:24 | False | False | NULL | NULL |

### Bottom 10 Records

| ID | TestName | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B67A8CB2-5978-4E19-BA52-526DB1B109DB | LRF Live Data Dashboard | NULL | NULL | 2025-11-15 09:07:18 | 2025-11-15 09:07:18 | False | False | NULL | NULL |
| 278EA3A9-8618-4386-A6D5-47ADD5CB15FE | EAF Live Data Dashboard | NULL | NULL | 2025-11-15 09:07:03 | 2025-11-15 09:07:03 | False | False | NULL | NULL |
| A35CFE71-888D-4CDC-9FC9-83BDD8459032 | Logsheets Report | NULL | NULL | 2025-11-15 09:06:51 | 2025-11-15 09:06:51 | False | False | NULL | NULL |
| 78964492-D17D-40C9-AA44-A914CC918B2B | Electrical Checklist Report | NULL | NULL | 2025-11-15 09:06:39 | 2025-11-15 09:06:39 | False | False | NULL | NULL |
| 8DF59CC1-A2F8-44A8-AB9D-B1B7E8331FFD | CCM Manual Entry Logbook | NULL | NULL | 2025-11-15 09:06:26 | 2025-11-15 09:06:26 | False | False | NULL | NULL |
| 0E0D4F5C-A439-4595-B142-F0EE8A8EF287 | LRF Manual Entry Logbook | NULL | NULL | 2025-11-15 09:06:14 | 2025-11-15 09:06:14 | False | False | NULL | NULL |
| 775445F3-03FC-4F36-9963-463CF2F146EC | Delay Type Master Logbook | NULL | NULL | 2025-11-15 09:06:03 | 2025-11-15 09:06:03 | False | False | NULL | NULL |
| 6E06E67E-D3B8-4016-ABD6-40832CEEDB76 | Shift Delay Entry Logbook | NULL | NULL | 2025-11-15 09:05:49 | 2025-11-15 09:05:49 | False | False | NULL | NULL |
| F8036A49-9EDF-40E8-981F-BFFED63A0398 | EAF Manual Entry Logbook | NULL | NULL | 2025-11-15 09:05:39 | 2025-11-15 09:05:39 | False | False | NULL | NULL |
| 48FE43F2-CB82-4B4D-B050-85E6BCCB2F42 | Power Consumption Report Logsheet | NULL | NULL | 2025-11-15 09:05:27 | 2025-11-15 09:05:27 | False | False | NULL | NULL |

---


## dbo.UAT_Tracking_Transaction

**Primary Key:** ID  
**Row Count:** 257  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| TotalUATsTested | int | YES | 10,0 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| TotalUserConductedTest | int | YES | 10,0 | — |
| TotalUATPassRate | decimal | YES | 18,2 | — |
| TotalUATFailRate | decimal | YES | 18,2 | — |
| LastTestConducted | datetime | YES | — | — |
| UATDuration | int | YES | 10,0 | — |

### Top 10 Records

| ID | TotalUATsTested | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0FF6A599-3070-4A59-9A14-AE5918FE6E0F | 30 | NULL | NULL | NULL | 2025-11-15 08:31:40 | NULL | False | False | NULL |
| 0E387AD0-5669-4E49-94D6-46D9951589B5 | 61 | NULL | NULL | NULL | 2025-11-15 08:47:20 | NULL | False | False | NULL |
| 0AF9C312-2794-4BC5-B113-EA9F24EF9CC5 | 62 | NULL | NULL | NULL | 2025-11-15 08:56:33 | NULL | False | False | NULL |
| 08D93296-5C1D-4C48-A2CF-F714760DC510 | 62 | NULL | NULL | NULL | 2025-11-15 08:56:18 | NULL | False | False | NULL |
| 0858F621-6C1D-454B-B0F9-148E2659B6A7 | 62 | NULL | NULL | NULL | 2025-11-15 08:54:22 | NULL | False | False | NULL |
| 07FF5C48-6925-4EC6-A97A-59995B80E8FD | 30 | NULL | NULL | NULL | 2025-11-15 08:13:21 | NULL | False | False | NULL |
| 05FA7D13-C171-4E22-BBF2-EE2DA9B456CD | 62 | NULL | NULL | NULL | 2025-11-15 09:05:27 | NULL | False | False | NULL |
| 02FA2D62-F3A0-4B9E-85B5-0BA3B3FA8F40 | 62 | NULL | NULL | NULL | 2025-11-15 08:49:13 | NULL | False | False | NULL |
| 0253442F-272B-4237-BBE3-8D8D17DB26A4 | 62 | NULL | NULL | NULL | 2025-11-15 09:06:26 | NULL | False | False | NULL |
| 022A0601-3E5D-451C-96F3-5C6FC897C7B8 | 43 | NULL | NULL | NULL | 2025-11-15 08:40:40 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | TotalUATsTested | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0FF6A599-3070-4A59-9A14-AE5918FE6E0F | 30 | NULL | NULL | NULL | 2025-11-15 08:31:40 | NULL | False | False | NULL |
| 0E387AD0-5669-4E49-94D6-46D9951589B5 | 61 | NULL | NULL | NULL | 2025-11-15 08:47:20 | NULL | False | False | NULL |
| 0AF9C312-2794-4BC5-B113-EA9F24EF9CC5 | 62 | NULL | NULL | NULL | 2025-11-15 08:56:33 | NULL | False | False | NULL |
| 08D93296-5C1D-4C48-A2CF-F714760DC510 | 62 | NULL | NULL | NULL | 2025-11-15 08:56:18 | NULL | False | False | NULL |
| 0858F621-6C1D-454B-B0F9-148E2659B6A7 | 62 | NULL | NULL | NULL | 2025-11-15 08:54:22 | NULL | False | False | NULL |
| 07FF5C48-6925-4EC6-A97A-59995B80E8FD | 30 | NULL | NULL | NULL | 2025-11-15 08:13:21 | NULL | False | False | NULL |
| 05FA7D13-C171-4E22-BBF2-EE2DA9B456CD | 62 | NULL | NULL | NULL | 2025-11-15 09:05:27 | NULL | False | False | NULL |
| 02FA2D62-F3A0-4B9E-85B5-0BA3B3FA8F40 | 62 | NULL | NULL | NULL | 2025-11-15 08:49:13 | NULL | False | False | NULL |
| 0253442F-272B-4237-BBE3-8D8D17DB26A4 | 62 | NULL | NULL | NULL | 2025-11-15 09:06:26 | NULL | False | False | NULL |
| 022A0601-3E5D-451C-96F3-5C6FC897C7B8 | 43 | NULL | NULL | NULL | 2025-11-15 08:40:40 | NULL | False | False | NULL |

---


## dbo.UserDetails

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | -1 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |

---


## dbo.VM_Monitoring

**Primary Key:** ID  
**Row Count:** 67  
**Date Range (ModifiedOn):** 2023-04-06 18:05:29 to 2023-07-04 10:48:18  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| TaskManagerCPU | varchar | YES | -1 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| TaskManagerRAM | varchar | YES | -1 | — |
| TaskManagerNetwork | varchar | YES | -1 | — |
| Entrydatetime | datetime | YES | — | — |
| TaskManagerCPURemarks | varchar | YES | 8000 | — |
| TaskManagerRAMRemarks | varchar | YES | 8000 | — |
| TaskManagerNetworkRemarks | varchar | YES | 8000 | — |

### Top 10 Records

| ID | TaskManagerCPU | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 316D719F-4FBA-420A-9270-2B1AD830EE26 | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA6wAAAIRCAYAAABOGDBbAAAAAXNSR0IArs4c6Q... | NULL | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | EFB2065E-24C3-42E4-847E-86AEDA8C5A89 | 2023-04-06 18:05:29 | 2023-04-06 18:05:29 | False | False | NULL |
| 537DF8E8-65B0-43DE-97B6-8ACD934DC83B | <p>dd</p> | NULL | 9EFA3064-E41F-4661-9244-8631B72F601D | 9EFA3064-E41F-4661-9244-8631B72F601D | 2023-04-07 10:53:02 | 2023-04-07 10:53:02 | False | False | NULL |
| 6C3D5412-EAAC-4AC9-BA09-2F4F9F9541BC | <p><img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAeAB4AAD/4RDyRXhpZgAATU0AKgAAAAgABAE7AAIAA... | 50F41A4B-D2E0-4871-9059-A62663EF8E06 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-07 19:37:07 | 2023-04-07 19:37:07 | False | False | NULL |
| B75A3022-78C5-4222-9159-880784293BFA | <p><img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAeAB4AAD/4RDyRXhpZgAATU0AKgAAAAgABAE7AAIAA... | 0C2EC874-7748-40A5-84EF-380CE3964D2C | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-08 10:34:22 | 2023-04-08 10:34:22 | False | False | NULL |
| BADA7DAD-2AAB-4038-A951-6093CF82A097 | <p><img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAeAB4AAD/4RDyRXhpZgAATU0AKgAAAAgABAE7AAIAA... | E8455E67-11BF-4B76-B52A-1D7FF8C7956E | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-10 13:01:16 | 2023-04-10 13:01:16 | False | False | NULL |
| F8071F3A-8058-4D2A-AB6A-386D9DC7D9BE | <p><img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/4RDyRXhpZgAATU0AKgAAAAgABAE7AAIAA... | 3FA889F2-9476-49F8-A8CC-9CFD16FDE396 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-11 12:11:17 | 2023-04-11 12:11:17 | False | False | NULL |
| 61C6D6E6-3F60-4BDE-A1BC-875B823F85E5 | <p><br><img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/4RDyRXhpZgAATU0AKgAAAAgABAE7A... | 590F69D8-9EF9-4E24-8C6D-DBB9F5A3582F | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-12 17:16:28 | 2023-04-12 17:16:27 | False | False | NULL |
| 3D5CF8AB-F6B3-4EE2-BC6F-6F9D6AA733CB | <p><img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/4RDyRXhpZgAATU0AKgAAAAgABAE7AAIAA... | 96FCFD29-D268-48FC-A21B-59EFF906C653 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-13 12:28:23 | 2023-04-13 12:28:23 | False | False | NULL |
| 320B43E2-9CCE-4846-A9F2-4AC8B892E51F | <p><img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/4RDyRXhpZgAATU0AKgAAAAgABAE7AAIAA... | C34AFF69-2B0B-4D06-AE9C-C2F4E7BF6D0C | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-14 10:12:55 | 2023-04-14 10:12:55 | False | False | NULL |
| 4AE9E4CF-2250-4084-868D-1219FBA61FCA | <p><img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/4RDyRXhpZgAATU0AKgAAAAgABAE7AAIAA... | 15AA35F0-3A90-4C73-82CA-D12D5C7FD9BD | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-04-15 09:35:13 | 2023-04-15 09:35:13 | False | False | NULL |

### Bottom 10 Records

| ID | TaskManagerCPU | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 477DEAF2-2280-40E8-9467-C3B1BD9AF651 | NULL | E630D763-579B-4476-8207-FB858ADFAC85 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-07-04 10:48:18 | 2023-07-04 10:48:18 | False | False | NULL |
| 8C0A3826-474A-467F-8065-45B39AE1E9FB | NULL | B5021435-5B6A-44D8-AF2E-499F12DF5B4D | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-07-03 17:06:09 | 2023-07-03 17:06:09 | False | False | NULL |
| 9656F84A-91F0-43AE-8E87-0FC123B8FE22 | NULL | CE5EF93E-761D-4E48-8A3C-28D2F1C06A19 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-30 16:54:42 | 2023-06-30 16:54:42 | False | False | NULL |
| 83E4443D-66D8-42CB-AF78-F3218C570D53 | NULL | 30451152-A13B-4FCF-908F-6D8590EC9145 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-06-28 16:55:25 | 2023-06-28 16:55:25 | False | False | NULL |
| F37B948C-1043-42D1-88B6-2907487E046B | NULL | 46DEF245-B8E8-464D-892F-D41B007B4EC0 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-26 10:47:40 | 2023-06-26 10:47:40 | False | False | NULL |
| C48C2AFB-6186-441B-B4E8-08C0F8036015 | NULL | 52347E61-7A6D-4D84-B379-904665BE01AE | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-23 17:16:31 | 2023-06-23 17:16:31 | False | False | NULL |
| 6F8C0022-682A-4FD7-B5F4-B2AD8361767E | NULL | 847F91E6-B5DB-4582-B6A7-356BD176842E | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-22 15:14:04 | 2023-06-22 15:14:04 | False | False | NULL |
| E8E69EE6-02C5-4DF5-8028-297CBFF2A149 | NULL | 1DB085FA-6C3A-4A50-A82E-64B0497CFC43 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-21 15:30:09 | 2023-06-21 15:30:09 | False | False | NULL |
| 7D8BD9D4-35F8-47CC-9A22-84E2CC59DF45 | NULL | 80C40A12-92A1-47F5-9F1B-EBF1B4CED735 | 88C277EC-D407-477C-AD45-83A63BDF24EE | 88C277EC-D407-477C-AD45-83A63BDF24EE | 2023-06-20 16:29:02 | 2023-06-20 16:29:02 | False | False | NULL |
| A666BF1C-9005-410F-BAD3-17AE8C82F7E3 | NULL | CEDBCADC-D841-49BE-8C12-CB35FC0E7A38 | 80534764-F53E-4106-81A8-D86849F6E75C | 80534764-F53E-4106-81A8-D86849F6E75C | 2023-06-19 15:37:41 | 2023-06-19 15:37:41 | False | False | NULL |

---


## dbo.VM_Monitoring_Audit

**Primary Key:** —  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2023-04-21 16:40:46 to 2023-05-13 09:55:10  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| TaskManagerCPU | varchar | YES | -1 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| TaskManagerRAM | varchar | YES | -1 | — |
| TaskManagerNetwork | varchar | YES | -1 | — |
| Entrydatetime | datetime | YES | — | — |
| TaskManagerCPURemarks | varchar | YES | 8000 | — |
| TaskManagerRAMRemarks | varchar | YES | 8000 | — |
| TaskManagerNetworkRemarks | varchar | YES | 8000 | — |

### Top 10 Records

| ID | TaskManagerCPU | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C225C464-E7C8-44F5-BBBD-CDADD10B2824 | NULL | A179ADC4-C03F-4CD4-931A-59330BEC18D0 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-04-21 16:40:46 | 2023-04-21 16:40:46 | False | False | NULL |
| C225C464-E7C8-44F5-BBBD-CDADD10B2824 | NULL | A179ADC4-C03F-4CD4-931A-59330BEC18D0 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-04-21 16:40:46 | 2023-04-21 16:43:20 | False | False | NULL |
| 7C7CC129-0999-43C7-AAFD-68FACE0F0EAB | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAisAAAHRCAYAAACrT/nKAAAgAElEQVR4nOzdf1... | C38C2F4B-8FA7-494D-86A5-54CB637E78A5 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-02 09:34:55 | 2023-05-02 09:34:55 | False | False | NULL |
| E52686B2-AAB4-404A-9C74-DDE511817EB4 | <p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAiIAAAHYCAYAAABwVYPIAAAgAElEQVR4nOzdfV... | 8F74CD16-B3C9-4C23-900A-887A9D7D38C2 | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 52E8D208-E1E8-491F-8EAC-D254E20B49ED | 2023-05-13 09:55:10 | 2023-05-13 09:55:10 | False | False | NULL |

---


## dbo.XStudio_Alarm_Viewer_Filter_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| AreaName | varchar | YES | 100 | — |
| TagName | varchar | YES | 100 | — |
| TagValue | decimal | YES | 18,4 | — |
| AlarmState | varchar | YES | 100 | — |
| AlarmType | varchar | YES | 100 | — |
| MessageType | varchar | YES | 100 | — |
| ReceivedTime | datetime | YES | — | — |
| EventTime | datetime | YES | — | — |
| AcknowledgeTime | datetime | YES | — | — |
| RetrunTime | datetime | YES | — | — |
| Remark | varchar | YES | 100 | — |
| Description | varchar | YES | 100 | — |

---


## dbo.XStudio_Shift_Dtl_Tbl

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| SrNo | int | YES | 10,0 | — |
| StartTime | time | YES | — | — |
| EndTime | time | YES | — | — |

---


## dbo.XStudio_Shift_Mst_Tbl

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| NoOfShift | int | YES | 10,0 | — |
| SrNo | int | YES | 10,0 | — |

---


## dbo.priority_mst

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-08-06 15:37:52 to 2025-08-06 15:45:35  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| priority | varchar | YES | 100 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| Icon | varchar | YES | 200 | — |

### Top 10 Records

| ID | priority | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CB077E82-9055-430B-AC00-F7C7F56F51DD | Critical | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2022-08-12 14:26:28 | 2025-08-06 15:37:52 | False | False | NULL |  |
| 65BE0464-2E42-4CBA-9ADF-F8E19E90B5B2 | High Priority | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2022-08-12 14:26:02 | 2025-08-06 15:39:06 | False | False | NULL |  |
| EEF8F1D9-180E-49E4-95C3-3F5CB0408028 | Standard | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2022-08-12 14:29:10 | 2025-08-06 15:45:35 | False | False | NULL |  |

---


## dbo.subarea

**Primary Key:** ID  
**Row Count:** 19  
**Date Range (ModifiedOn):** 2022-08-12 13:19:39 to 2025-08-06 11:35:22  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| area | varchar | YES | -1 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BD4A6C38-625F-41E0-8808-C088BC687FDF | Tag Scanning | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-12 13:19:39 | 2022-08-12 13:19:39 | False | False | NULL |
| 033718A7-6DAA-4177-B07D-79998AF3A75E | User Access | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-12 13:30:46 | 2022-08-12 13:30:46 | False | False | NULL |
| D86EDE27-EA27-45E5-A9A4-E50106A83928 | Role Rights | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-12 13:51:18 | 2022-08-12 13:51:18 | False | False | NULL |
| F605E04E-D07A-4EFF-980B-50034DAC578A | Reports | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-12 15:44:37 | 2022-08-12 15:44:37 | False | False | NULL |
| CA6B9FF4-90FF-435A-B562-0ED7096B4919 | Tablet  | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 2022-08-12 13:30:36 | 2022-09-22 14:39:13 | False | False | NULL |
| 3DC69284-0192-4460-BBE9-2D78F329E500 | Register/Format | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | 5FE97C53-D3CA-4ABA-B52C-C1A8AE3934EF | 2022-08-12 13:17:36 | 2022-12-06 16:38:16 | False | False | NULL |
| CB3EA3B7-EFD0-47F7-8585-E003B798B1EC | Customization | NULL | FBB82B7F-78F9-49B2-B396-C459C56235B1 | FBB82B7F-78F9-49B2-B396-C459C56235B1 | 2023-04-18 11:13:46 | 2023-04-18 11:13:46 | False | False | NULL |
| 95D8FFF4-F100-41D7-819F-806F2DAD6CDB | Register/Format | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2022-08-12 13:31:06 | 2025-08-05 16:25:53 | True | False | NULL |
| 7EFFBECC-BD60-4B3D-8E7C-C39414558019 | Bangalore Servers | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2022-08-12 13:30:05 | 2025-08-05 16:26:04 | True | False | NULL |
| EB5E7751-980A-4757-A2FD-4E275292DBEC | Bangalore SAN | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2022-08-12 13:30:17 | 2025-08-05 16:26:08 | True | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 59881DB3-CAAB-46DB-973E-E50F807B9BF1 | UAT | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-06 11:35:22 | 2025-08-06 11:35:22 | False | False | NULL |
| EC3953CD-A26B-458A-B362-2E1102AC74A4 | Data Sync | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2022-08-12 13:30:52 | 2025-08-05 16:28:27 | True | False | NULL |
| 4BF92639-85A7-4A89-8787-95E4EFEFD61B | NFC Tags | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2022-08-12 13:30:30 | 2025-08-05 16:28:11 | True | False | NULL |
| 9A787139-E455-414E-ABE9-8319853B840F | Local Client Software Installation | NULL | 2872F583-6495-4CCC-93B3-98A4E63858A4 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2022-10-18 17:01:33 | 2025-08-05 16:28:08 | True | False | NULL |
| A6CA29BE-2798-4C20-9732-208124B2C521 | Version Update | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2022-08-12 13:31:33 | 2025-08-05 16:27:35 | True | False | NULL |
| 9302724F-EDFD-4BCF-BDC2-708322BDC64B | Router | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2022-08-12 13:29:46 | 2025-08-05 16:27:04 | True | False | NULL |
| 24774047-C5FE-4D34-BF92-B72845D592F0 | PLHO SAN | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2022-08-12 13:30:11 | 2025-08-05 16:26:28 | True | False | NULL |
| D87A8081-C261-4C45-837D-843CA331627D | PLHO Servers | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2022-08-12 13:29:57 | 2025-08-05 16:26:25 | True | False | NULL |
| 6DEA694C-5517-49BF-B666-4D7B791B7D73 | Role Rights | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2022-08-12 13:49:01 | 2025-08-05 16:26:13 | True | False | NULL |
| EB5E7751-980A-4757-A2FD-4E275292DBEC | Bangalore SAN | NULL | 0E06BAC4-DD4B-4ADB-9F8C-58BFF94711E8 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2022-08-12 13:30:17 | 2025-08-05 16:26:08 | True | False | NULL |

---


## dbo.subarea_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| area | varchar | YES | -1 | — |

---


## dbo.subareadetails

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | -1 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| subarea | varchar | YES | -1 | — |

---


## dbo.subareadetails_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | -1 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| subarea | varchar | YES | -1 | — |

---


## dbo.systemreferencedocuments

**Primary Key:** ID  
**Row Count:** 12  
**Date Range (ModifiedOn):** 2025-08-11 13:36:47 to 2025-11-11 13:39:07  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| versionno | varchar | YES | 100 | — |
| Description | varchar | YES | -1 | — |
| releasedate | date | YES | — | — |
| document | varchar | YES | 8000 | — |
| documenttype | varchar | YES | -1 | — |
| srno | int | YES | 10,0 | — |
| DOCXDocument | varchar | YES | 8000 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7873D569-4637-4791-88CE-13B30DA71526 | USER GUIDE BOOKLET-1 - Helpdesk Usage guide | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-08-08 12:05:07 | 2025-08-11 13:36:47 | False | False | NULL |
| 8044D88A-E15D-49B8-92DF-7AC5FCB38099 | USER GUIDE BOOKLET-2 - SMS KPI Module | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-08-11 13:37:58 | 2025-08-11 13:37:58 | False | False | NULL |
| E86A4EA5-D71D-482C-A3C1-0454F4D41382 | USER GUIDE BOOKLET-4 SMS Delay Conditions | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-10-06 11:47:40 | 2025-10-06 11:48:07 | False | False | NULL |
| 5CD4B9B0-0E39-45FD-B838-4E93A0A79016 | USER GUIDE BOOKLET-5 RM Delay Conditions | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-10-06 11:49:31 | 2025-10-06 11:49:31 | False | False | NULL |
| 802F96FD-A976-4309-A778-C0BDBA9D9315 | USER GUIDE BOOKLET-3 User Manual of Billet Yard Management | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-10-06 10:01:32 | 2025-10-06 11:50:40 | False | False | NULL |
| 71DBB701-E842-422E-B525-4848CF89EDBD | USER GUIDE BOOKLET-6 EAF KPI Module | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-11 13:25:17 | 2025-11-11 13:25:17 | False | False | NULL |
| E49E0FAD-4C2D-4D61-9240-800A8780F348 | USER GUIDE BOOKLET-7 LRF KPI Module | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-11 13:26:51 | 2025-11-11 13:26:51 | False | False | NULL |
| 77C33B74-B457-479E-BEE9-65613F2301AC | USER GUIDE BOOKLET-8 CCM KPI Module | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-11 13:27:59 | 2025-11-11 13:27:59 | False | False | NULL |
| 112A3D25-BD2B-4A16-9260-11C12130FE03 | USER GUIDE BOOKLET-10 Billet Length Conditions | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-11 13:34:30 | 2025-11-11 13:34:50 | False | False | NULL |
| FAD5ED93-6769-4C34-92E1-280BA01C35F6 | USER GUIDE BOOKLET-12 Mill Module | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-11 13:35:56 | 2025-11-11 13:38:01 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5EF5C48B-9B44-4050-80FA-DBE4546086C3 | USER GUIDE BOOKLET-9 CCM KPI Module Billets Production | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-11 13:39:07 | 2025-11-11 13:39:07 | False | False | NULL |
| 4EB5B12A-7596-4736-B4B2-0A71E95EAB49 | USER GUIDE BOOKLET-11 Billet In Furnace Conditions | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-11 13:33:30 | 2025-11-11 13:38:15 | False | False | NULL |
| FAD5ED93-6769-4C34-92E1-280BA01C35F6 | USER GUIDE BOOKLET-12 Mill Module | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-11 13:35:56 | 2025-11-11 13:38:01 | False | False | NULL |
| 112A3D25-BD2B-4A16-9260-11C12130FE03 | USER GUIDE BOOKLET-10 Billet Length Conditions | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-11 13:34:30 | 2025-11-11 13:34:50 | False | False | NULL |
| 77C33B74-B457-479E-BEE9-65613F2301AC | USER GUIDE BOOKLET-8 CCM KPI Module | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-11 13:27:59 | 2025-11-11 13:27:59 | False | False | NULL |
| E49E0FAD-4C2D-4D61-9240-800A8780F348 | USER GUIDE BOOKLET-7 LRF KPI Module | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-11 13:26:51 | 2025-11-11 13:26:51 | False | False | NULL |
| 71DBB701-E842-422E-B525-4848CF89EDBD | USER GUIDE BOOKLET-6 EAF KPI Module | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-11 13:25:17 | 2025-11-11 13:25:17 | False | False | NULL |
| 802F96FD-A976-4309-A778-C0BDBA9D9315 | USER GUIDE BOOKLET-3 User Manual of Billet Yard Management | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-10-06 10:01:32 | 2025-10-06 11:50:40 | False | False | NULL |
| 5CD4B9B0-0E39-45FD-B838-4E93A0A79016 | USER GUIDE BOOKLET-5 RM Delay Conditions | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-10-06 11:49:31 | 2025-10-06 11:49:31 | False | False | NULL |
| E86A4EA5-D71D-482C-A3C1-0454F4D41382 | USER GUIDE BOOKLET-4 SMS Delay Conditions | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-10-06 11:47:40 | 2025-10-06 11:48:07 | False | False | NULL |

---


## dbo.systemreferencedocuments_Audit

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| versionno | varchar | YES | 100 | — |
| Description | varchar | YES | -1 | — |
| releasedate | date | YES | — | — |
| document | varchar | YES | 8000 | — |
| documenttype | varchar | YES | -1 | — |
| srno | int | YES | 10,0 | — |
| DOCXDocument | varchar | YES | 8000 | — |

---
