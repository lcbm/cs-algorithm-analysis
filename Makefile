PYTHONPATH := .
VENV := venv
SCRIPTS := scripts
REQUIREMENTS := -r requirements.txt

BIN := $(VENV)/bin
PIP := $(BIN)/pip
PYTHON := $(BIN)/python
PRE_COMMIT := $(BIN)/pre-commit


run:
	$(PYTHON) $(SCRIPTS)/main.py

bootstrap: venv \
	requirements \
	pre-commit-hooks

venv:
	python3 -m venv $(VENV)

requirements:
	$(PIP) install $(REQUIREMENTS)

pre-commit-hooks:
	$(PRE_COMMIT) install

clean:
	@find . -type d -name '__pycache__' -exec rm -rf {} +

clean-all: clean
	@rm -r $(VENV)
