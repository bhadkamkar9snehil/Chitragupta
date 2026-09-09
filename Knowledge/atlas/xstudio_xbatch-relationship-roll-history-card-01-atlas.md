---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: roll-history-card part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Roll_History_Card.DeptHead -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: DeptHead-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Roll_History_Card.Signature -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: Signature-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
