import numpy as np
from causallearn.search.ConstraintBased.FCI import fci

# Load the dataset
dataset = np.loadtxt(str(snakemake.input.dataset), delimiter=",")[1:]

# Run FCI algorithm
g, edges = fci(dataset)
pag = g.graph

# get labels of causal order of nodes
causal_order = g.get_causal_ordering()
node_map = g.get_node_map()
causal_order = [node_map[node] for node in causal_order]


# save outputs
np.savetxt(snakemake.output["pag"], pag, delimiter=",", fmt="%d")
np.savetxt(snakemake.output["causal_order"], causal_order, delimiter=",", fmt="%d")
