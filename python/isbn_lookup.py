#!/usr/bin/env python
#
# Uses the REST API of ISBNdb.com to get book information
# using the ISBN. Each book's information is saved in a
# JSON file with the ISBN in the file name. Requires a
# file with the isbn of each book, one per line.
#
# Usage: ./isbn_lookup.py <isbn list>

import local_settings
import urllib
from sys import argv
import json


web_key = local_settings.ISBNDB_KEY
url_format = "http://isbndb.com/api/v2/json/{0}/book/{1}"
input_filename = argv[1]


def get_book_url(isbn):
    return url_format.format(web_key, isbn)


with open(input_filename, "r") as input_file:
    for line in input_file:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        tokens = line.split()
        isbn = tokens[0]
        if not isbn:
            continue
        webcontent = urllib.urlopen(get_book_url(isbn))
        webtext = webcontent.read()
        if not webtext:
            continue

        with open("{0}.json".format(isbn), "w") as output:
            output.write(webtext)
