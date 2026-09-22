---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: rm-charging-plan part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## RM_Charging_Plan.MaterialId -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialId-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
