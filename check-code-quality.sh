#!/bin/bash

black --config .black.toml .
pylint --rcfile .pylintrc *.py type_hints/
flake8 --config .flake8
mypy . --exclude venv
ruff . --config ruff.toml --fix