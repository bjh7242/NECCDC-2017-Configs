#!/bin/bash
# This will join Ubuntu 12.04 hosts to the domain
# ./join.sh $TEAM_NUMBER

sudo ntpdate 10.0.$1.40

apt-get update
apt-get install winbind samba smbfs smbclient krb5-user libpam-winbind -y
cat <<EOF > /etc/samba/smb.conf
[global]
    workgroup = F-SPORTS$1
    security = ads
    realm = F-SPORTS$1.CO
    domain master = no
    local master = no
    preferred master = no
    idmap backend = tdb
    idmap uid = 10000-99999
    idmap gid = 10000-99999
    winbind enum users = yes
    winbind enum groups = yes
    winbind use default domain = yes
    winbind nested groups = yes
    winbind refresh tickets = yes
    template homedir = /home/%D/%U
    template shell = /bin/bash
    client use spnego = yes
    client ntlmv2 auth = yes
    encrypt passwords = yes
    restrict anonymous = 2
    log file = /var/log/samba/log.%m
    max log size = 50
    winbind offline logon = true
EOF
service smbd restart
service winbind restart
net ads join -U Administrator
pam-auth-update
sed -i 's/passwd.*/passwd:         compat winbind/g' /etc/nsswitch.conf
sed -i 's/group.*/group:          compat winbind/g' /etc/nsswitch.conf
sed -i 's/shadow.*/shadow:         compat winbind/g' /etc/nsswitch.conf
echo "session required			pam_mkhomedir.so skel=/etc/skel umask=0022" >> /etc/pam.d/common-account
service smbd restart
service winbind restart
echo 'Done!'
