#!/usr/bin/env python

from sys import argv
import yaml

EXCLUDED_KEYS = ("sources",)
VISIBILY_IDENTIFYABLE = ("age", "gender", "race")
PERCENT_FMT = "'%s': %s"

def toplist_string(oldlist):
    newlist = []
    for category in sorted(oldlist.keys(), reverse=True):
        for pair in oldlist[category]:
            newlist.append(PERCENT_FMT % (pair[0].capitalize(), pair[1]))
    return ", ".join(newlist)


def vi_string(data):
    vi = dict([(key, data[key]) for key in data if key in VISIBILY_IDENTIFYABLE])
    return ", ".join([PERCENT_FMT % (key.capitalize(), vi[key][0] ) for key in sorted(vi.keys())])
        

args = argv[1:]
if not args:
    print("Missing input file.")
    exit(1)

yamldata = yaml.load(open(args[0], "r").read())

excluded = {}
for removethis in EXCLUDED_KEYS:
    if removethis in yamldata:
        excluded[removethis] = yamldata.pop(removethis)

for key in yamldata:
    strval = yamldata[key]
    intval = int(strval.replace("%", ""))
    yamldata[key] = (strval, intval)

percents = {}
for category in yamldata:
    percent = yamldata[category][1]
    val = (category, yamldata[category][0])
    if not percent in percents:
        percents[percent] = [val]
    else:
        percents[percent].append(val)

majority_list = dict([(percent, percents[percent]) for percent in percents if percent > 50])
toplist = dict([(key, majority_list[key]) for key in  sorted(majority_list.keys(), reverse=True)[0:5]])

print("Out of %d criteria ..." % len(yamldata))
print("Was in the majority (>= 50%%) in %d categories" % len(majority_list))
print("Top %d criteria are %s" % (len(toplist), toplist_string(toplist)))
print("Visibly Identifiable criteria are %s" % vi_string(yamldata))
print("")
print("Raw Percentages:")
for category in sorted(yamldata.keys()):
    print("%s: %s" % (category.capitalize(), yamldata[category][0]))

if "sources" in excluded:
    print("")
    print("Sources:")
    for source in excluded["sources"]:
        print(source)
