# Draw phylogenetic tree of all species
## `src`
- `get_daphnia_query.py`
- `blast_vs_dapfnia.sh`
- `concat_fasta.py`
- `make_all_tree.sh`
- `rm_procambarus.R`

## pipeline
```bash
mkdir -p tree_all/blst tree_all/concatnated_fasta tree_all/aln tree_all/out
python3 tree_all/src/get_daphnia_query.py -i tree_all/orthologous_groups -o tree_all/daphina_query_seq.fa
qsub tree_all/src/blast_vs_dapfnia.sh

mkdir tree_all/blst/unused_species
mv tree_all/blst/daphnia_procambarus_virginalis_longest_ens.blastp tree_all/blst/unused_species/daphnia_procambarus_virginalis_longest_ens.blastp  # low BUSCO
mv tree_all/blst/daphnia_chionoecetes_opilio_longest_ncbi.blastp tree_all/blst/unused_species/daphnia_chionoecetes_opilio_longest_ncbi.blastp  # low BUSCO

python3 tree_all/src/concat_fasta.py -f seq -b tree_all/blst --identity 40 -o tree_all/concatnated_fasta
qsub tree_all/src/make_all_tree.sh

Rscript tree_all/src/rm_procambarus.R
```
