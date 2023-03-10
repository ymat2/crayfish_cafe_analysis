#$ -S /bin/bash
#$ -cwd
#$ -o cafe5/noPvir/
#$ -e cafe5/noPvir/
#$ -l medium
#$ -l s_vmem=128G
#$ -l mem_req=128G

module load singularity

# cat cafe5/Orthologs.GeneCount.Filtered.tsv | cut -f 1-4,6-12 > cafe5/noPvir/Orthologs.GeneCount.noPvir.tsv

singularity exec /usr/local/biotools/c/cafe:5.0.0--h2e03b76_0 cafe5 \
	-i cafe5/noPvir/Orthologs.GeneCount.noPvir.tsv \
	-t cafe5/noPvir/ultrametric_iqtree_noPvir.nwk \
	-o cafe5/noPvir/results
	-k 3
