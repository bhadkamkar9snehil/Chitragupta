---
type: procedure
title: "XMES_EAF_SprayCoolingFlowDuration_USP"
built: "2026-09-24T11:36:36"
---

# XMES_EAF_SprayCoolingFlowDuration_USP

Parameters: @HeatID varchar, @StartTime datetime, @EndTime datetime.

## Writes

- EAF_PER_HEAT: E1SprayCollingFlowDurationSec, E2SprayCollingFlowDurationSec, E3SprayCollingFlowDurationSec

## Reads

- EAF_PER_HEAT: HeatID, IsDeleted
