# XStudio_Xbatch.dbo.XStudio_List_SAP_Posting_Tbl_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| Edit | varchar | NO |
| PlantCode | varchar | YES |
| IsProcessed | bit | YES |
| ID | varchar | NO |
| EntryDateTime | datetime | YES |
| ReportDate | date | YES |
| WorkOrderNumber | varchar | YES |
| HeatNo | varchar | YES |
| BatchNoorBilletNo | varchar | YES |
| MaterialCode | varchar | YES |
| StorageLocation | varchar | YES |
| Quantity | decimal | YES |
| UnitofMeasure | varchar | YES |
| MovementType | varchar | YES |
| PostingType | varchar | YES |
| PostingDate | datetime | YES |
| CreatedOn | datetime | YES |
| CreatedBy | varchar | YES |
| ModifiedOn | datetime | YES |
| Delete | varchar | NO |
| ModifiedBy | varchar | YES |
| SAPStatus | varchar | YES |
| SAPDocumentNo | varchar | YES |
| Details | varchar | NO |
| SAPMessage | varchar | YES |
| CreatedByid | varchar | YES |
| SAPPayloadJSON | varchar | YES |
| ModifiedByid | varchar | YES |
| MaterialColourCode | varchar | YES |
| StorageColourCode | varchar | YES |
| WorkOrderColourCode | varchar | YES |

## Sample rows (top 5, real live data)

| Edit | PlantCode | IsProcessed | ID | EntryDateTime | ReportDate | WorkOrderNumber | HeatNo | BatchNoorBilletNo | MaterialCode | StorageLocation | Quantity | UnitofMeasure | MovementType | PostingType | PostingDate | CreatedOn | CreatedBy | ModifiedOn | Delete | ModifiedBy | SAPStatus | SAPDocumentNo | Details | SAPMessage | CreatedByid | SAPPayloadJSON | ModifiedByid | MaterialColourCode | StorageColourCode | WorkOrderColourCode |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {"Link": "XBatch/ControlRoom/Edit_Page_SAP_Posting_Tbl","LinkTarget": "null","Pa | SMS |  | 006CB253-B0D8-4A2E-A71C-95B3B9A63AD5 |  |  | WO_001 | 1506341 |  | Dolo | ScrapYard | 2.340 | ton | 261 | Consumption | 2025-11-01 00:00:00 | 2025-10-30 07:58:50.670000 |  |  | {"LvId": "0CDE710F-8FA9-4B6A-B819-644584AFA022","RecordId" : "006CB253-B0D8-4A2E |  | Pending |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"0CDE710F-8FA9-4B6A-B8 |  |  |  |  |  | background-color:#b87a47; color:#ffffff |  |
| {"Link": "XBatch/ControlRoom/Edit_Page_SAP_Posting_Tbl","LinkTarget": "null","Pa | SMS |  | 00AB9E1D-3369-443E-A090-926DE652A8C6 |  |  | WO_001 | 1506339 |  | Skull | ScrapYard | 3.500 | ton | 261 | Consumption | 2025-11-01 00:00:00 | 2025-10-30 06:06:14.827000 |  |  | {"LvId": "0CDE710F-8FA9-4B6A-B819-644584AFA022","RecordId" : "00AB9E1D-3369-443E |  | Pending |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"0CDE710F-8FA9-4B6A-B8 |  |  |  |  | background-color:#a95677; color:#ffffff | background-color:#b87a47; color:#ffffff |  |
| {"Link": "XBatch/ControlRoom/Edit_Page_SAP_Posting_Tbl","LinkTarget": "null","Pa | SMS |  | 0620F7F2-CEB5-40C3-B3C2-9885CD512CE9 |  |  | WO_002 | 1506371 |  | GLS | BilletYard | 77.061 | ton | 101 | Production | 2025-11-01 00:00:00 | 2025-10-31 12:31:23.813000 |  |  | {"LvId": "0CDE710F-8FA9-4B6A-B819-644584AFA022","RecordId" : "0620F7F2-CEB5-40C3 |  | Pending |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"0CDE710F-8FA9-4B6A-B8 |  |  |  |  |  | background-color:#4942bd; color:#ffffff |  |
| {"Link": "XBatch/ControlRoom/Edit_Page_SAP_Posting_Tbl","LinkTarget": "null","Pa | SMS |  | 06D41AF7-8D17-4E34-B91C-79C9B383BDC5 |  |  | WO_002 | 1506373 |  | LS | BilletYard | 71.965 | ton | 101 | Production | 2025-11-01 00:00:00 | 2025-10-31 13:45:46.300000 |  |  | {"LvId": "0CDE710F-8FA9-4B6A-B819-644584AFA022","RecordId" : "06D41AF7-8D17-4E34 |  | Pending |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"0CDE710F-8FA9-4B6A-B8 |  |  |  |  | background-color:#e76508; color:#ffffff | background-color:#4942bd; color:#ffffff |  |
| {"Link": "XBatch/ControlRoom/Edit_Page_SAP_Posting_Tbl","LinkTarget": "null","Pa | SMS |  | 0BD10250-E93A-4617-A708-1FB3096CA392 |  |  | WO_002 | 1506373 | GLS_1506373 | GLS | ScrapYard | 77.680 | ton | 261 | Consumption | 2025-11-01 00:00:00 | 2025-10-31 14:44:01.360000 |  |  | {"LvId": "0CDE710F-8FA9-4B6A-B819-644584AFA022","RecordId" : "0BD10250-E93A-4617 |  | Pending |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"0CDE710F-8FA9-4B6A-B8 |  |  |  |  |  | background-color:#b87a47; color:#ffffff |  |