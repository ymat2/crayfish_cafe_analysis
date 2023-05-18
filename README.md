# Crayfish CAFE Analysis
Source codes for estimating the evolution of gene family in Decapoda including *Procambarus clakii* .

## Requirements
- Unix-like environment
  - Development env.: MacOS Ventura 13
  - Production env.: [Nig supercomputer](https://sc.ddbj.nig.ac.jp/en/) CentOS 7
- R (>=4.2.0)
- python3 (>=3.9.0)
- BLAST
- [MAFFT](https://mafft.cbrc.jp/alignment/software/) (>=7.0)
- [trimAl](http://trimal.cgenomics.org/trimal) (>=1.2.0)
- [iqtree](http://www.iqtree.org) (>=1.6.12)
- [CAFE5](https://github.com/hahnlab/CAFE5)


## `src/`
- `blast_array.sh`
:	conduct `blastp` against the fly genes

- `blast2table`
:	classify the genes of each species into orthologous groups based on fly genes

- `filter_table.py`
:	filter the single copy orthologs and the ortholog groups that cannot be used for CAFE analysis

- `OG_separator.py`
:	output the sequences to a FASTA file for each single copy orthologs

- `aln_trim_iqtree.sh`
:	align the sequences, trim the gaps, and infer the ML tree using the single copy orthologs

- `phylo.R`
: prepare ultrametric tree for CAFE analysis

- `make_nexus.py`
:	write nexus file used in `iqtree`

- `run_cafe5.sh`
:	conduct `CAFE5` analysis

```bash
mkdir -p blst out tree/sco
qsub blast_array.sh
python3 src/blast2table.py -i blst -o out
python3 src/filter_table.py
python3 src/OG_separater.py -f seq -l out/SingleCopyOrthologs.txt -p tree/sco
qsub src/aln_trim_iqtree.sh
Rscript src/phylo.R ?
```
