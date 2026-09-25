// L1 Helpdesk API: the one owner of L1 behaviour. Jev decides each turn (answer / ask / raise ticket) and
// which GBrain world pages are relevant; the configured writer model only phrases replies; tickets land in
// Complaint_Mst_Tbl for the L2 pipeline. The Next.js app (l1-ui) renders all of it.
using System.Diagnostics;
using System.Text;
using System.Text.Json;
using System.Text.Json.Nodes;
using L1Api;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddDataProtection();
builder.Services.AddSingleton<Settings>();
var app = builder.Build();
await Db.Migrate();

var json = new JsonSerializerOptions(JsonSerializerDefaults.Web) { PropertyNamingPolicy = null };

const string Persona = """
    You are the first-line support assistant for XBatch, the MES of Sohar Steel (EAF, LRF, CCM, rolling mill, billet yard,
    SAP interface). Write for plant users: short, plain, friendly, no jargon about databases or AI.
    Never invent plant data, values, or causes: you cannot see live data. Use KNOWLEDGE only to explain which screen or
    report shows something and how XBatch behaves; name screens by their visible names, never table or procedure names.
    You may explain the user's own tickets from TICKETS, quoting the support team where it matters.
    If the user reports a problem, ask only for what is missing: which heat / billet / work order / screen, when,
    what they expected and what they see. Do not promise fixes. Use Markdown lists only when listing several items.
    """;

// ---------------------------------------------------------------- accounts & public config
app.MapGet("/api/users", async (string? q) => await Db.Query(Db.Config, """
    SELECT TOP 25 ID, Name, FullName, EmailID FROM dbo.XStudio_User_Mst_Tbl
    WHERE ISNULL(IsDeleted, 0) = 0 AND (@q IS NULL OR Name LIKE '%' + @q + '%' OR FullName LIKE '%' + @q + '%' OR EmailID LIKE '%' + @q + '%')
    ORDER BY ISNULL(FullName, Name)
    """, ("@q", string.IsNullOrWhiteSpace(q) ? null : q)));

app.MapGet("/api/users/{id}", async (string id) => await Db.User(id) is { } u ? Results.Ok(u) : Results.NotFound());

app.MapGet("/api/config", async (Settings s) =>
{
    var all = await s.Public();
    return Results.Ok(new { widget = all["widget"], ai = new { provider = all["ai"]!["provider"]?.ToString() } });
});

// ---------------------------------------------------------------- conversations
app.MapGet("/api/sessions", async (string userId) => await Db.H("""
    SELECT s.ID, s.Title, s.TicketNo, s.Status, s.Rating, s.CreatedOn, s.ModifiedOn,
           (SELECT TOP 1 LEFT(Content, 160) FROM dbo.L1_Chat_Message_Tbl m WHERE m.SessionID = s.ID ORDER BY m.ID DESC) AS LastMessage,
           (SELECT COUNT(*) FROM dbo.L1_Chat_Message_Tbl m WHERE m.SessionID = s.ID) AS MessageCount
    FROM dbo.L1_Chat_Session_Tbl s WHERE s.UserID = @u ORDER BY s.ModifiedOn DESC
    """, ("@u", userId)));

app.MapPost("/api/sessions", async (JsonObject body) => (await Db.H(
    "INSERT INTO dbo.L1_Chat_Session_Tbl (UserID, Title) OUTPUT inserted.ID, inserted.Title, inserted.Status, inserted.ModifiedOn VALUES (@u, N'New conversation')",
    ("@u", body["userId"]?.ToString()))).First());

app.MapPatch("/api/sessions/{id:guid}", async (Guid id, JsonObject body) =>
{
    if (body["title"]?.ToString()?.Trim() is { Length: > 0 } title)
        await Db.Exec("UPDATE dbo.L1_Chat_Session_Tbl SET Title = @t WHERE ID = @s", ("@t", Db.Trim(title, 200)), ("@s", id));
    if (body["status"]?.ToString() is "open" or "resolved" && body["status"]!.ToString() is var status)
        await Db.Exec("UPDATE dbo.L1_Chat_Session_Tbl SET Status = @st, ModifiedOn = GETDATE() WHERE ID = @s", ("@st", status), ("@s", id));
    if (body["rating"] is JsonValue r && r.TryGetValue<int>(out var rating) && rating is >= 1 and <= 5)
        await Db.Exec("UPDATE dbo.L1_Chat_Session_Tbl SET Rating = @r WHERE ID = @s", ("@r", rating), ("@s", id));
    return Results.Ok();
});

