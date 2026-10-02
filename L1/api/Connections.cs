// Connections: the settings a fresh install needs after it launches (SQL, LM Studio, Jev, GBrain).
// One JSON file (chitragupta.json) is the bootstrap store; both the API and the engine export it to the
// environment their code already reads. The console's Connections panel reads, tests and saves it.
// See docs/plans/no-hermes-architecture.md (D9).
using System.Diagnostics;
using System.Text.Json;
using System.Text.Json.Nodes;
using System.Security.Cryptography;
using System.Text;
using Microsoft.Data.SqlClient;

namespace L1Api;

public static class Connections
{
    // (section, key) -> environment variable, identical to Model_Bench/chitragupta_config.py.
    static readonly (string Section, string Key, string Env, bool Secret)[] Map =
    [
        ("sql", "server", "MSSQL_MCP_SERVER", false), ("sql", "user", "MSSQL_MCP_USER", false), ("sql", "password", "MSSQL_MCP_PASSWORD", true),
        ("lm_studio", "base_url", "LMSTUDIO_BASE_URL", false),
        ("jev", "api_key", "TYPESAFE_API_KEY", true), ("jev", "base_url", "TYPESAFE_BASE_URL", false),
        ("gbrain", "url", "CHITRAGUPTA_GBRAIN_URL", false), ("gbrain", "token", "CHITRAGUPTA_GBRAIN_TOKEN", true),
        ("gbrain", "client_id", "CHITRAGUPTA_GBRAIN_CLIENT_ID", false), ("gbrain", "client_secret", "CHITRAGUPTA_GBRAIN_CLIENT_SECRET", true),
        ("gbrain", "home", "CHITRAGUPTA_GBRAIN_HOME", false), ("gbrain", "bin", "CHITRAGUPTA_GBRAIN_BIN", false),
    ];

