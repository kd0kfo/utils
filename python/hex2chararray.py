#!/usr/bin/env python
#
# Takes in a long hex string, such as one representing a hash, and returns the bytes represented as
# hexadecimal bytes in an array.
#
# Example:
# 1b826051506f463f07307598fcf12fd6
# would give
# 0x1b, 0x82, 0x60, 0x51, 0x50, 0x6f, 0x46, 0x3f, 0x07, 0x30, 0x75, 0x98, 0xfc, 0xf1, 0x2f, 0xd6

from sys import argv

s = argv[1]

t = []
for i in xrange(0,len(s),2):
    t.append(s[i:i+2])

print ", ".join("0x%0.2x" % int(e, 16) for e in t)