app.MapDelete("/api/sessions/{id:guid}", async (Guid id) =>
{
    await Db.Exec("DELETE FROM dbo.L1_Chat_Message_Tbl WHERE SessionID = @s; DELETE FROM dbo.L1_Chat_Session_Tbl WHERE ID = @s", ("@s", id));
    return Results.Ok();
});

app.MapGet("/api/sessions/{id:guid}/messages", async (Guid id) => await Db.H(
    "SELECT ID, Role, Content, Decision, TicketNo, SourcesJson, Feedback, CreatedOn FROM dbo.L1_Chat_Message_Tbl WHERE SessionID = @s ORDER BY ID", ("@s", id)));

app.MapPost("/api/messages/{id:long}/feedback", async (long id, JsonObject body) =>
{
    var v = body["value"]?.GetValue<int>() ?? 0;
    await Db.Exec("UPDATE dbo.L1_Chat_Message_Tbl SET Feedback = @v WHERE ID = @id", ("@v", v is -1 or 1 ? v : null), ("@id", id));
    return Results.Ok();
});

// One chat turn, streamed as server-sent events: status → sources → tokens → done.
app.MapPost("/api/sessions/{id:guid}/turn", async (Guid id, JsonObject body, HttpContext http, Settings settings) =>
{
    var text = body["text"]?.ToString()?.Trim() ?? "";
    var handoff = body["handoff"]?.GetValue<bool>() == true;
    var user = await Db.User(body["userId"]?.ToString());
    if ((text.Length == 0 && !handoff) || user is null) return Results.BadRequest();

    http.Response.Headers.ContentType = "text/event-stream";
    http.Response.Headers.CacheControl = "no-store";
    http.Response.Headers["X-Accel-Buffering"] = "no";
    var ct = http.RequestAborted;
    async Task Send(string evt, object data)
    {
        await http.Response.WriteAsync($"event: {evt}\ndata: {JsonSerializer.Serialize(data, json)}\n\n", ct);
        await http.Response.Body.FlushAsync(ct);
    }

    var clock = Stopwatch.StartNew();
    var userMessageId = text.Length > 0
        ? (await Db.H("INSERT INTO dbo.L1_Chat_Message_Tbl (SessionID, Role, Content) OUTPUT inserted.ID VALUES (@s, 'user', @c)",
            ("@s", id), ("@c", text))).First()["ID"]
        : null;
    await Send("user", new { id = userMessageId });

    var cfg = await settings.Load();
    var history = (await Db.H("SELECT Role, Content FROM dbo.L1_Chat_Message_Tbl WHERE SessionID = @s ORDER BY ID", ("@s", id)))
        .Select(m => (role: m["Role"]!.ToString()!, content: m["Content"]!.ToString()!)).ToList();
    var session = (await Db.H("SELECT TicketNo FROM dbo.L1_Chat_Session_Tbl WHERE ID = @s", ("@s", id))).First();
    var transcript = string.Join("\n", history.Select(h => $"{h.role}: {h.content}"));
    var latest = history.LastOrDefault(h => h.role == "user").content ?? "";

    await Send("status", new { text = handoff ? "Handing over to the support team" : "Reading your message" });
    var ticketsTask = Tickets.ForUser(user["EmailID"]?.ToString(), 10);
    var k = cfg["knowledge"]!;
    var sourcesTask = !handoff && k["gbrain"]?.GetValue<bool>() == true
        ? Knowledge.Search(latest, k["source"]?.ToString() ?? "xstudio-knowledge", k["limit"]?.GetValue<int>() ?? 4, ct)
        : Task.FromResult(new List<Source>());
    var tickets = await ticketsTask;
    var ticketText = string.Join("\n", tickets.Select(t =>
        $"{t["TicketNo"]}: \"{t["BriefDetails"]}\" — {t["StateLabel"]}. Support team's latest reply: {(t["ReplyText"] is null ? "none yet" : Db.Trim(t["ReplyText"], 300))}"));

    var decision = handoff ? "ticket" : "answer";
    if (!handoff && session["TicketNo"] is null)
    {
        await Send("status", new { text = "Deciding how to help" });
        var options = new Dictionary<string, string>
        {
            ["answer"] = "Answer directly: a question about XBatch screens or behaviour, about using this helpdesk, or about the user's existing tickets",
            ["ask"] = "The user reports a problem but key details are missing (which heat/billet/work order/screen, when, what is wrong)",
            ["ticket"] = "The user reports a problem (data, screen, report, SAP, login, device, request) with enough detail to hand to the support team, or asks for a person",
        };
        decision = (await Jev.Ask(new { conversation = transcript, users_existing_tickets = ticketText },
            new { next = new { type = "choice", criteria = options, instructions = "What should first-line support do next with this conversation?" } }))
            ?["next"]?["choice"]?.ToString() ?? "ask";
    }

    var sources = new List<Source>();
    if (decision != "ticket")
    {
        var hits = await sourcesTask;
        if (hits.Count > 0)
        {
            await Send("status", new { text = "Checking XBatch knowledge" });
            sources = await Knowledge.Relevant(transcript, hits);
            await Send("sources", sources.Select(s => new { s.Slug, s.Title, s.Type }));
        }
    }

    var reply = new StringBuilder();
    Dictionary<string, object?>? ticket = null;
    var ai = settings.Ai(cfg);
    if (decision == "ticket")
    {
        await Send("status", new { text = "Raising a ticket" });
        var ticketNo = await Tickets.Create(user, history.Where(h => h.role == "user").Select(h => h.content).ToList(), transcript);
        await Db.Exec("UPDATE dbo.L1_Chat_Session_Tbl SET TicketNo = @t, ModifiedOn = GETDATE() WHERE ID = @s", ("@t", ticketNo), ("@s", id));
        ticket = await Tickets.One(ticketNo);
        reply.Append($"I've raised **{ticketNo.Replace('_', ' ')}** for the support team with everything you told me. " +
                     "They investigate it against XBatch directly; their reply will appear on the ticket, and if they need anything from you they will ask there.");
        await Send("token", new { text = reply.ToString() });
        await Send("ticket", ticket!);
    }
    else
    {
        await Send("status", new { text = "Writing a reply" });
        var knowledge = string.Join("\n\n", sources.Select(s => $"[{s.Title}] {s.Snippet}"));
        var system = Persona + "\nTICKETS:\n" + (ticketText.Length > 0 ? ticketText : "(none)")
                     + "\nKNOWLEDGE:\n" + (knowledge.Length > 0 ? knowledge : "(none)")
                     + (decision == "ask" ? "\nThe user reported a problem: ask for the missing details, briefly." : "");
        try
        {
            await foreach (var chunk in Llm.Stream(ai, system, history, ct))
            {
                reply.Append(chunk);
                await Send("token", new { text = chunk });
            }
        }
        catch (Exception ex) when (ex is not OperationCanceledException)
        {
            app.Logger.LogWarning(ex, "writer model failed");
        }
        if (reply.ToString().Trim().Length == 0)
        {
            reply.Clear().Append(decision == "ask"
                ? "Could you tell me which heat, billet, work order or screen this is about, when it happened, and what you see?"
                : "I couldn't answer that just now. Try again, or choose **Talk to support** and I'll raise a ticket.");
            await Send("token", new { text = reply.ToString() });
        }
    }

    var sourcesJson = sources.Count > 0 ? JsonSerializer.Serialize(sources.Select(s => new { s.Slug, s.Title, s.Type }), json) : null;
    var saved = (await Db.H("""
        INSERT INTO dbo.L1_Chat_Message_Tbl (SessionID, Role, Content, Decision, TicketNo, SourcesJson, Model, LatencyMs)
        OUTPUT inserted.ID VALUES (@s, 'assistant', @c, @d, @t, @src, @m, @l);
        """, ("@s", id), ("@c", reply.ToString().Trim()), ("@d", decision), ("@t", ticket?["TicketNo"]), ("@src", sourcesJson),
        ("@m", decision == "ticket" ? null : $"{ai.Provider}:{ai.Model}"), ("@l", (int)clock.ElapsedMilliseconds))).First()["ID"];
    if (history.Count(h => h.role == "user") <= 1 && latest.Length > 0)
        await Db.Exec("UPDATE dbo.L1_Chat_Session_Tbl SET Title = @t WHERE ID = @s AND Title = N'New conversation'", ("@t", Db.Trim(latest, 90)), ("@s", id));
    await Db.Exec("UPDATE dbo.L1_Chat_Session_Tbl SET ModifiedOn = GETDATE(), Status = 'open' WHERE ID = @s", ("@s", id));
    await Send("done", new { id = saved, decision, ticketNo = ticket?["TicketNo"] });
    return Results.Empty;
});

