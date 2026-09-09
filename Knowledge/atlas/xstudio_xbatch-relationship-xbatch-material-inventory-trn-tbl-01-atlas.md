---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xbatch-material-inventory-trn-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Xbatch_Material_Inventory_Trn_Tbl.MaterialGrade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialGrade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Xbatch_Material_Inventory_Trn_Tbl.ParentID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Xbatch_Material_Inventory_Trn_Tbl.PlantName -> Plant_Name_MST.Plant
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: PlantName-Plant_Name_MST
Provenance: xstudio_configuration_relationship (1 source row(s))

## Xbatch_Material_Inventory_Trn_Tbl.StorageLocation -> Storage_Location_MST.StorageLocation
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StorageLocation-Storage_Location_MST
Provenance: xstudio_configuration_relationship (1 source row(s))

## Xbatch_Material_Inventory_Trn_Tbl.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOMID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
