# NECCDC-2017-Configs
Configs for NECCDC 2017

## PowerShell Remoting with Ansible
Run the following Commands on Windows 8+/2012+ to enable PS Remoting
```
PS> Enable-PSRemoting -Force -SkipNetworkProfileCheck
PS> Set-Item wsman:\localhost\client\trustedhosts *
C:\> winrm set winrm/config/client/auth @{Basic="true"}
C:\> winrm set winrm/config/service/auth @{Basic="true"}
C:\> winrm set winrm/config/service @{AllowUnencrypted="true"}
```

Enabling PS Remoting on Windows 7 
NOTE: 
* Windows 7 SP1 must be installed in order to upgrade PowerShell to v3.0 (to work with Ansible)
* .NET 4.0 must be installed to upgrade to PowerShell 3.0
* Administrator account must have a password AND the network profile for the firewall must NOT be set to public
```
C:\> reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f
C:\> shutdown -r -t 0
PS> Enable-PSRemoting -Force 
PS> Set-Item wsman:\localhost\client\trustedhosts *
C:\> winrm set winrm/config/client/auth @{Basic="true"}
C:\> winrm set winrm/config/service/auth @{Basic="true"}
C:\> winrm set winrm/config/service @{AllowUnencrypted="true"}
```


The Ansible Inventory file must have several parameters set for hosts to take advantage of the WinRM feature. 
Example:
```
[windows]
192.168.0.108   ansible_connection=winrm  ansible_user=admin    ansible_password=netsys ansible_port=5985
192.168.0.104   ansible_connection=winrm  ansible_user=admin    ansible_password=netsys ansible_port=5985 (optional if using HTTPS: ansible_winrm_server_cert_validation=ignore)
```


