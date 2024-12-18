import sys
import pandas as pd
import numpy as np


if len(sys.argv) < 2:
    print("Usage: python table.py <csv_filename>")
    sys.exit(1)

# Get filename from command-line argument
csv_filename = sys.argv[1]
# Read the CSV file
df = pd.read_csv(csv_filename)

# Group by method and graph_size, calculate mean SHD
grouped = df.groupby(['method', 'graph_size'])['shd'].mean().unstack()



# Generate LaTeX table
latex_table = "\\begin{table}[h]\n\\centering\n\\begin{tabular}{|l|c|c|}\n\\hline\n"
latex_table += "Method & Small & Medium \\\\\n\\hline\n"
for method in ['standard', 'child']:
    small = grouped.loc[method, 'small']
    medium = grouped.loc[method, 'medium']
    latex_table += f"{method.capitalize()} & {small:.4f} & {medium:.4f} \\\\\n"
latex_table += "\\hline\n\\end{tabular}\n"
latex_table += "\\caption{Comparison of average SHD values for standard and child methods}\n"
latex_table += "\\label{tab:shd_comparison}\n\\end{table}"

print(latex_table)



# Create a markdown table
markdown_table = "| Method | Small | Medium |\n|--------|-------|--------|\n"
for method in ['standard', 'child']:
    small = grouped.loc[method, 'small']
    medium = grouped.loc[method, 'medium']
    markdown_table += f"| {method.capitalize()} | {small:.4f} | {medium:.4f} |\n"

print(markdown_table)
