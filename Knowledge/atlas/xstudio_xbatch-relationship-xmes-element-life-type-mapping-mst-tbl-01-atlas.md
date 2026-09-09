---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xmes-element-life-type-mapping-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_Element_Life_Type_Mapping_Mst_Tbl.ElementType -> XMES_Life_Element_Type_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ElementType-XMES_Life_Element_Type_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Element_Life_Type_Mapping_Mst_Tbl.ParentID -> XMES_Life_Tracker_Register_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_Life_Tracker_Register_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
