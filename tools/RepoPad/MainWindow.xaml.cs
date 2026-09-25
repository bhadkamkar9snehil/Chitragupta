using System.Collections.ObjectModel;
using System.Diagnostics;
using System.IO;
using System.Text.Json;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;

namespace RepoPad;

public partial class MainWindow : Window
{
    private readonly string _configPath =
        Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "RepoPad", "repos.json");

    private bool _running;

    public ObservableCollection<RepoAction> Repositories { get; } = [];

    public MainWindow()
    {
        InitializeComponent();
        DataContext = this;
        Loaded += (_, _) => LoadConfiguration();
    }

    private void LoadConfiguration()
    {
        try
        {
            if (!File.Exists(_configPath))
            {
                SetStatus("NO CONFIG", "#B94A3A");
                Append("RepoPad configuration was not found.");
                Append(_configPath);
                return;
            }

            var json = File.ReadAllText(_configPath);
            var config = JsonSerializer.Deserialize<RepoPadConfig>(json, new JsonSerializerOptions
            {
                PropertyNameCaseInsensitive = true
            });

            Repositories.Clear();
            foreach (var repo in config?.Repos ?? [])
                Repositories.Add(repo);

            if (Repositories.Count == 0)
            {
                SetStatus("NO REPOS", "#B94A3A");
                Append("No repository buttons are configured.");
                return;
            }

            SetStatus("READY", "#5D8C62");
            Append("RepoPad ready.");
            Append("Press a repository key to pull, validate, build and restart it.");
        }
        catch (Exception ex)
        {
            SetStatus("CONFIG ERROR", "#B94A3A");
            Append(ex.Message);
        }
    }

    private async void RepoButton_Click(object sender, RoutedEventArgs e)
    {
        if (_running || sender is not Button { Tag: RepoAction repo })
            return;

        var scriptPath = Path.IsPathRooted(repo.Script)
            ? repo.Script
            : Path.Combine(repo.Path, repo.Script);

        if (!Directory.Exists(repo.Path) || !File.Exists(scriptPath))
        {
            SetStatus("PATH ERROR", "#B94A3A");
            Append($"Cannot find {repo.Name} apply script:");
            Append(scriptPath);
            return;
        }

        _running = true;
        PadItems.IsEnabled = false;
        SetStatus("RUNNING", "#D5A33F");
        OutputBox.Clear();
        Append($"> {repo.Name}");
        Append($"> {scriptPath}");
        Append("");

        try
        {
            using var process = new Process();
            process.StartInfo = new ProcessStartInfo
            {
                FileName = "powershell.exe",
                WorkingDirectory = repo.Path,
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                CreateNoWindow = true
            };
            process.StartInfo.ArgumentList.Add("-NoProfile");
            process.StartInfo.ArgumentList.Add("-ExecutionPolicy");
            process.StartInfo.ArgumentList.Add("Bypass");
            process.StartInfo.ArgumentList.Add("-File");
            process.StartInfo.ArgumentList.Add(scriptPath);

            process.OutputDataReceived += (_, args) =>
            {
                if (args.Data is not null)
                    Dispatcher.BeginInvoke(() => Append(args.Data));
            };
            process.ErrorDataReceived += (_, args) =>
            {
                if (args.Data is not null)
                    Dispatcher.BeginInvoke(() => Append(args.Data));
            };

            if (!process.Start())
                throw new InvalidOperationException("PowerShell did not start.");

            process.BeginOutputReadLine();
            process.BeginErrorReadLine();
            await process.WaitForExitAsync();

            if (process.ExitCode == 0)
            {
                SetStatus("READY", "#5D8C62");
                Append("");
                Append("DONE — refresh the application in your browser.");
                if (!string.IsNullOrWhiteSpace(repo.Url))
                    Append(repo.Url);
            }
            else
            {
                SetStatus("FAILED", "#B94A3A");
                Append("");
                Append($"Apply failed with exit code {process.ExitCode}.");
            }
        }
        catch (Exception ex)
        {
            SetStatus("FAILED", "#B94A3A");
            Append("");
            Append(ex.Message);
        }
        finally
        {
            _running = false;
            PadItems.IsEnabled = true;
        }
    }

    private void Append(string line)
    {
        OutputBox.AppendText(line + Environment.NewLine);
        OutputBox.ScrollToEnd();
    }

    private void SetStatus(string text, string color)
    {
        StatusText.Text = text;
        StatusLed.Fill = (Brush)new BrushConverter().ConvertFromString(color)!;
    }
}

public sealed class RepoPadConfig
{
    public List<RepoAction> Repos { get; set; } = [];
}

public sealed class RepoAction
{
    public string Id { get; set; } = "";
    public string Name { get; set; } = "";
    public string Subtitle { get; set; } = "";
    public string Path { get; set; } = "";
    public string Script { get; set; } = "";
    public string Accent { get; set; } = "#D85E2B";
    public string? Url { get; set; }
}
