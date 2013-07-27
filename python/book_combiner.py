#!/usr/bin/env python
#
# Combines book data produced by isbn_lookup.py. Catalog is saved
# as a pickle file.
#
# Usage: book_combiner.py <dataset 1> <dataset 2> ...
#
# Each dataset name is a file called <dataset>.dat, which is a
# list of isbns, and a directory called <dataset> which has a
# json file for each isbn, produced by isbn_lookup.py
#

from sys import argv
import json
import pickle

catalog_list = argv[1:]

isbn_map = {}
author_map = {}
title_map = {}


def get_json_data(isbn, directory=None):
    import os.path as OP
    if directory:
        input_filename = OP.join(directory, isbn)
    else:
        input_filename = isbn
    input_filename += ".json"
    data = json.loads(open(input_filename, "r").read())

    if "error" in data:
        return data

    return data["data"][0]


for catalog in catalog_list:
    with open("{0}.dat".format(catalog), "r") as isbns:
        for line in isbns:
            if not line:
                continue
            isbn = line.strip()
            if not isbn or isbn[0] == "#":
                continue

            try:
                data = get_json_data(isbn, catalog)
            except Exception as e:
                print("No data for {0}".format(isbn))
                raise e

            if "error" in data:
                print("Invalid ISBN: {0}".format(data["error"]))
                continue

            title = data["title"]
            if not title in title_map:
                title_map[title] = [data]
            else:
                title_map[title].append(data)

            for author in data["author_data"]:
                if not author["name"] in author_map:
                    author_map[author["name"]] = [data]
                else:
                    author_map[author["name"]].append(data)

            for isbn_type in ('isbn10', 'isbn13'):
                if data[isbn_type]:
                    isbn_map[data[isbn_type]] = data


catalog_data = {"isbn": isbn_map, "titles": title_map, "authors": author_map}

pickle.dump(catalog_data, open("catalog.pickle", "wb"))
