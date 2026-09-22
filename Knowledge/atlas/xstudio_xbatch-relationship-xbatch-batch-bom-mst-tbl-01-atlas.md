---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xbatch-batch-bom-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XBatch_Batch_BOM_Mst_Tbl.ItemID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ItemID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_BOM_Mst_Tbl.OperationID -> XBatch_Batch_Operation_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: OperationID-XBatch_Batch_Operation_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_BOM_Mst_Tbl.ParentID -> XBatch_Batch_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Batch_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_BOM_Mst_Tbl.PhaseGroupID -> XBatch_Batch_Phase_Group_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: PhaseGroupID-XBatch_Batch_Phase_Group_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_BOM_Mst_Tbl.PhaseID -> XBatch_Batch_Phase_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: PhaseID-XBatch_Batch_Phase_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_BOM_Mst_Tbl.UnitProcedureID -> XBatch_Batch_Unit_Procedure_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UnitProcedureID-XBatch_Batch_Unit_Procedure_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_BOM_Mst_Tbl.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOMID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
