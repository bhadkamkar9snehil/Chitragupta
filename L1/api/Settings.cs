// Runtime settings the support console edits: AI provider, knowledge, look and feel.
// Secrets are encrypted at rest with ASP.NET Data Protection and never returned to the browser.
using System.Text.Json;
using System.Text.Json.Nodes;
using Microsoft.AspNetCore.DataProtection;

namespace L1Api;

public record AiConfig(string Provider, string Kind, string BaseUrl, string Model, string? ApiKey, double Temperature, int MaxTokens, string? Command);

public class Settings(IDataProtectionProvider dp)
{
    readonly IDataProtector protector = dp.CreateProtector("L1.Settings.Secrets");

    public static readonly JsonObject Defaults = new()
    {
        ["ai"] = new JsonObject
        {
            ["provider"] = "lmstudio", ["kind"] = "openai",
            ["baseUrl"] = Environment.GetEnvironmentVariable("L1_LMSTUDIO_URL") ?? "http://100.111.69.102:1235/v1",
            ["model"] = Environment.GetEnvironmentVariable("L1_QWEN_MODEL") ?? "qwen/qwen3.5-9b",
            ["temperature"] = 0.2, ["maxTokens"] = 600, ["command"] = "codex",
        },
        ["knowledge"] = new JsonObject { ["gbrain"] = true, ["source"] = "xstudio-knowledge", ["limit"] = 4 },
        ["widget"] = new JsonObject
        {
            ["name"] = "XBatch Helpdesk",
            ["greeting"] = "Tell us what is going wrong. We will answer straight away or hand it to the support team.",
            ["accent"] = "#c2410c",
            ["suggestions"] = new JsonArray("GR not happening for a heat, SAP shows an error",
                "Report value looks different from what I see on the screen", "A screen is not showing today's data",
                "What is the status of my tickets?"),
            ["frameAncestors"] = "*",
        },
    };

    public async Task<JsonObject> Load()
    {
        var merged = (JsonObject)Defaults.DeepClone();
        foreach (var row in await Db.H("SELECT [Key], Value FROM dbo.L1_Setting_Tbl"))
            if (row["Value"] is string v && JsonNode.Parse(v) is JsonObject stored && merged[row["Key"]!.ToString()!] is JsonObject section)
                foreach (var (k, node) in stored) section[k] = node?.DeepClone();
        return merged;
    }

    public async Task Save(string section, JsonObject values)
    {
        if (!Defaults.ContainsKey(section)) throw new ArgumentException(section);
        var current = (await Load())[section]!.AsObject();
        foreach (var (k, node) in values)
        {
            if (k == "apiKey")
            {
                var key = node?.ToString();
                if (key == "__keep__") continue;
                current["apiKeyProtected"] = string.IsNullOrEmpty(key) ? null : protector.Protect(key);
                continue;
            }
            current[k] = node?.DeepClone();
        }
        await Db.Exec("""
            MERGE dbo.L1_Setting_Tbl t USING (SELECT @k AS [Key]) s ON t.[Key] = s.[Key]
            WHEN MATCHED THEN UPDATE SET Value = @v, ModifiedOn = GETDATE()
            WHEN NOT MATCHED THEN INSERT ([Key], Value) VALUES (@k, @v)
            """, ("@k", section), ("@v", current.ToJsonString()));
    }

    // What the console may see: everything except secrets, plus whether a key is stored.
    public async Task<JsonObject> Public()
    {
        var all = await Load();
        var ai = all["ai"]!.AsObject();
        ai["hasApiKey"] = ai["apiKeyProtected"] is not null;
        ai.Remove("apiKeyProtected");
        return all;
    }

    public AiConfig Ai(JsonObject all, JsonObject? draft = null)
    {
        var ai = all["ai"]!.AsObject();
        string S(string k) => draft?[k]?.ToString() ?? ai[k]?.ToString() ?? "";
        var key = draft?["apiKey"]?.ToString();
        if (string.IsNullOrEmpty(key) || key == "__keep__")
            key = ai["apiKeyProtected"]?.ToString() is { Length: > 0 } p ? protector.Unprotect(p) : null;
        return new AiConfig(S("provider"), S("kind"), S("baseUrl").TrimEnd('/'), S("model"), key,
            double.TryParse(S("temperature"), out var t) ? t : 0.2, int.TryParse(S("maxTokens"), out var m) ? m : 600, S("command"));
    }
}
