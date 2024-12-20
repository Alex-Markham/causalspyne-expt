import pickle

import numpy as np
import pandas as pd
from causalspyne.ancestral_acc import ancestral_acc

# load inputs
with open(snakemake.input["true_dag"], "rb") as inp:
    true_dag = pickle.load(inp)
dataset = np.loadtxt(str(snakemake.input["pred_order"]), delimiter=",")

# evaluate
acc = ancestral_acc(true_dag, pred_order)

# save output
acc_df = pd.DataFrame(
    {
        "method": [snakemake.wildcards["method"]],
        "graph_size": [snakemake.wildcards["graph_size"]],
        "samp_size": [snakemake.wildcards["samp_size"]],
        "seed": [snakemake.wildcards["seed"]],
        "anc_acc": [acc],
        "dag_size": [len(true_dag)],
        "num_hidden": [len(hidden_nodes)],
    }
)

# output
acc_df.to_csv(snakemake.output["anc_acc"], index=False)
