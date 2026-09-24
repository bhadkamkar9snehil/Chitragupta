---
type: table
title: "MES_SAP_Inventory_Stock_Tbl"
built: "2026-09-24T11:36:36"
---

# MES_SAP_Inventory_Stock_Tbl

Table in XStudio_Xbatch. Rows: 3,967.

## Identifiers it holds

- SDDocument: same values as key `SDDocument`

## Written by

- XMES_SAP_I_Inventory_Stock_Data_Usp
- XStudio_Inventory_Pull_Schedule_TSQL_Task_Usp
- api:SAP RM Hold Inventory Pull Morning (api_log)
- api:SAP RM Hot Out Billet Inventory Pull Morning (api_log)
- api:SAP RM In Inventory Pull Morning (api_log)
- api:SAP RM Local Inventory Pull Morning (api_log)
- api:SAP RM Out Inventory Pull Morning (api_log)
- api:SAP RM Raw Materials Inventory Pull Morning (api_log)
- api:SAP RM Scrapyard Inventory Pull Morning (api_log)
- api:SAP SMS Consumable Inventory Pull Morning (api_log)
- api:SAP SMS RAW Materials Inventory Stock (api_log)
- api:SAP SMS Semifinished Inventory Pull Morning (api_log)
- api:SAP SMS Shop Floor Inventory Pull Morning (api_log)
- api:SAP WRM Hold Inventory Pull Morning (api_log)
- api:SAP WRM Hot Out Billet Inventory Pull Morning (api_log)
- api:SAP WRM In Inventory Pull Morning (api_log)
- api:SAP WRM Out Inventory Pull Morning (api_log)
- api:SAP WRM Raw Materials Inventory Pull Morning (api_log)
- api:SAP WRM Scrapyard Inventory Pull Morning (api_log)

## Read by

- XMES_SAP_I_Inventory_Stock_Data_Usp
- XStudio_Inventory_Pull_Schedule_TSQL_Task_Usp

## Columns

- ID varchar(36)
- Name varchar(100)
- ParentID varchar(36)
- CreatedBy varchar(36)
- ModifiedBy varchar(36)
- CreatedOn datetime
- ModifiedOn datetime
- IsDeleted bit
- IsSystem bit
- AssignedUserID varchar(36)
- HostAddress varchar(100)
- DbSyncStatus varchar(500)
- MobileSyncStatus varchar(100)
- Source varchar(20)
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- Material varchar(100)
- Plant int
- StorageLocation varchar(100)
- Batch varchar(100)
- Supplier varchar(100)
- Customer varchar(100)
- WebElementInternalID varchar(100)
- SDDocument varchar(100)
- SDDocumentItem int
- InventorySpecialStockType varchar(100)
- InventoryStockType varchar(100)
- MaterialBaseUnit varchar(100)
- MatlWrhsStkQtyInMatlBaseUnit decimal
- MetaData varchar(-1)
- PlantName varchar(36)
