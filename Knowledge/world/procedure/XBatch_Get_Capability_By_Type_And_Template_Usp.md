---
type: procedure
title: "XBatch_Get_Capability_By_Type_And_Template_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Get_Capability_By_Type_And_Template_Usp

Parameters: @Type varchar, @EquipmentTypeID varchar, @EquipmentTemplateID varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- Equipment_Type_Mst_Tbl: ID, IsDeleted, Name
- XStudio_Equipment_Mst_Vw: EquipmetTypeID, TemplateID