// ---------------------------------------------------------------- requester tickets
app.MapGet("/api/tickets", async (string userId) =>
    await Db.User(userId) is { } u ? Results.Ok(await Tickets.ForUser(u["EmailID"]?.ToString())) : Results.NotFound());

app.MapGet("/api/tickets/{id}", async (string id) =>
{
    if (await Tickets.One(id) is not { } t) return Results.NotFound();
    t["Timeline"] = await Tickets.Timeline(t);
    t["SessionID"] = (await Db.H("SELECT TOP 1 ID FROM dbo.L1_Chat_Session_Tbl WHERE TicketNo = @n", ("@n", t["TicketNo"]))).FirstOrDefault()?["ID"];
    return Results.Ok(t);
});

// The requester answers the support team (or adds information): recorded, and the ticket goes back to L2.
app.MapPost("/api/tickets/{id}/reply", async (string id, JsonObject body) =>
{
    var text = body["text"]?.ToString()?.Trim();
    if (string.IsNullOrEmpty(text) || await Tickets.One(id) is not { } t) return Results.BadRequest();
    await Db.Exec("INSERT INTO dbo.L1_Ticket_Event_Tbl (TicketID, UserID, Kind, Content) VALUES (@t, @u, 'answer', @c)",
        ("@t", t["ID"]!.ToString()), ("@u", body["userId"]?.ToString()), ("@c", text));
    await Db.Exec("UPDATE dbo.Complaint_Mst_Tbl SET ReplyRemarks = @c, AskStatus = 'Enter', ModifiedOn = GETDATE() WHERE ID = @id",
        ("@c", text), ("@id", t["ID"]));
    return Results.Ok();
});

