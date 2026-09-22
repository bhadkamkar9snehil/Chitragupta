---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xmes-stage-position-mapping-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_Stage_Position_Mapping_Mst_Tbl.PositionType -> XMES_State_Position_State_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: PositionType-XMES_State_Position_State_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Stage_Position_Mapping_Mst_Tbl.StageCode -> XMES_Process_Stage_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StageCode-XMES_Process_Stage_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
