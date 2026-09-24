// L1 chat: the human front door to Chitragupta. Jev decides each turn (answer / ask / raise ticket),
// Qwen (LM Studio) only phrases replies, tickets land in Complaint_Mst_Tbl for the L2 pipeline, and
// the user sees L2's replies and answers L2's questions here. Quick and dirty on purpose.
using System.Data;
using System.Net.Http.Json;
using System.Text.Json;
using System.Text.Json.Nodes;
using System.Text.RegularExpressions;
using Microsoft.Data.SqlClient;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddCors(o => o.AddDefaultPolicy(p => p.AllowAnyOrigin().AllowAnyHeader().AllowAnyMethod()));
var app = builder.Build();
app.UseCors();

string Env(string name, string fallback = "") => Environment.GetEnvironmentVariable(name) ?? fallback;
string Conn(string db) => $"Server={Env("MSSQL_MCP_SERVER", "10.2.6.204")};Database={db};User Id={Env("MSSQL_MCP_USER", "sa")};" +
                          $"Password={Env("MSSQL_MCP_PASSWORD")};TrustServerCertificate=True;Encrypt=True;Connect Timeout=30";
var helpdesk = Conn("XStudio_Helpdesk");
var config = Conn("XStudio_Configuration_Xbatch");
var lmStudio = Env("L1_LMSTUDIO_URL", "http://100.111.69.102:1235/v1");
var qwenModel = Env("L1_QWEN_MODEL", "qwen/qwen3.5-9b");
var http = new HttpClient { Timeout = TimeSpan.FromSeconds(180) };

async Task<List<Dictionary<string, object?>>> Query(string cs, string sql, params (string, object?)[] ps)
{
    await using var con = new SqlConnection(cs);
    await con.OpenAsync();
    await using var cmd = new SqlCommand(sql, con);
    foreach (var (n, v) in ps) cmd.Parameters.AddWithValue(n, v ?? DBNull.Value);
    await using var r = await cmd.ExecuteReaderAsync();
    var rows = new List<Dictionary<string, object?>>();
    while (await r.ReadAsync())
    {
        var row = new Dictionary<string, object?>();
        for (var i = 0; i < r.FieldCount; i++) row[r.GetName(i)] = r.IsDBNull(i) ? null : r.GetValue(i);
        rows.Add(row);
    }
    return rows;
}

// Chat storage lives beside the tickets; created on first start.
await Query(helpdesk, """
    IF OBJECT_ID('dbo.L1_Chat_Session_Tbl') IS NULL
        CREATE TABLE dbo.L1_Chat_Session_Tbl (ID uniqueidentifier NOT NULL PRIMARY KEY DEFAULT NEWID(),
            UserID varchar(36) NOT NULL, Title nvarchar(200) NULL, TicketNo varchar(100) NULL,
            CreatedOn datetime NOT NULL DEFAULT GETDATE(), ModifiedOn datetime NOT NULL DEFAULT GETDATE());
    IF OBJECT_ID('dbo.L1_Chat_Message_Tbl') IS NULL
        CREATE TABLE dbo.L1_Chat_Message_Tbl (ID bigint IDENTITY PRIMARY KEY, SessionID uniqueidentifier NOT NULL,
            Role varchar(20) NOT NULL, Content nvarchar(max) NOT NULL, CreatedOn datetime NOT NULL DEFAULT GETDATE());
    SELECT 1 AS ok;
    """);

async Task<Dictionary<string, object?>?> User(string userId) =>
    (await Query(config, "SELECT ID, Name, FullName, EmailID, ContactNo FROM dbo.XStudio_User_Mst_Tbl WHERE ID = @id", ("@id", userId)))
    .FirstOrDefault();

