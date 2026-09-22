---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xbatch-batch-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XBatch_Batch_Mst_Tbl.ParentID -> XBatch_Recipe_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Recipe_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Mst_Tbl.ProcessCellID -> XBatch_Process_Cell_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ProcessCellID-XBatch_Process_Cell_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Mst_Tbl.QuantityUnitID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CapacityUnitID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Mst_Tbl.StatusID -> XBatch_Status_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StatusID-XBatch_Status_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Mst_Tbl.WorkOrderID -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: WorkOrderID-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
