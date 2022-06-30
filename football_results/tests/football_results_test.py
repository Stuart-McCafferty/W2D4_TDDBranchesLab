import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    pass

    def setUp(self):
        self.draw = {
            "home_score": 1,
            "away_score": 1
        }
        self.homeWin = {
            "home_score": 5,
            "away_score": 1
        }
        self.awayWin = {
            "home_score": 1,
            "away_score": 6
        }

        self.scores = [self.draw, self.homeWin, self.awayWin]
    def test_draw(self):
        self.assertEqual("Draw, Score was 1 - 1", get_result(self.draw))
    
    def test_homeWin(self):
        self.assertEqual("Home wins, Score was 5 - 1", get_result(self.homeWin))
   
    def test_drawWin(self):
        self.assertEqual("Away wins, Score was 1 - 6", get_result(self.awayWin))
 

    # Test we get right list of result strings for a list of final score dictionaries. 
    def test_results(self):
        self.resultList = []
        self.resultList.append(get_result(self.draw))
        self.resultList.append(get_result(self.homeWin))
        self.resultList.append(get_result(self.awayWin))

        self.assertEqual(self.resultList, get_results(self.scores))

if __name__ == "__main__":
    unittest.main()
