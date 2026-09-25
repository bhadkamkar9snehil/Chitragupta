// Pipeline health for the console: the two existing diagnostics, not a new one.
//  - status:      the L2 runtime's own `l2_pipeline_runtime.py status` (WSL, the profile's .env)
//  - performance: `Model_Bench/benchmark_l2_performance.py --json` (the one live-health report; extend it, not this)
// Both are read-only. Results are cached briefly so a page refresh cannot pile processes onto WSL or SQL.
using System.Collections.Concurrent;
using System.Diagnostics;
using System.Text.Json.Nodes;

namespace L1Api;

public static class Health
{
    static readonly ConcurrentDictionary<string, (DateTime At, JsonNode? Data, string? Error)> Cache = new();
    static readonly SemaphoreSlim Gate = new(1, 1);

    // The .env is CRLF; a raw `source` puts \r into the server name and every SQL login times out.
    const string RuntimeStatus =
        "cd ~ && set -a && source <(tr -d '\\r' < ~/.hermes/profiles/l2-investigator/.env) && set +a && " +
        "python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py status";

    public static Task<IResult> Status() => Cached("status", TimeSpan.FromSeconds(20), async () =>
    {
        var psi = new ProcessStartInfo("wsl.exe");
        foreach (var a in new[] { "-e", "bash", "-lc", RuntimeStatus }) psi.ArgumentList.Add(a);
        var (json, error) = await RunJson(psi, TimeSpan.FromSeconds(120));
        if (json is null) return (null, error);
        return json["ok"]?.GetValue<bool>() == true ? (json["result"], null) : (null, json["error"]?.ToString() ?? "The runtime reported a failure.");
    });

    public static Task<IResult> Performance(double? hours)
    {
        var h = Math.Clamp(hours ?? 24, 0.5, 168);
        return Cached($"perf:{h}", TimeSpan.FromSeconds(30), async () =>
        {
            var script = RepoFile("Model_Bench", "benchmark_l2_performance.py");
            if (script is null) return (null, "Model_Bench/benchmark_l2_performance.py was not found next to the API.");
            var psi = new ProcessStartInfo("python") { WorkingDirectory = Path.GetDirectoryName(Path.GetDirectoryName(script))! };
            foreach (var a in new[] { script, "--hours", h.ToString(System.Globalization.CultureInfo.InvariantCulture), "--json" }) psi.ArgumentList.Add(a);
            return await RunJson(psi, TimeSpan.FromSeconds(90));
        });
    }

    static async Task<IResult> Cached(string key, TimeSpan ttl, Func<Task<(JsonNode?, string?)>> load)
    {
        if (Cache.TryGetValue(key, out var hit) && DateTime.Now - hit.At < ttl) return Reply(hit);
        await Gate.WaitAsync();
        try
        {
            if (Cache.TryGetValue(key, out hit) && DateTime.Now - hit.At < ttl) return Reply(hit);
            var (data, error) = await load();
            var entry = (DateTime.Now, data, error);
            Cache[key] = entry;
            return Reply(entry);
        }
        finally { Gate.Release(); }
    }

    static IResult Reply((DateTime At, JsonNode? Data, string? Error) e) =>
        Results.Ok(new { at = e.At, ok = e.Error is null, error = e.Error, data = e.Data });

    static async Task<(JsonNode?, string?)> RunJson(ProcessStartInfo psi, TimeSpan timeout)
    {
        psi.RedirectStandardOutput = true;
        psi.RedirectStandardError = true;
        psi.UseShellExecute = false;
        try
        {
            using var proc = Process.Start(psi)!;
            using var cts = new CancellationTokenSource(timeout);
            var stdout = proc.StandardOutput.ReadToEndAsync(cts.Token);
            var stderr = proc.StandardError.ReadToEndAsync(cts.Token);
            try { await proc.WaitForExitAsync(cts.Token); }
            catch (OperationCanceledException) { proc.Kill(true); return (null, $"Timed out after {timeout.TotalSeconds:0} s."); }
            var output = await stdout;
            var start = output.IndexOf('{');
            if (start < 0) return (null, Db.Trim((await stderr).Trim() is { Length: > 0 } err ? err : $"No output (exit {proc.ExitCode}).", 400));
            return (JsonNode.Parse(output[start..]), null);
        }
        catch (Exception ex) { return (null, Db.Trim(ex.Message, 400)); }
    }

    // The API runs from the repo (dotnet run) or its bin folder; find the repo file either way.
    static string? RepoFile(params string[] parts)
    {
        for (var dir = new DirectoryInfo(AppContext.BaseDirectory); dir is not null; dir = dir.Parent)
        {
            var path = Path.Combine([dir.FullName, .. parts]);
            if (File.Exists(path)) return path;
        }
        return null;
    }
}
