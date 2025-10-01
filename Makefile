#* Variables
SHELL := /usr/bin/env bash
PYTHON := python
PYTHONPATH := `pwd`
VENV_DIR := .venv

#* Installation and Environment Setup
.PHONY: check-uv
check-uv:
	@if ! command -v uv &> /dev/null; then \
		echo "uv could not be found. Please install it first. See https://astral.sh/uv"; \
		exit 1; \
	fi

.PHONY: venv
venv: check-uv
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Creating virtual environment in $(VENV_DIR)..."; \
		uv venv $(VENV_DIR) -p $(PYTHON); \
	else \
		echo "Virtual environment $(VENV_DIR) already exists."; \
	fi

.PHONY: compile-reqs
compile-reqs: check-uv pyproject.toml
	@echo "Compiling dependencies to requirements.txt..."
	uv pip compile pyproject.toml --all-extras --no-header --no-annotate --output-file requirements.txt

.PHONY: install
install: venv compile-reqs
	@echo "Syncing dependencies from requirements.txt..."
	uv pip sync requirements.txt
	@echo "Installing local package in editable mode..."
	uv pip install -e .[mcp]
	@echo "Attempting to install mypy types..."
	-uv run -- mypy --install-types --non-interactive ./

.PHONY: pre-commit-install
pre-commit-install: check-uv
	@echo "Installing pre-commit hooks..."
	uv run -- pre-commit install

#* Formatters
.PHONY: codestyle
codestyle: check-uv
	@echo "Running formatters..."
	uv run -- pyupgrade --exit-zero-even-if-changed --py310-plus mh_operator/*.py mh_operator/utils/*.py tests/*.py
	uv run -- isort --settings-path pyproject.toml ./
	uv run -- black --config pyproject.toml ./

.PHONY: formatting
formatting: codestyle

#* Linting
.PHONY: test
test: check-uv
	@echo "Running tests..."
	PYTHONPATH=$(PYTHONPATH) uv run -- pytest -c pyproject.toml --cov-report=html --cov=mh_operator tests/
	@echo "Generating coverage badge..."
	uv run -- coverage-badge -o assets/images/coverage.svg -f

.PHONY: check-codestyle
check-codestyle: check-uv
	@echo "Checking code style..."
	uv run -- isort --diff --check-only --settings-path pyproject.toml ./
	uv run -- black --diff --check --config pyproject.toml ./
	uv run -- darglint --verbosity 2 mh_operator tests

.PHONY: mypy
mypy: check-uv
	@echo "Running mypy type checks..."
	-uv run -- mypy --config-file pyproject.toml ./

.PHONY: check-safety
check-safety: check-uv
	@echo "Running safety checks..."
	# Check installed packages for known vulnerabilities
	-uv run -- safety check --full-report
	# Check installed packages consistency
	uv pip check
	# Run bandit security linter
	uv run -- bandit -ll --recursive mh_operator tests

.PHONY: lint
lint: test check-codestyle mypy check-safety

#* Cleaning
.PHONY: pycache-remove
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

.PHONY: dsstore-remove
dsstore-remove:
	find . | grep -E ".DS_Store" | xargs rm -rf

.PHONY: mypycache-remove
mypycache-remove:
	find . | grep -E ".mypy_cache" | xargs rm -rf

.PHONY: ipynbcheckpoints-remove
ipynbcheckpoints-remove:
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf

.PHONY: pytestcache-remove
pytestcache-remove:
	find . | grep -E ".pytest_cache" | xargs rm -rf

.PHONY: build-remove
build-remove:
	rm -rf build/

.PHONY: venv-remove
venv-remove:
	rm -rf $(VENV_DIR)

.PHONY: reqs-remove
reqs-remove:
	rm -f requirements.txt requirements.lock # Remove generated req files

.PHONY: cleanup
cleanup: pycache-remove dsstore-remove mypycache-remove ipynbcheckpoints-remove pytestcache-remove venv-remove reqs-remove

.PHONY: clean
clean: cleanup build-remove
	rm -rf dist *.egg-info .coverage coverage.xml htmlcov assets/images/coverage.svg
