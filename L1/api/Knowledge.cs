// L1's knowledge is the same generated XBatch world L2 walks: GBrain source `xstudio-knowledge`.
// GBrain runs natively; one CLI call per turn. Jev decides which hits are relevant; code never ranks by hand.
using System.Diagnostics;
using System.Text.Json.Nodes;

namespace L1Api;

public record Source(string Slug, string Title, string Type, string Snippet);

public static class Knowledge
{
    // GBrain runs natively (Bun). Home and binary are overridable; the defaults are where the installer puts them.
    static string Home => Environment.GetEnvironmentVariable("CHITRAGUPTA_GBRAIN_HOME")
        ?? Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), ".chitragupta", "gbrain");
    static string Bin => Environment.GetEnvironmentVariable("CHITRAGUPTA_GBRAIN_BIN")
        ?? Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), ".bun", "bin", "gbrain.exe");

    public static async Task<List<Source>> Search(string query, string sourceId, int limit, CancellationToken ct = default)
    {
        var psi = new ProcessStartInfo(Bin) { RedirectStandardOutput = true, RedirectStandardError = true, UseShellExecute = false };
        psi.Environment["GBRAIN_HOME"] = Home;
        foreach (var a in new[] { "search", query, "--source-id", sourceId, "--limit", limit.ToString(), "--json" }) psi.ArgumentList.Add(a);
        try
        {
            using var proc = Process.Start(psi)!;
            using var timeout = CancellationTokenSource.CreateLinkedTokenSource(ct);
            timeout.CancelAfter(TimeSpan.FromSeconds(20));
            var output = await proc.StandardOutput.ReadToEndAsync(timeout.Token);
            await proc.WaitForExitAsync(timeout.Token);
            var start = output.IndexOf('[');
            if (start < 0) return [];
            return (JsonNode.Parse(output[start..])?.AsArray() ?? [])
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
