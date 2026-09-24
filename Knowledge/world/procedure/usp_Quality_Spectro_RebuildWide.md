---
type: procedure
title: "usp_Quality_Spectro_RebuildWide"
built: "2026-09-24T11:36:36"
---

# usp_Quality_Spectro_RebuildWide

Parameters: @SampleID varchar, @FromDate datetime, @ToDate datetime, @HeatNo varchar.

## Reads

- Quality_Spectro_Sample: HeatNo, ID, XMLCreatedAt

## Calls

- usp_Quality_Spectro_BuildWideForSample
