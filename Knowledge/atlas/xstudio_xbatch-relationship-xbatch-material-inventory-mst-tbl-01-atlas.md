---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xbatch-material-inventory-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XBatch_Material_Inventory_Mst_Tbl.GradeID -> XBatch_Material_Grade_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: GradeID-XBatch_Material_Grade_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.InwardBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: InwardBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.LocationID -> XBatch_Storage_Rack_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> Many
Relation: LocationID-XBatch_Storage_Rack_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.MaterialGrade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialGrade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.OperationID -> XBatch_Batch_Operation_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: OperationID-XBatch_Batch_Operation_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.Outwardby -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: Outwardby-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.OutwardLocation -> XBatch_OutwardLocation_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: OutwardLocation-XBatch_OutwardLocation_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.ParentID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.PlantName -> Plant_Name_MST.Plant
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: PlantName-Plant_Name_MST
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.StorageLocation -> Storage_Location_MST.StorageLocation
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StorageLocation-Storage_Location_MST
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOMID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
