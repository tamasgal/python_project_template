A Python Project Template
=========================

Fork this project and adjust the following files to your needs to get started
with a new Python project:

- ``requirements.txt`` - a list of Python packages needed for your software
- ``setup.py`` - this includes meta data for your package and is required
  for the ``pip install`` procedure
- ``doc/conf.py`` - the documentation is configured in this file
- ``.gitlab-ci.yml`` - this file describes the stages and jobs you want to
  run on the KM3NeT continuous integration server
- ``.coveragerc`` - contains a list of files to include or skip. Make sure
  to update the package name to match yours

Note that the GitLab CI is using KM3NeT services (the GitLab runners and
the KM3NeT Docker registry), so make sure you update the settings to match
your environment.

Don't write me a mail, please create an issue
(https://git.km3net.de/examples/python_project/issues) if you have any
questions, feedback or feature request. Merge requests are welcome!

**Tamás Gál**

Features of this Template
=========================

- Package installation using ``pip install .`` (also via ``make install``)
- Test Suite infrastructure included
    - ``make test`` will run all tests
    - ``make test-loop`` will run the tests and watch files for changes to rerun
      them continuously
- Documentation infrastructure: ``cd doc && make html``
    - Docs: https://examples.pages.km3net.de/python_project
    - Code coverage: https://examples.pages.km3net.de/python_project/coverage/
- Continuous Integration on the KM3NeT GitLab server

Installing
----------

Install it with::

    make install

Testing
-------

Run the tests with::

    make test
