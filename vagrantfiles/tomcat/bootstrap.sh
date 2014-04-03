#!/usr/bin/env bash

#Prereqs
yum -y install java-1.7.0-openjdk java-1.7.0-openjdk-devel make git gcc gcc-c++ vim-enhanced emacs python

# Tomcat
export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk.x86_64
export CATALINA_HOME=/opt/tomcat
export CATALINA_BASE=/opt/tomcat

cd /opt
wget http://mirrors.ibiblio.org/apache/tomcat/tomcat-7/v7.0.53/bin/apache-tomcat-7.0.53.tar.gz
tar xzvf apache-tomcat-7.0.53.tar.gz
ln -s apache-tomcat-7.0.53 /opt/tomcat
cd /opt/tomcat/bin
tar xvfz commons-daemon-native.tar.gz
cd commons-daemon-1.0.15-native-src/unix
./configure
make
cp jsvc ../..
cd ../..

# Deploy wars if available
cd /vagrant
if [[ -d webapps ]];then
	cd webapps/
	cp *.war $CATALINA_HOME/webapps/
	cd /vagrant
fi

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
