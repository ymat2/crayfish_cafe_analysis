import os
import glob
import argparse


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--indir")
	parser.add_argument("-o", "--outfile")
	args = parser.parse_args()

	blast_files = glob.glob(args.indir+"/*.fa")
	daphnia_query_list = []
	for f in blast_files:
		daphnia_query_list.append(daphnia_seq(f))
	write_query(daphnia_query_list, args.outfile)


def daphnia_seq(pth):
	seq_list = []
	gene_name = pth.split("/")[-1].split("_")[0]
	with open(pth) as fin:
		for line in fin:
			if line[0] == ">":
				seq_list.append([line.rstrip("\n")[1:],""])
			else:
				seq_list[-1][1] += line.rstrip("\n")
	for i in seq_list:
		if i[0] == "daphnia":
			return [gene_name, i[1]]

def write_query(lst, f):
	with open(f, "w") as fout:
		for gn in lst:
			gene_name, seq = gn[0], gn[1]
			fout.write(">"+gene_name+"\n")
			fout.write(seq + "\n")


if __name__ == "__main__":
	main()
