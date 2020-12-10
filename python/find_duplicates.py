#!/usr/bin/env python3
#
# Searches through a directory and builds a list of md5 hashes. Then it can search through another directory and find files that are also in that directory.
#
# Usage: find_duplicates.py DIRECTORY - Search DIRECTORY and prints a map of hashes and paths as YAML
#        find_duplicates.py DIRECTORY DIRECTORY2 - Lists files in DIRECTORY2 that are also in DIRECTORY
#        find_duplicates.py YAMLFILE DIRECTORY - Lists files in DIRECTORY that are in the YAML file of hashes and paths.


from sys import argv
import os
import yaml
import hashlib

srcdir = argv[1]

def generate_hash_dict(srcdir):
    retval = {}
    for root, dirs, files in os.walk(srcdir, topdown = False):
        for name in files:
            path = os.path.join(root, name)
            h = hashlib.md5()
            h.update(open(path, "rb").read())
            digest = h.hexdigest()
            if digest not in retval.keys():
                retval[digest] = [path]
            else:
                retval[digest].append(path)
    return retval

def generate_duplicates(otherdir, hashdict):
    retval = []
    for root, dirs, files in os.walk(otherdir, topdown = False):
        for name in files:
            path = os.path.join(root, name)
            h = hashlib.md5()
            h.update(open(path, "rb").read())
            digest = h.hexdigest()
            if digest in hashdict.keys():
                retval.append(path)
    return retval

if ".yml" == srcdir[-4:]:
    hashes = yaml.load(open(srcdir).read())
else:
    hashes = generate_hash_dict(srcdir)

if len(argv) > 2:
    for f in generate_duplicates(argv[2], hashes):
        print(f)
else:
    print(yaml.dump(hashes))
