param([string]$DomainName, [string]$DomainController, [string]$Username, [string]$Password, [string]$newname)

$secpass = ConvertTo-SecureString $Password -AsPlainText -Force
$cred = New-Object -typename System.Management.Automation.PSCredential -argumentlist $Username,$secpass

# you need to reboot after renaming and then join the host to a domain, so this won't work in the same script :(
#Rename-Computer -NewName $newname

# If PowerShell v4.0+
#Set-DnsClientServerAddress -ServerAddresses {$DomainController} -InterfaceAlias *

# Set DNS server to the DC in order to authenticate with that domain
Invoke-Command -ScriptBlock {
$interface = Get-WmiObject Win32_NetworkAdapterConfiguration -filter "ipenabled = 'true'"
$interface.SetDNSServerSearchOrder($DomainController)
}

Add-Computer -Credential $cred -DomainName $DomainName -Restart 
