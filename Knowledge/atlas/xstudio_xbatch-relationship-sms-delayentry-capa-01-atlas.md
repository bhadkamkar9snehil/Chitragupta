---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: sms-delayentry-capa part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## SMS_DelayEntry_CAPA.DelayTransactionid -> ShiftDelayEntry.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: DelayTransactionid-ShiftDelayEntry
Provenance: xstudio_configuration_relationship (1 source row(s))

## SMS_DelayEntry_CAPA.Responsibility -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: Responsibility-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
