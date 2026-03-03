
PYTHON      := python3
MAIN        := a_maze_ing.py
CONFIG      := config.txt
PIP         := pip3
VENV        := .venv
PKG_NAME    := mazegen
PKG_VERSION := 1.0.0

all: install

install: 
	$(PIP) install flake8
	$(PIP) install mypy

run:
	$(PYTHON) $(MAIN) $(CONFIG)

debug:
	$(PYTHON) -m pdb $(MAIN) $(CONFIG)

clean:
	find . -type d -name "__pycache__"   -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache"   -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info"    -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc"         -delete                        2>/dev/null || true
	rm -rf dist/ build/
	@echo "Clean done."

lint:
	flake8 .
	mypy . \
	    --warn-return-any \
	    --warn-unused-ignores \
	    --ignore-missing-imports \
	    --disallow-untyped-defs \
	    --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict

help:
	@echo ""
	@echo "A-Maze-ing — available make targets:"
	@echo ""
	@echo "  install      Install project dependencies (flake8, mypy, build)"
	@echo "  run          Run the maze generator with default config"
	@echo "  debug        Run under Python pdb debugger"
	@echo "  lint         Run flake8 + mypy (standard flags)"
	@echo "  lint-strict  Run flake8 + mypy --strict"
	@echo "  test         Run pytest unit tests"
	@echo "  build-pkg    Build the reusable mazegen pip package"
	@echo "  clean        Remove caches and build artefacts"
	@echo ""

.PHONY: install run debug clean lint lint-strict help
