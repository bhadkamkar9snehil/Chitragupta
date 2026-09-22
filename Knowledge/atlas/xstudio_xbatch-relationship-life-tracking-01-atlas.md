---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: life-tracking part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Life_Tracking.Area -> Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Area-Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Life_Tracking.LifeName -> LifeName_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: LifeName-LifeName_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
