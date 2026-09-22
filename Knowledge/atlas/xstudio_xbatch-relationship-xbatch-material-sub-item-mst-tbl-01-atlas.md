---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xbatch-material-sub-item-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XBatch_Material_Sub_Item_Mst_Tbl.ParentID -> XBatch_Material_Item_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Material_Item_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Sub_Item_Mst_Tbl.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UnitID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
