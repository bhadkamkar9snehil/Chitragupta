---
type: procedure
title: "XMES_CCM_BILLET_MASTER_CREATE_USP"
built: "2026-09-24T11:36:36"
---

# XMES_CCM_BILLET_MASTER_CREATE_USP

Parameters: @ProducedEventID varchar.

## Writes

- XMES_CCM_Billet_Master_Trn_Tbl: Batch, BilletNo, BilletQuantity, BilletWeight, CreatedBy, EntryDateTime, HeatNo, IsProcessed, ManufacturingOrder, Materialid, ModifiedBy, Name, Plant, ProcessStage, Qualitygradeid, ReportDate, Source, UOMID

## Reads

- CCM_Per_Heat: Grade, HeatID, Material, WorkOrder
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name, UnitID
- XBatch_Work_Order_Mst_Tbl: ID, IsDeleted, ProductionPlant
- XMES_CCM_Billet_Genealogy_Trn_Tbl: BilletNo, HeatNo, IsDeleted, ProducedEndTime, ProducedEventID, Status
- XMES_CCM_Billet_Master_Trn_Tbl: IsDeleted
