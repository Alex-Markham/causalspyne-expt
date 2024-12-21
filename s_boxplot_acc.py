import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

acc_results = pd.read_csv("results/acc.csv")
fig, ax = plt.subplots()
plot = sns.catplot(
    data=acc_results,
    x="graph_size",
    y="anc_acc",
    hue="method",
    log_scale=False,
    legend=True,
    palette="Set2",
    row="alg",
    kind="box", # swarm
)
ax.ticklabel_format(style='sci', scilimits=(0,0), axis='both')
plt.ylim(0, 1)
plot.figure.savefig("acc.pdf")
