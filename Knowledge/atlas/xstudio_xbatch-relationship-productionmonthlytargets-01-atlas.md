---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: productionmonthlytargets part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## ProductionMonthlyTargets.FiscalYear -> financialyears.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: FiscalYear-financialyears
Provenance: xstudio_configuration_relationship (1 source row(s))
