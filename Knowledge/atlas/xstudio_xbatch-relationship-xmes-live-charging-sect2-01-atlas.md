---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xmes-live-charging-sect2 part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_Live_Charging_SECT2.ID -> XMES_RM_Furnace_Billet_Trn_Tbl.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> Many
Relation: ID-XMES_RM_Furnace_Billet_Trn_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Live_Charging_SECT2.ParentID -> XMES_Live_Charging_SECT1.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_Live_Charging_SECT1
Provenance: xstudio_configuration_relationship (1 source row(s))
