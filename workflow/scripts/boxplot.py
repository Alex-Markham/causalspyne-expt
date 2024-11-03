import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


shd_results = pd.read_csv(snakemake.input["csv"])

plt.figure(figsize=(12, 6))
sns.boxplot(x="graph_size", y="shd", data=shd_results, hue="method")
plt.title("")
plt.xlabel("")
plt.ylabel("Structural Hamming Distance (SHD)")

plt.savefig(snakemake.output[0])

# small = shd_results[shd_results["graph_size"] == "small"]
# small["dag_size"].mean()
# small["num_hidden"].mean()

# medium = shd_results[shd_results["graph_size"] == "medium"]
# medium["dag_size"].mean()
# medium["num_hidden"].mean()
