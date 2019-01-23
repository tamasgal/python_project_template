#!usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: bar.py
from __future__ import division
"""
The bar module.

"""

__author__ = "Jürgen"
__credits__ = ["The guy in your office", "Tom"]
__license__ = "MIT"
__maintainer__ = "Your Buddy"
__email__ = "yname@km3net.de"


def whats_the_meaning_of_life(n_cores=23):
    """Answers the question about the meaning of life.

    You don't even have to ask the question, it will figure it out for you.
    Don't use more cores than available to mankind.

    Parameters
    ----------
    n_cores: int [default: 23]
        The number of CPU cores to use.

    Returns
    -------
    int
        The type of the expected answer is of course an integer.
    """
    return 42


def calculate_mean(numbers):
    """Calculates the mean of a list of numbers

    Parameters
    ----------
    numbers: iterable[numbers]

    Returns
    -------
    number
    """
    return sum(numbers) / len(numbers)
