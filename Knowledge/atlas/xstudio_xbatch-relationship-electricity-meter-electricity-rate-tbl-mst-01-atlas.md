---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: electricity-meter-electricity-rate-tbl-mst part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Electricity_Meter_Electricity_Rate_Tbl_Mst.Months -> Month_Master.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Months-Month_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electricity_Meter_Electricity_Rate_Tbl_Mst.Year -> Year_Master.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Year-Year_Master
Provenance: xstudio_configuration_relationship (1 source row(s))
