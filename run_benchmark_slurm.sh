#!/bin/bash
uv run snakemake --profile ./slurm --keep-going --rerun-incomplete all
