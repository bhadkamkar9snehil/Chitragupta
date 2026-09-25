// L2/L3 operations for the helpdesk suite. Everything is read from the tables the L2 runtime already writes
// (runs, trace events, SQL actions, L3 queue, ticket activity) plus the Hermes Kanban board over WSL.
// The only writes are the human L3 desk's own actions: assign, note, resolve.
using System.Diagnostics;
using System.Text.Json;
using System.Text.Json.Nodes;

namespace L1Api;

public static class Ops
{
    const string RunSelect = """
        SELECT TOP {0} r.ID, r.TicketID, c.TicketNo, c.BriefDetails, c.FirstLastName, r.AttemptNo, r.ProcessStatus, r.IsActive,
               r.Route, r.ResponseType, r.ExecutionMode, r.JevReviewDecision, r.JevReviewConfidence, r.JevRiskScore, r.JevModel,
               r.LocalModelState, r.LocalModelPurpose, r.ClaimedOn, r.HeartbeatOn, r.CompletedOn, r.CreatedOn, r.ErrorMessage,
               r.EscalateToL3, r.IsResolved, r.RequiresUserInput,
               (SELECT COUNT(*) FROM dbo.Hermes_L2_SQL_Action_Trn_Tbl a WHERE a.RunID = CONVERT(varchar(36), r.ID)) AS SqlActions,
               (SELECT COUNT(*) FROM dbo.Hermes_Agent_Trace_Trn_Tbl t WHERE t.RunID = CONVERT(varchar(36), r.ID)) AS Events,
               (SELECT COUNT(*) FROM dbo.Hermes_Agent_Trace_Trn_Tbl t WHERE t.RunID = CONVERT(varchar(36), r.ID) AND t.EventType = 'jev_system_one') AS JevCalls,
               DATEDIFF(second, r.ClaimedOn, ISNULL(r.CompletedOn, GETDATE())) AS Seconds
        FROM dbo.Hermes_L2_Response_Trn_Tbl r
        LEFT JOIN dbo.Complaint_Mst_Tbl c ON c.ID = r.TicketID
        WHERE r.IsDeleted = 0
        """;

    public static Task<List<Dictionary<string, object?>>> Runs(string? q, int top = 200) => Db.H(string.Format(RunSelect, top) + """
         AND (@q IS NULL OR c.TicketNo LIKE '%' + @q + '%' OR c.BriefDetails LIKE '%' + @q + '%' OR r.Route LIKE '%' + @q + '%')
         ORDER BY ISNULL(r.HeartbeatOn, r.CreatedOn) DESC
        """, ("@q", string.IsNullOrWhiteSpace(q) ? null : q));

    public static async Task<Dictionary<string, object?>?> Run(string id)
    {
        var run = (await Db.H(string.Format(RunSelect, 1) + " AND CONVERT(varchar(36), r.ID) = @id", ("@id", id))).FirstOrDefault();
        if (run is null) return null;
        var detail = (await Db.H("""
            SELECT ProblemSummary, Findings, RootCause, Resolution, ReplyText, JevTriageJson, JevInvestigationJson, JevReviewJson,
                   JevTraceJson, JevKBCurationJson, ActionsTakenJson
            FROM dbo.Hermes_L2_Response_Trn_Tbl WHERE CONVERT(varchar(36), ID) = @id
            """, ("@id", id))).First();
        foreach (var (k, v) in detail) run[k] = v;
        run["Events"] = await Events(id, null);
        run["Trail"] = await Trail(id);
        run["SqlActionList"] = await Db.H("""
            SELECT ActionNo, ActionType, OperationName, SchemaName, ObjectName, DatabaseName, Purpose, Status, RowsAffected,
                   StartedOn, CompletedOn, LEFT(SqlText, 1500) AS SqlText, ErrorMessage
            FROM dbo.Hermes_L2_SQL_Action_Trn_Tbl WHERE RunID = @id AND IsDeleted = 0 ORDER BY ActionNo
            """, ("@id", id));
        return run;
    }