app.MapPost("/api/tickets/{id}/rating", async (string id, JsonObject body) =>
{
    var rating = body["rating"]?.GetValue<int>() ?? 0;
    if (rating is < 1 or > 5 || await Tickets.One(id) is not { } t) return Results.BadRequest();
    await Db.Exec("INSERT INTO dbo.L1_Ticket_Event_Tbl (TicketID, UserID, Kind, Content, Rating) VALUES (@t, @u, 'rating', @c, @r)",
        ("@t", t["ID"]!.ToString()), ("@u", body["userId"]?.ToString()), ("@c", body["comment"]?.ToString()), ("@r", rating));
    return Results.Ok();
});

// "Still not fixed": a new ticket that points at the old one; the resolved ticket's lifecycle is not touched.
app.MapPost("/api/tickets/{id}/follow-up", async (string id, JsonObject body) =>
{
    var text = body["text"]?.ToString()?.Trim();
    var user = await Db.User(body["userId"]?.ToString());
    if (string.IsNullOrEmpty(text) || user is null || await Tickets.One(id) is not { } t) return Results.BadRequest();
    var line = $"Follow-up to {t["TicketNo"]} (\"{Db.Trim(t["BriefDetails"], 200)}\"): {text}";
    var no = await Tickets.Create(user, [line], line);
    await Db.Exec("INSERT INTO dbo.L1_Ticket_Event_Tbl (TicketID, UserID, Kind, Content) VALUES (@t, @u, 'follow_up', @c)",
        ("@t", t["ID"]!.ToString()), ("@u", user["ID"]?.ToString()), ("@c", $"{no}: {text}"));
    return Results.Ok(await Tickets.One(no));
});

// ---------------------------------------------------------------- support console
var admin = app.MapGroup("/api/admin");

admin.MapGet("/tickets", async (string? q, string? tone, string? area, string? source) =>
{
    var rows = (await Db.H(Tickets.Select(300) + """
         AND (@q IS NULL OR c.TicketNo LIKE '%' + @q + '%' OR c.BriefDetails LIKE '%' + @q + '%' OR c.FirstLastName LIKE '%' + @q + '%' OR c.EmailID LIKE '%' + @q + '%')
         AND (@area IS NULL OR a.Name = @area)
         ORDER BY c.ModifiedOn DESC
        """, ("@q", string.IsNullOrWhiteSpace(q) ? null : q), ("@area", string.IsNullOrWhiteSpace(area) ? null : area)))
        .Select(Tickets.WithState)
        .Where(r => string.IsNullOrWhiteSpace(source) || r["Channel"]?.ToString() == source);
    return string.IsNullOrWhiteSpace(tone) ? rows.ToList() : rows.Where(r => r["StateTone"]?.ToString() == tone).ToList();
});

admin.MapGet("/tickets/{id}", async (string id) =>
{
    if (await Tickets.One(id) is not { } t) return Results.NotFound();
    t["Timeline"] = await Tickets.Timeline(t);
    t["Runs"] = await Db.H("""
        SELECT ID, AttemptNo, ProcessStatus, ResponseType, Route, ClaimedOn, CompletedOn, ErrorMessage
        FROM dbo.Hermes_L2_Response_Trn_Tbl WHERE TicketID = @id AND IsDeleted = 0 ORDER BY CreatedOn DESC
        """, ("@id", t["ID"]));
    var chat = (await Db.H("SELECT TOP 1 ID FROM dbo.L1_Chat_Session_Tbl WHERE TicketNo = @n", ("@n", t["TicketNo"]))).FirstOrDefault();
    t["Transcript"] = chat is null ? null : await Db.H(
        "SELECT ID, Role, Content, Decision, SourcesJson, Feedback, Model, LatencyMs, CreatedOn FROM dbo.L1_Chat_Message_Tbl WHERE SessionID = @s ORDER BY ID",
        ("@s", chat["ID"]));
    return Results.Ok(t);
});

