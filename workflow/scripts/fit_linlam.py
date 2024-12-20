import numpy as np
from causallearn.search.HiddenCausal.GIN.GIN import GIN

# Load the dataset
dataset = np.loadtxt(str(snakemake.input.dataset), delimiter=",")[1:]

# Run LiNLAM algorithm
graph, causal_order = GIN(dataset)

# save outputs
np.savetxt(snakemake.output["graph"], graph.graph, delimiter=",", fmt="%d")
np.savetxt(snakemake.output["causal_order"], causal_order, delimiter=",", fmt="%d")
