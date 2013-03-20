#!/usr/bin/env python

import os
import os.path as OP

DEFAULT_CORE_COUNT = 640

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

def print_usage():                        
    print("Usage: cpuset_probe.py [-d DIR] [-f] [-q LIST]")
    print("Options:")
    print("-n, --num_cores INT\tNumber of cores. Default: {0}".format(core_count))
    print("-d, --directory PATH\tDirectory of CPUSET files. Default: /dev/cpuset")
    print("-f, --free\t\tDisplay free cores.")
    print("-q, --query LIST\tLookup specific cores. Core list should be a commas separated list (no whitespace)")

if __name__ == "__main__":
    from sys import argv
    from getopt import getopt

    base_dir = "/dev/cpuset"
    core_count = DEFAULT_CORE_COUNT
    query = None
    free_list = None
    show_free_list = False
    (opts,args) = getopt(argv[1:],"d:hq:",["directory=","help","free","query="])

    for (opt,optarg) in opts:
        while opt[0] == "-":
            opt = opt[1:]
        if opt in ["d","directory"]:
            base_dir = optarg
        elif opt in ["f","free"]:
            free_list = list(xrange(0,core_count))
            show_free_list = True
        elif opt in ["h", "help"]:
            print_usage()
            exit(0)
        elif opt in ["q","query"]:
            query = [int(i) for i in optarg.split(',')]
            

    get_core_info(base_dir,query,free_list)
    
    if show_free_list:
        if not free_list:
            print("No free cores")
        else:
            print("Free cores: {0}".format(", ".join([str(i) for i in free_list])))
