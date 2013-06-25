#!/usr/bin/env python
#
# This is a very simple script to check on the success of jenkins
# builds. It will collect all of the project names. Then using that
# list, it will check to see if the status is "SUCCESS". If any
# project is NOT "SUCCESS", it will return 1. Otherwise it will 
# return 0.
#
# If a hostname/port is different from localhost/8080, update
# the variable JENKINS_ADDR below.

from jenkinsapi.jenkins import Jenkins

JENKINS_ADDR = 'http://localhost:8080'

J = Jenkins(JENKINS_ADDR)
have_failed_project = False
for key in J.keys():
    last_build = J[key].get_last_build()
    last_build_status = last_build.get_status()
    print("Status of {0}: {1}".format(key,last_build_status))
    if last_build_status != "SUCCESS":
        have_failed_project = True
    

if have_failed_project:
    exit(1)
