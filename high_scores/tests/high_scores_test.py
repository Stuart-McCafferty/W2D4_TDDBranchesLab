import unittest

from src.high_scores import latest, personal_best, personal_top_three


class HighScoresTest(unittest.TestCase):
    
    def setUp(self):
        self.scoreList = [5, 1, 6, 8, 9]
    
    def test_return_latest_score(self):
        self.assertEqual(9, self.latest(self.scoreList))

    # Test latest score (the last thing in the list)

    # Test personal best (the highest score in the list)

    # Test top three from list of scores

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
