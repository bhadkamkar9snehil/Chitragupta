---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: sms-production-summary part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## SMS_Production_Summary.Particulars -> Particulars_Masters.Particulars
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Particulars-Particulars_Masters
Provenance: xstudio_configuration_relationship (1 source row(s))

## SMS_Production_Summary.Type -> Particulars_Masters.Type
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Type-Particulars_Masters
Provenance: xstudio_configuration_relationship (1 source row(s))

## SMS_Production_Summary.UOM -> Particulars_Masters.UOM
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOM-Particulars_Masters
Provenance: xstudio_configuration_relationship (1 source row(s))
