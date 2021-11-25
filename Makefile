build:
	py -m build

clean:
	rm -rf build/ dist/ *.egg-info/ src/*/__pycache__ src/mazesforprogrammers/*/__pycache__ tests/*/__pycache__ lint.html

install:
	pip install -e ./

test: lint-warn
	pytest

lint:
	flake8  tests src --max-line-length=120 --statistics

lint-warn:
	flake8  tests src --max-line-length=120 --exit-zero --statistics