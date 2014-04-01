#!/usr/bin/env bash

yum -y install postgresql-server
service postgresql initdb
service postgresql start
