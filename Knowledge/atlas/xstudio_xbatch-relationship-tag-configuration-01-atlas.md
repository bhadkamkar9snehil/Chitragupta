---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: tag-configuration part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Tag_Configuration.Area -> Area_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Area-Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Tag_Configuration.HeatID -> EAF_PER_HEAT.HeatID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: HeatID-EAF_PER_HEAT
Provenance: xstudio_configuration_relationship (1 source row(s))
