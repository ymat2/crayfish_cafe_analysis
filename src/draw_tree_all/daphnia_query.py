import os
import glob

files = glob.glob("./tree_all/orthologous_groups/*.fa")

def daphnia_seq(f):
	seq_list = []
	gene_name = f.split("/")[-1].split("_")[0]
	with open(f) as fin:
		for line in fin:
			if line[0] == ">":
				seq_list.append([line.rstrip("\n")[1:],""])
			else:
				seq_list[-1][1] += line.rstrip("\n")
	for i in seq_list:
		if i[0] == "daphnia":
			return [gene_name, i[1]]

daphnia_seq_list = []
for f in files:
	daphnia_seq_list.append(daphnia_seq(f))

with open("./blst/daphnia_sco.fa", "w") as fout:
	for gn in daphnia_seq_list:
		fout.write(">"+gn[0]+"\n")
		fout.write(gn[1] + "\n")