// Tickets the user raised (matched by email), with the latest L2 reply.
async Task<List<Dictionary<string, object?>>> Tickets(string email) => await Query(helpdesk, """
    SELECT TOP 30 c.ID, c.TicketNo, c.BriefDetails, c.Status, c.AskStatus, c.CreatedOn, c.ReplyRemarks,
           r.ResponseType, r.ProcessStatus, r.ReplyText, r.CompletedOn
    FROM dbo.Complaint_Mst_Tbl c
    OUTER APPLY (SELECT TOP 1 ResponseType, ProcessStatus, ReplyText, CompletedOn FROM dbo.Hermes_L2_Response_Trn_Tbl x
                 WHERE x.TicketID = c.ID AND x.IsDeleted = 0 ORDER BY x.CreatedOn DESC) r
    WHERE ISNULL(c.IsDeleted, 0) = 0 AND c.EmailID = @e ORDER BY c.CreatedOn DESC
    """, ("@e", email));

async Task<JsonNode?> Jev(object state, object questions)
{
    var req = new HttpRequestMessage(HttpMethod.Post, Env("TYPESAFE_BASE_URL", "https://api.typesafe.ai") + "/v1/systemone")
        { Content = JsonContent.Create(new { model = Env("TYPESAFE_DEFAULT_MODEL", "jev-latest"), state, questions }) };
    req.Headers.Add("Authorization", "Bearer " + Env("TYPESAFE_API_KEY"));
    try { var res = await http.SendAsync(req); return JsonNode.Parse(await res.Content.ReadAsStringAsync())?["answers"]; }
    catch { return null; }
}

async Task<string> Qwen(string system, IEnumerable<(string role, string content)> turns)
{
    var messages = new List<object> { new { role = "system", content = system } };
    messages.AddRange(turns.Select(t => new { role = t.role, content = t.content }));
    try
    {
        var res = await http.PostAsJsonAsync(lmStudio + "/chat/completions",
            new { model = qwenModel, messages, temperature = 0.2, max_tokens = 400 });
        var text = JsonNode.Parse(await res.Content.ReadAsStringAsync())?["choices"]?[0]?["message"]?["content"]?.ToString() ?? "";
        return Regex.Replace(text, @"(?s)<think>.*?</think>", "").Trim();
    }
    catch { return ""; }
}

const string System = """
    You are the L1 support assistant for XBatch, the MES of Sohar Steel (EAF, LRF, CCM, rolling mill, SAP interface).
    Be brief and plain. Never invent plant data, values or causes: you cannot see the database.
    You may explain the status of the user's own tickets from the TICKETS section, word for word where it matters.
    If the user reports a problem, ask only for what is missing: which heat / billet / work order / screen, when, what
    they expected and what they see. Do not promise fixes.
    """;

app.MapGet("/api/users", async (string? q) => await Query(config, """
    SELECT TOP 20 ID, Name, FullName, EmailID FROM dbo.XStudio_User_Mst_Tbl
    WHERE ISNULL(IsDeleted, 0) = 0 AND (@q IS NULL OR Name LIKE '%' + @q + '%' OR FullName LIKE '%' + @q + '%') ORDER BY FullName
    """, ("@q", string.IsNullOrWhiteSpace(q) ? null : q)));

app.MapGet("/api/sessions", async (string userId) => await Query(helpdesk,
    "SELECT ID, Title, TicketNo, ModifiedOn FROM dbo.L1_Chat_Session_Tbl WHERE UserID = @u ORDER BY ModifiedOn DESC", ("@u", userId)));

app.MapPost("/api/sessions", async (JsonObject body) => (await Query(helpdesk,
    "INSERT INTO dbo.L1_Chat_Session_Tbl (UserID, Title) OUTPUT inserted.ID, inserted.Title VALUES (@u, N'New chat')",
    ("@u", body["userId"]?.ToString()))).First());

app.MapGet("/api/sessions/{id:guid}/messages", async (Guid id) => await Query(helpdesk,
    "SELECT Role, Content, CreatedOn FROM dbo.L1_Chat_Message_Tbl WHERE SessionID = @s ORDER BY ID", ("@s", id)));

app.MapGet("/api/tickets", async (string userId) =>
    await User(userId) is { } u ? Results.Ok(await Tickets(u["EmailID"]?.ToString() ?? "")) : Results.NotFound());

