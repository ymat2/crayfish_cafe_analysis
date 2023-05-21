if (!require("tidyverse", quietly = TRUE)) install.packages("tidyverse")
if (!require("phytools", quietly = TRUE)) install.packages("phytools")

library(conflicted)
library(tidyverse)
library(phytools)


# with_P_vir -------------------------------------------------------------------
tr = ape::read.tree("tree_all/run.nex.treefile") |>
  ape::drop.tip("procambaru")

# write_newick -----------------------------------------------------------------
ape::write.tree(tr, file="tree_all/out/iqtree_all.nwk")
