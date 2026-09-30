---
type: procedure
title: "XSTUDIO_WORKFLOW_0C110E49-9524-40BE-9C70-4A0BEDB53C79_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_0C110E49-9524-40BE-9C70-4A0BEDB53C79_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- Electricity_Meter_Reading: Consumption, EndDateTime, FeederName, ID, Position, Price, Quality, Value

## Writes (named in its SQL text)

- Electricity_Meter_Reading
