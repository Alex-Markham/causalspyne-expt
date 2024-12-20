import numpy as np
from causallearn.search.HiddenCausal.GIN.GIN import GIN
from causalspyne.utils_causallearn_g2ancestral import get_causal_order

# Load the dataset
dataset = np.loadtxt(str(snakemake.input.dataset), delimiter=",")[1:]

# Run LiNLAM algorithm
graph, latent_causal_order = GIN(dataset)

obs_causal_order, order_latent = get_causal_order(graph, node_names)


# save outputs
np.savetxt(snakemake.output["graph"], graph.graph, delimiter=",", fmt="%d")
np.savetxt(snakemake.output["causal_order"], obs_causal_order, delimiter=",", fmt="%d")
