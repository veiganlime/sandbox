$data = Get-Content -Path "json_list/list.json" | ConvertFrom-Json


$today = (Get-Date).ToString("yyyy-MM-dd")


foreach ($item in @($data)) {
    if ($item.Fälligkeitsdatum -eq $today) {
        Write-Output "Die Berechtigung von $($item.User) wird entfernt!"
        
       
        $data = $data | Where-Object { $_.ID -ne $item.ID }
    }
}

$data | ConvertTo-Json -Depth 10 | Set-Content -Path "json_list/list.json"