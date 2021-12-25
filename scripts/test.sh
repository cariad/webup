#!/bin/env bash

set -euo pipefail

rm -rf docs
pdoc webup --output-directory docs --edit-url webup=https://github.com/cariad/webup/blob/main/webup/
touch docs/.nojekyll

pytest -vv
