from causalspyne.ancestral_shd import structural_hamming_distance
import numpy as np
import pandas as pd


# snakemake input
true_dag = np.loadtxt(str(snakemake.input.true_dag), delimiter=",", skiprows=1)
hidden_nodes = list(np.loadtxt(str(snakemake.input.hidden_nodes), delimiter=","))
est_pag = np.loadtxt(str(snakemake.input.est_pag), delimiter=",")

# find true PAG and compute SHD
shd = structural_hamming_distance(true_dag, hidden_nodes, est_pag)

shd_df = pd.DataFrame(
    {
        "method": [snakemake.wildcards["method"]],
        "samp_size": [snakemake.wildcards["samp_size"]],
        "seed": [snakemake.wildcards["seed"]],
        "shd": [shd],
    }
)

# output
shd_df.to_csv(snakemake.output["shd"], index=False)
