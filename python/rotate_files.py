#!/usr/bin/env python

from sys import argv
from glob import glob
from os.path import isfile
from shutil import move

NEW_FILENAME_FORMAT = "%s.%d"
EXISTS_EXCEPT_FORMAT = "File already exists. Attepted to move %s to %s"

args = argv[1:]

if not args:
    print("Usage: rotate_files.py <filename>")
    exit(1)

basefilename = args[0]

files = {}

for fn in glob("%s.*" % basefilename):
    idx = fn.rfind(".")
    idstring = fn[idx + 1:]
    filenumber = int(idstring)
    files[filenumber] = fn

for idx in sorted(files.keys(), reverse=True):
    newfilename = NEW_FILENAME_FORMAT % (basefilename, idx + 1)
    if isfile(newfilename):
        raise Exception(EXISTS_EXCEPT_FORMAT % (files[idx], newfilename))
    move(files[idx], newfilename)

newfilename = NEW_FILENAME_FORMAT % (basefilename, 1)
if isfile(newfilename):
    raise Exception(EXISTS_EXCEPT_FORMAT % (basefilename, newfilename))
move(basefilename, newfilename)
