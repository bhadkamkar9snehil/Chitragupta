---
type: procedure
title: "Xstudio_Historian_EAF_Custom_usp"
built: "2026-09-24T11:36:36"
---

# Xstudio_Historian_EAF_Custom_usp

Parameters: @StartTime datetime, @EndTime datetime, @Attribute varchar, @Equipment varchar, @CollectorID varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- EAF_PER_HEAT: EndTime, HeatStart, ID
