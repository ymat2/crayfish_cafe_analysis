def main():
	new_line = []
	sco = []

	with open("cafe5/Orthologs.GeneCount.Filtered.tsv", "w") as fout:
		with open("out/Orthologs.GeneCount.tsv") as fin:
			for line in fin:
				if line.split("\t")[0] == "FBgn":
					sp_name = [shortName(sp) for sp in line.split("\t")[1:]]
					fout.write("Description\tID\t"+"\t".join(sp_name)+"\n")
				else:
					if over100(line) or allEqual(line):
						if isSCO(line):
							sco.append(line.split("\t")[0])
							continue
						else:
							continue
					else:
						fout.write(line.split("\t")[0]+"\t"+line)

	with open("out/SingleCopyOrthologs.txt", "w") as fout:
		with open("out/Orthologs.tsv") as fin:
			for line in fin:
				if line.split("\t")[0] == "FBgn":
					sp_name = [shortName(sp) for sp in line.split("\t")[1:]]
				else:
					id = line.split("\t")[0]
					gns = line.rstrip("\n").split("\t")[1:]
					if id in sco:
						fout.write(id+"\t"+"\t".join([sp+":"+gn for sp, gn in zip(sp_name, gns)])+"\n")


def over100(line):
	if all([int(c)<100 for c in line.rstrip("\n").split("\t")[1:]]):
		return False
	else:
		return True

def allEqual(line):
	if len(set(line.rstrip("\n").split("\t")[1:])) == 1:
		return True
	else:
		return False

def isSCO(line):
	if list(set(line.rstrip("\n").split("\t")[1:])) == ["1"]:
		return True
	else:
		return False

def shortName(sp):
	tabs = sp.split("_")
	sname = tabs[0][0].upper()+tabs[1][:3]
	return sname


if __name__ == "__main__":
	main()
