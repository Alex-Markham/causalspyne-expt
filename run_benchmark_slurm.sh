#!/bin/bash
#SBATCH --partition=cpu_p
export logdir="slurm_logs/"
echo "slurm logs going into ${logdir}"
uv run snakemake --profile "config.yaml" --keep-going --keep-incomplete --notemp
