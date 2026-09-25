// Tickets are Complaint_Mst_Tbl rows the L2 pipeline owns. L1 creates them, reads L2's published replies,
// records the requester's answers/ratings in L1_Ticket_Event_Tbl, and never drives the L2 lifecycle itself.
using System.Text.Json;
using System.Text.RegularExpressions;

namespace L1Api;

public static class Tickets
{
    public const string StandardPriority = "EEF8F1D9-180E-49E4-95C3-3F5CB0408028";

    public static string Select(int top) => $"""
        SELECT TOP {top} c.ID, c.TicketNo, c.BriefDetails, c.Description, c.Status, c.AskStatus, c.CreatedOn, c.ModifiedOn,
               c.ReplyRemarks, c.Source, c.EmailID, c.FirstLastName, c.CreatedBy, c.ExtractedEntitiesJson,
               a.Name AS Area, k.Name AS Type, p.priority AS Priority,
               -- XStudio's insert trigger rewrites Source, so the chat link is the reliable channel marker.
               CASE WHEN EXISTS (SELECT 1 FROM dbo.L1_Chat_Session_Tbl l WHERE l.TicketNo = c.TicketNo) THEN 'Helpdesk chat' ELSE 'Other' END AS Channel,
               r.ResponseType, r.ReplyText, r.CompletedOn, run.ProcessStatus AS RunStatus,
               (SELECT MIN(CompletedOn) FROM dbo.Hermes_L2_Response_Trn_Tbl f
                 WHERE f.TicketID = c.ID AND f.IsDeleted = 0 AND f.ProcessStatus = 'COMPLETED' AND f.ReplyText IS NOT NULL) AS FirstReplyOn,
               (SELECT TOP 1 Rating FROM dbo.L1_Ticket_Event_Tbl e WHERE e.TicketID = CONVERT(varchar(36), c.ID) AND e.Kind = 'rating'
                 ORDER BY e.ID DESC) AS Rating
        FROM dbo.Complaint_Mst_Tbl c
        LEFT JOIN dbo.Area_Mst_Tbl a ON a.ID = c.AreaID
        LEFT JOIN dbo.ComplaintType_Mst_Tbl k ON k.ID = c.ComplaintTypeID
        LEFT JOIN dbo.priority_mst p ON p.ID = c.Priority
        OUTER APPLY (SELECT TOP 1 ResponseType, ReplyText, CompletedOn FROM dbo.Hermes_L2_Response_Trn_Tbl x
                     WHERE x.TicketID = c.ID AND x.IsDeleted = 0 AND x.ProcessStatus = 'COMPLETED' AND x.ReplyText IS NOT NULL
                     ORDER BY x.CompletedOn DESC) r
        OUTER APPLY (SELECT TOP 1 ProcessStatus FROM dbo.Hermes_L2_Response_Trn_Tbl y
                     WHERE y.TicketID = c.ID AND y.IsDeleted = 0 ORDER BY y.CreatedOn DESC) run
        WHERE ISNULL(c.IsDeleted, 0) = 0
        """;

    // What a requester reads as the ticket's state; Helpdesk + L2 rows are the only inputs.
    public static Dictionary<string, object?> WithState(Dictionary<string, object?> t)
    {
        var (label, tone) = (t["Status"]?.ToString(), t["AskStatus"]?.ToString(), t["ResponseType"]?.ToString()) switch
        {
            ("Closed", _, _) => ("Resolved", "done"),
            (_, "Ask", _) => ("Waiting for your reply", "attention"),
            (_, _, "RESOLUTION") => ("Resolved", "done"),
            (_, _, "NEEDS_HUMAN_ACTION") => ("With the support team", "progress"),
            (_, _, "L3_ESCALATION") => ("Escalated to specialist", "progress"),
            (_, _, "UPDATE") => ("Update posted", "progress"),
            _ => ("Being investigated", "pending"),
        };
        t["StateLabel"] = label;
        t["StateTone"] = tone;
        return t;
    }

    public static async Task<List<Dictionary<string, object?>>> ForUser(string? email, int top = 50) =>
        (await Db.H(Select(top) + " AND c.EmailID = @e ORDER BY c.CreatedOn DESC", ("@e", email ?? ""))).Select(WithState).ToList();

    public static async Task<Dictionary<string, object?>?> One(string id) =>
        (await Db.H(Select(1) + " AND (CONVERT(varchar(36), c.ID) = @id OR c.TicketNo = @id)", ("@id", id))).Select(WithState).FirstOrDefault();

