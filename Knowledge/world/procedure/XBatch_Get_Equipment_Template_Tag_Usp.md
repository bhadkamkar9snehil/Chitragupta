---
type: procedure
title: "XBatch_Get_Equipment_Template_Tag_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Get_Equipment_Template_Tag_Usp

Parameters: @EquipmentTypeID varchar, @TemplateID varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- Equipment_Type_Mst_Tbl: BatchingEquipmentClass, ID, Name
