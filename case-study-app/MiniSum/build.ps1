<#
    Build & publish 3 phiên bản MiniSum, sau đó copy file .exe ra case-study-app/.

    Yêu cầu: .NET SDK 8.0 trở lên (project target net8.0-windows).
    Cách dùng:
        powershell -ExecutionPolicy Bypass -File .\build.ps1
#>
param(
    [string]$Configuration = "Release",
    [string]$Runtime = "win-x64"
)

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$outRoot = Join-Path $root "out"

$projects = @(
    @{ Project = "v1\MiniSum.csproj";    Exe = "MiniSum.exe";    OutDir = "v1" },
    @{ Project = "v2\MiniSum_v2.csproj"; Exe = "MiniSum_v2.exe"; OutDir = "v2" },
    @{ Project = "v3\MiniSum_v3.csproj"; Exe = "MiniSum_v3.exe"; OutDir = "v3" }
)

foreach ($item in $projects) {
    $projectPath = Join-Path $root $item.Project
    $publishDir = Join-Path $outRoot $item.OutDir

    Write-Host "==> Publish $($item.Exe)"
    dotnet publish $projectPath -c $Configuration -r $Runtime --self-contained false -p:PublishSingleFile=true -o $publishDir
    if ($LASTEXITCODE -ne 0) { throw "Publish that bai: $($item.Project)" }

    Copy-Item (Join-Path $publishDir $item.Exe) (Join-Path $root "..\$($item.Exe)") -Force
}

Write-Host ""
Write-Host "Hoan tat. 3 file .exe da duoc copy vao case-study-app/"
Get-ChildItem (Join-Path $root "..\*.exe") | Select-Object Name, Length, LastWriteTime