admin.MapGet("/conversations", async (string? q, string? filter) =>
{
    var rows = await Db.H("""
        SELECT TOP 300 s.ID, s.UserID, s.Title, s.TicketNo, s.Status, s.Rating, s.CreatedOn, s.ModifiedOn,
               (SELECT COUNT(*) FROM dbo.L1_Chat_Message_Tbl m WHERE m.SessionID = s.ID) AS MessageCount,
               (SELECT COUNT(*) FROM dbo.L1_Chat_Message_Tbl m WHERE m.SessionID = s.ID AND m.Feedback = -1) AS Negative,
               (SELECT TOP 1 LEFT(Content, 160) FROM dbo.L1_Chat_Message_Tbl m WHERE m.SessionID = s.ID ORDER BY m.ID DESC) AS LastMessage
        FROM dbo.L1_Chat_Session_Tbl s
        WHERE (@q IS NULL OR s.Title LIKE '%' + @q + '%' OR s.TicketNo LIKE '%' + @q + '%')
          AND (@f IS NULL OR (@f = 'ticket' AND s.TicketNo IS NOT NULL) OR (@f = 'answered' AND s.TicketNo IS NULL)
               OR (@f = 'negative' AND EXISTS (SELECT 1 FROM dbo.L1_Chat_Message_Tbl m WHERE m.SessionID = s.ID AND m.Feedback = -1)))
        ORDER BY s.ModifiedOn DESC
        """, ("@q", string.IsNullOrWhiteSpace(q) ? null : q), ("@f", string.IsNullOrWhiteSpace(filter) ? null : filter));
    var ids = rows.Select(r => r["UserID"]!.ToString()!).Distinct().ToList();
    var users = ids.Count == 0 ? [] : (await Db.Query(Db.Config,
        $"SELECT CONVERT(varchar(36), ID) AS ID, ISNULL(FullName, Name) AS Name, EmailID FROM dbo.XStudio_User_Mst_Tbl WHERE CONVERT(varchar(36), ID) IN ({string.Join(",", ids.Select((_, i) => "@u" + i))})",
        ids.Select((v, i) => ("@u" + i, (object?)v)).ToArray())).ToDictionary(u => u["ID"]!.ToString()!.ToUpperInvariant());
    foreach (var r in rows)
        if (users.TryGetValue(r["UserID"]!.ToString()!.ToUpperInvariant(), out var u)) { r["UserName"] = u["Name"]; r["UserEmail"] = u["EmailID"]; }
    return rows;
});

admin.MapGet("/conversations/{id:guid}", async (Guid id) => await Db.H(
    "SELECT ID, Role, Content, Decision, TicketNo, SourcesJson, Feedback, Model, LatencyMs, CreatedOn FROM dbo.L1_Chat_Message_Tbl WHERE SessionID = @s ORDER BY ID",
    ("@s", id)));

