using System.Collections.ObjectModel;
using System.Diagnostics;
using System.Globalization;
using System.IO;
using System.Text.Json;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Media;

namespace RepoPad;

public partial class MainWindow : Window
{
    private readonly string _configPath =
        Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "RepoPad", "repos.json");

    private bool _running;
    private RepoAction? _selectedRepo;

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
                SetSurfaceState("NO CONFIG", "#B94A3A", "CONFIG MISSING");
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
            var slot = 1;
            foreach (var repo in config?.Repos ?? [])
            {
                repo.Slot = $"A{slot:00}";
                Repositories.Add(repo);
                slot++;
            }

            RepoCountText.Text = Repositories.Count.ToString("00");

            if (Repositories.Count == 0)
            {
                SetSurfaceState("NO REPOS", "#B94A3A", "NO REPOSITORIES");
                Append("No repository buttons are configured.");
                return;
            }

            SelectRepository(Repositories[0]);
            SetSurfaceState("READY", "#5D8C62", "STANDBY");
            Append("Ready.");
        }
        catch (Exception ex)
        {
            SetSurfaceState("CONFIG ERROR", "#B94A3A", "CONFIGURATION ERROR");
            Append(ex.Message);
        }
    }

    private async void RepoButton_Click(object sender, RoutedEventArgs e)
    {
        if (_running || sender is not Button { Tag: RepoAction repo })
            return;

        SelectRepository(repo);

        var scriptPath = Path.IsPathRooted(repo.Script)
            ? repo.Script
            : Path.Combine(repo.Path, repo.Script);

        if (!Directory.Exists(repo.Path) || !File.Exists(scriptPath))
        {
            SetSurfaceState("PATH ERROR", "#B94A3A", "APPLY SCRIPT NOT FOUND");
            Append($"Cannot find {repo.Name} apply script:");
            Append(scriptPath);
            return;
        }

        _running = true;
        PadItems.IsEnabled = false;
        UtilityActions.IsEnabled = false;
        RunProgress.Visibility = Visibility.Visible;
        SetSurfaceState("RUNNING", "#D5A33F", $"EXECUTING {repo.Slot}");
        OutputBox.Clear();
        Append($"[{DateTime.Now:HH:mm:ss}] {repo.Name}");
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
                SetSurfaceState("READY", "#5D8C62", "APPLY COMPLETE");
                LastRunText.Text = $"DONE {DateTime.Now:HH:mm}";
                Append("");
                Append("DONE — refresh the application in your browser.");
                if (!string.IsNullOrWhiteSpace(repo.Url))
                    Append(repo.Url);
            }
            else
            {
                SetSurfaceState("FAILED", "#B94A3A", $"EXIT {process.ExitCode}");
                LastRunText.Text = $"FAILED {DateTime.Now:HH:mm}";
                Append("");
                Append($"Apply failed with exit code {process.ExitCode}.");
            }
        }
        catch (Exception ex)
        {
            SetSurfaceState("FAILED", "#B94A3A", "EXECUTION ERROR");
            LastRunText.Text = $"FAILED {DateTime.Now:HH:mm}";
            Append("");
            Append(ex.Message);
        }
        finally
        {
            _running = false;
            PadItems.IsEnabled = true;
            UtilityActions.IsEnabled = true;
            RunProgress.Visibility = Visibility.Collapsed;
        }
    }

    private void OpenApp_Click(object sender, RoutedEventArgs e)
    {
        if (_selectedRepo is null || string.IsNullOrWhiteSpace(_selectedRepo.Url))
        {
            Append("No application URL is configured for the selected repository.");
            return;
        }

        try
        {
            Process.Start(new ProcessStartInfo(_selectedRepo.Url) { UseShellExecute = true });
        }
        catch (Exception ex)
        {
            Append($"Could not open application: {ex.Message}");
        }
    }

    private void OpenFolder_Click(object sender, RoutedEventArgs e)
    {
        if (_selectedRepo is null || !Directory.Exists(_selectedRepo.Path))
        {
            Append("The selected repository folder is unavailable.");
            return;
        }

        try
        {
            Process.Start(new ProcessStartInfo("explorer.exe", $"\"{_selectedRepo.Path}\"")
            {
                UseShellExecute = true
            });
        }
        catch (Exception ex)
        {
            Append($"Could not open repository folder: {ex.Message}");
        }
    }

    private void ClearLog_Click(object sender, RoutedEventArgs e)
    {
        OutputBox.Clear();
        CommandStateText.Text = "STANDBY";
    }

    private void SelectRepository(RepoAction repo)
    {
        _selectedRepo = repo;
        SelectedRepoName.Text = $"{repo.Slot} / {repo.Name}";
        SelectedRepoPath.Text = repo.Path;
    }

    private void Append(string line)
    {
        OutputBox.AppendText(line + Environment.NewLine);
        OutputBox.ScrollToEnd();
    }

    private void SetSurfaceState(string status, string color, string command)
    {
        StatusText.Text = status;
        StatusLed.Fill = (Brush)new BrushConverter().ConvertFromString(color)!;
        CommandStateText.Text = command;
    }
}

public sealed class HexBrushConverter : IValueConverter
{
    public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
    {
        try
        {
            var text = value?.ToString();
            if (!string.IsNullOrWhiteSpace(text))
                return (Brush)new BrushConverter().ConvertFromString(text)!;
        }
        catch
        {
        }

        return new SolidColorBrush(Color.FromRgb(216, 94, 43));
    }

    public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture) =>
        Binding.DoNothing;
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
    public string Slot { get; set; } = "";
}
