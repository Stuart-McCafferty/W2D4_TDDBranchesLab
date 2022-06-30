import unittest

from src.high_scores import *


class HighScoresTest(unittest.TestCase):
    
    def setUp(self):
        self.scoreList = [5, 1, 10, 8, 9]
    
    def test_return_latest_score(self):
        self.assertEqual(9, latest(self.scoreList))

    def test_return_max_score(self):
        self.assertEqual(10, personal_best(self.scoreList))

    def test_return_top_three_scores(self):
        self.assertEqual([10, 9, 8], personal_top_three(self.scoreList))

    def test_return_descending_list(self):
        self.assertEqual([10, 9 ,8 , 5, 1], descending_list(self.scoreList))

    def test_return_three_same_top_scores(self):
        self.tiedScores = [12, 10, 10, 6 ,10 , 7 , 8]
        self.assertEqual([12, 10, 10], personal_top_three(self.tiedScores))

    def test_return_top_three_when_less_than_three(self):
        self.twoScores = [2, 4]
        self.assertEqual([4, 2], personal_top_three(self.twoScores))
        
    def test_return_top_one_when_there_is_one(self):
        self.oneScore = [1]
        self.assertEqual([1], personal_top_three(self.oneScore))    
