$Users = Import-Csv -Path "C:\useraccounts.csv"
foreach ($User in $Users)
{
    $Displayname = $User.mlb_name
    $SAM = $User.bref_id
    $Description = $User.mlb_team_long
    $Password = $User.password
    New-ADUser -Name "$Displayname" -DisplayName "$Displayname" -SamAccountName $SAM -Description "$Description" -AccountPassword (ConvertTo-SecureString $Password -AsPlainText -Force) -Enabled $true -ChangePasswordAtLogon $false -PasswordNeverExpires $true
}