// The user answers an L2 QUESTION: the reply goes on the ticket and the ticket becomes eligible again.
app.MapPost("/api/tickets/{id}/reply", async (string id, JsonObject body) => await Query(helpdesk, """
    UPDATE dbo.Complaint_Mst_Tbl SET ReplyRemarks = @t, AskStatus = 'Enter', ModifiedOn = GETDATE() WHERE ID = @id;
    SELECT @@ROWCOUNT AS updated;
    """, ("@t", body["text"]?.ToString()), ("@id", id)));

app.MapPost("/api/sessions/{id:guid}/messages", async (Guid id, JsonObject body) =>
{
    var userId = body["userId"]?.ToString() ?? "";
    var text = body["text"]?.ToString()?.Trim() ?? "";
    if (text.Length == 0 || await User(userId) is not { } user) return Results.BadRequest();
    await Query(helpdesk, "INSERT INTO dbo.L1_Chat_Message_Tbl (SessionID, Role, Content) VALUES (@s, 'user', @c); SELECT 1 AS ok",
        ("@s", id), ("@c", text));
    var history = (await Query(helpdesk, "SELECT Role, Content FROM dbo.L1_Chat_Message_Tbl WHERE SessionID = @s ORDER BY ID", ("@s", id)))
        .Select(m => (role: m["Role"]!.ToString()!, content: m["Content"]!.ToString()!)).ToList();
    var session = (await Query(helpdesk, "SELECT TicketNo FROM dbo.L1_Chat_Session_Tbl WHERE ID = @s", ("@s", id))).First();
    var tickets = await Tickets(user["EmailID"]?.ToString() ?? "");
    var ticketText = string.Join("\n", tickets.Take(8).Select(t =>
        $"{t["TicketNo"]}: \"{t["BriefDetails"]}\" status {t["Status"]}/{t["AskStatus"]}; L2: {t["ResponseType"] ?? "not answered yet"} {Trim(t["ReplyText"], 300)}"));
    var transcript = string.Join("\n", history.Select(h => $"{h.role}: {h.content}"));

    // Jev decides what to do; code acts on it.
    var options = new Dictionary<string, string>
    {
        ["answer"] = "Answer directly: a question about using this chat or about the user's existing tickets and their L2 replies",
        ["ask"] = "The user reports a problem but key details are missing (which heat/billet/work order/screen, when, what is wrong)",
        ["ticket"] = "The user reports a problem (data, screen, report, SAP, login, device, request) with enough detail to hand to L2 support",
    };
    var decision = session["TicketNo"] is not null ? "answer" : (await Jev(
        new { conversation = transcript, users_existing_tickets = ticketText },
        new { next = new { type = "choice", criteria = options,
                           instructions = "What should L1 support do next with this conversation?" } }))?["next"]?["choice"]?.ToString() ?? "ask";

    string reply;
    if (decision == "ticket")
    {
        var ticketNo = await CreateTicket(user, history.Where(h => h.role == "user").Select(h => h.content).ToList(), transcript);
        await Query(helpdesk, "UPDATE dbo.L1_Chat_Session_Tbl SET TicketNo = @t, Title = @ti, ModifiedOn = GETDATE() WHERE ID = @s; SELECT 1 AS ok",
            ("@t", ticketNo), ("@ti", Trim(history.First(h => h.role == "user").content, 80)), ("@s", id));
        reply = $"I have raised {ticketNo} for the L2 support team with the details above. You will see their reply under My tickets; " +
                "if they need more information they will ask here.";
    }
    else
    {
        reply = await Qwen(System + "\nTICKETS:\n" + (ticketText.Length > 0 ? ticketText : "(none)")
                           + (decision == "ask" ? "\nThe user reported a problem: ask for the missing details." : ""), history);
        if (reply.Length == 0) reply = decision == "ask"
            ? "Could you tell me which heat / billet / work order or screen this is about, when it happened, and what you see?"
            : "Sorry, I could not answer that right now. Please try again, or describe the problem and I will raise a ticket.";
        if (history.Count(h => h.role == "user") == 1)
            await Query(helpdesk, "UPDATE dbo.L1_Chat_Session_Tbl SET Title = @t WHERE ID = @s; SELECT 1 AS ok", ("@t", Trim(text, 80)), ("@s", id));
    }
    await Query(helpdesk, "INSERT INTO dbo.L1_Chat_Message_Tbl (SessionID, Role, Content) VALUES (@s, 'assistant', @c); UPDATE dbo.L1_Chat_Session_Tbl SET ModifiedOn = GETDATE() WHERE ID = @s; SELECT 1 AS ok",
        ("@s", id), ("@c", reply));
    return Results.Ok(new { decision, reply });
});

