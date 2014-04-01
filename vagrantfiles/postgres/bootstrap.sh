#!/usr/bin/env bash

yum -y install postgresql-server python vim-enhanced emacs elinks gcc gcc-c++ java java-devel make
service postgresql initdb
service postgresql start
