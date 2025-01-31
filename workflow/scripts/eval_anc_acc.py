import pickle

import numpy as np
import pandas as pd
from causalspyne.ancestral_acc import ancestral_acc

# load inputs
with open(snakemake.input["true_dag"], "rb") as inp:
    true_dag = pickle.load(inp)
pred_order = np.loadtxt(str(snakemake.input["pred_order"]), delimiter=",", dtype=int)
hidden_nodes = np.loadtxt(
    str(snakemake.input["hidden_nodes"]), delimiter=",", dtype=int
).tolist()

if type(hidden_nodes) is int:
    hidden_nodes = [hidden_nodes]

# evaluate
acc = ancestral_acc(true_dag, pred_order, hidden_nodes)

# save output
acc_df = pd.DataFrame(
    {
        "alg": [snakemake.wildcards["alg"]],
        "method": [snakemake.wildcards["method"]],
        "graph_size": [snakemake.wildcards["graph_size"]],
        "samp_size": [snakemake.wildcards["samp_size"]],
        "seed": [snakemake.wildcards["seed"]],
        "anc_acc": [acc],
        "dag_size": [len(pred_order)],
        "num_hidden": [len(hidden_nodes)],
    }
)

# output
acc_df.to_csv(snakemake.output["anc_acc"], index=False)
