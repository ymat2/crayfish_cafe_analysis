#$ -S /bin/bash
#$ -cwd
#$ -l medium
#$ -l s_vmem=64G
#$ -l mem_req=64G

#ls tree_all/ortholog_with_decapoda/* | xargs wc | awk '$1 == 90 { print $4 }' | cut -d / -f 3 | while read x; do
#	singularity exec /usr/local/biotools/m/mafft:7.508--hec16e2b_0 mafft --auto tree_all/ortholog_with_decapoda/$x > tree_all/aln2/$x.maf
#	singularity exec /usr/local/biotools/t/trimal:1.4.1--hc9558a2_4 trimal -in tree_all/aln2/$x.maf -out tree_all/aln2/$x.maf.trimed.fa -nogaps
#done

# python3 src/make_nexus.py tree_all/run2.nex 50
singularity exec /usr/local/biotools/i/iqtree:1.6.9--he941832_0 iqtree -sp tree_all/run2.nex -nt 1 -bb 1000