    // Trace events for a run, oldest first; `since` makes it a cheap live poll.
    public static Task<List<Dictionary<string, object?>>> Events(string runId, DateTime? since) => Db.H("""
        SELECT TOP 600 ID, EventType, ToolName, Name, Model, Provider, Status, DurationMs, EventOn, ErrorMessage,
               LEFT(ArgsJson, 1200) AS ArgsJson, CASE WHEN ToolName = 'WORLD_WALK_TRAIL' THEN NULL ELSE LEFT(ResultJson, 1500) END AS ResultJson
        FROM dbo.Hermes_Agent_Trace_Trn_Tbl
        WHERE RunID = @r AND IsDeleted = 0 AND (@s IS NULL OR EventOn > @s)
          AND EventType NOT IN ('compute_sample', 'lmstudio_sample', 'trace_context')
        ORDER BY EventOn, ID
        """, ("@r", runId), ("@s", since));

    public static async Task<JsonNode?> Trail(string runId)
    {
        var row = (await Db.H("""
            SELECT TOP 1 ResultJson FROM dbo.Hermes_Agent_Trace_Trn_Tbl
            WHERE RunID = @r AND ToolName = 'WORLD_WALK_TRAIL' ORDER BY EventOn DESC
            """, ("@r", runId))).FirstOrDefault();
        try { return row?["ResultJson"] is string s ? JsonNode.Parse(s) : null; } catch { return null; }
    }

    // The run to watch: the active one, else the most recently touched.
    public static async Task<Dictionary<string, object?>?> LiveRun() => (await Db.H(string.Format(RunSelect, 1) +
        " ORDER BY CASE WHEN r.IsActive = 1 THEN 0 ELSE 1 END, ISNULL(r.HeartbeatOn, ISNULL(r.CompletedOn, r.CreatedOn)) DESC")).FirstOrDefault();

    public static async Task<object> Overview()
    {
        var counts = (await Db.H("""
            SELECT
              (SELECT COUNT(*) FROM dbo.Complaint_Mst_Tbl c WHERE ISNULL(c.IsDeleted,0) = 0 AND c.Status <> 'Closed' AND ISNULL(c.AskStatus,'') <> 'Ask'
                 AND NOT EXISTS (SELECT 1 FROM dbo.Hermes_L2_Response_Trn_Tbl r WHERE r.TicketID = c.ID AND r.IsDeleted = 0)) AS NewTickets,
              (SELECT COUNT(*) FROM dbo.Hermes_L2_Response_Trn_Tbl WHERE IsDeleted = 0 AND IsActive = 1) AS ActiveRuns,
              (SELECT COUNT(*) FROM dbo.Complaint_Mst_Tbl WHERE ISNULL(IsDeleted,0) = 0 AND AskStatus = 'Ask') AS WaitingOnRequester,
              (SELECT COUNT(*) FROM dbo.Hermes_L3_Escalation_Trn_Tbl WHERE IsDeleted = 0 AND ISNULL(L3Status,'Open') <> 'Resolved') AS L3Open,
              (SELECT COUNT(*) FROM dbo.Complaint_Mst_Tbl WHERE ISNULL(IsDeleted,0) = 0 AND Status <> 'Closed') AS OpenTickets,
              (SELECT COUNT(*) FROM dbo.Hermes_L2_Response_Trn_Tbl WHERE IsDeleted = 0 AND CompletedOn >= DATEADD(hour, -24, GETDATE())) AS RunsLast24h,
              (SELECT COUNT(*) FROM dbo.L1_Chat_Session_Tbl WHERE CreatedOn >= DATEADD(hour, -24, GETDATE())) AS ChatsLast24h,
              (SELECT MAX(ClaimedOn) FROM dbo.Hermes_L2_Response_Trn_Tbl WHERE IsDeleted = 0) AS LastClaimOn,
              (SELECT COUNT(*) FROM dbo.Hermes_Agent_Trace_Trn_Tbl WHERE EventType = 'jev_system_one' AND EventOn >= DATEADD(hour, -24, GETDATE())) AS JevCallsLast24h,
              (SELECT COUNT(*) FROM dbo.Hermes_Agent_Trace_Trn_Tbl WHERE EventType = 'post_api_request' AND EventOn >= DATEADD(hour, -24, GETDATE())) AS ModelCallsLast24h
            """)).First();
        var outcomes = await Db.H("""
            SELECT ISNULL(ResponseType, 'In progress') AS Label, COUNT(*) AS Count FROM dbo.Hermes_L2_Response_Trn_Tbl
            WHERE IsDeleted = 0 GROUP BY ResponseType ORDER BY COUNT(*) DESC
            """);
        var lm = (await Db.H("""
            SELECT TOP 1 EventOn, ResultJson FROM dbo.Hermes_Agent_Trace_Trn_Tbl WHERE EventType = 'lmstudio_sample' ORDER BY EventOn DESC
            """)).FirstOrDefault();
        return new { counts, outcomes, lmStudio = lm, activity = await Activity(40), live = await LiveRun() };
    }