admin.MapGet("/stats", async (int? days) =>
{
    var d = Math.Clamp(days ?? 14, 1, 90);
    var tickets = (await Db.H(Tickets.Select(2000) + " AND c.CreatedOn >= DATEADD(day, -@d, CAST(GETDATE() AS date)) ORDER BY c.CreatedOn",
        ("@d", d))).Select(Tickets.WithState).ToList();
    var chats = (await Db.H("""
        SELECT CAST(CreatedOn AS date) AS Day, COUNT(*) AS Conversations, SUM(CASE WHEN TicketNo IS NULL THEN 1 ELSE 0 END) AS Answered
        FROM dbo.L1_Chat_Session_Tbl WHERE CreatedOn >= DATEADD(day, -@d, CAST(GETDATE() AS date)) GROUP BY CAST(CreatedOn AS date)
        """, ("@d", d)));
    var feedback = (await Db.H("""
        SELECT SUM(CASE WHEN Feedback = 1 THEN 1 ELSE 0 END) AS Up, SUM(CASE WHEN Feedback = -1 THEN 1 ELSE 0 END) AS Down,
               AVG(CAST(LatencyMs AS float)) AS AvgLatencyMs
        FROM dbo.L1_Chat_Message_Tbl WHERE Role = 'assistant' AND CreatedOn >= DATEADD(day, -@d, CAST(GETDATE() AS date))
        """, ("@d", d))).First();
    var runtimeTotals = (await Db.H("""
        SELECT
          (SELECT COUNT(*) FROM dbo.Hermes_L2_Response_Trn_Tbl r
             WHERE r.IsDeleted = 0 AND r.CreatedOn >= DATEADD(day, -@d, CAST(GETDATE() AS date))) AS Runs,
          (SELECT AVG(CAST(DATEDIFF(second, r.ClaimedOn, r.CompletedOn) AS float)) FROM dbo.Hermes_L2_Response_Trn_Tbl r
             WHERE r.IsDeleted = 0 AND r.ClaimedOn IS NOT NULL AND r.CompletedOn IS NOT NULL
               AND r.CompletedOn >= DATEADD(day, -@d, CAST(GETDATE() AS date))) AS AvgRunSeconds,
          (SELECT MAX(DATEDIFF(second, r.ClaimedOn, r.CompletedOn)) FROM dbo.Hermes_L2_Response_Trn_Tbl r
             WHERE r.IsDeleted = 0 AND r.ClaimedOn IS NOT NULL AND r.CompletedOn IS NOT NULL
               AND r.CompletedOn >= DATEADD(day, -@d, CAST(GETDATE() AS date))) AS MaxRunSeconds,
          (SELECT AVG(CAST(a.ActionCount AS float)) FROM (
             SELECT COUNT(*) AS ActionCount FROM dbo.Hermes_L2_SQL_Action_Trn_Tbl x
             WHERE x.IsDeleted = 0 AND x.StartedOn >= DATEADD(day, -@d, CAST(GETDATE() AS date))
             GROUP BY x.RunID
           ) a) AS AvgSqlReadsPerRun,
          (SELECT AVG(CAST(t.DurationMs AS float)) FROM dbo.Hermes_Agent_Trace_Trn_Tbl t
             WHERE t.EventType = 'post_tool_call' AND t.EventOn >= DATEADD(day, -@d, CAST(GETDATE() AS date))) AS AvgToolMs,
          (SELECT AVG(CAST(t.DurationMs AS float)) FROM dbo.Hermes_Agent_Trace_Trn_Tbl t
             WHERE t.EventType = 'jev_system_one' AND t.EventOn >= DATEADD(day, -@d, CAST(GETDATE() AS date))) AS AvgJevMs,
          (SELECT AVG(CAST(t.DurationMs AS float)) FROM dbo.Hermes_Agent_Trace_Trn_Tbl t
             WHERE t.EventType = 'post_api_request' AND t.EventOn >= DATEADD(day, -@d, CAST(GETDATE() AS date))) AS AvgModelMs,
          (SELECT SUM(CASE WHEN t.Status = 'error' OR t.ErrorMessage IS NOT NULL THEN 1 ELSE 0 END) FROM dbo.Hermes_Agent_Trace_Trn_Tbl t
             WHERE t.EventType = 'post_tool_call' AND t.EventOn >= DATEADD(day, -@d, CAST(GETDATE() AS date))) AS ToolErrors,
          (SELECT COUNT(*) FROM dbo.Hermes_Agent_Trace_Trn_Tbl t
             WHERE t.EventType = 'api_request_error' AND t.EventOn >= DATEADD(day, -@d, CAST(GETDATE() AS date))) AS ModelErrors,
          (SELECT SUM(TRY_CAST(JSON_VALUE(CASE WHEN ISJSON(t.UsageJson) = 1 THEN t.UsageJson ELSE '{}' END, '$.total_tokens') AS bigint))
             FROM dbo.Hermes_Agent_Trace_Trn_Tbl t
             WHERE t.EventType = 'post_api_request' AND t.EventOn >= DATEADD(day, -@d, CAST(GETDATE() AS date))) AS TotalTokens,
          (SELECT AVG(TRY_CAST(JSON_VALUE(CASE WHEN ISJSON(t.ResultJson) = 1 THEN t.ResultJson ELSE '{}' END, '$.gpu_util_pct') AS float))
             FROM dbo.Hermes_Agent_Trace_Trn_Tbl t
             WHERE t.EventType IN ('gpu_sample','compute_sample') AND t.EventOn >= DATEADD(day, -@d, CAST(GETDATE() AS date))) AS AvgGpuUtilPct,
          (SELECT MAX(TRY_CAST(COALESCE(
                 JSON_VALUE(CASE WHEN ISJSON(t.ResultJson) = 1 THEN t.ResultJson ELSE '{}' END, '$.gpu_mem_used_mb'),
                 JSON_VALUE(CASE WHEN ISJSON(t.ResultJson) = 1 THEN t.ResultJson ELSE '{}' END, '$.mem_used_mb')) AS int))
             FROM dbo.Hermes_Agent_Trace_Trn_Tbl t
             WHERE t.EventType IN ('gpu_sample','compute_sample') AND t.EventOn >= DATEADD(day, -@d, CAST(GETDATE() AS date))) AS PeakGpuVramMb,
          (SELECT AVG(TRY_CAST(JSON_VALUE(CASE WHEN ISJSON(t.ResultJson) = 1 THEN t.ResultJson ELSE '{}' END, '$.cpu_util_pct') AS float))
             FROM dbo.Hermes_Agent_Trace_Trn_Tbl t
             WHERE t.EventType IN ('gpu_sample','compute_sample') AND t.EventOn >= DATEADD(day, -@d, CAST(GETDATE() AS date))) AS AvgCpuUtilPct
        """, ("@d", d))).First();
    var runtimeTools = await Db.H("""
        SELECT TOP 10 ToolName AS Label, COUNT(*) AS Calls,
               SUM(CASE WHEN Status = 'error' OR ErrorMessage IS NOT NULL THEN 1 ELSE 0 END) AS Errors,
               AVG(CAST(DurationMs AS float)) AS AvgMs, MAX(DurationMs) AS MaxMs
        FROM dbo.Hermes_Agent_Trace_Trn_Tbl
        WHERE EventType = 'post_tool_call' AND ToolName IS NOT NULL
          AND EventOn >= DATEADD(day, -@d, CAST(GETDATE() AS date))
        GROUP BY ToolName
        ORDER BY AVG(CAST(DurationMs AS float)) DESC, COUNT(*) DESC
        """, ("@d", d));
    var runtimeModels = await Db.H("""
        SELECT TOP 10 ISNULL(Model, 'unknown') AS Model, ISNULL(Provider, 'unknown') AS Provider, COUNT(*) AS Calls,
               AVG(CAST(DurationMs AS float)) AS AvgMs,
               SUM(TRY_CAST(JSON_VALUE(CASE WHEN ISJSON(UsageJson) = 1 THEN UsageJson ELSE '{}' END, '$.total_tokens') AS bigint)) AS Tokens
        FROM dbo.Hermes_Agent_Trace_Trn_Tbl
        WHERE EventType = 'post_api_request' AND EventOn >= DATEADD(day, -@d, CAST(GETDATE() AS date))
        GROUP BY Model, Provider ORDER BY COUNT(*) DESC
        """, ("@d", d));
    var runtimeSeries = await Db.H("""
        SELECT CAST(EventOn AS date) AS Day,
               SUM(CASE WHEN EventType = 'post_tool_call' THEN 1 ELSE 0 END) AS ToolCalls,
               SUM(CASE WHEN EventType = 'post_api_request' THEN 1 ELSE 0 END) AS ModelCalls,
               SUM(CASE WHEN EventType = 'jev_system_one' THEN 1 ELSE 0 END) AS JevCalls,
               SUM(CASE WHEN EventType = 'post_api_request'
                        THEN ISNULL(TRY_CAST(JSON_VALUE(CASE WHEN ISJSON(UsageJson) = 1 THEN UsageJson ELSE '{}' END, '$.total_tokens') AS bigint), 0)
                        ELSE 0 END) AS Tokens
        FROM dbo.Hermes_Agent_Trace_Trn_Tbl
        WHERE EventOn >= DATEADD(day, -@d, CAST(GETDATE() AS date))
        GROUP BY CAST(EventOn AS date) ORDER BY Day
        """, ("@d", d));
    var firstReplyHours = tickets.Where(t => t["FirstReplyOn"] is DateTime).Select(t => ((DateTime)t["FirstReplyOn"]! - (DateTime)t["CreatedOn"]!).TotalHours).ToList();
    var ratings = tickets.Where(t => t["Rating"] is int).Select(t => (int)t["Rating"]!).ToList();
    var series = Enumerable.Range(0, d).Select(i => DateTime.Today.AddDays(i - d + 1)).Select(day => new
    {
        day = day.ToString("yyyy-MM-dd"),
        tickets = tickets.Count(t => ((DateTime)t["CreatedOn"]!).Date == day),
        resolved = tickets.Count(t => t["StateTone"]?.ToString() == "done" && ((DateTime)t["CreatedOn"]!).Date == day),
        conversations = chats.Where(c => (DateTime)c["Day"]! == day).Sum(c => (int)c["Conversations"]!),
        answered = chats.Where(c => (DateTime)c["Day"]! == day).Sum(c => (int)c["Answered"]!),
    }).ToList();
    return new
    {
        days = d,
        totals = new
        {
            tickets = tickets.Count,
            fromChat = tickets.Count(t => t["Channel"]?.ToString() == "Helpdesk chat"),
            open = tickets.Count(t => t["StateTone"]?.ToString() != "done"),
            waiting = tickets.Count(t => t["StateTone"]?.ToString() == "attention"),
            resolved = tickets.Count(t => t["StateTone"]?.ToString() == "done"),
            conversations = series.Sum(s => s.conversations),
            answeredWithoutTicket = series.Sum(s => s.answered),
            medianFirstReplyHours = firstReplyHours.Count == 0 ? (double?)null : firstReplyHours.Order().ElementAt(firstReplyHours.Count / 2),
            csat = ratings.Count == 0 ? (double?)null : ratings.Average(),
            ratings = ratings.Count,
            thumbsUp = feedback["Up"], thumbsDown = feedback["Down"], avgLatencyMs = feedback["AvgLatencyMs"],
        },
        series,
        byState = tickets.GroupBy(t => t["StateLabel"]!.ToString()!).Select(g => new { label = g.Key, count = g.Count() }).OrderByDescending(g => g.count),
        byArea = tickets.GroupBy(t => t["Area"]?.ToString() ?? "Unassigned").Select(g => new { label = g.Key, count = g.Count() }).OrderByDescending(g => g.count),
        byType = tickets.GroupBy(t => t["Type"]?.ToString() ?? "Unassigned").Select(g => new { label = g.Key, count = g.Count() }).OrderByDescending(g => g.count),
        runtime = new { totals = runtimeTotals, tools = runtimeTools, models = runtimeModels, series = runtimeSeries },
    };
});

