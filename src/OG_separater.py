import os
import glob


seq_list = []
id2seq = {}

fasta = glob.glob("seq/*.pep")
for f in fasta:
	with open(f) as fin:
		for line in fin:
			if line[0] == ">":
				seq_list.append([line.rstrip("\n")[1:], ""])
			else:
				seq_list[-1][1] += line.rstrip("\n")
for sblst in seq_list:
	id2seq[sblst[0]] = sblst[1]


with open("out/SingleCopyOrthologs.txt") as fin:
	for line in fin:
		fbgn = line.rstrip("\n").split("\t")[0]
		genes = line.rstrip("\n").split("\t")[1:]
		with open("tree/sco/"+fbgn+".fa", "w") as fout:
			fout.write(">fly32\n")
			fout.write(id2seq[fbgn]+"\n")
			for id in genes:
				sname = id.split(":")[0]
				gn = id.split(":")[1]
				fout.write(">"+sname+"\n")
				fout.write(id2seq[gn]+"\n")
			
