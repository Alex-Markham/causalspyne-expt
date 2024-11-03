import pandas as pd

# join results
eval_df = pd.concat([pd.read_csv(path) for path in snakemake.input])

# output
eval_df.to_csv(snakemake.output["csv"], index=False)
