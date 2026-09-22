---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: switchgear-panel-breaker-status part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Switchgear_Panel_Breaker_Status.EngineerName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: EngineerName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Switchgear_Panel_Breaker_Status.TechnicianName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: TechnicianName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
