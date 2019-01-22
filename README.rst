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

Installing
----------

Install it with::

    make install

Testing
-------

Run the tests with::

    make test
