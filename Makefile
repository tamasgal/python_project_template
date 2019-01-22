PKGNAME=foo

default: install

install: 
	pip install .

install-dev:
	pip install -e .

clean:
	python setup.py clean --all

test: 
	py.test --junitxml=./reports/junit.xml -o junit_suite_name=$(PKGNAME) $(PKGNAME)

test-cov:
	py.test --cov ./ --cov-report term-missing --cov-report xml:reports/coverage.xml --cov-report html:reports/coverage $(PKGNAME)

test-loop: 
	py.test $(PKGNAME)
	ptw --ext=.py,.pyx --ignore=doc $(PKGNAME)

flake8: 
	py.test --flake8

pep8: flake8

docstyle: 
	py.test --docstyle

lint: 
	py.test --pylint

dependencies:
	pip install -Ur requirements.txt

yapf:
	yapf -i -r $(PKGNAME)
	yapf -i setup.py

.PHONY: install install-dev clean test test-cov test-loop flake8 pep8 docstyle lint dependencies yapf
