import os
import glob
import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--fasta")
	parser.add_argument("-l", "--list_sco")
	parser.add_argument("-p", "--path_sco")
	args = parser.parse_args()

	sep_og(args.fasta, args.list_sco, args.path_sco)


def sep_og(fasta_dir, sco_list, sco_path):
	id2seq = fasta2dict(fasta_dir)

	with open("out/SingleCopyOrthologs.txt") as fin:
		for line in fin:
			write_sco(sco_path, line, id2seq)


def fasta2dict(dir):
	seq_list = []
	seq_dict = {}

	fasta = glob.glob(dir+"/*.pep")
	for f in fasta:
		with open(f) as fin:
			for line in fin:
				if line[0] == ">":
					seq_list.append([line.rstrip("\n")[1:], ""])
				else:
					seq_list[-1][1] += line.rstrip("\n")
	for sblst in seq_list:
		seq_dict[sblst[0]] = sblst[1]

	return seq_dict


def write_sco(pth, line, dct):
	fbgn = line.rstrip("\n").split("\t")[0]
	genes = line.rstrip("\n").split("\t")[1:]
	with open(pth+"/"+fbgn+".fa", "w") as f:
		f.write(">fly32\n")
		f.write(dct[fbgn]+"\n")
		for id in genes:
			sname = id.split(":")[0]
			gn = id.split(":")[1]
			f.write(">"+sname+"\n")
			f.write(dct[gn]+"\n")


if __name__ == "__main__":
	main()
