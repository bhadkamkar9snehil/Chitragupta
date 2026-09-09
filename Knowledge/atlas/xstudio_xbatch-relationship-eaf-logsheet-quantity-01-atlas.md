---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: eaf-logsheet-quantity part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## EAF_LogSheet_Quantity.Grade -> Grade_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## EAF_LogSheet_Quantity.HeatNo -> EAF_PER_HEAT.HeatID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: HeatNo-EAF_PER_HEAT
Provenance: xstudio_configuration_relationship (1 source row(s))

## EAF_LogSheet_Quantity.TestName -> Grade_Test_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: TestName-Grade_Test_Master
Provenance: xstudio_configuration_relationship (1 source row(s))
