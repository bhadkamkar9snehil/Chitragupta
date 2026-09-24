---
type: procedure
title: "XMES_U_SMS_Production_Summary_BestData_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_U_SMS_Production_Summary_BestData_Usp

Parameters: @BestDayDate date, @BestMonthDate date, @Particular varchar.

## Writes

- SMS_Production_Summary: BestDay, BestDayDate, BestMonth, BestMonthDate, FTDPercentage, FTDTon, MTDPercentage, MTDTon

## Reads

- SMS_Production_BestDay_BestMonth_Data: BestDayDate, BestMonthDate, FTDPercentageBestDay, FTDPercentageBestMonth, FTDTonBestDay, FTDTonBestMonth, IsDeleted, MTDPercentageBestDay, MTDPercentageBestMonth, MTDTonBestDay, MTDTonBestMonth, Particulars
- SMS_Production_Summary: IsDeleted, Particulars, ReportDate
