---
type: procedure
title: "XBatch_RM_Billet_Assign_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_RM_Billet_Assign_Usp

Parameters: @RollingPlanID varchar, @HeatNo varchar, @TotalQty int, @AssignQty int, @RequiredQty int.

## Writes

- Billet_Inventory: IsAllocated
- RM_Charging_Plan: BilletNo, CurrentLocation, HeatNo, MaterialId, PO, RollingDate, RollingID, SequenceNo, Size
- RM_Rolling_Plan: AssignedQty, Status

## Reads

- Billet_Inventory: BOMid, ID, IsDeleted, LotNumber, SublotNumber
- RM_Charging_Plan: IsDeleted
- RM_Rolling_Plan: ID, IsDeleted, MaterialID, PONumber, ReleaseRollingQty, RollingDate, RollingID, Size
- XBatch_Formula_Mst_Tbl: ID, IsDeleted, ParentID
- XBatch_Material_Mst_Tbl: ID, IsDeleted

## Calls

- XBatch_RM_Billet_Assign_SPValidation_Usp
