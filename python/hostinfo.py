#!/usr/bin/env python


def load_properties(filename):
    retval = {}

    with open(filename, "r") as inputfile:
        for line in inputfile:
            line = line.strip()
            if not line or line[0] == '#':
                continue

            tokens = line.split("=")
            if len(tokens) == 1:
                retval[tokens[0].strip()] = None
            else:
                retval[tokens[0].strip()] = "=".join(tokens[1:]).strip()

    return retval

if __name__ == "__main__":
    from sys import argv

    args = argv[1:]
    if not args:
        filename = "/etc/hostinfo"
    else:
        filename = args[0]

    properties = load_properties(filename)
    for key in properties:
        print("{0} => {1}".format(key, properties[key]))
