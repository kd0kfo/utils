#!/usr/bin/env python
#
# Looks up a book by author and/or title (logical OR not AND)
# using a catalog pickle file produced by book_combiner.py
#
# Usage: find_bookpy [-a author] [-t title] <catalog file>
#
# Note: May combine multiple authors and titles. Criteria
# will be combined using logical OR.

from getopt import getopt, GetoptError
from sys import argv
import pickle


def print_book(book):
    author_list = [author["name"].encode("UTF-8")
                   for author in book["author_data"]]
    print("{0} by {1}. ISBN: {2}. Dewey Decimal: {3}"
          .format(book["title"], " and ".join(author_list),
                  book["isbn10"], book["dewey_decimal"]))


(opts, args) = getopt(argv[1:], "a:t:", ["author=", "title="])

author_search = []
title_search = []

for (opt, optarg) in opts:
    while opt[0] == "-":
        opt = opt[1:]
    if opt in ["a", "author"]:
        author_search.append(optarg)
    elif opt in ["t", "title"]:
        title_search.append(optarg)

if not args:
    print("Catalog pickle needed.")
    exit(1)

pickle_filename = args[0]

catalog = pickle.load(open(pickle_filename, "rb"))

for author in author_search:
    found_author = False
    for book_author in catalog["authors"]:
        if author in book_author:
            for book in catalog["authors"][book_author]:
                print_book(book)
            found_author = True
    if not found_author:
        print("Author not found: {0}".format(author))


for title in title_search:
    found_title = False
    for book_title in catalog["titles"]:
        if title in book_title:
            for book in catalog["titles"][book_title]:
                print_book(book)
            found_title = True
    if not found_title:
        print("Title not found: {0}".format(author))
