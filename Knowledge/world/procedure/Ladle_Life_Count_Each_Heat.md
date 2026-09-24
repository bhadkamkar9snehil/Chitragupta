---
type: procedure
title: "Ladle_Life_Count_Each_Heat"
built: "2026-09-24T11:36:36"
---

# Ladle_Life_Count_Each_Heat

Parameters: @RecordId varchar.

## Writes

- Life_Tracking: CurrentLife

## Reads

- LRF_Ladle_No_Per_Heat: ActiveLadle, ID, IsDeleted
- Life_Tracking: IsDeleted, Name
