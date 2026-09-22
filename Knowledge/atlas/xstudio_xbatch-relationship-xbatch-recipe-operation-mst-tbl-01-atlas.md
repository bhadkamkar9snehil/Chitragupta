---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xbatch-recipe-operation-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XBatch_Recipe_Operation_Mst_Tbl.EquipmentTypeID -> Equipment_Type_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentTypeID-Equipment_Type_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Recipe_Operation_Mst_Tbl.OutputMaterialID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: OutputMaterialID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Recipe_Operation_Mst_Tbl.ParentID -> XBatch_Recipe_Unit_Procedure_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Recipe_Unit_Procedure_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
