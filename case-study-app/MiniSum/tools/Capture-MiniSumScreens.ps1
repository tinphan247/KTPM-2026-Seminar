<#
    Capture-MiniSumScreens.ps1
    Chụp ảnh giao diện MiniSum (dùng cho slide/report) và dump cây UI Automation
    để đối chiếu AutomationId.

    Cách dùng:
        powershell -ExecutionPolicy Bypass -File .\Capture-MiniSumScreens.ps1 -Exe ..\..\MiniSum.exe    -Version v1 -OutDir ..\..\..\docs\screenshots\app
        powershell -ExecutionPolicy Bypass -File .\Capture-MiniSumScreens.ps1 -Exe ..\..\MiniSum_v2.exe -Version v2 -OutDir ..\..\..\docs\screenshots\app
        powershell -ExecutionPolicy Bypass -File .\Capture-MiniSumScreens.ps1 -Exe ..\..\MiniSum_v3.exe -Version v3 -OutDir ..\..\..\docs\screenshots\app

    Lưu ý: nên chạy khi màn hình đang ở scale 100% và không có cửa sổ nào che lên app.
#>
param(
    [Parameter(Mandatory = $true)][string]$Exe,
    [Parameter(Mandatory = $true)]
    [ValidateSet("v1", "v2", "v3")]
    [string]$Version,
    [Parameter(Mandatory = $true)][string]$OutDir
)

$ErrorActionPreference = "Stop"
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName Microsoft.VisualBasic

Add-Type @"
using System;
using System.Runtime.InteropServices;
public class MiniSumWin32
{
    [StructLayout(LayoutKind.Sequential)]
    public struct RECT { public int Left, Top, Right, Bottom; }

    [StructLayout(LayoutKind.Sequential)]
    public struct POINT { public int X, Y; }

    [DllImport("user32.dll")] public static extern bool SetWindowPos(IntPtr hWnd, IntPtr hWndInsertAfter, int x, int y, int cx, int cy, uint flags);
    [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr hWnd, out RECT rect);
    [DllImport("user32.dll")] public static extern bool GetClientRect(IntPtr hWnd, out RECT rect);
    [DllImport("user32.dll")] public static extern bool ClientToScreen(IntPtr hWnd, ref POINT point);

    /// <summary>
    /// Vùng ảnh cần chụp: đúng vùng client của cửa sổ (không gồm thanh tiêu đề của Windows).
    /// Cách này không phụ thuộc viền trong suốt của DWM nên ảnh luôn khớp với giao diện.
    /// </summary>
    public static RECT GetCaptureBounds(IntPtr hwnd)
    {
        RECT client;
        POINT origin = new POINT();
        GetClientRect(hwnd, out client);
        ClientToScreen(hwnd, ref origin);

        RECT bounds = new RECT();
        bounds.Left = origin.X;
        bounds.Top = origin.Y;
        bounds.Right = origin.X + client.Right;
        bounds.Bottom = origin.Y + client.Bottom;
        return bounds;
    }
}
"@

if (-not (Test-Path $OutDir)) { New-Item -ItemType Directory -Path $OutDir -Force | Out-Null }

function Get-WindowByName([int]$procId, [string]$name, [int]$timeoutSec = 10) {
    $conditions = New-Object System.Windows.Automation.AndCondition(
        (New-Object System.Windows.Automation.PropertyCondition(
            [System.Windows.Automation.AutomationElement]::NameProperty, $name)),
        (New-Object System.Windows.Automation.PropertyCondition(
            [System.Windows.Automation.AutomationElement]::ProcessIdProperty, $procId)),
        (New-Object System.Windows.Automation.PropertyCondition(
            [System.Windows.Automation.AutomationElement]::ControlTypeProperty,
            [System.Windows.Automation.ControlType]::Window)))

    $deadline = (Get-Date).AddSeconds($timeoutSec)
    while ((Get-Date) -lt $deadline) {
        $wins = [System.Windows.Automation.AutomationElement]::RootElement.FindAll(
            [System.Windows.Automation.TreeScope]::Descendants, $conditions)
        foreach ($win in $wins) {
            if (-not $win.Current.IsOffscreen) { return $win }
        }
        Start-Sleep -Milliseconds 200
    }
    throw "Khong tim thay cua so '$name' cua process $procId"
}

function Find-ById($root, [string]$id) {
    $cond = New-Object System.Windows.Automation.PropertyCondition(
        [System.Windows.Automation.AutomationElement]::AutomationIdProperty, $id)
    return $root.FindFirst([System.Windows.Automation.TreeScope]::Descendants, $cond)
}

function Set-Text($root, [string]$id, [string]$value) {
    $el = Find-ById $root $id
    if ($el -eq $null) { throw "Khong tim thay AutomationId '$id'" }
    $el.GetCurrentPattern([System.Windows.Automation.ValuePattern]::Pattern).SetValue($value)
    Start-Sleep -Milliseconds 150
}

