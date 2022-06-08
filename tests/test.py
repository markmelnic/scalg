import os, sys, inspect, unittest, scalg

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

DATA = [
    [2016, 21999, 62000,  181],
    [2013, 21540, 89000,  223],
    [2015, 18900, 100000, 223],
    [2013, 24200, 115527, 223],
    [2016, 24990, 47300,  223],
]
WEIGHTS = [1, 0, 0, 1]

class SE(unittest.TestCase):
    def test_score_default(self):
        expected_result = [
            [2016, 21999, 62000, 181, 2.2756757812463335],
            [2013, 21540, 89000, 223, 1.9553074815952338],
            [2015, 18900, 100000, 223, 2.894245191297678],
            [2013, 24200, 115527, 223, 1.1297208538587848],
            [2016, 24990, 47300, 223, 3.0]
        ]

        result = scalg.score(DATA, WEIGHTS)
        assert result == expected_result

    def test_score_scores(self):
        expected_result = [
            2.2756757812463335,
            1.9553074815952338,
            2.894245191297678,
            1.1297208538587848,
            3.0
        ]

        result = scalg.score(DATA, WEIGHTS, get_scores=True)
        assert result == expected_result

    def test_score_score_lists(self):
        expected_result = [
            [1.0, 0.0, 0.6666666666666666, 0.0, 1.0],
            [0.49113300492610834, 0.5665024630541872, 1.0, 0.12972085385878485, 0.0],
            [0.7845427763202251, 0.38880501854104677, 0.22757852463101114, 0.0, 1.0],
            [0.0, 1.0, 1.0, 1.0, 1.0]
        ]

        result = scalg.score(DATA, WEIGHTS, get_score_lists=True)
        assert result == expected_result

class SEC(unittest.TestCase):
    def test_score_columns(self):
        expected_result = [
            [2016, 21999, 62000, 181, 1.4911330049261085],
            [2013, 21540, 89000, 223, 0.5665024630541872],
            [2015, 18900, 100000, 223, 1.6666666666666665],
            [2013, 24200, 115527, 223, 0.12972085385878485],
            [2016, 24990, 47300, 223, 1.0]
        ]

        result = scalg.score_columns(DATA, [0, 1], WEIGHTS)
        assert result == expected_result
