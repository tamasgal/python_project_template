A Python Project Template
=========================

Fork this project by clicking on the ``Fork`` button
(https://git.km3net.de/examples/python_project/forks/new) and afterwards
go to your project "settings/advanced" and click on
"Remove fork relationship".

Finally adjust the following files to your needs to get started with a
new Python project:

- ``requirements.txt`` - a list of Python packages needed for your software
- ``setup.py`` - this includes meta data for your package and is required
  for the ``pip install`` procedure. The most important things to change
  are listed at the top of the file.
- ``pyproject.toml`` - the project meta
- ``doc/conf.py`` - the documentation is configured in this file. Make sure
  to update the descriptions, title, ``import`` statements and so on.
  Add ``*.rst`` files inside the ``doc`` folder and include them in
  ``index.rst``. If you need more information, check out the Sphinx
  documentation.
- ``.gitlab-ci.yml`` - this file describes the stages and jobs you want to
  run on the KM3NeT continuous integration servers
- ``.coveragerc`` - contains a list of files to include or skip in the test
  coverage reports. Make sure to update the package name to match yours and
  exclude files which should not be tracked

Please note that the GitLab CI is using KM3NeT services (the GitLab runners and
the KM3NeT Docker registry), so make sure you update the settings to match
your environment if you want to use another GitLab server.

Don't write me a mail, please create an issue
(https://git.km3net.de/examples/python_project/issues) if you have any
questions, feedback or feature requests. Merge requests are welcome!

**Tamás Gál**

Features of this Template
-------------------------

- Automatic versioning using Git tags. Do ``git tag -a vX.Y.Z`` and
  push the tag with ``git push --tags``. It will include the version tag
  and also the development status within the version string automatically
- Package installation using ``pip install .`` (also via ``make install``)
- Test Suite infrastructure included
    - ``make test`` will run all tests
    - ``make test-loop`` will run the tests and watch files for changes to rerun
      them continuously
- Documentation infrastructure which includes automatic generation of HTML
  pages, publishing using **GitLab pages**  
  and the generation of a fully browsable coverage report under the following
  links:
    - Docs: https://examples.pages.km3net.de/python_project
    - Code coverage: https://examples.pages.km3net.de/python_project/coverage/
- Continuous Integration on the KM3NeT GitLab server

Installing the Python Package
-----------------------------

This Python package works out of the box. Explore it with with the following
commands.

Install it with::

    pip install /path/to/the/project/folder

or::

    make install

Run the tests with::

    make test


