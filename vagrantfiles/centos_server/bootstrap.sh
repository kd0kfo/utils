#!/usr/bin/env bash

yum -y install postgresql-server httpd perl php python python-setuptools python-pip vim-enhanced emacs elinks gcc gcc-c++ java java-devel make git subversion

chkconfig postgresql on
service postgresql initdb
service postgresql start

chkconfig httpd on
service httpd start

CREATETAG=$(echo This machine was setup using vagrant on $(date +"%Y-%m-%d %H:%M"))
CREATEFILE=/etc/hostinfo.created
echo $CREATETAG > $CREATEFILE
echo >> $CREATEFILE
echo >> $CREATEFILE
echo It started with these packages >> $CREATEFILE
rpm -qa >> $CREATEFILE

echo $CREATETAG > /etc/motd
echo >> /etc/motd
echo Very convenient. >> /etc/motd
echo Then again it is Linux. >> /etc/motd
echo So no surprise. w00t! >> /etc/motd
