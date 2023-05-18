#$ -S /bin/bash
#$ -cwd
#$ -o cafe5/
#$ -e cafe5/
#$ -l medium
#$ -l s_vmem=128G
#$ -l mem_req=128G

module load singularity

singularity exec /usr/local/biotools/c/cafe:5.0.0--h2e03b76_0 cafe5 \
	-i cafe5/Orthologs.GeneCount.Filtered.tsv \
	-t cafe5/ultrametric_iqtree.nwk \
	-o cafe5/results \
	-k 3
