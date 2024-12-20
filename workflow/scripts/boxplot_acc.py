import pandas as pd
import seaborn as sns

acc_results = pd.read_csv(snakemake.input["csv"])

plot = sns.catplot(
    data=acc_results,
    x="graph_size",
    y="anc_acc",
    hue="method",
    log_scale=True,
    legend=True,
    palette="Set2",
    row="alg",
    kind="box",
)
plot.figure.savefig(snakemake.output[0])
