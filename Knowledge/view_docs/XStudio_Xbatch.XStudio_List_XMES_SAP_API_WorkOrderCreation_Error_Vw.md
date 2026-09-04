# XStudio_Xbatch.dbo.XStudio_List_XMES_SAP_API_WorkOrderCreation_Error_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| Edit | varchar | NO |
| ID | varchar | NO |
| Name | varchar | YES |
| EntryDateTime | datetime | YES |
| ReportDate | date | YES |
| TransactionID | varchar | YES |
| IsProcessed | bit | YES |
| RecordID | varchar | YES |
| CreatedOn | datetime | YES |
| TotalQuantity | decimal | YES |
| Material | varchar | YES |
| CustomerName | varchar | YES |
| WorkOrderType | varchar | YES |
| Body | varchar | YES |
| Status | varchar | YES |
| SuccessMessage | varchar | YES |
| Delete | varchar | NO |
| Details | varchar | NO |
| ErrorMessage | varchar | YES |

## Sample rows (top 5, real live data)

| Edit | ID | Name | EntryDateTime | ReportDate | TransactionID | IsProcessed | RecordID | CreatedOn | TotalQuantity | Material | CustomerName | WorkOrderType | Body | Status | SuccessMessage | Delete | Details | ErrorMessage |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_WorkOrderCreation_Error","Li | 16092DC9-3FC4-4F08-9B34-0AEBD2BF4C3A |  | 2026-02-10 17:38:46.883000 |  | 56fb28d3-6288-4621-a689-789395a58fc0 |  | 016C17D6-441C-4A4B-B412-57F6C75D5593 | 2026-02-10 11:50:14.033000 | 60000.00 | BL_SAE1018_150X150 |  | SS02 | Body: {"ManufacturingOrderType":"SS02","Material":"BL_SAE1018_150X150","Producti | PopUp |  | {"LvId": "9762B9DE-428E-477F-A4C8-C6B13FEA2397","RecordId" : "16092DC9-3FC4-4F08 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"9762B9DE-428E-477F-A4 |  Http URL: https://jsis-cpi-account-bcp9lrkq.it-cpi012-rt.cfapps.ap21.hana.ondem |
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_WorkOrderCreation_Error","Li | 21CBB236-C2AE-4053-85D3-59E9052D36DD |  | 2026-03-05 14:31:40.003000 |  | 9791ec57-b8b6-4dc0-a76f-a8db67717b39 |  | 008C8ABB-8E4D-4D4B-AEAE-130DD8C7DD47 | 2026-03-05 14:25:41.253000 | 500.00 | BL_3SP/P_140X140 |  | SS02 | Body: {"ManufacturingOrderType":"SS02","Material":"BL_3SP/P_140X140","Production | PopUp |  | {"LvId": "9762B9DE-428E-477F-A4C8-C6B13FEA2397","RecordId" : "21CBB236-C2AE-4053 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"9762B9DE-428E-477F-A4 |  Http URL: https://jsis-cpi-account-bcp9lrkq.it-cpi012-rt.cfapps.ap21.hana.ondem |
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_WorkOrderCreation_Error","Li | 302D96A2-5973-49AC-B1F2-C538D68FEB8C |  | 2026-04-23 15:26:33.070000 |  | 8dfd3d51-0e56-4f61-8a1b-4fc1612c6f0a |  |  |  |  |  |  |  | Body: {     "ManufacturingOrderType": "",     "Material": "",     "ProductionPla | PopUp |  | {"LvId": "9762B9DE-428E-477F-A4C8-C6B13FEA2397","RecordId" : "302D96A2-5973-49AC | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"9762B9DE-428E-477F-A4 |  Property 'MfgOrderPlannedStartDate' at offset '117' has invalid value '' |
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_WorkOrderCreation_Error","Li | 322FF78E-85F8-4491-AE2A-BC009821B47A |  | 2026-02-14 10:33:43.843000 |  | 65a62c54-d795-4f60-a8bf-8381232a5c0d |  |  |  |  |  |  |  | Body: {"ManufacturingOrderType":"","Material":"","ProductionPlant":"","MfgOrderP | PopUp |  | {"LvId": "9762B9DE-428E-477F-A4C8-C6B13FEA2397","RecordId" : "322FF78E-85F8-4491 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"9762B9DE-428E-477F-A4 |  Property 'MfgOrderPlannedStartDate' at offset '93' has invalid value '' |
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_WorkOrderCreation_Error","Li | 3D88EA1F-261A-4882-8070-E8389539DF92 |  | 2026-07-31 09:48:07.350000 |  | eab53393-0922-4ebf-8bf4-5101841d32a4 |  |  |  |  |  |  |  | Body: {     "ManufacturingOrderType": "",     "Material": "",     "ProductionPla | PopUp |  | {"LvId": "9762B9DE-428E-477F-A4C8-C6B13FEA2397","RecordId" : "3D88EA1F-261A-4882 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"9762B9DE-428E-477F-A4 |  Property 'MfgOrderPlannedStartDate' at offset '121' has invalid value '' |