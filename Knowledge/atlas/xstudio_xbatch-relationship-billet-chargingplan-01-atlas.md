---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: billet-chargingplan part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Billet_ChargingPlan.entityid -> XStudio_Entities_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: entityid-XStudio_Entities_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
