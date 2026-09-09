---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: storage-location-mst part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Storage_Location_MST.Plant -> Plant_Name_MST.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Plant-Plant_Name_MST
Provenance: xstudio_configuration_relationship (1 source row(s))
