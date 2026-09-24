---
type: procedure
title: "SP_GET_AREAWISE_TAG_TREND"
built: "2026-09-24T11:36:36"
---

# SP_GET_AREAWISE_TAG_TREND

Parameters: @Heatno int, @Tagarea nvarchar, @SRNO int.

## Reads

- BilletsCastCount: EndTime, HeatID, IsDeleted, StartTime
- EAF_PER_HEAT: EndTime, HeatID, HeatStart, IsDeleted
- LRF_Per_Heat: EndTime, HeatID, IsDeleted, StartTime
- Tag_Configuration: Area, IsDeleted, MappedTag, Srno
