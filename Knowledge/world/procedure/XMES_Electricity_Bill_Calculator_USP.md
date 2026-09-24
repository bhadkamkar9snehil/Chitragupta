---
type: procedure
title: "XMES_Electricity_Bill_Calculator_USP"
built: "2026-09-24T11:36:36"
---

# XMES_Electricity_Bill_Calculator_USP

Parameters: @EntryDAte date.

## Writes

- Electricity_Meter_Bill_Amount: AccountNo, CreatedOn, DistributionSystemCharge, FeederName, ModifiedOn, Month, MonthNumber, MonthYear, Source, SupplyServiceCharge, TotalEnergyCharge, TotalEngeryConsumptionCalculate, Year
- Electricity_Meter_Bill_Details_Time_Of_Use: CreatedOn, FeederName, Month, MonthNumber, Rate, ReportDate, Source, TimeofUse, Year
- Electricity_Meter_Electricity_Bill_Details: Charge, Consumption, CreatedOn, FeederName, ModifiedOn, Month, MonthNumber, Rate, ReportDate, Source, TimeOfUse, Year
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- Electricity_Meter_Bill_Amount: IsDeleted
- Electricity_Meter_Bill_Details_Time_Of_Use: FeederName, Month, TimeofUse, Year
- Electricity_Meter_Electricity_Bill_Details: Charge, Consumption, FeederName, IsDeleted, Month, MonthNumber, ReportDate, Year
- Electricity_Meter_Electricity_Rate_Tbl_Mst: EntryDatetime, IsDeleted, Months, NightPeak, OffPeak, WeekdayDayPeak, WeekendDayPeak, Year
- Electricity_Meter_Reading: Consumption, EndDateTime, FeederName, IsDeleted, ReportDate
- Electricity_Meter_Timing: DayOfWeek, EntryDatetime, FromTime, IsDeleted, RateBand, ToTime, Weekdays, Year
- Rate_Band_Master: ID, IsDeleted, Name

## What its own log shows

1,816 log rows, 2026-05-28 15:12 to 2026-09-02 07:10.

Steps:
- 1 Entered
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 01-Aug-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 01-Feb-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 01-Jul-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 01-Jun-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 01-May-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 01-Sep-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 02-Apr-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 02-Aug-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 02-Jul-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 02-Jun-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 02-May-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 03-Aug-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 03-Jul-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 03-Jun-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 04-Aug-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 04-Jul-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 04-Jun-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 05-Aug-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 05-Jul-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 05-Jun-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 06-Aug-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 06-Jul-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 06-Jun-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 07-Aug-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 07-Jul-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 07-Jun-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 08-Aug-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 08-Jul-2026 Start
- 2 Insert Calculated Consumption and rate data into table variable for reportdate 08-Jun-2026 Start

Example call: `EXEC XStudio_Xbatch.dbo.XMES_Electricity_Bill_Calculator_USP @EntryDAte='31-May-2026'`
