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
from sys import argv
from getopt import getopt

DEFAULT_JENKINS_ADDR = 'http://localhost:8080'

jenkins_addr = DEFAULT_JENKINS_ADDR
ignore_list = []


(opts, args) = getopt(argv[1:], "a:hi:", ["address", "help", "ignore"])

for (opt, optarg) in opts:
    while opt[0] == '-':
        opt = opt[1:]
    if opt in ["a", "address"]:
        jenkins_addr = optarg
    elif opt in ["h", "help"]:
        print("jenkins_checker.py [-a ADDRESS] [-i IGNORE,LIST]")
        print("Options:")
        print("-a, --address ADDRESS: Address to be used to query jenkins")
        print("-i, --ignore LIST: Comma separated list of project names"
              "to ignore")
        exit(0)
    elif opt in ["i", "ignore"]:
        ignore_list += optarg.split(',')


J = Jenkins(jenkins_addr)
failed_projects = []
for key in J.keys():
    last_build = J[key].get_last_build()
    last_build_status = last_build.get_status()
    print("Status of {0}: {1}".format(key, last_build_status))
    if last_build_status != "SUCCESS" and key not in ignore_list:
        failed_projects.append(key)


if failed_projects:
    from sys import stderr
    stderr.write("The following builds failed: {0}\n"
                 .format(", ".join(failed_projects)))
    exit(1)
