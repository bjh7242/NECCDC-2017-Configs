# https://github.com/wumb0/ISTS-PS-Scripts/blob/master/resource/Add-DnsRecordsFromCSV.ps1 

param (
    [Parameter(Mandatory=$true)][string]$FileName,
    [Parameter(Mandatory=$true)][int32]$TeamNumber,
    [switch]$CreatePtrs = $true
)

Import-Csv $FileName | % {
    $fqdn = $_.Name.replace("teamX","team$TeamNumber")
    $name = $fqdn.split(".")[0]
    $domain_split = $fqdn.split(".")
    $domain = ($domain_split[1..($domain_split.length -1)] -join ".")
    $ip = $_.Address.replace("X", $TeamNumber)
    if ($_.Type -eq "A"){
        Add-DnsServerResourceRecordA -Name $name -IPv4Address $ip -ZoneName $domain -CreatePtr:$CreatePtrs
    }
    if ($_.Type -eq "MX"){
        Add-DnsServerResourceRecordMX -Name . -Preference 10 -MailExchange $fqdn -ZoneName $domain
    }
}

