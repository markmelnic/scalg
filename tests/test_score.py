import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import unittest
from scalg.scalg import score

DATA = [
    [2016, 21999, 62000, 181],
    [2013, 21540, 89000, 223],
    [2015, 18900, 100000, 223],
    [2013, 24200, 115527, 223],
    [2016, 24990, 47300, 223],
]


class SE(unittest.TestCase):
    def test_score_default(self):
        score(DATA, [1, 0, 0, 1])

    def test_score_scores(self):
        score(DATA, [1, 0, 0, 1], "scores")

    def test_score_score_lists(self):
        score(DATA, [1, 0, 0, 1], "score_lists")
