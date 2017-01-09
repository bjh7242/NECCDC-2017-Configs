param([string]$DomainName, [string]$DomainController, [string]$Username, [string]$Password)

$secpass = ConvertTo-SecureString $Password -AsPlainText -Force
$cred = New-Object -typename System.Management.Automation.PSCredential -argumentlist $Username,$secpass

# If PowerShell v4.0+
#Set-DnsClientServerAddress -ServerAddresses {$DomainController} -InterfaceAlias *

# Set DNS server to the DC in order to authenticate with that domain
Invoke-Command -ScriptBlock {
$interface = Get-WmiObject Win32_NetworkAdapterConfiguration -filter "ipenabled = 'true'"
$interface.SetDNSServerSearchOrder($DomainController)
}

Add-Computer -Credential $cred -DomainName $DomainName -Restart 
