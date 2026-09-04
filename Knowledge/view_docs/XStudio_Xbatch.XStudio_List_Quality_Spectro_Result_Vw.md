# XStudio_Xbatch.dbo.XStudio_List_Quality_Spectro_Result_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| SampleName | varchar | YES |
| Edit | varchar | NO |
| MethodName | varchar | YES |
| OperatorName | varchar | YES |
| ID | varchar | NO |
| HeatNo | varchar | YES |
| SampleType | varchar | YES |
| LineName | varchar | YES |
| ReplicateNo | int | YES |
| Element | varchar | YES |
| ResultType | varchar | YES |
| StatType | varchar | YES |
| ResultValue | decimal | YES |
| Unit | varchar | YES |
| Status | varchar | YES |
| Delete | varchar | NO |
| MinLimit | decimal | YES |
| Details | varchar | NO |
| MaxLimit | decimal | YES |
| SampleID | varchar | YES |
| Sample_XMLCreatedAt | datetime | YES |

## Sample rows (top 5, real live data)

| SampleName | Edit | MethodName | OperatorName | ID | HeatNo | SampleType | LineName | ReplicateNo | Element | ResultType | StatType | ResultValue | Unit | Status | Delete | MinLimit | Details | MaxLimit | SampleID | Sample_XMLCreatedAt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1602371 L3 SK | {"Link": "XBatch/ControlRoom/Edit_Page_Quality_Spectro_Result","LinkTarget": "nu | Fe-10_3SP/P | SK | 8FBD64AA-8E78-436A-8337-7EE5290F1216 | 1602371 | L3 | W | 1 | W | Conc | Reported | 0.0005 | % |  | {"LvId": "74F0116D-4EA4-4FAD-ABEB-1BC7AB22087A","RecordId" : "8FBD64AA-8E78-436A |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"74F0116D-4EA4-4FAD-AB |  | 3E6BBF12-B766-4B5A-AB3A-FA735BDCBE7D | 2026-04-12 17:45:25 |
| 1600934 TS SK | {"Link": "XBatch/ControlRoom/Edit_Page_Quality_Spectro_Result","LinkTarget": "nu | Fe-10_3SP/P | SK | 6FB8242C-BAA3-44C2-87E8-C4148AF435DB | 1600934 | TS | N | 0 | N | Conc | Reported | 0.0073 | % |  | {"LvId": "74F0116D-4EA4-4FAD-ABEB-1BC7AB22087A","RecordId" : "6FB8242C-BAA3-44C2 |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"74F0116D-4EA4-4FAD-AB |  | EA9E39AA-8913-4386-8908-8C0DE2DC7B5B | 2026-02-09 19:25:13 |
| 1603305 L1 SK | {"Link": "XBatch/ControlRoom/Edit_Page_Quality_Spectro_Result","LinkTarget": "nu | Fe-10_3SP/P | SK | 6FB891DF-0A01-49BD-96A3-1B8A1557044B | 1603305 | L1 | Si | -1 | Si | Conc | Mean | 0.1258 | % |  | {"LvId": "74F0116D-4EA4-4FAD-ABEB-1BC7AB22087A","RecordId" : "6FB891DF-0A01-49BD |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"74F0116D-4EA4-4FAD-AB |  | 4DA43F96-C71E-42CE-B00F-ADF7201A3110 | 2026-06-01 19:20:01 |
| 1603200 L2 DK | {"Link": "XBatch/ControlRoom/Edit_Page_Quality_Spectro_Result","LinkTarget": "nu | Fe-10_3SP/P | DK | 2CC99A51-A956-4FDF-BAE6-1522CE72C202 | 1603200 | L2 | Co | -1 | Co | Conc | Mean | 0.0050 | % |  | {"LvId": "74F0116D-4EA4-4FAD-ABEB-1BC7AB22087A","RecordId" : "2CC99A51-A956-4FDF |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"74F0116D-4EA4-4FAD-AB |  | F95EF1F9-5D50-427E-A272-5DC3DD00A8A3 | 2026-05-27 06:12:32 |
| 1603594 L3 SK | {"Link": "XBatch/ControlRoom/Edit_Page_Quality_Spectro_Result","LinkTarget": "nu | Fe-10_3SP/P | SK | 2CC9D9F7-B5DD-4AB4-A138-B962F0997C91 | 1603594 | L3 | Sn | 1 | Sn | Conc | Reported | 0.0042 | % |  | {"LvId": "74F0116D-4EA4-4FAD-ABEB-1BC7AB22087A","RecordId" : "2CC9D9F7-B5DD-4AB4 |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"74F0116D-4EA4-4FAD-AB |  | 5D23C241-7A24-434E-A06E-C9B858A569B3 | 2026-06-17 19:51:59 |