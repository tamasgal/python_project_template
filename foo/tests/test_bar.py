#!usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test_bar.py
from unittest import TestCase

from foo.bar import whats_the_meaning_of_life

__author__ = "Your Name"
__credits__ = []
__license__ = "MIT"
__maintainer__ = "Your Name"
__email__ = "yname@km3net.de"


class TestMeaningOfLife(TestCase):
    """Tests for the bar module"""

    def test_meaning_of_life(self):
        assert 42 == whats_the_meaning_of_life()

    def test_meaning_of_life_with_one_core(self):
        assert 42 == whats_the_meaning_of_life(n_cores=1)
