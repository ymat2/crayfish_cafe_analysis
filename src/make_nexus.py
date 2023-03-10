import os
import glob
import sys
from Bio import SeqIO

# fasta = glob.glob("tree/sco/*.maf.trimed.fa")
fasta = glob.glob("tree_all/aln2/*.maf.trimed.fa")

def len_seq(file):
	fas = SeqIO.parse(file, 'fasta')
	seq_length = [len(record.seq) for record in fas]
	return seq_length[0]

with open(sys.argv[1], "w") as fout:
	fout.write("#nexus\nbegin sets;\n")
	for i, f in enumerate(fasta):
		if len_seq(f) > int(sys.argv[2]):
			fout.write("\tcharset part"+str(i)+" = "+f+": ;\n")
	fout.write("end;\n")	
