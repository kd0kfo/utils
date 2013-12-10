#!/usr/bin/env python
#
# Takes a list of file sizes and adds them.
# Returns the results in bytes.

from sys import argv, stdin, stdout
from getopt import getopt

KNOWN_UNITS = {"k": 1024, "m": 1048576, "g": 1073741824, "t": 1099511627776}


def print_usage():
    from os.path import basename
    print("Usage: {0} [-h] [-i FILE] [-o FILE] [--output_utils CHAR]"
          .format(basename(argv[0])))
    print("Options:")
    print("-i, --input FILE\t\tInput file to be read (Default: Standard Input)")
    print("-o, --output FILE\t\tOutput file to be used"
          " (Default: Standard Output)")
    print("    --output_units CHAR\t\tUnits to be used (case insensitive)."
          " Options are K, M, G and T (Default: none)")
    

def get_conversion_factor(units):
    if not units in KNOWN_UNITS:
        raise Exception("Unkown Units: {0}".format(units))

    return KNOWN_UNITS[units]


infile = stdin
outfile = stdout
output_factor = 1

short_opts = "hi:o:"
long_opts = ["help", "input=", "output=", "output_units="]

(opts, args) = getopt(argv[1:], short_opts, long_opts)

for (opt, optargs) in opts:
    while opt[0] == '-':
        opt = opt[1:]

    if opt in ["h", "help"]:
        print_usage()
        exit(0)
    elif opt in ["i", "input"]:
        infile = open(optargs, "r")
    elif opt in ["o", "output"]:
        outfile = open(optargs, "w")
    elif opt == "output_units":
        output_factor = get_conversion_factor(optargs.lower())

total_in_bytes = 0.0
for line in infile:
    val = line.strip()

    # If it's already a number, i.e. no units attached,
    # simply add and continue
    if val.isdigit():
        total_in_bytes += float(val)
        continue

    # Get units and convert number to bytes
    unit = val[-1].lower()
    val = float(val[0:-1])

    factor = get_conversion_factor(unit)

    total_in_bytes += factor*val

print(total_in_bytes / output_factor)
