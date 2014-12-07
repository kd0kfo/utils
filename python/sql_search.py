#!/usr/bin/env python

from sys import argv, stdout, stderr
from os.path import isfile
import argparse
import sqlite3

def search(args):
    if not args.db:
        raise Exception("No database defined.")
    if not isfile(args.db):
        raise Exception("No such database: %s" % args.db)
    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("select * from %s where %s = :query " % (args.table, args.column), {"query": " ".join(args.query)})

    row = cursor.fetchone()
    while row:
        for key in row.keys():
            print("%s: %s" % (key, row[key]))
        print("")
        row = cursor.fetchone()
    

parser = argparse.ArgumentParser(description="Quick Command Line SQLite3 tool")

parser.add_argument("db")

subparsers = parser.add_subparsers(help="Command to run")

subparser = subparsers.add_parser("search", help="Search for rows containing search strings in specified columns")
subparser.add_argument("table", type=str, help="Table Name")
subparser.add_argument("column", type=str, help="Column to search")
subparser.add_argument("query", type=str, nargs="+", help="String to find in column")
subparser.set_defaults(func=search)

args = parser.parse_args()
args.func(args)
