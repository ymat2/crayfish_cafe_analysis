import os
import glob
import argparse


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--indir")
	parser.add_argument("-o", "--outdir")
	args = parser.parse_args()

	blast_files = glob.glob(args.indir + "/fly_*.blastp")
	fly_gn_dct = {}  # flygn[sp_name] = {dict_sp}
	for f in blast_files:
		add_dict(f, fly_gn_dct)

	fly_gn_lst = []  # list of fly genes that have orthologs
	for d in fly_gn_dct:
		for gn in fly_gn_dct[d]:
			fly_gn_lst.append(gn)

	write_table(args.outdir, fly_gn_dct, fly_gn_lst)
	write_count(args.outdir, fly_gn_dct, fly_gn_lst)


def add_dict(pth, dct):
	with open(pth) as fin:

		sp_name = pth.lstrip("blst/fly_").split(".")[0]
		dct[sp_name] = {}  # dct[sp_name][fly_gene] = [sp_genes]

		for line in fin:
			qseq = line.split("\t")[0]
			sseq = line.split("\t")[1]

			if sseq not in dct[sp_name]:
				dct[sp_name][sseq] = [qseq]
			else:
				dct[sp_name][sseq] += [qseq]


def write_table(outdir, gndct, gnlst):
	with open(outdir+"/Orthologs.tsv", "w") as fout:
		fout.write("FBgn\t"+"\t".join([sp for sp in gndct])+"\n")
		for gn in list(set(gnlst)):
			fout.write(gn)
			for sp in gndct:
				if gn in gndct[sp]:
					fout.write("\t"+",".join(list(set(gndct[sp][gn]))))
				else:
					fout.write("\t")
			fout.write("\n")


def write_count(outdir, gndct, gnlst):
	with open(outdir+"/Orthologs.GeneCount.tsv", "w") as fout:
		fout.write("FBgn\t"+"\t".join([sp for sp in gndct])+"\n")
		for gn in list(set(gnlst)):
			fout.write(gn)
			for sp in gndct:
				if gn in gndct[sp]:
					fout.write("\t"+str(len(set(gndct[sp][gn]))))
				else:
					fout.write("\t0")
			fout.write("\n")


if __name__ == "__main__":
	main()
