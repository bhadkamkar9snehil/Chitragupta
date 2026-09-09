---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: rebar-quality-data part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Rebar_Quality_Data.BilletGrade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: BilletGrade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Rebar_Quality_Data.Grade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Rebar_Quality_Data.HeatNo -> EAF_PER_HEAT.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: HeatNo-EAF_PER_HEAT
Provenance: xstudio_configuration_relationship (1 source row(s))

## Rebar_Quality_Data.ShiftInChargeOperation -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: ShiftInChargeOperation-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