    public static string Path => Environment.GetEnvironmentVariable("CHITRAGUPTA_CONFIG_FILE")
        ?? System.IO.Path.Combine(OperatingSystem.IsWindows()
            ? Environment.GetEnvironmentVariable("PROGRAMDATA") ?? @"C:\ProgramData"
            : System.IO.Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), ".chitragupta"), "Chitragupta", "chitragupta.json");

    static JsonObject Read()
    {
        if (!File.Exists(Path)) return new();
        var file = JsonNode.Parse(File.ReadAllText(Path)) as JsonObject ?? throw new InvalidDataException("Invalid Chitragupta settings file.");
        foreach (var (section, key, _, secret) in Map)
            if (secret && file[section]?[key]?.ToString() is { } value && value.StartsWith("dpapi:", StringComparison.Ordinal))
            {
                if (!OperatingSystem.IsWindows()) throw new InvalidOperationException("Windows-protected credentials must be configured on this machine.");
                file[section]![key] = Encoding.UTF8.GetString(ProtectedData.Unprotect(Convert.FromBase64String(value[6..]), null, DataProtectionScope.LocalMachine));
            }
        return file;
    }

    public static bool SqlConfigured => !string.IsNullOrWhiteSpace(Environment.GetEnvironmentVariable("MSSQL_MCP_SERVER"))
        && !string.IsNullOrEmpty(Environment.GetEnvironmentVariable("MSSQL_MCP_PASSWORD"));

    public static void ProtectStoredSecrets()
    {
        if (!OperatingSystem.IsWindows() || !File.Exists(Path)) return;
        var stored = JsonNode.Parse(File.ReadAllText(Path));
        if (Map.Any(m => m.Secret && stored?[m.Section]?[m.Key]?.ToString() is { Length: > 0 } v && !v.StartsWith("dpapi:", StringComparison.Ordinal)))
            Save(new JsonObject());
    }

    /// <summary>Export the file to the environment. A missing file is normal on first run.</summary>
    public static void Apply()
    {
        var file = Read();
        foreach (var (section, key, env, _) in Map)
            if (file[section]?[key] is JsonNode node) Environment.SetEnvironmentVariable(env, node.ToString() is { Length: > 0 } v ? v : null);
    }

    // What the panel may see: everything except secrets, plus whether each secret is set.
    public static JsonObject Public()
    {
        var file = Read();
        var view = new JsonObject();
        foreach (var (section, key, env, secret) in Map)
        {
            var sec = view[section] as JsonObject ?? (JsonObject)(view[section] = new JsonObject());
            var v = file[section]?[key]?.ToString();
            if (secret) sec[key + "_set"] = !string.IsNullOrEmpty(v);
            else sec[key] = v ?? Environment.GetEnvironmentVariable(env);
        }
        view["path"] = Path;
        return view;
    }

    /// <summary>Merge submitted values into the file. A blank secret keeps the stored one.</summary>
    public static void Save(JsonObject submitted)
    {
        var file = Read();
        foreach (var (section, key, _, secret) in Map)
        {
            if (submitted[section]?[key] is not JsonNode node) continue;
            var value = node.ToString();
            if (secret && value.Length == 0) continue;
            var sec = file[section] as JsonObject ?? (JsonObject)(file[section] = new JsonObject());
            sec[key] = value;
        }
        Directory.CreateDirectory(System.IO.Path.GetDirectoryName(Path)!);
        foreach (var (section, key, _, secret) in Map)
            if (OperatingSystem.IsWindows() && secret && file[section]?[key]?.ToString() is { Length: > 0 } value)
                file[section]![key] = "dpapi:" + Convert.ToBase64String(ProtectedData.Protect(Encoding.UTF8.GetBytes(value), null, DataProtectionScope.LocalMachine));
        var temporary = Path + "." + Guid.NewGuid().ToString("N") + ".tmp";
        try
        {
            if (OperatingSystem.IsWindows())
            {
                using (File.Create(temporary)) { }
                Restrict(temporary);
            }
            File.WriteAllText(temporary, file.ToJsonString(new JsonSerializerOptions { WriteIndented = true }));
            File.Move(temporary, Path, overwrite: true);
        }
        finally { if (File.Exists(temporary)) File.Delete(temporary); }
        Apply();
    }

    // The file holds the SQL password and API keys: only the account that wrote it, SYSTEM and Administrators may read it.
    [System.Runtime.Versioning.SupportedOSPlatform("windows")]
    static void Restrict(string path)
    {
        var security = new System.Security.AccessControl.FileSecurity();
        security.SetAccessRuleProtection(isProtected: true, preserveInheritance: false);
        foreach (var sid in new System.Security.Principal.SecurityIdentifier?[] {
                     new(System.Security.Principal.WellKnownSidType.LocalSystemSid, null),
                     new(System.Security.Principal.WellKnownSidType.BuiltinAdministratorsSid, null),
                     System.Security.Principal.WindowsIdentity.GetCurrent().User })
            if (sid is not null)
                security.AddAccessRule(new System.Security.AccessControl.FileSystemAccessRule(sid,
                    System.Security.AccessControl.FileSystemRights.FullControl, System.Security.AccessControl.AccessControlType.Allow));
        new FileInfo(path).SetAccessControl(security);
    }

    static string Value(JsonObject? candidate, string section, string key, string env)
    {
        var v = candidate?[section]?[key]?.ToString();
        return string.IsNullOrEmpty(v) ? Read()[section]?[key]?.ToString() ?? Environment.GetEnvironmentVariable(env) ?? "" : v;
    }

    /// <summary>Probe one connection with the candidate values (falling back to what is stored).</summary>
    public static async Task<object> Test(string name, JsonObject? candidate)
    {
        try
        {
            switch (name)
            {
                case "sql":
                {
                    var cs = new SqlConnectionStringBuilder
                    {
                        DataSource = Value(candidate, "sql", "server", "MSSQL_MCP_SERVER"), UserID = Value(candidate, "sql", "user", "MSSQL_MCP_USER"),
                        Password = Value(candidate, "sql", "password", "MSSQL_MCP_PASSWORD"), InitialCatalog = "XStudio_Helpdesk",
                        TrustServerCertificate = true, ConnectTimeout = 20,
                    };
                    await using var con = new SqlConnection(cs.ConnectionString);
                    await con.OpenAsync();
                    await using var cmd = new SqlCommand("SELECT @@VERSION", con);
                    return new { ok = true, detail = ((string?)await cmd.ExecuteScalarAsync())?.Split('\n')[0] };
                }
                case "lm_studio":
                {
                    var url = Value(candidate, "lm_studio", "base_url", "LMSTUDIO_BASE_URL").TrimEnd('/');
                    using var http = new HttpClient { Timeout = TimeSpan.FromSeconds(10) };
                    var models = JsonNode.Parse(await http.GetStringAsync(url + "/models"))?["data"]?.AsArray().Select(m => m?["id"]?.ToString()).ToList() ?? [];
                    return new { ok = models.Count > 0, detail = $"{models.Count} models", models };
                }
                case "jev":
                {
                    var key = Value(candidate, "jev", "api_key", "TYPESAFE_API_KEY");
                    return new { ok = key.Length > 0, detail = key.Length > 0 ? "API key set" : "No API key" };
                }
                case "gbrain":
                {
                    var url = Value(candidate, "gbrain", "url", "CHITRAGUPTA_GBRAIN_URL").TrimEnd('/');
                    if (url.Length == 0) return new { ok = false, detail = "No GBrain service URL." };
                    using var http = new HttpClient { Timeout = TimeSpan.FromSeconds(10) };
                    var health = JsonNode.Parse(await http.GetStringAsync(url + "/health"));
                    var hits = await Knowledge.Search("XBatch", "xstudio-knowledge", 1, url: url, token: Value(candidate, "gbrain", "token", "CHITRAGUPTA_GBRAIN_TOKEN"));
                    return new { ok = hits.Count > 0, detail = $"GBrain {health?["version"]} ({health?["engine"]}); search returned {hits.Count} hit(s)" };
                }
                default: return new { ok = false, detail = "Unknown connection." };
            }
        }
        catch (Exception ex) { return new { ok = false, detail = Db.Trim(ex.Message, 300) }; }
    }
}
