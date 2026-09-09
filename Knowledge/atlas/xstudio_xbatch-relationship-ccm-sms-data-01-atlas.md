---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: ccm-sms-data part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## CCM_SMS_Data.EquipmentID -> CCM_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-CCM_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
