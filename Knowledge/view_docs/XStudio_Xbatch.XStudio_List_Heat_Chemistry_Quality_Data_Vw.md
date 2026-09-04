# XStudio_Xbatch.dbo.XStudio_List_Heat_Chemistry_Quality_Data_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| EntryDate | datetime | YES |
| HeatNo | varchar | YES |
| Edit | varchar | NO |
| SampleType | varchar | YES |
| ID | varchar | NO |
| Action | varchar | YES |
| Status | varchar | YES |
| SteelGrade | varchar | YES |
| SrNo | int | YES |
| ReceivedTime | datetime | YES |
| ReportedTime | datetime | YES |
| C | decimal | YES |
| Grade | varchar | YES |
| Section | varchar | YES |
| Mn | decimal | YES |
| Si | decimal | YES |
| Shift | varchar | YES |
| S | decimal | YES |
| P | decimal | YES |
| Cr | decimal | YES |
| Mo | decimal | YES |
| V | decimal | YES |
| Al | decimal | YES |
| Sn | decimal | YES |
| Pb | decimal | YES |
| Co | decimal | YES |
| N2PPM | decimal | YES |
| Cu | decimal | YES |
| Ce | decimal | YES |
| As | decimal | YES |
| B | decimal | YES |
| Ca | decimal | YES |
| Nb | decimal | YES |
| W | decimal | YES |
| Ceq | decimal | YES |
| MnPerSi | decimal | YES |
| MnPerS | decimal | YES |
| Ag | decimal | YES |
| Ni | decimal | YES |
| TI | decimal | YES |
| Bi | decimal | YES |
| Fe | decimal | YES |
| Ta | decimal | YES |
| Sb | decimal | YES |
| Zr | decimal | YES |
| Chemist | varchar | YES |
| ModifyOn | datetime | YES |
| ModifyBy | varchar | YES |
| Remarks | varchar | YES |
| Details | varchar | NO |
| ModifiedBy | varchar | YES |
| Dateyyyymmdd | varchar | YES |
| Delete | varchar | NO |
| GradeColorCode | varchar | YES |
| InspectionLot | varchar | YES |

## Sample rows (top 5, real live data)

