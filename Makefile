#!/usr/bin/make

# These need to be at the top
PRESET_VARS := $(.VARIABLES)

# Project variables
PYTHON_VERSION_        := "3.11"
PYTHON                 := $(shell which python$(PYTHON_VERSION_))
PY_FILES               := $(shell find . -name '*.py' | grep -v "/.venv/" | grep -v "/jib-aoc/")
PY_FILES_EXT           := $(shell find . -name '*.py' | grep -v "/.venv/")
INSTALLED_PIP_PACKAGES := $(shell $(PYTHON) -m pip freeze)

.PHONY: all
all: check  # Normally this wouldn't be the default target, but since we're not really building anything here...

.PHONY: check
check: CHECK = --check  # set this so "format" checks but doesn't change the files
check: lint test  ## Check the code.

.PHONY: clean
clean:  ## Clean up.
	@find . -name "__pycache__" | grep -v "/.venv/" | xargs rm -rf
	@rm -rf .pytest_cache tests/.pytest_cache
	@rm -rf .mypy_cache
	@rm -rf .pytype

.PHONY: dep
dep: requirements.txt venv-check  ## Install requirements.
	$(PYTHON) -m pip install --quiet --upgrade pip setuptools wheel
	$(PYTHON) -m pip install --quiet --requirement requirements.txt

.PHONY: dep-base
dep-base: requirements.base.txt venv-check  ## Install base requirements.
	$(PYTHON) -m pip install --quiet --requirement requirements.base.txt

.PHONY: dep-dev
dep-dev: requirements.dev.txt venv-check  ## Install dev requirements.
	$(PYTHON) -m pip install --quiet --requirement requirements.dev.txt

.PHONY: format
format: dep-dev  ## Format the code.
	@$(PYTHON) -m black $(CHECK) $(PY_FILES)
	@$(PYTHON) -m isort $(CHECK) $(PY_FILES)

.PHONY: help
help:  ## Display this help.
	@grep -h -E '^[a-zA-Z0-9._-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'

.PHONY: lint
lint: dep-dev format  ## Lint the code.
	@$(PYTHON) -m pylint $(PY_FILES)
	@$(PYTHON) -m pydocstyle $(PY_FILES)
	@$(PYTHON) -m mypy --strict $(PY_FILES_EXT)
	@$(PYTHON) -m pytype --jobs=auto --keep-going $(PY_FILES_EXT)

requirements.txt: requirements.base.txt  ## Clean/update the virtual env and make a new requirements file.
	@$(MAKE) venv-clean  # This is not listed as a dependency because we don't want it to run unnecessarily.
	@$(MAKE) dep-base  # This is not listed as a dependency because we don't want it to run unnecessarily.
	$(PYTHON) -m pip freeze > $@

.PHONY: showvars
showvars:  ## Display variables available in the Makefile.
	$(foreach v, $(filter-out $(PRESET_VARS) PRESET_VARS,$(.VARIABLES)), $(info $(v) = $($(v))))

.PHONY: test
test:  ## Run unit tests.
	$(PYTHON) -m pytest --verbose --capture=no tests

.venv:
	@rm -rf .venv
	$(PYTHON) -m venv .venv

.PHONY: venv
venv: .venv  # Create a Python virtual environment.
	@printf "To activate the virtual environment:\n\n"
	@printf "source .venv/bin/activate\n"

.PHONY: venv-check
venv-check:  # Verify that we are in a virtual environment.
ifndef VIRTUAL_ENV
ifndef PYTHON_VERSION
	$(error this should only be executed in a Python virtual environment)
endif
endif

.PHONY: venv-clean
venv-clean: venv-check  ## Remove all packages from the virtual environment.
ifdef INSTALLED_PIP_PACKAGES
	-@$(PYTHON) -m pip uninstall --quiet --yes $(INSTALLED_PIP_PACKAGES)
	$(PYTHON) -m pip install --quiet --upgrade pip setuptools wheel
endif