// Deterministic ticket: requester fields, what they wrote, the transcript, identifiers found in it.
// Area and complaint type are Jev choices over the Helpdesk's real lists.
async Task<string> CreateTicket(Dictionary<string, object?> user, List<string> userLines, string transcript)
{
    var areas = await Query(helpdesk, "SELECT ID, Name FROM dbo.Area_Mst_Tbl WHERE ISNULL(IsDeleted,0) = 0");
    var types = await Query(helpdesk, "SELECT ID, Name FROM dbo.ComplaintType_Mst_Tbl WHERE ISNULL(IsDeleted,0) = 0");
    var areaOpts = areas.ToDictionary(a => a["ID"]!.ToString()!, a => a["Name"]!.ToString()!);
    var typeOpts = types.ToDictionary(t => t["ID"]!.ToString()!, t => t["Name"]!.ToString()!);
    var answers = await Jev(new { conversation = transcript }, new
    {
        area = new { type = "choice", criteria = areaOpts, instructions = "Which plant area is this problem about? (Common if unclear)" },
        kind = new { type = "choice", criteria = typeOpts, instructions = "What kind of request is this?" },
    });
    var area = answers?["area"]?["choice"]?.ToString() ?? areas.First(a => a["Name"]!.ToString() == "Common")["ID"]!.ToString();
    var kind = answers?["kind"]?["choice"]?.ToString() ?? types.First()["ID"]!.ToString();
    var description = string.Join("\n", userLines);
    var ids = Regex.Matches(description, @"(?<![\d.])(\d{7}_S\d+_\d+|\d{7,12})(?!\d)").Select(m => m.Value).Distinct().ToList();
    var next = (await Query(helpdesk,
        "SELECT ISNULL(MAX(TRY_CAST(REPLACE(TicketNo, 'Ticket_', '') AS int)), 0) + 1 AS n FROM dbo.Complaint_Mst_Tbl WHERE TicketNo LIKE 'Ticket[_]%'"))
        .First()["n"];
    var ticketNo = $"Ticket_{next}";
    await Query(helpdesk, """
        INSERT INTO dbo.Complaint_Mst_Tbl (ID, AreaID, CreatedBy, CreatedOn, ModifiedOn, IsDeleted, IsSystem, Source, ComplaintTypeID,
            Description, BriefDetails, Status, TicketNo, Priority, FirstLastName, ContactNo, EmailID, messages, AskStatus,
            SourceSystem, ConversationSummary, ExtractedEntitiesJson)
        VALUES (NEWID(), @area, @user, GETDATE(), GETDATE(), 0, 0, 'L1-Chat', @kind, @desc, @brief, 'Enter', @no,
            'EEF8F1D9-180E-49E4-95C3-3F5CB0408028', @name, @phone, @email, 'Enter', 'Enter', 'Xbatch', @summary, @entities);
        SELECT 1 AS ok;
        """, ("@area", area), ("@user", user["ID"]), ("@kind", kind), ("@desc", description), ("@brief", Trim(userLines.First(), 480)),
        ("@no", ticketNo), ("@name", user["FullName"] ?? user["Name"]), ("@phone", user["ContactNo"]), ("@email", user["EmailID"]),
        ("@summary", Trim(transcript, 4000)), ("@entities", JsonSerializer.Serialize(new { identifiers = ids })));
    return ticketNo;
}

static string Trim(object? v, int n) { var s = v?.ToString() ?? ""; return s.Length <= n ? s : s[..n]; }

app.Run();
