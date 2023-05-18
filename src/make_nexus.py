import os
import glob
import sys
import argparse
from Bio import SeqIO


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-a", "--alndir")
	parser.add_argument("-l", "--minlen", type=int)
	parser.add_argument("-o", "--outfile")
	args = parser.parse_args()

	fasta = glob.glob(args.alndir+"/*.maf.trimed.fa")
	write_nexus(args.outfile, fasta, args.minlen)


def len_seq(file):
	fas = SeqIO.parse(file, 'fasta')
	seq_length = [len(record.seq) for record in fas]
	return seq_length[0]


def write_nexus(pth, fs, l):
	with open(pth, "w") as fout:
		fout.write("#nexus\nbegin sets;\n")
		for i, f in enumerate(fs):
			if len_seq(f) > l:
				fout.write("\tcharset part"+str(i)+" = "+f+": ;\n")
		fout.write("end;\n")


if __name__ == "__main__":
	main()
