
import unittest
from scalg.scalg import score_columns

class Score_Columns(unittest.TestCase):
    data = [[2016 ,21999 ,62000  ,181],
                [2013 ,21540 ,89000  ,223],
                [2015 ,18900 ,100000 ,223],
                [2013 ,24200 ,115527 ,223],
                [2016 ,24990 ,47300  ,223]]

    def test_score_columns(self):
        score_columns(self.data, [1, 3], [1, 0, 0, 1])

    def test_score_columns_scores(self):
        score_columns(self.data, [1, 3], [1, 0, 0, 1], 'scores')

    def test_score_columns_score_lists(self):
        score_columns(self.data, [1, 3], [1, 0, 0, 1], 'score_lists')