    // Everything that happened on the ticket, oldest first: the report, L2 publications, the requester's own events.
    public static async Task<List<Dictionary<string, object?>>> Timeline(Dictionary<string, object?> t)
    {
        var id = t["ID"]!.ToString()!;
        var items = new List<Dictionary<string, object?>>
        {
            new() { ["Kind"] = "created", ["Actor"] = "requester", ["Text"] = t["Description"] ?? t["BriefDetails"], ["At"] = t["CreatedOn"] },
        };
        foreach (var r in await Db.H("""
                     SELECT ID, ResponseType, ReplyText, CompletedOn FROM dbo.Hermes_L2_Response_Trn_Tbl
                     WHERE TicketID = @id AND IsDeleted = 0 AND ProcessStatus = 'COMPLETED' AND ReplyText IS NOT NULL
                     """, ("@id", id)))
            items.Add(new() { ["Kind"] = "reply", ["Actor"] = "support", ["ResponseType"] = r["ResponseType"], ["Text"] = r["ReplyText"], ["At"] = r["CompletedOn"] });
        foreach (var e in await Db.H("SELECT Kind, Content, Rating, CreatedOn FROM dbo.L1_Ticket_Event_Tbl WHERE TicketID = @id", ("@id", id)))
            items.Add(new() { ["Kind"] = e["Kind"], ["Actor"] = "requester", ["Text"] = e["Content"], ["Rating"] = e["Rating"], ["At"] = e["CreatedOn"] });
        return items.OrderBy(i => i["At"] as DateTime? ?? DateTime.MinValue).ToList();
    }

    // Deterministic ticket: requester fields, what they wrote, transcript, identifiers in it.
    // Area and complaint type are Jev's choices over the Helpdesk's own lists.
    public static async Task<string> Create(Dictionary<string, object?> user, List<string> userLines, string transcript, string? priorityId = null)
    {
        var areas = await Db.H("SELECT ID, Name FROM dbo.Area_Mst_Tbl WHERE ISNULL(IsDeleted,0) = 0");
        var types = await Db.H("SELECT ID, Name FROM dbo.ComplaintType_Mst_Tbl WHERE ISNULL(IsDeleted,0) = 0");
        var answers = await Jev.Ask(new { conversation = transcript }, new
        {
            area = new { type = "choice", criteria = areas.ToDictionary(a => a["ID"]!.ToString()!, a => a["Name"]!.ToString()!),
                         instructions = "Which plant area is this problem about? (Common if unclear)" },
            kind = new { type = "choice", criteria = types.ToDictionary(k => k["ID"]!.ToString()!, k => k["Name"]!.ToString()!),
                         instructions = "What kind of request is this?" },
        });
        var area = answers?["area"]?["choice"]?.ToString() ?? areas.First(a => a["Name"]!.ToString() == "Common")["ID"]!.ToString();
        var kind = answers?["kind"]?["choice"]?.ToString() ?? types.First()["ID"]!.ToString();
        var description = string.Join("\n", userLines);
        var ids = Regex.Matches(description, @"(?<![\d.])(\d{7}_S\d+_\d+|\d{7,12})(?!\d)").Select(m => m.Value).Distinct().ToList();
        // Number and insert in one statement so two chats cannot take the same number.
        var row = await Db.H("""
            DECLARE @no varchar(100) = 'Ticket_' + CONVERT(varchar(20), (SELECT ISNULL(MAX(TRY_CAST(REPLACE(TicketNo, 'Ticket_', '') AS int)), 0) + 1
                FROM dbo.Complaint_Mst_Tbl WITH (UPDLOCK, HOLDLOCK) WHERE TicketNo LIKE 'Ticket[_]%'));
            INSERT INTO dbo.Complaint_Mst_Tbl (ID, AreaID, CreatedBy, CreatedOn, ModifiedOn, IsDeleted, IsSystem, Source, ComplaintTypeID,
                Description, BriefDetails, Status, TicketNo, Priority, FirstLastName, ContactNo, EmailID, messages, AskStatus,
                SourceSystem, ConversationSummary, ExtractedEntitiesJson)
            VALUES (NEWID(), @area, @user, GETDATE(), GETDATE(), 0, 0, 'L1-Chat', @kind, @desc, @brief, 'Enter', @no,
                @prio, @name, @phone, @email, 'Enter', 'Enter', 'Xbatch', @summary, @entities);
            SELECT @no AS TicketNo;
            """, ("@area", area), ("@user", user["ID"]), ("@kind", kind), ("@desc", description), ("@brief", Db.Trim(userLines.FirstOrDefault(), 480)),
            ("@prio", priorityId ?? StandardPriority), ("@name", user["FullName"] ?? user["Name"]), ("@phone", user["ContactNo"]),
            ("@email", user["EmailID"]), ("@summary", Db.Trim(transcript, 4000)), ("@entities", JsonSerializer.Serialize(new { identifiers = ids })));
        return row.First()["TicketNo"]!.ToString()!;
    }
}
