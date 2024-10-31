from causallearn.search.ConstraintBased.FCI import fci
import numpy as np

# Load the dataset
dataset = np.loadtxt(str(snakemake.input.dataset), delimiter=",")[1:]

# Run FCI algorithm
g, edges = fci(dataset)
pag = g.graph

# save pag
np.savetxt(snakemake.output["pag"], pag, delimiter=",", fmt="%d")
