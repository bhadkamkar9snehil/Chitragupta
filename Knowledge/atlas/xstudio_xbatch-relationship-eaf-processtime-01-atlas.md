---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: eaf-processtime part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## EAF_ProcessTime.EquipmentID -> EAF_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-EAF_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
