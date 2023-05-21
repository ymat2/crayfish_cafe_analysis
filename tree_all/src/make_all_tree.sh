#$ -S /bin/bash
#$ -cwd
#$ -e tree_all/
#$ -o tree_all/
#$ -l medium
#$ -l s_vmem=64G
#$ -l mem_req=64G

ls tree_all/concatnated_fasta/* | xargs wc | awk '$1 == 86 { print $4 }' | cut -d / -f 3 | while read x; do  # if all species(n=43) exists
	singularity exec /usr/local/biotools/m/mafft:7.508--hec16e2b_0 mafft --auto tree_all/concatnated_fasta/$x > tree_all/aln/$x.maf
	singularity exec /usr/local/biotools/t/trimal:1.4.1--hc9558a2_4 trimal -in tree_all/aln/$x.maf -out tree_all/aln/$x.maf.trimed.fa -nogaps
done

python3 src/make_nexus.py -a tree_all/aln -o tree_all/run.nex -l 50
singularity exec /usr/local/biotools/i/iqtree:1.6.12--he513fc3_0 iqtree -sp tree_all/run.nex -nt 1 -bb 1000
