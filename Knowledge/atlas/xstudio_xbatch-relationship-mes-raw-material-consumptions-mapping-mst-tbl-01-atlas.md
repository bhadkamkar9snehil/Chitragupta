---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: mes-raw-material-consumptions-mapping-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.Attributeids -> XStudio_Attribute_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: Attributeids-XStudio_Attribute_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.Entityids -> XStudio_Entities_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: Entityids-XStudio_Entities_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.Materialid -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Materialid-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.Unitid -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Unitid-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
