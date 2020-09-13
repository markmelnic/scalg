
import csv, unittest
import scalg

def read_csv(filename):

    if ".csv" not in filename:
        filename = str(filename) + ".csv"

    # read file contents
    with open(filename, mode="r", newline='') as csvFile:
        csvReader = csv.reader(csvFile)
        return list(csvReader)

class Scalg(unittest.TestCase):
    def test_scalg_default(self):
        data = read_csv('sample.csv')
        scalg.score(data, [1, 0, 0, 1])

    def test_scalg_scores(self):
        data = read_csv('sample.csv')
        scalg.score(data, [1, 0, 0, 1], 'scores')

    def test_scalg_score_lists(self):
        data = read_csv('sample.csv')
        scalg.score(data, [1, 0, 0, 1], 'score_lists')

    def test_score_columns(self):
        data = read_csv('sample.csv')
        scalg.score_columns(data, [1, 3], [1, 0, 0, 1])

    def test_score_columns_scores(self):
        data = read_csv('sample.csv')
        scalg.score_columns(data, [1, 3], [1, 0, 0, 1], 'scores')

    def test_score_columns_score_lists(self):
        data = read_csv('sample.csv')
        scalg.score_columns(data, [1, 3], [1, 0, 0, 1], 'score_lists')
