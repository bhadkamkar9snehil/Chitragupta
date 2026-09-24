---
type: procedure
title: "SP_SMS_Producation_Summary"
built: "2026-09-24T11:36:36"
---

# SP_SMS_Producation_Summary

Parameters: @ReportDate date.

## Writes

- CCM_Per_Heat: ReportDate
- Highest_Production_Entry: Availability, AvailabilityDate, BestAspect, DayProduction, DayProductionDate, EntryDateTime, HighestProduction, HighestProductionDate, LadleLife, LongestSequence, LongestSequenceDate, Rejections, ReportDate, ShellLife, Source, Status
- SMS_Production_Summary: BestDay, BestDayDate, BestMonth, BestMonthDate, EntryDateTime, FTDPercentage, FTDTon, IsDeleted, MTDPercentage, MTDTon, Particulars, ReportDate, Reportdatetext, Source, Type, UOM

## Reads

- Agency_Wise_Delay: Agency, Duration, IsDeleted, ParentID
- CCM_Per_Heat: HeatReportDate, IsDeleted, LadleSequence
- DelayAgency_Master: AreaName, ID, IsDeleted, Name
- DelaySubType_Master: ID, IsDeleted, Name
- EAF_PER_HEAT: CdriConsumption, HBIConsumption, IsDeleted, ReportDate
- Heat_End_Selection_Trn_Tbl: CalTimeinMinutes, IsDeleted, ModifiedOn, ReportDate
- Highest_Production_Entry: IsDeleted
- Particulars_Masters: CreatedOn, IsDeleted, Particulars, Type, UOM
- Power_Consumption_Report: EntryDateTime, OxygenPlant4A, SMSAuxWithoutO2
- SMS_Production_Summary: IsDeleted, MTDTon, Particulars, ReportDate
- ShiftDelayEntry: AreaName, DelayInMinutes, DelaySubtypeid, DelayType, ID, IsDeleted, ReportDate, SMSReportDate

## Calls

- XMES_Recalculate_BackCalculation_GLS_USP
