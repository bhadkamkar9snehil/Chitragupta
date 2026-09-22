---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xmes-live-billet-charging-bed part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_Live_Billet_Charging_Bed.ID -> XMES_Billet_Tracking_Trn_Tbl.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ID-XMES_Billet_Tracking_Trn_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Live_Billet_Charging_Bed.ParentID -> RM_Operator_HeatSelection.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-RM_Operator_HeatSelection
Provenance: xstudio_configuration_relationship (1 source row(s))
