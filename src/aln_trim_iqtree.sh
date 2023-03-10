#$ -S /bin/bash
#$ -cwd
#$ -pe def_slot 4
#$ -l medium
#$ -l s_vmem=64G
#$ -l mem_req=64G

module load singularity

awk '{print($1)}' out/SingleCopyOrthologs.txt | while read x; do
	singularity exec /usr/local/biotools/m/mafft:7.508--hec16e2b_0 mafft --auto tree/sco/$x.fa > tree/sco/$x.maf.fa
	singularity exec /usr/local/biotools/t/trimal:1.4.1--hc9558a2_4 trimal -in tree/sco/$x.maf.fa -out tree/sco/$x.maf.trimed.fa -nogaps
done

python3 src/make_nexus.py tree/run.nex 50
singularity exec /usr/local/biotools/i/iqtree:1.6.9--he941832_0 iqtree -sp tree/run.nex -nt 4 -bb 1000
