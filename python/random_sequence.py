#!/usr/bin/env python

"""
This script generates random sequences.

Command line arguments:
-b, --bases STRING - String of characters to be used  (default: ATGC)
-n, --num_seqs INT - Number of sequences to be writen in the file (default: 1)
-o, --output FILENAME - String file name of output (default: standard output)
-s, --size INT  - Number of bases in the sequences (default: 1000000)

"""

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import random

default_bases = ['A','T','G','C']
		
def rand_seq(bases = default_bases, size = 1000000):
	seq = Seq("")
	rand_size = len(bases) - 1
	for i in range(0,size):
		seq += bases[random.randint(0,rand_size)]
	return seq



if __name__ == "__main__":
	from sys import argv,stdout
	from getopt import getopt

	bases = default_bases
	size = 1000000
	num_seqs = 1
	
	short_opts = "b:n:o:s:"
	long_opts = ["bases=","size=","num_seqs=","output="]
	output_filename = None

	(opts, args) = getopt(argv[1:],short_opts,long_opts)
	
	for (opt,optarg) in opts:
		while opt[0] == "-":
			opt = opt[1:]
		if opt in ["b","bases"]:
			bases = list(optarg)
		elif opt in ["s", "size"]:
			size = int(optarg)
		elif opt in ["o","output"]:
			output_filename = optarg
		elif opt in ["n","num_seqs"]:
			num_seqs = int(optarg)
		else:
			print("Unknown flag: %s" % opt)
			exit(1)
				
	output = stdout
	if output_filename:
		output = open(output_filename,"w")

	counter = 0
	while counter < num_seqs:
		seq = rand_seq(bases,size)
		rec = SeqRecord(seq)
		rec.id = "Random Sequence %s" % (counter+1)
		SeqIO.write(rec,output,"fasta")
		counter += 1
	