    // One feed across the suite: L2 runs, L3 changes, ticket activity, L1 conversations.
    public static async Task<List<Dictionary<string, object?>>> Activity(int top) => await Db.H($"""
        SELECT TOP {top} * FROM (
          SELECT r.CompletedOn AS At, 'l2' AS Lane, 'L2 published ' + ISNULL(r.ResponseType, '') AS Title, c.TicketNo, CONVERT(varchar(36), r.ID) AS RunID, c.BriefDetails AS Detail
            FROM dbo.Hermes_L2_Response_Trn_Tbl r JOIN dbo.Complaint_Mst_Tbl c ON c.ID = r.TicketID WHERE r.IsDeleted = 0 AND r.CompletedOn IS NOT NULL
          UNION ALL
          SELECT r.ClaimedOn, 'l2', 'L2 claimed', c.TicketNo, CONVERT(varchar(36), r.ID), c.BriefDetails
            FROM dbo.Hermes_L2_Response_Trn_Tbl r JOIN dbo.Complaint_Mst_Tbl c ON c.ID = r.TicketID WHERE r.IsDeleted = 0 AND r.ClaimedOn IS NOT NULL
          UNION ALL
          SELECT a.CreatedOn, CASE WHEN a.ActorType = 'Human' THEN 'l3' ELSE 'l2' END, a.ActivityType + ISNULL(' by ' + a.ActorName, ''), c.TicketNo, a.RunID, LEFT(a.NoteText, 200)
            FROM dbo.Hermes_Ticket_Activity_Trn_Tbl a JOIN dbo.Complaint_Mst_Tbl c ON CONVERT(varchar(36), c.ID) = a.TicketID WHERE a.IsDeleted = 0
          UNION ALL
          SELECT c.CreatedOn, 'l1', 'Ticket raised', c.TicketNo, NULL, c.BriefDetails FROM dbo.Complaint_Mst_Tbl c WHERE ISNULL(c.IsDeleted,0) = 0
          UNION ALL
          SELECT s.CreatedOn, 'l1', 'Conversation started', s.TicketNo, NULL, s.Title FROM dbo.L1_Chat_Session_Tbl s
        ) x WHERE At IS NOT NULL ORDER BY At DESC
        """);

    public static Task<List<Dictionary<string, object?>>> L3(string? status) => Db.H("""
        SELECT e.ID, e.TicketID, e.TicketNo, e.RunID, e.EscalationCategory, e.L3Status, e.ProblemSummary, e.Findings, e.RootCause,
               e.SuggestedAction, e.ReplyText, e.EscalatedOn, e.AssignedToUserID, e.AssignedOn, e.L3Remarks, e.L3ResolutionSummary,
               e.ResolvedOn, e.ResolvedByUserID, c.BriefDetails, c.FirstLastName, c.EmailID, c.Status AS TicketStatus, a.Name AS Area
        FROM dbo.Hermes_L3_Escalation_Trn_Tbl e
        LEFT JOIN dbo.Complaint_Mst_Tbl c ON CONVERT(varchar(36), c.ID) = CONVERT(varchar(36), e.TicketID)
        LEFT JOIN dbo.Area_Mst_Tbl a ON a.ID = c.AreaID
        WHERE e.IsDeleted = 0 AND (@s IS NULL OR ISNULL(e.L3Status, 'Open') = @s)
        ORDER BY CASE ISNULL(e.L3Status, 'Open') WHEN 'Open' THEN 0 WHEN 'In progress' THEN 1 ELSE 2 END, e.EscalatedOn DESC
        """, ("@s", string.IsNullOrWhiteSpace(status) ? null : status));

