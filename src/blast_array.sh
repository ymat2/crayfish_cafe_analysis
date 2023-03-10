#$ -S /bin/bash
#$ -t 1-10:1
#$ -cwd
#$ -o /dev/null
seq_ids=(chionoecetes_opilio_longest_ncbi eriocheir_sinensis_longest_ncbi homarus_americanus_longest_ens penaeus_chinensis_longest_ncbi penaeus_japonicus_longest_ens penaeus_monodon_longest_ens penaeus_vannamei_longest_ens portunus_trituberculatus_longest_ens procambarus_clarkii_longest_ens procambarus_virginalis_longest_ens)
seq_id=${seq_ids[$SGE_TASK_ID-1]}

module load singularity

blastp \
	-evalue 1e-4\
	-max_target_seqs 1\
	-outfmt 6\
	-query seq/${seq_id}.pep\
	-db blst/fly32_longest.pep\
	-out blst/fly_${seq_id}.blastp
