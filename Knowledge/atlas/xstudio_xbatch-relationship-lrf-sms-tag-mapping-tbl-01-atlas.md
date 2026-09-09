---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: lrf-sms-tag-mapping-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## LRF_SMS_Tag_Mapping_Tbl.DataSourceID -> XStudio_DataSource_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: DatasourceID-XStudio_DataSource_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## LRF_SMS_Tag_Mapping_Tbl.EquipmentID -> LRF_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-LRF_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
