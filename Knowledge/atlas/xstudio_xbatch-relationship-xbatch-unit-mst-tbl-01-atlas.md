---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xbatch-unit-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XBatch_Unit_Mst_Tbl.CurrentBatchID -> XBatch_Batch_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CurrentBatchID-XBatch_Batch_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Unit_Mst_Tbl.CurrentUnitProcedureID -> XBatch_Batch_Unit_Procedure_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CurrentUnitProcedureID-XBatch_Batch_Unit_Procedure_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Unit_Mst_Tbl.ParentID -> XBatch_Process_Cell_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Process_Cell_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