admin.MapGet("/lookups", async () => new
{
    areas = (await Db.H("SELECT Name FROM dbo.Area_Mst_Tbl WHERE ISNULL(IsDeleted,0) = 0 ORDER BY Name")).Select(r => r["Name"]),
    sources = new[] { "Helpdesk chat", "Other" },
});

admin.MapGet("/settings", async (Settings s) => await s.Public());
admin.MapPut("/settings/{section}", async (string section, JsonObject body, Settings s) =>
{
    await s.Save(section, body);
    return Results.Ok(await s.Public());
});

admin.MapPost("/ai/models", async (JsonObject draft, Settings s) =>
{
    try { return Results.Ok(await Llm.Models(s.Ai(await s.Load(), draft))); }
    catch (Exception ex) { return Results.Ok(new { error = Db.Trim(ex.Message, 300) }); }
});

admin.MapPost("/ai/test", async (JsonObject draft, Settings s) =>
{
    var clock = Stopwatch.StartNew();
    try
    {
        var text = await Llm.Complete(s.Ai(await s.Load(), draft), "Reply with exactly: Connected.", [("user", "Say it.")]);
        return Results.Ok(new { ok = text.Length > 0, reply = Db.Trim(text, 200), ms = clock.ElapsedMilliseconds });
    }
    catch (Exception ex) { return Results.Ok(new { ok = false, error = Db.Trim(ex.Message, 300), ms = clock.ElapsedMilliseconds }); }
});

