# XStudio_Xbatch.dbo.XStudio_List_XMES_SAP_API_GoodsMovement_Error_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| Edit | varchar | NO |
| ID | varchar | NO |
| Name | varchar | YES |
| EntryDateTime | datetime | YES |
| ReportDate | date | YES |
| IsProcessed | bit | YES |
| TransactionID | varchar | YES |
| RecordID | varchar | YES |
| ManufacturingOrder | varchar | YES |
| MovementType | int | YES |
| Type | varchar | YES |
| Batch | varchar | YES |
| Material | varchar | YES |
| Body | varchar | YES |
| ErrorMessage | varchar | YES |
| Status | varchar | YES |
| Delete | varchar | NO |
| Details | varchar | NO |

## Sample rows (top 5, real live data)

| Edit | ID | Name | EntryDateTime | ReportDate | IsProcessed | TransactionID | RecordID | ManufacturingOrder | MovementType | Type | Batch | Material | Body | ErrorMessage | Status | Delete | Details |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_GoodsMovement_Error","LinkTa | 72D26D6C-DB28-4FDA-B40D-C689221F0699 |  | 2026-02-16 21:36:26.347000 |  |  | 67f00fc1-6baf-46b7-b99a-f9428b66df12 | D1A4DFDF-3EB1-43A0-8362-993834700D0F | 140000000240 | 531 | Reversal |  | SCALE_CCM | Body:{ "Material": "SCALE_CCM", "Plant": "7502", "StorageLocation": "", "Batch": |  Http URL: https://jsis-cpi-account-bcp9lrkq.it-cpi012-rt.cfapps.ap21.hana.ondem | Completed | {"LvId": "FBAACB05-2EE3-454F-9568-8EB285BA36B6","RecordId" : "72D26D6C-DB28-4FDA | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"FBAACB05-2EE3-454F-95 |
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_GoodsMovement_Error","LinkTa | 732317F7-3FEE-4D98-ADA7-031AA8463A75 |  | 2026-03-17 00:14:09.950000 |  |  | 4ecdbe01-fd00-4379-be29-4b6a07e7eef1 | FE2105C8-0147-486C-8414-BF3612933AB6 | 120000149402 | 101 | Reversal | 1601823 | B500BLMNHC_GLS |  |  Http URL: https://jsis-cpi-production-w76gw8lc.it-cpi012-rt.cfapps.ap21.hana.on | Completed | {"LvId": "FBAACB05-2EE3-454F-9568-8EB285BA36B6","RecordId" : "732317F7-3FEE-4D98 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"FBAACB05-2EE3-454F-95 |
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_GoodsMovement_Error","LinkTa | 73449EB6-6357-4984-B10D-65A39C0828A3 |  | 2026-05-12 11:49:52.883000 |  |  | 76b0b7f7-36f0-4500-8e78-cbe562c9c4d8 | 74854F8E-556C-4B60-A1F6-8B5AC7CA5535 | 140000000265 | 101 | Production | 1602930_12 | BL_CRSRM_150X150 | Body:{ "Material": "BL_CRSRM_150X150", "Plant": "7502", "StorageLocation": "2103 |  Http URL: https://jsis-cpi-production-w76gw8lc.it-cpi012-rt.cfapps.ap21.hana.on | Completed | {"LvId": "FBAACB05-2EE3-454F-9568-8EB285BA36B6","RecordId" : "73449EB6-6357-4984 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"FBAACB05-2EE3-454F-95 |
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_GoodsMovement_Error","LinkTa | 739FBEB4-9CE5-4F65-9A9B-617BDEAE3D05 |  | 2026-06-16 23:32:32.900000 |  |  | 18e5a827-644e-4328-a900-fa7f70562bcf | A8763815-2FF2-4AF9-A4B3-83207E467F4D |  | 101 | Production | 1603575 |  | Body:{ "Material": "", "Plant": "", "StorageLocation": "", "Batch": "1603575", " |  Http URL: https://jsis-cpi-production-w76gw8lc.it-cpi012-rt.cfapps.ap21.hana.on | Completed | {"LvId": "FBAACB05-2EE3-454F-9568-8EB285BA36B6","RecordId" : "739FBEB4-9CE5-4F65 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"FBAACB05-2EE3-454F-95 |
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_GoodsMovement_Error","LinkTa | 73A74457-1824-4E73-8A70-6D396264FF92 |  | 2026-02-04 05:36:51.370000 |  |  | 951b2fc7-c3be-4c39-bd0f-2af05eb8ba6c | 9085DC2A-CA0C-478C-95FC-6F98B147B5CA | 140000000227 | 101 | Production | 1600787_12 | BL_3SP/P_150X150 | Body:{ "Material": "BL_3SP/P_150X150", "Plant": "7502", "StorageLocation": "2103 |  Http URL: https://jsis-cpi-account-bcp9lrkq.it-cpi012-rt.cfapps.ap21.hana.ondem | Completed | {"LvId": "FBAACB05-2EE3-454F-9568-8EB285BA36B6","RecordId" : "73A74457-1824-4E73 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"FBAACB05-2EE3-454F-95 |