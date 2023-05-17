library(conflicted)
library(tidyverse)
library(phytools)


# with_P_vir -------------------------------------------------------------------
tr = ape::read.tree("results_iqtree/run.nex.treefile")

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


# without_P_vir ----------------------------------------------------------------
tr_no_pvir = ape::drop.tip(tr, "Pvir")
tr_ultra_no_pvir = ape::drop.tip(tr_ultra, "Pvir")


# write_newick -----------------------------------------------------------------
ape::write.tree(tr, file="results_iqtree/iqtree.nwk")
ape::write.tree(tre_no_pvir, file="results_iqtree/iqtree_noPvir.nwk")
ape::write.tree(tr_ultra, file="results_iqtree/ultrametric_iqtree.nwk")
ape::write.tree(tr_ultra_no_pvir, file="results_iqtree/ultrametric_iqtree_noPvir.nwk")
