---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xbatch-material-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XBatch_Material_Mst_Tbl.Grade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Mst_Tbl.PageID -> XStudio_Page_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: PageID-XStudio_Page_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Mst_Tbl.PlantID -> Plant_Name_MST.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: PlantID-Plant_Name_MST
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Mst_Tbl.RawMaterialName -> MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: RawMaterialName-MES_Raw_Material_Consumptions_Mapping_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Mst_Tbl.StoragelocationID -> Storage_Location_MST.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StoragelocationID-Storage_Location_MST
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Mst_Tbl.TypeID -> XBatch_Material_Type_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: TypeID-XBatch_Material_Type_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Mst_Tbl.UnitID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UnitID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
