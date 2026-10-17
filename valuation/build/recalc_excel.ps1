# Recalculate workbooks in a private Excel instance and save them, so cached values
# exist for openpyxl (data_only=True) checks. Macros disabled, no link updates, no
# data refresh; only the Excel instance created here is closed.
# Usage: powershell -NoProfile -ExecutionPolicy Bypass -File recalc_excel.ps1 <path1.xlsx> [<path2.xlsx> ...]
param([Parameter(ValueFromRemainingArguments = $true)][string[]]$Paths)

$ErrorActionPreference = "Stop"
$excel = New-Object -ComObject Excel.Application
try {
    $excel.Visible = $false
    $excel.DisplayAlerts = $false
    $excel.AskToUpdateLinks = $false
    $excel.AutomationSecurity = 3   # msoAutomationSecurityForceDisable
    $excel.EnableEvents = $false
    foreach ($p in $Paths) {
        $full = (Resolve-Path -LiteralPath $p).Path
        # UpdateLinks = 0 (never), ReadOnly = false
        $wb = $excel.Workbooks.Open($full, 0, $false)
        try {
            $excel.CalculateFullRebuild()
            $wb.Save()
            Write-Output "recalculated: $full"
        }
        finally {
            $wb.Close($false)
            [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($wb)
        }
    }
}
finally {
    $excel.Quit()
    [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($excel)
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}
