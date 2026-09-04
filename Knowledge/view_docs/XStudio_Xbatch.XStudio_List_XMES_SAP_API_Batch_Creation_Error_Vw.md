# XStudio_Xbatch.dbo.XStudio_List_XMES_SAP_API_Batch_Creation_Error_Vw

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
| CreatedOn | datetime | YES |
| BatchNo | varchar | YES |
| Body | varchar | YES |
| SuccessMessage | varchar | YES |
| ErrorMessage | varchar | YES |
| Status | varchar | YES |
| Delete | varchar | NO |
| Details | varchar | NO |

## Sample rows (top 5, real live data)

| Edit | ID | Name | EntryDateTime | ReportDate | IsProcessed | TransactionID | RecordID | CreatedOn | BatchNo | Body | SuccessMessage | ErrorMessage | Status | Delete | Details |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_Batch_Creation_Error","LinkT | 0019BFFC-A821-437B-80A4-082D29EC9B7F |  | 2026-04-09 09:04:08.723000 |  |  | c683aced-9b35-4f9d-aa40-b9f1cdad60c9 | EE79E74E-7641-45FE-A5F5-048ECAACB549 | 2026-04-09 09:04:08.723000 | 1602294_12 | Body: {     "Material": "",     "BatchIdentifyingPlant": "",     "Batch": "16022 |  |  Http URL: https://jsis-cpi-production-w76gw8lc.it-cpi012-rt.cfapps.ap21.hana.on | PopUp | {"LvId": "FFE26170-2842-4FF8-BE51-23D4C7734D78","RecordId" : "0019BFFC-A821-437B | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"FBAACB05-2EE3-454F-95 |
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_Batch_Creation_Error","LinkT | 01CD335A-3366-44F8-9DEE-FCF41BC40938 |  | 2026-03-19 16:24:19.603000 |  |  | 51d288ed-ac9e-49b4-abb5-78f549668006 | BD6EEEE5-C5DA-4D6A-B0A4-B714C43C20B7 | 2026-03-19 16:24:19.603000 | 1601889_06 | Body: {     "Material": "BL_B500BLMNHC_150X150",     "BatchIdentifyingPlant": "" |  |  Http URL: https://jsis-cpi-production-w76gw8lc.it-cpi012-rt.cfapps.ap21.hana.on | PopUp | {"LvId": "FFE26170-2842-4FF8-BE51-23D4C7734D78","RecordId" : "01CD335A-3366-44F8 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"FBAACB05-2EE3-454F-95 |
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_Batch_Creation_Error","LinkT | 01F8E7E1-CC83-4127-A9DA-9468808E4502 |  | 2026-02-05 12:19:50.147000 |  |  | 84ba56c8-2e81-4f56-8549-9fa03e9762c8 | 627819F4-E5C8-4AC5-BFA5-D79C37FDBB30 | 2026-02-05 12:19:50.147000 | 1600820_12 | Body: {     "Material": "BL_3SP/P_150X150",     "BatchIdentifyingPlant": "",     |  |  Http URL: https://jsis-cpi-account-bcp9lrkq.it-cpi012-rt.cfapps.ap21.hana.ondem | PopUp | {"LvId": "FFE26170-2842-4FF8-BE51-23D4C7734D78","RecordId" : "01F8E7E1-CC83-4127 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"FBAACB05-2EE3-454F-95 |
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_Batch_Creation_Error","LinkT | 02F9C535-3EF1-4E43-BF22-55047667C2D7 |  | 2026-02-03 10:27:05.297000 |  |  | b2016477-b910-455b-a1d1-705c2f747512 | E8F1F061-7AFE-463E-B524-1129EABBE2E5 | 2026-02-03 10:27:05.297000 | 1600728_12 | Body: {     "Material": "BL_3SP/P_150X150",     "BatchIdentifyingPlant": "",     |  |  Http URL: https://jsis-cpi-account-bcp9lrkq.it-cpi012-rt.cfapps.ap21.hana.ondem | PopUp | {"LvId": "FFE26170-2842-4FF8-BE51-23D4C7734D78","RecordId" : "02F9C535-3EF1-4E43 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"FBAACB05-2EE3-454F-95 |
| {"Link": "XBatch/ControlRoom/Edit_Page_XMES_SAP_API_Batch_Creation_Error","LinkT | 0389BF56-0BEB-4AC9-A94E-BD87F6D3B3B6 |  | 2026-05-15 08:32:19.780000 |  |  | ac975934-f2eb-4496-bf51-519e857f2658 | 60C05F9D-1D18-4467-8AFB-CF62892508A0 | 2026-05-15 08:32:19.780000 | 1602978_12 | Body: {     "Material": "BL_3SP/P_150X150",     "BatchIdentifyingPlant": "",     |  |  Http URL: https://jsis-cpi-production-w76gw8lc.it-cpi012-rt.cfapps.ap21.hana.on | PopUp | {"LvId": "FFE26170-2842-4FF8-BE51-23D4C7734D78","RecordId" : "0389BF56-0BEB-4AC9 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"FBAACB05-2EE3-454F-95 |