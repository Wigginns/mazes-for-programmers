clean:
	rm -rf build/ dist/ *.egg-info/ src/*/__pycache__ src/mazesforprogrammers/*/__pycache__ tests/*/__pycache__ lint.html

install:
	pip install -e ./

test:
	pytest

lint:
	flake8 --max-line-length=120 tests/ src/