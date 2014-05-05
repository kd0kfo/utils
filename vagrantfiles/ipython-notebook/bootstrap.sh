#!/usr/bin/env bash

yum -y install python python-devel python-setuptools python-matplotlib python-gtkextra vim-enhanced emacs elinks gcc gcc-c++ make git subversion blas-devel lapack-devel freetype-devel

easy_install pip

cd
git clone https://github.com/ipython/ipython.git
cd ipython
git checkout rel-1.2.1
pip install $PWD

pip install --upgrade numpy
pip install scipy
pip install Cython
pip install jinja2
pip install tornado
pip install pygments

cd
git clone https://github.com/zeromq/pyzmq.git
cd pyzmq
pip install $PWD


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
