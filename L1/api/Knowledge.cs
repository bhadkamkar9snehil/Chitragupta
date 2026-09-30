// L1's knowledge is the same generated XBatch world L2 walks: GBrain source `xstudio-knowledge`.
// GBrain runs as one service (`gbrain serve --http`) because its embedded database admits a single process;
// every client, including this one, asks it over MCP/HTTP. Jev decides which hits are relevant; code never ranks by hand.
using System.Text.Json.Nodes;

namespace L1Api;

public record Source(string Slug, string Title, string Type, string Snippet);

public static class Knowledge
{
    static readonly HttpClient Http = new() { Timeout = TimeSpan.FromSeconds(20) };

    public static async Task<List<Source>> Search(string query, string sourceId, int limit, CancellationToken ct = default, string? url = null, string? token = null)
    {
        url ??= Environment.GetEnvironmentVariable("CHITRAGUPTA_GBRAIN_URL");
        token ??= Environment.GetEnvironmentVariable("CHITRAGUPTA_GBRAIN_TOKEN");
        if (string.IsNullOrWhiteSpace(url)) return [];
        try
        {
            var body = new JsonObject
            {
                ["jsonrpc"] = "2.0", ["id"] = 1, ["method"] = "tools/call",
                ["params"] = new JsonObject { ["name"] = "search", ["arguments"] = new JsonObject { ["query"] = query, ["limit"] = limit } },
            };
            using var req = new HttpRequestMessage(HttpMethod.Post, url.TrimEnd('/') + "/mcp") { Content = new StringContent(body.ToJsonString(), System.Text.Encoding.UTF8, "application/json") };
            req.Headers.Accept.ParseAdd("application/json, text/event-stream");
            req.Headers.Authorization = new("Bearer", token);
            using var res = await Http.SendAsync(req, ct);
            var raw = await res.Content.ReadAsStringAsync(ct);
            var data = raw.Split('\n').FirstOrDefault(l => l.StartsWith("data:"))?[5..].Trim() ?? raw;
            var text = string.Concat(JsonNode.Parse(data)?["result"]?["content"]?.AsArray().Select(c => c?["text"]?.ToString()) ?? []);
            var start = text.IndexOf('[');
            if (start < 0) return [];
            // A bearer token searches its granted sources; keep the wanted one.
            return (JsonNode.Parse(text[start..])?.AsArray() ?? [])
                .Where(n => n?["source_id"]?.ToString() is null or "" || n["source_id"]!.ToString() == sourceId)
                .Select(n => new Source(n?["slug"]?.ToString() ?? "", n?["title"]?.ToString() ?? "", n?["type"]?.ToString() ?? "",
                                        Db.Trim(n?["chunk_text"]?.ToString(), 1200)))
                .Where(s => s.Slug.Length > 0).DistinctBy(s => s.Slug).ToList();
        }
        catch { return []; }
    }

    // Jev keeps only hits that help answer this requester: one batched noul call, same 0.60 gate as L2's walk.
    public static async Task<List<Source>> Relevant(string conversation, List<Source> hits)
    {
        if (hits.Count == 0) return hits;
        var questions = new JsonObject();
        var pages = new JsonObject();
        for (var i = 0; i < hits.Count; i++)
        {
            pages[$"h{i}"] = $"{hits[i].Title} ({hits[i].Type}): {Db.Trim(hits[i].Snippet, 600)}";
            questions[$"h{i}"] = new JsonObject
            {
                ["type"] = "noul",
                ["instructions"] = new JsonObject
                {
                    ["task"] = "Does this XBatch knowledge page help answer the user's latest message?",
                    ["conversation_path"] = "conversation", ["page_path"] = $"pages.h{i}",
                },
            };
        }
        var answers = await Jev.Ask(new { conversation, pages }, questions);
        return hits.Where((_, i) => (double?)answers?[$"h{i}"]?["noul"] >= 0.60).ToList();
    }
}
