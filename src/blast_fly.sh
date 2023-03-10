#$ -S /bin/bash
#$ -cwd
#$ -o /dev/null

# makeblastdb -in seq/fly32_longest.pep -out blst/fly32_longest.pep -dbtype prot -hash_index
blastp -outfmt "6 qseqid sseqid pident qcovs evalue" -evalue 1e-4 -db blst/fly32_longest.pep -query seq/fly32_longest.pep -out blst/fly32_longest.blastp
