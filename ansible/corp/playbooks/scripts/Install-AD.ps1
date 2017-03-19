#
# Windows PowerShell script for AD DS Deployment
#
param([string]$DomainName, [string]$NetBiosName, [string]$ADPassword)

Add-WindowsFeature AD-Domain-Services,RSAT-AD-PowerShell,RSAT-AD-AdminCenter
$password = ConvertTo-SecureString "$ADPassword" -asplaintext -force

Import-Module ADDSDeployment
Install-ADDSForest `
-SafeModeAdministratorPassword $password `
-CreateDnsDelegation:$false `
-DatabasePath "C:\Windows\NTDS" `
-DomainMode "Win2012" `
-DomainName "$DomainName" `
-DomainNetbiosName "$NetBiosName" `
-ForestMode "Win2012" `
-InstallDns:$true `
-LogPath "C:\Windows\NTDS" `
-NoRebootOnCompletion:$false `
-SysvolPath "C:\Windows\SYSVOL" `
-Force:$true
