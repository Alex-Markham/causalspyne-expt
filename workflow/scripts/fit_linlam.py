import pickle

import numpy as np
from causallearn.search.HiddenCausal.GIN.GIN import GIN
from causalspyne.utils_causallearn_g2ancestral import get_causalearn_order

# Load the dataset
dataset = np.loadtxt(str(snakemake.input.dataset), delimiter=",")[1:]
with open(snakemake.input["node_names"], "rb") as inp:
    node_names = pickle.load(inp)

# Run LiNLAM algorithm
graph, latent_causal_order = GIN(dataset)

obs_causal_order, order_latent = get_causalearn_order(graph, node_names)
obs_causal_order = [
    int(x_str[1:]) for x_str in obs_causal_order
]  # strip X and convert to int for labels like "X1"


# save outputs
np.savetxt(snakemake.output["graph"], graph.graph, delimiter=",", fmt="%d")
np.savetxt(snakemake.output["causal_order"], obs_causal_order, delimiter=",", fmt="%d")