| EntryDate | HeatNo | Edit | SampleType | ID | Action | Status | SteelGrade | SrNo | ReceivedTime | ReportedTime | C | Grade | Section | Mn | Si | Shift | S | P | Cr | Mo | V | Al | Sn | Pb | Co | N2PPM | Cu | Ce | As | B | Ca | Nb | W | Ceq | MnPerSi | MnPerS | Ag | Ni | TI | Bi | Fe | Ta | Sb | Zr | Chemist | ModifyOn | ModifyBy | Remarks | Details | ModifiedBy | Dateyyyymmdd | Delete | GradeColorCode | InspectionLot |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-03-17 08:11:00 | 1601839 | {"Link": "XBatch/ControlRoom/Edit_Page_Heat_Chemistry_Quality_Data","LinkTarget" | TS | F9768A9F-0769-4B83-8B13-B130CB9C1CDF | Released | Released | HHMNB500B |  | 2026-03-17 08:11:06 | 2026-03-17 08:11:10 | 0.2150 |  | 150 | 0.7200 | 0.1800 |  | 0.0200 | 0.0090 | 0.0110 | 0.0050 | 0.0030 | 0.0020 | 0.0060 |  |  | 60.0000 | 0.0430 |  |  | 0.0003 | 0.0001 |  |  | 0.3446 | 4.0000 | 36.0000 | 0.0001 | 0.0290 | 0.0010 | 0.0011 | 98.5947 | 0.0022 | 0.0155 | 0.1203 | DK | 2026-03-17 12:27:16.977000 | Devraj Yadav |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"17362EF6-83CB-4D2C-86 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-03-17 | {"LvId": "17362EF6-83CB-4D2C-8680-76BEE4AA8940","RecordId" : "F9768A9F-0769-4B83 |  | 40003913953 |
| 2026-03-29 17:00:00 | 1602074 | {"Link": "XBatch/ControlRoom/Edit_Page_Heat_Chemistry_Quality_Data","LinkTarget" | TD | F97DC665-FB7E-48E1-A85F-AA6F10D6DA7E | Released | Released | B500BLMNHC |  | 2026-03-29 17:00:38 | 2026-03-29 17:00:39 | 0.1822 |  |  | 0.5188 | 0.1800 |  | 0.0156 | 0.0153 | 0.0223 | 0.0064 | 0.0043 | 0.0027 | 0.0046 | 0.0002 | 0.0059 | 56.0000 | 0.0358 | 0.0006 | 0.0033 | 0.0001 | 0.0007 | 0.0006 | -0.0021 | 0.2792 | 2.7997 | 33.3155 | 0.0001 | 0.0231 | 0.0007 | 0.0015 | 98.9077 | 0.0038 | 0.0148 | 0.0395 | Y | 2026-03-30 02:01:28 | Devraj Yadav |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"17362EF6-83CB-4D2C-86 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-03-29 | {"LvId": "17362EF6-83CB-4D2C-8680-76BEE4AA8940","RecordId" : "F97DC665-FB7E-48E1 |  |  |
| 2026-04-11 04:12:00 | 1602336 | {"Link": "XBatch/ControlRoom/Edit_Page_Heat_Chemistry_Quality_Data","LinkTarget" | TD | F97EF8EC-69EF-442E-A957-C3B313D3F6DE | Released | Released | SAE1008 |  | 2026-04-11 04:12:11 | 2026-04-11 04:12:27 | 0.0770 |  | 150X150 | 0.4000 | 0.1250 |  | 0.0120 | 0.0090 | 0.0195 | 0.0106 | 0.0026 | 0.0029 | 0.0048 | 0.0006 | 0.0063 | 60.0000 | 0.0243 | 0.0016 | 0.0034 | 0.0001 | 0.0003 | 0.0025 |  | 0.1551 | 3.2314 | 34.8874 | 0.0001 | 0.0393 | 0.0011 |  | 98.9615 | 0.0022 | 0.0129 | 0.2686 | SANTOSH | 2026-04-11 22:54:42.870000 | Devraj Yadav |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"17362EF6-83CB-4D2C-86 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-04-11 | {"LvId": "17362EF6-83CB-4D2C-8680-76BEE4AA8940","RecordId" : "F97EF8EC-69EF-442E |  | 40004001339 |
| 2026-03-10 06:07:00 | 1601660 | {"Link": "XBatch/ControlRoom/Edit_Page_Heat_Chemistry_Quality_Data","LinkTarget" | TS | F9821836-9AB7-440E-B7C0-556B66D2BED5 | Released | Released | B500BLMNHC |  | 2026-03-10 05:59:51 | 2026-03-10 06:07:24 | 0.2287 |  | 150X150 | 0.5096 | 0.1278 |  | 0.0200 | 0.0097 | 0.0120 | 0.0058 | 0.0036 | 0.0017 | 0.0054 | 0.0006 | 0.0063 | 56.0000 | 0.0386 | 0.0008 | 0.0034 | 0.0003 |  | 0.0023 | -0.0021 | 0.3221 | 3.9868 | 24.4189 |  | 0.0242 | 0.0008 |  | 98.8148 | 0.0045 | 0.0154 | 0.1662 | SK | 2026-03-10 10:57:27 | Devraj Yadav |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"17362EF6-83CB-4D2C-86 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-03-10 | {"LvId": "17362EF6-83CB-4D2C-8680-76BEE4AA8940","RecordId" : "F9821836-9AB7-440E |  |  |
| 2026-05-25 14:52:00 | 1603167 | {"Link": "XBatch/ControlRoom/Edit_Page_Heat_Chemistry_Quality_Data","LinkTarget" | TD | F98733D8-27C2-4703-A2D0-8D9909F38205 | Released | Released | HHMNB500B |  | 2026-05-25 14:48:22 | 2026-05-25 14:52:22 | 0.2462 |  |  | 0.7044 | 0.1699 |  | 0.0183 | 0.0083 | 0.0162 | 0.0065 | 0.0016 | 0.0017 | 0.0045 | 0.0005 | 0.0053 | 70.0000 | 0.0291 | 0.0004 | 0.0047 | 0.0002 | 0.0001 | 0.0023 |  | 0.3716 | 4.1454 | 38.7173 | 0.0001 | 0.0178 | 0.0010 |  | 98.5872 | 0.0054 | 0.0154 | 0.1565 | SK | 2026-05-25 15:06:26 | Devraj Yadav |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"17362EF6-83CB-4D2C-86 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-05-25 | {"LvId": "17362EF6-83CB-4D2C-8680-76BEE4AA8940","RecordId" : "F98733D8-27C2-4703 |  |  |