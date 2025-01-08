import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

shd_results = pd.read_csv(snakemake.input["csv"])

plot = sns.catplot(
    data=shd_results,
    x="graph_size",
    y="shd",
    hue="method",
    log_scale=False,
    legend=True,
    palette="Set2",
    row="alg",
    kind="box",
)
plot.figure.savefig(snakemake.output[0])

# small = shd_results[shd_results["graph_size"] == "small"]
# small["dag_size"].mean()
# small["num_hidden"].mean()

# medium = shd_results[shd_results["graph_size"] == "medium"]
# medium["dag_size"].mean()
# medium["num_hidden"].mean()
