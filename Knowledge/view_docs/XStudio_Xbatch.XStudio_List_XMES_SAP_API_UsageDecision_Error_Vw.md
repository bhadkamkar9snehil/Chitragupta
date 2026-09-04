# XStudio_Xbatch.dbo.XStudio_List_XMES_SAP_API_UsageDecision_Error_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| Edit | varchar | NO |
| ID | varchar | NO |
| Name | varchar | YES |
| EntryDateTime | datetime | YES |
| ReportDate | date | YES |
| IsProcessed | bit | YES |
| CreatedOn | datetime | YES |
| HeatNo | varchar | YES |
| TransactionID | varchar | YES |
| RecordID | varchar | YES |
| InspectionLot | varchar | YES |
| Body | varchar | YES |
| SuccessMessage | varchar | YES |
| ErrorMessage | varchar | YES |
| Status | varchar | YES |
| Delete | varchar | NO |
| Details | varchar | NO |

## Sample rows (top 5, real live data)

| Edit | ID | Name | EntryDateTime | ReportDate | IsProcessed | CreatedOn | HeatNo | TransactionID | RecordID | InspectionLot | Body | SuccessMessage | ErrorMessage | Status | Delete | Details |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_UsageDecision_Error","LinkTa | 01D78752-1A96-486B-9E8C-434FF36256AD |  | 2026-02-21 14:11:25.960000 |  |  | 2026-02-21 14:08:25.500000 | 1601239 | 57a4c007-fd51-476f-b663-0eae85948d14 | 25950BB1-F7B0-49C5-A490-A643F1B850FA | 40002997353 | Body: {     "InspLot": "40002997353",     "UsgDecCode": "01" } |  |  Http URL: https://jsis-cpi-account-bcp9lrkq.it-cpi012-rt.cfapps.ap21.hana.ondem | PopUp | {"LvId": "69C677BD-7B34-49FB-B6D6-C991C142019E","RecordId" : "01D78752-1A96-486B | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"FBAACB05-2EE3-454F-95 |
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_UsageDecision_Error","LinkTa | 03682194-70DA-4C58-8FD8-72E9BA3D50C8 |  | 2026-05-01 01:28:40.997000 |  |  | 2026-05-01 01:28:27.247000 | 1602347 | d971b9b4-bb64-4870-9e5a-3a89c889cae0 | 98C17A67-2826-4394-80EA-271C90464FBA | 40004001609 | Body: {     "InspLot": "40004001609",     "UsgDecCode": "01" } |  |  Http URL: https://jsis-cpi-production-w76gw8lc.it-cpi012-rt.cfapps.ap21.hana.on | PopUp | {"LvId": "69C677BD-7B34-49FB-B6D6-C991C142019E","RecordId" : "03682194-70DA-4C58 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"FBAACB05-2EE3-454F-95 |
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_UsageDecision_Error","LinkTa | 03FAAD3C-2A6A-4FAB-838D-BA8AB83334A6 |  | 2026-04-23 18:02:53.780000 |  |  | 2026-04-23 17:59:05.043000 | 1602592 | d01e3e82-14ef-4146-803f-f862b7b78ac6 | 53545757-DE34-4D19-B5B4-7D2BE2EE6651 | 40004043963 | Body: {     "InspLot": "40004043963",     "UsgDecCode": "01" } |  |  Http URL: https://jsis-cpi-production-w76gw8lc.it-cpi012-rt.cfapps.ap21.hana.on | PopUp | {"LvId": "69C677BD-7B34-49FB-B6D6-C991C142019E","RecordId" : "03FAAD3C-2A6A-4FAB | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"FBAACB05-2EE3-454F-95 |
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_UsageDecision_Error","LinkTa | 0438BC84-868D-4CF5-9DC1-1517B58D5E33 |  | 2026-02-24 10:21:18.370000 |  |  | 2026-02-24 10:19:03.310000 | 1601305 | 8563b55b-80f3-44cb-a543-6acf87650233 | 69E7A2B7-7811-4E87-8B8E-911C4AC4D24B | 40002997487 | Body: {     "InspLot": "40002997487",     "UsgDecCode": "01" } |  |  Http URL: https://jsis-cpi-account-bcp9lrkq.it-cpi012-rt.cfapps.ap21.hana.ondem | PopUp | {"LvId": "69C677BD-7B34-49FB-B6D6-C991C142019E","RecordId" : "0438BC84-868D-4CF5 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"FBAACB05-2EE3-454F-95 |
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_UsageDecision_Error","LinkTa | 05BA278F-2EAB-4E96-A4EC-3662CAD9C363 |  | 2026-02-20 17:27:03.933000 |  |  | 2026-02-20 17:25:55.410000 | 1601220 | f593a96f-8e46-43c8-8ad6-8d09404e1827 | A6D8CCF1-63BA-4DB7-B5A9-33FB4DB3965B | 40002997305 | Body: {     "InspLot": "40002997305",     "UsgDecCode": "01" } |  |  Http URL: https://jsis-cpi-account-bcp9lrkq.it-cpi012-rt.cfapps.ap21.hana.ondem | PopUp | {"LvId": "69C677BD-7B34-49FB-B6D6-C991C142019E","RecordId" : "05BA278F-2EAB-4E96 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"FBAACB05-2EE3-454F-95 |