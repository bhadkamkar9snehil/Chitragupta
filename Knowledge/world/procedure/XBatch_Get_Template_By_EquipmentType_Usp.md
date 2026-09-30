---
type: procedure
title: "XBatch_Get_Template_By_EquipmentType_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Get_Template_By_EquipmentType_Usp

Parameters: @Type varchar, @EquipmentTypeID varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- Equipment_Type_Mst_Tbl: BatchingEquipmentClass, ID, IsBatchingEntity, IsDeleted, Name
