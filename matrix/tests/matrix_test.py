import unittest

from src.matrix import Matrix

class MatrixTest(unittest.TestCase):

    def setUp(self):
        pass
    # Tests

    def test_extract_row_from_one_number_matrix(self):
        matrix = Matrix("1")
        self.assertEqual(matrix.row(1), [1])

    # Test can extract a given row
    def test_extract_given_row(self):
        matrix = Matrix("1 2 5\n5 2 3\n 6 6 7")
        self.assertEqual([5, 3, 2], matrix.row(2))

    # Test can extract a given row where numbers have different number of digits
    # Example matrix:
    #
    # 1 2
    # 10 20


    # Test can extract row from non-square matrix
    # Example matrix:
    #
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # 8 7 6

    # Test can extract a column

    # Test can extract column from a one number matrix

    # Test can extract a column from non-square matrix
    # Example matrix:
    #
    # 1 2 3 4
    # 5 6 8 8
    # 9 8 7 6

    # Test can extract column when numbers have different number of digits
    # Example matrix:
    #
    # 89 1903 3
    # 18 3 1
    # 9 4 800



