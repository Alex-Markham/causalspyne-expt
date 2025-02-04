#!/bin/bash
#SBATCH --partition=cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --nice=10000
#SBATCH -t 24:00:00
#SBATCH -c 2
#SBATCH --mem=10G

export logdir="slurm_logs/"
echo "slurm logs going into ${logdir}"
uv run snakemake --profile "~/caucalspyne-expt/config.yaml" --keep-going --keep-incomplete --notemp
