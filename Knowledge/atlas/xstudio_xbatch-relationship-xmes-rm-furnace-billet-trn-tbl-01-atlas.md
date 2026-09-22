---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xmes-rm-furnace-billet-trn-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_RM_Furnace_Billet_Trn_Tbl.HeatNo -> XBatch_Material_Inventory_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: HeatNo-XBatch_Material_Inventory_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Furnace_Billet_Trn_Tbl.ParentID -> XMES_Live_Charging_SECT2.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_Live_Charging_SECT2
Provenance: xstudio_configuration_relationship (1 source row(s))
