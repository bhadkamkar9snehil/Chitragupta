---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: billet-inventory-view part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Billet_Inventory_View.BOMid -> XBatch_Formula_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: BOMid-XBatch_Formula_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Billet_Inventory_View.GradeID -> XBatch_Material_Grade_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: GradeID-XBatch_Material_Grade_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Billet_Inventory_View.MaterialID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MateriaiID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Billet_Inventory_View.OperationID -> XBatch_Batch_Operation_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: OperationID-XBatch_Batch_Operation_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Billet_Inventory_View.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOMID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