admin.MapPost("/knowledge/search", async (JsonObject body, Settings s) =>
{
    var k = (await s.Load())["knowledge"]!;
    return (await Knowledge.Search(body["q"]?.ToString() ?? "", k["source"]?.ToString() ?? "xstudio-knowledge", 8))
        .Select(h => new Dictionary<string, object?> { ["Slug"] = h.Slug, ["Title"] = h.Title, ["Type"] = h.Type, ["Snippet"] = h.Snippet });
});

// ---------------------------------------------------------------- L2 / L3 operations
var ops = app.MapGroup("/api/ops");
ops.MapGet("/overview", Ops.Overview);
ops.MapGet("/runs", (string? q) => Ops.Runs(q));
ops.MapGet("/runs/{id}", async (string id) => await Ops.Run(id) is { } r ? Results.Ok(r) : Results.NotFound());
ops.MapGet("/live", async (string? runId, DateTime? since) =>
{
    var run = string.IsNullOrEmpty(runId) ? await Ops.LiveRun() : (await Ops.Runs(null)).FirstOrDefault(r => r["ID"]?.ToString()?.Equals(runId, StringComparison.OrdinalIgnoreCase) == true);
    if (run is null) return Results.Ok(new { run = (object?)null });
    var id = run["ID"]!.ToString()!;
    return Results.Ok(new { run, events = await Ops.Events(id, since), trail = since is null ? await Ops.Trail(id) : null });
});
ops.MapGet("/board", Ops.Board);
ops.MapGet("/l3", (string? status) => Ops.L3(status));
ops.MapPost("/l3/{id}", (string id, JsonObject body) => Ops.L3Act(id, body));
ops.MapGet("/tools", Ops.Tools);
ops.MapGet("/logs", (int? take) => Ops.RuntimeLogs(take));
ops.MapGet("/status", Health.Status);
ops.MapGet("/performance", (double? hours) => Health.Performance(hours));

app.Run();
