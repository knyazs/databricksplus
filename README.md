# Databricks Plus

This package serves as a wrapper to simplifies use of existing as well as add some new Databricks functionalities.

# Build

Building wheel: py setup.py bdist_wheel

# Usage

Install whl file on databricks cluster, import it: 

import dbxplus
from dbxplus import repo, batch, workspace

and use function of choice:

print(dbxplus.repo.getCurrentBranch())