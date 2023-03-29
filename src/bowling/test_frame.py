import unittest

from frame import Frame


class TestFrames(unittest.TestCase):

    def test_score_valid(self):
        frameTest = Frame(1, 2)
        self.assertEqual(frameTest.score(), 3)
    
    def test_score_invalid_more_than_10(self):
        frameTest = Frame(5, 6)
        with self.assertRaises(ValueError):
            frameTest.score()

    def test_score_invalid_negative(self):
        frameTest = Frame(5, -1)
        with self.assertRaises(ValueError):
            frameTest.score()

    def test_is_strike_true(self):
        frameTest = Frame(10, 0)
        self.assertEqual(frameTest.is_strike(), True)

    def test_is_strike_invalid(self):
        frameTest = Frame(10, 3)
        with self.assertRaises(ValueError):
            frameTest.score()

    def test_is_strike_false(self):
        frameTest = Frame(4, 6)
        self.assertEqual(frameTest.is_strike(), False)

    def test_is_spare_true(self):
        frameTest = Frame(4, 6)
        self.assertEqual(frameTest.is_spare(), True)

    def test_is_spare_false(self):
        frameTest = Frame(4, 5)
        self.assertEqual(frameTest.is_spare(), False)



if __name__ == '__main__':
    unittest.main()
