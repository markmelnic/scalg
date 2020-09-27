import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import unittest
from scalg.scalg import score_columns

DATA = [
    [2016, 21999, 62000, 181],
    [2013, 21540, 89000, 223],
    [2015, 18900, 100000, 223],
    [2013, 24200, 115527, 223],
    [2016, 24990, 47300, 223],
]


class SEC(unittest.TestCase):
    def test_score_columns(self):
        score_columns(DATA, [1, 3], [1, 0, 0, 1])
