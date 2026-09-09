---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: productionweeklytargets part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## ProductionWeeklyTargets.Month -> ProductionMonthlyTargets.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Month-ProductionMonthlyTargets
Provenance: xstudio_configuration_relationship (1 source row(s))

## ProductionWeeklyTargets.Week -> Week_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Week-Week_Master
Provenance: xstudio_configuration_relationship (1 source row(s))
