# pip install uv
# uv will be responsible for updating all dependencies in the benchmark, the uv.lock file need to be pushed each time
uv sync   # ensures my environment matches the uv.lock file
uv lock --upgrade-package causalSpyne  # <package> does not have to be in pip, this is specified in pyproject.toml
# e.g. uv lock --upgrade-package pyqt6-qt6==6.7.1 to downgrade 6.8.0 to 6.7.1 to avoid platform
# consistency problems.
# [tool.uv.sources]
# causalspyne = { git = "https://github.com/marrlab/causalspyne" }
snakemake all # don't use this
uv run snakemake all   # this does not require installation of snakemake, uv will create a temporary virtural environment
#uv add numpy will add new packages
#uv add causaulspyne@git.come

# final results live in the "results" directory
# in the workflow diretory you can find the snakefile
