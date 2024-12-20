import numpy as np
from causallearn.search.HiddenCausal.GIN.GIN import GIN

# Load the dataset
dataset = np.loadtxt(str(snakemake.input.dataset), delimiter=",")[1:]

# Run LiNLAM algorithm
graph, latent_causal_order = GIN(dataset)

# causal order of labels of observed nodes
causal_order = graph.get_causal_ordering()
node_map = graph.get_node_map()
obs_causal_order = [node_map[node] for node in causal_order]


# save outputs
np.savetxt(snakemake.output["graph"], graph.graph, delimiter=",", fmt="%d")
np.savetxt(snakemake.output["causal_order"], obs_causal_order, delimiter=",", fmt="%d")
