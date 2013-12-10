#!/usr/bin/env python
#
# Displays the full path to a file or directory.
# If the file does not exist, or if the link is broken, and error message is
# displayed and the script exits with error code 1

import os.path
from sys import argv

filename = argv[1]
path = os.path.abspath(filename)
if not os.path.lexists(path):
    print("{0} was not found".format(filename))
    exit(1)

print(path)
