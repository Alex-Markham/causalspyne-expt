#!/bin/bash
#SBATCH --partition=cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --nice=10000
#SBATCH -t 24:00:00
#SBATCH -c 2
#SBATCH --mem=10G

uv run snakemake --profile "~/caucalspyne-expt/slurm" --keep-going --keep-incomplete
