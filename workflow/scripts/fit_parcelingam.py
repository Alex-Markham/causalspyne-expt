import numpy as np
from lingam import BottomUpParceLiNGAM

# Load the dataset
dataset = np.loadtxt(str(snakemake.input.dataset), delimiter=",")[1:]

# Run algorithm
model = BottomUpParceLiNGAM()
model.fit(dataset)

# Format output
nested_list = model.causal_order_
flat_list = [
    item
    for sublist in nested_list
    for item in (sublist if isinstance(sublist, list) else [sublist])
]

graph = model.adjacency_matrix_.astype(bool)  # NOT SURE THIS IS A PAG!

# save outputs
np.savetxt(snakemake.output["pag"], graph, delimiter=",", fmt="%d")
np.savetxt(snakemake.output["causal_order"], flat_list, delimiter=",", fmt="%d")
