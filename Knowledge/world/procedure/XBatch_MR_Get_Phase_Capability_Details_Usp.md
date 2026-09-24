---
type: procedure
title: "XBatch_MR_Get_Phase_Capability_Details_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_MR_Get_Phase_Capability_Details_Usp

Parameters: @PhaseID varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- XBatch_Batch_Phase_Mst_Tbl: CapabilityID, ID, IsDeleted, TemplateID
- XBatch_Equipment_Mst_Vw: EquipmentTypeName, TemplateID