function Invoke-Button($root, [string]$id) {
    $el = Find-ById $root $id
    if ($el -eq $null) { throw "Khong tim thay AutomationId '$id'" }
    $el.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern).Invoke()
    Start-Sleep -Milliseconds 150
}

function Save-Screenshot($window, [string]$fileName) {
    $handle = [IntPtr]$window.Current.NativeWindowHandle
    # Đưa cửa sổ về màn hình chính, tạm bật topmost để không bị cửa sổ khác che khi chụp.
    # SWP_NOSIZE 0x1 | SWP_SHOWWINDOW 0x40, HWND_TOPMOST = -1
    [MiniSumWin32]::SetWindowPos($handle, [IntPtr](-1), 140, 80, 0, 0, 0x41) | Out-Null
    Start-Sleep -Milliseconds 450

    $bounds = [MiniSumWin32]::GetCaptureBounds($handle)
    $width = $bounds.Right - $bounds.Left
    $height = $bounds.Bottom - $bounds.Top
    $path = Join-Path $OutDir $fileName

    $bitmap = New-Object System.Drawing.Bitmap $width, $height
    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
    try {
        $graphics.CopyFromScreen($bounds.Left, $bounds.Top, 0, 0,
            [System.Drawing.Size]::new($width, $height))
        $bitmap.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
    }
    finally {
        $graphics.Dispose()
        $bitmap.Dispose()
        # HWND_NOTOPMOST = -2, SWP_NOSIZE 0x1 | SWP_NOMOVE 0x2
        [MiniSumWin32]::SetWindowPos($handle, [IntPtr](-2), 0, 0, 0, 0, 0x3) | Out-Null
    }

    Write-Host ("  anh  {0}  ({1}x{2})" -f $fileName, $width, $height)
}

function Write-UiaTree($window, [string]$title) {
    Write-Host ("--- UIA {0} ---" -f $title)
    $all = $window.FindAll([System.Windows.Automation.TreeScope]::Descendants,
        [System.Windows.Automation.Condition]::TrueCondition)

    foreach ($el in $all) {
        $type = $el.Current.ControlType.ProgrammaticName -replace "ControlType\.", ""
        $id = $el.Current.AutomationId
        $name = $el.Current.Name -replace "\r?\n", " "
        Write-Host ("  {0,-12} id={1,-22} name={2}" -f $type, $id, $name)
    }
}

Write-Host ("=== Chup anh {0}: {1} ===" -f $Version, $Exe)
$proc = Start-Process -FilePath $Exe -PassThru
try {
    $login = Get-WindowByName $proc.Id "MiniSum - Dang nhap"
    Start-Sleep -Milliseconds 600

    if ($Version -eq "v1") {
        Save-Screenshot $login "login.png"

        Set-Text $login "txtUser" "admin"
        Set-Text $login "txtPass" "sai-mat-khau"
        Invoke-Button $login "btnLogin"
        Start-Sleep -Milliseconds 400
        Save-Screenshot $login "login-error.png"

        Set-Text $login "txtPass" "1234"
        Invoke-Button $login "btnLogin"
        Start-Sleep -Milliseconds 250
        Save-Screenshot $login "login-success.png"

        Write-UiaTree $login "Login"
    }
    else {
        Set-Text $login "txtUser" "admin"
        Set-Text $login "txtPass" "1234"
        Invoke-Button $login "btnLogin"
    }

    $calc = Get-WindowByName $proc.Id "MiniSum - Tinh tong"
    Start-Sleep -Milliseconds 600

    $sumId = switch ($Version) { "v2" { "btnCalculate" } default { "btnSum" } }

    Save-Screenshot $calc "calculator-$Version.png"

    Set-Text $calc "txtA" "5"
    Set-Text $calc "txtB" "7"
    Invoke-Button $calc $sumId
    Start-Sleep -Milliseconds 400
    Save-Screenshot $calc "calculator-$Version-result.png"

    if ($Version -eq "v2") {
        Invoke-Button $calc "btnHistory"
        $history = Get-WindowByName $proc.Id "MiniSum - Lich su tinh toan"
        Start-Sleep -Milliseconds 600
        Save-Screenshot $history "history-v2.png"
        Write-UiaTree $history "History (v2)"

        Invoke-Button $history "btnClose"
        Start-Sleep -Milliseconds 400
    }

    if ($Version -eq "v3") {
        Set-Text $calc "txtA" "abc"
        Set-Text $calc "txtB" "1"
        Invoke-Button $calc $sumId
        Start-Sleep -Milliseconds 400
        Save-Screenshot $calc "calculator-v3-error.png"
    }

    Write-UiaTree $calc "Calculator"

    Invoke-Button $calc "btnLogout"
    Start-Sleep -Milliseconds 600
}
finally {
    Start-Sleep -Milliseconds 300
    if (-not $proc.HasExited) { Stop-Process -Id $proc.Id -Force }
}

Write-Host "Hoan tat."
