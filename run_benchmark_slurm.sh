#!/bin/bash
export logdir="slurm_logs/"
echo "slurm logs going into ${logdir}"
snakemake --profile "config_slurm.yaml" --keep-going --keep-incomplete --notemp
