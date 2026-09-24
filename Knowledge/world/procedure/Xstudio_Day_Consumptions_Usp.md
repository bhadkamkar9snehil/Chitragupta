---
type: procedure
title: "Xstudio_Day_Consumptions_Usp"
built: "2026-09-24T11:36:36"
---

# Xstudio_Day_Consumptions_Usp

Parameters: @ID varchar, @DatabaseName varchar, @EntityName varchar.

## Writes

- Consumptions_Summary_Day: EAF, LRF, ModifiedOn, OxygenPlant4A, ReportDate, RollingMill, Source, Transformer132kv1, Transformer132kv2, Transformer15MVA, Transformer24MVA, Transformer33kv1, Transformer33kv2, WRM

## Reads

- Power_Consumption_LogSheet: EAF, EntryDateTime, ID, IsDeleted, LRF, OxygenPlant4A, RollingMill, Transformer132kv1, Transformer132kv2, Transformer15MVA, Transformer24MVA, Transformer33kv1, Transformer33kv2, WRM

## Calls

- XStudio_Update_Day_Consumptions_Usp
