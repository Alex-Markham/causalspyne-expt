from causalspyne.ancestral_shd import structural_hamming_distance
import numpy as np
import pandas as pd


# snakemake input
true_dag = np.loadtxt(str(snakemake.input.true_dag), delimiter=",", skiprows=1)
hidden_nodes = np.loadtxt(str(snakemake.input.hidden_nodes), delimiter=",")
if hidden_nodes.ndim == 1:
    hidden_nodes = hidden_nodes.tolist()
else:
    hidden_nodes = hidden_nodes[None].tolist()

est_pag = np.loadtxt(str(snakemake.input.est_pag), delimiter=",")

# find true PAG and compute SHD
shd = structural_hamming_distance(true_dag, hidden_nodes, est_pag)

shd_df = pd.DataFrame(
    {
        "alg": [snakemake.wildcards["alg"]],
        "method": [snakemake.wildcards["method"]],
        "graph_size": [snakemake.wildcards["graph_size"]],
        "samp_size": [snakemake.wildcards["samp_size"]],
        "seed": [snakemake.wildcards["seed"]],
        "shd": [shd],
        "dag_size": [len(true_dag)],
        "num_hidden": [len(hidden_nodes)],
    }
)

# output
shd_df.to_csv(snakemake.output["shd"], index=False)
