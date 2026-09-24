---
type: procedure
title: "XStudio_Update_Day_Consumptions_Usp"
built: "2026-09-24T11:36:36"
---

# XStudio_Update_Day_Consumptions_Usp

Parameters: @ReportDate date.

## Writes

- Consumptions_Summary_Day: EAF_YD, LRF_YD, ModifiedOn, OxygenPlant4A_YD, RollingMill_YD, Source, Transformer132kv1_YD, Transformer132kv2_YD, Transformer15MVA_YD, Transformer24MVA_YD, Transformer33kv1_YD, Transformer33kv2_YD, WRM_YD

## Reads

- Consumptions_Summary_Day: EAF, IsDeleted, LRF, OxygenPlant4A, ReportDate, RollingMill, Transformer132kv1, Transformer132kv2, Transformer15MVA, Transformer24MVA, Transformer33kv1, Transformer33kv2, WRM
