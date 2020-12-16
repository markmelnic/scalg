import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import unittest
import scalg

DATA = [
    [2016, 21999, 62000, 181],
    [2013, 21540, 89000, 223],
    [2015, 18900, 100000, 223],
    [2013, 24200, 115527, 223],
    [2016, 24990, 47300, 223],
]
WEIGHTS = [1, 0, 0, 1]

class SE(unittest.TestCase):
    def test_score_default(self, ):
        scalg.score(DATA, WEIGHTS)

    def test_score_scores(self, ):
        scalg.score(DATA, WEIGHTS, get_scores=True)

    def test_score_score_lists(self, ):
        scalg.score(DATA, WEIGHTS, get_score_lists=True)

class SEC(unittest.TestCase):
    def test_score_columns(self, ):
        req_result = [
                [2016, 21999, 62000, 181, 1.4911330049261085],
                [2013, 21540, 89000, 223, 0.5665024630541872],
                [2015, 18900, 100000, 223, 1.6666666666666665],
                [2013, 24200, 115527, 223, 0.12972085385878485],
                [2016, 24990, 47300, 223, 1.0]
            ]

        result = scalg.score_columns(DATA, [0, 1], WEIGHTS)
        assert result == req_result
