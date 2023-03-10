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


dap_sco = {}
def add_dict(blst):
	sps = blst.split("/")[-1].split("_")
	sp = sps[1][0]+sps[2][:3]
	with open(blst) as fin:
		for line in fin:
			qry = line.split("\t")[0]
			db = line.split("\t")[1]
			idn = line.split("\t")[2]
			if float(idn) >= 60:
				if qry in dap_sco:
					if sp not in dap_sco[qry]:
						dap_sco[qry][sp] = db
					else:
						continue
				else:
					dap_sco[qry] = {}
					dap_sco[qry][sp] = db
blst = glob.glob("blst/daphnia_*.blastp")
for f in blst:
	add_dict(f)


for gn in dap_sco:
	with open("tree_all/ortholog_with_decapoda/"+gn+".fa", "w") as fout:
		with open("tree_all/orthologous_groups/"+gn+"_nogap.fa") as fin:
			for line in fin:
				fout.write(line)
		for sp in dap_sco[gn]:
			fout.write(">"+sp+"\n")
			fout.write(id2seq[dap_sco[gn][sp]]+"\n")
