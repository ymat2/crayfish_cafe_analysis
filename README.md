# Source codes for estimating the evolution of gene family in Decapoda
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

- `make_nexus.py`
:	write nexus file used in `iqtree`

- `run_cafe5.sh`
:	conduct `CAFE5` analysis
