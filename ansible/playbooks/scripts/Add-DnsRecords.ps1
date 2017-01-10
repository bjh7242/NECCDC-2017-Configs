# https://github.com/wumb0/ISTS-PS-Scripts/blob/master/resource/Add-DnsRecordsFromCSV.ps1 
# PTR records assume that the network is a /24

param (
    [Parameter(Mandatory=$true)][string]$FileName,
    [Parameter(Mandatory=$true)][int32]$TeamNumber,
    [switch]$CreatePtrs = $true
)

Import-Csv $FileName | % {
    $CreatedRevZone = $false
    $RevZoneName = $_.Address.split(".")[2] + "." + $_.Address.split(".")[1] + "." + $_.Address.split(".")[0] + ".in-addr.arpa"

    # If the user wants a reverse zone, create it on the first loop only
    if ($CreatePtrs -eq $true -and $CreatedRevZone -ne $true) {
        $NetworkId = $_.Address.split(".")[0] + "." + $_.Address.split(".")[1] + "." + $_.Address.split(".")[2] + ".0/24"
        Add-DnsServerPrimaryZone -NetworkId "$NetworkId" -ReplicationScope Domain
        $CreatedRevZone = $true
    }

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
    if ($CreatePtrs -eq $true) {
        # Add-DnsServerResourceRecordPtr -name "134" -ZoneName "164.168.192.in-addr.arpa" -PtrDomainName "dc.team0.ccdc"
        Add-DnsServerResourceRecordPtr -name $_.Address.split(".")[3] -ZoneName $RevZoneName -PtrDomainName $fqdn
    }
}

