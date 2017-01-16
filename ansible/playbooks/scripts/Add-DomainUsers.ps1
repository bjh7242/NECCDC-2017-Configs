$Users = Import-Csv -Path "C:\useraccounts.csv"

$domainname = (Get-ADDomain | select -expand dnsroot)

foreach ($User in $Users)
{
    $Displayname = $User.mlb_name
    $SAM = $User.bref_id
    $Description = $User.mlb_team_long
    $Password = $User.password
    $Email = $SAM + "@" + $domainname
    New-ADUser -Name "$Displayname" -DisplayName "$Displayname" -SamAccountName $SAM -Description "$Description" -AccountPassword (ConvertTo-SecureString $Password -AsPlainText -Force) -EmailAddress $Email -Enabled $true -ChangePasswordAtLogon $false -PasswordNeverExpires $true
}