    // Human L3 actions. Resolving can close the ticket and leave a requester-visible note; the L2 run history is untouched.
    public static async Task<IResult> L3Act(string id, JsonObject body)
    {
        var row = (await L3(null)).FirstOrDefault(r => r["ID"]?.ToString()?.Equals(id, StringComparison.OrdinalIgnoreCase) == true);
        var actor = await Db.User(body["userId"]?.ToString());
        if (row is null || actor is null) return Results.BadRequest();
        var name = actor["FullName"]?.ToString() ?? actor["Name"]?.ToString();
        var action = body["action"]?.ToString();
        var text = body["text"]?.ToString()?.Trim();
        async Task Note(string type, string? note, bool visible) => await Db.Exec("""
            INSERT INTO dbo.Hermes_Ticket_Activity_Trn_Tbl (TicketID, RunID, ActivityType, ActorType, ActorName, NoteText, IsCustomerVisible, CreatedBy, Source)
            VALUES (@t, @r, @type, 'Human', @n, @note, @v, @u, 'L3-Desk')
            """, ("@t", row["TicketID"]?.ToString()), ("@r", row["RunID"]?.ToString()), ("@type", type), ("@n", name), ("@note", note), ("@v", visible), ("@u", actor["ID"]?.ToString()));
        switch (action)
        {
            case "assign":
                await Db.Exec("UPDATE dbo.Hermes_L3_Escalation_Trn_Tbl SET AssignedToUserID = @u, AssignedOn = GETDATE(), L3Status = 'In progress', ModifiedOn = GETDATE() WHERE ID = @id",
                    ("@u", actor["ID"]?.ToString()), ("@id", id));
                await Note("Assignment", $"Picked up by {name}", false);
                break;
            case "note" when !string.IsNullOrEmpty(text):
                await Db.Exec("UPDATE dbo.Hermes_L3_Escalation_Trn_Tbl SET L3Remarks = ISNULL(L3Remarks + CHAR(10), '') + @x, ModifiedOn = GETDATE() WHERE ID = @id", ("@x", text), ("@id", id));
                await Note("Note", text, body["public"]?.GetValue<bool>() == true);
                break;
            case "resolve" when !string.IsNullOrEmpty(text):
                await Db.Exec("""
                    UPDATE dbo.Hermes_L3_Escalation_Trn_Tbl SET L3Status = 'Resolved', L3ResolutionSummary = @x, ResolvedOn = GETDATE(),
                        ResolvedByUserID = @u, IsProcessed = 1, ModifiedOn = GETDATE() WHERE ID = @id
                    """, ("@x", text), ("@u", actor["ID"]?.ToString()), ("@id", id));
                await Note("Resolution", text, true);
                if (body["closeTicket"]?.GetValue<bool>() == true)
                    await Db.Exec("UPDATE dbo.Complaint_Mst_Tbl SET Status = 'Closed', ModifiedOn = GETDATE() WHERE CONVERT(varchar(36), ID) = @t", ("@t", row["TicketID"]?.ToString()));
                break;
            case "reopen":
                await Db.Exec("UPDATE dbo.Hermes_L3_Escalation_Trn_Tbl SET L3Status = 'Open', ResolvedOn = NULL, ModifiedOn = GETDATE() WHERE ID = @id", ("@id", id));
                await Note("Reopened", $"Reopened by {name}", false);
                break;
            default:
                return Results.BadRequest();
        }
        return Results.Ok();
    }

