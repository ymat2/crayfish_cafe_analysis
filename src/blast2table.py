import os
import glob

flygn = {}  # flygn[sp_name] = {dict_sp}
gnlst = []  # list of fly genes that have orthologs

def add_dict(path_):
	with open(path_) as fin:
	
		sp_name = path_.lstrip("blst/fly_").split(".")[0]
		flygn[sp_name] = {}  # flygn[sp_name][fly_gene] = [sp_genes]
	
		for line in fin:
			qseq = line.split("\t")[0]
			sseq = line.split("\t")[1]
			
			if sseq not in flygn[sp_name]:
				flygn[sp_name][sseq] = [qseq]
				gnlst.append(sseq)
			else:
				flygn[sp_name][sseq] += [qseq]
				gnlst.append(sseq)


blast_files = glob.glob("blst/fly_*.blastp")

for f in blast_files:
	add_dict(f)

with open("out/Orthologs.tsv", "w") as fout:
	fout.write("FBgn\t"+"\t".join([sp for sp in flygn])+"\n")
	for gn in list(set(gnlst)):
		fout.write(gn)
		for sp in flygn:
			if gn in flygn[sp]:
				fout.write("\t"+",".join(list(set(flygn[sp][gn]))))
			else:
				fout.write("\t")
		fout.write("\n")

with open("out/Orthologs.GeneCount.tsv", "w") as fout:
	fout.write("FBgn\t"+"\t".join([sp for sp in flygn])+"\n")
	for gn in list(set(gnlst)):
		fout.write(gn)
		for sp in flygn:
			if gn in flygn[sp]:
				fout.write("\t"+str(len(set(flygn[sp][gn]))))
			else:
				fout.write("\t0")
		fout.write("\n")

