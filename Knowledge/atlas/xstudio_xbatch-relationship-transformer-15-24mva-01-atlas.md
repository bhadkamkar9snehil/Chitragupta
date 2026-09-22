---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: transformer-15-24mva part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Transformer_15_24MVA.EngineerName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: EngineerName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Transformer_15_24MVA.TechnicianName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: TechnicianName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
