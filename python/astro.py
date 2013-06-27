#!/usr/bin/env python
#
# Script to do simple Astronomy calculations
#
# Requires a json file called "astro.json" with the following local information:
# "lat" - Latitude in radians
# "lon" - Longitude in radians
#
# Usage: ./astro.py <command> [options]

import ephem, json
from sys import argv

LAT = 0
LON = 0

with open("astro.json","r") as jsonf:
    init_data = json.loads(jsonf.read())
    LAT = init_data["lat"]
    LON = init_data["lon"]

def get_observer():
    o = ephem.Observer()
    o.lat = LAT
    o.lon = LON
    return o

def get_lst():
    o = get_observer()
    return o.sidereal_time()

cmd = argv[1]
cmd_args = argv[2:]

if cmd == "lst":
    lst = get_lst()
    print("{2} = {0:.2f} rad = {1:.2f}".format(float(lst),float(lst)*(180/ephem.pi),lst))
elif cmd == "ha":
    lst = float(get_lst())
    ra = float(cmd_args[0])
    ha = lst-ra
    print("{0}h = {1} rad = {2} deg".format(ha*(12/ephem.pi),ha,ha*(180/ephem.pi)))
elif cmd == "coords":
    from math import sin,cos,asin,acos
    lst = float(get_lst())
    ra = float(cmd_args[0])
    dec = float(cmd_args[1])
    ha = lst-ra
    sin_alt = sin(dec)*sin(LAT) + cos(dec)*cos(LAT)*cos(ha)
    alt = asin(sin_alt)
    cos_a = (sin(dec) - sin_alt*sin(LAT))/(cos(alt)*cos(LAT))
    a = acos(cos_a)
    az = a
    if ha > 0:
        az = 2*ephem.pi-a
    print("(az, alt) = ({0} rad, {1} rad)".format(az, alt))
    print("          = ({0} deg, {1} deg)".format(az*(180/ephem.pi),alt*(180/ephem.pi)))
