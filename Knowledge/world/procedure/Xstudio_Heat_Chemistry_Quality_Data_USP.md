---
type: procedure
title: "Xstudio_Heat_Chemistry_Quality_Data_USP"
built: "2026-09-24T11:36:36"
---

# Xstudio_Heat_Chemistry_Quality_Data_USP

Parameters: @ID varchar, @Mode varchar.

## Writes

- Heat_Chemistry_Quality_Data: HeatSequence, ReportDate, SampleNo, Source

## Reads

- CCM_Per_Heat: HeatID, IsDeleted, LadleSequenceText
- Heat_Chemistry_Quality_Data: HeatNo, ID, SampleType, XMLCreatedon
