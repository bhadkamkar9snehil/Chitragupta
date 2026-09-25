// The writer model. Three officially supported protocols cover every provider on the settings screen:
//   openai    - /chat/completions: LM Studio, Ollama, OpenAI, Gemini, Groq, OpenRouter, any compatible server
//   anthropic - /v1/messages
//   codex     - the Codex CLI, the only official way to run on a ChatGPT plan (sign in with `codex login`)
using System.Diagnostics;
using System.Net.Http.Headers;
using System.Runtime.CompilerServices;
using System.Text;
using System.Text.Json;
using System.Text.Json.Nodes;

namespace L1Api;

public static class Llm
{
    static readonly HttpClient Http = new() { Timeout = TimeSpan.FromMinutes(5) };

    static HttpRequestMessage Request(AiConfig c, HttpMethod method, string path, object? body = null)
    {
        var req = new HttpRequestMessage(method, c.BaseUrl + path);
        if (body is not null) req.Content = JsonContent.Create(body);
        if (c.Kind == "anthropic")
        {
            req.Headers.Add("x-api-key", c.ApiKey ?? "");
            req.Headers.Add("anthropic-version", "2023-06-01");
        }
        else if (!string.IsNullOrEmpty(c.ApiKey)) req.Headers.Authorization = new AuthenticationHeaderValue("Bearer", c.ApiKey);
        return req;
    }

    public static async Task<List<string>> Models(AiConfig c)
    {
        if (c.Kind == "codex") return ["gpt-5-codex", "gpt-5", "gpt-5-mini"];
        using var res = await Http.SendAsync(Request(c, HttpMethod.Get, "/models"));
        res.EnsureSuccessStatusCode();
        var data = JsonNode.Parse(await res.Content.ReadAsStringAsync())?["data"]?.AsArray() ?? [];
        return data.Select(m => m?["id"]?.ToString() ?? "").Where(m => m.Length > 0).OrderBy(m => m).ToList();
    }

    public static async IAsyncEnumerable<string> Stream(AiConfig c, string system, IEnumerable<(string role, string content)> turns,
        [EnumeratorCancellation] CancellationToken ct = default)
    {
        var chunks = c.Kind switch { "anthropic" => Anthropic(c, system, turns, ct), "codex" => Codex(c, system, turns, ct), _ => OpenAi(c, system, turns, ct) };
        // Reasoning models may stream <think>…</think>; the requester never sees it.
        var thinking = false;
        var pending = "";
        await foreach (var chunk in chunks)
        {
            pending += chunk;
            var output = new StringBuilder();
            while (pending.Length > 0)
            {
                var tag = thinking ? "</think>" : "<think>";
                var at = pending.IndexOf(tag, StringComparison.Ordinal);
                if (at >= 0)
                {
                    if (!thinking) output.Append(pending[..at]);
                    pending = pending[(at + tag.Length)..];
                    thinking = !thinking;
                    continue;
                }
                var keep = Math.Min(pending.Length, tag.Length - 1); // a tag may be split across chunks
                while (keep > 0 && !tag.StartsWith(pending[^keep..], StringComparison.Ordinal)) keep--;
                if (!thinking) output.Append(pending[..^keep]);
                pending = pending[^keep..];
                break;
            }
            if (output.Length > 0) yield return output.ToString();
        }
        if (!thinking && pending.Length > 0) yield return pending;
    }

    static async IAsyncEnumerable<string> Sse(HttpRequestMessage req, Func<JsonNode, string?> pick, [EnumeratorCancellation] CancellationToken ct)
    {
        using var res = await Http.SendAsync(req, HttpCompletionOption.ResponseHeadersRead, ct);
        if (!res.IsSuccessStatusCode) throw new HttpRequestException($"{(int)res.StatusCode}: {Db.Trim(await res.Content.ReadAsStringAsync(ct), 300)}");
        using var reader = new StreamReader(await res.Content.ReadAsStreamAsync(ct));
        while (await reader.ReadLineAsync(ct) is { } line)
        {
            if (!line.StartsWith("data:")) continue;
            var data = line[5..].Trim();
            if (data == "[DONE]") yield break;
            JsonNode? node;
            try { node = JsonNode.Parse(data); } catch { continue; }
            if (node is not null && pick(node) is { Length: > 0 } text) yield return text;
        }
    }

