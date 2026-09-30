---
type: procedure
title: "XMES_I_Particulars_for_BestData_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_I_Particulars_for_BestData_Usp

Parameters: @bestdaydate date, @bestMonthDate date.

## Writes

- SMS_Production_BestDay_BestMonth_Data: BestDayDate, BestMonthDate, FTDPercentageBestDay, FTDPercentageBestMonth, FTDTonBestDay, FTDTonBestMonth, MTDPercentageBestDay, MTDPercentageBestMonth, MTDTonBestDay, MTDTonBestMonth, Particulars, Srno, Type, UOM

## Reads

- Particulars_Masters: IsDeleted, Particulars, SrNo, Type, UOM
