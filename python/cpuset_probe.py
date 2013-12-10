#!/usr/bin/env python

import os
import os.path as OP

DEFAULT_CORE_COUNT = 640
DEFAULT_MEM_COUNT = 80

def parse_resource(resfilename):
    retval = []
    with open(resfilename,"r") as resfile:
        for line in resfile:
            line = line.strip()
            if not line:
                continue # If, for example, no cores are assigned in cpus, line will have only contained an EOL character
            tokens = line.split(",")
            for token in tokens:
                if not "-" in token:
                    retval.append(int(token))
                else:
                    (start,end) = token.split("-")
                    retval += list(range(int(start),int(end)+1))
    return retval

def get_res_info(directory,query = None,free_list = None, search_type = "cpus"):
    cpuset_name = directory
    if cpuset_name == "/dev/cpuset":
        cpuset_name = "root"
    if "/dev/cpuset/" in cpuset_name:
        cpuset_name = cpuset_name.replace("/dev/cpuset/","")
    for dirent in os.listdir(directory):
        entpath = OP.join(directory,dirent)
        if OP.isdir(entpath):
            get_res_info(entpath,query,free_list,search_type)
        if dirent == search_type:
            reslist = parse_resource(entpath)
            if not query:
                print("{0}: {1}".format(cpuset_name,reslist))
            else:
                for q in query:
                    if q in reslist:
                        print("{0} in {1}".format(q,cpuset_name))
            if cpuset_name != "root" and free_list:
                for core in reslist:
                    if core in free_list:
                        free_list.remove(core)

def print_usage():                        
    print("Usage: cpuset_probe.py [-d DIR] [-f] [-q LIST]")
    print("Options:")
    print("-d, --directory PATH\tDirectory of CPUSET files. Default: /dev/cpuset")
    print("-f, --free\t\tDisplay free cores.")
    print("-m, --mems\t\tSearch mems instead of cpus")
    print("-n, --num_cores INT\tNumber of cores. Default: {0}".format(core_count))
    print("-q, --query LIST\tLookup specific cores. Core list should be a commas separated list (no whitespace)")

if __name__ == "__main__":
    from sys import argv
    from getopt import getopt

    base_dir = "/dev/cpuset"
    core_count = DEFAULT_CORE_COUNT
    query = None
    free_list = None
    show_free_list = False
    search_type = "cpus"
    (opts,args) = getopt(argv[1:],"c:d:fhmq:",["core_count=","directory=","help","free","mems","query="])

    for (opt,optarg) in opts:
        while opt[0] == "-":
            opt = opt[1:]
        if opt in ["c", "core_count"]:
            core_count = int(optarg)
        elif opt in ["d","directory"]:
            base_dir = optarg
        elif opt in ["f","free"]:
            free_list = list(xrange(0,core_count))
            show_free_list = True
        elif opt in ["h", "help"]:
            print_usage()
            exit(0)
        elif opt in ["m","mems"]:
            search_type = "mems"
        elif opt in ["q","query"]:
            query = [int(i) for i in optarg.split(',')]
            

    get_res_info(base_dir,query,free_list,search_type)
    
    if show_free_list:
        if not free_list:
            print("No free {0}".format(search_type))
        else:
            print("Free cores: {0}".format(", ".join([str(i) for i in free_list])))
