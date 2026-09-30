---
type: screen
title: "List_SMS_Production_Summary_Duplicate_MobileView"
built: "2026-09-24T11:36:36"
---

# List_SMS_Production_Summary_Duplicate_MobileView

XStudio screen 'List_SMS_Production_Summary_Duplicate_MobileView' (SMS Production Summary Duplicate MobileView; page None, list view List_SMS_Production_Summary_Duplicate_MobileView).
Shows rows of XStudio_List_SMS_Production_Summary_Duplicate_MobileView_Vw.
Filter: only rows where type!='0'
and 
CAST(ReportDate AS DATE) = CAST(DATEADD(DAY, -1, GETDATE()) AS DATE);
