from causalspyne import gen_partially_observed
import numpy as np
import pandas as pd

# snakemake inputs
method = snakemake.wildcards["method"]
seed = int(snakemake.wildcards["seed"])
samp_size = int(snakemake.wildcards["samp_size"])
graph_size = snakemake.wildcards["graph_size"]

output_dir = snakemake.output["dataset"][:-8]

if method == "standard":
    percentile = [0, 0.1]
elif method == "child":
    percentile = [0.5, 1.0]

if graph_size == "small":
    num_micro, num_macro = 2, 3
    degree = 2
elif graph_size == "medium":
    num_micro, num_macro = 4, 5
    degree = 4
elif graph_size == "large":
    num_micro, num_macro = 8, 12
    degree = 5

# causalspyne data generation
arr_data, node_names = gen_partially_observed(
    size_micro_node_dag=num_micro,
    num_macro_nodes=num_macro,
    degree=degree,  # average vertex/node degree
    list_confounder2hide=percentile,  # choie of confounder to hide: percentile or index of all toplogically sorted confounders
    num_sample=samp_size,
    rng=np.random.default_rng(seed),
    output_dir=output_dir,
    graphviz=False,
    plot=False,
)


# outputs
data_df = pd.DataFrame(arr_data)
data_df.to_csv(snakemake.output["dataset"], index=False)
# `snakemake.output['dag']` and `snakemake.output['hidden_nodes']`
# saved automatically in call to `gen_partially_observed()`
