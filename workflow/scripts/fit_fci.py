import numpy as np
from causallearn.search.ConstraintBased.FCI import fci

# Load the dataset
dataset = np.loadtxt(str(snakemake.input.dataset), delimiter=",")[1:]

# Run FCI algorithm
g, edges = fci(dataset)
pag = g.graph
causal_order = g.get_causal_ordering()

# save outputs
np.savetxt(snakemake.output["pag"], pag, delimiter=",", fmt="%d")
np.savetxt(snakemake.output["causal_order"], causal_order, delimiter=",", fmt="%d")
