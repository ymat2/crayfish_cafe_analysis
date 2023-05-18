if (!require("tidyverse", quietly = TRUE)) install.packages("tidyverse")
if (!require("phytools", quietly = TRUE)) install.packages("phytools")

library(conflicted)
library(tidyverse)
library(phytools)


# with_P_vir -------------------------------------------------------------------
tr = ape::read.tree("tree/run.nex.treefile")

mrca = ape::getMRCA(tr, tip=c("fly32", "Pcla"))
tr_ultra = ape::chronopl(
  tr,
  100000,
  age.min = 409.3,
  age.max = 536.3,
  node = mrca,
  S = 1,
  tol = 1e-8,
  CV = FALSE,
  eval.max = 500,
  iter.max = 500
  ) |>
  ape::drop.tip("fly32")
is.ultrametric(tr_ultra)


# write_newick -----------------------------------------------------------------
ape::write.tree(tr, file="tree/iqtree.nwk")
ape::write.tree(tr_ultra, file="cafe5/ultrametric_iqtree.nwk")
