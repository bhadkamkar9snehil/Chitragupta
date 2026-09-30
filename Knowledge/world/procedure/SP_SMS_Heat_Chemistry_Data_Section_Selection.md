---
type: procedure
title: "SP_SMS_Heat_Chemistry_Data_Section_Selection"
built: "2026-09-24T11:36:36"
---

# SP_SMS_Heat_Chemistry_Data_Section_Selection

Parameters: @FirstHeat varchar, @LastHeat varchar, @Grade varchar.

## Writes

- Heat_Chemistry_Quality_Data: Grade

## Reads

- Heat_Chemistry_Quality_Data: HeatNo, IsDeleted
