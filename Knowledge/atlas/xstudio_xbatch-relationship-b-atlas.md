---
type: Reference
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: B

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Billet_ChargingPlan.entityid -> XStudio_Entities_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: entityid-XStudio_Entities_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Billet_Cross_Section.CreatedBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: CreatedBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Billet_Inventory.BOMid -> XBatch_Formula_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: BOMid-XBatch_Formula_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Billet_Inventory.GradeID -> XBatch_Material_Grade_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: GradeID-XBatch_Material_Grade_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Billet_Inventory.MaterialID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MateriaiID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Billet_Inventory.OperationID -> XBatch_Batch_Operation_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: OperationID-XBatch_Batch_Operation_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Billet_Inventory.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOMID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

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

## Breakers_Details.EngineerName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: EngineerName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Breakers_Details.TechnicianName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: TechnicianName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

