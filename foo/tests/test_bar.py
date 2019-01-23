#!usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test_bar.py
from unittest import TestCase

from foo.bar import whats_the_meaning_of_life, calculate_mean

__author__ = "Your Name"
__credits__ = []
__license__ = "MIT"
__maintainer__ = "Jürgen"
__email__ = "yname@km3net.de"


class TestMeaningOfLife(TestCase):
    """Tests for the bar module"""

    def test_meaning_of_life(self):
        assert 42 == whats_the_meaning_of_life()

    def test_meaning_of_life_with_one_core(self):
        assert 42 == whats_the_meaning_of_life(n_cores=1)


class TestCalculateMean(TestCase):
    """Tests for the calculate_mean function"""

    def test_calculate_mean_of_a_single_number_returns_the_number_itself(self):
        assert 0 == calculate_mean([0])
        assert 1 == calculate_mean([1])
        assert 2 == calculate_mean([2])
        assert -1 == calculate_mean([-1])
        assert 1.5 == calculate_mean([1.5])

    def test_calculate_mean_returns_mean_of_a_list_of_numbers(self):
        assert 2 == calculate_mean([1, 2, 3])
        assert 3 == calculate_mean([1, 2, 3, 4, 5])

    def test_calculate_mean_returns_correct_value_for_negative_numbers(self):
        assert -3 == calculate_mean([-1, -2, -3, -4, -5])

    def test_calculate_mean_of_some_other_numbers(self):
        self.assertAlmostEqual(2.5, calculate_mean([1, 2, 3, 4]))
