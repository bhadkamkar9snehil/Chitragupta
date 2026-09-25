// SQL access for the L1 API. XStudio_Helpdesk holds tickets plus L1's own tables; the XStudio
// configuration DB holds accounts (never the Password column).
using Microsoft.Data.SqlClient;

namespace L1Api;

public static class Db
{
    static string Env(string name, string fallback = "") => Environment.GetEnvironmentVariable(name) ?? fallback;
    static string Conn(string db) =>
        $"Server={Env("MSSQL_MCP_SERVER", "10.2.6.204")};Database={db};User Id={Env("MSSQL_MCP_USER", "sa")};" +
        $"Password={Env("MSSQL_MCP_PASSWORD")};TrustServerCertificate=True;Encrypt=True;Connect Timeout=30";

    public static readonly string Helpdesk = Conn("XStudio_Helpdesk");
    public static readonly string Config = Conn("XStudio_Configuration_Xbatch");

    public static async Task<List<Dictionary<string, object?>>> Query(string cs, string sql, params (string, object?)[] ps)
    {
        await using var con = new SqlConnection(cs);
        await con.OpenAsync();
        await using var cmd = new SqlCommand(sql, con) { CommandTimeout = 60 };
        foreach (var (n, v) in ps) cmd.Parameters.AddWithValue(n, v ?? DBNull.Value);
        await using var r = await cmd.ExecuteReaderAsync();
        var rows = new List<Dictionary<string, object?>>();
        do
        {
            while (await r.ReadAsync())
            {
                var row = new Dictionary<string, object?>();
                for (var i = 0; i < r.FieldCount; i++) row[r.GetName(i)] = r.IsDBNull(i) ? null : r.GetValue(i);
                rows.Add(row);
            }
        } while (rows.Count == 0 && await r.NextResultAsync());
        return rows;
    }

    public static Task<List<Dictionary<string, object?>>> H(string sql, params (string, object?)[] ps) => Query(Helpdesk, sql, ps);
    public static async Task Exec(string sql, params (string, object?)[] ps) => await Query(Helpdesk, sql + "; SELECT 1 AS ok", ps);

    // L1's own tables, created or extended on start. Tickets themselves stay in Complaint_Mst_Tbl.
    public static Task Migrate() => Exec("""
        IF OBJECT_ID('dbo.L1_Chat_Session_Tbl') IS NULL
            CREATE TABLE dbo.L1_Chat_Session_Tbl (ID uniqueidentifier NOT NULL PRIMARY KEY DEFAULT NEWID(),
                UserID varchar(36) NOT NULL, Title nvarchar(200) NULL, TicketNo varchar(100) NULL,
                CreatedOn datetime NOT NULL DEFAULT GETDATE(), ModifiedOn datetime NOT NULL DEFAULT GETDATE());
        IF COL_LENGTH('dbo.L1_Chat_Session_Tbl', 'Status') IS NULL
            ALTER TABLE dbo.L1_Chat_Session_Tbl ADD Status varchar(20) NOT NULL DEFAULT 'open', Rating int NULL;
        IF OBJECT_ID('dbo.L1_Chat_Message_Tbl') IS NULL
            CREATE TABLE dbo.L1_Chat_Message_Tbl (ID bigint IDENTITY PRIMARY KEY, SessionID uniqueidentifier NOT NULL,
                Role varchar(20) NOT NULL, Content nvarchar(max) NOT NULL, CreatedOn datetime NOT NULL DEFAULT GETDATE());
        IF COL_LENGTH('dbo.L1_Chat_Message_Tbl', 'Decision') IS NULL
            ALTER TABLE dbo.L1_Chat_Message_Tbl ADD Decision varchar(20) NULL, TicketNo varchar(100) NULL,
                SourcesJson nvarchar(max) NULL, Feedback int NULL, Model nvarchar(200) NULL, LatencyMs int NULL;
        IF OBJECT_ID('dbo.L1_Ticket_Event_Tbl') IS NULL
            CREATE TABLE dbo.L1_Ticket_Event_Tbl (ID bigint IDENTITY PRIMARY KEY, TicketID varchar(36) NOT NULL,
                UserID varchar(36) NULL, Kind varchar(20) NOT NULL, Content nvarchar(max) NULL, Rating int NULL,
                CreatedOn datetime NOT NULL DEFAULT GETDATE());
        IF OBJECT_ID('dbo.L1_Setting_Tbl') IS NULL
            CREATE TABLE dbo.L1_Setting_Tbl ([Key] varchar(100) NOT NULL PRIMARY KEY, Value nvarchar(max) NULL,
                ModifiedOn datetime NOT NULL DEFAULT GETDATE())
        """);

    public static async Task<Dictionary<string, object?>?> User(string? id) => string.IsNullOrEmpty(id) ? null :
        (await Query(Config, "SELECT ID, Name, FullName, EmailID, ContactNo FROM dbo.XStudio_User_Mst_Tbl WHERE ID = @id", ("@id", id)))
        .FirstOrDefault();

    public static string Trim(object? v, int n) { var s = v?.ToString() ?? ""; return s.Length <= n ? s : s[..n]; }
}
