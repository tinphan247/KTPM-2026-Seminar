<#
    Verify-MiniSum.ps1
    Kiểm tra nhanh (smoke test) một bản build MiniSum thông qua UI Automation,
    đóng vai trò "kiểm thử trước khi bàn giao" cho Katalon Studio và WinAppDriver.

    Cách dùng:
        powershell -ExecutionPolicy Bypass -File .\Verify-MiniSum.ps1 -Exe ..\MiniSum.exe -Version v1
        powershell -ExecutionPolicy Bypass -File .\Verify-MiniSum.ps1 -Exe ..\MiniSum_v2.exe -Version v2
        powershell -ExecutionPolicy Bypass -File .\Verify-MiniSum.ps1 -Exe ..\MiniSum_v3.exe -Version v3

    Script sẽ tự mở ứng dụng, thao tác bằng UI Automation rồi đóng ứng dụng.
#>
param(
    [Parameter(Mandatory = $true)][string]$Exe,
    [Parameter(Mandatory = $true)]
    [ValidateSet("v1", "v2", "v3")]
    [string]$Version
)

$ErrorActionPreference = "Stop"
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes

$script:failures = 0

function Check([string]$label, [bool]$ok, [string]$detail = "") {
    if ($ok) {
        Write-Host ("PASS  {0}" -f $label)
    }
    else {
        Write-Host ("FAIL  {0}  {1}" -f $label, $detail)
        $script:failures++
    }
}

function Get-LoginWindow($proc, [int]$timeoutSec = 10) {
    $cond = New-Object System.Windows.Automation.PropertyCondition(
        [System.Windows.Automation.AutomationElement]::ProcessIdProperty, $proc.Id)
    $deadline = (Get-Date).AddSeconds($timeoutSec)
    while ((Get-Date) -lt $deadline) {
        $win = [System.Windows.Automation.AutomationElement]::RootElement.FindFirst(
            [System.Windows.Automation.TreeScope]::Children, $cond)
        if ($win -ne $null) { return $win }
        Start-Sleep -Milliseconds 200
    }
    throw "Khong tim thay cua so cua process $($proc.Id)"
}

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
    return $null
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

function Get-Text($root, [string]$id) {
    $el = Find-ById $root $id
    if ($el -eq $null) { return $null }
    return $el.Current.Name
}

Write-Host ("=== Kiem tra {0}: {1} ===" -f $Version, $Exe)
$proc = Start-Process -FilePath $Exe -PassThru
try {
    $login = Get-LoginWindow $proc
    Start-Sleep -Milliseconds 500
    Check "Cua so Login dung title" ($login.Current.Name -eq "MiniSum - Dang nhap") $login.Current.Name

    foreach ($id in @("txtUser", "txtPass", "btnLogin", "lblMessage")) {
        Check "Login co AutomationId $id" ((Find-ById $login $id) -ne $null)
    }

    # 1. Dang nhap sai mat khau
    Set-Text $login "txtUser" "admin"
    Set-Text $login "txtPass" "sai-mat-khau"
    Invoke-Button $login "btnLogin"
    Start-Sleep -Milliseconds 400
    $msg = Get-Text $login "lblMessage"
    Check "Sai mat khau -> thong bao loi" ($msg -eq "Sai tai khoan hoac mat khau") $msg

    # 2. Dang nhap hop le
    Set-Text $login "txtPass" "1234"
    Invoke-Button $login "btnLogin"
    Start-Sleep -Milliseconds 400
    $msg = Get-Text $login "lblMessage"
    Check "Dang nhap hop le -> lblMessage" ($msg -eq "Dang nhap thanh cong") $msg

    # 3. Chuyen sang man hinh tinh toan (sau 1s)
    Start-Sleep -Milliseconds 1500
    $calc = Get-WindowByName $proc.Id "MiniSum - Tinh tong"
    Check "Chuyen sang cua so Calculator" ($calc -ne $null)
    if ($calc -eq $null) { throw "Khong mo duoc cua so Calculator" }

    $sumId = switch ($Version) { "v2" { "btnCalculate" } default { "btnSum" } }
    foreach ($id in @("txtA", "txtB", $sumId, "lblResult", "btnLogout")) {
        Check "Calculator co AutomationId $id" ((Find-ById $calc $id) -ne $null)
    }

    # 4. Tinh tong hop le
    Set-Text $calc "txtA" "5"
    Set-Text $calc "txtB" "7"
    Invoke-Button $calc $sumId
    Start-Sleep -Milliseconds 400
    $result = Get-Text $calc "lblResult"
    Check "5 + 7 = 12" ($result -eq "Ket qua: 5 + 7 = 12") $result

    # 5. Kiem tra dac thu tung phien ban
    if ($Version -eq "v3") {
        Check "v3 co nhan lblError" ((Find-ById $calc "lblError") -ne $null)

        Set-Text $calc "txtA" "abc"
        Set-Text $calc "txtB" "1"
        Invoke-Button $calc $sumId
        Start-Sleep -Milliseconds 300
        $err = Get-Text $calc "lblError"
        Check "v3 chan du lieu khong phai so" ($err -eq "Gia tri khong hop le: phai la so nguyen") $err

        Set-Text $calc "txtA" "100"
        Set-Text $calc "txtB" "1"
        Invoke-Button $calc $sumId
        Start-Sleep -Milliseconds 300
        $err = Get-Text $calc "lblError"
        Check "v3 chan A ngoai mien" ($err -eq "A ngoai mien [-99, 99]") $err

        Set-Text $calc "txtA" ""
        Set-Text $calc "txtB" "1"
        Invoke-Button $calc $sumId
        Start-Sleep -Milliseconds 300
        $err = Get-Text $calc "lblError"
        Check "v3 chan du lieu rong" ($err -eq "Vui long nhap day du gia tri A va B") $err
    }
    else {
        Check "$Version khong co nhan lblError" ((Find-ById $calc "lblError") -eq $null)

        Set-Text $calc "txtA" "abc"
        Set-Text $calc "txtB" "1"
        Invoke-Button $calc $sumId
        Start-Sleep -Milliseconds 300
        $result = Get-Text $calc "lblResult"
        Check "$Version bao sai dinh dang tren lblResult" ($result -eq "Nhap sai dinh dang") $result
    }

    if ($Version -eq "v2") {
        Check "v2 co nut btnHistory" ((Find-ById $calc "btnHistory") -ne $null)
        Invoke-Button $calc "btnHistory"
        Start-Sleep -Milliseconds 600
        $history = Get-WindowByName $proc.Id "MiniSum - Lich su tinh toan"
        Check "v2 mo duoc man hinh Lich su" ($history -ne $null)
        if ($history -ne $null) {
            Start-Sleep -Milliseconds 300
            Check "Lich su co danh sach lstHistory" ((Find-ById $history "lstHistory") -ne $null)
            Invoke-Button $history "btnClose"
            Start-Sleep -Milliseconds 300
        }
    }

    # 6. Dang xuat quay ve Login
    Invoke-Button $calc "btnLogout"
    Start-Sleep -Milliseconds 600
    $loginAgain = Get-WindowByName $proc.Id "MiniSum - Dang nhap"
    Check "Dang xuat quay ve man hinh Login" ($loginAgain -ne $null)
}
finally {
    Start-Sleep -Milliseconds 300
    if (-not $proc.HasExited) { Stop-Process -Id $proc.Id -Force }
}

Write-Host ("--- Ket qua {0}: {1} loi ---" -f $Version, $script:failures)
if ($script:failures -gt 0) { exit 1 }
