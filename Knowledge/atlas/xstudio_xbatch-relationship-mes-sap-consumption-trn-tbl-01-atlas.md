---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: mes-sap-consumption-trn-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## MES_SAP_Consumption_Trn_Tbl.Saptransactionid -> XMES_SAP_API_GoodsMovement_Error.TransactionID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Saptransactionid-XMES_SAP_API_GoodsMovement_Error
Provenance: xstudio_configuration_relationship (1 source row(s))
