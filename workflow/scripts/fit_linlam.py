from causallearn.search.HiddenCausal.GIN.GIN import GIN
import numpy as np

# Load the dataset
dataset = np.loadtxt(str(snakemake.input.dataset), delimiter=",")[1:]

# Run LiNLAM algorithm
graph, causal_order = GIN(dataset)

# convert graph to PAG now...
# pag = ...

# save graph
np.savetxt(snakemake.output["pag"], pag, delimiter=",", fmt="%d")