    public static async Task<object> Tools() => new
    {
        tools = await Db.H("""
            SELECT ToolName, COUNT(*) AS Calls, SUM(CASE WHEN Status = 'error' OR ErrorMessage IS NOT NULL THEN 1 ELSE 0 END) AS Errors,
                   AVG(CAST(DurationMs AS float)) AS AvgMs, MAX(DurationMs) AS MaxMs, MAX(EventOn) AS LastUsed
            FROM dbo.Hermes_Agent_Trace_Trn_Tbl WHERE EventType = 'post_tool_call' AND ToolName IS NOT NULL GROUP BY ToolName ORDER BY COUNT(*) DESC
            """),
        jev = await Db.H("""
            SELECT ToolName AS Stage, COUNT(*) AS Calls, SUM(CASE WHEN Status = 'error' OR ErrorMessage IS NOT NULL THEN 1 ELSE 0 END) AS Errors,
                   AVG(CAST(DurationMs AS float)) AS AvgMs, MAX(EventOn) AS LastUsed
            FROM dbo.Hermes_Agent_Trace_Trn_Tbl WHERE EventType = 'jev_system_one' GROUP BY ToolName ORDER BY COUNT(*) DESC
            """),
        models = await Db.H("""
            SELECT Model, Provider, COUNT(*) AS Calls, AVG(CAST(DurationMs AS float)) AS AvgMs, MAX(EventOn) AS LastUsed
            FROM dbo.Hermes_Agent_Trace_Trn_Tbl WHERE EventType = 'post_api_request' GROUP BY Model, Provider ORDER BY COUNT(*) DESC
            """),
        catalog = await Db.H("SELECT ActionCategory, ActionName, PermissionLevel, Description FROM dbo.Hermes_Agent_Action_Catalog_Mst_Tbl WHERE IsDeleted = 0"),
        sql = await Db.H("""
            SELECT TOP 60 a.ActionNo, a.ActionType, a.OperationName, a.ObjectName, a.Purpose, a.Status, a.RowsAffected, a.StartedOn,
                   DATEDIFF(millisecond, a.StartedOn, a.CompletedOn) AS Ms, a.RunID, c.TicketNo, a.ErrorMessage
            FROM dbo.Hermes_L2_SQL_Action_Trn_Tbl a LEFT JOIN dbo.Complaint_Mst_Tbl c ON CONVERT(varchar(36), c.ID) = a.TicketID
            WHERE a.IsDeleted = 0 ORDER BY a.StartedOn DESC
            """),
    };

    // ---------------------------------------------------------------- Hermes Kanban (SQLite board in WSL)
    public static async Task<JsonNode?> Kanban(string command)
    {
        var psi = new ProcessStartInfo("wsl.exe") { RedirectStandardOutput = true, RedirectStandardError = true, UseShellExecute = false };
        foreach (var a in new[] { "-e", "bash", "-lc", "$HOME/.hermes/hermes-agent/venv/bin/python -m hermes_cli.main kanban " + command + " --json 2>/dev/null" })
            psi.ArgumentList.Add(a);
        try
        {
            using var proc = Process.Start(psi)!;
            using var cts = new CancellationTokenSource(TimeSpan.FromSeconds(20));
            var output = await proc.StandardOutput.ReadToEndAsync(cts.Token);
            var start = output.IndexOfAny(['[', '{']);
            return start < 0 ? null : JsonNode.Parse(output[start..]);
        }
        catch { return null; }
    }

    public static async Task<object> Board()
    {
        var tasks = await Kanban("list");
        var stats = await Kanban("stats");
        var list = (tasks as JsonArray ?? tasks?["tasks"]?.AsArray() ?? []).Select(t => new
        {
            id = t?["id"]?.ToString(),
            title = t?["title"]?.ToString(),
            status = t?["status"]?.ToString(),
            assignee = t?["assignee"]?.ToString(),
            priority = t?["priority"]?.ToString(),
            createdAt = t?["created_at"]?.GetValue<long?>(),
            startedAt = t?["started_at"]?.GetValue<long?>(),
            completedAt = t?["completed_at"]?.GetValue<long?>(),
            error = t?["last_failure_error"]?.ToString(),
            skills = t?["skills"],
            body = Db.Trim(t?["body"]?.ToString(), 6000),
        }).ToList();
        return new { available = tasks is not null, tasks = list, stats };
    }
}
