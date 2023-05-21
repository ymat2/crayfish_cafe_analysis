import os
import glob
import argparse


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--fasta_dir")
	parser.add_argument("-b", "--blast_dir")
	parser.add_argument("--identity", type=int, default=30)
	parser.add_argument("-o", "--outdir")
	args = parser.parse_args()

	id2seq = {}
	fasta_files = glob.glob(args.fasta_dir+"/*.pep")
	for f in fasta_files:
		fasta2dict(id2seq, f)

	dap_sco = {}
	blast_files = glob.glob(args.blast_dir+"/daphnia_*.blastp")
	for f in blast_files:
		blast2sco(dap_sco, f, args.identity)

	for gn in dap_sco:
		concat_fasta(id2seq, dap_sco, gn, args.outdir)


def fasta2dict(dct, pth):
	with open(pth) as fin:
		gn = ""
		for line in fin:
			if line[0] == ">":
				gn = line.rstrip("\n")[1:]
				dct[gn] = ""
			else:
				dct[gn] += line.rstrip("\n")

#fasta = glob.glob("seq/*.pep")
#for f in fasta:
#	with open(f) as fin:
#		for line in fin:
#			if line[0] == ">":
#				seq_list.append([line.rstrip("\n")[1:], ""])
#			else:
#				seq_list[-1][1] += line.rstrip("\n")
#for sblst in seq_list:
#	id2seq[sblst[0]] = sblst[1]


def blast2sco(dct, pth, p_idnt):
	sp_short_name = pth.split("/")[-1].split("_")
	sp_short_name = sp_short_name[1][0]+sp_short_name[2][:3]

	with open(pth) as fin:
		for line in fin:
			qry = line.split("\t")[0]
			db = line.split("\t")[1]
			idn = line.split("\t")[2]
			if float(idn) >= p_idnt:
				if qry in dct:
					if sp_short_name not in dct[qry]:
						dct[qry][sp_short_name] = db
					else:
						continue
				else:
					dct[qry] = {}
					dct[qry][sp_short_name] = db


def concat_fasta(seq_dct, sco_dct, gn, pth):
	with open(pth+"/"+gn+".fa", "w") as fout:
		with open("tree_all/orthologous_groups/"+gn+"_nogap.fa") as fin:
			for line in fin:
				fout.write(line)
		for sp in sco_dct[gn]:
			fout.write(">"+sp+"\n")
			fout.write(seq_dct[sco_dct[gn][sp]]+"\n")


if __name__ == "__main__":
	main()