    static IAsyncEnumerable<string> OpenAi(AiConfig c, string system, IEnumerable<(string role, string content)> turns, CancellationToken ct)
    {
        var messages = new List<object> { new { role = "system", content = system } };
        messages.AddRange(turns.Select(t => new { t.role, t.content }));
        return Sse(Request(c, HttpMethod.Post, "/chat/completions",
            new { model = c.Model, messages, temperature = c.Temperature, max_tokens = c.MaxTokens, stream = true }),
            n => n["choices"]?[0]?["delta"]?["content"]?.ToString(), ct);
    }

    static IAsyncEnumerable<string> Anthropic(AiConfig c, string system, IEnumerable<(string role, string content)> turns, CancellationToken ct) =>
        Sse(Request(c, HttpMethod.Post, "/messages",
            new { model = c.Model, system, messages = turns.Select(t => new { t.role, t.content }), temperature = c.Temperature, max_tokens = c.MaxTokens, stream = true }),
            n => n["type"]?.ToString() == "content_block_delta" ? n["delta"]?["text"]?.ToString() : null, ct);

    static async IAsyncEnumerable<string> Codex(AiConfig c, string system, IEnumerable<(string role, string content)> turns, [EnumeratorCancellation] CancellationToken ct)
    {
        var outFile = Path.GetTempFileName();
        var psi = new ProcessStartInfo(string.IsNullOrWhiteSpace(c.Command) ? "codex" : c.Command!)
        {
            RedirectStandardInput = true, RedirectStandardOutput = true, RedirectStandardError = true, UseShellExecute = false,
            WorkingDirectory = Path.GetTempPath(),
        };
        foreach (var a in new[] { "exec", "--skip-git-repo-check", "--sandbox", "read-only", "--output-last-message", outFile })
            psi.ArgumentList.Add(a);
        if (!string.IsNullOrWhiteSpace(c.Model)) { psi.ArgumentList.Add("--model"); psi.ArgumentList.Add(c.Model); }
        psi.ArgumentList.Add("-");
        using var proc = Process.Start(psi) ?? throw new InvalidOperationException("Codex CLI did not start.");
        await proc.StandardInput.WriteAsync(system + "\n\nConversation:\n" + string.Join("\n", turns.Select(t => $"{t.role}: {t.content}"))
                                            + "\n\nWrite only the next assistant message. Do not run commands.");
        proc.StandardInput.Close();
        await proc.WaitForExitAsync(ct);
        if (proc.ExitCode != 0) throw new InvalidOperationException("Codex CLI failed: " + Db.Trim(await proc.StandardError.ReadToEndAsync(ct), 300));
        yield return (await File.ReadAllTextAsync(outFile, ct)).Trim();
        File.Delete(outFile);
    }

    public static async Task<string> Complete(AiConfig c, string system, IEnumerable<(string role, string content)> turns, CancellationToken ct = default)
    {
        var sb = new StringBuilder();
        await foreach (var t in Stream(c, system, turns, ct)) sb.Append(t);
        return sb.ToString().Trim();
    }
}

public static class Jev
{
    static readonly HttpClient Http = new() { Timeout = TimeSpan.FromSeconds(90) };
    static string Env(string n, string f = "") => Environment.GetEnvironmentVariable(n) ?? f;

    public static async Task<JsonNode?> Ask(object state, object questions)
    {
        var req = new HttpRequestMessage(HttpMethod.Post, Env("TYPESAFE_BASE_URL", "https://api.typesafe.ai") + "/v1/systemone")
            { Content = JsonContent.Create(new { model = Env("TYPESAFE_DEFAULT_MODEL", "jev-latest"), state, questions }) };
        req.Headers.Add("Authorization", "Bearer " + Env("TYPESAFE_API_KEY"));
        try { using var res = await Http.SendAsync(req); return JsonNode.Parse(await res.Content.ReadAsStringAsync())?["answers"]; }
        catch { return null; }
    }
}
