

install: 
	pip3 install flake8
	pip3 install mypy

run:
	python3 a_maze_ing.py config.txt
	
debug:
	python3 a_maze_ing.py config.txt

clean:
	rm -f  __pycache__ .mypy_cache

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict

.PHONY: install run debug clean lint lint-strict
