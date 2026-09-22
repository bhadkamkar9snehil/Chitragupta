---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: electricity-meter-electricity-bill-details part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Electricity_Meter_Electricity_Bill_Details.TimeOfUse -> Rate_Band_Master.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: TimeOfUse-Rate_Band_Master
Provenance: xstudio_configuration_relationship (1 source row(s))
