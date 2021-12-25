#!/bin/env bash

set -euo pipefail

find . -name "*.sh" -not -path "*/.venv/*" -exec shellcheck -o all --severity style -x {} +

if [[ "${CI:=}" == "true" ]]; then
  black . --check --diff
else
  black .
fi

flake8 .

if [[ "${CI:=}" == "true" ]]; then
  isort . --check-only --diff
else
  isort .
fi

mypy webup
mypy tests

yamllint --strict .
