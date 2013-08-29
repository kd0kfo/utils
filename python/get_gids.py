#!/usr/bin/env python

import grp
from sys import argv

if len(argv) == 1:
    print("./get_gids.py <user name>")
    exit(1)

username = argv[1]

for group in grp.getgrall():
    if username in group.gr_mem:
        print("{0}\t{1}".format(group.gr_gid, group.gr_name))
