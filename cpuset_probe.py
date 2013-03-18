#!/usr/bin/env python

import os
import os.path as OP

def parse_cpus(cpufilename):
    retval = []
    with open(cpufilename,"r") as cpufile:
        for line in cpufile:
            tokens = line.strip().split(",")
            for token in tokens:
                if not "-" in token:
                    retval.append(int(token))
                else:
                    (start,end) = token.split("-")
                    retval += list(range(int(start),int(end)+1))
    return retval

def get_core_info(directory,query = None,free_list = None):
    cpuset_name = directory
    if cpuset_name == "/dev/cpuset":
        cpuset_name = "root"
    if "/dev/cpuset/" in cpuset_name:
        cpuset_name = cpuset_name.replace("/dev/cpuset/","")
    for dirent in os.listdir(directory):
        entpath = OP.join(directory,dirent)
        if OP.isdir(entpath):
            get_core_info(entpath,query,free_list)
        if dirent == "cpus":
            cpulist = parse_cpus(entpath)
            if not query:
                print("{0}: {1}".format(cpuset_name,cpulist))
            else:
                for q in query:
                    if q in cpulist:
                        print("{0} in {1}".format(q,cpuset_name))
            if cpuset_name != "root" and free_list:
                for core in cpulist:
                    if core in free_list:
                        free_list.remove(core)

if __name__ == "__main__":
    from sys import argv
    base_dir = "/dev/cpuset"
    query = None
    free_list = list(xrange(0,640))
    if len(argv) != 1:
        base_dir = argv[1]
    if len(argv) > 2:
        query = [int(i) for i in argv[2].split(',')]
    get_core_info(base_dir,query,free_list)
    if not free_list:
        print("No free cores")
    else:
        print("Free cores: {0}".format(", ".join([str(i) for i in free_list])))
