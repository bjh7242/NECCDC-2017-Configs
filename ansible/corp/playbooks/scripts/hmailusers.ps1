param([string]$dnsroot)
#$domain = Get-ADDomain 
# 
# The base DN for accounts (DC=example,DC=com): 
# 
#$dn = 'DC=f-sports1,DC=co'
# 
# The domain used for emails (example.com): 
# 
#$dnsroot = 'f-sports1.co'
# 
# Enter your hMailServer password here: 
# 
$hmail_password = "Netsys123$" 
# 
# Max size of account mailbox (in megs): 
# 
$hmail_maxsize = 10000 
# 
Import-Csv -Path C:\useraccounts.csv | % {
 $hm = New-Object -ComObject hMailServer.Application 
 $hm.Authenticate("Administrator", $hmail_password) | Out-Null 
 $hmdom = $hm.Domains.ItemByName($dnsroot) 
 $hmact = $hmdom.Accounts.Add() 
 # Filling attributes for the email account based on current information, including AD integration for the password 
 $hmact.Address = $_.bref_id + '@' + "$dnsroot"
 $hmact.Active = $true 
 $hmact.IsAD = $true 
 #$hmact.MaxSize = $hmail_maxsize 
 $hmact.ADDomain = $dnsroot
 $hmact.ADUsername = $_.bref_id
 #$hmact.PersonFirstName = $fn 
 #$hmact.PersonLastName = $ln 
 $hmact
 $hmact.save() 
 Write-Host $user.bref_id
 Write-Host "Done." 
}
